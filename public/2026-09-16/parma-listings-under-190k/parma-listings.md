# Parma Area Listings Under $190K — Pull Attempt

**Date:** 2026-09-16 23:26 UTC  
**Status:** ❌ FAILED — Zillapi credits exhausted

---

## Blocker Summary

| Source | Attempted? | Result |
|--------|-----------|--------|
| Zillapi MCP (`mcp_zillapi_search_listings`) | ✅ Yes (3 calls) | **Out of credits** (ZIP 44129); MCP server unreachable (44134, 44130) |
| Zillow.com (browser) | ⛔ Skipped | Per skill: blocked by PerimeterX/Cloudflare captchas |
| Redfin | ⛔ Skipped | Per skill: blocked by captchas |
| Realtor.com | ⛔ Skipped | Per skill: blocked by captchas |
| Web search | ⛔ Skipped | Per skill: unreliable for live listings |

---

## Target Search Parameters

| ZIP | Neighborhood | Bounding Box | Max Price |
|-----|-------------|-------------|-----------|
| 44129 | Parma West | -81.78, 41.37, -81.68, 41.42 | $190,000 |
| 44134 | Parma SE | -81.72, 41.35, -81.65, 41.40 | $190,000 |
| 44130 | Parma SW / Middleburg Hts | -81.80, 41.35, -81.73, 41.41 | $190,000 |

---

## Direct Zillow Search URLs

Open these in your browser to view current listings manually:

- **[ZIP 44129 — For Sale ≤$190K](https://www.zillow.com/homes/for_sale/44129/0-190000_price/0-500000_mp/41.420494,-81.679813,41.369944,-81.780163_rect/12_zm/)**  
- **[ZIP 44134 — For Sale ≤$190K](https://www.zillow.com/homes/for_sale/44134/0-190000_price/0-500000_mp/41.399541,-81.649789,41.349628,-81.720312_rect/12_zm/)**  
- **[ZIP 44130 — For Sale ≤$190K](https://www.zillow.com/homes/for_sale/44130/0-190000_price/0-500000_mp/41.409674,-81.72993,41.350031,-81.80056_rect/12_zm/)**

---

## Next Steps

1. **Top up Zillapi credits** at https://zillapi.com/app/billing
2. Re-run this cron job or trigger manually: `hermes cron run parma-submarket-screen`
3. The pipeline will auto-populate listing tables with investor verdicts (take / negotiate / pass)
4. Results will land in:
   - `/opt/data/outputs/YYYY-MM-DD/parma-listings-under-190k/parma-listings.md` (full report)
   - `/opt/data/parma-latest-listings.md` (quick-reference table)

---

## Context: Why This Pull Matters

This screen targets the sub-$190K band across three core Parma ZIPs — the sweet spot for first-time landlord acquisition in Cuyahoga County's most stable working-class suburbs. When credits are restored, the pipeline extracts: address, price, beds, baths, sqft, zpids with direct Zillow URLs, rent Zestimates, and listing condition notes — all sorted lowest-price-first with explicit investor verdicts.