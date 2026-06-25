import streamlit as st
from streamlit_autorefresh import st_autorefresh
import random
import time
import pandas as pd

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="Real-Time AI Dashboard", layout="wide")

st.title("🚀 Real-Time AI Monitoring Dashboard")

# =========================
# AUTO REFRESH (1 second)
# =========================
st_autorefresh(interval=1000, limit=None, key="refresh")

# =========================
# SIMULATED LIVE DATA
# =========================
cpu = random.randint(10, 100)
memory = random.randint(20, 95)
traffic = random.randint(100, 1000)
threat_score = random.randint(1, 100)

# Threat Level Logic
if threat_score < 40:
    threat_level = "🟢 Low"
elif threat_score < 75:
    threat_level = "🟡 Medium"
else:
    threat_level = "🔴 High"

# =========================
# DASHBOARD CARDS
# =========================
col1, col2, col3, col4 = st.columns(4)

col1.metric("CPU Usage", f"{cpu}%")
col2.metric("Memory Usage", f"{memory}%")
col3.metric("Network Traffic", traffic)
col4.metric("Threat Level", threat_level)

st.write("⏱ Last Updated:", time.strftime("%H:%M:%S"))

# =========================
# TRAFFIC TREND (LIVE GRAPH)
# =========================
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame({
        "time": [],
        "traffic": []
    })

# append new data
new_row = pd.DataFrame({
    "time": [time.strftime("%H:%M:%S")],
    "traffic": [traffic]
})

st.session_state.data = pd.concat([st.session_state.data, new_row]).tail(20)

st.subheader("📊 Real-Time Traffic Trend")

st.line_chart(
    st.session_state.data.set_index("time")
)

# =========================
# THREAT METER (BAR STYLE)
# =========================
st.subheader("⚠ Threat Severity Meter")

st.progress(threat_score)

st.write(f"Threat Score: **{threat_score}/100**")

# =========================
# ALERT SYSTEM
# =========================
if threat_score > 75:
    st.error("🚨 HIGH THREAT DETECTED!")
elif threat_score > 40:
    st.warning("⚠ Medium Risk Detected")
else:
    st.success("✅ System Stable")

# =========================
# FOOTER
# =========================
st.caption("Real-Time AI Dashboard | Updates every 1 second")