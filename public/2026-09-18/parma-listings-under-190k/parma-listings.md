# Parma Submarket Listing Screen — Under $190K
**Date:** 2026-09-18  
**Status:** ⚠️ ZILLAPI CREDITS EXHAUSTED — NO LIVE DATA RETRIEVED  
**ZIPs Targeted:** 44129, 44134, 44130

---

## Bottom Line

**Zillapi credits are depleted for this billing cycle.** All three MCP calls failed (one "out of credits," two "server unreachable" after cascading failures). Web search is also unavailable (firecrawl-py not installed). No listings were retrieved; no data was fabricated. The table below records the exact state of every source attempted.

---

## Source Attempt Log

| # | Source | Target | Method | Result |
|---|---|---|---|---|
| 1 | Zillapi MCP | ZIP 44129 (bbox: -81.78,41.37,-81.68,41.42) | `search_listings` for_sale, ≤$190K | ❌ `Out of credits for this cycle` |
| 2 | Zillapi MCP | ZIP 44134 (bbox: -81.72,41.35,-81.65,41.40) | `search_listings` for_sale, ≤$190K | ❌ `MCP server unreachable (105 failures)` |
| 3 | Zillapi MCP | ZIP 44130 (bbox: -81.80,41.35,-81.73,41.41) | `search_listings` for_sale, ≤$190K | ❌ `MCP server unreachable (105 failures)` |
| 4 | Firecrawl web search | Zillow.com 44129 | `web_search` | ❌ `firecrawl-py not installed (lazy installs disabled)` |
| 5 | Firecrawl web search | Redfin.com 44129 | `web_search` | ❌ `firecrawl-py not installed (lazy installs disabled)` |

---

## Direct Zillow Search URLs

Open in any browser to replicate what Zillapi would have returned:

| ZIP | Neighborhood | Direct Zillow Link |
|---|---|---|
| **44129** | Parma West (Ridgewood, State Rd corridor) | [Open on Zillow →](https://www.zillow.com/parma-oh-44129/houses/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-81.78%2C%22east%22%3A-81.68%2C%22south%22%3A41.37%2C%22north%22%3A41.42%7D%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A190000%7D%2C%22mp%22%3A%7B%22min%22%3A1%7D%7D%2C%22isMapVisible%22%3Atrue%7D) |
| **44134** | Parma South / Garfield Heights border | [Open on Zillow →](https://www.zillow.com/parma-oh-44134/houses/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-81.72%2C%22east%22%3A-81.65%2C%22south%22%3A41.35%2C%22north%22%3A41.4%7D%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A190000%7D%2C%22mp%22%3A%7B%22min%22%3A1%7D%7D%2C%22isMapVisible%22%3Atrue%7D) |
| **44130** | Parma SE / Middleburg Heights | [Open on Zillow →](https://www.zillow.com/parma-oh-44130/houses/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-81.8%2C%22east%22%3A-81.73%2C%22south%22%3A41.35%2C%22north%22%3A41.41%7D%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A190000%7D%2C%22mp%22%3A%7B%22min%22%3A1%7D%7D%2C%22isMapVisible%22%3Atrue%7D) |

---

## No Listings Table — No Data Retrieved

The listing tables and investor verdict columns requested cannot be populated. When Zillapi credits refresh, the pipeline will:

1. Pull all three bounding boxes in parallel
2. Deduplicate across ZIPs
3. Sort by price ascending
4. Add investor verdicts using price-to-rent ratios
5. Save to this report and update the quick-reference file

---

## Next Steps

| Action | Detail |
|---|---|
| **Wait for credit refresh** | Zillapi credits replenish on billing cycle; pull will auto-resume when available |
| **Manual screening** | Use the three direct Zillow URLs above to browse listings now |
| **Re-run cron** | This job will attempt the pull again on next scheduled run |
| **Top up credits** | Visit [zillapi.com/app/billing](https://zillapi.com/app/billing) to add credits immediately |

---

## Files Written

| File | Content |
|---|---|
| `/opt/data/parma-pull-status.txt` | Timestamped failure log with error details and Zillow URLs |
| `/opt/data/outputs/2026-09-18/parma-listings-under-190k/parma-listings.md` | This report |

---

*No listings were fabricated. All data above reflects actual tool outcomes.*