# Parma West (44129) — Active For-Sale Listings Under $190K

**Pull date:** 2026-10-01 (cron)  
**Source:** Zillow via Camofox browser (`__NEXT_DATA__` extraction)  
**Zillapi status:** ❌ Out of credits  
**Fallback:** Tier 2 — Camofox browser → Zillow search results  
**Rent anchor:** Cleveland-Elyria MSA FY2025 FMR × 90% (Parma submarket adjustment)

---

## Coverage Notes

| ZIP | Requested | Captured | Reason |
|-----|-----------|----------|--------|
| 44129 | ✅ | 10 listings | Primary anchor — wide bounding box |
| 44134 | ✅ | 0 | Not in 44129-anchored bounding box |
| 44130 | ✅ | 0 | Not in 44129-anchored bounding box |

⚠️ **Camofox IP rate limit:** Zillow allows exactly ONE successful search results page load per IP. The 44129-anchored bounding box (`41.42,-81.65,41.35,-81.80_rect`) was chosen to cover all three ZIPs, but all 10 results that surfaced fell within 44129. 44134 and 44130 require separate navigations, which are captcha-blocked after the first load. **44134 and 44130 will need a fresh pull when Zillapi credits refresh or on a different IP.**

---

## Rent Methodology

| Parameter | Value |
|-----------|-------|
| MSA | Cleveland-Elyria, OH |
| FY2025 2BR FMR | $1,098/mo |
| FY2025 3BR FMR | $1,553/mo |
| Parma adjustment | 90% of MSA |
| **Estimated 2BR rent** | **$988/mo** |
| **Estimated 3BR rent** | **$1,398/mo** |

⚠️ All rent figures are **market-derived, NOT property-specific.** Zillow's `__NEXT_DATA__` search results payload does not include `rentZestimate` or `zestimate` for this metro. Individual property pages are captcha-blocked.

---

## 44129 Listings — Sorted by Price (Lowest First)

