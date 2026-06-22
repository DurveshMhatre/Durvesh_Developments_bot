from __future__ import annotations

import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from config.settings import (
    BUSINESS_TYPES,
    SCRAPE_SCHEDULE_HOUR,
    TARGET_CITIES,
)
from utils.logger import get_logger
from utils.telegram_alert import send_alert

logger = get_logger(__name__)

_scheduler: BackgroundScheduler | None = None


# ══════════════════════════════════════════════════════════════════
#  JOB FUNCTIONS
# ══════════════════════════════════════════════════════════════════

def _run_daily_scrape():
    """Daily scraping job: Google Maps + JustDial → score → dedup → save."""
    logger.info("═══ Daily scrape job started ═══")

    from phase1_leads.google_maps_scraper import scrape as scrape_gmaps
    from phase1_leads.justdial_scraper import scrape as scrape_justdial
    from phase1_leads.lead_scorer import score_lead_dict
    from phase1_leads.dedup import deduplicate
    from utils.sheets_client import (
        append_leads,
        get_all_leads,
        get_active_scrape_targets,
        update_scrape_target_last_scraped,
        update_scrape_target_status,
    )
    from config.settings import SKIP_PLAYWRIGHT_SCRAPING

    all_new_leads = []

    # Try fetching dynamic targets from Google Sheets first
    targets = get_active_scrape_targets()

    if targets:
        logger.info("Loaded %d active scrape targets from Google Sheet ScrapeTargets.", len(targets))
        for t in targets:
            city = t["city"]
            btype = t["category"]
            row = t["row"]
            if not city or not btype:
                continue

            logger.info("Running scrape for: %s in %s...", btype, city)
            scrape_success = False

            if not SKIP_PLAYWRIGHT_SCRAPING:
                try:
                    # Google Maps
                    gmaps_leads = scrape_gmaps(city, btype)
                    all_new_leads.extend(gmaps_leads)
                    scrape_success = True
                except Exception as exc:
                    logger.error("Google Maps scraper error (%s/%s): %s", city, btype, exc)
            else:
                logger.info("Skipping Google Maps Playwright scraping (SKIP_PLAYWRIGHT_SCRAPING is True)")

            try:
                # JustDial
                justdial_leads = scrape_justdial(city, btype)
                all_new_leads.extend(justdial_leads)
                scrape_success = True
            except Exception as exc:
                logger.error("JustDial scraper error (%s/%s): %s", city, btype, exc)

            # Update last scraped timestamp and status in Sheets
            update_scrape_target_last_scraped(row)
            if scrape_success:
                update_scrape_target_status(row, "Completed")
            else:
                update_scrape_target_status(row, "Failed")
    else:
        # Fallback to .env values if Google Sheets has no active targets
        logger.info("No active scrape targets in Google Sheets. Using config values: TARGET_CITIES=%s, BUSINESS_TYPES=%s", TARGET_CITIES, BUSINESS_TYPES)
        for city in TARGET_CITIES:
            for btype in BUSINESS_TYPES:
                if not SKIP_PLAYWRIGHT_SCRAPING:
                    try:
                        # Google Maps
                        gmaps_leads = scrape_gmaps(city, btype)
                        all_new_leads.extend(gmaps_leads)
                    except Exception as exc:
                        logger.error("Google Maps scraper error (%s/%s): %s", city, btype, exc)
                else:
                    logger.info("Skipping Google Maps Playwright scraping (SKIP_PLAYWRIGHT_SCRAPING is True)")

                try:
                    # JustDial
                    justdial_leads = scrape_justdial(city, btype)
                    all_new_leads.extend(justdial_leads)
                except Exception as exc:
                    logger.error("JustDial scraper error (%s/%s): %s", city, btype, exc)

    # Score all leads
    for lead in all_new_leads:
        score_lead_dict(lead)

    # Dedup against existing data using fuzzy matching module
    existing = get_all_leads()
    unique = deduplicate(all_new_leads, existing)

    # Save to Sheets
    saved = append_leads(unique)

    logger.info(
        "═══ Daily scrape complete: %d scraped, %d unique, %d saved ═══",
        len(all_new_leads), len(unique), saved,
    )

    send_alert(
        f"🔍 <b>Daily Scrape Complete</b>\n\n"
        f"  • Total scraped: {len(all_new_leads)}\n"
        f"  • After dedup: {len(unique)}\n"
        f"  • Saved to Sheets: {saved}",
        level="info",
    )


