# DVDH Live Signal Analysis Dashboard
# Production Hardened Version
# Hybrid Model: φ-weighted Sine + Logistic Map Noise
# License: MIT

import time
import streamlit as st
import datetime
import math
import smtplib
import ssl
import requests
import hashlib
from email.message import EmailMessage

# Optional external module protection
try:
    from countdown import get_countdown_state
    COUNTDOWN_AVAILABLE = True
except Exception:
    COUNTDOWN_AVAILABLE = False


# =============================
# Page Configuration
# =============================
st.set_page_config(
    page_title="DVDH Live Signal Dashboard",
    layout="wide"
)

st.title("🌌 DVDH Live Signal Analysis Dashboard")
st.subheader("Hybrid Harmonic Diagnostic System")

st.markdown("""
**Scope Notice**  
Diagnostic visualization only.  
No physical or observational claims are asserted.
""")

st.divider()


# =============================
# Safe Countdown Section
# =============================
st.header("⏳ Observation Countdown")

if COUNTDOWN_AVAILABLE:
    @st.cache_data(ttl=60)
    def countdown_state_cached():
        return get_countdown_state()

    try:
        state = countdown_state_cached()

        if state["state"] == "PRE_WINDOW":
            st.metric("Status (UTC)", "PRE-WINDOW",
                      f"{state['days_remaining']} days remaining")
        elif state["state"] == "LIVE_WINDOW":
            st.success("🟢 Observation window LIVE")
        else:
            st.info("🔵 Observation window closed")

    except Exception as e:
        st.warning(f"Countdown error: {e}")
else:
    st.info("Countdown module not available.")

st.divider()


# =============================
# Core Inputs
# =============================
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Accuracy Meter")
    st.progress(0.0)
    st.caption("Residual placeholder")

with col2:
    st.subheader("🧭 Θ_obs Tracker")

    t1 = st.number_input("Δt₁ (ms)", min_value=0.1, value=10.0)
    t2 = st.number_input("Δt₂ (ms)", min_value=0.1, value=16.0)

    phi = (1 + math.sqrt(5)) / 2
    ratio = t2 / t1 if t1 > 0 else 0.0
    theta_obs = abs(ratio - phi)

    st.metric("Spike Ratio", f"{ratio:.4f}")
    st.metric("Golden Ratio φ", f"{phi:.4f}")
    st.metric("Θ_obs", f"{theta_obs:.6f}")

st.divider()


# =============================
# Alert Configuration
# =============================
st.markdown("### 📧 Alert Configuration")

alert_threshold = st.number_input(
    "Alert if Θ_obs below:",
    min_value=0.0001,
    value=0.02,
    format="%.4f"
)

recipient_email = st.text_input("Recipient Email")

if "last_email" not in st.session_state:
    st.session_state.last_email = None

if "last_telegram" not in st.session_state:
    st.session_state.last_telegram = None


# =============================
# Hybrid Drift Engine
# =============================
if "logistic_x" not in st.session_state:
    st.session_state.logistic_x = 0.6180339887

if "time_step" not in st.session_state:
    st.session_state.time_step = 0


def hybrid_drift():
    A = 0.05
    phi = (1 + math.sqrt(5)) / 2
    t = st.session_state.time_step

    sine_part = A * math.sin(2 * math.pi * phi * t)

    r = 3.99
    x = st.session_state.logistic_x
    x_next = r * x * (1 - x)
    st.session_state.logistic_x = x_next

    noise = (x_next - 0.5) * 0.02

    st.session_state.time_step += 1
    return sine_part + noise


# =============================
# Safe Email Function
# =============================
def send_email_alert(theta_value):

    email_user = st.secrets.get("EMAIL_USER")
    email_pass = st.secrets.get("EMAIL_PASS")

    if not email_user or not email_pass:
        st.warning("Email credentials not configured.")
        return False

    if not recipient_email:
        return False

    msg = EmailMessage()
    msg["Subject"] = "DVDH Θ Alert"
    msg["From"] = email_user
    msg["To"] = recipient_email
    msg.set_content(f"Theta detected: {theta_value:.6f}")

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(email_user, email_pass)
            server.send_message(msg)
        return True
    except Exception as e:
        st.error(f"Email error: {e}")
        return False


# =============================
# Safe Telegram Function
# =============================
def send_telegram_alert(theta_value):

    token = st.secrets.get("TELEGRAM_TOKEN")
    chat_id = st.secrets.get("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        return False

    try:
        r = requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": f"🚨 LIVE Θ Alert\nΘ_obs = {theta_value:.6f}"
            },
            timeout=5
        )
        return r.status_code == 200
    except Exception as e:
        st.error(f"Telegram error: {e}")
        return False


# =============================
# Safe SHA256 Anchor
# =============================
def anchor_theta(theta_value):

    try:
        timestamp = datetime.datetime.utcnow().isoformat() + "Z"
        raw = f"{timestamp}|{theta_value:.6f}"
        digest = hashlib.sha256(raw.encode()).hexdigest()

        with open("theta_anchor_log.txt", "a") as f:
            f.write(f"{timestamp} | {theta_value:.6f} | {digest}\n")

        return digest
    except Exception as e:
        st.error(f"Anchor write error: {e}")
        return None


# =============================
# LIVE Tracker
# =============================
st.divider()
st.markdown("### 🔴 LIVE Θ Tracker")

live = st.toggle("Enable LIVE tracking", value=False)
placeholder = st.empty()

if live:
    with placeholder.container():

        drift = hybrid_drift()
        t2_live = max(0.1, t2 + drift)

        ratio_live = t2_live / t1
        theta_live = abs(ratio_live - phi)

        st.metric("LIVE Θ_obs", f"{theta_live:.6f}")

        if theta_live < alert_threshold:

            now = datetime.datetime.utcnow()

            if (st.session_state.last_email is None or
               (now - st.session_state.last_email).total_seconds() >= 3600):

                if send_email_alert(theta_live):
                    st.session_state.last_email = now
                    st.success("Email sent")

            if (st.session_state.last_telegram is None or
               (now - st.session_state.last_telegram).total_seconds() >= 60):

                if send_telegram_alert(theta_live):
                    st.session_state.last_telegram = now
                    st.success("Telegram sent")

            hash_val = anchor_theta(theta_live)
            if hash_val:
                st.caption(f"SHA256: {hash_val[:16]}...")

        time.sleep(1.5)
        st.rerun()

else:
    st.caption("LIVE tracker paused.")


# =============================
# Footer
# =============================
st.caption("DVDH Hybrid Simulation • Production Hardened • MIT License")
