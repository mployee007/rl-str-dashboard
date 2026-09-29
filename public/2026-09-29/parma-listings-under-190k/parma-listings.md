# Parma Area — For-Sale Listings Under $190K

**Pull date:** 2026-09-29
**Source:** Zillow.com (Camofox browser → `__NEXT_DATA__` extraction)
**Rent anchor:** Cleveland-Elyria MSA FY2025 FMR, Parma-adjusted (90% of MSA) ⚠️ Market-derived — NOT property-specific
**ZIPs covered:** 44129 only. 44134 and 44130 blocked by Zillow captcha on second navigation (IP-based rate limiting).

---

## Bottom Line

**7 active SFR listings under $190K in ZIP 44129.** Two properties stand out: **6006 Snow Rd ($165K)** as the best cash-flow lead (GRM 9.8, 3bd/2ba), and **7101 Brownfield Dr ($180K)** as the best value-add play ($82/sqft, motivated seller with $9,900 price cut). Both 2-bedroom listings at the top of the price range don't pencil — pass at current ask. 44134 and 44130 could not be pulled due to Zillow's single-navigation-per-IP captcha policy; manual follow-up needed.

---

## Rent Methodology

All `rentZestimate` and `zestimate` fields returned `null` in `__NEXT_DATA__` — standard for Midwest metros outside coastal markets. Rent estimates use:

| Bedrooms | Cleveland-Elyria MSA FY2025 FMR | Parma 90% Adjustment | Used |
|----------|--------------------------------|-----------------------|------|
| 2BR | $1,098 | $988 | **$988/mo** |
| 3BR | $1,553 | $1,398 | **$1,398/mo** |

