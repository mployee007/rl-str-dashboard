# Parma West Listings — Under $190K
**Pull Date:** 2026-09-15 · **Status:** BLOCKED — Zillapi out of credits

---

## ⛔ Zillapi Credit Exhaustion

All three ZIP searches failed because the Zillapi account is out of credits for this billing cycle.

| ZIP | Bounding Box | Error |
|-----|-------------|-------|
| **44129** (Parma West) | `-81.78,41.37,-81.68,41.42` | Out of credits |
| **44134** (Parma South) | `-81.72,41.35,-81.65,41.40` | Server unreachable (cascading) |
| **44130** (Middleburg Hts / Parma border) | `-81.80,41.35,-81.73,41.41` | Server unreachable (cascading) |

---

## Manual Fallback: Direct Zillow Search Links

Open these in your browser to see live listings under $190K in each ZIP:

- **[44129 — Parma West](https://www.zillow.com/homes/for_sale/44129_rb/0-190000_price/0-527_mp/)**  
- **[44134 — Parma South](https://www.zillow.com/homes/for_sale/44134_rb/0-190000_price/0-527_mp/)**  
- **[44130 — Middleburg Hts (adjacent)](https://www.zillow.com/homes/for_sale/44130_rb/0-190000_price/0-527_mp/)**

---

## What Will Be In the Report Once Credits Refresh

1. **Ranked listing table per ZIP** sorted by price (lowest first)
2. **Columns:** Address, Price, Beds, Baths, Sqft, ZPID (with Zillow URL), rentZestimate, DOM, condition notes
3. **Investor verdict column** — take / negotiate / pass — based on price-to-rent ratio and condition
4. **Quick-reference file** at `/opt/data/parma-latest-listings.md`

---

## Resume Instructions

Top up at https://zillapi.com/app/billing, then re-trigger this cron job. The skill will auto-resume.