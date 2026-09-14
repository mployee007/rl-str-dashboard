# Parma West Listings — Under $190K Pull Report

**Pull date:** 2026-09-14  
**Status:** ❌ BLOCKED — Zillapi credits exhausted  
**ZIP codes requested:** 44129, 44134, 44130  
**Price ceiling:** $190,000  

---

## Blocker Details

All three Zillapi bounding-box queries failed:

| ZIP | Bounding Box | Result |
|-----|-------------|--------|
| 44129 (Parma West) | `-81.78,41.37,-81.68,41.42` | `Out of credits for this cycle` |
| 44134 (Parma South) | `-81.72,41.35,-81.65,41.40` | `MCP server unreachable (10 failures)` |
| 44130 (Middleburg Hts / SW Parma) | `-81.80,41.35,-81.73,41.41` | `MCP server unreachable (10 failures)` |

The 44129 call consumed a credit attempt and returned the "out of credits" message. The subsequent 44134 and 44130 calls failed with server-unreachable errors before any credit was deducted.

---

## No Fabricated Data

No listings are presented below because none could be retrieved. Per the `real-estate-submarket-screening` skill protocol:
- I did **not** attempt Zillow.com, Redfin, Trulia, or other listing sites (all block with captchas).
- I did **not** fabricate or synthesize listing data.

---

## Direct Zillow Search Links (Open in Browser)

| ZIP | Zillow Search URL |
|-----|-------------------|
| 44129 | https://www.zillow.com/homes/44129_rb/?searchQueryState={"pagination":{},"usersSearchTerm":"44129","mapBounds":{"west":-81.78,"east":-81.68,"south":41.37,"north":41.42},"filterState":{"price":{"max":190000},"sort":{"value":"globalrelevanceex"},"isForSaleByAgent":{"value":false},"isForSaleByOwner":{"value":false},"isForSaleForeclosure":{"value":false},"isAuctions":{"value":false},"isNewConstruction":{"value":false}}} |
| 44134 | https://www.zillow.com/homes/44134_rb/?searchQueryState={"pagination":{},"usersSearchTerm":"44134","mapBounds":{"west":-81.72,"east":-81.65,"south":41.35,"north":41.40},"filterState":{"price":{"max":190000},"sort":{"value":"globalrelevanceex"}}} |
| 44130 | https://www.zillow.com/homes/44130_rb/?searchQueryState={"pagination":{},"usersSearchTerm":"44130","mapBounds":{"west":-81.80,"east":-81.73,"south":41.35,"north":41.41},"filterState":{"price":{"max":190000},"sort":{"value":"globalrelevanceex"}}} |

---

## Next Steps

1. **Top up Zillapi credits** at https://zillapi.com/app/billing
2. **Re-run the cron job** — it will pick up the saved status and resume from scratch
3. Once credits refresh, the pull should complete in 3 API calls (~3-6 credits)

---

*Status file: `/opt/data/parma-pull-status.txt`*  
*Report saved: `/opt/data/outputs/2026-09-14/parma-listings-under-190k/parma-listings.md`*