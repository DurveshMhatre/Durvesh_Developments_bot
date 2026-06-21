"""
╔══════════════════════════════════════════════════════════════════╗
║         DURVESH DEVELOPMENTS — WhatsApp Outreach Templates       ║
║                                                                  ║
║  Written by: Senior Marketing Head + Outreach Expert Persona     ║
║  Language:   Hinglish (Hindi + English) — Maximum Relatability   ║
║  Tone:       Warm • Confident • Conversational • Trust-Building  ║
║  Strategy:   Hook → Value → Proof → CTA → Urgency               ║
║                                                                  ║
║  WhatsApp Formatting Supported:                                  ║
║    *bold*  _italic_  ~strikethrough~  ```monospace```            ║
║  Note: Keep lines short (≤ 60 chars) for mobile readability      ║
╚══════════════════════════════════════════════════════════════════╝
"""

from __future__ import annotations

from config.settings import (
    AGENT_NAME,
    COMPANY_NAME,
    PORTFOLIO_URL,
    UPI_ID,
)

# ══════════════════════════════════════════════════════════════════
#  WELCOME MESSAGES
#  Strategy : HOOK in line 1, VALUE in body, SOFT CTA at end
#  Variants : A/B test across different business types
# ══════════════════════════════════════════════════════════════════

# ── Variant A : Generic (No Website Detected) ─────────────────────
WELCOME_MESSAGE = (
    "🙏 *Namaste {business_name} ji!*\n\n"

    "Maine aapka business Google Maps par dekha —\n"
    "aapke *{review_count}+ reviews* aur *{rating}⭐ rating*\n"
    "dekh ke laga aap bohot mehnat karte hain! 👏\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "❌ *Ek Problem Notice Ki:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Aapki koi *professional website nahi hai.*\n\n"

    "Iska matlab hai ki aaj bhi hazaron log\n"
    "*\"{business_type} near me\"* Google karte hain\n"
    "aur... aap *invisible* hain unke liye. 😔\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "✅ *Main Kya Kar Sakta Hoon:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Main *{agent_name}* hoon — {company_name} se.\n"
    "Main {city} ke local businesses ke liye\n"
    "*professional websites banata hoon —*\n"
    "*sirf ₹2,999 se starting!* 🚀\n\n"

    "⚡ *24 se 72 ghante mein delivery*\n"
    "💳 *Razorpay payment gateway included*\n"
    "📍 *Google Business Profile FREE*\n"
    "📱 *100% mobile optimized*\n\n"

    "Kya aap chahenge ki main aapke liye\n"
    "*ek FREE demo website* banake dikhaaun?\n\n"

    "Bas *\"HAAN\"* reply kijiye! 😊\n\n"

    "— {agent_name}\n"
    "📞 {company_name} | {city}"
)

# ── Variant B : Competitor Angle (Higher Urgency) ─────────────────
WELCOME_MESSAGE_B = (
    "🙏 *{business_name} ji, ek zaroori baat!*\n\n"

    "Main {agent_name} hoon, {company_name} se.\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "📊 *{city} mein Research Ki:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Aapke competitors already online hain:\n\n"

    "🔴 *{competitor_1}* — Website + Google Ads\n"
    "🔴 *{competitor_2}* — Online booking active\n"
    "🔴 *{competitor_3}* — 200+ Google reviews\n\n"

    "Aap? *Abhi bhi sirf word-of-mouth par!* 😟\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "💡 *Mera Solution:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Aapki *professional website* — *48 ghante mein!*\n\n"

    "✅ Starting sirf *₹2,999*\n"
    "✅ UPI/Card payments ready\n"
    "✅ Google Maps integration\n"
    "✅ WhatsApp business button\n"
    "✅ *FREE domain (1st year)*\n\n"

    "Interested? Bas *\"YES\"* reply karo!\n\n"

    "Portfolio dekho: {portfolio_url}\n\n"

    "— {agent_name} 🙏\n"
    "{company_name}"
)

# ── Variant C : Local Trust Angle (Warm & Personal) ───────────────
WELCOME_MESSAGE_C = (
    "🙏 *Namaste {business_name} ji!*\n\n"

    "Main {agent_name} —\n"
    "aapka hi ek {city} wala! 😊\n\n"

    "Main {company_name} chalata hoon\n"
    "jahan hum local businesses ke liye\n"
    "*AI-powered websites* banate hain.\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "🤔 *Ek Sawaal:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Aapke paas kitne customers *directly*\n"
    "*Google* se aate hain?\n\n"

    "Agar jawaab *\"bahut kam\"* hai —\n"
    "toh main help kar sakta hoon! 🚀\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "🎁 *Aapke Liye FREE Offer:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "*FREE Website Audit* — Bilkul FREE!\n\n"

    "Main aapko dikhaunga:\n"
    "📌 Aap Google par kahan hain\n"
    "📌 Competitors kya kar rahe hain\n"
    "📌 Exactly kya karna chahiye\n\n"

    "Koi commitment nahi. Bas ek reply. 😊\n\n"

    "*\"AUDIT\"* likhiye — baaki main sambhalunga!\n\n"

    "— {agent_name}\n"
    "{company_name} | {city} 📍"
)


# ══════════════════════════════════════════════════════════════════
#  FOLLOW-UP MESSAGES
#  Strategy  : Each follow-up adds NEW value, never just reminds
#  Sequence  : Day 1 → Day 3 → Day 7 → Day 14 (Final)
#  Rule      : Never beg. Always offer something new.
# ══════════════════════════════════════════════════════════════════

# ── Follow-Up 1 : Day 1-2 (Add Urgency + Value) ───────────────────
FOLLOW_UP_1 = (
    "🔥 *{business_name} ji — Limited Offer!*\n\n"

    "Ye week ek *special deal* chal rahi hai\n"
    "sirf {city} ke businesses ke liye:\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "🎁 *Is Hafte Book Karo, FREE Milega:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "✅ Professional Website\n"
    "✅ *FREE AI Gemini Logo Design* (₹999 value)\n"
    "✅ *FREE Google Business Setup* (₹599 value)\n"
    "✅ *FREE WhatsApp Button Integration*\n"
    "✅ *FREE Domain — 1st Year*\n\n"

    "💰 *Sab milega sirf ₹{package_price} mein!*\n"
    "⚡ Delivery: *{delivery_time}*\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "⏳ *Offer sirf {offer_expiry} tak valid hai!*\n\n"

    "Confirm karne ke liye reply karo:\n"
    "*\"BOOK\"* — Abhi secure karo ye deal! 🚀\n\n"

    "— {agent_name}\n"
    "{company_name} | 📞 {phone_number}"
)

