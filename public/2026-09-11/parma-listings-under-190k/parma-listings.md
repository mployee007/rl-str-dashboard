# Parma Listings Under $190K — Pull Report
**Date:** 2026-09-11  
**Status:** ❌ FAILED — All data sources unavailable

---

## Bottom Line

No for-sale listings could be retrieved for ZIPs 44129, 44134, or 44130. Zillapi is out of credits, the MCP server is unreachable, and all web-based fallbacks (Zillow.com, Redfin) are blocked by bot detection or missing backend dependencies (`firecrawl-py` not installed and uninstallable due to filesystem permissions).

---

## Attempt Log

| # | Source | Method | Target | Result |
|---|--------|--------|--------|--------|
| 1 | Zillapi MCP | `mcp_zillapi_search_listings` | 44129 bbox | ❌ Out of credits |
| 2 | Zillapi MCP | `mcp_zillapi_search_listings` | 44134 bbox | ❌ MCP server unreachable (56 failures) |
| 3 | Zillapi MCP | `mcp_zillapi_search_listings` | 44130 bbox | ❌ MCP server unreachable (56 failures) |
| 4 | Zillow.com | `browser_navigate` | 44129 filtered search | ❌ Blocked — captcha wall |
| 5 | Zillow.com | `web_extract` | 44129 houses page | ❌ firecrawl-py not installed |
| 6 | Redfin.com | `web_extract` | Parma city page | ❌ firecrawl-py not installed |
| 7 | Web Search | `web_search` | site:zillow.com 44129 | ❌ firecrawl-py not installed |
| 8 | Dependency fix | `uv pip install firecrawl-py` | — | ❌ Permission denied |
| 9 | Dependency fix | `sudo` / `pip` | — | ❌ Not available |

---

## Direct Zillow Search URLs (Open in Your Browser)

These filtered URLs will show active listings in each ZIP under $190K:

- **44129 (Parma West):**  
  https://www.zillow.com/parma-oh-44129/houses/?searchQueryState={"filterState":{"price":{"max":190000},"sort":{"value":"globalrelevanceex"},"fsba":{"value":false},"fsbo":{"value":false},"nc":{"value":false},"fore":{"value":false},"cmsn":{"value":false},"auc":{"value":false},"pmf":{"value":false},"pf":{"value":false},"tow":{"value":false},"mf":{"value":false},"con":{"value":false},"land":{"value":false},"apa":{"value":false},"manu":{"value":false},"apco":{"value":false}},"isMapVisible":true,"isListVisible":true,"mapBounds":{"west":-81.785,"east":-81.675,"south":41.37,"north":41.42}}

- **44134 (Parma South):**  
  https://www.zillow.com/parma-oh-44134/houses/?searchQueryState={"filterState":{"price":{"max":190000},"sort":{"value":"globalrelevanceex"},"fsba":{"value":false},"fsbo":{"value":false},"nc":{"value":false},"fore":{"value":false},"cmsn":{"value":false},"auc":{"value":false},"pmf":{"value":false},"pf":{"value":false},"tow":{"value":false},"mf":{"value":false},"con":{"value":false},"land":{"value":false},"apa":{"value":false},"manu":{"value":false},"apco":{"value":false}},"isMapVisible":true,"isListVisible":true,"mapBounds":{"west":-81.725,"east":-81.645,"south":41.35,"north":41.40}}

- **44130 (Middleburg Heights / Parma SW):**  
  https://www.zillow.com/middleburg-heights-oh-44130/houses/?searchQueryState={"filterState":{"price":{"max":190000},"sort":{"value":"globalrelevanceex"},"fsba":{"value":false},"fsbo":{"value":false},"nc":{"value":false},"fore":{"value":false},"cmsn":{"value":false},"auc":{"value":false},"pmf":{"value":false},"pf":{"value":false},"tow":{"value":false},"mf":{"value":false},"con":{"value":false},"land":{"value":false},"apa":{"value":false},"manu":{"value":false},"apco":{"value":false}},"isMapVisible":true,"isListVisible":true,"mapBounds":{"west":-81.805,"east":-81.725,"south":41.35,"north":41.41}}

---

## Files Saved

| File | Content |
|------|---------|
| `/opt/data/parma-pull-status.txt` | Full attempt log with timestamps |
| `/opt/data/parma-latest-listings.md` | Not created (no data) |

---

## Next Steps

1. **Top up Zillapi credits** at https://zillapi.com/app/billing — the current cycle is exhausted.
2. **Fix firecrawl:** Install `firecrawl-py==4.17.0` in `/opt/hermes/.venv` with write permissions (the venv is read-only for the agent user).
3. **Re-run** when either dependency is restored. The cron job or manual re-invocation will pick up where this left off.
4. **Manual workaround:** Use the direct Zillow URLs above in your own browser — they're pre-filtered to houses under $190K in each ZIP.