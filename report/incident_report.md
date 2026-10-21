# Mini SOC Investigation Report

## 1. Executive Summary

This investigation analyzed 96 simulated authentication events using
Python, pandas, and matplotlib. The analysis identified a source IP
with repeated failed login attempts followed by a successful login
to the admin account.

The activity is suspicious and warrants further investigation.
Because the dataset is simulated, this finding is a demonstration
of detection logic, not evidence of a real security incident.

## 2. Investigation Scope

- Log source: Simulated authentication logs
- Dataset: data/auth_logs.csv
- Total events analyzed: 96
- Analysis tools: Python, pandas, matplotlib
- Detection threshold: 5 or more failed login attempts from one IP

## 3. Key Findings

- Total authentication events: 96
- Successful logins: 66
- Failed logins: 30
- Most suspicious source IP: 203.0.113.77
- Failed attempts from that IP: 15
- Account successfully accessed in the simulated sequence: admin
- Successful login time: October 20, 2026, at 11:16 AM

The source IP generated 15 failed login attempts before a successful
login to the admin account. This pattern may indicate a password
guessing attempt followed by successful authentication.

## 4. Evidence

The analysis generated the following output files:

- outputs/failed_logins_by_ip.csv
- outputs/failed_logins_by_user.csv
- outputs/success_after_failures.csv
- outputs/failed_logins_by_ip.png
- outputs/authentication_timeline.png

The detection is based on event counts and timestamps. The logs alone
do not establish who performed the activity or whether an account
was actually compromised.

## 5. Severity Assessment

Suggested severity: Medium — requires investigation.

Rationale: Multiple failed logins followed by a successful admin
login could indicate unauthorized access. Additional evidence would
be needed to confirm malicious activity and determine impact.

## 6. Recommended Response

1. Review authentication events before and after the successful login.
2. Verify whether the admin login was authorized.
3. Review the account's activity and affected host.
4. Check for additional suspicious authentication patterns.
5. If investigating a real environment, follow the organization's
   incident response process and escalate according to policy.

## 7. Limitations

- All events in this project are simulated.
- The IP addresses use documentation-reserved ranges.
- A threshold-based alert can produce false positives.
- No real account compromise or attacker identity has been established.

## 8. Conclusion

This project demonstrates basic authentication log analysis,
failed-login threshold detection, identification of a successful
login following repeated failures, and generation of investigation
artifacts using Python.