# ── Follow-Up 2 : Day 3-4 (Pain Point Re-engagement) ────────────────
FOLLOW_UP_2 = (
    "🙏 *{business_name} ji,*\n\n"

    "Pichle kuch din sochta raha —\n"
    "aapke business ke baare mein kuch\n"
    "important share karna chahta tha.\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "😟 *Ye Padhke Dukh Hua:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Har mahine *{monthly_searches}+ log* Google par\n"
    "search karte hain:\n"
    "*\"{search_term}\"*\n\n"

    "Inme se *90% log* kisi website wale\n"
    "ko prefer karte hain.\n\n"

    "Matlab aap har mahine\n"
    "*{lost_customers}+ potential customers*\n"
    "miss kar rahe hain. 😔\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "💡 *Simple Solution:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Ek *professional website* —\n"
    "starting sirf *₹2,999!*\n\n"

    "Ye investment ek month mein\n"
    "wapas aa jaati hai — *guaranteed!*\n\n"

    "Interested hai to bas batao:\n"
    "*\"HAAN\"* ✅ ya *\"NAHI\"* ❌\n\n"

    "Dono answer theek hain — bas reply karo! 😊\n\n"

    "— {agent_name}\n"
    "{company_name} 🙏"
)

# ── Follow-Up 3 : Day 7 (Final Breakup Message) ─────────────────
FOLLOW_UP_3 = (
    "👋 *{business_name} ji — Last Message!*\n\n"

    "Main samajhta hoon —\n"
    "shayad ye sahi time nahi aapke liye.\n\n"

    "Koi problem nahi! 🙏\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "🎁 *Jaane Se Pehle — Ek Gift:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Main aapke liye *FREE* banata hoon:\n\n"

    "📊 *Aapka Digital Report Card*\n"
    "  • Google visibility score\n"
    "  • Competitor comparison\n"
    "  • Top 3 improvement areas\n\n"

    "Bilkul FREE. Koi catch nahi.\n"
    "Just ek token of appreciation\n"
    "aapka time dene ke liye. 😊\n\n"

    "Chahiye? *\"REPORT\"* likhiye!\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Jab bhi website chahiye —\n"
    "main hamesha yahan hoon! 🤝\n\n"

    "Aapka din shubh ho!\n\n"

    "— {agent_name}\n"
    "{company_name} | {portfolio_url}"
)


# ══════════════════════════════════════════════════════════════════
#  PACKAGE RECOMMENDATION MESSAGES
#  Strategy  : Personalized → Specific → Visual → Clear CTA
#  Format    : WhatsApp bold/italic used for visual hierarchy
# ══════════════════════════════════════════════════════════════════

# ── Full Package Recommendation ────────────────────────────────────
PACKAGE_RECOMMENDATION = (
    "🎯 *{business_name} ji — Aapke Liye Perfect Plan!*\n\n"

    "Aapka business sun ke laga ki\n"
    "ye package exactly fit baithega:\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "📦 *{package_name} Package*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "💰 *Price: {price_display}* (one-time)\n"
    "🔄 Renewal: {renewal_price}/year (2nd year se)\n"
    "⚡ Delivery: *{delivery_time}*\n"
    "✏️ Revisions: *{revision_count} rounds FREE*\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "✅ *Aapko Kya Milega:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"
    "{features_list}\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "🏆 *Ye Package Kyun?*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"
    "{package_reasoning}\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "💳 *Payment Process:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Step 1️⃣ — *50% advance* pay karo\n"
    "Step 2️⃣ — Hum website banate hain\n"
    "Step 3️⃣ — Aap *approve* karo\n"
    "Step 4️⃣ — *50% balance* pay karo\n"
    "Step 5️⃣ — Website *LIVE!* 🚀\n\n"

    "💳 UPI ID: `{upi_id}`\n"
    "   _(GPay • PhonePe • Paytm — sab chalega!)_\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "🖥️ *Humara Kaam Dekhiye:*\n"
    "{portfolio_url}\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Reply karo:\n"
    "✅ *\"CONFIRM\"* — Ye package book karna hai\n"
    "🔄 *\"OPTIONS\"* — Dusre packages dekhne hain\n"
    "❓ *\"SAWAAL\"* — Kuch poochna hai\n\n"

    "Aapka jawab wait kar raha hoon! 😊\n\n"

    "— {agent_name}\n"
    "{company_name} 🙏"
)

# ── Quick Package Summary (Short Version) ─────────────────────────
PACKAGE_QUICK_SUMMARY = (
    "⚡ *Quick Summary — {business_name} ji:*\n\n"

    "┌─────────────────────────┐\n"
    "│ 📦 *{package_name}*          │\n"
    "│ 💰 *{price_display}*        │\n"
    "│ ⏱️ *{delivery_time}*        │\n"
    "└─────────────────────────┘\n\n"

    "*Top 3 Features:*\n"
    "  {feature_1}\n"
    "  {feature_2}\n"
    "  {feature_3}\n\n"

    "*\"DETAILS\"* — Full breakdown\n"
    "*\"BOOK\"* — Abhi confirm karo! 🚀"
)

# ── All Packages Comparison ────────────────────────────────────────
ALL_PACKAGES_COMPARISON = (
    "📋 *{business_name} ji — Sabhi Plans:*\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "1️⃣ *SINGLE PAGE — ₹2,999*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "⚡ Delivery: 24 hours\n"
    "👥 Best for: Salons, Shops, Tailors\n"
    "✅ 1 page • Domain FREE • WhatsApp button\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "2️⃣ *STARTER — ₹6,999*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "⚡ Delivery: 48 hours\n"
    "👥 Best for: Clinics, Coaching Centers\n"
    "✅ 5 pages • SEO • Gallery • Forms\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "3️⃣ *PROFESSIONAL — ₹16,999* ⭐\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "⚡ Delivery: 72 hours\n"
    "👥 Best for: Real Estate, Restaurants\n"
    "✅ 10 pages • Razorpay • GBP FREE\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "4️⃣ *E-COMMERCE — ₹20,999*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "⚡ Delivery: 5 days\n"
    "👥 Best for: Retail, Boutiques\n"
    "✅ Full store • 100 products • EMI\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "*Aapke {business_type} ke liye*\n"
    "*main recommend karunga: {recommended_package}* 💡\n\n"

    "Reply:\n"
    "*\"1\"* *\"2\"* *\"3\"* *\"4\"* — Package select karo\n"
    "*\"CALL\"* — Direct baat karte hain 📞"
)


# ══════════════════════════════════════════════════════════════════
#  INTERESTED CLIENT RESPONSES
#  Strategy : Immediate warm response, clear next steps, momentum
# ══════════════════════════════════════════════════════════════════

