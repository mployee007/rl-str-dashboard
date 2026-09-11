# Parma West Submarket Screen — Active Listings Under $190K

**Pull date:** 2026-09-11 00:51 UTC  
**Status:** ❌ BLOCKED — Zillapi credits exhausted

## Source Status

| Source | Result |
|---|---|
| Zillapi MCP (44129) | ❌ Out of credits — "Top up or upgrade at https://zillapi.com/app/billing." |
| Zillapi MCP (44134) | ❌ MCP server unreachable (51 consecutive failures) |
| Zillapi MCP (44130) | ❌ MCP server unreachable (51 consecutive failures) |
| Zillow.com (web) | Not attempted — blocked by PerimeterX/Cloudflare captchas (per skill guidance) |
| Redfin.com | Not attempted — blocked by captchas (per skill guidance) |
| Realtor.com | Not attempted — blocked by captchas (per skill guidance) |

## Target ZIPs & Bounding Boxes

| ZIP | Area | Bounding Box (W,S,E,N) |
|---|---|---|
| 44129 | Parma West / Seven Hills | -81.78, 41.37, -81.68, 41.42 |
| 44134 | Parma Central / South | -81.72, 41.35, -81.65, 41.40 |
| 44130 | Parma Heights / Middleburg Hts | -81.80, 41.35, -81.73, 41.41 |

**Price cap:** $190,000

## Direct Zillow Search URLs

Open these in your own browser to view active listings:

- **[44129 — Parma West / Seven Hills](https://www.zillow.com/homes/for_sale/44129_house,apartment_condo,townhouse_type/0-190000_price/0-408_mp/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-81.78%2C%22south%22%3A41.37%2C%22east%22%3A-81.68%2C%22north%22%3A41.42%7D%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A190000%7D%2C%22homeType%22%3A%7B%22value%22%3A%5B%22houses%22%2C%22apartments%22%2C%22townhomes%22%5D%7D%7D%7D)**
- **[44134 — Parma Central / South](https://www.zillow.com/homes/for_sale/44134_house,apartment_condo,townhouse_type/0-190000_price/0-457_mp/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-81.72%2C%22south%22%3A41.35%2C%22east%22%3A-81.65%2C%22north%22%3A41.40%7D%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A190000%7D%2C%22homeType%22%3A%7B%22value%22%3A%5B%22houses%22%2C%22apartments%22%2C%22townhomes%22%5D%7D%7D%7D)**
- **[44130 — Parma Heights / Middleburg Hts](https://www.zillow.com/homes/for_sale/44130_house,apartment_condo,townhouse_type/0-190000_price/0-454_mp/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-81.80%2C%22south%22%3A41.35%2C%22east%22%3A-81.73%2C%22north%22%3A41.41%7D%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A190000%7D%2C%22homeType%22%3A%7B%22value%22%3A%5B%22houses%22%2C%22apartments%22%2C%22townhomes%22%5D%7D%7D%7D)**

## Remediation

1. **Top up Zillapi credits** at https://zillapi.com/app/billing
2. **Retry this cron job** — it will resume once credits are available
3. **Manual fallback:** use the direct Zillow links above and manually populate the listing table

## Status Files

- Status tracker: `/opt/data/parma-pull-status.txt`
- Quick-reference: `/opt/data/parma-latest-listings.md` (empty — no data pulled)
- This report: `/opt/data/outputs/2026-09-11/parma-listings-under-190k/parma-listings.md`