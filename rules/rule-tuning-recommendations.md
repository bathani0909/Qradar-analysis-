# Rule Tuning Recommendations

## Goal
Improve signal quality while preserving meaningful authentication and reconnaissance detections.

## Recommended Tuning Ideas

### 1) Suppress known internal scanners or expected testing sources
If a known security tool or lab host repeatedly touches honeypot-style assets, suppress or label it appropriately.

### 2) Raise priority when failures target privileged accounts
Authentication failures involving `root`, `admin`, or `Administrator` should carry more weight than generic low-value accounts.

### 3) Increase confidence for fail-to-success patterns
A success event following repeated failures should be treated as higher priority than failure-only behavior.

### 4) Reduce noise from isolated single-user typos
Single-user, low-volume authentication mistakes should not be prioritized the same way as broad multi-account attempts.
