# Use Case: Brute Force Detection

## Objective
Detect repeated failed authentication attempts against the same user or destination within a short time window.

## Detection Logic
- Multiple failed login attempts
- Same source or multiple sources
- Same username or same destination host
- Repeated authentication failure events

## Why It Matters
Brute-force attacks may lead to unauthorized access if credentials are guessed successfully.

## QRadar Relevance
Observed across:
- Multiple Login Failures for the Same User
- Repeated Windows Login Failures
- Repeated Non-Windows Login Failures

## Recommended Enhancements
- Prioritize privileged accounts
- Correlate with eventual success
- Enrich with source asset context
