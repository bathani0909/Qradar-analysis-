# QRadar Offense Analysis Lab

A SOC-style blue-team portfolio project that documents how IBM QRadar offenses can be investigated, validated, explained, and improved through analyst reasoning, AQL pivots, IOC extraction, and detection-tuning recommendations.

This repository is intentionally written like a **junior SOC / detection analyst knowledge base** rather than a screenshot dump. The goal is to show not only **what fired**, but also **why it mattered**, **what evidence was reviewed**, **what alternative explanations were considered**, and **what a security team should do next**.

---

## What this project demonstrates

This project is designed to demonstrate practical blue-team skills:

- **QRadar offense triage**
- **Authentication abuse investigation**
- **Brute force and password spraying analysis**
- **Success-after-failure validation**
- **Privileged account targeting review**
- **Username enumeration and reconnaissance analysis**
- **Honeypot / tarpit interaction review**
- **AQL-based evidence pivoting**
- **IOC extraction and case documentation**
- **Detection engineering thinking**
- **SOC reporting and escalation reasoning**

---

## Lab scope

### Platform
- IBM QRadar (lab / training-style environment)

### Primary event themes
- Authentication failures
- Authentication failures followed by success
- Invalid user / bad username events
- Privileged account targeting
- Honeypot / tarpit access
- New host discovery / reconnaissance indicators

### Core objective
Show how an analyst can take noisy offense data and convert it into:
1. a clear investigative narrative,
2. a defensible security assessment,
3. and actionable detection improvements.

---

## Why this repo is different from a basic QRadar project

Most beginner SIEM projects stop at:
- screenshots,
- offense titles,
- and short descriptions.

This repo is built to go further by documenting:

- what triggered the offense,
- what the initial hypothesis was,
- what pivots were used,
- what evidence increased or decreased confidence,
- what false positives were considered,
- and what the SOC should do next.

That structure is much closer to how real investigations are documented in an operational environment.

---

## Investigation themes covered

### 1) Brute force and password spraying
Repeated authentication failures are reviewed to determine whether they are more consistent with:
- isolated user error,
- noisy infrastructure behavior,
- or deliberate credential abuse.

### 2) Failures followed by success
This pattern is treated as higher-signal because it may indicate:
- successful credential guessing,
- compromised accounts,
- or attacker persistence after repeated failed access.

### 3) Privileged account targeting
Attempts against accounts such as:
- `root`
- `admin`
- `Administrator`

are given additional scrutiny because they carry higher operational and security impact.

### 4) Invalid / bad username enumeration
This pattern can indicate:
- guessed account names,
- broad identity discovery attempts,
- or automated username validation behavior.

### 5) Honeypot / tarpit and reconnaissance activity
Activity involving intentionally sensitive or trap-like assets is treated as higher-confidence suspicious behavior because legitimate access should be limited or non-existent.

---

## Repository structure

```text
README.md                         -> Project overview and reviewer guide
CASE_INDEX.md                     -> Fast summary of all cases
DETECTION_GAPS.md                 -> Missing visibility and improvement opportunities
LESSONS_LEARNED.md                -> Key blue-team takeaways

docs/
  executive-summary.md            -> Short reviewer briefing
  attack-story.md                 -> End-to-end attacker narrative
  lab-environment.md              -> Lab context and assumptions
  mitre-mapping.md                -> ATT&CK-aligned interpretation
  offense-analysis-methodology.md -> Repeatable analyst workflow
  triage-workflow.md              -> Quick triage model
  triage-runbook.md               -> SOC-style runbook for offense review
  interview-talk-track.md         -> Talking points for recruiters/interviewers

offenses/
  001-008 case files              -> Detailed offense investigations
  offense-template.md             -> Reusable case format

queries/
  useful-aql-queries.md           -> Investigation-focused AQL queries
  aql-hunting-library.md          -> Categorized hunting/query reference
  triage-pivot-checklist.md       -> Pivot ideas during offense review

rules/
  observed-qradar-rules.md        -> What appears to have triggered
  correlation-observations.md     -> Rule behavior observations
  rule-tuning-recommendations.md  -> Suggested tuning improvements

use-cases/
  Detection concept writeups      -> Reusable blue-team use cases

iocs/
  extracted-iocs.md               -> Consolidated indicators
  suspicious-source-ips.md        -> Source IP summary
  targeted-usernames.md           -> Targeted identity summary
  attacked-assets.md              -> Affected assets summary

reports/
  incident-summary.md             -> Consolidated SOC-style summary

tools/
  ioc_extractor.py                -> Example helper script for extracting IOCs
```

---

## Recommended reading order for recruiters / hiring managers

If you only read a few files, use this order:

1. `README.md`
2. `docs/executive-summary.md`
3. `reports/incident-summary.md`
4. `CASE_INDEX.md`
5. `offenses/001-brute-force-and-password-spraying.md`
6. `offenses/002-failed-logins-followed-by-success.md`
7. `offenses/005-honeypot-and-tarpit-access.md`
8. `docs/offense-analysis-methodology.md`
9. `rules/rule-tuning-recommendations.md`

That path gives the fastest understanding of the project’s depth and quality.

---

## What a reviewer should conclude after reading this repo

A reviewer should be able to conclude that the author can:

- triage QRadar offenses methodically,
- separate noisy events from meaningful attacker behavior,
- explain authentication abuse patterns clearly,
- document evidence in a SOC-friendly format,
- think about false positives and confidence,
- and suggest realistic tuning and escalation actions.

That is the primary purpose of this project.

---
