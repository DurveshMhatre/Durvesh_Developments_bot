"""
Gemini-powered AI conversation handler.

Builds context-aware prompts including conversation history, stage info,
and business context, then extracts structured JSON responses.
"""

from __future__ import annotations

from typing import Any

from config.settings import (
    AGENT_NAME,
    COMPANY_NAME,
    PACKAGES,
    PORTFOLIO_URL,
    UPI_ID,
    AUTOMATION_PACKAGES,
    ADDITIONAL_SERVICES,
)
from phase2_whatsapp.stage_manager import Stage, get_missing_fields
from utils.gemini_client import generate_json
from utils.logger import get_logger
from utils.telegram_alert import send_alert

logger = get_logger(__name__)

# ══════════════════════════════════════════════════════════════════
#  SYSTEM PROMPTS
# ══════════════════════════════════════════════════════════════════

_BASE_SYSTEM_PROMPT = """\
You are {agent_name}, a friendly and professional sales agent for {company_name}, \
a website development company. You are chatting with a potential client via WhatsApp.

COMPANY INFO:
- Company: {company_name}
- Portfolio: {portfolio_url}
- Payment: UPI ({upi_id})
- Packages:
{packages_text}

COMMUNICATION STYLE:
- Be warm, friendly, and professional
- Use Hindi/Hinglish naturally — match the client's language
- Use emojis sparingly (1-2 per message)
- Keep messages concise (max 3-4 short paragraphs)
- NEVER be pushy. If client says no, accept gracefully
- Sound like a real person, NOT a bot

CURRENT STAGE: {current_stage}
{stage_instructions}

CONVERSATION HISTORY (most recent):
{history_text}

COLLECTED DATA SO FAR:
{collected_data_text}

RESPOND STRICTLY AS JSON with this schema:
{{
  "response": "Your WhatsApp reply message text here",
  "data_collected": {{"field_name": "value", ...}},
  "should_advance_stage": true/false,
  "sentiment": "positive" | "neutral" | "negative",
  "is_not_interested": true/false
}}

RULES:
- "response" must be a natural, conversational reply
- "data_collected" should contain any NEW information the client just shared \
  (business_name, services_description, pages_needed, features, budget, design_preferences)
- "should_advance_stage" = true ONLY when all required info for current stage is collected
- "is_not_interested" = true ONLY if the client clearly declines / refuses
- If the client asks irrelevant questions, gently steer back to the topic
"""

_STAGE_INSTRUCTIONS = {
    Stage.WELCOME: (
        "GOAL: The client just received our intro message. Gauge their interest.\n"
        "- If they seem interested, express excitement and prepare to send the requirements form link.\n"
        "- If they ask what we do, explain briefly with examples.\n"
        "- Set should_advance_stage=true when the client shows interest and is willing to talk."
    ),
    Stage.REQUIREMENTS: (
        "GOAL: Guide the client to fill out the web requirements form.\n"
        "- The link to the form is: {form_link}\n"
        "- If they ask questions (e.g. about packages, prices, features, or portfolio), answer them fully, naturally, and politely, and then gently remind them to fill out the form: {form_link} to proceed with their custom quote.\n"
        "- If they share requirements directly in the chat, note them in data_collected and answer normally, but ask them to submit the form at {form_link} to complete the submission.\n"
        "- If they reply 'DONE' (or state they filled it) AND the collected data below contains at least business_name, services_description, and pages_needed, set should_advance_stage=true.\n"
        "- If they say they filled it/DONE but the collected data is still empty, politely explain that we haven't received their form inputs yet, and ask them to make sure they click 'Submit' on the form."
    ),
    Stage.PACKAGE: (
        "GOAL: We have recommended a package based on their form inputs.\n"
        "- Answer any questions they have about the package, pricing (including renewal pricing, automation package prices, and additional services), features, or timeline.\n"
        "- The final goal is to prompt/guide the client to get on a Google Meet or phone call to finalize slot bookings and answer any remaining questions.\n"
        "- If the client agrees to get on a Google Meet/phone call (or says 'Haan, call/meet karo', 'Call me', 'Let\'s schedule a call', etc.), set should_advance_stage=true."
    ),
    Stage.CALL_SCHEDULE: (
        "GOAL: The client has agreed to a call. Schedule a specific time.\n"
        "- Ask the client for their preferred date and time for a Google Meet or phone call.\n"
        "- Suggest available slots like 'Kal 11am ya 3pm, kab free hain?'\n"
        "- Be flexible and accommodate their schedule.\n"
        "- Once they confirm a specific time/date (or say 'abhi call karo', 'kal theek hai', etc.), set should_advance_stage=true.\n"
        "- Capture any scheduling info in data_collected (e.g. 'call_time': 'Tomorrow 3pm')."
    ),
    Stage.CONTRACT: (
        "GOAL: Share contract terms and get agreement from the client.\n"
        "- The contract terms have been sent in a separate message. Your job is to answer any questions about the terms.\n"
        "- Key terms: 50% advance payment, balance after website approval, timeline as per package, revision rounds as per package, written agreement.\n"
        "- If the client agrees to the terms (says 'Theek hai', 'Done', 'Agree', 'Accept', 'Haan chalega'), set should_advance_stage=true.\n"
        "- If they have concerns, address them professionally. If they want changes, explain standard policy."
    ),
    Stage.PAYMENT: (
        "GOAL: Collect 50% advance payment from the client.\n"
        "- Payment details have been sent. Your job is to assist with any payment questions.\n"
        "- UPI ID: {upi_id}\n"
        "- Accepted: GPay, PhonePe, Paytm, Bank Transfer\n"
        "- If the client says they have paid (e.g. 'Payment done', 'Paid', 'Bhej diya', 'Screenshot bheja'), set should_advance_stage=true.\n"
        "- Remind them to share a payment screenshot for confirmation.\n"
        "- Be patient — don't rush. Let them pay at their convenience."
    ),
    Stage.DEMO: (
        "GOAL: The client has paid. A demo website is being prepared / has been shared.\n"
        "- Reassure the client that work has started and they will receive a demo preview soon.\n"
        "- If they ask about timeline, refer to the package delivery time.\n"
        "- If the client approves the demo (says 'APPROVED', 'Approved', 'Perfect', 'Bahut accha', 'Go live'), set should_advance_stage=true.\n"
        "- If they want changes, note down the requested changes in data_collected and acknowledge.\n"
        "- Do NOT set should_advance_stage=true until they explicitly approve."
    ),
}


