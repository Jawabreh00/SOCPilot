def get_checklist(attack):

    checklists = {

        "Brute Force": [

            "Is the source IP internal?",

            "Review Windows Event ID 4625.",

            "Did any login eventually succeed?",

            "Check if MFA is enabled.",

            "Has this IP attacked before?",

            "Is the account locked?"
        ],

        "Port Scan": [

            "Is the scanner authorized?",

            "Is the IP internal?",

            "Were many ports scanned?",

            "Check Firewall logs.",

            "Check IDS/IPS alerts.",

            "Has this IP scanned before?"
        ]

    }

    return checklists.get(attack, [])