# Offense 001 — Brute Force and Password Spraying

## 1. Executive Summary
This case reviews repeated authentication failures to determine whether the activity is more consistent with normal user mistakes or deliberate credential abuse. The concentration of attempts, repeated account targeting, and systematic feel of the pattern make this a meaningful security event rather than background noise.

## 2. Detection Trigger
- **Observed Theme:** Repeated authentication failures across one or more usernames
- **Likely Rule / Logic:** High volume or clustered failed authentication events grouped into a single offense
- **Primary Risk:** Credential guessing, password spraying, brute force, account pressure
- **Suggested Severity:** Medium to High
- **Analyst Confidence:** High

## 3. Why This Offense Matters
Repeated failed authentication is one of the most common noisy signals in enterprise logging, but it becomes important when the pattern shows coordination. Multiple usernames from one source, or repeated attempts against the same identity across a short window, indicate attacker intent more than user frustration.

## 4. Initial Analyst Hypothesis
The activity likely represents either password spraying (many usernames, fewer attempts per account) or brute-force behavior (more attempts against fewer accounts) rather than accidental mistyping.

## 5. Evidence Reviewed
### Supporting screenshots
- `../screenshots/offense-001-overview.png`
- `../screenshots/offense-001-username-targeting.png`
- `../screenshots/offense-001-source-ip-patterns.png`

### Key evidence points
- Repeated authentication failures are visible across a concentrated set of events.
- Multiple usernames appear to be involved rather than a single user retrying once or twice.
- The source pattern appears systematic enough to justify deeper investigation.

## 6. Investigation Steps
1. Review the offense summary and grouped events.
2. Identify the most repeated source, user, destination, or event pattern.
3. Pivot into supporting event context and compare repetition vs spread.
4. Check whether the pattern is isolated, broad, privileged, or followed by success.
5. Assess whether the behavior is more consistent with noise or malicious intent.

## 7. Analyst Interpretation
The visible pattern aligns more strongly with **credential abuse** than with routine user error. The most important signal is not just failure volume, but the structure of the behavior: repeated attempts, identity spread, and a systematic pattern. That combination is commonly associated with brute-force or password-spraying activity.

## 8. False Positive Considerations
- A user repeatedly entering the wrong password could produce failures, but would usually be limited to one username.
- A broken script or service account can also create repeated failures, but usually shows a more consistent single-account pattern.
- Internal vulnerability or authentication testing can mimic this behavior and should be ruled out with asset and source validation.

## 9. MITRE ATT&CK Mapping
- **Primary Tactic:** Credential Access
- **Primary Technique:** T1110 — Brute Force
- **Why this fits:** The offense reflects repeated attempts to gain access by testing credentials rather than using a known valid account from the start.

## 10. Recommended Validation / Next Steps
- Pivot on the top source IP to identify all targeted usernames.
- Check whether any of the targeted users later authenticated successfully.
- Validate whether privileged or service accounts were involved.
- Compare source behavior across other assets and time windows.

## 11. Final Analyst Verdict
**Assessment:** Suspicious activity consistent with credential guessing and worthy of escalation or deeper validation.

**SOC Action:** Investigate the source, review targeted accounts, and increase urgency if a success event or privileged account is involved.
