import os
import glob


def read_latest_report():

    report_files = glob.glob("reports/incident_*.txt")

    if not report_files:
        return []

    latest = max(report_files, key=os.path.getctime)

    incidents = []

    with open(latest, "r") as file:
        lines = file.readlines()

    incident = {}

    for line in lines:

        line = line.strip()

        if line.startswith("Attack:"):
            incident["Attack"] = line.replace("Attack:", "").strip()

        elif line.startswith("IP:"):
            incident["IP"] = line.replace("IP:", "").strip()

        elif line.startswith("Severity:"):
            incident["Severity"] = line.replace("Severity:", "").strip()
            if incident["Severity"] == "High":
                incident["Severity"] = "🔴 High"

            elif incident["Severity"] == "Medium":
                incident["Severity"] = "🟡 Medium"

            elif incident["Severity"] == "Low":
                 incident["Severity"] = "🟢 Low"

        elif line.startswith("MITRE Technique:"):

             incident["MITRE"] = line.replace("MITRE Technique:", "").strip()    

        elif line.startswith("--------------------------------------"):
            if incident:
                incidents.append(incident)
                incident = {}

    return incidents