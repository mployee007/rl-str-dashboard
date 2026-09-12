# Parma Listings Under $190K — FAILED PULL

**Date:** 2026-09-12
**Target ZIPs:** 44129, 44134, 44130
**Price Cap:** $190,000
**Status:** ❌ Zillapi unavailable — no listings retrieved

---

## Source Attempts

| Source | ZIP(s) | Result |
|--------|--------|--------|
| Zillapi `mcp_zillapi_search_listings` | 44129 | **Out of credits** — top up at https://zillapi.com/app/billing |
| Zillapi `mcp_zillapi_search_listings` | 44134 | **MCP server unreachable** — 61 consecutive failures |
| Zillapi `mcp_zillapi_search_listings` | 44130 | **MCP server unreachable** — 61 consecutive failures |

---

## Direct Zillow Search URLs (Open in Browser)

- **44129 (Parma West):** https://www.zillow.com/parma-oh-44129/houses/?searchQueryState={"pagination":{},"usersSearchTerm":"44129","mapBounds":{"west":-81.78,"south":41.37,"east":-81.68,"north":41.42},"filterState":{"sort":{"value":"globalrelevanceex"},"price":{"max":190000},"fsba":{"value":false},"fsbo":{"value":false},"nc":{"value":false},"fore":{"value":false},"cmsn":{"value":false},"auc":{"value":false},"pmf":{"value":false},"pf":{"value":false},"ah":{"value":true}},"isListVisible":true}
- **44134:** https://www.zillow.com/parma-oh-44134/houses/?searchQueryState={"pagination":{},"usersSearchTerm":"44134","mapBounds":{"west":-81.72,"south":41.35,"east":-81.65,"north":41.4},"filterState":{"sort":{"value":"globalrelevanceex"},"price":{"max":190000},"ah":{"value":true}},"isListVisible":true}
- **44130:** https://www.zillow.com/middleburg-heights-oh-44130/houses/?searchQueryState={"pagination":{},"usersSearchTerm":"44130","mapBounds":{"west":-81.8,"south":41.35,"east":-81.73,"north":41.41},"filterState":{"sort":{"value":"globalrelevanceex"},"price":{"max":190000},"ah":{"value":true}},"isListVisible":true}

---

## Next Steps

1. **Top up Zillapi credits** at https://zillapi.com/app/billing
2. **Check MCP server health** — if credits are available but the server is unreachable, the Zillapi MCP backend needs attention
3. **Re-run** this cron job or trigger a manual pull once credits/server are restored

*Report automatically saved to `/opt/data/parma-pull-status.txt`*