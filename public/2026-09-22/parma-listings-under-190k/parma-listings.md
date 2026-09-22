# Parma Area Listings Pull — Status: FAILED (Out of Credits)

**Run timestamp:** 2026-09-22 18:51:23 UTC
**Target ZIPs:** 44129, 44134, 44130
**Price cap:** $190,000
**Status:** FOR_SALE

---

## Zillapi Error Summary

| ZIP | Bounding Box | Attempt | Error |
|-----|-------------|---------|-------|
| 44129 | `-81.78,41.37,-81.68,41.42` | 1 | **Out of credits** — top up at https://zillapi.com/app/billing |
| 44134 | `-81.72,41.35,-81.65,41.40` | 1 | MCP server unreachable (5 consecutive failures) |
| 44130 | `-81.80,41.35,-81.73,41.41` | 1 | MCP server unreachable (5 consecutive failures) |

## Sources Attempted

| Source | Result |
|--------|--------|
| Zillapi MCP (`mcp_zillapi_search_listings`) | ❌ Out of credits / server unreachable |
| Zillow.com | ⛔ Known captcha/PerimeterX block (not attempted per skill instructions) |
| Redfin.com | ⛔ Known captcha/Cloudflare block (not attempted) |
| Realtor.com | ⛔ Known bot protection (not attempted) |

## Direct Zillow Search URLs

The user can open these in their own browser to view listings:

- **ZIP 44129 (Parma West, OH)** under $190K:
  https://www.zillow.com/parma-oh-44129/houses/0-190000_att/

- **ZIP 44134 (Parma East, OH)** under $190K:
  https://www.zillow.com/parma-oh-44134/houses/0-190000_att/

- **ZIP 44130 (Middleburg Heights / Parma Heights)** under $190K:
  https://www.zillow.com/middleburg-heights-oh-44130/houses/0-190000_att/

## Next Steps

1. Top up Zillapi credits at https://zillapi.com/app/billing
2. Re-run this cron job or trigger manually once credits are available
3. No data was fabricated — report is accurate as of pull time