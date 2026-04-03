# Offense 007 — Repeated Linux Authentication Failures

## 1. Executive Summary
This offense focuses on repeated authentication failures observed in a **Linux authentication context**, most likely involving services such as:

- SSH,
- local account authentication,
- or other Linux login-related mechanisms.

This case is important because Linux authentication activity often provides strong visibility into:

- brute-force attempts,
- opportunistic SSH targeting,
- account guessing,
- and repeated unauthorized access attempts.

While repeated Linux login failures can sometimes be benign, they become more meaningful when they show:

- repeated attempts from one source,
- broad username targeting,
- privileged account focus (especially `root`),
- or overlap with other suspicious access patterns.

From a SOC perspective, this offense is useful because Linux authentication logs often reveal attacker behavior early — especially in environments with exposed services or administrative systems.

---

## 2. Detection Trigger
- **Observed Theme:** Repeated Linux authentication failures
- **Likely QRadar Logic:** Grouped failed Linux authentication events associated with repeated source, username, or service patterns
- **Primary Risk:** SSH / Linux credential abuse / unauthorized access attempts
- **Suggested Severity:** Medium to High
- **Analyst Confidence:** Medium to High

---

## 3. Why This Offense Matters
Linux authentication failures are especially relevant because Linux systems are often:

- externally reachable,
- administratively important,
- or associated with infrastructure and service access.

That means repeated failures in a Linux context can indicate more than simple user mistakes.

### Why this matters operationally
A Linux authentication pattern becomes important when it suggests:

- repeated account testing,
- SSH brute-force behavior,
- or attacker interest in administrative access.

This is especially true if the offense includes:

- `root`,
- repeated source concentration,
- or spread across multiple usernames or systems.

### Analyst mindset
A good analyst should ask:

> “Does this look like normal failed login noise, or does it look like someone trying to get shell access?”

That is the core question in this case.

---

## 4. Initial Analyst Hypothesis
The initial working hypothesis is:

> A source or automated process is attempting repeated authentication against Linux systems in a way that may reflect SSH brute force, account guessing, or access probing.

The investigation goal is to determine whether the behavior is:

- expected administrative noise,
- service or credential misconfiguration,
- or suspicious access pressure against Linux accounts.

The offense becomes more meaningful if it overlaps with:

- root account targeting,
- username enumeration,
- or later successful Linux logins.

---

## 5. Evidence Reviewed

### Screenshot 1 — Linux / General Authentication Failure Pattern
![Authentication Failure Patterns](../screenshots/auth-failure-patterns.png)

**What this screenshot helps show:**  
This screenshot provides supporting evidence for repeated authentication failure behavior and helps visualize the pattern being investigated.

**Why it matters:**  
The analyst needs to determine whether the failures are isolated noise or part of a broader Linux-focused credential abuse pattern.

---

### Screenshot 2 — QRadar Offense Context
![QRadar Offense Overview](../screenshots/offense-000-offense-list-overview.png)

**What this screenshot helps show:**  
This provides additional QRadar context by showing how this offense appears within the broader set of suspicious authentication-related cases.

**Why it matters:**  
It helps reinforce that this offense should be reviewed not only in isolation but also as part of a larger attack or reconnaissance storyline.

---

## 6. Key Evidence Points
The strongest indicators in this offense are:

- repeated Linux authentication failures,
- enough repetition to justify offense grouping,
- and a pattern that may reflect account or service access attempts rather than ordinary login noise.

### Why that matters
Linux authentication abuse is often associated with:

- SSH brute force,
- repeated admin account targeting,
- or opportunistic attempts against internet-facing or important infrastructure systems.

That makes repeated Linux auth failures especially valuable to review carefully.

---

## 7. Investigation Steps
A proper analyst review for this offense should include:

1. Review the offense summary and grouped Linux authentication events.
2. Identify the most repeated usernames involved.
3. Determine whether `root` or other privileged accounts appear.
4. Identify whether the failures come from:
   - one source,
   - many sources,
   - internal systems,
   - or external systems.
5. Determine whether the activity is focused on:
   - one Linux host,
   - multiple Linux hosts,
   - or a wider access pattern.
6. Check whether the same source also appears in:
   - brute-force offenses,
   - host discovery,
   - or username enumeration cases.
7. Review whether any later successful authentication events exist.

---

## 8. Analyst Interpretation
This offense is suspicious because repeated Linux authentication failures often represent more than casual user mistakes.

### Why
Linux systems are commonly targeted for shell access, administrative control, and persistence.

That means a repeated authentication pattern in a Linux context can reflect:

- SSH brute force,
- privileged account targeting,
- or attacker attempts to gain foothold access.

### Security meaning
The offense is most concerning when the pattern shows:

- one source repeatedly attempting access,
- multiple usernames being tested,
- or administrative accounts being targeted.

Those conditions make the activity much more consistent with deliberate credential abuse.

---

## 9. False Positive Considerations
There are still realistic benign explanations that should be considered.

### Possible false positives
- An admin repeatedly mistyping credentials
- Incorrect SSH keys or password retries
- Scripts or scheduled jobs using stale credentials
- Monitoring or orchestration systems attempting invalid logins
- Internal testing or lab activity

### Why those explanations are not always enough
Those explanations become less convincing when:

- the source is external,
- multiple usernames are targeted,
- root is involved,
- or the same source appears in multiple suspicious cases.

That is why cross-case and source-based correlation is especially valuable here.

---

## 10. MITRE ATT&CK Mapping
- **Primary Tactic:** Credential Access
- **Primary Technique:** **T1110 — Brute Force**
- **Secondary Technique Consideration:** **T1078 — Valid Accounts** (if successful access later occurs)

### Why this fits
This offense aligns well with brute-force-style credential abuse because it reflects repeated attempts to gain access using tested or guessed credentials against Linux authentication services.

If the activity later transitions into successful login or shell access, the significance increases substantially.

---

## 11. Recommended Validation / Next Steps
The SOC should validate this offense by:

- identifying the top source responsible for the failures,
- checking whether the source is internal, external, or expected,
- reviewing whether the activity targets one or many Linux accounts,
- determining whether `root` or privileged users are involved,
- and checking for later successful authentication or command execution behavior.

### Escalate faster if:
- the source is external,
- the target is internet-facing,
- `root` is involved,
- or later successful Linux access is observed.

---

## 12. Final Analyst Verdict
**Assessment:** Suspicious repeated Linux authentication activity consistent with possible SSH or account credential abuse.

**SOC Action:**  
Investigate the source, validate targeted Linux identities, correlate with related offenses, and escalate if the activity overlaps with privilege targeting or successful access.
