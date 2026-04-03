# Detection Gaps Identified

This file documents the main visibility and detection-quality limitations observed while reviewing the QRadar offenses in this project.

The purpose of this file is to show that alert review is not enough on its own. Good analysts should also identify **where the detection program is incomplete**.

---

## Gap 1 — Authentication context is stronger than identity context

### Observation
There is enough evidence to identify repeated authentication failures and suspicious access patterns, but not always enough context to quickly determine:

- whether a targeted user is privileged,
- whether the account is human or service-based,
- whether the activity aligns with normal login behavior.

### Why this matters
Without identity enrichment, analysts spend more time deciding whether the event is dangerous or simply noisy.

### Improvement
Integrate or enrich with:
- Active Directory / IAM role context
- service account tagging
- privileged user tagging
- last-seen / normal behavior baselines

---

## Gap 2 — Success-after-failure deserves stronger prioritization

### Observation
A repeated failure pattern is useful, but a **successful authentication following repeated failures** is materially more important.

### Why this matters
This is one of the clearest transitions from:
- “possible noise”
to
- “possible compromise”

### Improvement
Increase severity or magnitude when:
- the same username is involved,
- the same source IP is involved,
- or the success follows a short burst of failures.

---

## Gap 3 — Honeypot / tarpit events should be treated as high-confidence

### Observation
Access to honeypot- or tarpit-like assets is inherently higher signal than generic authentication noise.

### Why this matters
Legitimate business justification for this type of access should be rare.

### Improvement
Prioritize these events with:
- higher offense magnitude,
- tighter escalation criteria,
- and faster analyst review expectations.

---

## Gap 4 — Username enumeration is often under-prioritized

### Observation
Bad username / invalid user activity may look low impact at first, but it often acts as a **precursor** to broader credential abuse.

### Why this matters
It may represent attacker learning and account discovery before password attacks begin.

### Improvement
Correlate invalid username behavior with:
- later brute-force attempts,
- broader source IP activity,
- privileged account targeting,
- and cross-host authentication attempts.

---

## Gap 5 — Asset criticality should influence offense interpretation

### Observation
A login attempt against a random lab host and a login attempt against a sensitive system should not be treated equally.

### Why this matters
The same event type can represent very different risk depending on the target.

### Improvement
Use asset context such as:
- server role,
- exposure level,
- business criticality,
- privileged access relationship.

---

## Gap 6 — Repeated authentication failures require better suppression logic

### Observation
Authentication failures are noisy by nature and can create analyst fatigue if they are not tuned properly.

### Why this matters
Too much low-value noise reduces the team’s ability to respond to higher-confidence activity.

### Improvement
Tune for:
- service accounts,
- known noisy hosts,
- maintenance windows,
- expected admin tooling,
- and repeated internal misconfiguration patterns.

---

## Bottom line

The environment already produces useful offense data. The next maturity step is not just **more alerts**, but **better context, stronger prioritization, and more precise escalation logic**.
