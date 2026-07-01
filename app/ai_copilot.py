import streamlit as st
from mitre_helper import get_mitre_info
from risk_engine import analyze_alert
from checklist_helper import get_checklist
from recommendation_engine import get_next_action


def show_ai_copilot(data):

    if not data:
        st.warning("No alerts available.")
        return

    current = data[0]

    mitre = get_mitre_info(current["Attack"])
    risk = 10.0
    confidence = 96

    status = "Likely True Positive"

    checklist = get_checklist(current["Attack"])
    checks = {}
    analysis = analyze_alert(current, checks)
    if analysis["risk"] >= 8:
        next_action = "Immediately isolate the affected host and begin incident response."

    elif analysis["risk"] >= 5:
        next_action = "Continue investigating the alert and collect additional evidence."

    else:
        next_action = "Monitor the alert. No immediate action is required."
    next_action = get_next_action(
        current["Attack"],
        analysis["risk"]
)    

    st.subheader("🤖 AI Security Copilot")

    col1, col2 = st.columns([2, 1])

    with col1:

        st.metric("Attack Type", current["Attack"])
        st.metric("Severity", current["Severity"])
        st.metric("Source IP", current["IP"])

        if mitre:

            st.divider()
            st.subheader("🛡 MITRE Intelligence")

            c1, c2 = st.columns([1, 2])

            with c1:
                st.metric("Technique", mitre["id"])
                st.metric("Tactic", mitre["tactic"])

            with c2:
                st.info(mitre["description"])

            st.markdown("### Detection Tips")
            st.warning(mitre["detection"]) 

    

    st.divider()

    

    st.subheader("📝 AI Summary")

    st.info(f"""
Attack Type: {current["Attack"]}

Source IP: {current["IP"]}

Severity: {current["Severity"]}

The observed behavior is consistent with this attack type.

The analyst should verify authentication logs and confirm whether the activity is malicious.
""")
    st.subheader("☑ False Positive Checklist")

    checks = {}

    for item in checklist:
        checks[item] = st.checkbox(item)

    analysis = analyze_alert(current, checks)
    with col2:

        st.metric("Confidence", f"{analysis['confidence']}%")
        st.metric("Risk Score", f"{analysis['risk']} / 10")
        st.metric("Status", analysis["verdict"])
    st.subheader("🧠 AI Verdict")


    if analysis["risk"] >= 8:
        st.success(f"""
    {analysis['verdict']}

    This alert is highly likely to represent malicious activity.
    Immediate investigation is recommended. 
    """)

    elif analysis["risk"] >= 5:
        st.warning(f"""
    {analysis['verdict']}

    This activity appears suspicious.
    Additional investigation is recommended.
    """)

    else:
        st.info(f"""
    {analysis['verdict']}

This alert currently has a low risk score.
Monitor the activity before taking action.
""")
    st.subheader("🎯 Next Best Action")
    st.warning(next_action)

    st.subheader("🔎 Investigation Guide")

    if mitre:
       for step in mitre["investigation"]:
          st.info(step)
    st.subheader("🔍 Extracted Indicators (IOCs)")

    ioc1, ioc2 = st.columns(2)

    with ioc1:
        st.code(f"Source IP: {current['IP']}")
        st.code(f"Attack Type: {current['Attack']}")

    with ioc2:
        if "MITRE Technique" in current:
            st.code(f"MITRE: {current['MITRE Technique']}")

        st.code(f"Severity: {current['Severity']}")

    if mitre:

            st.subheader("✅ Response Playbook")

            for action in mitre["response"]:
                st.success(action)