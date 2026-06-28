from datetime import datetime


def detect_brute_force(alerts):

    failed_ips = {}
    last_attempt = {}

    for alert in alerts:

        if alert["event"] == "Failed login":

            ip = alert["ip"]
            current_time = datetime.strptime(alert["time"], "%H:%M:%S")

            if ip not in last_attempt:
                last_attempt[ip] = current_time
            else:
                difference = current_time - last_attempt[ip]
                
                last_attempt[ip] = current_time

            if ip not in failed_ips:
                failed_ips[ip] = 1
            else:
                failed_ips[ip] += 1
    results = []
    for ip, count in failed_ips.items():

        

        if count >= 3:

            results.append({
                "attack": "Brute Force",
                "ip": ip,
                "failed_logins": count,
                "severity": "High"
})

        print("-------------------------")

    return results