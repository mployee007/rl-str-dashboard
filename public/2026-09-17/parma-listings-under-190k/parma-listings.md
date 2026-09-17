# Parma Submarket Listing Screen — September 17, 2026

## Bottom Line
**Zillapi credits exhausted; MCP server partially unreachable.** No live listing data was retrieved for ZIPs 44129, 44134, or 44130 at the $190K cap. This report documents the attempt and provides manual fallback URLs so the screen can be completed when credits refresh or via browser.

---

## Status

| ZIP | Bounding Box | Attempt #1 | Status |
|---|---|---|---|
| 44129 (Parma West) | -81.78, 41.37, -81.68, 41.42 | `mcp_zillapi_search_listings` | ❌ Out of credits |
| 44134 (Parma East) | -81.72, 41.35, -81.65, 41.40 | `mcp_zillapi_search_listings` | ❌ MCP unreachable |
| 44130 (Middleburg Hts) | -81.80, 41.35, -81.73, 41.41 | `mcp_zillapi_search_listings` | ❌ MCP unreachable |

---

## Direct Zillow Search URLs

Open these in your browser to view current listings:

| ZIP | URL |
|---|---|
| **44129** | [Zillow: Parma West under $190K](https://www.zillow.com/parma-oh-44129/houses/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%2244129%22%2C%22filterState%22%3A%7B%22maxPrice%22%3A%7B%22value%22%3A190000%7D%2C%22sort%22%3A%7B%22value%22%3A%22priced%22%7D%7D%2C%22isListVisible%22%3Atrue%7D) |
| **44134** | [Zillow: Parma East under $190K](https://www.zillow.com/parma-oh-44134/houses/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%2244134%22%2C%22filterState%22%3A%7B%22maxPrice%22%3A%7B%22value%22%3A190000%7D%2C%22sort%22%3A%7B%22value%22%3A%22priced%22%7D%7D%2C%22isListVisible%22%3Atrue%7D) |
| **44130** | [Zillow: Middleburg Hts under $190K](https://www.zillow.com/middleburg-heights-oh-44130/houses/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%2244130%22%2C%22filterState%22%3A%7B%22maxPrice%22%3A%7B%22value%22%3A190000%7D%2C%22sort%22%3A%7B%22value%22%3A%22priced%22%7D%7D%2C%22isListVisible%22%3Atrue%7D) |

---

## Next Steps

1. **Top up Zillapi credits** at https://zillapi.com/app/billing
2. **Re-run this cron job** — it will pick up where it left off
3. Or **manually screen** the above Zillow URLs and feed the results back into the pipeline

---

*Status file also saved to /opt/data/parma-pull-status.txt*  
*Report saved to /opt/data/outputs/2026-09-17/parma-listings-under-190k/parma-listings.md*