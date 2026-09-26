# Parma Submarket — Active Listings Under $190K
**Pull date:** Saturday, September 26, 2026  
**Source:** Zillow.com (Camofox browser → `__NEXT_DATA__` extraction)  
**Zillapi status:** ❌ Out of credits (no Zestimate/rent data available)

---

## Bottom Line

**ZIP 44129 (Parma West)** has 8 active SFH listings under $190K, ranging $165K–$190K. The market is competitive at this price point — all but two listings cluster at $189,900. The stand-out lead is **6006 Snow Rd at $165K** (3/2, 1,188 sqft, GRM ~9.8). Two 2BR listings at $184K–$190K are overpriced for their rent potential and should be passed. No multifamily inventory under $190K in this ZIP.

**ZIPs 44134 and 44130:** Could not be pulled — Zillow triggered Cloudflare "Press & Hold" captcha on the second browser navigation (IP-based rate limiting after a single successful page load). See data gaps section below.

---

## Rent Methodology

⚠️ **All rent figures are market-derived estimates — NOT property-specific.**

- **Source:** HUD FY2025 Fair Market Rents, Cleveland-Elyria MSA
- **Baseline:** 3BR FMR = $1,553/mo; 2BR FMR = $1,098/mo (40th percentile gross rents)
- **Parma adjustment factor:** 90% of MSA (working-class suburb)
- **Estimated Parma rents:** 3BR ≈ **$1,398/mo** | 2BR ≈ **$988/mo**
- `rentZestimate` was **null for all 8 properties** in `__NEXT_DATA__` — typical for this metro
- Individual property pages are captcha-blocked; these estimates are the best available without Zillapi credits

**Formulas used:**
- Annual Gross Rent = Monthly Rent × 12
- GRM = Purchase Price ÷ Annual Gross Rent
- Gross Yield = Annual Gross Rent ÷ Purchase Price

---

## ZIP 44129 — Active Listings (Price: Low → High)

