# Parma Listings Pull — BLOCKED (Zillapi Out of Credits)

**Timestamp:** 2026-09-13T00:00:00-04:00
**Target ZIPs:** 44129 (Parma West), 44134 (Parma South), 44130 (Parma Heights)
**Price Cap:** $190,000
**Status:** ❌ FAILED — Zillapi credit pool exhausted

## Sources Tried

| # | Source | Method | Result |
|---|--------|--------|--------|
| 1 | Zillapi (44129) | `mcp_zillapi_search_listings` bbox: -81.78,41.37,-81.68,41.42 | ❌ Out of credits |
| 2 | Zillapi (44134) | `mcp_zillapi_search_listings` bbox: -81.72,41.35,-81.65,41.40 | ❌ MCP server unreachable (70 consecutive failures) |
| 3 | Zillapi (44130) | `mcp_zillapi_search_listings` bbox: -81.80,41.35,-81.73,41.41 | ❌ MCP server unreachable (70 consecutive failures) |

## Notes
- Zillow.com, Redfin, Trulia, Realtor.com, Homes.com, Movoto all block automated access with PerimeterX/Cloudflare captchas — not attempted.
- `web_search` and `web_extract` for listing data are also reliably blocked — not attempted per skill instructions (avoid wasting turns).
- No previously-saved JSON listing dump exists for these ZIPs — no cached data to fall back to.

## Direct Zillow Search URLs (open in your browser)

- **44129 (Parma West) under $190K:**  
  https://www.zillow.com/homes/for_sale/44129_rb/0-190000_price/0-177_mp/41.4003,-81.7078,41.3983,-81.7101_rect/13_zm/

- **44134 (Parma South) under $190K:**  
  https://www.zillow.com/homes/for_sale/44134_rb/0-190000_price/0-177_mp/41.3852,-81.6884,41.3825,-81.6913_rect/13_zm/

- **44130 (Parma Heights) under $190K:**  
  https://www.zillow.com/homes/for_sale/44130_rb/0-190000_price/0-177_mp/41.3761,-81.7715,41.3740,-81.7751_rect/13_zm/

## Next Steps
This cron job will retry on the next scheduled cycle. To resume immediately:
1. Top up Zillapi credits at https://zillapi.com/app/billing
2. Re-run the pull