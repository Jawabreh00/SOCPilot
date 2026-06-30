def analyze_alert(alert, checks=None):
    if checks is None:
            checks = {}
    attack = alert["Attack"]
    severity = alert["Severity"]

    confidence = 70
    risk = 5.0
    verdict = "Suspicious Activity"

    if attack == "Brute Force":
        confidence = 96
        risk = 9.5
        verdict = "Likely True Positive"

    elif attack == "Port Scan":
        confidence = 72
        risk = 5.8
        verdict = "Suspicious Activity"

    if "High" in severity:
        risk += 0.5

    elif "Low" in severity:
        risk -= 1

    risk = min(risk, 10)

    return {
        "confidence": confidence,
        "risk": round(risk,1),
        "verdict": verdict
    }