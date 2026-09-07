# Parma Listings Under $190K — Pull Report
**Generated:** 2026-09-07 15:30 UTC (cron run #2)
**Status:** ❌ FAILED — Zillapi unavailable

---

## Executive Summary

The scheduled pull for ZIPs **44129** (Parma West), **44134** (Parma), and **44130** (Middleburg Heights / Parma Heights) could not complete. Zillapi returned **"Out of credits for this cycle"** on the 44129 call, and the MCP server was unreachable on both 44134 and 44130. Zero listings were retrieved.

This is the second failed run today. The historical baseline from `cleveland_zip_stats.json` provides stale but directionally useful reference numbers for these ZIPs.

---

## Source Attempts

| # | Source | Target | Method | Result |
|---|--------|--------|--------|--------|
| 1 | Zillapi MCP | ZIP 44129 | `mcp_zillapi_search_listings` (bbox: -81.78,41.37,-81.68,41.42, price_max=$190K, for_sale) | **Out of credits** |
| 2 | Zillapi MCP | ZIP 44134 | `mcp_zillapi_search_listings` (bbox: -81.72,41.35,-81.65,41.40, price_max=$190K, for_sale) | MCP server unreachable (29 failures) |
| 3 | Zillapi MCP | ZIP 44130 | `mcp_zillapi_search_listings` (bbox: -81.80,41.35,-81.73,41.41, price_max=$190K, for_sale) | MCP server unreachable (29 failures) |

---

## Historical Baseline (from cleveland_zip_stats.json)

This is the last known live-pull data — directionally useful, not current:

| ZIP | Area | Sale Count | Median Sale | Rent Count | Median Rent | GRM | Gross Yield |
|-----|------|-----------|-------------|-----------|-------------|-----|-------------|
| 44129 | Parma West | 16 | $190,000 | 30 | $1,950 | 8.1 | 12.32% |
| 44134 | Parma East / Brooklyn Hts / Seven Hills | 44 | $200,000 | 32 | $1,675 | 10.0 | 10.05% |
| 44130 | Middleburg Hts / Parma Hts (mid) | 7 | $199,900 | 0 | $1,575 | 10.6 | 9.45% |

**Key takeaway from historical data:** At the $190K cap, 44129 is the only ZIP where the median sale sits at the cap (half the market is at/under). In 44134 and 44130, median sales sit above $190K, so the sub-$190K slice is the bottom of those markets — likely smaller homes, fixers, or distressed properties.

---

## Investor Context (using historical data)

### 44129 — Parma West: Best yield zone
- **Median sale $190K / median rent $1,950 → GRM 8.1 (12.3% gross yield)**
- Highest yield of the three. At sub-$190K, you're buying below median — could push gross yield toward 13-14%.
- **Verdict: TAKE SELECTIVELY** — best cash-flow ZIP of the three. Screen for block quality near York/State roads; avoid the industrial edges.

### 44134 — Parma East / Seven Hills: Mixed bag
- **Median sale $200K / median rent $1,675 → GRM 10.0 (10.1% yield)**
- Sub-$190K slice is the bottom quartile. Expect smaller sqft, older builds (1950s-60s), or cosmetic needs.
- **Verdict: NEGOTIATE** — only at $160K or below with verified rent over $1,500. Not a yield play at retail.

### 44130 — Middleburg Heights / Parma Heights: Thin at cap
- **Median sale $199,900 / median rent $1,575 → GRM 10.6 (9.5% yield)**
- Only 7 properties in the historical pull. Sub-$190K slice is tiny and likely needs rehab.
- **Verdict: PASS** — yield too thin at $190K cap. Better value in 44129 for the same price band.

---

## What To Do

1. **Top up credits** at https://zillapi.com/app/billing and re-run the cron job
2. **Manual fallback** — open these direct Zillow searches in a browser:

| ZIP | Area | Direct Zillow Link |
|-----|------|-------------------|
| 44129 | Parma West | [Open in Zillow](https://www.zillow.com/parma-oh-44129/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%2244129%22%2C%22mapBounds%22%3A%7B%22west%22%3A-81.78%2C%22east%22%3A-81.68%2C%22south%22%3A41.37%2C%22north%22%3A41.42%7D%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A190000%7D%7D%2C%22isListVisible%22%3Atrue%7D) |
| 44134 | Parma | [Open in Zillow](https://www.zillow.com/parma-oh-44134/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%2244134%22%2C%22mapBounds%22%3A%7B%22west%22%3A-81.72%2C%22east%22%3A-81.65%2C%22south%22%3A41.35%2C%22north%22%3A41.40%7D%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A190000%7D%7D%2C%22isListVisible%22%3Atrue%7D) |
| 44130 | Middleburg Hts / Parma Hts | [Open in Zillow](https://www.zillow.com/parma-heights-oh-44130/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%2244130%22%2C%22mapBounds%22%3A%7B%22west%22%3A-81.80%2C%22east%22%3A-81.73%2C%22south%22%3A41.35%2C%22north%22%3A41.41%7D%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A190000%7D%7D%2C%22isListVisible%22%3Atrue%7D) |

---

*No listings were fabricated. This report reflects only real tool output and historical baseline data. Resume when Zillapi credits are available.*