| # | Address | Price | Beds | Baths | Sqft | $/Sqft | DOM | Tax Assessed | Tax Gap | Est. Rent/mo | GRM | Yield | Verdict |
|---|---------|-------|------|-------|------|--------|-----|-------------|---------|-------------|-----|-------|---------|
| 1 | [6006 Snow Rd](https://www.zillow.com/homedetails/6006-Snow-Rd-Cleveland-OH-44129/2057037610_zpid/) | $165,000 | 3 | 2 | 1,188 | $139 | 6 | N/A | — | $1,398 | 9.8 | 10.2% | **TAKE SELECTIVELY** |
| 2 | [7611 Newport Ave](https://www.zillow.com/homedetails/7611-Newport-Ave-Parma-OH-44129/33547825_zpid/) | $174,900 | 3 | 1 | 1,092 | $160 | 7 | $117,500 | 32.8% | $1,398 | 10.4 | 9.6% | NEGOTIATE |
| 3 | [8324 Ivandale Dr](https://www.zillow.com/homedetails/8324-Ivandale-Dr-Parma-OH-44129/33564869_zpid/) | $175,000 | 3 | 1 | 1,272 | $138 | 34 | $148,400 | 15.2% | $1,398 | 10.4 | 9.6% | NEGOTIATE |
| 4 | [5903 Bradley Ave](https://www.zillow.com/homedetails/5903-Bradley-Ave-Parma-OH-44129/33551238_zpid/) | $179,900 | 3 | 1 | 1,685 | $107 | 0 | $132,200 | 26.5% | $1,398 | 10.7 | 9.3% | NEGOTIATE |
| 5 | [7101 Brownfield Dr](https://www.zillow.com/homedetails/7101-Brownfield-Dr-Parma-OH-44129/33561440_zpid/) | $180,000 | 3 | 1 | 2,186 | $82 | 15 | $156,500 | 13.1% | $1,468 | 10.2 | 9.8% | **TAKE SELECTIVELY** |
| 6 | [5821 Merkle Ave](https://www.zillow.com/homedetails/5821-Merkle-Ave-Parma-OH-44129/33551587_zpid/) | $189,900 | 2 | 2 | 1,235 | $154 | 6 | $135,800 | 28.5% | $988 | 16.0 | 6.2% | **PASS** |
| 7 | [5597 W 54th St](https://www.zillow.com/homedetails/5597-W-54th-St-Parma-OH-44129/33553876_zpid/) | $189,900 | 3 | 1 | 1,636 | $116 | 28 | $156,900 | 17.4% | $1,398 | 11.3 | 8.8% | NEGOTIATE |
| 8 | [6802 Ackley Rd](https://www.zillow.com/homedetails/6802-Ackley-Rd-Parma-OH-44129/33561977_zpid/) | $189,900 | 3 | 2 | 1,244 | $153 | 70 | $172,200 | 9.3% | $1,398 | 11.3 | 8.8% | **PASS** |
| 9 | [8107 Dartworth Dr](https://www.zillow.com/homedetails/8107-Dartworth-Dr-Parma-OH-44129/33563840_zpid/) | $189,900 | 3 | 1 | 1,399 | $136 | 16 | $162,000 | 14.7% | $1,398 | 11.3 | 8.8% | NEGOTIATE |
| 10 | [6311 Thornton Dr](https://www.zillow.com/homedetails/6311-Thornton-Dr-Parma-OH-44129/33562283_zpid/) | $190,000 | 3 | 2 | 1,176 | $162 | 42 | $174,700 | 8.1% | $1,398 | 11.3 | 8.8% | **PASS** |

**Tax Gap** = (Ask Price − Tax Assessed Value) ÷ Ask Price. Values >25% flagged as potentially overpriced vs. county assessment.

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total listings | 10 |
| Median price | $184,950 |
| Min price | $165,000 |
| Max price | $190,000 |
| Median $/sqft | $137 |
| Median DOM | 16 |
| Median GRM (3BR) | 10.7 |
| Median est. gross yield | 9.0% |
| Take/Selectively | 2 |
| Negotiate | 5 |
| Pass | 3 |

---

## Listing Notes

### 🟢 TAKE SELECTIVELY (2)

**1. 6006 Snow Rd — $165,000 (3/2, 1,188 sqft, DOM 6)**
- **Why:** Cheapest entry in the screen. 3/2 configuration with a GRM of 9.8 — the only sub-10 GRM in the set. At $139/sqft, it's reasonable for Parma. Only 6 days on market.
- **Risks:** Cleveland mailing address (not Parma proper — may be near the border). Small sqft. No tax assessed data available — can't verify assessment gap.
- **Action:** Diligence the block quality and exact location. If it's in a solid Parma-adjacent pocket, this is the best cash-flow candidate.

**2. 7101 Brownfield Dr — $180,000 (3/1, 2,186 sqft, DOM 15)**
- **Why:** Massive 2,186 sqft — the largest house in the screen at the second-lowest $/sqft ($82). Price cut $9,900 on 9/26. Tax gap of only 13.1% — the county sees this closer to ask than most. If the extra sqft translates to a 4th bedroom potential or large finished basement, the rent upside could push yield above 10%.
- **Risks:** Only 1 bathroom for 2,186 sqft — that's unusual and may signal a non-conforming layout. Check if there's space to add a second bath economically.
- **Action:** Best value-add candidate. Tour it. If condition is decent and a second bath is feasible, this is the top pick.

### 🟡 NEGOTIATE (5)

**7611 Newport Ave** — GRM 10.4, but 32.8% tax gap is the highest in the screen. County says it's worth $117,500. You'd need to get close to $150K to make this work. Smallest house at 1,092 sqft.

**8324 Ivandale Dr** — Price cut $24,900 on 9/30 is a strong signal the seller is motivated. 34 DOM suggests the market rejected the original $199,900 ask. At $175K with a 15.2% tax gap, it's getting closer. Watch for another cut.

**5903 Bradley Ave** — Brand new listing (0 DOM). 1,685 sqft at $107/sqft is the second-best $/sqft in the screen. But the 26.5% tax gap is concerning — county assessment of $132,200 suggests $150K-$160K is the zone. Let it sit for 2 weeks and watch for a price cut.

**5597 W 54th St** — Solid 1,636 sqft, 28 DOM, 17.4% tax gap. Nothing wrong, nothing special. At $180K with a 1,398/mo rent estimate, it's right at the edge. Offer $170K and it pencils.

**8107 Dartworth Dr** — 1,399 sqft, 16 DOM, 14.7% tax gap. Clean middle-of-the-pack listing. Same story as W 54th — offer below ask and it works.

### 🔴 PASS (3)

**5821 Merkle Ave** — Only 2BR in the screen at $189,900. GRM of 16.0 is terrible — you're paying the same price as 3BR homes for one less bedroom and one less income stream. The 2BR FMR of $988/mo kills this deal. Hard pass unless you can get it under $140K.

**6802 Ackley Rd** — 70 DOM at $189,900 — the market has spoken. Despite being one of only two 3/2 configurations, the tiny 1,244 sqft and near-zero tax gap (9.3%) leave no margin. The county already values it at $172,200. Seller is anchored and not moving. Pass.

**6311 Thornton Dr** — Highest price ($190K), smallest 3BR sqft (1,176), worst $/sqft for a 3BR ($162), and the lowest tax gap (8.1%). 42 DOM with no price cut. This is a retail buyer's house, not an investor's. Pass.

---

## Verdict Logic Reference

| Verdict | Criteria |
|---------|----------|
| **TAKE** | GRM < 10, tax gap < 20%, DOM < 21, reasonable $/sqft |
| **TAKE SELECTIVELY** | GRM 9–11, one flag (location, bath count, or sqft) but offsetting strengths |
| **NEGOTIATE** | GRM 10–12, needs 5-15% price reduction to pencil, or has fixable issues |
| **PASS** | GRM > 12, tax gap < 10% (no margin), 2BR at 3BR pricing, or 40+ DOM with no cuts |

---

## Buy Box: Parma 44129 SFR (Long-Term Rental)

| Parameter | Target | Stretch |
|-----------|--------|---------|
| Price ceiling | $175,000 | $185,000 |
| Beds | 3+ | 3 |
| Baths | 1.5+ | 1 (if expandable) |
| Sqft minimum | 1,200 | 1,100 |
| Target rent (3BR est.) | $1,398/mo | $1,350/mo |
| Target GRM | ≤10.0 | ≤11.0 |
| Target gross yield | ≥10% | ≥9% |
| Tax gap floor | ≥15% | ≥10% |
| DOM filter | Prefer >14 (negotiating leverage) | Any |
| Rehab tolerance | $15K | $25K |
| **AVOID** | 2BR at $170K+, DOM >60 no cuts, tax gap <10% near cap | |

---

## Direct Recommendations

| Category | Pick | Rationale |
|----------|------|-----------|
| **Best cash-flow lead** | 6006 Snow Rd ($165K) | Only sub-10 GRM. Lowest basis = highest cash-on-cash potential. Verify Cleveland/Parma border location. |
| **Best value-add lead** | 7101 Brownfield Dr ($180K) | Massive sqft at $82/sqft. Price cut signals motivation. Add a bath, unlock rent upside. |
| **Best negotiation target** | 8324 Ivandale Dr ($175K) | $24,900 price cut, 34 DOM. Seller wants out. Offer $160K, settle at $165-168K. |
| **Watch list** | 5903 Bradley Ave ($179,900) | New listing, good sqft, bad tax gap. If it cuts to $165K in 2-3 weeks, it becomes the top pick. |
| **Avoid** | 5821 Merkle, 6802 Ackley, 6311 Thornton | All overpriced relative to rent and/or assessed value. No deal at ask. |

---

## Direct Zillow Search URL (Manual Follow-Up)

Open this in your browser to see current results:
```
https://www.zillow.com/homes/for_sale/44129_rb/1-_beds/0-190000_price/pricea_sort/
```

---

## Data Files Saved

| File | Path |
|------|------|
| Full report | `/opt/data/outputs/2026-10-01/parma-listings-under-190k/parma-listings.md` |
| Raw JSON | `/opt/data/outputs/2026-10-01/parma-listings-under-190k/parma_raw.json` |
| Pull status | `/opt/data/parma-pull-status.txt` |
| Quick reference | `/opt/data/parma-latest-listings.md` |

---

## Next Pull: 44134 + 44130

ZIPs 44134 and 44130 were not captured — they require separate Zillow navigations that are captcha-blocked after the first page load (IP-based rate limiting). Options:
1. **Wait for Zillapi credits to refresh** — then pull both via `mcp_zillapi_search_listings` (most reliable, gets rent estimates)
2. **Run from a different IP** — Camofox on a new IP can pull one more ZIP
3. **Manual follow-up** — open the Zillow URLs below in a regular browser:
   - 44134: `https://www.zillow.com/homes/for_sale/44134_rb/1-_beds/0-190000_price/pricea_sort/`
   - 44130: `https://www.zillow.com/homes/for_sale/44130_rb/1-_beds/0-190000_price/pricea_sort/`