# Executive Summary

## Project Overview
This project documents a QRadar-based investigation into suspicious authentication and reconnaissance activity observed across a lab environment.

## Main Security Findings
- Repeated failed authentication attempts across multiple usernames
- Failed logins followed by successful authentication
- Privileged account targeting (`root`, `admin`, `Administrator`)
- Invalid / bad username enumeration
- Suspicious interactions with honeypot / tarpit-defined assets
- New host discovery and reconnaissance indicators

## Most Important Offense Themes
1. Brute-force and password spraying activity
2. Failed-to-success authentication chains
3. Root / privileged account targeting
4. Username enumeration behavior
5. Honeypot / tarpit access anomalies

## Security Interpretation
The observed QRadar offenses suggest a coordinated authentication abuse and reconnaissance scenario rather than isolated login failures.

## Skills Demonstrated
- SIEM investigation
- QRadar offense triage
- MITRE ATT&CK mapping
- Detection engineering thinking
- IOC extraction
- Log and authentication analysis

## Recommended Reviewer Path
For the clearest understanding of this project, review these files in order:
1. `README.md`
2. `docs/attack-story.md`
3. `reports/incident-summary.md`
4. `offenses/001-brute-force-and-password-spraying.md`
5. `offenses/002-failed-logins-followed-by-success.md`
