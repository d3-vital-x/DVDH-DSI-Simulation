# DVDH Live Signal Analysis Dashboard
# Streamlit Optimized Skeleton v1.0
# Purpose: Diagnostic-only observational geometry analysis
# License: MIT

import time
import random
import streamlit as st
import datetime
import math
import os
import smtplib
import ssl
from email.message import EmailMessage
from countdown import get_countdown_state
import requests
import hashlib

# =============================
# Page Configuration
# =============================
st.set_page_config(
    page_title="DVDH Live Signal Dashboard",
    layout="wide"
)

# =============================
# Header
# =============================
st.title("🌌 DVDH Live Signal Analysis Dashboard")
st.subheader("Transforming Theories, Illuminating Singularities")

st.markdown("""
**Scope Notice**  
Diagnostic visualization only.  
No observational or physical claims are asserted.
""")

st.divider()

# =============================
# Countdown
# =============================
@st.cache_data(ttl=60)
def countdown_state_cached():
    return get_countdown_state()

st.header("⏳ Observation Countdown")
state = countdown_state_cached()

if state["state"] == "PRE_WINDOW":
    st.metric("Status (UTC)", "PRE-WINDOW",
              f"{state['days_remaining']} days remaining")
elif state["state"] == "LIVE_WINDOW":
    st.success("🟢 Observation window LIVE (15–22 Feb 2026)")
else:
    st.info("🔵 Observation window closed")

st.divider()

# =============================
# Layout
# =============================
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 ΛCDM vs DVDH Accuracy Meter")
    st.progress(0.0)
    st.caption("Residual-based accuracy comparison (inactive placeholder)")

with col2:
    st.subheader("🧭 Θ_obs — DSI Projection Tracker")

    t1 = st.number_input("Δt₁ (ms)", min_value=0.1, value=10.0, step=0.1)
    t2 = st.number_input("Δt₂ (ms)", min_value=0.1, value=16.0, step=0.1)

    phi = (1 + math.sqrt(5)) / 2
    ratio = t2 / t1 if t1 > 0 else 0.0
    theta_obs = abs(ratio - phi)

    st.metric("Spike Ratio", f"{ratio:.4f}")
    st.metric("Golden Ratio φ", f"{phi:.4f}")
    st.metric("Θ_obs", f"{theta_obs:.6f}")

st.divider()

# =============================
# Email Configuration
# =============================
st.markdown("### 📧 Email Alert Configuration")

alert_threshold = st.number_input(
    "Alert if Θ_obs falls below:",
    min_value=0.0001,
    value=0.02,
    step=0.001,
    format="%.4f"
)

recipient_email = st.text_input("Recipient Email")

# Session State Init
if "last_alert_time" not in st.session_state:
    st.session_state.last_alert_time = None

if "last_telegram_alert" not in st.session_state:
    st.session_state.last_telegram_alert = None

# =============================
# Alert Functions
# =============================
def send_email_alert(theta_value):
    email_user = st.secrets["EMAIL_USER"]
    email_pass = st.secrets["EMAIL_PASS"]

    if not email_user or not email_pass:
        return False

    msg = EmailMessage()
    msg["Subject"] = "DVDH LIVE Θ Alert"
    msg["From"] = email_user
    msg["To"] = recipient_email

    msg.set_content(f"Θ_obs = {theta_value:.6f}")

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(email_user, email_pass)
            server.send_message(msg)
        return True
    except Exception:
        return False


def send_telegram_alert(theta_value):
    try:
        token = st.secrets["TELEGRAM_TOKEN"]
        chat_id = st.secrets["TELEGRAM_CHAT_ID"]
    except KeyError:
        return False

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    try:
        r = requests.post(
            url,
            json={"chat_id": chat_id,
                  "text": f"🚨 LIVE Θ Alert\nΘ_obs = {theta_value:.6f}"},
            timeout=2
        )
        return r.status_code == 200
    except Exception:
        return False


def anchor_theta_locally(theta_value):
    timestamp = datetime.datetime.utcnow().isoformat()
    raw = f"{timestamp}|{theta_value:.6f}"
    hash_digest = hashlib.sha256(raw.encode()).hexdigest()

    with open("theta_anchor_log.txt", "a") as f:
        f.write(f"{timestamp} | {theta_value:.6f} | {hash_digest}\n")

    return hash_digest


def verify_anchor_record(timestamp, theta_value, given_hash):
    raw = f"{timestamp}|{float(theta_value):.6f}"
    recalculated = hashlib.sha256(raw.encode()).hexdigest()
    return recalculated == given_hash, recalculated


# =============================
# LIVE Θ Tracker
# =============================
st.divider()
st.markdown("### 🔴 LIVE Θ Tracker")

live_mode = st.toggle("Enable LIVE Θ tracking", value=False)
live_placeholder = st.empty()

if live_mode:
    with live_placeholder.container():

        drift = random.uniform(-0.5, 0.5)
        t2_live = max(0.1, t2 + drift)

        ratio_live = t2_live / t1
        theta_live = abs(ratio_live - phi)

        st.metric("LIVE Θ_obs", f"{theta_live:.6f}")

        if theta_live < alert_threshold:

            now = datetime.datetime.utcnow()

            # Email Cooldown
            if (st.session_state.last_alert_time is None or
                (now - st.session_state.last_alert_time).total_seconds() >= 3600):

                if recipient_email and send_email_alert(theta_live):
                    st.session_state.last_alert_time = now
                    st.success("📧 Email sent")

            # Telegram Cooldown
            if (st.session_state.last_telegram_alert is None or
                (now - st.session_state.last_telegram_alert).total_seconds() >= 60):

                if send_telegram_alert(theta_live):
                    st.session_state.last_telegram_alert = now
                    st.success("📲 Telegram sent")

            # Blockchain Anchor
            hash_anchor = anchor_theta_locally(theta_live)
            st.caption(f"🔗 SHA256 Anchor: {hash_anchor[:16]}...")

        time.sleep(1.5)
        st.rerun()

else:
    st.caption("LIVE Θ tracker is paused.")

# =============================
# Verification Tool
# =============================
st.divider()
st.markdown("### 🔍 SHA256 Anchor Verification Tool")

verify_timestamp = st.text_input("Timestamp (ISO format)")
verify_theta = st.text_input("Θ_obs value")
verify_hash = st.text_input("Recorded SHA256 hash")

if st.button("Verify Anchor Record"):

    if verify_timestamp and verify_theta and verify_hash:

        valid, recalculated = verify_anchor_record(
            verify_timestamp,
            verify_theta,
            verify_hash
        )

        if valid:
            st.success("✅ Record VALID")
        else:
            st.error("❌ Hash mismatch detected")
            st.caption(f"Recalculated: {recalculated}")

    else:
        st.warning("Please fill all fields.")

# =============================
# Footer
# =============================
st.caption("DVDH–DSI Simulation Project • MIT License • Diagnostic Use Only")
