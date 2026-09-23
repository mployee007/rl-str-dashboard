# Parma Listing Pull Summary — 2026-09-23

- **Source:** Zillow.com via Camofox browser (headless Firefox)
- **Zillapi:** Unavailable (out of credits; MCP server also went unreachable)
- **Search tool (web_search):** Blocked — firecrawl-py not installed, no permission to install
- **SearXNG (agent_search):** Degraded — only Bing working, returns Parma Italy not Ohio
- **Listings found:** 10 houses + 1 vacant lot across 44129, 44134, 44130
- **Zillow captcha:** Triggered on individual property pages and rental search — could not get Zestimates
- **Rent estimates:** Market-derived ($1,350/mo 3br, $1,050/mo 2br) — NOT property-specific

## Files
- `parma-listings.md` — Full report with tables, verdicts, and recommendations
- `parma-listings-raw.json` — Structured JSON with all fields
- `/opt/data/parma-latest-listings.md` — Quick reference table for one-glance access

## Top 3 Leads
1. **7611 Newport Ave** — $174,900, 3/1, GRM 10.8x, fresh 2hr listing → ACT FAST
2. **10366 Manorford Dr** — $119,900, 2/1, GRM 9.5x, possible distress → verify condition
3. **7101 Brownfield Dr** — $189,900, 3/1, 2,186 sqft, best value per sqft → negotiate down

## Next Run Improvements
- Wait for Zillapi credit refresh for property-specific Zestimates
- Try to install firecrawl-py for web_search fallback
- Consider narrower 44134 bbox to find more inventory