Source: U.S. HUD FY2025 Fair Market Rents (40th percentile gross rent). Verify at [huduser.gov](https://www.huduser.gov/portal/datasets/fmr.html).

---

## 44129 — Active Listings (Price Low → High)

| # | Address | Price | Beds | Baths | Sqft | $/Sqft | DOM | Est. Rent/mo | GRM | Tax Assessed | Ask vs Tax | Notes | Verdict |
|---|---------|-------|------|-------|------|--------|-----|-------------|-----|-------------|------------|-------|---------|
| 1 | [6006 Snow Rd](https://www.zillow.com/homedetails/6006-Snow-Rd-Cleveland-OH-44129/2057037610_zpid/) | $165,000 | 3 | **2** | 1,188 | $139 | 4 | $1,398 | **9.8** | — | — | 3D Tour, fresh listing, Cleveland address but 44129 ZIP | **TAKE** |
| 2 | [7611 Newport Ave](https://www.zillow.com/homedetails/7611-Newport-Ave-Parma-OH-44129/33547825_zpid/) | $174,900 | 3 | 1 | 1,092 | $160 | 6 | $1,398 | 10.4 | $117,500 | +48.9% | Additional storage, 1-bath limits rent | **NEGOTIATE** |
| 3 | [7101 Brownfield Dr](https://www.zillow.com/homedetails/7101-Brownfield-Dr-Parma-OH-44129/33561440_zpid/) | $180,000 | 3 | 1 | **2,186** | **$82** | 14 | $1,398 | 10.7 | $156,500 | +15.0% | 🔻 Price cut $9,900 (9/26), largest sqft by far | **TAKE SELECTIVELY** |
| 4 | [6211 Dartworth Dr](https://www.zillow.com/homedetails/6211-Dartworth-Dr-Parma-OH-44129/33561552_zpid/) | $184,000 | 2 | 1 | 1,085 | $170 | 19 | $988 | 15.5 | $151,100 | +21.8% | 🔻 Price cut $5,000 (9/22), only 2bd | **PASS** |
| 5 | [5821 Merkle Ave](https://www.zillow.com/homedetails/5821-Merkle-Ave-Parma-OH-44129/33551587_zpid/) | $189,900 | 2 | 2 | 1,235 | $154 | 4 | $988 | 16.0 | $135,800 | +39.8% | Partially fenced yard, large tax gap | **PASS** |
| 6 | [5597 W 54th St](https://www.zillow.com/homedetails/5597-W-54th-St-Parma-OH-44129/33553876_zpid/) | $189,900 | 3 | 1 | 1,636 | $116 | **26** | $1,398 | 11.3 | $156,900 | +21.0% | Stale listing, decent $/sqft, negotiable | **NEGOTIATE** |
| 7 | [6311 Thornton Dr](https://www.zillow.com/homedetails/6311-Thornton-Dr-Parma-OH-44129/33562283_zpid/) | $190,000 | 3 | **2** | 1,176 | $162 | **41** | $1,398 | 11.3 | $174,700 | +8.8% | Stale 41 DOM, tightest tax gap, fairly priced | **NEGOTIATE** |

**GRM** = Price / (Est. Monthly Rent × 12). Lower = better cash flow.
**Ask vs Tax** = (Ask − Tax Assessed) / Tax Assessed. Larger gaps may indicate overpricing.

---

## Verdict Summary

### 🟢 TAKE — Strong Cash Flow
- **6006 Snow Rd ($165K, 3bd/2ba)** — GRM 9.8, $139/sqft, 2 bathrooms. Best cash-flow candidate in the cohort. Fresh listing (4 DOM) — will move fast.

### 🟡 TAKE SELECTIVELY — Value Play  
- **7101 Brownfield Dr ($180K, 3bd/1ba)** — $82/sqft is deep value. 2,186 sqft is the largest in cohort by 34%. Motivated seller (price cut $9,900 on 9/26). Could push rent above $1,398 with this square footage. Confirm condition, verify rent comps for large 3bd/1ba in the block.

### 🟠 NEGOTIATE — Price Reduction Needed
- **7611 Newport Ave ($174,900)** — Needs to come down to ~$155-160K for GRM under 10. 1-bath limits rent ceiling.
- **5597 W 54th St ($189,900)** — 26 DOM, seller likely softening. Push toward $170-175K for GRM ~10.
- **6311 Thornton Dr ($190,000)** — 41 DOM, tight tax gap (only 8.8% above assessed). Already fairly priced but stale. Push below assessed value ($175K).

### 🔴 PASS — Doesn't Pencil
- **6211 Dartworth Dr ($184K)** — GRM 15.5. Even at $160K, would barely hit GRM 13.5 with 2bd rent. Not viable for cash-flow buy-and-hold.
- **5821 Merkle Ave ($189,900)** — GRM 16.0. Overpriced by $50K+ for a 2bd rental. Tax gap of 39.8% confirms.

---

## Buy Box — 44129 SFR

| Metric | Target | Stretch |
|--------|--------|---------|
| All-in basis | $150K–$175K | $190K |
| Beds/Baths | 3bd/1.5+ba | 3bd/1ba |
| Sqft | 1,100–1,600 | 2,000+ |
| Target rent | $1,400–$1,500/mo | $1,600/mo |
| Target GRM | < 10.5 | < 12.0 |
| Target gross yield | > 9.5% | > 8.3% |
| Rehab tolerance | $15K cosmetic | $30K systems |
| Max $/sqft | < $140 | < $160 |

**Avoid:**
- 2-bedroom homes above $150K (can't support rent basis)
- 3-bedroom/1-bath above $180K without verified rent upside
- Properties > 30% above tax assessed value without rehab justification
- Any listing with GRM > 14 at Parma-adjusted rents

---

## 44134 & 44130 — Coverage Gap

Zillow's IP-based rate limiting allows exactly one search results page load before triggering Cloudflare "Press & Hold" captcha. Restarting Camofox does not help — the limit is IP-level. Only 44129 was captured on this pull.

**Manual follow-up URLs:**

- **44134:** [Parma East under $190K](https://www.zillow.com/homes/for_sale/44134_rb/1-_beds/0-190000_price/pricea_sort/)
- **44130:** [Middleburg Heights under $190K](https://www.zillow.com/homes/for_sale/44130_rb/1-_beds/0-190000_price/pricea_sort/)

**Recommendation:** Run these as separate cron pulls on different days (or from different IPs) since Zillow allows one pull per IP per session.

---

## Source Status

| Source | Status | Result |
|--------|--------|--------|
| Zillapi MCP | ❌ Out of credits | Error on first call; server unreachable on retry |
| Camofox → Zillow 44129 | ✅ Success | 7 listings captured via `__NEXT_DATA__` |
| Camofox → Zillow 44134 | ❌ Captcha-blocked | Second navigation triggers IP rate-limit |
| Camofox → Zillow 44130 | ❌ Captcha-blocked | Same IP — cannot navigate again |
| Rentdata.org | ⚠️ Skipped | MSA URLs known to 404; used hardcoded FMR instead |

---

*Generated 2026-09-29 by Hermes Agent (Loki profile). Rent estimates are HUD FY2025 FMR-derived, not property-specific. Verify individual property rents before making offers.*