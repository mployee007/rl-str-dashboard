# Parma West Area — Listings Under $190K
**Generated:** 2026-09-08  
**Status:** ❌ BLOCKED — Zillapi out of credits  
**Target ZIPs:** 44129 (Parma West), 44134 (Parma South), 44130 (Middleburg Heights)

---

## Blocked: Zillapi Credits Exhausted

All three Zillapi bounding-box queries failed with credit exhaustion. No live listing data was retrieved.

### Sources Attempted

| # | Source | Method | Result |
|---|---|---|---|
| 1 | Zillapi MCP | `mcp_zillapi_search_listings` (44129 bbox) | ❌ Out of credits for this cycle |
| 2 | Zillapi MCP | `mcp_zillapi_search_listings` (44134 bbox) | ❌ MCP server unreachable (retry cooldown) |
| 3 | Zillapi MCP | `mcp_zillapi_search_listings` (44130 bbox) | ❌ MCP server unreachable (retry cooldown) |

No alternative web sources were attempted because Zillow.com, Redfin, Trulia, Realtor.com, Homes.com, and Movoto all block automated access with PerimeterX/Cloudflare captchas (per the `real-estate-submarket-screening` skill protocol).

---

## Direct Zillow Search URLs (Manual Fallback)

Open these in your browser to view active for-sale listings under $190K:

### 44129 — Parma West
🔗 [Zillow: 44129, For Sale, Max $190K](https://www.zillow.com/parma-oh-44129/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%2244129%22%2C%22mapBounds%22%3A%7B%22west%22%3A-81.78%2C%22east%22%3A-81.68%2C%22south%22%3A41.37%2C%22north%22%3A41.42%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A%22postal_code%22%2C%22regionIndex%22%3A0%7D%5D%2C%22filterState%22%3A%7B%22maxPrice%22%3A%7B%22value%22%3A190000%7D%2C%22isAllHomes%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isMapVisible%22%3Atrue%2C%22isListVisible%22%3Atrue%7D)

### 44134 — Parma South
🔗 [Zillow: 44134, For Sale, Max $190K](https://www.zillow.com/parma-oh-44134/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%2244134%22%2C%22mapBounds%22%3A%7B%22west%22%3A-81.72%2C%22east%22%3A-81.65%2C%22south%22%3A41.35%2C%22north%22%3A41.40%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A%22postal_code%22%2C%22regionIndex%22%3A0%7D%5D%2C%22filterState%22%3A%7B%22maxPrice%22%3A%7B%22value%22%3A190000%7D%2C%22isAllHomes%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isMapVisible%22%3Atrue%2C%22isListVisible%22%3Atrue%7D)

### 44130 — Middleburg Heights
🔗 [Zillow: 44130, For Sale, Max $190K](https://www.zillow.com/middleburg-heights-oh-44130/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%2244130%22%2C%22mapBounds%22%3A%7B%22west%22%3A-81.80%2C%22east%22%3A-81.73%2C%22south%22%3A41.35%2C%22north%22%3A41.41%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A%22postal_code%22%2C%22regionIndex%22%3A0%7D%5D%2C%22filterState%22%3A%7B%22maxPrice%22%3A%7B%22value%22%3A190000%7D%2C%22isAllHomes%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isMapVisible%22%3Atrue%2C%22isListVisible%22%3Atrue%7D)

---

## Next Steps

1. **Top up Zillapi credits** at https://zillapi.com/app/billing
2. **Re-run this cron job** — it will pick up from the saved status file and produce the full listing table
3. **Or manually review** the direct Zillow URLs above to spot-check current inventory

The report structure (sorted-price tables with take/negotiate/pass verdicts, price-to-rent analysis, and buy-box thresholds) will populate automatically when credits are available.

---

## No Fabricated Listings

Per protocol: no listing data, rent estimates, or property details were fabricated. This report reflects only what the tools returned. When credits refresh, the automated pipeline will produce:
- Full markdown listing tables for each ZIP
- Investor verdict columns
- Price-to-rent ratio analysis
- `/opt/data/parma-latest-listings.md` quick-reference file