from datetime import datetime
alerts = [
    {
        "time": "10:00:01",
        "ip": "192.168.1.10",
        "event": "Failed login"
    },

    {
        "time": "10:00:08",
        "ip": "192.168.1.10",
        "event": "Failed login"
    },

    {
        "time": "10:00:15",
        "ip": "192.168.1.10",
        "event": "Failed login"
    },

    {
        "time": "10:05:00",
        "ip": "192.168.1.15",
        "event": "User login"
    }
]


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
            print("Time Difference:", difference)
            print("Seconds:", difference.total_seconds())
            last_attempt[ip] = current_time

        if ip not in failed_ips:
            failed_ips[ip] = 1
        else:
            failed_ips[ip] += 1

for ip, count in failed_ips.items():

    print("IP:", ip)
    print("Failed Logins:", count)

    if count >= 3:
        print("🚨 Possible Brute Force Attack")

    print("----------------------")
    alerts_from_file = []
    log_file = open("sample_logs/failed_login.log", "r")

for line in log_file:
    parts = line.strip().split(",")
    time = parts[0]
    ip = parts[1]
    event = parts[2]

    alert = {
    "time": time,
    "ip": ip,
    "event": event
}

    alerts_from_file.append(alert)

log_file.close()

print(alerts_from_file)
    
