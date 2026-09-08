# Parma Listings Under $190K — 2026-09-08

**Status:** ❌ **BLOCKED — Zillapi out of credits**

## What was attempted

Three bounding-box queries via `mcp_zillapi_search_listings` targeting:

| ZIP | Bounding Box | Price Cap | Result |
|-----|-------------|-----------|--------|
| 44129 | -81.78,41.37,-81.68,41.42 | $190,000 | Out of credits |
| 44134 | -81.72,41.35,-81.65,41.40 | $190,000 | MCP server unreachable |
| 44130 | -81.80,41.35,-81.73,41.41 | $190,000 | MCP server unreachable |

## Blocked sources per skill protocol

Per the `real-estate-submarket-screening` skill, Zillapi is the only reliable path. All web-based real estate sites (Zillow.com, Redfin, Trulia, Realtor.com, Homes.com, Movoto) block with captchas. No alternate sources were attempted per the skill's explicit instruction to not waste turns on blocked sites.

## Manual fallback

Open these direct Zillow searches in a browser:

- **[44129 under $190K](https://www.zillow.com/homes/for_sale/44129_rb/pricea_sort/41.42,-81.68,41.37,-81.78_rect/11_zm/0-190000_price/)**
- **[44134 under $190K](https://www.zillow.com/homes/for_sale/44134_rb/pricea_sort/41.40,-81.65,41.35,-81.72_rect/11_zm/0-190000_price/)**
- **[44130 under $190K](https://www.zillow.com/homes/for_sale/44130_rb/pricea_sort/41.41,-81.73,41.35,-81.80_rect/11_zm/0-190000_price/)**

## Resume

Top up Zillapi credits at https://zillapi.com/app/billing and this job will pick up on the next cron cycle. No listings were fabricated.