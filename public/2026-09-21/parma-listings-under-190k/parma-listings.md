# Parma Area Listings Under $190K — STATUS: ZILLAPI DOWN

**Run date:** 2026-09-21
**Target ZIPs:** 44129, 44134, 44130
**Price cap:** $190,000

---

## ❌ Pull Failed — Zillapi Unavailable

| Error | Detail |
|-------|--------|
| Zillapi credits | Exhausted — `Out of credits for this cycle` |
| Zillapi MCP server | Unreachable (131 consecutive failures) |

---

## Direct Zillow Links (Manual Fallback)

| ZIP | Area | Zillow Search |
|-----|------|--------------|
| 44129 | Parma West | [View on Zillow](https://www.zillow.com/homes/for_sale/44129_zip/1-_beds/0-190000_price/0-405_mp/) |
| 44134 | Parma East / Seven Hills | [View on Zillow](https://www.zillow.com/homes/for_sale/44134_zip/1-_beds/0-190000_price/0-405_mp/) |
| 44130 | Middleburg Heights / Parma Heights | [View on Zillow](https://www.zillow.com/homes/for_sale/44130_zip/1-_beds/0-190000_price/0-405_mp/) |

---

## What Was Requested

- Active for-sale house listings (1+ beds) under $190K in ZIPs 44129, 44134, 44130
- Property details: address, price, beds, baths, sqft, zpid, rentZestimate, condition/DOM notes
- Sorted by price (lowest first), with investor verdict column (take/negotiate/pass)
- Output to `/opt/data/outputs/2026-09-21/parma-listings-under-190k/parma-listings.md`

---

## Resolution

This cron job will re-attempt on the next scheduled run. No listings were fabricated. Status file saved at `/opt/data/parma-pull-status.txt`.

To resume manually when credits are available, re-run this skill with the same parameters.