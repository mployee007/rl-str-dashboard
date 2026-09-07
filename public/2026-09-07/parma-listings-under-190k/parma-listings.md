# Parma Listings Under $190K — Pull Failed

**Date:** 2026-09-07  
**Target ZIPs:** 44129, 44134, 44130  
**Status:** ❌ Blocked — Zillapi out of credits

---

## Blocker Summary

All three Zillapi calls failed. The MCP server returned "Out of credits for this cycle" on the first call (44129) and became unreachable after 25 consecutive failures for the remaining two (44134, 44130).

No listings were fabricated.

---

## Attempt Log

| ZIP | Bounding Box | Method | Result |
|-----|-------------|--------|--------|
| 44129 | -81.78,41.37,-81.68,41.42 | mcp_zillapi_search_listings | ❌ Out of credits |
| 44134 | -81.72,41.35,-81.65,41.40 | mcp_zillapi_search_listings | ❌ MCP unreachable |
| 44130 | -81.80,41.35,-81.73,41.41 | mcp_zillapi_search_listings | ❌ MCP unreachable |

---

## Direct Zillow Search URLs (open in your browser)

- **[44129 under $190K](https://www.zillow.com/parma-oh-44129/houses/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-81.78%2C%22east%22%3A-81.68%2C%22south%22%3A41.37%2C%22north%22%3A41.42%7D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A190000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22homeType%22%3A%7B%22value%22%3A%5B%22houses%22%5D%7D%7D%2C%22isListVisible%22%3Atrue%7D)**
- **[44134 under $190K](https://www.zillow.com/parma-oh-44134/houses/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-81.72%2C%22east%22%3A-81.65%2C%22south%22%3A41.35%2C%22north%22%3A41.40%7D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A190000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22homeType%22%3A%7B%22value%22%3A%5B%22houses%22%5D%7D%7D%2C%22isListVisible%22%3Atrue%7D)**
- **[44130 under $190K](https://www.zillow.com/parma-oh-44130/houses/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-81.80%2C%22east%22%3A-81.73%2C%22south%22%3A41.35%2C%22north%22%3A41.41%7D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A190000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22homeType%22%3A%7B%22value%22%3A%5B%22houses%22%5D%7D%7D%2C%22isListVisible%22%3Atrue%7D)**

---

## Next Steps

1. Top up credits at https://zillapi.com/app/billing
2. Re-run this pull once credits refresh
3. Previous session data (if any) may be available in saved JSON files — check `/opt/data/outputs/` for prior Parma runs

---

## Saved Artifacts

| File | Path |
|------|------|
| Status log | `/opt/data/parma-pull-status.txt` |
| This report | `/opt/data/outputs/2026-09-07/parma-listings-under-190k/parma-listings.md` |