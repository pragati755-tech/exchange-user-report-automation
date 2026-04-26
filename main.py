import json
import csv

count = 0                 # active users
Inactive = []
ITE3 = []
Gmail = []
total_users = 0

with open("exchange_users.csv", "r") as file:
    csv_reader = csv.DictReader(file)

    for line in csv_reader:
        total_users += 1

        login_days = int(line["last_login_days"])
        email = line["email"]

        # Active users
        if login_days <= 30:
            count += 1

        # Inactive users
        if login_days > 30:
            Inactive.append({
                "name": line["name"],
                "email": line["email"]
            })

        # IT E3 users
        if line["department"] == "IT" and line["license"] == "E3":
            ITE3.append(line["name"])

        # Gmail users
        if email.endswith("@gmail.com"):
            username = email.split("@")[0]
            Gmail.append(username)

# Write inactive users CSV
with open("Inactive.csv", "w", newline="") as newfile:
    csv_writer = csv.DictWriter(newfile, fieldnames=["name", "email"])

    csv_writer.writeheader()

    for row in Inactive:
        csv_writer.writerow(row)

# JSON summary
summary = {
    "total_users": total_users,
    "active_users": count,
    "inactive_users": len(Inactive),
    "gmail_users": len(Gmail)
}

with open("summary.json", "w") as file:
    json.dump(summary, file, indent=4)

# Output
print("IT E3 Users:", ITE3)
print("Gmail Users:", Gmail)
print(summary)
