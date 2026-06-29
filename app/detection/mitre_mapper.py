MITRE_ATTACKS = {
    "Brute Force": {
        "technique": "T1110",
        "name": "Brute Force"
    },

    "Port Scan": {
        "technique": "T1046",
        "name": "Network Service Discovery"
    }
}

def get_mitre_info(attack_name):
    return MITRE_ATTACKS.get(attack_name)