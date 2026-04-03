# Use Case: Password Spray Detection

## Objective
Detect repeated authentication attempts across multiple usernames using a small set of passwords or repeated password failures.

## Detection Indicators
- Many usernames targeted
- Common usernames (admin, root, guest, test)
- Repeated failures from same source

## Why It Matters
Password spraying is designed to avoid lockouts while still discovering weak or reused credentials.

## QRadar Relevance
Observed through repeated authentication failures across multiple usernames.

## Recommended Enhancements
- Track source-to-many-user relationships
- Alert on common admin username targeting
