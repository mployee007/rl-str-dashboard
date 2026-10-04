# Parma Listings Screen — Under $190K

**Date:** 2026-10-04 (automated cron)
**Target ZIPs:** 44129, 44134, 44130
**Status:** ⚠️ PARTIAL — 44129 data available (fresh pull today). 44134 and 44130 blocked (Zillapi credits exhausted, Camofox captcha'd).

---

## Data Source Status

| Source | Result |
|--------|--------|
| **Zillapi MCP** (`mcp_zillapi_search_listings`) | ❌ Out of credits. "Out of credits for this cycle." Subsequent calls unreachable (38 consecutive failures). |
| **Camofox → Zillow search results** | ❌ IP rate-limited. Cloudflare "Press & Hold" captcha on first navigation to `44129_rb/`. Reference ID `7ac67135-c03b-11f1-9171-f12b8c1cc1eb`. |
| **SearXNG / agent_search** | ❌ Returned Parma, Italy results — not Ohio. Confirmed skill pitfall. |
| **web_search / web_extract** | ❌ Requires firecrawl — unavailable in cron (lazy installs disabled). |
| **Prior saved data (44129)** | ✅ Fresh pull from earlier today (2026-10-04) — 13 listings under $190K. |

**44134 and 44130 are blocked** — Zillapi credits exhausted AND Camofox IP is captcha'd. Only 44129 data is available from an earlier pull this morning.

---

## Market Context: Cleveland-Elyria MSA → Parma Submarket

### Rent Anchors (FY2025 HUD Fair Market Rents — 40th percentile gross rent)

Cleveland-Elyria MSA baseline with Parma adjustment (90% of MSA):

| Unit | MSA FMR | Parma Est. (90%) |
|------|---------|-------------------|
| Studio | $824 | $742 |
| 1BR | $903 | $813 |
| 2BR | $1,098 | $988 |
| **3BR** | **$1,553** | **$1,398** |
| 4BR | $1,810 | $1,629 |

⚠️ Market-derived — NOT property-specific. FMRs are 40th percentile gross rents; actual property-level rents vary by condition, block quality, and unit mix.

### Rent Estimates Used in This Report

- **3BR:** $1,398/mo → $16,776/yr (Parma-adjusted MSA FMR)
- **2BR:** $988/mo → $11,856/yr (Parma-adjusted MSA FMR)
- All rent figures flagged as ⚠️ estimates — not from property-level rent zestimates

---

## Buy Box Derivation (Under $190K Cap)

| Metric | Value |
|--------|-------|
| **Annual gross rent (3BR)** | $16,776 |
| **Target GRM** | 8–10 (Midwest working-class suburb) |
| **Target basis (GRM 8)** | ~$134,000 |
| **Stretch basis (GRM 10)** | ~$168,000 |
| **Target gross yield** | 10%–12.5% |
| **Cash buyer target** | GRM ≤ 8 (≈ $134K on 3BR) |
| **Financed target** | GRM ≤ 10 (≈ $168K on 3BR) |

### By Property Type

| Type | Parma Rent Est. | Target Basis (GRM 8) | Stretch Basis (GRM 10) | Gross Yield at $190K |
|------|----------------|----------------------|------------------------|------------------------|
| 1BR | $813/mo | ~$78,000 | ~$97,500 | 5.1% |
| 2BR | $988/mo | ~$95,000 | ~$118,500 | 6.2% |
| 3BR | $1,398/mo | ~$134,000 | ~$168,000 | 8.8% |
| 4BR | $1,629/mo | ~$156,000 | ~$195,000 | 10.3% |

**Key takeaway:** At the $190K cap, only 3BR properties approach viable gross yields. 1BR and 2BR at/near $190K are **pass** unless rents significantly exceed FMR estimates.

---

## 44129 — Parma West: Live Listings (sorted by price, lowest first)

**13 active listings under $190K.** Data pulled 2026-10-04 via Zillapi (saved JSON: `listings_44129.json`).

| # | Price | Address | Bd/Ba | Sqft | $/Sqft | DOM | Tax Gap | Yield | Verdict | Notes |
|---|-------|---------|-------|------|--------|-----|---------|-------|---------|-------|
| 1 | **$165,000** | 6006 Snow Rd, Cleveland | 3/2 | 1,188 | $139 | 8 | N/A | **10.2%** | ✅ **TAKE** | 2BA — rent premium potential. Best yield in set. |
| 2 | **$170,000** | 5814 Forest Ave, Parma | 3/1 | 1,092 | $156 | 1 | 14.4% | **9.9%** | ✅ **TAKE** | 1 DOM — very fresh. Two car garage. Best entry below stretch basis. |
| 3 | **$174,900** | 7611 Newport Ave, Parma | 3/1 | 1,092 | $160 | 10 | **32.8%** | **9.6%** | ⚠️ **NEGOTIATE** | ⚡ TAX GAP 33% — serious lender risk. Assessed at $117.5K vs ask $174.9K. |
| 4 | **$175,000** | 7514 Manhattan Ave, Parma | 3/1 | N/A | N/A | 0 | 25.9% | **9.6%** | ✅ **TAKE** | Listed today (0 DOM). Tax gap 26% — elevated but fresh listing has no leverage yet. |
| 5 | **$175,000** | 8324 Ivandale Dr, Parma | 3/1 | 1,272 | $138 | 36 | 15.2% | **9.6%** | ✅ **TAKE** | 🔥 Price cut $24,900 (was $199,900, cut 9/30). 36 DOM — motivated seller. Best $/sqft among 3BRs with data. |
| 6 | **$179,900** | 5903 Bradley Ave, Parma | 3/1 | 1,685 | $107 | 3 | 26.5% | **9.3%** | ⚠️ **NEGOTIATE** | Tax gap 27% — elevated. Good sqft value at $107/sqft. Detached garage. |
| 7 | **$180,000** | 7101 Brownfield Dr, Parma | 3/1 | 2,186 | **$82** | 18 | 13.1% | **9.3%** | ⚠️ **NEGOTIATE** | 🔥 Price cut $9,900 (was $189,900). 🏆 BEST SQFT VALUE: $82/sqft on 2,186 sqft. |
| 8 | $189,900 | 5821 Merkle Ave, Parma | 2/2 | 1,235 | $154 | 8 | 28.5% | **6.2%** | ❌ **PASS** | Only 2BR. At $190K, 2BR doesn't pencil in Parma (GRM 16). |
| 9 | $189,900 | 5597 W 54th St, Parma | 3/1 | 1,636 | $116 | 30 | 17.4% | **8.8%** | ⚠️ **NEGOTIATE** | 30 DOM — seller may be getting impatient. Fair sqft value. |
| 10 | $189,900 | 6040 W 54th St, Parma | 3/2 | 1,632 | $116 | 2 | 22.4% | **8.8%** | ⚠️ **NEGOTIATE** | 2 DOM — very fresh. 2BA premium. Tax gap 22% — elevated. |
| 11 | $189,900 | 6802 Ackley Rd, Parma | 3/2 | 1,244 | $153 | **72** | **9.3%** | **8.8%** | ⚡ **NEGOTIATE (priority)** | 🏆 Tax gap 9% — seller near floor. 72 DOM — very motivated. 2BA premium. |
| 12 | $189,900 | 8107 Dartworth Dr, Parma | 3/1 | 1,399 | $136 | 18 | 14.7% | **8.8%** | ⚠️ **NEGOTIATE** | Standard Parma 3/1. Fair metrics, no standout signal. |
| 13 | $190,000 | 6311 Thornton Dr, Parma | 3/2 | 1,176 | $162 | 45 | **8.1%** | **8.8%** | ⚡ **NEGOTIATE (priority)** | 🏆 Tax gap 8% — seller near floor. 45 DOM — motivated. 2BA premium. |

**Legend:** ✅ TAKE = attractive if diligence confirms | ⚠️ NEGOTIATE = interesting but only at better pricing/verified rents | ❌ PASS = doesn't fit strategy | ⚡ = priority negotiation target

### 44129 Summary Statistics

| Metric | Value |
|--------|-------|
| Count | 13 listings |
| Price range | $165,000 – $190,000 |
| Median price | $179,900 |
| Mean price | $181,492 |
| Median $/sqft | $138 |
| Median DOM | 10 days |
| Median gross yield (3BR) | 9.3% |
| Take | 4 listings |
| Negotiate | 8 listings |
| Pass | 1 listing |

---

## 44134 — Parma South

**⚠️ Blocked — no live data available.** Zillapi credits exhausted and Camofox IP captcha'd. This ZIP could not be pulled on 2026-10-04.

**Submarket profile (from prior thesis):** Value-add SFR zone. More entry-level price points, higher rehab likelihood, block-by-block variability. **Best chance at sub-$150K entries** in the Parma market.

**Direct URL (manual review):** https://www.zillow.com/homes/for_sale/44134_rb/1-_beds/0-190000_price/pricea_sort/

**Verdict (prior):** **Take selectively** — target GRM ≤ 10, verify block quality, budget for rehab.

---

## 44130 — Parma Heights / Middleburg Heights Fringe

**⚠️ Blocked — no live data available.** Zillapi credits exhausted and Camofox IP captcha'd. This ZIP could not be pulled on 2026-10-04.

**Submarket profile (from prior thesis):** Mixed area stretching into commercial corridors. Smaller housing stock on average. Less consistent block quality than 44129.

**Direct URL (manual review):** https://www.zillow.com/homes/for_sale/44130_rb/1-_beds/0-190000_price/pricea_sort/

**Verdict (prior):** **Negotiate** — verify block quality before bidding. Expect smaller sqft and more variability.

---

## Submarket Ranking (Parma Tri-ZIP)

| ZIP | Area | Investor Fit | Today's Verdict |
|-----|------|-------------|-----------------|
| **44129** | Parma West | Stabilized SFR hold; older housing stock (1940s-60s), decent block quality, strong rental demand, most data-rich ZIP | **Negotiate selectively** — 4 takes, 8 negotiates, 1 pass in today's screen |
| **44134** | Parma South | Value-add SFR; more entry-level price points, higher rehab likelihood, block-by-block variability | **Take selectively** — best chance at sub-$150K entries (⚠️ no live data today) |
| **44130** | Parma Hts / Midburg Hts fringe | Mixed; stretches into commercial corridors, smaller housing stock | **Negotiate** — verify block quality before bidding (⚠️ no live data today) |

---

## Buy Box by Property Type (from Today's 44129 Data)

### 3BR / 1BA — The Parma Standard

| Threshold | Value |
|-----------|-------|
| Target all-in basis | $165,000 – $175,000 |
| Stretch all-in basis | $180,000 |
| Target monthly rent | $1,398 (Parma-adj. FMR) |
| Target gross yield | 9.6% – 10.2% |
| Rehab tolerance | $15K max (cosmetic, systems only if discounted) |
| **Avoid if** | Tax gap > 30%, DOM > 90 days without price cut, block distress |

### 3BR / 2BA — Rent Premium Potential

| Threshold | Value |
|-----------|-------|
| Target all-in basis | $165,000 – $185,000 |
| Stretch all-in basis | $190,000 |
| Target monthly rent | $1,450 – $1,550 (2BA premium over FMR) |
| Target gross yield | 9.2% – 10.2% |
| Rehab tolerance | $10K max (2BA stock typically in better condition) |
| **Avoid if** | Tax gap > 25%, priced identically to 3/1 comps with no 2BA premium rationale |

### 2BR — Pass Zone at Current Pricing

| Threshold | Value |
|-----------|-------|
| Target all-in basis | < $120,000 |
| Stretch all-in basis | $130,000 |
| **At $189,900+** | **PASS** — GRM 16 at 2BR FMR of $988/mo. Does not pencil. |

---

## Direct Recommendations

### Best Current SFR Lead in 44129
**🥇 6006 Snow Rd — $165,000 (3/2, 1,188 sqft, 8 DOM)**
- Best gross yield in the set: **10.2%**
- 2BA configuration commands rent premium
- Lowest absolute price — most room for appreciation
- ⚡ Action: Verify condition, confirm rent comps, offer at $155K (GRM 9.2)

### Best Value Play (Forced Appreciation)
**🥇 8324 Ivandale Dr — $175,000 (3/1, 1,272 sqft, 36 DOM)**
- 🔥 Price cut $24,900 — seller acknowledged overpricing
- 36 DOM — motivated, negotiating leverage
- $138/sqft — good value for Parma
- ⚡ Action: Offer $160K (post-cut leverage), budget $10K cosmetic rehab, target $1,450 rent

### Best Negotiation Target (Motivated Seller)
**🥇 6802 Ackley Rd — $189,900 (3/2, 1,244 sqft, 72 DOM)**
- Tax gap only 9% — seller near assessed floor
- 72 DOM — strongest motivation signal in the set
- 2BA premium, decent block (Ackley corridor)
- ⚡ Action: Offer $170K, cite DOM. At $170K, gross yield jumps to 9.9%.

### Runner-Up Negotiation Target
**🥈 6311 Thornton Dr — $190,000 (3/2, 1,176 sqft, 45 DOM)**
- Tax gap 8% — tightest spread to assessed value
- 45 DOM — motivated, Berkshire Hathaway listing (professional seller)
- ⚡ Action: Offer $175K. At $175K, gross yield improves to 9.6%.

### Clear Pass
**❌ 5821 Merkle Ave — $189,900 (2/2, 1,235 sqft)**
- 2BR at $190K = GRM 16. Does not pencil in Parma at any reasonable rent estimate.
- Even at $1,200/mo (22% above FMR), gross yield only hits 7.6%.

### Best Overall Hold Submarket
**🏆 44129 (Parma West)** — most data, most consistent block quality, strongest rental demand, widest selection of 3BRs with viable yields.

### If You're Buying One Property Tomorrow
**6006 Snow Rd at $165K** — best yield, 2BA, lowest absolute basis. Verify condition and comp rents, then negotiate hard. At current ask, GRM is 9.8 — acceptable for financed buy-and-hold. At $155K, GRM drops to 9.2 — a clear take.

---

## ZIPs Without Data — Direct URLs

Open these in your own browser to see live listings:

| ZIP | Area | Direct Zillow URL |
|-----|------|-------------------|
| 44129 | Parma West | https://www.zillow.com/homes/for_sale/44129_rb/1-_beds/0-190000_price/pricea_sort/ |
| 44134 | Parma South | https://www.zillow.com/homes/for_sale/44134_rb/1-_beds/0-190000_price/pricea_sort/ |
| 44130 | Parma Hts / Midburg Hts | https://www.zillow.com/homes/for_sale/44130_rb/1-_beds/0-190000_price/pricea_sort/ |

---

## Action Items

1. **Top up Zillapi credits** at https://zillapi.com/app/billing — needed for 44134 and 44130 pulls
2. **Manual review** of 44134 and 44130 via direct Zillow URLs above
3. **Diligence priority:** 6006 Snow Rd, 8324 Ivandale Dr, 6802 Ackley Rd
4. **Re-run** when Zillapi credits are restored for full tri-ZIP coverage

---

*Report generated by Hermes Agent (Loki profile) — 2026-10-04*
*Rent anchors: U.S. HUD FY2025 Fair Market Rents, Cleveland-Elyria MSA, Parma adjustment (90%)*
*Raw data: /opt/data/outputs/2026-10-04/parma-listings-under-190k/listings_44129.json*