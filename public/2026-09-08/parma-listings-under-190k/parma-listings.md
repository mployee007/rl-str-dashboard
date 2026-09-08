# Parma West Listings Under $190K — Pull Failed (2026-09-08)

**Status:** ❌ ZILLAPI UNAVAILABLE — No live data retrieved.

## Blocker Summary

| Attempt | Tool | Target ZIP | Result |
|---------|------|-----------|--------|
| 1 | `mcp_zillapi_search_listings` | 44129 | **Out of credits** — needs top-up at https://zillapi.com/app/billing |
| 2 | `mcp_zillapi_search_listings` | 44134 | MCP server unreachable (33 failures) |
| 3 | `mcp_zillapi_search_listings` | 44130 | MCP server unreachable (33 failures) |

## What Went Wrong

1. **Primary cause:** The Zillapi account is out of credits for this billing cycle.
2. **Secondary cause:** The MCP server connection appears to have dropped (calls 2 and 3), which may be related to the credit exhaustion or an independent infrastructure issue.

## Manual Fallback URLs

Open these in your browser to view current listings manually:

- **ZIP 44129 (Parma West):** https://www.zillow.com/homes/for_sale/44129_zip/0-190000_price/0-488_mp/
- **ZIP 44134 (Parma South/Southeast):** https://www.zillow.com/homes/for_sale/44134_zip/0-190000_price/0-488_mp/
- **ZIP 44130 (Middleburg Heights area):** https://www.zillow.com/homes/for_sale/44130_zip/0-190000_price/0-488_mp/

## Next Steps

1. **Top up Zillapi credits** at https://zillapi.com/app/billing
2. **Wait for MCP server recovery** (auto-retry window ~60 seconds, but credits must be restored first)
3. **Re-run** this cron job or trigger manually once credits are live
4. The output files are pre-staged at:
   - `/opt/data/outputs/2026-09-08/parma-listings-under-190k/parma-listings.md`
   - `/opt/data/parma-latest-listings.md`
   - `/opt/data/parma-pull-status.txt`

No data was fabricated. Every listing field below is empty because no API calls succeeded.