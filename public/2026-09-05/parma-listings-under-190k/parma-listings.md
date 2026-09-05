# Parma Listings Under $190K — Pull Failed

**Date:** 2026-09-05  
**Status:** ❌ Zillapi credits exhausted

---

## Blocker

Zillapi returned **"Out of credits for this cycle"** on the first call (ZIP 44129), and the MCP server became unreachable on subsequent calls. No live listing data could be retrieved.

## Sources Tried

| Source | Result |
|--------|--------|
| Zillapi MCP (`mcp_zillapi_search_listings`) — ZIP 44129 | ❌ Out of credits |
| Zillapi MCP (`mcp_zillapi_search_listings`) — ZIP 44134 | ❌ Server unreachable (cascade) |
| Zillapi MCP (`mcp_zillapi_search_listings`) — ZIP 44130 | ❌ Server unreachable (cascade) |
| Zillow.com direct browser | 🔒 PerimeterX/Cloudflare blocked |
| Redfin.com direct browser | 🔒 Captcha blocked |
| web_search / web_extract | 🔒 All major listing sites block automated access |

## Direct Zillow Search URLs (open in your own browser)

- **[44129 — Parma West, under $190K](https://www.zillow.com/parma-oh-44129/houses/under-190000_sort/)**  
- **[44134 — Parma Central, under $190K](https://www.zillow.com/parma-oh-44134/houses/under-190000_sort/)**  
- **[44130 — Parma South, under $190K](https://www.zillow.com/parma-oh-44130/houses/under-190000_sort/)**

## Next Step

Re-run this pull when Zillapi credits are restored. Top up at: https://zillapi.com/app/billing

The bounding boxes are saved in `/opt/data/parma-pull-status.txt` for re-use.