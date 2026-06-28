from datetime import datetime

def save_report(results):

    with open("reports/incident_report.txt", "w") as report:

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

            report.write("\n")
            report.write("-" * 40 + "\n\n")