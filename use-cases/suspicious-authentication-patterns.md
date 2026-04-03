# Use Case: Suspicious Authentication Patterns

## Objective
Identify authentication patterns that suggest attacker behavior rather than user mistakes.

## Patterns of Interest
- Repeated login failures
- Invalid / bad usernames
- Failed logins followed by success
- Privileged account targeting

## Why It Matters
Correlated patterns provide stronger confidence than isolated failed login events.

## Recommended Enhancements
- Build chained correlation rules
- Enrich with account criticality and asset context
