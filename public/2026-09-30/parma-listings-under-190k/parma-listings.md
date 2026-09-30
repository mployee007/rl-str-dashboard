# Parma Area — For-Sale Listings Under $190K

**Pull date:** 2026-09-30
**Fresh data:** ❌ NOT AVAILABLE — Zillapi out of credits, Camofox captcha-blocked
**Data shown:** From 2026-09-29 pull (1 day stale). DOM values aged +1.
**Source:** Zillow.com (Camofox browser → `__NEXT_DATA__` extraction, 9/29 pull)
**Rent anchor:** Cleveland-Elyria MSA FY2025 FMR, Parma-adjusted (90% of MSA) ⚠️ Market-derived — NOT property-specific
**ZIPs covered:** 44129 only. 44134 and 44130 blocked by Zillow captcha.

---

## Source Status

| Source | Status | Result |
|--------|--------|--------|
| Zillapi MCP | ❌ Out of credits | "Out of credits for this cycle" |
| Camofox → Zillow 44129 | ❌ Captcha-blocked | Cloudflare "Press & Hold" — IP rate-limited |
| Camofox → Zillow 44134 | ❌ Captcha-blocked | Never reached — single nav per IP |
| Camofox → Zillow 44130 | ❌ Captcha-blocked | Never reached — single nav per IP |
| Prior data (9/29) | ✅ Available | 7 listings for 44129; 44134/44130 not covered |

---

## ⚠️ STALE DATA WARNING

The listings below are from the **2026-09-29 pull** — DOM values have been aged +1 day but may not reflect new listings, price changes, or off-market removals since then. Treat all data as approximate.

---

## Bottom Line

**7 active SFR listings under $190K in ZIP 44129 (as of 9/29, aged to 9/30).** Two properties stood out on 9/29: **6006 Snow Rd ($165K)** as the best cash-flow lead (GRM 9.8, 3bd/2ba), and **7101 Brownfield Dr ($180K)** as the best value-add play ($82/sqft, seller cut $9,900 on 9/26). 44134 and 44130 remain uncovered.

---

## Rent Methodology

All `rentZestimate` and `zestimate` fields returned `null` in `__NEXT_DATA__` — standard for Midwest metros. Rent estimates use:

| Bedrooms | Cleveland-Elyria MSA FY2025 FMR | Parma 90% Adjustment | Used |
|----------|--------------------------------|-----------------------|------|
| 2BR | $1,098 | $988 | **$988/mo** |
| 3BR | $1,553 | $1,398 | **$1,398/mo** |

