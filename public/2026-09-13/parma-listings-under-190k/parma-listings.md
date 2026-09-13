# Parma, OH — Listings Under $190K
**Pull date:** 2026-09-13  
**Target ZIPs:** 44129 (Parma West), 44134 (Parma South), 44130 (Parma Heights)  
**Status:** ❌ BLOCKED — No data retrieved

---

## Blocker Summary

All data sources exhausted. Zillapi is out of credits and the MCP server became unreachable mid-pull. Web sources (Zillow.com, Realtor.com) block non-browser access with PerimeterX/Cloudflare captchas. The firecrawl web extraction dependency is not installed and the system venv is read-only, preventing a just-in-time install.

---

## Sources Attempted

| # | Source | Method | Result |
|---|--------|--------|--------|
| 1 | Zillapi | `mcp_zillapi_search_listings` (44129) | ❌ Out of credits for this cycle |
| 2 | Zillapi | `mcp_zillapi_search_listings` (44134) | ❌ Server unreachable (73 consecutive failures) |
| 3 | Zillapi | `mcp_zillapi_search_listings` (44130) | ❌ Server unreachable (73 consecutive failures) |
| 4 | Zillow.com | Browser (`browser_navigate`) | ❌ PerimeterX captcha — "Access Denied" |
| 5 | Realtor.com | `web_extract` | ❌ firecrawl not installed / captcha-blocked |
| 6 | Web search | `web_search` | ❌ firecrawl not installed |

---

## Manual Workaround

Open these URLs in a regular browser to view current listings:

- **44129:** https://www.zillow.com/parma-oh-44129/houses/under-190000_sort-pricedays_sort.asc/
- **44134:** https://www.zillow.com/parma-oh-44134/houses/under-190000_sort-pricedays_sort.asc/
- **44130:** https://www.zillow.com/parma-heights-oh-44130/houses/under-190000_sort-pricedays_sort.asc/

---

## Next Steps

1. Top up Zillapi credits at https://zillapi.com/app/billing
2. Re-run this cron job after credits refresh
3. Alternatively, install firecrawl (`uv pip install firecrawl-py`) in a writable venv for web extraction fallback