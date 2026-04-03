# Useful AQL Queries

## 1) Find repeated authentication failures by source IP

**Purpose**  
Identify whether a single source IP is repeatedly attempting authentication across multiple accounts or systems.

```sql
SELECT sourceip, username, COUNT(*) AS fail_count
FROM events
WHERE LOGSOURCETYPENAME(devicetype) ILIKE '%auth%'
GROUP BY sourceip, username
ORDER BY fail_count DESC
LAST 24 HOURS
```

## 2) Look for fail-then-success patterns

```sql
SELECT starttime, sourceip, destinationip, username, QIDNAME(qid) AS event_name
FROM events
WHERE username IS NOT NULL
ORDER BY starttime DESC
LAST 24 HOURS
```

## 3) Review bad / invalid usernames

```sql
SELECT sourceip, username, COUNT(*) AS attempts
FROM events
WHERE username IS NOT NULL
GROUP BY sourceip, username
ORDER BY attempts DESC
LAST 24 HOURS
```
