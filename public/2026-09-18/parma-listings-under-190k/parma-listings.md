# Parma Listings Under $190K — Pull Failed

**Timestamp:** 2026-09-18 (cron run)  
**Status:** ❌ Zillapi out of credits — no listings pulled

---

## Blocker Diagnostics

| Source | Method | Result |
|---|---|---|
| **Zillapi MCP** | `mcp_zillapi_search_listings` (44129) | ❌ Out of credits for this cycle |
| **Zillapi MCP** | `mcp_zillapi_search_listings` (44134) | ❌ MCP server unreachable (109 failures) |
| **Zillapi MCP** | `mcp_zillapi_search_listings` (44130) | ❌ MCP server unreachable (109 failures) |
| **Zillow.com / Redfin / Realtor.com / Trulia** | web_search / web_extract / browser | ⛔ Not attempted — known captcha block (PerimeterX/Cloudflare) per skill protocol |

---

## Direct Zillow Search URLs (open in your browser)

**44129 — Parma West, under $190K:**
https://www.zillow.com/parma-west-cleveland-oh-44129/houses/?searchQueryState={"pagination":{},"usersSearchTerm":"44129","mapBounds":{"west":-81.78,"east":-81.68,"south":41.37,"north":41.42},"filterState":{"price":{"max":190000},"mp":{"min":1},"sort":{"value":"globalrelevanceex"},"ah":{"value":true}},"isListVisible":true}

**44134 — Parma, under $190K:**
https://www.zillow.com/parma-oh-44134/houses/?searchQueryState={"pagination":{},"usersSearchTerm":"44134","mapBounds":{"west":-81.72,"east":-81.65,"south":41.35,"north":41.40},"filterState":{"price":{"max":190000},"mp":{"min":1},"sort":{"value":"globalrelevanceex"},"ah":{"value":true}},"isListVisible":true}

**44130 — Parma / Middleburg Heights, under $190K:**
https://www.zillow.com/middleburg-heights-oh-44130/houses/?searchQueryState={"pagination":{},"usersSearchTerm":"44130","mapBounds":{"west":-81.80,"east":-81.73,"south":41.35,"north":41.41},"filterState":{"price":{"max":190000},"mp":{"min":1},"sort":{"value":"globalrelevanceex"},"ah":{"value":true}},"isListVisible":true}

---

## Resume Plan

When Zillapi credits refresh:
1. Re-run `mcp_zillapi_search_listings` for all three ZIPs at $190K cap
2. Enrich with `mcp_zillapi_get_zestimate` per property
3. Generate the full ranked table + verdicts
4. Save to `/opt/data/outputs/YYYY-MM-DD/parma-listings-under-190k/parma-listings.md`