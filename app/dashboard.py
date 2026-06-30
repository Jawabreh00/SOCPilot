import streamlit as st

from ai_copilot import show_ai_copilot
from report_reader import read_latest_report
from metrics import show_metrics

st.set_page_config(
    page_title="SOCPilot",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ SOCPilot Dashboard")

st.subheader("📊 Statistics")

data = read_latest_report()
st.sidebar.header("🔎 Filters")

severity_filter = st.sidebar.multiselect(
    "Severity",
    ["🔴 High", "🟠 Medium", "🟢 Low"],
    default=["🔴 High", "🟠 Medium", "🟢 Low"]
)

attack_types = sorted(list(set(item["Attack"] for item in data)))

attack_filter = st.sidebar.multiselect(
    "Attack Type",
    attack_types,
    default=attack_types
)

ip_search = st.sidebar.text_input("Search IP")
filtered_data = []

for incident in data:

    if incident["Attack"] not in attack_filter:
        continue

    severity = incident["Severity"]

    if "High" in severity:
        severity_name = "🔴 High"

    elif "Medium" in severity:
        severity_name = "🟠 Medium"

    else:
        severity_name = "🟢 Low"

    if severity_name not in severity_filter:
        continue

    if ip_search and ip_search not in incident["IP"]:
        continue

    filtered_data.append(incident)

data = filtered_data
selected_alert = st.sidebar.selectbox(
    "🎯 Select Alert",
    range(len(data)),
    format_func=lambda i: f"{data[i]['Attack']} - {data[i]['IP']}"
)

current_alert = data[selected_alert]
show_metrics(data)
st.divider()
show_ai_copilot([current_alert])
st.subheader("🚨 Detected Incidents")
st.divider()
st.table(data)
st.divider()

