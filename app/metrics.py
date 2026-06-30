import streamlit as st


def show_metrics(data):

    total_alerts = len(data)

    high_alerts = sum(
        1 for incident in data
        if "High" in incident["Severity"]
    )

    medium_alerts = sum(
        1 for incident in data
        if "Medium" in incident["Severity"]
    )

    low_alerts = sum(
        1 for incident in data
        if "Low" in incident["Severity"]
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Alerts", total_alerts)

    with col2:
        st.metric("🔴 High", high_alerts)

    with col3:
        st.metric("🟠 Medium", medium_alerts)

    with col4:
        st.metric("🟢 Low", low_alerts)