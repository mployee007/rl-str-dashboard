# Run Log — NQ Futures EMA/VWAP Tutorial

## 2026-10-08

### 13:38 UTC — Session initialized
- Created output structure: `outputs/2026-10-08/nq-futures-ema-vwap-tutorial/`
- Loaded options-strategy-playbooks skill for structural template
- Loaded output-organization skill for file conventions

### 13:39 UTC — Contract spec research
- Web search (SearXNG) degraded — Bing-only results, mostly AWS noise
- CME curl blocked (JS challenge)
- Retrieved NQ specs via browser → confirmed $20/point, $5/tick, RTH hours
- Retrieved MNQ specs via browser → confirmed $2/point, $0.50/tick

### 13:40 UTC — Playbook written
- Wrote canonical playbook: `inputs/reference/nq-futures-ema-vwap-playbook.md` (~16KB, 13 sections)
- Includes: instrument specs table, chart setup, entry/exit rules, risk sizing formula + tables, worked examples, pre-trade checklist, journal template, common mistakes, glossary

### 13:40 UTC — Session files written
- summary.md, sources.json, decisions.md, run-log.md initialized
- Snapshot mirrored to artifacts/exports/