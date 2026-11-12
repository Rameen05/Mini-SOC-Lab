# Mini SOC Investigation Report

## 1. Executive Summary

This investigation analyzed 96 simulated authentication events using Python, pandas, and matplotlib. The analysis identified a source IP associated with repeated failed login attempts followed by a successful login to the admin account.

The detection identified 14 failed login attempts within the 15-minute period preceding the successful login.

The activity is suspicious and warrants further investigation. Because the dataset is simulated, this finding demonstrates detection logic rather than evidence of a real security incident.

## 2. Investigation Scope

- Log source: Simulated authentication logs
- Dataset: `data/auth_logs.csv`
- Total events analyzed: 96
- Analysis tools: Python, pandas, matplotlib
- Initial threshold: 5 or more failed login attempts from one IP
- Detection window: 15 minutes before a successful login
- Detection condition: At least 5 failed attempts from the same IP within that window, followed by a successful login

## 3. Key Findings

- Total authentication events: 96
- Successful logins: 66
- Failed logins: 30
- Most suspicious source IP: `203.0.113.77`
- Total failed attempts from that IP: 15
- Failed attempts within the 15-minute detection window: 14
- Account successfully accessed in the simulated sequence: `admin`
- Successful login time: October 20, 2026, at 11:16 AM

The source IP generated 15 failed login attempts overall. Fourteen occurred within the 15-minute period preceding a successful login to the admin account.

This pattern may indicate a password-guessing attempt followed by successful authentication.

## 4. Detection Logic and Evidence

The Python detection script:

1. Groups authentication events by source IP.
2. Identifies IP addresses with at least 5 failed login attempts.
3. Examines each successful login from those IP addresses.
4. Checks for failed attempts from the same IP during the preceding 15 minutes.
5. Flags the sequence when at least 5 failures occurred within that window.

The investigation identified the following sequence:

| Indicator | Finding |
|---|---|
| Source IP | `203.0.113.77` |
| Target account | `admin` |
| Total failed attempts | 15 |
| Failures in detection window | 14 |
| Detection window | 15 minutes |
| Successful login | 11:16 AM |

Generated evidence:

- `outputs/failed_logins_by_ip.csv`
- `outputs/failed_logins_by_user.csv`
- `outputs/success_after_failures.csv`
- `outputs/failed_logins_by_ip.png`
- `outputs/authentication_timeline.png`

The detection is based on event counts and timestamps. The logs alone do not establish who performed the activity or whether an account was actually compromised.

## 5. Severity Assessment

**Suggested severity: Medium — requires investigation.**

Rationale: Multiple failed login attempts followed by a successful admin login within a short period could indicate unauthorized access. Additional evidence would be needed to confirm malicious activity and determine impact.

## 6. Recommended Response

1. Review authentication events before and after the successful login.
2. Verify whether the admin login was authorized.
3. Review the account's activity and affected host.
4. Check for additional suspicious authentication patterns.
5. If investigating a real environment, follow the organization's incident response process and escalate according to policy.

## 7. Limitations

- All events in this project are simulated.
- The IP addresses use documentation-reserved ranges.
- Threshold-based detection can still produce false positives.
- The 15-minute detection window is a configurable rule, not proof of malicious activity.
- No real account compromise or attacker identity has been established.

## 8. Conclusion

This project demonstrates authentication log analysis, failed-login threshold detection, time-window-based correlation of failed and successful logins, and generation of investigation artifacts using Python.

The improved detection logic provides more context than a simple total-failure threshold by identifying repeated failures within a defined period before a successful login.