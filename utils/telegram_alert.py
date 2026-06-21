"""
WhatsApp-based admin alerts and notifications.

Replaces the previous Telegram alert utility to route alerts to the administrator's WhatsApp number.
"""

from __future__ import annotations

import re
import httpx

from config.settings import (
    ADMIN_PHONE_NUMBER,
    WHATSAPP_MODE,
    WHATSAPP_WEB_JS_URL,
)
from utils.logger import get_logger

logger = get_logger(__name__)


def _html_to_whatsapp(html_text: str) -> str:
    """
    Translate basic HTML formatting tags to WhatsApp markdown.
    
    WhatsApp supports:
      - *bold*
      - _italic_
      - ~strikethrough~
      - ```monospace```
    """
    text = html_text
    # Replace line breaks
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.IGNORECASE)
    # Replace bold tags
    text = re.sub(r"</?(b|strong)>", "*", text, flags=re.IGNORECASE)
    # Replace italic tags
    text = re.sub(r"</?(i|em)>", "_", text, flags=re.IGNORECASE)
    # Replace code/pre tags
    text = re.sub(r"</?pre>", "```", text, flags=re.IGNORECASE)
    text = re.sub(r"</?code>", "`", text, flags=re.IGNORECASE)
    # Strip any remaining HTML tags (like <a>, <div> etc)
    text = re.sub(r"<[^>]+>", "", text)
    # Unescape common HTML entities
    text = text.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
    return text.strip()


async def _send_async(text: str) -> bool:
    """Send an alert asynchronously to the admin's WhatsApp number."""
    if not ADMIN_PHONE_NUMBER:
        logger.warning("ADMIN_PHONE_NUMBER not configured — skipping WhatsApp alert.")
        return False

    logger.debug("Sending async WhatsApp alert to admin...")
    wa_text = _html_to_whatsapp(text)

    try:
        if WHATSAPP_MODE == "meta_cloud":
            from phase2_whatsapp.meta_cloud_api import send_text_message
            await send_text_message(ADMIN_PHONE_NUMBER, wa_text)
        else:
            url = f"{WHATSAPP_WEB_JS_URL}/send"
            payload = {"phone": ADMIN_PHONE_NUMBER, "message": wa_text}
            async with httpx.AsyncClient(timeout=15) as client:
                resp = await client.post(url, json=payload)
                resp.raise_for_status()
        logger.debug("WhatsApp admin alert sent successfully.")
        return True
    except Exception as exc:
        logger.error("Failed to send async WhatsApp admin alert: %s", exc)
        return False


def send_sync(text: str) -> bool:
    """Send an alert synchronously (blocking) to the admin's WhatsApp number."""
    if not ADMIN_PHONE_NUMBER:
        logger.warning("ADMIN_PHONE_NUMBER not configured — skipping WhatsApp alert.")
        return False

    logger.debug("Sending sync WhatsApp alert to admin...")
    wa_text = _html_to_whatsapp(text)

    try:
        if WHATSAPP_MODE == "meta_cloud":
            from phase2_whatsapp.meta_cloud_api import send_text_message_sync
            send_text_message_sync(ADMIN_PHONE_NUMBER, wa_text)
        else:
            url = f"{WHATSAPP_WEB_JS_URL}/send"
            payload = {"phone": ADMIN_PHONE_NUMBER, "message": wa_text}
            with httpx.Client(timeout=15) as client:
                resp = client.post(url, json=payload)
                resp.raise_for_status()
        logger.debug("WhatsApp admin alert sent successfully.")
        return True
    except Exception as exc:
        logger.error("Failed to send sync WhatsApp admin alert: %s", exc)
        return False


# ══════════════════════════════════════════════════════════════════
#  PUBLIC API
# ══════════════════════════════════════════════════════════════════

def send_alert(message: str, level: str = "info") -> bool:
    """
    Send an alert to the admin's WhatsApp (synchronous).

    Args:
        message: Alert body text (HTML allowed).
        level: ``"info"`` | ``"warning"`` | ``"error"`` | ``"critical"``

    Returns:
        ``True`` if the message was sent successfully.
    """
    emoji_map = {
        "info": "ℹ️",
        "warning": "⚠️",
        "error": "🔴",
        "critical": "🚨",
    }
    emoji = emoji_map.get(level, "ℹ️")
    formatted = f"{emoji} *[{level.upper()}]*\n\n{message}"
    return send_sync(formatted)


async def send_alert_async(message: str, level: str = "info") -> bool:
    """Async version of :func:`send_alert`."""
    emoji_map = {
        "info": "ℹ️",
        "warning": "⚠️",
        "error": "🔴",
        "critical": "🚨",
    }
    emoji = emoji_map.get(level, "ℹ️")
    formatted = f"{emoji} *[{level.upper()}]*\n\n{message}"
    return await _send_async(formatted)
