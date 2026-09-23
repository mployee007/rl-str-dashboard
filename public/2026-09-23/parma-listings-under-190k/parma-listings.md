# Parma Listings Under $190K — BLOCKED (Zillapi credits exhausted)

**Pull date:** 2026-09-23 | **Status:** ❌ No data

## Error
Zillapi returned: `Out of credits for this cycle. Top up or upgrade at https://zillapi.com/app/billing.`

## Attempt log
| ZIP | Bounding Box | Result |
|---|---|---|
| 44129 (Parma West) | -81.78,41.37,-81.68,41.42 | Out of credits |
| 44134 (Parma) | -81.72,41.35,-81.65,41.40 | Server unreachable (post-credit-exhaustion) |
| 44130 (Parma East) | -81.80,41.35,-81.73,41.41 | Server unreachable (post-credit-exhaustion) |

## Direct Zillow Search URLs
- [44129 — Parma West, ≤$190K](https://www.zillow.com/homes/for_sale/44129_att/41.362,-81.68,41.42,-81.78_rect/11_zm/0-190000_price/0-0_mp/pricea_sort/)
- [44134 — Parma, ≤$190K](https://www.zillow.com/homes/for_sale/44134_att/41.355,-81.65,41.4,-81.72_rect/11_zm/0-190000_price/0-0_mp/pricea_sort/)
- [44130 — Parma East, ≤$190K](https://www.zillow.com/homes/for_sale/44130_att/41.355,-81.73,41.41,-81.8_rect/11_zm/0-190000_price/0-0_mp/pricea_sort/)

## Next Steps
1. Top up Zillapi credits at https://zillapi.com/app/billing
2. Re-run this cron job or trigger manually: `hermes cron run parma-listings-pull`
3. Report will populate `outputs/YYYY-MM-DD/parma-listings-under-190k/parma-listings.md` with full tables and investor verdicts