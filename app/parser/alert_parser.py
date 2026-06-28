from datetime import datetime
from app.parser.log_reader import read_logs
from app.detection.brute_force import detect_brute_force
from app.detection.port_scan import detect_port_scan
from app.report_generator import save_report
"""
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
"""
alerts = read_logs("sample_logs/failed_login.log")

"""

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
    """
results = []

results.extend(detect_brute_force(alerts))
results.extend(detect_port_scan(alerts))

for result in results:

    print("=" * 40)
    print("🚨 Attack:", result["attack"])
    print("IP:", result["ip"])
    print("Severity:", result["severity"])

    if "failed_logins" in result:
        print("Failed Logins:", result["failed_logins"])

    print("Description:", result["description"])
    print("Recommendation:", result["recommendation"])    
    
save_report(results)
