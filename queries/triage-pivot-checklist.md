# Triage Pivot Checklist

## When investigating a QRadar offense, pivot on:

### Source IP
- Has this source appeared in other offenses?
- Is it internal, external, lab, or admin-owned?
- Did it target multiple users or hosts?

### Destination IP
- Is the target a critical system?
- Is it a honeypot / tarpit / decoy?
- Was it targeted repeatedly?

### Username
- Is the username valid?
- Is it privileged?
- Was it used in failed-then-success authentication?

### Event Pattern
- Failed only?
- Failed then success?
- Invalid username first, valid username later?
- Honeypot interaction followed by auth attempts?

### Escalation Conditions
Escalate quickly if:
- privileged accounts are involved
- failures are followed by success
- honeypot/tarpit assets are touched
- repeated behavior occurs from the same source
