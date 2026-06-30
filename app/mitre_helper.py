def get_mitre_info(attack):

    mitre = {

        "Brute Force": {
            "id": "T1110",
            "tactic": "Credential Access",
            "description": "The attacker attempts multiple password combinations to gain unauthorized access.",
            "detection": "Review failed login events (Windows Event ID 4625).",
            "response": [
                "Block the source IP",
                "Enable MFA",
                "Reset compromised credentials",
                "Review authentication logs"
            ],
        "investigation": [
            "Review Windows Event ID 4625",
            "Count failed login attempts",
            "Identify targeted accounts",
            "Check if login succeeded after failures",
            "Search source IP in Threat Intelligence",
            "Verify MFA status"
        ]
        },

        "Port Scan": {
            "id": "T1046",
            "tactic": "Discovery",
            "description": "The attacker scans the network looking for open services and vulnerable hosts.",
            "detection": "Look for multiple connection attempts across many ports.",
            "response": [
                "Block scanning IP",
                "Review firewall logs",
                "Check exposed services",
                "Monitor for follow-up attacks"
            ],
            
            

        "investigation": [
                "Review firewall logs",
                "Identify scanned ports",
                "Check exposed services",
                "Search for exploitation attempts",
                "Review IDS/IPS alerts",
                "Determine scan type"
        ]
        }

    }

    return mitre.get(attack)