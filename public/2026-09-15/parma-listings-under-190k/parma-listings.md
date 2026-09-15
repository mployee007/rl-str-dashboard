# Parma-Area Listings Pull — FAILED (Zillapi Credit Exhaustion)

**Timestamp:** 2026-09-15T00:00:00Z (approx)
**Task:** Pull active for-sale house listings ≤ $190K in ZIP codes 44129, 44134, 44130
**Status:** ❌ FAILED — Zillapi out of credits

---

## Source Attempts

| Source | ZIP(s) | Result |
|--------|--------|--------|
| Zillapi `search_listings` | 44129 | **"Out of credits for this cycle."** — Top up at https://zillapi.com/app/billing |
| Zillapi `search_listings` | 44134 | **MCP server unreachable** (82 consecutive failures) |
| Zillapi `search_listings` | 44130 | **MCP server unreachable** (82 consecutive failures) |

All three bounding-box calls consumed **zero credits** — no listings were retrieved.

---

## Direct Search URLs (open in your browser)

These Zillow URLs are pre-filtered to the requested ZIP + price cap:

- **ZIP 44129 (Parma West):** https://www.zillow.com/homes/for_sale/44129_rb/?searchQueryState={"pagination":{},"usersSearchTerm":"44129","mapBounds":{"west":-81.78,"east":-81.68,"south":41.37,"north":41.42},"filterState":{"price":{"max":190000},"sort":{"value":"globalrelevanceex"}}}
- **ZIP 44134 (Parma East / Seven Hills):** https://www.zillow.com/homes/for_sale/44134_rb/?searchQueryState={"pagination":{},"usersSearchTerm":"44134","mapBounds":{"west":-81.72,"east":-81.65,"south":41.35,"north":41.40},"filterState":{"price":{"max":190000},"sort":{"value":"globalrelevanceex"}}}
- **ZIP 44130 (Middleburg Heights / Parma Heights):** https://www.zillow.com/homes/for_sale/44130_rb/?searchQueryState={"pagination":{},"usersSearchTerm":"44130","mapBounds":{"west":-81.80,"east":-81.73,"south":41.35,"north":41.41},"filterState":{"price":{"max":190000},"sort":{"value":"globalrelevanceex"}}}

---

## Next Steps

1. **Wait for Zillapi credit refresh** (cycle resets automatically) and retry the pull.
2. **Use the direct Zillow URLs above** to manually review current listings in the meantime.
3. **Re-run this cron job** once credits are restored — the script will pick up where it left off.

---

*Status file saved to `/opt/data/parma-pull-status.txt`*
*This report saved to `/opt/data/outputs/2026-09-15/parma-listings-under-190k/parma-listings.md`*