# ── Initial Interest Confirmation ─────────────────────────────────
INTERESTED_HANDOFF = (
    "🎉 *Waah! Bahut Badhiya {business_name} ji!*\n\n"

    "Ye sunke bahut khushi hui! 😊\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "📋 *Aage Kya Hoga:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "⏰ *Next 2 hours mein* — Main ya\n"
    "   {agent_name} aapko call/WA karenge\n\n"

    "📝 *Call mein hum discuss karenge:*\n"
    "  • Aapka exact requirement\n"
    "  • Best package recommendation\n"
    "  • Design preferences\n"
    "  • Content & photos needed\n"
    "  • Payment process\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "🚀 *Jaldi Start Karna Hai?*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Ye *3 cheezein* abhi share karo:\n\n"

    "1️⃣ *Business ka full naam*\n"
    "2️⃣ *Kya services/products offer karte ho*\n"
    "3️⃣ *Koi preferred color/style hai?*\n\n"

    "Jitni jaldi details, utni jaldi website! ⚡\n\n"

    "*{company_name}* mein aapka swagat hai! 🙏\n\n"

    "— {agent_name}\n"
    "📞 {phone_number}"
)

# ── Post Payment Confirmation ──────────────────────────────────────
PAYMENT_RECEIVED = (
    "💚 *Payment Received! Thank You {business_name} ji!*\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "🧾 *Payment Summary:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "📦 Package: *{package_name}*\n"
    "💰 Amount: *{amount_paid}*\n"
    "📅 Date: *{payment_date}*\n"
    "🆔 Ref: `{transaction_id}`\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "⏱️ *Delivery Timeline:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "🟡 *Abhi* — Work started!\n"
    "🟡 *{milestone_1_time}* — Design ready (preview)\n"
    "🟡 *{milestone_2_time}* — Your feedback\n"
    "🟢 *{go_live_time}* — WEBSITE LIVE! 🚀\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Kisi bhi sawaal ke liye — anytime WhatsApp karo!\n\n"

    "Aapka trust = Hamaari zimmedaari! 🙏\n\n"

    "— {agent_name}\n"
    "{company_name}"
)

# ── Website Preview Ready ──────────────────────────────────────────
WEBSITE_PREVIEW_READY = (
    "🎨 *{business_name} ji — Preview Ready Hai!*\n\n"

    "Aapki website ka *pehla look* taiyaar hai!\n"
    "Dekho aur batao kaisi lagi! 👀\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "🔗 *Preview Link:*\n"
    "{preview_url}\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "*Check Karo:*\n"
    "✅ Naam aur address sahi hai?\n"
    "✅ Photos theek lag rahi hain?\n"
    "✅ Colors pasand aaye?\n"
    "✅ Services sahi likhi hain?\n"
    "✅ Contact details correct hain?\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Reply karo:\n"
    "🟢 *\"APPROVED\"* — Bilkul perfect!\n"
    "🔄 *\"CHANGES\"* — Kuch badalna hai\n"
    "📞 *\"CALL\"* — Discussion chahiye\n\n"

    "⏳ *Review time: 24 hours*\n"
    "_(Uske baad auto-approved)_\n\n"

    "— {agent_name} 😊\n"
    "{company_name}"
)


# ══════════════════════════════════════════════════════════════════
#  OBJECTION HANDLING MESSAGES
#  Strategy : Acknowledge → Reframe → Prove → Re-offer
#  Never argue. Always empathize and provide value.
# ══════════════════════════════════════════════════════════════════

# ── Price Objection ────────────────────────────────────────────────
OBJECTION_TOO_EXPENSIVE = (
    "🙏 *Samajh sakta hoon, {business_name} ji!*\n\n"

    "Budget ki tension sabko hoti hai.\n"
    "Main honest rehna chahta hoon aapke saath:\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "📊 *Real Comparison:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "📰 *Newspaper ad (1 hafte):*\n"
    "   ₹8,000–₹15,000 → Sirf 7 din\n\n"

    "📺 *Cable TV ad (1 mahina):*\n"
    "   ₹10,000–₹25,000 → Sirf 30 din\n\n"

    "🌐 *Professional Website:*\n"
    "   *₹2,999* → *HAMESHA ke liye!* ✅\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "💰 *ROI Calculate Karo:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Agar website se sirf *2 extra customers*\n"
    "per month aaye — kitna kamaoge?\n\n"

    "*2 customers × ₹{avg_order_value} = ₹{monthly_gain}*\n\n"

    "Website ka paisa *{payback_months} mahine* mein\n"
    "wapas aa jaata hai! 📈\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "🎁 *Budget Tight? No Problem:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "✅ *50% advance* — Kaam shuru\n"
    "✅ *50% baad mein* — Jab approve karo\n\n"

    "Pehle *₹{advance_amount}* se start karo! 💪\n\n"

    "Baat karte hain? *\"HAAN\"* reply karo!\n\n"

    "— {agent_name} 🙏"
)

# ── Trust Objection ────────────────────────────────────────────────
OBJECTION_NOT_TRUSTWORTHY = (
    "🙏 *Bilkul sahi poocha {business_name} ji!*\n\n"

    "Online trust banana mushkil hota hai.\n"
    "Main aapki jagah bhi yehi poochta! 😊\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "🛡️ *Hum Kyon Trustworthy Hain:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "📍 *Local hoon* — {city} mein hi rehta hoon\n"
    "   (Office pe mil sakte hain!)\n\n"

    "🏆 *Real Projects* — {portfolio_url}\n"
    "   (Live websites dekhiye abhi!)\n\n"

    "⭐ *Client References* — 3 clients se\n"
    "   directly baat kar sakte hain aap\n\n"

    "📜 *Written Agreement* — Sab kuch\n"
    "   likhit mein milega (deliverables,\n"
    "   timeline, payment terms)\n\n"

    "💳 *50-50 Payment* — Poora advance\n"
    "   nahi! Pehle website dekho,\n"
    "   phir baaki payment karo\n\n"

    "🔄 *30-Day Refund* — Kaam shuru\n"
    "   na hua to full refund!\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Kya aap *in-person* milna chahenge?\n"
    "Main {city} mein hi hoon! ☕\n\n"

    "*\"MEET\"* reply karo — time fix karte hain!\n\n"

    "— {agent_name}\n"
    "{company_name} | 📍 {city}"
)

# ── "Already Have Website" Objection ──────────────────────────────
OBJECTION_HAVE_WEBSITE = (
    "🙏 *Bahut Badhiya {business_name} ji!*\n\n"

    "Ye toh great news hai ki website already hai!\n\n"

    "Ek kaam karein — main FREE mein\n"
    "*aapki website audit kar deta hoon*:\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "🔍 *FREE Audit Mein Dekhenge:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "📱 Mobile speed score\n"
    "🔍 Google ranking status\n"
    "💳 Payment gateway present?\n"
    "📞 WhatsApp button working?\n"
    "📍 Google Maps integrated?\n"
    "🔒 SSL certificate valid?\n"
    "⚡ Page load time\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Agar website perfectly theek hai —\n"
    "_main khud bolunga chhod do!_ 😊\n\n"

    "Agar issues hain — *hum fix kar denge!*\n\n"

    "Website URL share karo:\n"
    "*\"AUDIT: [your-website.com]\"*\n\n"

    "FREE hai — koi obligation nahi! 🙏\n\n"

    "— {agent_name}\n"
    "{company_name}"
)

