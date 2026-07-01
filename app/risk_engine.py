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

    # False Positive Adjustments

    if checks.get("Is the source IP internal?"):
        risk -= 1.5
        confidence -= 8

    if checks.get("Did any login eventually succeed?"):
        risk += 1
        confidence += 3

    if checks.get("Check if MFA is enabled."):
        risk -= 1
        confidence -= 5

    if checks.get("Has this IP attacked before?"):
        risk += 1
        confidence += 4

    if checks.get("Is the account locked?"):
        risk -= 0.5    

    risk = max(0, min(risk, 10))
    confidence = max(0, min(confidence, 100))
    if risk >= 8:
        verdict = "Likely True Positive"
    elif risk >= 5:
        verdict = "Needs Investigation"

    else:
        verdict = "Likely False Positive"
    return {
        "confidence": confidence,
        "risk": round(risk,1),
        "verdict": verdict
        }