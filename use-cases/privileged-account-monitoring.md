# Use Case: Privileged Account Monitoring

## Objective
Monitor suspicious authentication activity involving privileged accounts.

## Accounts of Interest
- root
- admin
- Administrator

## Why It Matters
Privileged account compromise can lead to full system control and lateral movement.

## QRadar Relevance
Observed in:
- Root Login Failed
- Repeated login failures against admin/root/Administrator

## Recommended Enhancements
- Alert separately for privileged accounts
- Increase severity when failures are followed by success