# ── "Need Time to Think" Objection ────────────────────────────────
OBJECTION_NEED_TIME = (
    "🙏 *Bilkul {business_name} ji — sochiye!*\n\n"

    "Ye important decision hai — jaldi karne\n"
    "ki koi zaroorat nahi! 😊\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "🎁 *Sochte Sochte — Ye Bhi Lo:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Main abhi bhej raha hoon:\n\n"

    "📊 *FREE Competitor Report*\n"
    "   (aapke 5 competitors online\n"
    "    kya kar rahe hain)\n\n"

    "🎨 *FREE Website Mockup*\n"
    "   (aapki website kaisi dikh\n"
    "    sakti hai — sirf for you)\n\n"

    "📈 *FREE Growth Roadmap*\n"
    "   (exactly kya karna chahiye\n"
    "    aapke business ke liye)\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Sab *100% FREE* — no strings! 🙏\n\n"

    "Bas *\"BHEJO\"* reply karo!\n\n"

    "Kaab bhi decide karo — main yahan hoon!\n\n"

    "— {agent_name} 😊"
)

# ── Discount Request Handling ──────────────────────────────────────
OBJECTION_WANTS_DISCOUNT = (
    "😊 *{business_name} ji — Main Honest Rahoon:*\n\n"

    "Hum pehle se bahut competitive price\n"
    "de rahe hain — agencies ₹50,000–₹2 lakh\n"
    "charge karti hain, hum sirf ₹{price_display}!\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "💡 *Lekin Ye Kar Sakta Hoon:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Option 1️⃣ *Start Smaller:*\n"
    "   *{lower_package}* plan se start karo\n"
    "   → *{lower_price}* mein!\n"
    "   Later upgrade karo (difference pay)\n\n"

    "Option 2️⃣ *Refer Karo, Bachao:*\n"
    "   1 referral = *₹1,000 credit* 🎁\n"
    "   2 referrals = *₹2,500 credit!*\n\n"

    "Option 3️⃣ *Content Aap Dijiye:*\n"
    "   Photos + text aap provide karo\n"
    "   → *₹1,500 discount* milega!\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Inme se kaunsa option theek lagta hai?\n"
    "*\"1\"* *\"2\"* *\"3\"* reply karo! 😊\n\n"

    "— {agent_name} 🙏"
)


# ══════════════════════════════════════════════════════════════════
#  NOT INTERESTED RESPONSES
#  Strategy : Never burn bridges. Leave positively. Ask for referral.
# ══════════════════════════════════════════════════════════════════

NOT_INTERESTED_RESPONSE = (
    "🙏 *Koi baat nahi {business_name} ji!*\n\n"

    "Aapka time dene ke liye shukriya! 😊\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "🌟 *Ek Chhoti Si Request:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Agar aapko kisi aur business owner ko\n"
    "jaante ho jise website ki zaroorat ho —\n"
    "mera number share kar dijiye! 🤝\n\n"

    "*Aapko milega:*\n"
    "🎁 *₹500 referral bonus* har successful\n"
    "   referral par! (UPI pe direct!)\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Aur jab bhi aapko website chahiye —\n"
    "main *hamesha yahan hoon!* 🙏\n\n"

    "Aapka din bahut accha ho!\n"
    "Business flourish kare! 🌸\n\n"

    "— {agent_name}\n"
    "{company_name}\n"
    "📞 {phone_number}"
)

# ── Wrong Number / Wrong Contact ───────────────────────────────────
NOT_INTERESTED_WRONG_CONTACT = (
    "🙏 *Sorry for the disturbance!*\n\n"

    "Aapko galti se message hua — maafi chahta hoon!\n\n"

    "Agar kabhi website ki zaroorat ho,\n"
    "please contact kijiye:\n\n"

    "📞 *{phone_number}*\n"
    "🌐 *{portfolio_url}*\n\n"

    "Have a great day! 🙏\n\n"

    "— {agent_name}, {company_name}"
)


# ══════════════════════════════════════════════════════════════════
#  POST-DELIVERY MESSAGES
#  Strategy : Delight, collect feedback, upsell, ask for referral
# ══════════════════════════════════════════════════════════════════

# ── Website Delivery Message ───────────────────────────────────────
WEBSITE_DELIVERY = (
    "🎉 *{business_name} ji — WEBSITE LIVE HAI!* 🚀\n\n"

    "*Mubaarak ho!* Aapka business ab officially\n"
    "online hai! 🌐✨\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "🔗 *Aapki Website:*\n"
    "*{live_url}*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "📱 *Abhi Karo:*\n"
    "  1. Website kholo\n"
    "  2. Screenshot lo\n"
    "  3. WhatsApp Status par lagao! 😄\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "🔐 *Login Credentials:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "🌐 Dashboard: {admin_url}\n"
    "👤 Username: `{username}`\n"
    "🔑 Password: `{password}`\n\n"

    "_(Please change password after first login!)_\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "📚 *Resources:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "🎥 Tutorial Video: {tutorial_url}\n"
    "📖 Quick Guide: {guide_url}\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Koi help chahiye to anytime WhatsApp karo!\n"
    "*Support period: {support_days} days* 🛡️\n\n"

    "{company_name} ki taraf se bahut\n"
    "*dhanyawad aur shubhkamnayein!* 🙏\n\n"

    "— {agent_name}"
)

# ── 7-Day Check-in ─────────────────────────────────────────────────
CHECKIN_7_DAYS = (
    "👋 *{business_name} ji — Kaisa Chal Raha Hai?*\n\n"

    "Website live hue ek hafte ho gaya! ⏰\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "📊 *Aapke Results Dekhna Chahta Hoon:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "📈 Website pe kitne visitors aaye?\n"
    "📞 Kitne calls/inquiries aaye?\n"
    "💬 WhatsApp button use hua?\n"
    "⭐ Koi customers ne online dhundha?\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Koi bhi issue ho to *abhi batao* —\n"
    "free mein fix kar dunga! 🔧\n\n"

    "Aur ek request — kya aap *Google pe*\n"
    "*ek review de sakte hain?* ⭐⭐⭐⭐⭐\n\n"

    "Bahut help hogi hume! 🙏\n\n"

    "— {agent_name}\n"
    "{company_name}"
)

