import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA = Path("data/auth_logs.csv")
OUTPUT = Path("outputs")
OUTPUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA, parse_dates=["timestamp"])

required = {
    "timestamp", "username", "source_ip",
    "event_type", "hostname", "country"
}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Missing required columns: {missing}")

df = df.dropna(subset=["timestamp", "username", "source_ip"])
df["event_type"] = df["event_type"].str.upper()
df = df[df["event_type"].isin(["SUCCESS", "FAILURE"])]

print("\n=== INVESTIGATION SUMMARY ===")
print(f"Total events: {len(df)}")
print("\nEvents by type:")
print(df["event_type"].value_counts())

failures = df[df["event_type"] == "FAILURE"]

failed_by_ip = failures.groupby("source_ip").size().sort_values(ascending=False)
print("\nTop source IPs by failed logins:")
print(failed_by_ip.head(10))

failed_by_user = failures.groupby("username").size().sort_values(ascending=False)
print("\nAccounts with most failed logins:")
print(failed_by_user.head(10))

threshold = 5
flagged_ips = failed_by_ip[failed_by_ip >= threshold]

print(f"\nIPs with at least {threshold} failures:")
print(flagged_ips if not flagged_ips.empty else "None found")

suspicious = []

for ip in flagged_ips.index:
    ip_events = df[df["source_ip"] == ip].sort_values("timestamp")
    success_events = ip_events[ip_events["event_type"] == "SUCCESS"]

    if not success_events.empty:
        first_success = success_events.iloc[0]
        prior_failures = ip_events[
            (ip_events["event_type"] == "FAILURE") &
            (ip_events["timestamp"] < first_success["timestamp"])
        ]

        if not prior_failures.empty:
            suspicious.append({
                "source_ip": ip,
                "successful_username": first_success["username"],
                "success_time": first_success["timestamp"],
                "prior_failure_count": len(prior_failures)
            })

timeline = pd.DataFrame(suspicious)
timeline.to_csv(OUTPUT / "success_after_failures.csv", index=False)

failed_by_ip.rename("failed_attempts").to_csv(
    OUTPUT / "failed_logins_by_ip.csv"
)
failed_by_user.rename("failed_attempts").to_csv(
    OUTPUT / "failed_logins_by_user.csv"
)

failed_by_ip.head(10).sort_values().plot(kind="barh")
plt.title("Top Source IPs by Failed Login Count")
plt.xlabel("Failed login attempts")
plt.ylabel("Source IP")
plt.tight_layout()
plt.savefig(OUTPUT / "failed_logins_by_ip.png", dpi=150)
plt.close()

time_counts = (
    df.set_index("timestamp")
      .groupby("event_type")
      .resample("30min")
      .size()
      .unstack(0)
      .fillna(0)
)

time_counts.plot()
plt.title("Authentication Events Over Time")
plt.xlabel("Time")
plt.ylabel("Number of events")
plt.tight_layout()
plt.savefig(OUTPUT / "authentication_timeline.png", dpi=150)
plt.close()

print("\nPossible success-after-failure sequences:")
print(timeline if not timeline.empty else "None found")
print("\nSaved results and charts in the outputs/ folder.")
