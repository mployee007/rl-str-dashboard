# Parma Listings Pull — BLOCKED

**Timestamp:** 2026-09-10T15:45:20Z  
**Status:** ❌ Zillapi credits exhausted + MCP server unreachable  
**Task:** Pull active for-sale house listings in ZIPs 44129, 44134, 44130 (max $190,000)

---

## Blocker Summary

All Zillapi MCP calls failed:

| Source | Endpoint | Result |
|---|---|---|
| Zillapi MCP | `search_listings` (44129 bbox) | ❌ "Out of credits for this cycle. Top up or upgrade at https://zillapi.com/app.billing." |
| Zillapi MCP | `search_listings` (44134 bbox) | ❌ "MCP server 'zillapi' is unreachable after 48 consecutive failures." |
| Zillapi MCP | `search_listings` (44130 bbox) | ❌ "MCP server 'zillapi' is unreachable after 48 consecutive failures." |

Per the skill's data-source strategy, all web-based real estate sites (Zillow.com, Redfin, Trulia, Realtor.com, Homes.com, Movoto) are known to block browser/curl access with PerimeterX/Cloudflare captchas, so no fallback web scraping was attempted.

---

## Manual Fallback URLs

The user can open these directly in a browser to see live listings:

| ZIP | Direct Zillow Search URL |
|---|---|
| 44129 | https://www.zillow.com/homes/for_sale/44129_rid/0-190000_price/0-1318_mp/ |
| 44134 | https://www.zillow.com/homes/for_sale/44134_rid/0-190000_price/0-1318_mp/ |
| 44130 | https://www.zillow.com/homes/for_sale/44130_rid/0-190000_price/0-1318_mp/ |

---

## Resolution

- **Top up Zillapi credits** at https://zillapi.com/app/billing
- **Re-run the cron task** once credits are available
- The task will auto-save raw JSON to `/opt/data/outputs/<date>/parma-listings-under-190k/` for downstream queries