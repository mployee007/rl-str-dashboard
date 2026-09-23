# Parma West Submarket — Active Listings Under $190K

**Status: FAILED — no data pulled (Zillapi out of credits).**

**Date:** 2026-09-23
**ZIPs requested:** 44129 (Parma West), 44134, 44130
**Filter:** for_sale, price ≤ $190,000

## Blocker

`mcp_zillapi_search_listings` returned:

> "Error: Out of credits for this cycle. Top up or upgrade at https://zillapi.com/app/billing."

The account's Zillapi credit pool is exhausted for the current billing cycle. Two of the three bounding-box calls also surfaced "MCP server 'zillapi' is unreachable after 5 consecutive failures" as a follow-on effect.

## What was NOT done

- ❌ No listings were pulled.
- ❌ No data was fabricated or estimated.
- ❌ No alternate listing sites were attempted (Zillow/Redfin/Trulia all block with captchas per the screening skill).

## Next steps

1. Re-run this task after credits refresh (top up at zillapi.com/app/billing, or wait for the next credit cycle).
2. The three bounding boxes are ready to reuse:
   - 44129: `-81.78,41.37,-81.68,41.42`
   - 44134: `-81.72,41.35,-81.65,41.40`
   - 44130: `-81.80,41.35,-81.73,41.41`

## Manual fallback (for the user)

Open these directly in a browser while credits are down:

- Zillow 44129 under $190K: https://www.zillow.com/homes/44129_rb/?price_max=190000
- Zillow 44134 under $190K: https://www.zillow.com/homes/44134_rb/?price_max=190000
- Zillow 44130 under $190K: https://www.zillow.com/homes/44130_rb/?price_max=190000

Full status log: `/opt/data/parma-pull-status.txt`