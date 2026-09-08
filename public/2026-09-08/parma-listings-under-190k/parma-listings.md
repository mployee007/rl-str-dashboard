# Parma Listings Under $190K — Pull Report
**Generated:** 2026-09-08 (cron run #3)
**Status:** ❌ FAILED — Zillapi unavailable (3rd consecutive failure)

---

## Executive Summary

The scheduled pull for ZIPs **44129** (Parma West), **44134** (Parma), and **44130** (Middleburg Heights / Parma Heights) could not complete. This is the **third consecutive failed run** across 2 days.

- **44129:** Zillapi returned "Out of credits for this cycle"
- **44134:** MCP server unreachable (30 consecutive failures)  
- **44130:** MCP server unreachable (30 consecutive failures)

Zero listings were retrieved. The historical baseline from `cleveland_zip_stats.json` provides stale but directionally useful reference numbers.

---

## Source Attempts (2026-09-08)

| # | Source | Target | Method | Result |
|---|--------|--------|--------|--------|
| 1 | Zillapi MCP | ZIP 44129 | `mcp_zillapi_search_listings` (bbox: -81.78,41.37,-81.68,41.42, price_max=$190K, for_sale) | **Out of credits** |
| 2 | Zillapi MCP | ZIP 44134 | `mcp_zillapi_search_listings` (bbox: -81.72,41.35,-81.65,41.40, price_max=$190K, for_sale) | MCP server unreachable (30 failures) |
| 3 | Zillapi MCP | ZIP 44130 | `mcp_zillapi_search_listings` (bbox: -81.80,41.35,-81.73,41.41, price_max=$190K, for_sale) | MCP server unreachable (30 failures) |

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

## Failure History

| Date | Run | 44129 | 44134 | 44130 |
|------|-----|-------|-------|-------|
| 2026-09-07 #1 | Cron | Out of credits | Out of credits | Out of credits |
| 2026-09-07 #2 | Cron | Out of credits | MCP unreachable | MCP unreachable |
| 2026-09-08 #3 | Cron | Out of credits | MCP unreachable | MCP unreachable |

---

## What To Do

1. **Top up credits** at https://zillapi.com/app/billing — the pool has been empty for 3 consecutive runs across 2 days. This is a billing issue, not a transient one.
2. **Check MCP server health** — even if credits are restored, the Zillapi MCP server must be reachable (30 consecutive failures on 44134/44130).
3. **Manual fallback** — open these direct Zillow searches in a browser:

| ZIP | Area | Direct Zillow Link |
|-----|------|-------------------|
| 44129 | Parma West | [Open in Zillow](https://www.zillow.com/parma-oh-44129/?searchQueryState={"pagination":{},"usersSearchTerm":"44129","mapBounds":{"west":-81.78,"east":-81.68,"south":41.37,"north":41.42},"filterState":{"price":{"max":190000}},"isListVisible":true}) |
| 44134 | Parma | [Open in Zillow](https://www.zillow.com/parma-oh-44134/?searchQueryState={"pagination":{},"usersSearchTerm":"44134","mapBounds":{"west":-81.72,"east":-81.65,"south":41.35,"north":41.40},"filterState":{"price":{"max":190000}},"isListVisible":true}) |
| 44130 | Middleburg Hts / Parma Hts | [Open in Zillow](https://www.zillow.com/parma-heights-oh-44130/?searchQueryState={"pagination":{},"usersSearchTerm":"44130","mapBounds":{"west":-81.80,"east":-81.73,"south":41.35,"north":41.41},"filterState":{"price":{"max":190000}},"isListVisible":true}) |

---

*No listings were fabricated. This report reflects only real tool output and historical baseline data. Resume when Zillapi credits are available and the MCP server is healthy.*