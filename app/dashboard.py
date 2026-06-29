import streamlit as st

st.set_page_config(
    page_title="SOCPilot",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ SOCPilot Dashboard")

st.subheader("📊 Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Alerts", 2)

with col2:
    st.metric("High Severity", 1)

with col3:
    st.metric("Medium Severity", 1)


st.subheader("🚨 Detected Incidents")

data = [
    {
        "Attack": "Brute Force",
        "IP": "192.168.1.10",
        "Severity": "High"
    },
    {
        "Attack": "Port Scan",
        "IP": "192.168.1.50",
        "Severity": "Medium"
    }
]

st.table(data)