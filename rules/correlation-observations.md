# Correlation Observations

## Key Observation
Many of the QRadar offenses observed in this dataset appear to represent different perspectives of the same broader attack sequence rather than completely independent incidents.

## Examples
- Multiple Login Failures
- Root Login Failed
- Bad Username
- Login Failures Followed by Success
- Repeated Windows / Non-Windows Login Failures

## Analyst Interpretation
This suggests:
- attacker iteration
- account discovery
- credential abuse
- privilege targeting
- possible successful access

## Triage Recommendation
Analysts should group related authentication offenses together instead of treating each row as a separate incident.
