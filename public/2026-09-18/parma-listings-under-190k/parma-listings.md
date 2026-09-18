# Parma Listings — Under $190K

**Date:** 2026-09-18  
**Status:** ❌ BLOCKED — Zillapi out of credits  
**ZIPs:** 44129 (Parma West), 44134 (Parma), 44130 (Parma/Middleburg Hts)

---

## Blocker Summary

| Source | Attempted | Result |
|---|---|---|
| Zillapi MCP (`mcp_zillapi_search_listings`) — 44129 | ✅ Called | Out of credits |
| Zillapi MCP (`mcp_zillapi_search_listings`) — 44134 | ✅ Called | Server unreachable |
| Zillapi MCP (`mcp_zillapi_search_listings`) — 44130 | ✅ Called | Server unreachable |
| Zillow.com / Redfin / Trulia / Realtor.com | ⛔ Skipped | Known captcha blocks (PerimiterX/Cloudflare) — per skill directive |

---

## Manual Fallback — Direct Zillow Search URLs

While Zillapi credits are exhausted, these direct Zillow URLs can be opened in a browser to view current listings:

- **44129 (Parma West):** https://www.zillow.com/homes/for_sale/44129_house_type/0-190000_price/0-189_mp/
- **44134 (Parma):** https://www.zillow.com/homes/for_sale/44134_house_type/0-190000_price/0-189_mp/
- **44130 (Parma / Middleburg Hts):** https://www.zillow.com/homes/for_sale/44130_house_type/0-190000_price/0-189_mp/

---

## Next Steps

1. **Top up Zillapi credits** at https://zillapi.com/app/billing
2. Pipeline will retry on **next scheduled cron run**
3. Raw data will be saved as `cleveland_zip_stats.json` and `cleveland_clean.json` when pull succeeds

Status file: `/opt/data/parma-pull-status.txt`