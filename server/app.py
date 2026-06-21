"""
FastAPI web server.

Serves webhook endpoints for WhatsApp (both Meta Cloud API and whatsapp-web.js)
and starts the APScheduler on startup.

Includes HMAC-SHA256 webhook signature verification for security.
"""

from __future__ import annotations

import asyncio
import hashlib
import hmac
from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI, Request, Response, Form
from fastapi.responses import HTMLResponse

from config.settings import META_VERIFY_TOKEN, META_APP_SECRET, WHATSAPP_MODE, PROJECT_ROOT
from phase2_whatsapp.bot import handle_incoming_message, _send
from phase2_whatsapp.meta_cloud_api import parse_webhook_message
from server.scheduler import run_startup_cycle, start_scheduler, shutdown_scheduler
from utils.logger import get_logger
from utils.sheets_client import (
    get_lead_by_phone,
    save_requirements,
    update_lead_field,
    save_package_recommendation,
    append_conversation,
)
from phase2_whatsapp.stage_manager import Stage
from phase2_whatsapp.conversation_engine import recommend_package
from phase2_whatsapp.templates import (
    PACKAGE_RECOMMENDATION,
    format_template,
    format_features_list,
)

logger = get_logger(__name__)


# ── Webhook signature verification ──────────────────────────────
def _verify_signature(payload: bytes, signature: str, secret: str) -> bool:
    """
    Verify the X-Hub-Signature-256 header from Meta's webhook.

    Handles both ``sha256=<hex>`` (standard Meta format) and raw hex.

    Args:
        payload: Raw request body bytes.
        signature: Value of X-Hub-Signature-256 header.
        secret: META_APP_SECRET from environment.

    Returns:
        True if signature is valid.
    """
    if not secret or not signature:
        logger.debug("Signature verification skipped: secret=%s, sig=%s",
                     bool(secret), bool(signature))
        return False

    expected = hmac.new(
        secret.encode("utf-8"), payload, hashlib.sha256
    ).hexdigest()

    # Handle both "sha256=<hex>" and raw hex formats
    if signature.startswith("sha256="):
        sig_hex = signature[7:]  # strip "sha256=" prefix
    else:
        sig_hex = signature

    is_valid = hmac.compare_digest(expected, sig_hex)
    if not is_valid:
        logger.debug(
            "Webhook signature mismatch: expected=%s, received=%s",
            expected[:16] + "...", sig_hex[:16] + "...",
        )
    return is_valid


# ── Lifespan (startup / shutdown) ────────────────────────────────
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Validate config, start scheduler on startup, shut down on exit."""
    logger.info("🚀 Starting AI Web Automation server...")

    # Validate environment variables at startup
    try:
        from utils.config_validator import validate_env
        validate_env(strict=False)  # Log warnings, don't crash
    except Exception as exc:
        logger.error("Config validation error: %s", exc)

    import os
    disable_startup = os.getenv("DISABLE_STARTUP_JOBS", "false").lower() == "true"

    if not disable_startup:
        start_scheduler()
        asyncio.create_task(asyncio.to_thread(run_startup_cycle))
    else:
        logger.info("⚠️ Startup automation and scheduler are disabled (DISABLE_STARTUP_JOBS=true)")

    yield

    if not disable_startup:
        shutdown_scheduler()
    logger.info("🛑 Server shut down.")


app = FastAPI(
    title="AI Web Automation",
    description="Lead scraping + WhatsApp bot automation server",
    version="1.0.0",
    lifespan=lifespan,
)


# ══════════════════════════════════════════════════════════════════
#  HEALTH CHECK (enhanced with quota reporting)
# ══════════════════════════════════════════════════════════════════

@app.get("/health")
async def health():
    """Return system health with quota usage stats."""
    from utils.gemini_client import get_quota_status

    gemini_quota = get_quota_status()

    return {
        "status": "ok",
        "whatsapp_mode": WHATSAPP_MODE,
        "gemini_quota": gemini_quota,
    }


@app.get("/health/detailed")
async def health_detailed():
    """Detailed health check for debugging (includes local storage, circuit breakers)."""
    from utils.gemini_client import get_quota_status
    from utils.local_storage import get_status as local_status
    from utils.circuit_breaker import gemini_breaker, whatsapp_breaker, sheets_breaker

    return {
        "status": "ok",
        "whatsapp_mode": WHATSAPP_MODE,
        "gemini_quota": get_quota_status(),
        "local_storage": local_status(),
        "circuit_breakers": {
            "gemini": gemini_breaker.get_status(),
            "whatsapp": whatsapp_breaker.get_status(),
            "sheets": sheets_breaker.get_status(),
        },
    }


# ══════════════════════════════════════════════════════════════════
#  META WHATSAPP CLOUD API WEBHOOK (Option A)
# ══════════════════════════════════════════════════════════════════

@app.get("/webhook/whatsapp")
async def verify_webhook(request: Request):
    """Handle Meta's webhook verification challenge."""
    params = request.query_params
    mode = params.get("hub.mode")
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")

    if mode == "subscribe" and token == META_VERIFY_TOKEN:
        logger.info("Meta webhook verified successfully.")
        return Response(content=challenge, media_type="text/plain")

    logger.warning("Meta webhook verification failed.")
    return Response(content="Forbidden", status_code=403)


