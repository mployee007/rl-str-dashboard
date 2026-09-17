# Parma Area Listings Under $190K — Pull Attempt

**Date:** 2026-09-17 00:00 UTC  
**Status:** ❌ FAILED — Zillapi credits exhausted (2nd consecutive day)

---

## Blocker Summary

| Source | Attempted? | Result |
|--------|-----------|--------|
| Zillapi MCP (`mcp_zillapi_search_listings`) | ✅ Yes (3 calls) | **Out of credits** (ZIP 44129 first call); MCP server unreachable for 44134 and 44130 (cascade from credit exhaustion) |
| Zillow.com (browser) | ⛔ Skipped | Per skill: blocked by PerimeterX/Cloudflare captchas |
| Redfin | ⛔ Skipped | Per skill: blocked by captchas |
| Realtor.com | ⛔ Skipped | Per skill: blocked by captchas |
| Web search | ⛔ Skipped | Per skill: unreliable for live listings |

---

## Target Search Parameters

| ZIP | Neighborhood | Bounding Box | Max Price |
|-----|-------------|-------------|-----------|
| 44129 | Parma West | -81.78, 41.37, -81.68, 41.42 | $190,000 |
| 44134 | Parma SE / Brooklyn Hts | -81.72, 41.35, -81.65, 41.40 | $190,000 |
| 44130 | Parma Mid / Middleburg Hts | -81.80, 41.35, -81.73, 41.41 | $190,000 |

---

## Historical ZIP Context (from last successful Cleveland pull)

These are benchmarks, NOT current live listings. Use for directional sizing only.

| ZIP | Neighborhood | Sale Count | Median Sale | Rent Count | Median Rent | Price/Rent | Gross Yield | Investor Fit |
|-----|-------------|-----------|-------------|-----------|-------------|-----------|-------------|--------------|
| **44129** | Parma West | 16 | **$190,000** | 30 | **$1,950** | 8.1x | **12.32%** | 🟢 Strong stabilized hold — median sits right at the $190K cap; sub-$190K deals in this ZIP are the sweet spot |
| **44134** | Parma SE / Brooklyn Hts | 44 | $200,000 | 32 | $1,675 | 10.0x | 10.05% | 🟡 Higher volume but median above cap — need to cherry-pick below-median; weaker yield than 44129 |
| **44130** | Parma Mid | 7 | $199,900 | 0 | $1,575 | 10.6x | 9.45% | 🟠 Thin inventory (7 sales), median above cap, weakest yield — least attractive of the three |

---

## Investor Takeaway (Directional Only)

**44129 is the clear priority ZIP** in the sub-$190K Parma screen:
- Median sale sits exactly at the $190,000 cap, meaning roughly half of listings fall below it
- Strongest gross yield at 12.32% — every point above 10% matters in a Midwest buy-and-hold strategy
- 30 rent comps available for triangulation
- Price-to-rent ratio of 8.1x is investment-grade ($1 in price buys ~$0.12 in annual rent)

**44134 is the secondary target:** 44 sale listings is 2.75× the volume of 44129, but median at $200K means you're fishing below-median. The yield spread (10.05% vs 12.32%) is ~230 bps — that's real money on a $150-190K basis.

**44130 should be deprioritized:** only 7 sales in the sample, median above cap, weakest yield. Unless a specific deal surfaces with a strong rent roll, the juice isn't worth the squeeze.

---

## Direct Zillow Search URLs

Open these in your browser to view current listings manually:

- **[ZIP 44129 — For Sale ≤$190K](https://www.zillow.com/homes/for_sale/44129/0-190000_price/0-500000_mp/41.420494,-81.679813,41.369944,-81.780163_rect/12_zm/)**
- **[ZIP 44134 — For Sale ≤$190K](https://www.zillow.com/homes/for_sale/44134/0-190000_price/0-500000_mp/41.399541,-81.649789,41.349628,-81.720312_rect/12_zm/)**
- **[ZIP 44130 — For Sale ≤$190K](https://www.zillow.com/homes/for_sale/44130/0-190000_price/0-500000_mp/41.409674,-81.72993,41.350031,-81.80056_rect/12_zm/)**

---

## Next Steps

1. **Top up Zillapi credits** at https://zillapi.com/app/billing
2. Re-run this cron job or trigger manually
3. When credits are live, the pipeline will:
   - Pull live listing tables sorted lowest-price-first
   - Attach rent Zestimates and listing condition notes
   - Assign investor verdicts (take / negotiate / pass) per property
4. Results land in:
   - `/opt/data/outputs/YYYY-MM-DD/parma-listings-under-190k/parma-listings.md` (full report)
   - `/opt/data/parma-latest-listings.md` (quick-reference table)

---

*Report generated 2026-09-17 — awaiting Zillapi credit refresh for live data.*