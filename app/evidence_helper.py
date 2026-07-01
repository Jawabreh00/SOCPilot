def get_evidence(attack):

    evidence = {

        "Brute Force": [
            "Multiple failed login attempts detected.",
            "Repeated authentication failures from the same source IP.",
            "Events occurred within a short time window.",
            "Pattern matches MITRE ATT&CK T1110."
        ],

        "Port Scan": [
            "Multiple destination ports were scanned.",
            "High connection rate detected.",
            "Sequential scanning behavior observed.",
            "Pattern matches MITRE ATT&CK T1046."
        ]

    }

    return evidence.get(
        attack,
        ["No supporting evidence available."]
    )