@app.post("/webhook/whatsapp")
async def meta_webhook(request: Request):
    """Receive incoming messages from Meta WhatsApp Cloud API."""
    # Read raw body for signature verification
    raw_body = await request.body()

    # Verify HMAC-SHA256 signature if META_APP_SECRET is configured
    if META_APP_SECRET:
        signature = request.headers.get("X-Hub-Signature-256", "")
        if not _verify_signature(raw_body, signature, META_APP_SECRET):
            logger.warning("Meta webhook: invalid signature — rejecting payload.")
            return Response(content="Invalid signature", status_code=403)

    import json
    body = json.loads(raw_body)
    parsed = parse_webhook_message(body)

    if parsed and parsed.get("message"):
        # Process in background to respond quickly to Meta
        asyncio.create_task(
            handle_incoming_message(
                phone=parsed["phone"],
                message=parsed["message"],
                name=parsed.get("name", ""),
            )
        )

    return {"status": "ok"}


# ══════════════════════════════════════════════════════════════════
#  WHATSAPP-WEB.JS WEBHOOK (Option B)
# ══════════════════════════════════════════════════════════════════

@app.post("/webhook/incoming")
async def wjs_webhook(request: Request):
    """Receive incoming messages from the Node.js whatsapp-web.js server."""
    body: dict[str, Any] = await request.json()
    phone = body.get("phone", "")
    message = body.get("message", "")
    name = body.get("name", "")

    if phone and message:
        asyncio.create_task(
            handle_incoming_message(phone=phone, message=message, name=name)
        )

    return {"status": "ok"}


# ══════════════════════════════════════════════════════════════════
#  REQUIREMENTS WEB FORM ENDPOINTS
# ══════════════════════════════════════════════════════════════════

@app.get("/requirements-form/{phone}", response_class=HTMLResponse)
async def get_requirements_form(phone: str):
    """Serve the requirements HTML form template, prefilling lead's name if available."""
    lead = get_lead_by_phone(phone)
    default_name = lead.get("Name", "") if lead else ""
    
    template_path = PROJECT_ROOT / "server" / "templates" / "requirements_form.html"
    try:
        with open(template_path, "r", encoding="utf-8") as f:
            html_content = f.read()
    except FileNotFoundError:
        logger.error("Requirements form HTML template not found at %s", template_path)
        return HTMLResponse(content="<h1>Template Not Found</h1>", status_code=404)
        
    # Inject variables manually
    html_content = html_content.replace("{{ phone }}", phone).replace("{{ default_name }}", default_name)
    return HTMLResponse(content=html_content)


