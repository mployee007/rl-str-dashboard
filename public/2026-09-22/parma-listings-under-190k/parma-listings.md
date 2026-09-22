# Parma West Listings Under $190K — Pull Blocked

**Date:** 2026-09-22  
**Time:** 03:43 UTC  
**Status:** ❌ Zillapi credits exhausted  
**Top-up:** https://zillapi.com/app/billing

---

## Blocker Summary

| Source | Result |
|---|---|
| **Zillapi MCP** (`mcp_zillapi_search_listings`) — ZIP 44129 | ❌ Out of credits for this cycle |
| **Zillapi MCP** (`mcp_zillapi_search_listings`) — ZIP 44134 | ❌ MCP server unreachable (14 consecutive failures) |
| **Zillapi MCP** (`mcp_zillapi_search_listings`) — ZIP 44130 | ❌ MCP server unreachable (14 consecutive failures) |
| Zillow.com (web) | ⛔ Captcha-blocked (PerimeterX) — skipped per skill guidance |
| Redfin (web) | ⛔ Captcha-blocked — skipped per skill guidance |
| Trulia/Realtor.com | ⛔ Captcha-blocked — skipped per skill guidance |

---

## Direct Zillow Search URLs (Open in Your Browser)

| ZIP | Neighborhood | Direct Zillow Link |
|---|---|---|
| **44129** | Parma West | [Zillow: 44129 under $190K](https://www.zillow.com/homes/for_sale/44129_zip/0-190000_price/0-1726_mp/41.42,-81.68,41.37,-81.78_rect/12_zm/) |
| **44134** | Parma Central | [Zillow: 44134 under $190K](https://www.zillow.com/homes/for_sale/44134_zip/0-190000_price/0-1726_mp/41.40,-81.65,41.35,-81.72_rect/12_zm/) |
| **44130** | Parma Heights | [Zillow: 44130 under $190K](https://www.zillow.com/homes/for_sale/44130_zip/0-190000_price/0-1726_mp/41.41,-81.73,41.35,-81.80_rect/12_zm/) |

---

## Bounding Boxes Used (for reference)

| ZIP | West | South | East | North |
|---|---|---|---|---|
| 44129 | -81.78 | 41.37 | -81.68 | 41.42 |
| 44134 | -81.72 | 41.35 | -81.65 | 41.40 |
| 44130 | -81.80 | 41.35 | -81.73 | 41.41 |

---

## Next Steps

1. **Top up Zillapi credits** at https://zillapi.com/app/billing
2. **Re-run the pull** — the cron job will pick up live listings automatically on its next cycle
3. **Manual fallback:** Use the direct Zillow links above to browse current listings in your own browser

*No fabricated data. This report will auto-update with real listings when Zillapi credits become available.*