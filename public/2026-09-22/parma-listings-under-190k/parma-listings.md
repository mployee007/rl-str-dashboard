# Parma West Listings Under $190K — Pull Blocked

**Date:** 2026-09-22  
**Status:** ❌ Zillapi credits exhausted  
**Top-up:** https://zillapi.com/app/billing

---

## Blocker Summary

| Source | Result |
|---|---|
| **Zillapi MCP** (`mcp_zillapi_search_listings`) | ❌ Out of credits — all 3 ZIP pulls rejected |
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
2. **Re-run this cron job** — it will auto-detect fresh credits and pull all three ZIPs
3. **Manual fallback:** Use the direct Zillow links above in your browser for an immediate look

---

*No listings were fabricated. This report reflects the actual blocker encountered on 2026-09-22.*