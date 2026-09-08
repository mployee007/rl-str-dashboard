# Parma West / 44129 + 44134 + 44130 — For-Sale Listings ≤ $190K

**Run date:** 2026-09-08 06:11 UTC
**Status:** ❌ PULL FAILED — no data returned

## Result

Zillapi MCP returned an out-of-credits error for this cycle:

> `Error: Out of credits for this cycle. Top up or upgrade at https://zillapi.com/app/billing.`

Two of the three parallel calls also surfaced an MCP transport error:

> `MCP server 'zillapi' is unreachable after 32 consecutive failures.`

## Targets attempted

| ZIP | Bounding box | Status filter | Price cap |
|-----|--------------|---------------|-----------|
| 44129 | -81.78, 41.37, -81.68, 41.42 | for_sale | $190,000 |
| 44134 | -81.72, 41.35, -81.65, 41.40 | for_sale | $190,000 |
| 44130 | -81.80, 41.35, -81.73, 41.41 | for_sale | $190,000 |

## Data source status

| Source | Result |
|--------|--------|
| Zillapi `search_listings` (44129) | ❌ Out of credits |
| Zillapi `search_listings` (44134) | ❌ MCP server unreachable |
| Zillapi `search_listings` (44130) | ❌ MCP server unreachable |

**No listings were fabricated.** This report intentionally contains zero property rows.

## Next actions

1. Top up Zillapi credits at https://zillapi.com/app/billing (or wait for cycle reset).
2. Re-run this pull — the three bounding boxes above are ready to go.
3. Direct Zillow search links the user can open manually in the meantime:
   - 44129: https://www.zillow.com/homes/for_sale/44129_rb/
   - 44134: https://www.zillow.com/homes/for_sale/44134_rb/
   - 44130: https://www.zillow.com/homes/for_sale/44130_rb/
