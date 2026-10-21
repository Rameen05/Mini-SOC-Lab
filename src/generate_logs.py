import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

random.seed(42)

OUTPUT = Path("data/auth_logs.csv")
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

start = datetime(2026, 10, 20, 8, 0, 0)
events = []

users = ["jlee", "mchen", "arivera", "admin", "tpatel"]
ips = ["192.0.2.10", "192.0.2.11", "198.51.100.20"]

# Generate ordinary login activity
for i in range(80):
    timestamp = start + timedelta(minutes=random.randint(0, 600))
    events.append({
        "timestamp": timestamp,
        "username": random.choice(users),
        "source_ip": random.choice(ips),
        "event_type": random.choices(
            ["SUCCESS", "FAILURE"], weights=[85, 15]
        )[0],
        "hostname": random.choice(
            ["WORKSTATION-01", "WORKSTATION-02"]
        ),
        "country": "US"
    })

# Simulate repeated failed logins
attack_ip = "203.0.113.77"
attack_start = start + timedelta(hours=3)

for i in range(15):
    events.append({
        "timestamp": attack_start + timedelta(minutes=i),
        "username": random.choice(["admin", "jlee", "mchen"]),
        "source_ip": attack_ip,
        "event_type": "FAILURE",
        "hostname": "WORKSTATION-01",
        "country": "Unknown"
    })

# Simulate a successful login after the failures
events.append({
    "timestamp": attack_start + timedelta(minutes=16),
    "username": "admin",
    "source_ip": attack_ip,
    "event_type": "SUCCESS",
    "hostname": "WORKSTATION-01",
    "country": "Unknown"
})

events.sort(key=lambda event: event["timestamp"])

with OUTPUT.open("w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=events[0].keys())
    writer.writeheader()

    for event in events:
        row = event.copy()
        row["timestamp"] = row["timestamp"].isoformat(sep=" ")
        writer.writerow(row)

print(f"Created {len(events)} simulated events: {OUTPUT}")
