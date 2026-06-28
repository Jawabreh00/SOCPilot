failed_count = 0

alerts = [
    "User login",
    "Failed login from 192.168.1.10",
    "Failed login from 192.168.1.10",
    "User logout",
    "Failed login from 192.168.1.10",
    "Password changed"
]

for alert in alerts:

    print("Analyzing:", alert)
    if "Failed login" in alert:
        failed_count += 1

print("----------------------")
print("Total Failed Logins:", failed_count)