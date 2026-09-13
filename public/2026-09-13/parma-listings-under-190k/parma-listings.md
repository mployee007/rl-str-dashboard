# Parma Listings Under $190K — BLOCKED

**Pull date:** 2026-09-13 00:29 EDT  
**Target ZIPs:** 44129 (Parma West), 44134 (Parma), 44130 (Parma/Middleburg Hts)  
**Price ceiling:** $190,000  
**Result:** **No listings retrieved — all sources blocked**

---

## Source-by-Source Failure Log

| # | Source | Method | Error |
|---|--------|--------|-------|
| 1 | **Zillapi MCP** (44129) | `search_listings` | Out of credits |
| 2 | **Zillapi MCP** (44134) | `search_listings` | Server unreachable (67 failures) |
| 3 | **Zillapi MCP** (44130) | `search_listings` | Server unreachable (67 failures) |
| 4 | **Zillow.com** | Browser navigate | Captcha wall |
| 5 | **Realtor.com** | Browser navigate | Blank iframe |
| 6 | **Redfin.com** | Browser navigate | Bot detection |
| 7 | **web_search** | Firecrawl backend | Not installed (venv permissions) |

---

## Manual Fallback: Direct Zillow Links

Open these in your own browser to see current listings:

- **[44129 homes under $190K](https://www.zillow.com/parma-oh-44129/houses/?searchQueryState=%7B%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A190000%7D%2C%22sort%22%3A%7B%22value%22%3A%22pricea%22%7D%7D%7D)**
- **[44134 homes under $190K](https://www.zillow.com/parma-oh-44134/houses/?searchQueryState=%7B%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A190000%7D%2C%22sort%22%3A%7B%22value%22%3A%22pricea%22%7D%7D%7D)**
- **[44130 homes under $190K](https://www.zillow.com/middleburg-heights-oh-44130/houses/?searchQueryState=%7B%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A190000%7D%2C%22sort%22%3A%7B%22value%22%3A%22pricea%22%7D%7D%7D)**

---

## Resolution Path

1. **Zillapi credits** — top up at https://zillapi.com/app/billing
2. **Server health** — the MCP server was fully unreachable; may need restart or provider-side fix
3. **Re-run cron** — once both are green, this job will pull all three ZIPs and produce the full report
4. **Manual workaround** — forward any listing data and I'll format it to match the standard table layout

---

## Impact Radius

This affects **all** cron jobs using Zillapi:
- STR deal flow dashboard
- Multi-city submarket screens
- Parma/Ohio buy-box pulls
- Any property lookup by address

No listings = no screening, no verdicts, no buy-box updates.