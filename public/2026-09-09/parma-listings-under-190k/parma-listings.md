# Parma West / Parma Listings Under $190K — Pull Blocked

**Date:** 2026-09-09  
**Target ZIPs:** 44129 (Parma West), 44134 (Parma), 44130 (Parma)  
**Price Cap:** $190,000  
**Status:** ❌ BLOCKED — Zillapi out of credits

---

## Sources Attempted

| Source | Tool | Result |
|---|---|---|
| Zillapi | `mcp_zillapi_search_listings` (44129 bbox) | **Out of credits** — "Top up or upgrade at https://zillapi.com/app/billing." |
| Zillapi | `mcp_zillapi_search_listings` (44134 bbox) | MCP server unreachable (43 consecutive failures) |
| Zillapi | `mcp_zillapi_search_listings` (44130 bbox) | MCP server unreachable (43 consecutive failures) |
| Zillow.com | web_search / web_extract / browser | Not attempted — known PerimeterX/Cloudflare block |
| Redfin | web_search / web_extract / browser | Not attempted — known PerimeterX/Cloudflare block |
| Trulia | web_search / web_extract / browser | Not attempted — known PerimeterX/Cloudflare block |
| Realtor.com | web_search / web_extract / browser | Not attempted — known PerimeterX/Cloudflare block |

---

## Direct Search URLs (Open in Your Browser)

- **ZIP 44129 under $190K:** https://www.zillow.com/homes/for_sale/44129/0-190000_price/0-372104_mp/
- **ZIP 44134 under $190K:** https://www.zillow.com/homes/for_sale/44134/0-190000_price/0-372022_mp/
- **ZIP 44130 under $190K:** https://www.zillow.com/homes/for_sale/44130/0-190000_price/0-371926_mp/

---

## Next Steps

1. Top up Zillapi credits at https://zillapi.com/app/billing
2. Re-run this cron job once credits are available
3. The job will save to `/opt/data/outputs/YYYY-MM-DD/parma-listings-under-190k/parma-listings.md`

Status file: `/opt/data/parma-pull-status.txt`