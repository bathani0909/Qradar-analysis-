# AQL Hunting Library

This file collects reusable QRadar AQL ideas that support the offense investigations in this repository.

The goal is not only to provide queries, but also to explain **when to use them** and **how to interpret the results**.

---

## 1) Repeated failed logins by source IP

```sql
SELECT sourceip, username, COUNT(*) AS fail_count
FROM events
WHERE QIDNAME(qid) ILIKE '%failed%'
GROUP BY sourceip, username
ORDER BY fail_count DESC
LAST 24 HOURS
```

**Use when:** validating brute-force or password-spraying behavior  
**Why it matters:** helps identify whether a source is repeatedly targeting one or many accounts  
**Interpret carefully if:** the source is a jump host, VPN concentrator, or shared admin system

---

## 2) Failures followed by success

```sql
SELECT sourceip, username, QIDNAME(qid), starttime
FROM events
WHERE username IS NOT NULL
  AND (QIDNAME(qid) ILIKE '%failed%' OR QIDNAME(qid) ILIKE '%success%')
ORDER BY username, starttime
LAST 24 HOURS
```

**Use when:** checking whether failed authentication attempts progressed into successful access  
**Why it matters:** one of the strongest account-compromise pivots in this repo  
**Interpret carefully if:** password resets, cached credentials, or user retry behavior are common

---

## 3) Privileged account targeting

```sql
SELECT sourceip, username, COUNT(*) AS attempts
FROM events
WHERE LOWER(username) IN ('root','admin','administrator')
GROUP BY sourceip, username
ORDER BY attempts DESC
LAST 7 DAYS
```

**Use when:** identifying high-value account focus  
**Why it matters:** privileged accounts should materially change triage priority  
**Interpret carefully if:** lab systems or test accounts intentionally use common admin names

---

## 4) Invalid / bad username enumeration

```sql
SELECT sourceip, username, COUNT(*) AS bad_user_events
FROM events
WHERE QIDNAME(qid) ILIKE '%invalid user%'
   OR QIDNAME(qid) ILIKE '%bad username%'
GROUP BY sourceip, username
ORDER BY bad_user_events DESC
LAST 24 HOURS
```

**Use when:** checking whether an actor is discovering valid usernames  
**Why it matters:** this may represent reconnaissance before password attacks  
**Interpret carefully if:** parsing or normalization differences cause noisy identity fields

---

## 5) Honeypot / tarpit interaction review

```sql
SELECT sourceip, destinationip, QIDNAME(qid), COUNT(*) AS event_count
FROM events
WHERE destinationip IS NOT NULL
GROUP BY sourceip, destinationip, QIDNAME(qid)
ORDER BY event_count DESC
LAST 24 HOURS
```

**Use when:** reviewing suspicious traffic to sensitive or trap-like hosts  
**Why it matters:** honeypot interaction is often higher-confidence than generic noise  
**Interpret carefully if:** the host inventory is incomplete or destination tagging is weak

---

## 6) Multi-host reconnaissance / discovery pattern

```sql
SELECT sourceip, COUNT(DISTINCT destinationip) AS unique_hosts
FROM events
GROUP BY sourceip
ORDER BY unique_hosts DESC
LAST 24 HOURS
```

**Use when:** identifying host discovery or broad reconnaissance  
**Why it matters:** wide spread can indicate scanning, mapping, or attacker exploration  
**Interpret carefully if:** the source is a known scanner, monitoring tool, or admin system

---

## Analyst note

AQL is most useful when it is used to answer a specific investigative question, not just to “look at data.”

A better workflow is:

1. form a hypothesis,
2. run the smallest query that can confirm or challenge it,
3. and document why the result changes confidence.
