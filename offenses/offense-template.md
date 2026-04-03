# Offense Title

## Offense ID
OFF-XXX

## Date Observed
YYYY-MM-DD

## Offense Name
Example: Multiple Login Failures for the Same User

## Severity
Low / Medium / High / Critical

## Category
Authentication / Brute Force / Reconnaissance / Lateral Movement / Persistence / Other

## Description
Brief explanation of what this offense means in QRadar.

## Trigger Logic
Describe what likely caused the offense or correlation rule to fire.

## Observed Details
- Source IP:
- Destination IP:
- Username:
- Log Source:
- Event Name:
- Event Count:
- Time Range:

## Investigation Steps
1. Review offense details in QRadar
2. Identify related events and flows
3. Check source IP reputation/internal ownership
4. Review username/account behavior
5. Check whether login attempts succeeded
6. Validate whether activity is malicious or expected

## Findings
Summarize what was discovered.

## Possible Impact
What could happen if this is malicious?

## MITRE ATT&CK Mapping
- Tactic:
- Technique:
- Technique ID:

## Triage Outcome
True Positive / False Positive / Benign / Needs Further Investigation

## Recommendations
- Tune correlation rule if needed
- Block suspicious IP if malicious
- Investigate affected host/account
- Add watchlist or reference set

## Evidence
- Screenshot(s)
- Event logs
- Notes

## Lessons Learned
What can be improved in future detections or investigations?
