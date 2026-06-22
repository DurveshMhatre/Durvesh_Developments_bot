"""
Central configuration module.

Loads all settings from environment variables (.env file) with sensible defaults.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# ── Paths ─────────────────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIG_DIR = PROJECT_ROOT / "config"
CREDENTIALS_DIR = CONFIG_DIR / "credentials"
LOGS_DIR = PROJECT_ROOT / "logs"

# Ensure directories exist
CREDENTIALS_DIR.mkdir(parents=True, exist_ok=True)
LOGS_DIR.mkdir(parents=True, exist_ok=True)

# Load .env — check config/ first (where the file lives), then project root
_env_config = CONFIG_DIR / ".env"
_env_root = PROJECT_ROOT / ".env"
if _env_config.exists():
    load_dotenv(_env_config)
elif _env_root.exists():
    load_dotenv(_env_root)

# ── AI & Data Config ──────────────────────────────────────────────
GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")
GOOGLE_SHEETS_ID: str = os.getenv("GOOGLE_SHEETS_ID", "")

# OAuth credentials paths
OAUTH_CREDENTIALS_FILE: Path = CREDENTIALS_DIR / "oauth_credentials.json"
OAUTH_TOKEN_FILE: Path = CREDENTIALS_DIR / "token.json"

# ── WhatsApp Mode ─────────────────────────────────────────────────
WHATSAPP_MODE: str = os.getenv("WHATSAPP_MODE", "meta_cloud")  # "meta_cloud" or "whatsapp_web_js"

# ── Meta WhatsApp Cloud API (Option A) ────────────────────────────
META_PHONE_NUMBER_ID: str = os.getenv("META_PHONE_NUMBER_ID", "")
META_ACCESS_TOKEN: str = os.getenv("META_ACCESS_TOKEN", "")
META_VERIFY_TOKEN: str = os.getenv("META_VERIFY_TOKEN", "your_custom_verify_token")
META_APP_SECRET: str = os.getenv("META_APP_SECRET", "")
META_WELCOME_TEMPLATE_NAME: str = os.getenv("META_WELCOME_TEMPLATE_NAME", "welcome_message_a")
META_FOLLOW_UP_1_TEMPLATE_NAME: str = os.getenv("META_FOLLOW_UP_1_TEMPLATE_NAME", "")
META_FOLLOW_UP_2_TEMPLATE_NAME: str = os.getenv("META_FOLLOW_UP_2_TEMPLATE_NAME", "")
META_FOLLOW_UP_3_TEMPLATE_NAME: str = os.getenv("META_FOLLOW_UP_3_TEMPLATE_NAME", "")
META_TEMPLATE_LANGUAGE_CODE: str = os.getenv("META_TEMPLATE_LANGUAGE_CODE", "en_US")

# ── Telegram Admin Alerts ─────────────────────────────────────────
TELEGRAM_BOT_TOKEN: str = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID: str = os.getenv("TELEGRAM_CHAT_ID", "")
ADMIN_PHONE_NUMBER: str = os.getenv("ADMIN_PHONE_NUMBER", "")
SERVER_PUBLIC_URL: str = os.getenv("SERVER_PUBLIC_URL", "http://localhost:8000").rstrip("/")

# ── Business Config ──────────────────────────────────────────────
COMPANY_NAME: str = os.getenv("COMPANY_NAME", "YourCompany")
AGENT_NAME: str = os.getenv("AGENT_NAME", "Priya")
PORTFOLIO_URL: str = os.getenv("PORTFOLIO_URL", "https://yourwebsite.com")
UPI_ID: str = os.getenv("UPI_ID", "name@upi")

# ── Package Pricing ──────────────────────────────────────────────
PACKAGES = {
    "Single Page": {
        "name": "Single Page",
        "price": 2999,
        "price_display": "₹2,999",
        "renewal_price": "₹2,999",
        "delivery_time": "24 hours",
        "revision_count": "1",
        "features": [
            "1 polished landing page",
            "Free domain (1st year)",
            "Mobile responsive design",
            "WhatsApp & Google Maps integration",
            "Contact form",
            "SSL certificate",
            "15 days free support",
        ],
    },
    "Starter": {
        "name": "Starter",
        "price": 6999,
        "price_display": "₹6,999",
        "renewal_price": "₹3,499",
        "delivery_time": "48 hours",
        "revision_count": "2",
        "features": [
            "Up to 5-page website",
            "Free domain (1st year)",
            "Basic SEO setup",
            "Image gallery",
            "WhatsApp & enquiry forms",
            "SSL certificate",
            "30 days free support",
            "2 revision rounds",
        ],
    },
    "Professional": {
        "name": "Professional",
        "price": 16999,
        "price_display": "₹16,999",
        "renewal_price": "₹4,999",
        "delivery_time": "72 hours",
        "revision_count": "3",
        "features": [
            "Up to 10-page website",
            "Free domain (1st year)",
            "Razorpay payment gateway integration",
            "Up to 25 listings/products",
            "Google Business Profile setup",
            "Lead capture system",
            "60 days free support",
            "3 revision rounds",
        ],
    },
    "E-Commerce": {
        "name": "E-Commerce",
        "price": 20999,
        "price_display": "₹20,999",
        "renewal_price": "₹6,999",
        "delivery_time": "5 days",
        "revision_count": "5",
        "features": [
            "Full online store",
            "100+ products capacity",
            "Razorpay (UPI/Cards/EMI)",
            "Inventory & order tracking",
            "Shipping integration",
            "Google Business Profile setup",
            "Owner training session",
            "90 days free support",
            "5 revision rounds",
        ],
    },
}

AUTOMATION_PACKAGES = {
    "WhatsApp Lead Management": {
        "name": "WhatsApp Lead Management",
        "price": 4999,
        "price_display": "₹4,999",
        "delivery_time": "48-72 hours",
        "features": [
            "Auto-capture leads from website forms",
            "Instant WhatsApp notifications",
            "Custom auto-reply templates",
            "Data stored in Google Sheets",
            "Follow-up reminder system",
        ],
    },
    "Google Sheets Automation": {
        "name": "Google Sheets Automation",
        "price": 3999,
        "price_display": "₹3,999",
        "delivery_time": "48-72 hours",
        "features": [
            "Form -> Sheets automation",
            "Email & WhatsApp notifications",
            "Data formatting & cleanup",
            "Scheduled reports",
            "Auto-sync between platforms",
        ],
    },
    "Custom Business Automation": {
        "name": "Custom Business Automation",
        "price": 7999,
        "price_display": "Starting ₹7,999",
        "delivery_time": "5-7 days",
        "features": [
            "Custom workflow design",
            "Multi-platform integration",
            "Invoice automation",
            "Inventory management sync",
            "Free consultation included",
        ],
    },
}

ADDITIONAL_SERVICES = {
    "GST Registration": "Govt fees + ₹599 (3-5 days)",
    "FSSAI Food License": "Govt fees + ₹399 (7-10 days)",
    "Udyam (MSME)": "₹399 (24 hours)",
    "Passport Services": "Govt fees + ₹599",
    "Payment Gateway Setup": "₹1,999 (Razorpay, PayU, Paytm)",
    "WhatsApp Business Setup": "₹1,999 (24 hours)",
    "SEO & Maintenance": "₹1,999/month (Cancel anytime)",
    "Google Business Profile": "₹599 (Free with Pro & E-Com packages)",
}

# ── Scraper Config ───────────────────────────────────────────────
TARGET_CITIES: list[str] = [
    c.strip()
    for c in os.getenv("TARGET_CITIES", "Delhi,Mumbai,Pune").split(",")
    if c.strip()
]

BUSINESS_TYPES: list[str] = [
    b.strip()
    for b in os.getenv("BUSINESS_TYPES", "Restaurant,Clinic,Salon,Gym,Retail").split(",")
    if b.strip()
]

HIGH_VALUE_TYPES: set[str] = {"Salon", "Clinic", "Restaurant", "Gym", "Spa", "Dental"}

SCRAPE_SCHEDULE_HOUR: int = int(os.getenv("SCRAPE_SCHEDULE_HOUR", "10"))
MAX_COLD_MESSAGES_PER_DAY: int = int(os.getenv("MAX_COLD_MESSAGES_PER_DAY", "12"))
SKIP_PLAYWRIGHT_SCRAPING: bool = os.getenv("SKIP_PLAYWRIGHT_SCRAPING", "false").lower() == "true"


# ── WhatsApp-web.js Node server ──────────────────────────────────
WHATSAPP_WEB_JS_URL: str = os.getenv("WHATSAPP_WEB_JS_URL", "http://localhost:3001")

# ── FastAPI Server ───────────────────────────────────────────────
SERVER_HOST: str = os.getenv("SERVER_HOST", "0.0.0.0")
SERVER_PORT: int = int(os.getenv("SERVER_PORT", "8000"))

# ── Timezone (for quota resets, scheduling) ──────────────────────
TIMEZONE: str = os.getenv("TIMEZONE", "Asia/Kolkata")
