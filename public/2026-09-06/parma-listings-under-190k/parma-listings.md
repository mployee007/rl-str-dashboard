# Parma Listings Under $190K — Pull Report

**Date:** 2026-09-06  
**Status:** ❌ BLOCKED — Zillapi credits exhausted

---

## Target ZIP Codes

| ZIP | Area | Bounding Box | Price Cap |
|-----|------|--------------|-----------|
| 44129 | Parma West, OH | `-81.78,41.37,-81.68,41.42` | $190,000 |
| 44134 | Parma, OH | `-81.72,41.35,-81.65,41.40` | $190,000 |
| 44130 | Parma / Middleburg Heights, OH | `-81.80,41.35,-81.73,41.41` | $190,000 |

---

## Source Results

| Source | Result |
|--------|--------|
| **Zillapi MCP** (`mcp_zillapi_search_listings`, 3 calls) | ❌ "Out of credits for this cycle. Top up or upgrade at https://zillapi.com/app/billing." |
| Zillow.com | ⛔ Skipped — known PerimeterX/Cloudflare captcha block (per skill instructions) |
| Redfin | ⛔ Skipped — known captcha block |
| Realtor.com | ⛔ Skipped — known captcha block |
| Trulia | ⛔ Skipped — known captcha block |
| web_search | ⛔ Not attempted — skill instructs not to waste turns on blocked sources |

---

## Direct Zillow Search URLs

Open these in your browser to view listings directly:

- **44129:** https://www.zillow.com/homes/for_sale/44129_rb/?searchQueryState={"pagination":{},"usersSearchTerm":"44129","mapBounds":{"west":-81.78,"east":-81.68,"south":41.37,"north":41.42},"filterState":{"max":{"value":190000},"sort":{"value":"globalrelevanceex"}},"isListVisible":true}
- **44134:** https://www.zillow.com/homes/for_sale/44134_rb/?searchQueryState={"pagination":{},"usersSearchTerm":"44134","mapBounds":{"west":-81.72,"east":-81.65,"south":41.35,"north":41.40},"filterState":{"max":{"value":190000},"sort":{"value":"globalrelevanceex"}},"isListVisible":true}
- **44130:** https://www.zillow.com/homes/for_sale/44130_rb/?searchQueryState={"pagination":{},"usersSearchTerm":"44130","mapBounds":{"west":-81.80,"east":-81.73,"south":41.35,"north":41.41},"filterState":{"max":{"value":190000},"sort":{"value":"globalrelevanceex"}},"isListVisible":true}

---

## Next Steps

1. **Top up Zillapi credits** at https://zillapi.com/app/billing  
2. Re-run this cron job or manually trigger the pull  
3. The `parma-pull-status.txt` file at `/opt/data/parma-pull-status.txt` will be overwritten with fresh data on next successful run

**No fabricated listings. No data was invented.**