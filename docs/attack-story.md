# Attack Story

## Narrative Summary
The reviewed QRadar offenses suggest a realistic attacker workflow rather than isolated unrelated alerts.

A practical interpretation of the activity is:

1. **Reconnaissance / probing**  
   Honeypot and tarpit-related alerts suggest early discovery behavior.

2. **Account discovery**  
   Invalid and bad username attempts suggest the actor may have been testing naming patterns and account validity.

3. **Credential abuse attempts**  
   Repeated authentication failures and broad username targeting are consistent with brute force or password spraying behavior.

4. **Potential access validation**  
   The fail-to-success offense is the most operationally important pattern because it suggests that at least some authentication attempts may have progressed beyond failure.

5. **Higher-value targeting**  
   Privileged account names increase the seriousness of the activity and should raise triage priority.

## Why This Matters
This is exactly the kind of analyst story-building expected in a SOC:

- not just acknowledging alerts,
- but connecting them into a meaningful sequence of behavior.
