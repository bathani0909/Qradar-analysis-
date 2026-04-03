# Lessons Learned

This file captures the main blue-team takeaways from the QRadar offense review documented in this repository.

---

## 1) Not every authentication failure is important — but patterns are

Single authentication failures are usually weak signals.

Repeated failures become much more meaningful when they show:
- source concentration,
- multiple targeted usernames,
- broad account coverage,
- privileged account interest,
- or a later successful login.

**Lesson:** Analysts should focus on **behavioral patterns**, not isolated events.

---

## 2) Success-after-failure is one of the highest-value pivots

A burst of failed attempts followed by a successful authentication is significantly more important than failure-only activity.

Why:
- it may indicate successful credential guessing,
- account takeover,
- or attacker persistence after trial-and-error access attempts.

**Lesson:** This pattern should receive higher priority than generic failed-login noise.

---

## 3) Honeypot access is stronger than “normal suspiciousness”

When an actor touches a host that should not attract legitimate traffic, confidence rises quickly.

**Lesson:** Honeypot / tarpit activity is one of the cleanest opportunities for low-noise, high-signal detection.

---

## 4) Privileged account targeting should always change the triage posture

Attempts against:
- `root`
- `admin`
- `Administrator`

should shift analyst thinking immediately.

Even if the event volume is small, the **impact potential** is high.

**Lesson:** Prioritization should be influenced by identity importance, not just event count.

---

## 5) Username enumeration often appears before more direct abuse

Bad username and invalid user events are easy to dismiss, but they may indicate that an attacker is trying to discover:
- valid accounts,
- naming conventions,
- and worthwhile targets.

**Lesson:** Reconnaissance against identity systems deserves more attention than many teams give it.

---

## 6) A good analyst writeup should include uncertainty

Security work is rarely perfect certainty.

A good case file should clearly explain:
- what is known,
- what is suspected,
- what is missing,
- and what would raise or lower confidence.

**Lesson:** Strong analysis is not about sounding certain — it is about being clear, evidence-based, and defensible.

---

## 7) Detection quality matters as much as detection quantity

If a rule fires constantly but rarely produces meaningful investigations, it drains analyst time.

**Lesson:** A mature security program is built not just on creating alerts, but on **tuning them to produce useful work**.

---

## Final takeaway

The most important lesson from this project is simple:

> Good blue-team work is not just identifying that something happened.  
> It is explaining **why it matters**, **how confident we are**, and **what should happen next**.
