import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import random

model = joblib.load("model.pkl")

st.set_page_config(
    page_title="Cyber Threat Detection",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Cyber Threat Detection Dashboard")

# Dashboard Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Requests", "1250")

with col2:
    st.metric("Detected Attacks", "320")

with col3:
    st.metric("Normal Traffic", "930")

st.divider()

# User Input
st.subheader("Traffic Analysis")

duration = st.number_input("Duration", min_value=0)

src_bytes = st.number_input("Source Bytes", min_value=0)

dst_bytes = st.number_input("Destination Bytes", min_value=0)

severity = 0

if st.button("Predict"):

    sample = pd.DataFrame(
        [[duration, src_bytes, dst_bytes]],
        columns=["duration", "src_bytes", "dst_bytes"]
    )

    prediction = model.predict(sample)

    severity = min(
        int((duration + src_bytes + dst_bytes) / 200),
        100
    )

    if prediction[0] == "attack":
        st.error("🔴 Attack Traffic Detected")
    else:
        st.success("🟢 Normal Traffic")

    st.subheader("Threat Severity Meter")

    st.progress(severity)

    st.write(f"Severity Score: {severity}/100")

st.divider()

# Real-Time Traffic Trend Graph
st.subheader("📈 Real-Time Traffic Trend")

traffic_data = pd.DataFrame({
    "Time": list(range(1, 21)),
    "Traffic": [random.randint(50, 500) for _ in range(20)]
})

fig = px.line(
    traffic_data,
    x="Time",
    y="Traffic",
    title="Network Traffic Trend"
)

st.plotly_chart(fig, use_container_width=True)

# Pie Chart
st.subheader("📊 Attack vs Normal Traffic")

pie_data = pd.DataFrame({
    "Type": ["Normal", "Attack"],
    "Count": [930, 320]
})

fig2 = px.pie(
    pie_data,
    names="Type",
    values="Count",
    title="Traffic Distribution"
)

st.plotly_chart(fig2, use_container_width=True)