# ── 30-Day Upsell Message ──────────────────────────────────────────
UPSELL_30_DAYS = (
    "🌟 *{business_name} ji — 30 Din Ho Gaye!*\n\n"

    "Ek mahina website ke saath ho gaya!\n"
    "Hope sab accha chal raha hai! 😊\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "🚀 *Aage Aur Grow Karo:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Existing clients ke liye *special rates:*\n\n"

    "📈 *SEO & Maintenance* — ₹1,999/month\n"
    "   (Google par top rank aao!)\n\n"

    "💬 *WhatsApp Business Setup* — ₹1,999\n"
    "   (Professional business account)\n\n"

    "📱 *Social Media Management* — ₹7,999/month\n"
    "   (Instagram + Facebook daily posts)\n\n"

    "📍 *Google Business Optimization* — ₹999\n"
    "   (More calls from Google Maps)\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Kaunsi service next chahiye?\n"
    "Reply karo aur *10% loyalty discount* pao! 🎁\n\n"

    "— {agent_name} 🙏\n"
    "{company_name}"
)

# ── Renewal Reminder ───────────────────────────────────────────────
RENEWAL_REMINDER = (
    "⚠️ *{business_name} ji — Important!*\n\n"

    "Aapki website ki *hosting + domain*\n"
    "*{days_until_expiry} din mein expire* ho rahi hai!\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "📅 *Expiry Date: {expiry_date}*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Renew na karne par:\n"
    "❌ Website *offline* ho jaayegi\n"
    "❌ Email *kaam karna band* kar dega\n"
    "❌ Google ranking *drop* ho sakti hai\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "✅ *Renewal Charge:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "💰 *₹{renewal_price}/year* (same as before)\n\n"

    "💳 UPI ID: `{upi_id}`\n"
    "   _(GPay • PhonePe • Paytm)_\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Payment karte hi *auto-renew* ho jaayega! ⚡\n\n"

    "Jaldi karo — *grace period sirf 7 din!*\n\n"

    "— {agent_name}\n"
    "{company_name} 🙏\n"
    "📞 {phone_number}"
)


# ══════════════════════════════════════════════════════════════════
#  SPECIAL CAMPAIGN MESSAGES
#  Strategy : Festival/seasonal offers, FOMO, limited time
# ══════════════════════════════════════════════════════════════════

# ── Festival Season Offer ──────────────────────────────────────────
FESTIVAL_CAMPAIGN = (
    "🎊 *{festival_name} Special Offer!* 🎊\n\n"

    "🙏 *{business_name} ji, {festival_greeting}!*\n\n"

    "Is tyohaar mein, hum {city} ke\n"
    "businesses ke liye special de rahe hain:\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "🎁 *{festival_name} Package:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "✅ Professional Website\n"
    "✅ *FREE AI Gemini Logo Design* (₹999 value)\n"
    "✅ *FREE {festival_bonus}*\n"
    "✅ *FREE Google Business Setup*\n"
    "✅ *FREE Domain (1st year)*\n\n"

    "💰 *Sab milega sirf ₹{festival_price}!*\n"
    "_Regular price: ~~₹{regular_price}~~_\n\n"

    "⏳ *Offer Valid Till: {offer_expiry}*\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Is {festival_name} pe business ko\n"
    "*online gift do!* 🎁\n\n"

    "*\"FESTIVAL\"* reply karo — book karo! 🚀\n\n"

    "— {agent_name}\n"
    "{company_name} | {city} 🙏"
)

# ── Industry-Specific Campaign ─────────────────────────────────────
INDUSTRY_CAMPAIGN = (
    "🙏 *{business_name} ji!*\n\n"

    "Main specifically *{business_type}* owners\n"
    "ke liye ek special offer le ke aaya hoon!\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "📊 *Kya Aap Jaante Ho?*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "🔍 *{industry_stat_1}*\n\n"

    "🔍 *{industry_stat_2}*\n\n"

    "🔍 *{industry_stat_3}*\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "💡 *{business_type} Website Mein:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "{industry_features_list}\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "💰 *Starting: ₹{industry_price}*\n"
    "⚡ *Delivery: {delivery_time}*\n\n"

    "Already {city} mein *{industry_client_count}+*\n"
    "*{business_type} businesses* hain hamare saath! 🏆\n\n"

    "*\"DEMO\"* reply karo — sample dekhte hain!\n\n"

    "— {agent_name}\n"
    "{company_name} 🙏"
)


# ══════════════════════════════════════════════════════════════════
#  TELEGRAM ADMIN ALERTS
#  Strategy : Quick scan format. Bold key info. Actionable.
# ══════════════════════════════════════════════════════════════════

ADMIN_NEW_INTERESTED_LEAD = (
    "🔥 <b>HOT LEAD — Action Required!</b>\n\n"

    "━━━━━━━━━━━━━━━━━━━\n"
    "📛 <b>Business:</b> {business_name}\n"
    "👤 <b>Contact:</b> {contact_name}\n"
    "📱 <b>Phone:</b> <code>{phone}</code>\n"
    "🏷️ <b>Type:</b> {business_type}\n"
    "📍 <b>City:</b> {city}\n"
    "⭐ <b>Rating:</b> {rating} ({review_count} reviews)\n"
    "━━━━━━━━━━━━━━━━━━━\n\n"

    "💬 <b>Their Message:</b>\n"
    "<i>{last_message}</i>\n\n"

    "━━━━━━━━━━━━━━━━━━━\n"
    "📋 <b>Requirements:</b>\n"
    "{requirements_summary}\n\n"

    "📦 <b>Recommended:</b> {package_name}\n"
    "💰 <b>Value:</b> {price_display}\n"
    "🕐 <b>Lead Age:</b> {lead_age}\n"
    "━━━━━━━━━━━━━━━━━━━\n\n"

    "🚨 <b>ACTION NEEDED:</b>\n"
    "→ Call/WA within <b>30 minutes!</b>\n"
    "→ Send payment link after confirmation\n"
    "→ UPI: <code>{upi_id}</code>\n\n"

    "📊 Conversation Stage: <b>{conversation_stage}</b>"
)

ADMIN_PAYMENT_RECEIVED = (
    "💰 <b>PAYMENT RECEIVED!</b> 🎉\n\n"

    "━━━━━━━━━━━━━━━━━━━\n"
    "📛 <b>Client:</b> {business_name}\n"
    "📱 <b>Phone:</b> <code>{phone}</code>\n"
    "💳 <b>Amount:</b> ₹{amount}\n"
    "📦 <b>Package:</b> {package_name}\n"
    "🆔 <b>Txn ID:</b> <code>{transaction_id}</code>\n"
    "📅 <b>Date:</b> {payment_date}\n"
    "━━━━━━━━━━━━━━━━━━━\n\n"

    "⚡ <b>ACTION:</b>\n"
    "→ Start website in <b>next 2 hours</b>\n"
    "→ Send confirmation WA to client\n"
    "→ Update CRM status to 'In Progress'\n"
    "→ Delivery deadline: <b>{delivery_deadline}</b>"
)

