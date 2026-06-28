def detect_port_scan(alerts):

    results = []

    for alert in alerts:

        if alert["event"] == "Port Scan":

            results.append({
    "attack": "Port Scan",
    "ip": alert["ip"],
    "severity": "Medium",
    "description": "Possible port scanning activity detected.",
    "recommendation": "Investigate the source IP and monitor network activity."
})

    return results