| # | Address | Price | Beds | Baths | Sqft | $/sqft | Est. Rent/mo | GRM | Gross Yield | DOM | Notes | URL |
|---|---------|-------|------|-------|------|--------|-------------|-----|-------------|-----|-------|-----|
| 1 | 6006 Snow Rd, Cleveland | $165,000 | 3 | 2 | 1,188 | $139 | ~$1,398 | **9.8** | **10.2%** | 1 | 3D Tour, Keller Williams Living | [zillow.com](https://www.zillow.com/homedetails/6006-Snow-Rd-Cleveland-OH-44129/2057037610_zpid/) |
| 2 | 7611 Newport Ave, Parma | $174,900 | 3 | 1 | 1,092 | $160 | ~$1,398 | 10.4 | 9.6% | 2 | Additional storage, Keller Williams Greater Metro | [zillow.com](https://www.zillow.com/homedetails/7611-Newport-Ave-Parma-OH-44129/33547825_zpid/) |
| 3 | 6211 Dartworth Dr, Parma | $184,000 | 2 | 1 | 1,085 | $170 | ~$988 | 15.5 | 6.4% | 15 | Open Sat 12-1:30pm, Russell Real Estate | [zillow.com](https://www.zillow.com/homedetails/6211-Dartworth-Dr-Parma-OH-44129/33561552_zpid/) |
| 4 | 6507 Forest Ave, Parma | $189,900 | 3 | 2 | 1,026 | $185 | ~$1,398 | 11.3 | 8.8% | 1 | Open Sat 10:30am-12:30pm, RE/MAX Above & Beyond | [zillow.com](https://www.zillow.com/homedetails/6507-Forest-Ave-Parma-OH-44129/33550416_zpid/) |
| 5 | 5821 Merkle Ave, Parma | $189,900 | 2 | 2 | 1,235 | $154 | ~$988 | 16.0 | 6.2% | 0 | Listed ~18 hours ago, EXP Realty | [zillow.com](https://www.zillow.com/homedetails/5821-Merkle-Ave-Parma-OH-44129/33551587_zpid/) |
| 6 | 5597 W 54th St, Parma | $189,900 | 3 | 1 | 1,636 | $116 | ~$1,398 | 11.3 | 8.8% | 22 | Beautiful curb appeal, EXP Realty | [zillow.com](https://www.zillow.com/homedetails/5597-W-54th-St-Parma-OH-44129/33553876_zpid/) |
| 7 | 7101 Brownfield Dr, Parma | $189,900 | 3 | 1 | 2,186 | $87 | ~$1,398 | 11.3 | 8.8% | 10 | Hardwood floors throughout, EXP Realty | [zillow.com](https://www.zillow.com/homedetails/7101-Brownfield-Dr-Parma-OH-44129/33561440_zpid/) |
| 8 | 6311 Thornton Dr, Parma | $190,000 | 3 | 2 | 1,176 | $162 | ~$1,398 | 11.3 | 8.8% | 37 | Stale — 37 DOM, Berkshire Hathaway Pro Realty | [zillow.com](https://www.zillow.com/homedetails/6311-Thornton-Dr-Parma-OH-44129/33562283_zpid/) |

---

## Investor Verdicts — ZIP 44129

### 🟢 TAKE Selectively

**6006 Snow Rd — $165,000 (3/2, 1,188 sqft, GRM 9.8)**
- **Best deal in the set.** $24K–$25K below the $189,900 cluster pricing for comparable 3/2 product.
- Only 1 day on market — will move fast at this price.
- Estimated gross yield 10.2% puts it in solid cash-flow territory for Parma.
- Diligence needed: condition, mechanicals, roof age, block quality. At $139/sqft there's likely deferred maintenance — figure a $15K–$25K rehab reserve.
- If systems are sound, this is a **buy at ask** candidate.

### 🟡 NEGOTIATE

**7611 Newport Ave — $174,900 (3/1, 1,092 sqft, GRM 10.4)**
- Second-best basis; GRM 10.4 is workable. Only 1 bathroom limits rent ceiling and tenant pool.
- Offer $160K–$165K to push GRM under 10. At ask, the single bath makes this a stretch.

**6507 Forest Ave — $189,900 (3/2, 1,026 sqft, GRM 11.3)**
- Smallest 3BR in the set — 1,026 sqft is tight. 2 baths helps. Open house today.
- At ask, GRM 11.3 is borderline for Parma. Needs to rent at $1,500+ to work, which is above the 90% MSA estimate for this block.
- Offer $170K or lower.

**5597 W 54th St — $189,900 (3/1, 1,636 sqft, GRM 11.3)**
- Largest 3BR at 1,636 sqft — spacious but only 1 bath. 22 DOM suggests it's sitting.
- Good value-add candidate if a half-bath can be added affordably. At $116/sqft, priced well per square foot.
- Offer $170K–$175K.

**7101 Brownfield Dr — $189,900 (3/1, 2,186 sqft, GRM 11.3)**
- Biggest house in the set at 2,186 sqft; hardwood floors. Only 1 bathroom is the bottleneck — a house this size needs 2 baths.
- $87/sqft is the cheapest per-square-foot in the set. Good forced-appreciation play if 2nd bath can be added.
- Offer $170K–$175K; factor $20K+ for bath addition in rehab budget.

**6311 Thornton Dr — $190,000 (3/2, 1,176 sqft, GRM 11.3)**
- 37 days on market — the stale listing. Seller may be motivated.
- 3/2 is the right configuration; size is adequate. At $162/sqft it's mid-pack.
- Use DOM as leverage. Offer $170K–$175K. If they won't budge, move on to the Snow Rd property.

### 🔴 PASS

**6211 Dartworth Dr — $184,000 (2/1, 1,085 sqft, GRM 15.5)**
- 2BR/1BA can't justify $184K in this market. Estimated rent ~$988/mo yields 6.4% gross — negative cash flow after taxes and insurance.
- There are 3BR houses at $165K–$175K. No reason to settle for 2BR at a higher basis.

**5821 Merkle Ave — $189,900 (2/2, 1,235 sqft, GRM 16.0)**
- 2BR at 3BR pricing. GRM 16.0 is the worst in the set. Even with 2 baths, the rent ceiling for a 2BR in Parma (~$988/mo estimated) doesn't support this price.
- Unless this is owner-occupied, hard pass.

---

## Multifamily (2–4 Unit) — ZIP 44129

**No multifamily inventory under $190K.** All 8 active listings are single-family. If duplexes exist in this ZIP below $190K, none are currently on market. The multifamily hunting ground in Parma (44129/44134/44130) likely starts above $200K.

---

## Data Gaps

### ZIP 44134 (Parma East)
- ❌ **Could not pull.** Zillow triggered "Press & Hold" captcha on second browser navigation.
- Direct Zillow search URL for manual follow-up: https://www.zillow.com/homes/for_sale/44134_rb/1-_beds/0-190000_price/pricea_sort/

### ZIP 44130 (Middleburg Heights / Parma Heights)
- ❌ **Could not pull.** Same IP-based captcha block.
- Direct Zillow search URL for manual follow-up: https://www.zillow.com/homes/for_sale/44130_rb/1-_beds/0-190000_price/pricea_sort/

### Zillapi credits
- ❌ Exhausted for this cycle. All three ZIP queries failed — first returned "Out of credits," subsequent calls hit MCP server unreachable.
- No Zestimate, rentZestimate, or year-built data available for any listing.

---

## Buy Box — ZIP 44129 SFR

| Parameter | Target | Stretch |
|-----------|--------|---------|
| **Preferred ZIPs** | 44129 | 44134, 44130 (unverified) |
| **Property type** | 3BR/2BA SFR | 3BR/1BA with bath-add potential |
| **Target all-in basis** | ≤$170,000 | ≤$185,000 |
| **Target monthly rent** | ≥$1,400/mo (3BR) | ≥$1,250/mo (3BR) |
| **Target gross yield** | ≥9.5% | ≥8.5% |
| **Target GRM** | ≤10.5 | ≤11.8 |
| **Rehab tolerance** | $15K–$25K | $30K (if bath addition) |
| **Avoid** | 2BR at >$175K; $/sqft >$170 without rent upside; >30 DOM without price cut | |

---

## Direct Recommendations

- **Best current SFR lead:** 6006 Snow Rd at $165K (3/2, GRM 9.8, 1 DOM — act fast)
- **Best forced-appreciation play:** 7101 Brownfield Dr (2,186 sqft at $87/sqft, add 2nd bath)
- **Best negotiation target:** 6311 Thornton Dr (37 DOM, ask $190K, offer $170K–$175K)
- **Avoid entirely:** 6211 Dartworth Dr ($184K 2BR) and 5821 Merkle Ave ($190K 2BR)
- **Next step for 44134/44130:** Open the direct Zillow URLs above in a personal browser (not captcha-blocked) or wait for Zillapi credit refresh

---

*Report generated by Hermes Agent (Loki profile) — cron job, 2026-09-26. Source: Zillow.com via Camofox browser, `__NEXT_DATA__` extraction. Rent estimates: HUD FY2025 FMR, Cleveland-Elyria MSA × 0.90 Parma adjustment.*