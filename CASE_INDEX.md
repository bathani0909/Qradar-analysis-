# Case Index

This file gives a recruiter- and analyst-friendly overview of the cases included in this repository.

## Case summary table

| ID | Case Title | Detection Theme | Primary Risk | Analyst Verdict | Confidence | Suggested Priority |
|---|---|---|---|---|---|---|
| 001 | Brute Force and Password Spraying | Authentication Abuse | Credential guessing | Suspicious | High | P2 |
| 002 | Failed Logins Followed by Success | Account Compromise Signal | Valid account abuse | High Risk | High | P1 |
| 003 | Root Account Targeting | Privileged Identity Threat | Privilege abuse / access attempts | Suspicious | High | P1 |
| 004 | Invalid and Bad Username Enumeration | Identity Reconnaissance | Username discovery | Suspicious | Medium-High | P2 |
| 005 | Honeypot and Tarpit Access | Reconnaissance / Unauthorized Interest | Host discovery / probing | Likely Malicious | High | P1 |
| 006 | Repeated Windows Authentication Failures | Windows Auth Abuse | Password guessing / account pressure | Suspicious | Medium | P2 |
| 007 | Repeated Linux Authentication Failures | Linux Auth Abuse | SSH / auth misuse | Suspicious | Medium | P2 |
| 008 | New Host Discovery and Reconnaissance | Network Discovery | Internal / external reconnaissance | Suspicious | Medium-High | P2 |

---

## How to read these cases

Each offense file is written to answer the same analyst questions:

1. **What triggered?**
2. **Why does it matter?**
3. **What evidence supports the concern?**
4. **What benign explanations were considered?**
5. **What should the SOC do next?**

That consistency is intentional and reflects how repeatable investigations should be documented.

---

## Highest-signal cases

If a reviewer only has 5–10 minutes, these are the strongest files to read first:

- `offenses/001-brute-force-and-password-spraying.md`
- `offenses/002-failed-logins-followed-by-success.md`
- `offenses/003-root-account-targeting.md`
- `offenses/005-honeypot-and-tarpit-access.md`

These best represent the most meaningful security patterns in the dataset.
