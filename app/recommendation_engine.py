def get_next_action(attack, risk):

    if attack == "Brute Force":

        if risk >= 8:
            return "Review Windows Event ID 4625 before blocking the source IP."

        elif risk >= 5:
            return "Verify whether any successful login (Event ID 4624) occurred."

        else:
            return "Continue monitoring authentication logs."


    elif attack == "Port Scan":

        if risk >= 8:
            return "Identify exposed services before blocking the scanning IP."

        elif risk >= 5:
            return "Check firewall and IDS alerts for additional activity."

        else:
            return "Continue monitoring network activity."


    return "Continue investigation."