def _format_packages() -> str:
    """Format package info for the system prompt."""
    lines: list[str] = ["WEBSITE DEVELOPMENT PACKAGES:"]
    for pkg in PACKAGES.values():
        features = ", ".join(pkg["features"])
        lines.append(
            f"  • {pkg['name']}: {pkg['price_display']} "
            f"(Renewal: {pkg['renewal_price']}/year, Delivery: {pkg['delivery_time']}, Revisions: {pkg['revision_count']}) "
            f"— {features}"
        )
    
    lines.append("\nBUSINESS AUTOMATION PACKAGES:")
    for pkg in AUTOMATION_PACKAGES.values():
        features = ", ".join(pkg["features"])
        lines.append(f"  • {pkg['name']}: {pkg['price_display']} (Delivery: {pkg['delivery_time']}) — {features}")
        
    lines.append("\nADDITIONAL SERVICES:")
    for svc, details in ADDITIONAL_SERVICES.items():
        lines.append(f"  • {svc}: {details}")
        
    return "\n".join(lines)


def _format_history(history: list[dict[str, Any]]) -> str:
    """Format conversation history for the system prompt."""
    if not history:
        return "(No previous messages)"

    lines: list[str] = []
    for msg in history:
        direction = msg.get("Direction", msg.get("direction", ""))
        text = msg.get("Message", msg.get("message", ""))
        speaker = "CLIENT" if direction == "in" else "YOU"
        lines.append(f"[{speaker}]: {text}")
    return "\n".join(lines)


def _format_collected_data(data: dict[str, Any]) -> str:
    """Format collected data for the system prompt."""
    if not data:
        return "(Nothing collected yet)"
    lines = [f"  • {k}: {v}" for k, v in data.items() if v]
    return "\n".join(lines) if lines else "(Nothing collected yet)"


# ══════════════════════════════════════════════════════════════════
#  PUBLIC API
# ══════════════════════════════════════════════════════════════════

