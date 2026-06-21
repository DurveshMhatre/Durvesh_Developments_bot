"""
Entrypoint script for the AI Web Automation project.

Usage:
    python run.py                  Start the FastAPI server (normal mode)
    python run.py --scrape-test    Run a single test scrape (1 city, 1 type)
    python run.py --send-test      Send a test WhatsApp message to yourself
    python run.py --template-test  Send the welcome template (first cold message test)
    python run.py --outreach-test  Run one outreach cycle (template to Ready for Outreach leads)
"""

from __future__ import annotations

import argparse
import asyncio
import sys
from pathlib import Path

import io

# Ensure project root is on sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent))

# Safeguard Windows console from UnicodeEncodeErrors due to emojis
if sys.platform.startswith("win"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")



def main() -> None:
    parser = argparse.ArgumentParser(description="AI Web Automation Runner")
    parser.add_argument(
        "--scrape-test",
        action="store_true",
        help="Run a test scrape for the first city/type combo and print results.",
    )
    parser.add_argument(
        "--send-test",
        type=str,
        metavar="PHONE",
        help="Send a test WhatsApp message to the given phone number (e.g. 919876543210).",
    )
    parser.add_argument(
        "--template-test",
        type=str,
        metavar="PHONE",
        help="Send the approved welcome template to a phone number (e.g. 919876543210).",
    )
    parser.add_argument(
        "--followup",
        type=int,
        choices=[1, 2, 3],
        help="Use with --template-test to test follow-up templates (1, 2, or 3) instead of welcome.",
    )
    parser.add_argument(
        "--outreach-test",
        action="store_true",
        help="Run one cold-outreach cycle for leads with Status = Ready for Outreach.",
    )
    args = parser.parse_args()

    if args.scrape_test:
        _run_scrape_test()
    elif args.send_test:
        _run_send_test(args.send_test)
    elif args.template_test:
        _run_template_test(args.template_test, followup_num=args.followup)
    elif args.outreach_test:
        _run_outreach_test()
    else:
        _run_server()


def _run_server() -> None:
    """Start the FastAPI server."""
    import uvicorn
    from config.settings import SERVER_HOST, SERVER_PORT

    print(f"🚀 Starting server on {SERVER_HOST}:{SERVER_PORT}...")
    uvicorn.run(
        "server.app:app",
        host=SERVER_HOST,
        port=SERVER_PORT,
        reload=True,
        log_level="info",
    )


def _run_scrape_test() -> None:
    """Run a quick test scrape with the first city and business type."""
    from config.settings import BUSINESS_TYPES, TARGET_CITIES
    from phase1_leads.google_maps_scraper import scrape as scrape_gmaps
    from phase1_leads.lead_scorer import score_lead_dict
    from utils.sheets_client import append_leads

    city = TARGET_CITIES[0] if TARGET_CITIES else "Mumbai"
    btype = BUSINESS_TYPES[0] if BUSINESS_TYPES else "Restaurant"

    print(f"🔍 Test scraping Google Maps for: {btype} in {city}...")
    leads = scrape_gmaps(city, btype)

    print(f"\n📋 Found {len(leads)} leads without a website:\n")
    for i, lead in enumerate(leads, 1):
        score_lead_dict(lead)
        print(
            f"  {i}. {lead['name']}"
            f"  📱 {lead.get('phone', 'N/A')}"
            f"  ⭐ {lead.get('rating', 0)}"
            f"  💯 Score: {lead.get('score', '?')}"
            f"  [{lead.get('status', '')}]"
        )

    if not leads:
        print("  (No leads found — this is normal if Google blocked the request)")
    else:
        print("\n💾 Saving leads to Google Sheets...")
        try:
            saved_count = append_leads(leads)
            print(f"✅ Successfully saved {saved_count} leads to Google Sheets!")
            print(f"🔗 Check your sheet here: https://docs.google.com/spreadsheets/d/{__import__('config.settings', fromlist=['GOOGLE_SHEETS_ID']).GOOGLE_SHEETS_ID}")
        except Exception as e:
            print(f"❌ Failed to save to Sheets: {e}")

    print(f"\n✅ Scrape test complete. {len(leads)} leads found.")


def _run_template_test(phone: str, followup_num: int | None = None) -> None:
    """Send approved templates — welcome or follow-ups."""
    from config.settings import (
        META_TEMPLATE_LANGUAGE_CODE,
        META_WELCOME_TEMPLATE_NAME,
        META_FOLLOW_UP_1_TEMPLATE_NAME,
        META_FOLLOW_UP_2_TEMPLATE_NAME,
        META_FOLLOW_UP_3_TEMPLATE_NAME,
        WHATSAPP_MODE,
        AGENT_NAME,
        COMPANY_NAME,
        PORTFOLIO_URL,
    )

    if WHATSAPP_MODE != "meta_cloud":
        print("⚠️  --template-test only applies to WHATSAPP_MODE=meta_cloud")
        return

    from phase2_whatsapp.meta_cloud_api import send_template_message

    if followup_num is None:
        template_name = META_WELCOME_TEMPLATE_NAME
        if not template_name:
            print("❌ META_WELCOME_TEMPLATE_NAME is not set in config/.env")
            return
        components = [
            {
                "type": "body",
                "parameters": [
                    {"type": "text", "text": "Test Clinic"},
                    {"type": "text", "text": "45"},
                    {"type": "text", "text": "4.8"},
                    {"type": "text", "text": "Dental Clinic"},
                    {"type": "text", "text": AGENT_NAME},
                    {"type": "text", "text": COMPANY_NAME},
                    {"type": "text", "text": "Thane"},
                ]
            }
        ]
    elif followup_num == 1:
        template_name = META_FOLLOW_UP_1_TEMPLATE_NAME
        if not template_name:
            print("❌ META_FOLLOW_UP_1_TEMPLATE_NAME is not set in config/.env")
            return
        components = [
            {
                "type": "body",
                "parameters": [
                    {"type": "text", "text": "Test Clinic"},
                    {"type": "text", "text": "Thane"},
                    {"type": "text", "text": "2,999"},
                    {"type": "text", "text": "48 ghante"},
                    {"type": "text", "text": "Sunday midnight"},
                ]
            }
        ]
    elif followup_num == 2:
        template_name = META_FOLLOW_UP_2_TEMPLATE_NAME
        if not template_name:
            print("❌ META_FOLLOW_UP_2_TEMPLATE_NAME is not set in config/.env")
            return
        components = [
            {
                "type": "body",
                "parameters": [
                    {"type": "text", "text": "Test Clinic"},
                    {"type": "text", "text": "500"},
                    {"type": "text", "text": "clinics in Thane"},
                    {"type": "text", "text": "150"},
                    {"type": "text", "text": AGENT_NAME},
                    {"type": "text", "text": COMPANY_NAME},
                ]
            }
        ]
    elif followup_num == 3:
        template_name = META_FOLLOW_UP_3_TEMPLATE_NAME
        if not template_name:
            print("❌ META_FOLLOW_UP_3_TEMPLATE_NAME is not set in config/.env")
            return
        components = [
            {
                "type": "body",
                "parameters": [
                    {"type": "text", "text": "Test Clinic"},
                ]
            }
        ]
    else:
        print("❌ Invalid follow-up number.")
        return

    print(
        f"📤 Sending template '{template_name}' "
        f"({META_TEMPLATE_LANGUAGE_CODE}) to {phone}..."
    )
    
    result = asyncio.run(
        send_template_message(
            phone,
            template_name=template_name,
            language_code=META_TEMPLATE_LANGUAGE_CODE,
            components=components,
        )
    )
    print(f"✅ Template sent! API response: {result}")


def _run_outreach_test() -> None:
    """Run one outreach cycle (cold messages + follow-ups)."""
    from phase2_whatsapp.outreach_scheduler import run_outreach_cycle
    from utils.sheets_client import get_leads_by_status

    ready = get_leads_by_status("Ready for Outreach")
    print(f"📋 Leads with Status = 'Ready for Outreach': {len(ready)}")
    if not ready:
        print(
            "⚠️  No leads to message. In Google Sheets, set one test lead:\n"
            "   • PhoneType = mobile\n"
            "   • Status = Ready for Outreach\n"
            "   • Phone = your WhatsApp number (e.g. 919876543210)"
        )
        return

    print("📤 Running outreach cycle...")
    run_outreach_cycle()
    print("✅ Outreach cycle finished. Check Google Sheets for status updates.")


def _run_send_test(phone: str) -> None:
    """Send a test message via WhatsApp to verify the API setup."""
    from config.settings import WHATSAPP_MODE

    test_message = (
        "👋 This is a test message from AI Web Automation.\n"
        "If you received this, your WhatsApp setup is working! ✅"
    )

    print(f"📤 Sending test message to {phone} via {WHATSAPP_MODE}...")

    if WHATSAPP_MODE == "meta_cloud":
        from phase2_whatsapp.meta_cloud_api import send_text_message
        result = asyncio.run(send_text_message(phone, test_message))
        print(f"✅ Message sent! API response: {result}")
    else:
        from phase2_whatsapp.whatsapp_web_js.bridge import send_message
        result = asyncio.run(send_message(phone, test_message))
        print(f"✅ Message sent! Response: {result}")


if __name__ == "__main__":
    main()
