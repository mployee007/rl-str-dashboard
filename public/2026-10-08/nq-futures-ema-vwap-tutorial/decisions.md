# Decisions — NQ Futures EMA/VWAP Tutorial

## 2026-10-08

### Decision: Use options-strategy-playbooks skill format as structural template
- **Context:** Needed a canonical playbook structure for a futures strategy tutorial
- **Options considered:** Freeform markdown, options-playbook format, video script
- **Decision:** Adapted the options-strategy-playbooks outline (sections 1-13 structure, canonical + snapshot pattern) for futures
- **Consequence:** Consistent format across trading strategy playbooks; easy to integrate future research

### Decision: Store canonical playbook in inputs/reference/
- **Context:** Playbook should persist and be updatable across sessions
- **Options considered:** Session-only output, AGENTS.md, inputs/reference/
- **Decision:** `inputs/reference/nq-futures-ema-vwap-playbook.md` as canonical, with session snapshot in `outputs/.../artifacts/exports/`
- **Consequence:** Follows established project convention for reusable reference files

### Decision: Retrieve live CME contract specs via browser
- **Context:** Firecrawl/web_extract unavailable; searches returning garbage
- **Options considered:** Trust user-provided numbers, try browser, skip verification
- **Decision:** Used browser to navigate to CME contract spec pages and extract verified specs
- **Consequence:** Confirmed NQ @ $20/point, MNQ @ $2/point, tick sizes, and session hours from official source