def _run_outreach_cycle():
    """Outreach job: send cold messages and follow-ups."""
    logger.info("═══ Outreach cycle started ═══")
    from phase2_whatsapp.outreach_scheduler import run_outreach_cycle
    run_outreach_cycle()


def run_startup_cycle() -> None:
    """
    Run one immediate scrape pass when the server starts.

    This lets the system fetch fresh leads without waiting for the
    first scheduled cron window.
    """
    logger.info("═══ Startup automation cycle started ═══")

    try:
        from utils.sheets_client import normalize_existing_leads
        normalize_existing_leads()
    except Exception as exc:
        logger.error("Startup lead-normalization failed: %s", exc)

    try:
        _run_daily_scrape()
    except Exception as exc:
        logger.error("Startup scrape cycle failed: %s", exc)

    try:
        _run_outreach_cycle()
    except Exception as exc:
        logger.error("Startup outreach cycle failed: %s", exc)

    logger.info("═══ Startup automation cycle finished ═══")


def _run_daily_summary():
    """Send a daily summary to the admin via Telegram."""
    logger.info("Sending daily summary...")
    from utils.sheets_client import get_all_leads
    from phase2_whatsapp.templates import ADMIN_DAILY_SUMMARY, format_template

    leads = get_all_leads()
    today_leads = [l for l in leads if str(l.get("DateAdded", "")).startswith(
        datetime.date.today().isoformat()
    )]

    msg = format_template(
        ADMIN_DAILY_SUMMARY,
        leads_scraped=len(today_leads),
        messages_sent=sum(1 for l in leads if l.get("Status") in (
            "First Message Sent", "Follow-Up 1 Sent", "Follow-Up 2 Sent"
        )),
        replies_received=sum(1 for l in leads if l.get("Status") == "In Conversation"),
        interested_count=sum(1 for l in leads if l.get("Status") == "Interested - Handoff"),
        not_interested_count=sum(1 for l in leads if l.get("Status") == "Not Interested"),
    )
    send_alert(msg, level="info")


# ══════════════════════════════════════════════════════════════════
#  SCHEDULER CONTROL
# ══════════════════════════════════════════════════════════════════

def start_scheduler() -> None:
    """Create and start all scheduled jobs."""
    global _scheduler

    _scheduler = BackgroundScheduler()

    # Daily scrape at configured hour (default 10 AM)
    _scheduler.add_job(
        _run_daily_scrape,
        trigger=CronTrigger(hour=SCRAPE_SCHEDULE_HOUR, minute=0),
        id="daily_scrape",
        name="Daily Lead Scraper",
        replace_existing=True,
    )

    # Outreach cycle at 10 AM and 11 AM
    _scheduler.add_job(
        _run_outreach_cycle,
        trigger=CronTrigger(hour="10,11", minute=0),
        id="outreach_cycle",
        name="Cold Outreach & Follow-ups",
        replace_existing=True,
    )

    # Daily summary at 9 PM
    _scheduler.add_job(
        _run_daily_summary,
        trigger=CronTrigger(hour=21, minute=0),
        id="daily_summary",
        name="Daily Telegram Summary",
        replace_existing=True,
    )

    _scheduler.start()
    logger.info(
        "Scheduler started with jobs: daily_scrape (@ %d:00), "
        "outreach_cycle (@ 10:00 & 11:00), daily_summary (@ 21:00)",
        SCRAPE_SCHEDULE_HOUR,
    )



def shutdown_scheduler() -> None:
    """Gracefully shut down the scheduler."""
    global _scheduler
    if _scheduler and _scheduler.running:
        _scheduler.shutdown(wait=False)
        logger.info("Scheduler shut down.")