def process_message(
    incoming_message: str,
    stage: Stage,
    history: list[dict[str, Any]],
    collected_data: dict[str, Any] | None = None,
    phone: str = "",
) -> dict[str, Any]:
    """
    Process an incoming WhatsApp message using Gemini AI.

    Args:
        incoming_message: The client's message text.
        stage: Current conversation stage.
        history: Last N messages from the conversation history.
        collected_data: Previously collected requirement fields.
        phone: Client's phone number.

    Returns:
        Dict with keys: ``response``, ``data_collected``,
        "should_advance_stage", "sentiment", "is_not_interested".
    """
    collected_data = collected_data or {}

    from config.settings import SERVER_PUBLIC_URL
    form_link = f"{SERVER_PUBLIC_URL}/requirements-form/{phone}" if phone else f"{SERVER_PUBLIC_URL}/requirements-form"

    # Build stage-specific instructions and format the form_link into them
    stage_instr = _STAGE_INSTRUCTIONS.get(stage, "").format(
        form_link=form_link,
        upi_id=UPI_ID,
    )


    system_prompt = _BASE_SYSTEM_PROMPT.format(
        agent_name=AGENT_NAME,
        company_name=COMPANY_NAME,
        portfolio_url=PORTFOLIO_URL,
        upi_id=UPI_ID,
        packages_text=_format_packages(),
        current_stage=stage.value,
        stage_instructions=stage_instr,
        history_text=_format_history(history),
        collected_data_text=_format_collected_data(collected_data),
    )

    try:
        result = generate_json(system_prompt, incoming_message)

        # Handle parse errors
        if result.get("parse_error"):
            logger.warning("Gemini returned unparseable response — using fallback.")
            return _fallback_response(stage)

        # Validate required keys
        if "response" not in result:
            logger.warning("Gemini response missing 'response' key — using fallback.")
            return _fallback_response(stage)

        # Ensure defaults
        result.setdefault("data_collected", {})
        result.setdefault("should_advance_stage", False)
        result.setdefault("sentiment", "neutral")
        result.setdefault("is_not_interested", False)

        logger.info(
            "Gemini response: stage=%s sentiment=%s advance=%s",
            stage.value,
            result.get("sentiment"),
            result.get("should_advance_stage"),
        )
        return result

    except Exception as exc:
        logger.error("Conversation engine failed: %s", exc)
        send_alert(
            f"Conversation engine error:\n<pre>{exc}</pre>\n\n"
            f"Stage: {stage.value}\nMessage: {str(incoming_message)[:200]}",
            level="error",
        )
        return _fallback_response(stage)


def _fallback_response(stage: Stage) -> dict[str, Any]:
    """Generate a safe fallback response when Gemini fails."""
    fallbacks = {
        Stage.WELCOME: (
            "Namaste! 🙏 Main abhi thoda busy hoon, lekin jaldi reply karungi. "
            "Kya aap mujhe apna business ka naam bata sakte hain?"
        ),
        Stage.REQUIREMENTS: (
            "Dhanyawad! 😊 Mujhe thoda aur detail chahiye aapke business ke baare mein. "
            "Kya aap bata sakte hain ki aap kya services offer karte hain?"
        ),
        Stage.PACKAGE: (
            "Bahut accha! 😊 Agar aapko koi sawal hai package ke baare mein, "
            "to zaroor puchiye. Main yahan help karne ke liye hoon!"
        ),
        Stage.CALL_SCHEDULE: (
            "Call schedule karne ke liye — aap kal ya parson kab free hain? "
            "Main time fix karta hoon! 📞"
        ),
        Stage.CONTRACT: (
            "Contract ke baare mein koi bhi sawal ho to puchiye! 📝 "
            "Main sab clear kar dunga."
        ),
        Stage.PAYMENT: (
            "Payment ke liye UPI ID bhej diya hai. 💳 "
            "Koi bhi issue ho to batao — main help karunga!"
        ),
        Stage.DEMO: (
            "Aapki website ka demo jaldi ready hoga! 🎨 "
            "Thoda patience rakhiye — bahut accha banega!"
        ),
    }
    return {
        "response": fallbacks.get(stage, "Dhanyawad! Main jaldi reply karungi. 😊"),
        "data_collected": {},
        "should_advance_stage": False,
        "sentiment": "neutral",
        "is_not_interested": False,
    }


def recommend_package(collected_data: dict[str, Any]) -> dict[str, Any]:
    """
    Choose the best package based on collected requirements.

    Returns the package dict from ``PACKAGES``.
    """
    pages = str(collected_data.get("pages_needed", "")).lower()
    features = str(collected_data.get("features", "")).lower()
    budget = str(collected_data.get("budget", "")).lower()

    # Simple rule-based recommendation
    if any(kw in features for kw in ["ecommerce", "e-commerce", "online store", "shop", "cart"]):
        return PACKAGES["E-Commerce"]
    if any(kw in features for kw in ["booking", "admin", "dashboard", "payment", "razorpay"]):
        return PACKAGES["Professional"]

    # Check page count
    try:
        page_count = int("".join(c for c in pages if c.isdigit()) or "0")
    except ValueError:
        page_count = 0

    if page_count > 5:
        return PACKAGES["Professional"]
    if page_count > 1:
        return PACKAGES["Starter"]
    if "single" in pages or "one" in pages or page_count == 1:
        return PACKAGES["Single Page"]

    # Check budget hints
    if any(kw in budget for kw in ["low", "kam", "sasta", "cheap", "basic"]):
        return PACKAGES["Starter"]
    if any(kw in budget for kw in ["premium", "best", "full", "unlimited"]):
        return PACKAGES["Professional"]

    # Default to Professional (best seller)
    return PACKAGES["Professional"]
