# Mini SOC Investigation Lab

## Overview

A beginner-friendly Security Operations Center (SOC) investigation project that analyzes simulated authentication logs to identify suspicious login activity.

Built with Python, pandas, and matplotlib, this project demonstrates basic security log analysis, failed-login detection, investigation reporting, and data visualization.

**Note:** All authentication events are simulated. This project does not analyze real user accounts or represent a confirmed security incident.

## Objectives

- Generate simulated authentication logs.
- Analyze successful and failed login attempts.
- Identify source IP addresses with repeated failed logins.
- Detect successful logins following repeated failures.
- Generate CSV investigation results and visualizations.
- Document findings and recommended response actions.

## Tools and Technologies

- Python
- pandas
- matplotlib
- CSV log analysis
- Git and GitHub (for version control and project sharing)

## Project Structure

```text
Mini-SOC-Lab/
├── data/
│   └── auth_logs.csv
├── src/
│   ├── generate_logs.py
│   └── analyze_logs.py
├── outputs/
│   ├── failed_logins_by_ip.csv
│   ├── failed_logins_by_user.csv
│   ├── success_after_failures.csv
│   ├── failed_logins_by_ip.png
│   └── authentication_timeline.png
├── report/
│   └── incident_report.md
└── README.md
```

## Detection Logic

The analysis script:

1. Loads authentication events and validates required columns.
2. Counts failed login attempts by source IP and username.
3. Flags IP addresses with at least five failed login attempts.
4. Checks for a successful login after earlier failures from the same IP.
5. Exports investigation results and charts.

A flagged pattern is an investigative lead, not proof of malicious activity.

## Sample Findings

The simulated dataset contains 96 authentication events:

- 66 successful logins
- 30 failed logins
- 15 failed attempts from `203.0.113.77`
- A subsequent successful login to the simulated `admin` account at 11:16 AM on October 20, 2026

The sequence was flagged for further investigation. No real account compromise was established.

## How to Run

Create and activate a virtual environment, then install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pandas matplotlib
```

Generate the simulated logs:

```bash
python src/generate_logs.py
```

Analyze the logs:

```bash
python src/analyze_logs.py
```

Review the generated CSV files and charts in the `outputs/` folder.

## Investigation Report

See [`report/incident_report.md`](report/incident_report.md) for the investigation summary, evidence, severity assessment, limitations, and recommended response.

## Future Improvements

- Add configurable detection thresholds.
- Detect repeated failures within a rolling time window.
- Add more authentication detection rules.
- Integrate with a SIEM such as Splunk.
- Add automated tests and structured alert output.

## Disclaimer

This project uses simulated data for educational and portfolio purposes only. The IP addresses used are documentation-reserved example addresses.
