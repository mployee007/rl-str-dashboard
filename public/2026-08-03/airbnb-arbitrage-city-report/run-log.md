# Run Log — Airbnb Arbitrage City Report

## 2026-08-03

### Initialized session output structure
- Created standard output files and artifact directories.

### Pulled rental inventory
- Queried Nashville and Columbus rental markets via Zillapi and Craigslist workflows.
- Zillapi returned mostly apartment inventory; Craigslist produced the usable SFH/townhome leads.

### Underwrote shortlist
- Applied conservative / moderate / optimistic ADR and occupancy cases.
- Filtered to properties exceeding a moderate-case spread of $1,300/month.
- Saved final report to artifacts/exports/nashville-columbus-sfh-townhome-shortlist.md.