ADMIN_DAILY_SUMMARY = (
    "📊 <b>Daily Performance Report</b>\n"
    "📅 {report_date}\n\n"

    "━━━━━━━━━━━━━━━━━━━\n"
    "🔍 <b>Lead Generation:</b>\n"
    "  Scraped today: <b>{leads_scraped}</b>\n"
    "  Qualified leads: <b>{qualified_leads}</b>\n"
    "  Already contacted: <b>{already_contacted}</b>\n\n"

    "📤 <b>Outreach:</b>\n"
    "  Messages sent: <b>{messages_sent}</b>\n"
    "  Delivered: <b>{messages_delivered}</b>\n"
    "  Failed: <b>{messages_failed}</b>\n\n"

    "📥 <b>Responses:</b>\n"
    "  Total replies: <b>{replies_received}</b>\n"
    "  Positive: <b>{interested_count}</b> ✅\n"
    "  Negative: <b>{not_interested_count}</b> ❌\n"
    "  No reply: <b>{no_reply_count}</b> ⏳\n\n"

    "💰 <b>Revenue:</b>\n"
    "  Payments today: <b>{payments_today}</b>\n"
    "  Amount: <b>₹{revenue_today}</b>\n\n"

    "━━━━━━━━━━━━━━━━━━━\n"
    "📈 <b>Conversion Rate:</b> {conversion_rate}%\n"
    "💬 <b>Response Rate:</b> {response_rate}%\n"
    "🏆 <b>Best Template:</b> {best_template}\n"
    "━━━━━━━━━━━━━━━━━━━\n\n"

    "🎯 <b>Tomorrow's Target:</b> {tomorrow_target} leads"
)

ADMIN_WEEKLY_SUMMARY = (
    "📊 <b>Weekly Performance Summary</b>\n"
    "📅 Week of {week_start} — {week_end}\n\n"

    "━━━━━━━━━━━━━━━━━━━\n"
    "🏆 <b>Weekly Highlights:</b>\n\n"

    "📤 Total messages: <b>{total_messages}</b>\n"
    "🎯 Interested leads: <b>{total_interested}</b>\n"
    "💰 Revenue: <b>₹{total_revenue}</b>\n"
    "🌐 Websites delivered: <b>{websites_delivered}</b>\n\n"

    "━━━━━━━━━━━━━━━━━━━\n"
    "📦 <b>Package Breakdown:</b>\n"
    "  Single Page: {single_page_count}\n"
    "  Starter: {starter_count}\n"
    "  Professional: {professional_count}\n"
    "  E-Commerce: {ecommerce_count}\n\n"

    "━━━━━━━━━━━━━━━━━━━\n"
    "💡 <b>Best Performing:</b>\n"
    "  City: <b>{best_city}</b>\n"
    "  Industry: <b>{best_industry}</b>\n"
    "  Template: <b>{best_template}</b>\n"
    "  Follow-up: <b>{best_followup}</b>\n"
    "━━━━━━━━━━━━━━━━━━━\n\n"

    "📈 Next week target: <b>₹{next_week_target}</b>"
)

ADMIN_SYSTEM_ERROR = (
    "🚨 <b>SYSTEM ALERT</b>\n\n"

    "❌ Error in: <b>{error_module}</b>\n"
    "📝 Message: <code>{error_message}</code>\n"
    "🕐 Time: {error_time}\n"
    "🔢 Error Code: <code>{error_code}</code>\n\n"

    "⚠️ <b>Affected:</b> {affected_leads} leads paused\n\n"

    "👉 Check logs immediately!"
)


# ══════════════════════════════════════════════════════════════════
#  SPECIAL SITUATION TEMPLATES
# ══════════════════════════════════════════════════════════════════

# ── Referral Request ───────────────────────────────────────────────
REFERRAL_REQUEST = (
    "🙏 *{business_name} ji — Ek Chhoti Si Madad!*\n\n"

    "Aap hamare happy client hain —\n"
    "aur iske liye bahut shukriya! 🌟\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "💰 *Kamao Referring Karke:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Kisi bhi business owner ko refer karo\n"
    "jo website banana chahta ho:\n\n"

    "1 referral = *₹500 cash* 🎁\n"
    "3 referrals = *₹2,000 cash* 🎁🎁\n"
    "5 referrals = *₹5,000 cash* 🤩\n\n"

    "_(UPI pe direct payment!)_\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Unhe bas ye number share karo:\n"
    "📞 *{phone_number}*\n\n"

    "Ya ye message forward karo! ⬇️\n\n"

    "---\n"
    "_Mujhe {agent_name} ne refer kiya {company_name} ke liye —_\n"
    "_professional websites starting ₹2,999 mein!_\n"
    "_Contact: {phone_number}_\n"
    "---\n\n"

    "Thank you {business_name} ji! 🙏"
)

# ── Google Review Request ──────────────────────────────────────────
GOOGLE_REVIEW_REQUEST = (
    "⭐ *{business_name} ji — Ek Favor!*\n\n"

    "Aapki website successfully live hai\n"
    "aur sab accha chal raha hai! 🎉\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "🙏 *Ek Chhoti Si Request:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Kya aap *Google par ek review* de\n"
    "sakte hain? Sirf 2 minute lagenge!\n\n"

    "👇 *Direct link:*\n"
    "{google_review_url}\n\n"

    "Aapka ek review bahut logo ko\n"
    "sahi decision lene mein help karta hai! 🌟\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Review dene par aapko milega:\n"
    "🎁 *FREE 1 month SEO consultation*\n"
    "🎁 *₹500 next service discount*\n\n"

    "Thank you bahut zyada! 🙏\n\n"

    "— {agent_name}\n"
    "{company_name}"
)


# ══════════════════════════════════════════════════════════════════
#  POST-REQUIREMENT PIPELINE MESSAGES
#  Stages: CALL_SCHEDULE → CONTRACT → PAYMENT → DEMO → DONE
# ══════════════════════════════════════════════════════════════════