Source: U.S. HUD FY2025 Fair Market Rents (40th percentile gross rent). Verify at [huduser.gov](https://www.huduser.gov/portal/datasets/fmr.html).

---

## 44129 — Active Listings (Price Low → High) — Data from 9/29, aged +1 DOM

| # | Address | Price | Beds | Baths | Sqft | $/Sqft | DOM* | Est. Rent/mo | GRM | Tax Assessed | Ask vs Tax | Notes | Verdict |
|---|---------|-------|------|-------|------|--------|------|-------------|-----|-------------|------------|-------|---------|
| 1 | [6006 Snow Rd](https://www.zillow.com/homedetails/6006-Snow-Rd-Cleveland-OH-44129/2057037610_zpid/) | $165,000 | 3 | **2** | 1,188 | $139 | 5 | $1,398 | **9.8** | — | — | 3D Tour, Cleveland address but 44129 ZIP | **TAKE** |
| 2 | [7611 Newport Ave](https://www.zillow.com/homedetails/7611-Newport-Ave-Parma-OH-44129/33547825_zpid/) | $174,900 | 3 | 1 | 1,092 | $160 | 6 | $1,398 | 10.4 | $117,500 | +48.9% | Additional storage, 1-bath limits rent | **NEGOTIATE** |
| 3 | [7101 Brownfield Dr](https://www.zillow.com/homedetails/7101-Brownfield-Dr-Parma-OH-44129/33561440_zpid/) | $180,000 | 3 | 1 | **2,186** | **$82** | 14 | $1,398 | 10.7 | $156,500 | +15.0% | 🔻 Price cut $9,900 (9/26), largest sqft | **TAKE SELECTIVELY** |
| 4 | [6211 Dartworth Dr](https://www.zillow.com/homedetails/6211-Dartworth-Dr-Parma-OH-44129/33561552_zpid/) | $184,000 | 2 | 1 | 1,085 | $170 | 19 | $988 | 15.5 | $151,100 | +21.8% | 🔻 Price cut $5,000 (9/22), only 2bd | **PASS** |
| 5 | [5821 Merkle Ave](https://www.zillow.com/homedetails/5821-Merkle-Ave-Parma-OH-44129/33551587_zpid/) | $189,900 | 2 | 2 | 1,235 | $154 | 4 | $988 | 16.0 | $135,800 | +39.8% | Partially fenced yard, large tax gap | **PASS** |
| 6 | [5597 W 54th St](https://www.zillow.com/homedetails/5597-W-54th-St-Parma-OH-44129/33553876_zpid/) | $189,900 | 3 | 1 | 1,636 | $116 | 26 | $1,398 | 11.3 | $156,900 | +21.0% | Stale, decent $/sqft, negotiable | **NEGOTIATE** |
| 7 | [6311 Thornton Dr](https://www.zillow.com/homedetails/6311-Thornton-Dr-Parma-OH-44129/33562283_zpid/) | $190,000 | 3 | **2** | 1,176 | $162 | 41 | $1,398 | 11.3 | $174,700 | +8.8% | Stale 41 DOM, tightest tax gap | **NEGOTIATE** |

*\*DOM values shown are from 9/29 pull + 1 day aged. Actual DOM may differ.*

**GRM** = Price / (Est. Monthly Rent × 12). Lower = better cash flow.
**Ask vs Tax** = (Ask − Tax Assessed) / Tax Assessed. Larger gaps may indicate overpricing.

---

## Verdict Summary

### 🟢 TAKE — Strong Cash Flow
- **6006 Snow Rd ($165K, 3bd/2ba)** — GRM 9.8, $139/sqft, 2 bathrooms. Best cash-flow candidate. May have gone under contract since 9/29.

### 🟡 TAKE SELECTIVELY — Value Play
- **7101 Brownfield Dr ($180K, 3bd/1ba)** — $82/sqft, 2,186 sqft (largest by 34%). Seller cut $9,900 on 9/26. Could push rent above FMR with this square footage.

### 🟠 NEGOTIATE — Price Reduction Needed
- **7611 Newport Ave ($174,900)** — Needs ~$155-160K for GRM under 10. 1-bath limits rent.
- **5597 W 54th St ($189,900)** — 26 DOM, push to $170-175K.
- **6311 Thornton Dr ($190,000)** — 41 DOM, tight tax gap. Push below assessed ($175K).

### 🔴 PASS — Doesn't Pencil
- **6211 Dartworth Dr ($184K)** — GRM 15.5, 2bd. Not viable for cash-flow.
- **5821 Merkle Ave ($189,900)** — GRM 16.0, tax gap 39.8%. Overpriced by ~$50K+.

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

## 44134 & 44130 — Still Uncovered

Both ZIPs have been consistently blocked across multiple pull attempts due to Zillow's single-navigation-per-IP captcha.

**Manual follow-up URLs:**
- **44134:** [Parma East under $190K](https://www.zillow.com/homes/for_sale/44134_rb/1-_beds/0-190000_price/pricea_sort/)
- **44130:** [Middleburg Heights under $190K](https://www.zillow.com/homes/for_sale/44130_rb/1-_beds/0-190000_price/pricea_sort/)

**Recommendation:** Separate cron pulls on different days, or use a VPN/proxy rotation to pull each ZIP from a different IP.

---

*Generated 2026-09-30 by Hermes Agent (Loki profile). Listings sourced from 9/29 Zillow pull — 1 day stale. Rent estimates are HUD FY2025 FMR-derived, not property-specific. Verify individual property rents and current listing status before making offers.*