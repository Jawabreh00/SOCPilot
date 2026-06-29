from datetime import datetime
from app.detection.mitre_mapper import get_mitre_info



def save_report(results):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"reports/incident_{timestamp}.txt"

    with open(filename, "w") as report:

        report.write("SOCPilot Incident Report\n")
        report.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
)
        report.write("=" * 40 + "\n\n")

        for result in results:

            report.write(f"Attack: {result['attack']}\n")
            report.write(f"IP: {result['ip']}\n")
            report.write(f"Severity: {result['severity']}\n")

            if "failed_logins" in result:
                report.write(f"Failed Logins: {result['failed_logins']}\n")

            report.write(f"Description: {result['description']}\n")
            report.write(f"Recommendation: {result['recommendation']}\n")
            mitre = get_mitre_info(result["attack"])

            if mitre:
                report.write(f"MITRE Technique: {mitre['technique']}\n")
                report.write(f"MITRE Name: {mitre['name']}\n")

            report.write("\n")
            report.write("-" * 40 + "\n\n")

    print(f"Report saved: {filename}")        