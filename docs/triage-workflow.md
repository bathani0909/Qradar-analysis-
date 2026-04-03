# Triage Workflow

## Initial Review
- Open offense in QRadar
- Review magnitude, category, and offense timeline
- Identify the triggering rule(s)

## Entity Pivoting
- Check source IP
- Check destination IP
- Check username / account
- Review asset context

## Event Validation
- Review raw event names and payloads
- Confirm whether the activity is repeated, correlated, or isolated

## Risk Decision
Classify the offense as:
- True Positive
- False Positive
- Benign / Expected
- Needs Further Investigation

## Documentation
Record:
- What happened
- Why it triggered
- What it means
- Recommended action
