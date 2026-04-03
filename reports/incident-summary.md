# Incident Summary

## Executive Summary
This repository documents a set of QRadar offenses centered on authentication abuse and suspicious reconnaissance activity. Across the reviewed offenses, the strongest recurring themes were:

- repeated authentication failures,
- broad username targeting,
- suspicious source concentration,
- privileged account targeting,
- fail-to-success authentication sequences,
- and honeypot/tarpit interaction.

Taken together, the activity is more consistent with **deliberate probing and credential abuse** than with isolated user error.

---

## Investigation Scope
The investigation focused on five offense themes:

1. Brute force / password spraying
2. Failed logins followed by success
3. Root / privileged account targeting
4. Invalid and bad username enumeration
5. Honeypot / tarpit access and reconnaissance behavior

---

## High-Level Assessment
### What stood out
- Multiple offenses shared authentication-related characteristics.
- Several usernames of operational or privileged interest were targeted.
- Repeated source IPs appeared across offense views.
- Honeypot / tarpit alerts suggested broader probing or discovery behavior.

### Why this matters
In a SOC context, these patterns are important because they indicate **intentional hostile behavior**, not just authentication noise.

---

## Evidence Snapshot
![Offense List Overview](../screenshots/offense-000-offense-list-overview.png)

---

## Recommended Analyst Actions
- Review raw authentication events for confirmed fail-to-success sequences.
- Pivot on repeated source IPs across all related log sources.
- Validate whether targeted usernames map to real accounts.
- Prioritize review of privileged account attempts.
- Check whether honeypot/tarpit access overlaps with authentication-related activity.

---

## Conclusion
The reviewed offenses collectively suggest a meaningful pattern of authentication abuse and reconnaissance behavior. While each offense can be evaluated independently, the strongest analyst conclusion comes from reviewing them **together as part of the same attack story**.
