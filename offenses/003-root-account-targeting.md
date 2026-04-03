# Offense 003 — Root Account Targeting

## 1. Executive Summary
This case focuses on attempts against privileged identities such as `root`, `admin`, or `Administrator`. Even a modest number of events becomes meaningful when the target account has elevated access.

## 2. Detection Trigger
- **Observed Theme:** Authentication activity against privileged accounts
- **Likely Rule / Logic:** Failures or suspicious access attempts involving high-value identities
- **Primary Risk:** Privilege abuse, high-impact account compromise, lateral movement enablement
- **Suggested Severity:** High
- **Analyst Confidence:** High

## 3. Why This Offense Matters
Privileged accounts are disproportionately important because successful access to them can lead to broad control over systems or services. That means analysts should shift from a volume-based mindset to an impact-based mindset.

## 4. Initial Analyst Hypothesis
The actor is either opportunistically guessing default/admin-style accounts or deliberately targeting privileged identities for high-value access.

## 5. Evidence Reviewed
### Supporting screenshots
- `../screenshots/offense-003-overview.png`
- `../screenshots/offense-003-privileged-account-targeting.png`

### Key evidence points
- The offense indicates attention directed toward privileged account naming patterns.
- The account targets imply an attempt to gain elevated access rather than ordinary user access.

## 6. Investigation Steps
1. Review the offense summary and grouped events.
2. Identify the most repeated source, user, destination, or event pattern.
3. Pivot into supporting event context and compare repetition vs spread.
4. Check whether the pattern is isolated, broad, privileged, or followed by success.
5. Assess whether the behavior is more consistent with noise or malicious intent.

## 7. Analyst Interpretation
Even if the event count is lower than other offenses, the risk is higher because the attacker is targeting the identities that matter most. This is the kind of case where business impact can outweigh raw alert volume.

## 8. False Positive Considerations
- Admins occasionally mistype passwords on privileged accounts.
- Security tools may probe default usernames in controlled testing.
- Some noisy devices or integrations can produce misleading admin-style account attempts.

## 9. MITRE ATT&CK Mapping
- **Primary Tactic:** Credential Access / Privilege Escalation
- **Primary Technique:** T1110 — Brute Force
- **Why this fits:** The behavior reflects repeated attempts to access high-value identities using guessed credentials.

## 10. Recommended Validation / Next Steps
- Confirm whether the targeted account exists and whether it is actively used.
- Determine whether the source is internal, external, expected, or suspicious.
- Review whether the account later authenticated anywhere successfully.
- Increase priority if the target has server, cloud, or identity admin access.

## 11. Final Analyst Verdict
**Assessment:** Suspicious and high-priority due to privileged account focus, even if final intent is not fully confirmed.

**SOC Action:** Treat as elevated risk, validate the account owner or admin team, and review related authentication activity immediately.