# ── Call Schedule Message ──────────────────────────────────────────
CALL_SCHEDULE_MSG = (
    "📞 *{business_name} ji — Call Schedule Karte Hain!*\n\n"

    "Bahut accha! Ab next step hai ek quick call —\n"
    "Google Meet ya phone call, jo aapko suit kare! 😊\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "🗓️ *Available Slots:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "📌 *Monday - Saturday*\n"
    "  ⏰ 10:00 AM - 1:00 PM\n"
    "  ⏰ 3:00 PM - 7:00 PM\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "💬 *Call Mein Discuss Karenge:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "  ✅ Aapka exact requirement\n"
    "  ✅ Design preferences & colors\n"
    "  ✅ Timeline & delivery date\n"
    "  ✅ Payment process\n"
    "  ✅ Koi bhi sawal!\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Bas batao — *kab free hain?* 📅\n\n"

    "Reply karo:\n"
    "📌 *\"KAL 11AM\"* — Kal 11 baje\n"
    "📌 *\"ABHI\"* — Abhi call karo\n"
    "📌 *Apna time batao!*\n\n"

    "— {agent_name}\n"
    "{company_name} 🙏"
)

# ── Contract Terms Message ─────────────────────────────────────────
CONTRACT_TERMS_MSG = (
    "📝 *{business_name} ji — Agreement Terms*\n\n"

    "Call ke baad ab next step — agreement terms.\n"
    "Ye transparent rakhna chahte hain! 🤝\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "📋 *Project Details:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "📦 Package: *{package_name}*\n"
    "💰 Total Cost: *{price_display}*\n"
    "⚡ Delivery: *{delivery_time}*\n"
    "✏️ Revisions: *{revision_count} rounds*\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "💳 *Payment Terms:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Step 1️⃣ — *50% advance* (₹{advance_amount}) abhi\n"
    "Step 2️⃣ — Hum website banate hain\n"
    "Step 3️⃣ — Aap *review & approve* karo\n"
    "Step 4️⃣ — *50% balance* (₹{balance_amount}) pay karo\n"
    "Step 5️⃣ — Website *LIVE!* 🚀\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "🔐 *Our Guarantee:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "  ✅ Written agreement milega\n"
    "  ✅ {revision_count} revision rounds FREE\n"
    "  ✅ Demo pehle dikhayenge — phir payment\n"
    "  ✅ Free support period included\n"
    "  ✅ Not satisfied? Full refund before work starts\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Agar ye terms theek hain to reply karo:\n"
    "✅ *\"AGREE\"* — Terms accepted!\n"
    "❓ *\"QUESTION\"* — Kuch poochna hai\n\n"

    "— {agent_name}\n"
    "{company_name} 🙏"
)

# ── Payment Request Message ────────────────────────────────────────
PAYMENT_REQUEST_MSG = (
    "💰 *{business_name} ji — Payment Details*\n\n"

    "Bahut badhiya! Terms agreed! 🎉\n"
    "Ab bas *50% advance* de dijiye —\n"
    "aur hum kaam shuru karte hain! 🚀\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "💳 *Payment Details:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "📦 Package: *{package_name}*\n"
    "💰 Total: *{price_display}*\n"
    "💵 Advance (50%): *₹{advance_amount}*\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "📱 *UPI Payment:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "🔗 UPI ID: `{upi_id}`\n\n"

    "_(GPay • PhonePe • Paytm — sab chalega!)_\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "📋 *Payment Karne Ke Baad:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "  1️⃣ Payment karo UPI se\n"
    "  2️⃣ *Screenshot* yahan share karo\n"
    "  3️⃣ *\"PAID\"* reply karo\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Jaise hi payment confirm hoga —\n"
    "hum *turant kaam shuru* kar denge! ⚡\n\n"

    "— {agent_name}\n"
    "{company_name} 🙏"
)

# ── Demo In Progress Message ──────────────────────────────────────
DEMO_IN_PROGRESS_MSG = (
    "🎨 *{business_name} ji — Work Started!* 🚀\n\n"

    "Payment receive ho gaya — *shukriya!* 💚\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "⏱️ *Timeline:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "📦 Package: *{package_name}*\n"
    "⚡ Demo Ready In: *{delivery_time}*\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "📋 *Kya Hoga Ab:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "🟡 *Abhi* — Design work started\n"
    "🟡 *{delivery_time} mein* — Demo preview ready\n"
    "🟢 *Aap approve karo* — Website LIVE!\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Jab demo ready hoga, main yahan share\n"
    "karunga preview link. Tab review karna! 😊\n\n"

    "Reply karo jab demo aaye:\n"
    "🟢 *\"APPROVED\"* — Perfect hai!\n"
    "🔄 *\"CHANGES\"* — Kuch badalna hai\n\n"

    "— {agent_name}\n"
    "{company_name} 🙏"
)

# ── Project Started / Final Done Message ──────────────────────────
PROJECT_STARTED_MSG = (
    "🎉 *{business_name} ji — APPROVED!* 🚀\n\n"

    "Bahut badhiya! Demo approved ho gaya!\n"
    "Ab hum website ko *final LIVE* karte hain! 🌐\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "📋 *Next Steps:*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "  1️⃣ *Balance payment:* ₹{balance_amount}\n"
    "     UPI: `{upi_id}`\n"
    "  2️⃣ Website goes *LIVE!* 🌐\n"
    "  3️⃣ Login credentials share honge\n"
    "  4️⃣ Free support period starts\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Balance payment karte hi website\n"
    "*live kar denge!* ⚡\n\n"

    "{company_name} mein aapka swagat hai! 🙏\n\n"

    "— {agent_name}\n"
    "{company_name}"
)


# ══════════════════════════════════════════════════════════════════
#  FORMAT HELPERS
#  Keep these clean, well-documented, and easy to extend
# ══════════════════════════════════════════════════════════════════

def format_template(template: str, **kwargs) -> str:
    """
    Safely format any template string with auto-injected defaults.

    Auto-fills the following keys if not provided:
        agent_name, company_name, portfolio_url, upi_id

    Args:
        template: Template string with {variable} placeholders
        **kwargs: Variable key-value pairs to substitute

    Returns:
        Formatted string. Missing keys are left as {placeholder}.

    Example:
        msg = format_template(WELCOME_MESSAGE,
                              business_name="Sharma Ji Store",
                              business_type="Kirana Store",
                              review_count="150",
                              rating="4.5",
                              city="Thane")
    """
    defaults = {
        "agent_name":    AGENT_NAME,
        "company_name":  COMPANY_NAME,
        "portfolio_url": PORTFOLIO_URL,
        "upi_id":        UPI_ID,
    }
    merged = {**defaults, **kwargs}

    try:
        return template.format(**merged)
    except KeyError:
        return template.format_map(_SafeDict(merged))


def format_features_list(features: list[str], emoji: str = "✅") -> str:
    """
    Convert a list of features into WhatsApp-friendly bulleted format.

    Args:
        features: List of feature strings
        emoji:    Bullet emoji (default ✅)

    Returns:
        Multi-line string with emoji bullets

    Example:
        format_features_list(["Mobile optimized", "FREE domain"])
        → "✅ Mobile optimized\\n✅ FREE domain"
    """
    return "\n".join(f"  {emoji} {feature}" for feature in features)


