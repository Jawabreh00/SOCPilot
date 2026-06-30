import streamlit as st
import pandas as pd
import plotly.express as px

def show_analytics(data):

    df = pd.DataFrame(data)

    if df.empty:
        return

    st.divider()
    st.subheader("📈 Analytics")

    attack_counts = (
        df["Attack"]
        .value_counts()
        .reset_index()
    )
    attack_counts.columns = ["Attack", "Count"]

    severity_counts = (
        df["Severity"]
        .value_counts()
        .reset_index()
    )
    severity_counts.columns = ["Severity", "Count"]
    

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### Attack Distribution")

        fig_attack = px.bar(
            attack_counts,
            x="Attack",
            y="Count",
            text="Count",
            color="Attack",
            color_discrete_map={
                "Brute Force": "#ef4444",
                "Port Scan": "#3b82f6",
                "Malware": "#8b5cf6",
                "SQL Injection": "#f59e0b"
    }
)
        fig_attack.update_layout(
            template="plotly_dark",
            xaxis_title="",
            yaxis_title="Alerts",
            showlegend=False,
            height=350
            
)

        fig_attack.update_traces(
            textposition="outside"
)

        st.plotly_chart(fig_attack, use_container_width=True)

    with col2:

        st.markdown("### Severity Distribution")
        severity_counts["Severity"] = severity_counts["Severity"].str.strip()

        fig_severity = px.bar(
            severity_counts,
            x="Severity",
            y="Count",
            text="Count",
            color="Severity",
           color_discrete_map={
               "🔴 High": "#dc2626",
               "🟡 Medium": "#f59e0b",
               "🟢 Low": "#22c55e",
}
    )

        fig_severity.update_layout(
            template="plotly_dark",
            xaxis_title="",
            yaxis_title="Alerts",
            showlegend=False,
            height=350
)
        fig_severity.update_traces(
            textposition="outside"
)

        st.plotly_chart(fig_severity, use_container_width=True)