# Offense 002 — Failed Logins Followed by Success

## 1. Executive Summary
This is one of the highest-signal cases in the repo because it reflects a common compromise pattern: repeated failed authentication followed by a successful login. That sequence may indicate that an actor eventually guessed or obtained valid credentials.

## 2. Detection Trigger
- **Observed Theme:** Authentication failures followed by successful access
- **Likely Rule / Logic:** Correlation of repeated failures with later success for the same or related identity/source
- **Primary Risk:** Potential account compromise or successful credential abuse
- **Suggested Severity:** High
- **Analyst Confidence:** High

## 3. Why This Offense Matters
Failure-only patterns are often noisy. Failure-then-success is different because it suggests the access attempt may have eventually worked. That makes this pattern much more actionable for a SOC.

## 4. Initial Analyst Hypothesis
The account may have been accessed after repeated credential guessing, or the success may represent a benign user finally entering the correct password. The goal is to distinguish those explanations.

## 5. Evidence Reviewed
### Supporting screenshots
- `../screenshots/offense-002-overview.png`
- `../screenshots/offense-002-failures-followed-by-success.png`

### Key evidence points
- Failed login attempts precede a successful authentication event.
- The event chain implies progression from access attempts to access achieved.
- Depending on user, host, and source context, this may indicate compromise or at minimum elevated risk.

## 6. Investigation Steps
1. Review the offense summary and grouped events.
2. Identify the most repeated source, user, destination, or event pattern.
3. Pivot into supporting event context and compare repetition vs spread.
4. Check whether the pattern is isolated, broad, privileged, or followed by success.
5. Assess whether the behavior is more consistent with noise or malicious intent.

## 7. Analyst Interpretation
This offense deserves a higher triage posture than standard failed-login activity. If the success event aligns to the same user, host, or source, the pattern is highly relevant. Even if it ultimately proves benign, it is exactly the kind of behavior a real SOC should review quickly.

## 8. False Positive Considerations
- A legitimate user may simply have remembered the correct password after several failed attempts.
- A password reset or stale cached credential can create a failure-then-success chain.
- MFA or login portal retries can occasionally create misleading sequences.

## 9. MITRE ATT&CK Mapping
- **Primary Tactic:** Credential Access / Defense Evasion / Persistence
- **Primary Technique:** T1078 — Valid Accounts
- **Why this fits:** If the successful authentication is attacker-driven, the actor has transitioned from guessing to use of a valid account.

## 10. Recommended Validation / Next Steps
- Validate whether the successful login came from the same source as the failures.
- Confirm whether the account is privileged, remote-access enabled, or sensitive.
- Check for unusual post-authentication behavior after the success event.
- Escalate quickly if the source is external or unfamiliar.

## 11. Final Analyst Verdict
**Assessment:** High-risk authentication sequence that should be treated as a possible account compromise until disproven.

**SOC Action:** Prioritize review, validate account ownership and source legitimacy, and reset or contain the account if evidence remains suspicious.
