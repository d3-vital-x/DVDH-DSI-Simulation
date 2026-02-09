# dashboard/countdown.py
# Diagnostic Time Window Controller
# Scope: Visualization & scheduling only (no observational claim)

from datetime import datetime, timezone

# === Fixed Diagnostic Window (UTC) ===
START_DATE = datetime(2026, 2, 15, 0, 0, 0, tzinfo=timezone.utc)
END_DATE   = datetime(2026, 2, 22, 23, 59, 59, tzinfo=timezone.utc)

def get_countdown_state(now=None):
    """
    Returns dashboard-safe time state.
    States:
      - PRE_WINDOW
      - LIVE_WINDOW
      - POST_WINDOW
    """
    now = now or datetime.now(timezone.utc)

    if now < START_DATE:
        delta = START_DATE - now
        return {
            "state": "PRE_WINDOW",
            "days_remaining": delta.days,
            "seconds_remaining": int(delta.total_seconds())
        }

    if START_DATE <= now <= END_DATE:
        delta = END_DATE - now
        return {
            "state": "LIVE_WINDOW",
            "days_remaining": delta.days,
            "seconds_remaining": int(delta.total_seconds())
        }

    return {
        "state": "POST_WINDOW",
        "days_remaining": 0,
        "seconds_remaining": 0
    }