@app.post("/requirements-form/{phone}", response_class=HTMLResponse)
async def post_requirements_form(
    phone: str,
    business_name: str = Form(...),
    services_description: str = Form(...),
    pages_needed: str = Form(...),
    design_preferences: str = Form(""),
    budget: str = Form(""),
    feature_whatsapp: str | None = Form(None),
    feature_maps: str | None = Form(None),
    feature_payments: str | None = Form(None),
    feature_booking: str | None = Form(None),
    feature_gallery: str | None = Form(None),
    feature_seo: str | None = Form(None),
):
    """
    Process requirements form submission:
    1. Collect features checklist
    2. Save to Google Sheets
    3. Update stage in Sheets to Stage.PACKAGE
    4. Automatically calculate and send WhatsApp package recommendation pitch
    5. Show beautiful glassmorphism confirmation screen
    """
    # 1. Collect features list
    features_selected = []
    for feat in [feature_whatsapp, feature_maps, feature_payments, feature_booking, feature_gallery, feature_seo]:
        if feat:
            features_selected.append(feat)
    features_str = ", ".join(features_selected)

    # Prepare data dictionary
    data = {
        "business_name": business_name.strip(),
        "services_description": services_description.strip(),
        "pages_needed": pages_needed.strip(),
        "features": features_str,
        "budget": budget.strip(),
        "design_preferences": design_preferences.strip(),
    }

    try:
        # 2. Save requirements to Sheets
        save_requirements(phone, data)

        # 3. Update lead stage to PACKAGE
        update_lead_field(phone, "CurrentStage", Stage.PACKAGE.value)

        # 4. Recommend package based on collected requirements
        pkg = recommend_package(data)

        # Build reasoning explanation (customized to their requirements)
        reasons = []
        if "ecommerce" in features_str.lower() or "store" in pages_needed.lower():
            reasons.append("Aapki e-commerce/store and payment checkout requirements ke liye full store platform zaroori hai.")
        elif "booking" in features_str.lower() or "payment" in features_str.lower():
            reasons.append("Payments and scheduling integration features ke liye hamara Professional package best match hai.")
        elif "5" in pages_needed or "starter" in pages_needed.lower():
            reasons.append("5 pages or SEO setups ke liye hamara Starter package design kiya gaya hai.")
        elif "1" in pages_needed or "single" in pages_needed.lower():
            reasons.append("Aapki single landing page requirement ke liye hamara Single Page plan best hai.")
        else:
            reasons.append(f"Aapki requirements aur page needs ke liye hamara {pkg['name']} plan perfectly suitable hai.")

        package_reasoning = " ".join(reasons)

        pkg_text = format_template(
            PACKAGE_RECOMMENDATION,
            business_name=data["business_name"],
            package_name=pkg["name"],
            price_display=pkg["price_display"],
            renewal_price=pkg.get("renewal_price", "₹4,999"),
            delivery_time=pkg.get("delivery_time", "72 hours"),
            revision_count=pkg.get("revision_count", "3"),
            features_list=format_features_list(pkg["features"]),
            package_reasoning=package_reasoning,
        )

        # Save package recommendation to Sheets
        save_package_recommendation(phone, pkg["name"], pkg["price"])

        # Send recommendation to WhatsApp
        await _send(phone, pkg_text)
        append_conversation(phone, "out", pkg_text, Stage.PACKAGE.value)

    except Exception as exc:
        logger.error("Error processing form submission for %s: %s", phone, exc)
        from utils.telegram_alert import send_alert
        send_alert(f"Error in web requirements form processing for {phone}: {exc}", level="error")

    # Show confirmation page
    confirmation_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Requirements Received — Durvesh Developments</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-gradient: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
      --accent-color: #10b981;
      --card-bg: rgba(30, 41, 59, 0.7);
      --border-color: rgba(255, 255, 255, 0.1);
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
    }
    body {
      font-family: 'Outfit', sans-serif;
      background: var(--bg-gradient);
      min-height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      color: var(--text-main);
      padding: 20px;
    }
    .container {
      width: 100%;
      max-width: 500px;
      background: var(--card-bg);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid var(--border-color);
      border-radius: 24px;
      padding: 40px 30px;
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
      text-align: center;
      animation: scaleUp 0.4s ease-out;
    }
    .icon {
      font-size: 64px;
      margin-bottom: 20px;
    }
    @keyframes scaleUp {
      from { transform: scale(0.9); opacity: 0; }
      to { transform: scale(1); opacity: 1; }
    }
    h1 {
      font-size: 26px;
      font-weight: 600;
      margin-bottom: 12px;
    }
    p {
      font-size: 15px;
      color: var(--text-muted);
      line-height: 1.6;
      margin-bottom: 28px;
    }
    .btn {
      display: inline-block;
      background: var(--accent-color);
      color: white;
      text-decoration: none;
      padding: 14px 28px;
      border-radius: 12px;
      font-weight: 600;
      transition: all 0.3s ease;
      box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
    }
    .btn:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(16, 185, 129, 0.4);
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="icon">✅</div>
    <h1>Requirements Submitted!</h1>
    <p>Thank you for submitting your requirements. We have automatically analyzed your inputs and sent our recommended plan directly to your WhatsApp number.</p>
    <a href="https://wa.me/919137804316" class="btn">Open WhatsApp Chat</a>
  </div>
</body>
</html>
"""
    return HTMLResponse(content=confirmation_html)


# ══════════════════════════════════════════════════════════════════
#  ENTRY POINT
# ══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    import uvicorn
    from config.settings import SERVER_HOST, SERVER_PORT

    uvicorn.run(
        "server.app:app",
        host=SERVER_HOST,
        port=SERVER_PORT,
        reload=True,
        log_level="info",
    )
