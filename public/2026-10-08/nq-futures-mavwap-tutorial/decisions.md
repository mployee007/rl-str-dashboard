# Decisions Log

## 2026-10-08 — Initial playbook creation

| Decision | Rationale |
|---|---|
| Canonical file at `inputs/reference/nq-futures-mavwap-playbook.md` | Follows existing convention from credit spreads playbook |
| 15-section structure with numbered sections | More sections than the options playbook because futures add contract specs, platform config, and transition planning |
| RTH-only as a hard requirement, not a suggestion | User explicitly called this out; 24h charts dilute the 420 EMA |
| MNQ-first with explicit transition criteria | User said "micros until the system proves itself"; made the transition checklist concrete and measurable |
| Scale-out at 1:1 and 2:1 with VWAP hard exit | User provided the exit framework; structured it as a two-half system with VWAP as the override |
| Contract-sizing formula with worked examples | This is the operational core of the risk rules; two account levels shown to cover both micro and full-size |
| "Three filters must agree" as the central thesis | The user's "real refinement" paragraph makes this the core edge — encoded it everywhere |
| FOMC/CPI/NFP sit-out rule with fallback | User specified these; added the "halve size, double stop" fallback for those who insist on trading them |