# Parma West Listings Under $190K — Pull Failed

**Date:** 2026-09-12
**Target ZIPs:** 44129 (Parma West), 44134 (Parma), 44130 (Parma/Middleburg Heights)
**Price Cap:** $190,000

## Status: ❌ FAILED — Zillapi Unavailable

| Source | ZIP | Result |
|--------|-----|--------|
| Zillapi MCP | 44129 | **Out of credits** — "Top up or upgrade at https://zillapi.com/app/billing" |
| Zillapi MCP | 44134 | **Server unreachable** — 58 consecutive failures, MCP server down |
| Zillapi MCP | 44130 | **Server unreachable** — 58 consecutive failures, MCP server down |
| web_search | all | **Blocked** — firecrawl-py not installed, lazy installs disabled |
| web_extract | all | Not attempted (Zillow captchas expected per skill docs) |
| browser | all | Not attempted (Zillow captchas expected per skill docs) |
| cached data | all | No prior pull files found on disk |

## No Listings to Display

Zero properties were retrieved. The Zillapi MCP server is down and credits are exhausted. No data was fabricated.

## Manual Self-Service Links

Until Zillapi recovers, open these in your browser:

- **44129:** https://www.zillow.com/homes/for_sale/44129_rb/under-190000/
- **44134:** https://www.zillow.com/homes/for_sale/44134_rb/under-190000/
- **44130:** https://www.zillow.com/homes/for_sale/44130_rb/under-190000/

## Resumption Plan

When Zillapi is back (server reachable + credits available):

1. Re-run the three bounding-box queries as defined in the cron job
2. Pull full property details via `mcp_zillapi_lookup_property_by_zpid` for each listing
3. Compute price-to-rent ratios using rent Zestimates
4. Assign take/negotiate/pass verdicts
5. Save to `/opt/data/outputs/YYYY-MM-DD/parma-listings-under-190k/parma-listings.md`
6. Update quick-reference at `/opt/data/parma-latest-listings.md`

**Status file:** `/opt/data/parma-pull-status.txt`