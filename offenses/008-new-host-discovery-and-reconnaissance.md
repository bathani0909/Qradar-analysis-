# Offense 008 — New Host Discovery and Reconnaissance

## Executive Summary
This case documents suspicious behavior associated with **network discovery and asset probing**. The purpose of the writeup is to show how an analyst should move from a QRadar offense title to a defensible security assessment.

## Detection Trigger
- **Observed Theme:** Network Discovery And Asset Probing
- **Suggested Severity:** Medium to High
- **Analyst Confidence:** Medium to High

## Why This Matters
This pattern is important because it may represent either:
- early-stage attacker learning,
- direct credential abuse,
- or reconnaissance that prepares for a later access attempt.

## Evidence Reviewed
Review the associated screenshots and grouped offense evidence in this folder and in `screenshots/`.

## Investigation Questions
1. Is the behavior concentrated to one source or broadly distributed?
2. Does the activity target valid, privileged, or guessed identities/assets?
3. Is there follow-on activity such as successful access or expanded scanning?
4. Does the pattern align with expected administrative or testing behavior?

## Analyst Interpretation
The behavior is suspicious enough to justify investigation because it reflects intent, not just noise. The exact risk level should be adjusted using:
- source legitimacy,
- target sensitivity,
- user/asset criticality,
- and whether the behavior progresses beyond discovery or failure events.

## False Positive Considerations
Possible benign explanations include:
- internal scanning,
- lab testing,
- misconfigured scripts,
- or normal but noisy admin activity.

## Recommended Next Steps
- Validate the source and target context.
- Compare with adjacent offenses and repeated source behavior.
- Escalate if privileged assets, external sources, or successful access are involved.

## Final Verdict
**Assessment:** Suspicious and useful for triage, hunting, and tuning.
