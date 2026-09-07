# Parma Area Listings Under $190K — Pull Report

**Date:** 2026-09-07  
**ZIPs targeted:** 44129 (Parma West), 44134 (Parma South), 44130 (Parma Heights area)  
**Price cap:** $190,000  
**Status:** ❌ FAILED — Zillapi credits exhausted

---

## Sources Tried

| Source | Method | Result |
|--------|--------|--------|
| Zillapi MCP (44129) | `mcp_zillapi_search_listings` | ❌ Out of credits |
| Zillapi MCP (44134) | `mcp_zillapi_search_listings` | ❌ MCP server unreachable (23 consecutive failures) |
| Zillapi MCP (44130) | `mcp_zillapi_search_listings` | ❌ MCP server unreachable (23 consecutive failures) |
| Firecrawl web search | `web_search` | ❌ lazy installs disabled |

---

## Direct Zillow Search URLs (open in browser)

- **[44129 — Parma West, under $190K](https://www.zillow.com/parma-oh-44129/homes/?searchQueryState={"pagination":{},"mapBounds":{"west":-81.78,"east":-81.68,"south":41.37,"north":41.42},"filterState":{"price":{"max":190000},"sortSelection":{"value":"globalrelevanceex"}},"isListVisible":true})**
- **[44134 — Parma South, under $190K](https://www.zillow.com/parma-oh-44134/homes/?searchQueryState={"pagination":{},"mapBounds":{"west":-81.72,"east":-81.65,"south":41.35,"north":41.40},"filterState":{"price":{"max":190000},"sortSelection":{"value":"globalrelevanceex"}},"isListVisible":true})**
- **[44130 — Parma Heights, under $190K](https://www.zillow.com/parma-heights-oh-44130/homes/?searchQueryState={"pagination":{},"mapBounds":{"west":-81.80,"east":-81.73,"south":41.35,"north":41.41},"filterState":{"price":{"max":190000},"sortSelection":{"value":"globalrelevanceex"}},"isListVisible":true})**

---

## Next Steps

1. Top up Zillapi credits at https://zillapi.com/app/billing
2. Re-run this cron job after credits refresh
3. Status file written to `/opt/data/parma-pull-status.txt` for monitoring

**No listings were fabricated. This report reflects actual tool results only.**