# Parma Listings Under $190K — Pull Report
**Generated:** 2026-09-07 (cron run)
**Status:** ❌ FAILED — Zillapi out of credits

---

## Executive Summary

The scheduled pull for ZIPs **44129** (Parma West), **44134** (Parma), and **44130** (Middleburg Heights / Parma Heights) could not complete. Zillapi returned **"Out of credits for this cycle"** on the primary call, and the MCP server became unreachable on subsequent attempts. Zero listings were retrieved.

---

## Source Attempts

| # | Source | Target | Method | Result |
|---|--------|--------|--------|--------|
| 1 | Zillapi MCP | ZIP 44129 | `mcp_zillapi_search_listings` (bbox: -81.78,41.37,-81.68,41.42, price_max=$190K, for_sale) | **Out of credits** |
| 2 | Zillapi MCP | ZIP 44134 | `mcp_zillapi_search_listings` (bbox: -81.72,41.35,-81.65,41.40, price_max=$190K, for_sale) | MCP server unreachable (28 failures) |
| 3 | Zillapi MCP | ZIP 44130 | `mcp_zillapi_search_listings` (bbox: -81.80,41.35,-81.73,41.41, price_max=$190K, for_sale) | MCP server unreachable (28 failures) |

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

*No listings were fabricated. This report reflects only real tool output. Resume when Zillapi credits are available.*