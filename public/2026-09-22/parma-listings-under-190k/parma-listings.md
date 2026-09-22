# Parma Area Listings Under $190K — Pull Report

**Date:** 2026-09-22  
**Status:** ❌ FAILED — Zillapi credits depleted + MCP server unreachable

## Target ZIP Codes

| ZIP | Area | Bounding Box | Status |
|-----|------|-------------|--------|
| 44129 | Parma West | -81.78,41.37,-81.68,41.42 | Out of credits |
| 44134 | Parma SE | -81.72,41.35,-81.65,41.40 | MCP server unreachable |
| 44130 | Parma SW | -81.80,41.35,-81.73,41.41 | MCP server unreachable |

## Errors Encountered

1. **44129:** `Out of credits for this cycle. Top up or upgrade at https://zillapi.com/app/billing.`
2. **44134:** `MCP server 'zillapi' is unreachable after 16 consecutive failures.`
3. **44130:** `MCP server 'zillapi' is unreachable after 16 consecutive failures.`

## Sources Attempted

| Source | Result |
|--------|--------|
| Zillapi MCP (search_listings) — 44129 | ❌ Out of credits |
| Zillapi MCP (search_listings) — 44134 | ❌ Server unreachable |
| Zillapi MCP (search_listings) — 44130 | ❌ Server unreachable |
| Web alternatives (Zillow.com, Redfin, etc.) | ⛔ Skipped per skill directive — all block with captchas |

## Direct Zillow Search URLs

Open these in a browser to view listings manually:

- **44129:** https://www.zillow.com/homes/for_sale/44129_rb/0-190000_price/0-500_mp/
- **44134:** https://www.zillow.com/homes/for_sale/44134_rb/0-190000_price/0-500_mp/
- **44130:** https://www.zillow.com/homes/for_sale/44130_rb/0-190000_price/0-500_mp/

## Next Steps

- Resume pull when Zillapi credits refresh or MCP server recovers
- Status file maintained at `/opt/data/parma-pull-status.txt`
- No fabricated listings — this report is a blocker notice only