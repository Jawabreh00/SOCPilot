def read_logs(file_path):

    alerts = []

    with open(file_path, "r") as log_file:

        for line in log_file:

            parts = line.strip().split(",")

            alert = {
                "time": parts[0],
                "ip": parts[1],
                "event": parts[2]
            }

            alerts.append(alert)

    return alerts

