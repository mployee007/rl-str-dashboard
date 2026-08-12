# Decisions — Multi-City STR Arbitrage Scan

## 2026-08-10

### Decision: Use uploaded ZIP reference list first, fallback to core ZIPs when absent
- **Context:** User requested ZIP-focused search tied to uploaded reference file.
- **Options considered:** Restrict only to listed cities vs. cover all requested cities with fallbacks.
- **Decision:** Use reference ZIPs where present; use core-city ZIP fallback when the file lacks that city.
- **Consequence:** Maintains coverage across all requested markets while honoring the uploaded list where possible.