def format_checklist(items: list[str]) -> str:
    """
    Format a checklist with number emojis (1️⃣, 2️⃣, etc.)

    Supports up to 10 items. Falls back to • for item 11+.

    Args:
        items: List of checklist item strings

    Returns:
        Multi-line numbered checklist string
    """
    number_emojis = [
        "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣",
        "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"
    ]
    lines = []
    for i, item in enumerate(items):
        bullet = number_emojis[i] if i < len(number_emojis) else "•"
        lines.append(f"  {bullet} {item}")
    return "\n".join(lines)


def format_separator(
    char: str = "━",
    length: int = 22,
    label: str = ""
) -> str:
    """
    Create a WhatsApp-friendly visual separator line.

    Args:
        char:   Separator character (default ━)
        length: Total character length (default 22)
        label:  Optional centered label text

    Returns:
        Separator string

    Examples:
        format_separator()          → "━━━━━━━━━━━━━━━━━━━━━━"
        format_separator(label="✅ Offer") → "━━ ✅ Offer ━━━━━━━"
    """
    if label:
        padding = max(0, length - len(label) - 2)
        left = char * (padding // 2)
        right = char * (padding - padding // 2)
        return f"{left} {label} {right}"
    return char * length


def get_template_by_stage(stage: str) -> str:
    """
    Return the appropriate template string based on conversation stage.

    Args:
        stage: One of 'welcome', 'follow_up_1', 'follow_up_2',
               'follow_up_3', 'follow_up_4', 'package',
               'interested', 'not_interested', 'delivery',
               'checkin', 'renewal', 'upsell'

    Returns:
        Template string for the given stage

    Raises:
        ValueError: If stage is not recognized
    """
    stage_map: dict[str, str] = {
        "welcome":         WELCOME_MESSAGE,
        "welcome_b":       WELCOME_MESSAGE_B,
        "welcome_c":       WELCOME_MESSAGE_C,
        "follow_up_1":     FOLLOW_UP_1,
        "follow_up_2":     FOLLOW_UP_2,
        "follow_up_3":     FOLLOW_UP_3,
        "package":         PACKAGE_RECOMMENDATION,
        "package_quick":   PACKAGE_QUICK_SUMMARY,
        "all_packages":    ALL_PACKAGES_COMPARISON,
        "interested":      INTERESTED_HANDOFF,
        "payment_rcvd":    PAYMENT_RECEIVED,
        "preview_ready":   WEBSITE_PREVIEW_READY,
        "not_interested":  NOT_INTERESTED_RESPONSE,
        "delivery":        WEBSITE_DELIVERY,
        "checkin":         CHECKIN_7_DAYS,
        "upsell":          UPSELL_30_DAYS,
        "renewal":         RENEWAL_REMINDER,
        "referral":        REFERRAL_REQUEST,
        "review":          GOOGLE_REVIEW_REQUEST,
        "festival":        FESTIVAL_CAMPAIGN,
        "industry":        INDUSTRY_CAMPAIGN,
        # Pipeline stages
        "call_schedule":   CALL_SCHEDULE_MSG,
        "contract":        CONTRACT_TERMS_MSG,
        "payment_request": PAYMENT_REQUEST_MSG,
        "demo_progress":   DEMO_IN_PROGRESS_MSG,
        "project_started": PROJECT_STARTED_MSG,
        # Objection handlers
        "obj_price":       OBJECTION_TOO_EXPENSIVE,
        "obj_trust":       OBJECTION_NOT_TRUSTWORTHY,
        "obj_has_site":    OBJECTION_HAVE_WEBSITE,
        "obj_time":        OBJECTION_NEED_TIME,
        "obj_discount":    OBJECTION_WANTS_DISCOUNT,
    }

    if stage not in stage_map:
        valid = ", ".join(f'"{k}"' for k in stage_map)
        raise ValueError(
            f"Unknown stage: '{stage}'. Valid stages: {valid}"
        )

    return stage_map[stage]


def build_message(
    stage: str,
    business_name: str,
    business_type: str = "",
    city: str = "Thane",
    **extra_vars,
) -> str:
    """
    Convenience function: fetch template by stage and auto-format it.

    Args:
        stage:         Conversation stage key (see get_template_by_stage)
        business_name: Client business name
        business_type: Type of business (e.g. 'Restaurant', 'Clinic')
        city:          Client city (default 'Thane')
        **extra_vars:  Any additional template variables

    Returns:
        Fully formatted WhatsApp message string

    Example:
        msg = build_message(
            stage="welcome",
            business_name="Sharma Sweets",
            business_type="Sweet Shop",
            city="Thane",
            review_count="230",
            rating="4.7"
        )
        print(msg)
    """
    template = get_template_by_stage(stage)
    return format_template(
        template,
        business_name=business_name,
        business_type=business_type,
        city=city,
        **extra_vars,
    )


class _SafeDict(dict):
    """
    Dict subclass that returns the original {key} placeholder
    for any missing key, preventing KeyError on partial formatting.
    """

    def __missing__(self, key: str) -> str:
        return f"{{{key}}}"


# ══════════════════════════════════════════════════════════════════
#  TEMPLATE REGISTRY — For programmatic access
#  Useful for A/B testing, analytics, and dynamic selection
# ══════════════════════════════════════════════════════════════════

TEMPLATE_REGISTRY: dict[str, dict] = {
    # WELCOME VARIANTS (A/B/C test these)
    "welcome_a": {
        "template":    WELCOME_MESSAGE,
        "description": "Generic cold outreach — No website detected",
        "stage":       "welcome",
        "variant":     "A",
        "best_for":    ["Restaurant", "Clinic", "Retail"],
    },
    "welcome_b": {
        "template":    WELCOME_MESSAGE_B,
        "description": "Competitor angle — High urgency",
        "stage":       "welcome",
        "variant":     "B",
        "best_for":    ["Real Estate", "Gym", "Education"],
    },
    "welcome_c": {
        "template":    WELCOME_MESSAGE_C,
        "description": "Local trust angle — Warm and personal",
        "stage":       "welcome",
        "variant":     "C",
        "best_for":    ["Small Shops", "Local Services", "Tailors"],
    },
    # FOLLOW-UPS
    "follow_up_1": {
        "template":    FOLLOW_UP_1,
        "description": "Day 1-2 follow-up with urgency + limited offer",
        "stage":       "follow_up",
        "send_after":  "24h",
    },
    "follow_up_2": {
        "template":    FOLLOW_UP_2,
        "description": "Day 3-4 pain point re-engagement",
        "stage":       "follow_up",
        "send_after":  "72h",
    },
    "follow_up_3": {
        "template":    FOLLOW_UP_3,
        "description": "Day 7 final breakup + free report offer",
        "stage":       "follow_up",
        "send_after":  "7d",
    },
}
