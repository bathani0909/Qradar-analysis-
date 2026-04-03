# QRadar Offense Triage Runbook

This runbook is a practical guide for how a SOC analyst should review the types of offenses documented in this repository.

---

## Step 1 — Validate what actually triggered

Before deciding whether an offense is dangerous, confirm:

- what event type triggered it,
- what rule or grouping logic likely created it,
- and whether the offense is based on one event or a repeated pattern.

### Key question
> Am I looking at a single noisy event, or a repeated security-relevant behavior?

---

## Step 2 — Identify the scope

Determine the size and shape of the activity:

- How many source IPs are involved?
- How many usernames are involved?
- How many destination systems are involved?
- Is the activity concentrated or broad?

### Why this matters
Attack behavior often looks **systematic**. Benign activity often looks **isolated** or operationally explainable.

---

## Step 3 — Determine whether the targets are meaningful

Not all targets are equal.

Increase concern if the activity involves:

- `root`
- `admin`
- `Administrator`
- servers or exposed systems
- honeypot / tarpit assets
- remote access infrastructure

### Key question
> Is the actor touching something that should materially change our risk posture?

---

## Step 4 — Look for progression

One of the most important analyst skills is recognizing whether activity is **advancing**.

Examples of progression:
- invalid usernames -> valid usernames
- repeated failures -> successful login
- one host -> many hosts
- one account -> privileged account
- probing -> access attempts

### Why this matters
Progression often indicates intent and increasing attacker confidence.

---

## Step 5 — Consider false positives before escalating

Good analysts do not assume every suspicious event is malicious.

Check whether the activity could be explained by:

- internal vulnerability scanning,
- password mistakes,
- broken service accounts,
- admin testing,
- or maintenance tooling.

### Important note
False positive consideration should not weaken the investigation — it should make the final conclusion more defensible.

---

## Step 6 — Assign a practical SOC outcome

Every offense should end with one of these actions:

- **Close as benign**
- **Monitor / watchlist**
- **Tune detection**
- **Escalate to incident response**
- **Contain / reset / block**

If a writeup cannot answer “what should happen next?”, it is incomplete.

---

## Triage shortcuts by pattern

### Repeated failures only
- Medium signal
- Check spread, source concentration, and account type

### Failures followed by success
- High signal
- Validate quickly for possible compromise

### Privileged account targeting
- High impact
- Prioritize even if event count is low

### Honeypot / tarpit access
- High confidence
- Escalate faster than normal auth noise

### Username enumeration
- Medium signal
- Useful precursor pattern for later abuse

---

## Final principle

> Triage is not just deciding whether something looks bad.  
> It is deciding whether the evidence justifies action.
