# Use Case: Honeypot / Tarpit Detection

## Objective
Detect suspicious communication with decoy or trap assets.

## Why It Matters
Legitimate systems should rarely interact with honeypots. Such interactions often indicate scanning, probing, or unauthorized behavior.

## QRadar Relevance
Observed through:
- Access to Honeypot or Tarpit Defined Address

## Recommended Enhancements
- Prioritize internal source systems
- Correlate with auth failures and scanning activity
