# Parma Area Listings Screen — Under $190K

**Date:** 2026-10-04 (automated cron)  
**Target ZIPs:** 44129, 44134, 44130  
**Status:** ⚠️ PARTIAL — 44129 from stale cache; 44134/44130 no data

---

## Data Source Status

| # | Source | Target | Result |
|---|--------|--------|--------|
| 1 | Zillapi MCP | 44129 | ❌ **Out of credits** — "Top up or upgrade at zillapi.com/app/billing" |
| 2 | Zillapi MCP | 44134 | ❌ MCP unreachable — 65 consecutive failures after credit exhaustion |
| 3 | Zillapi MCP | 44130 | ❌ MCP unreachable — 65 consecutive failures after credit exhaustion |
| 4 | Camofox → Zillow | 44129 | ❌ **Captcha blocked** — Cloudflare "Press & Hold" (ref: df7d4e6a-bfd5-11f1-8372-0197d4f99c22) |
| 5 | Cached JSON | 44129 | ⚠️ **Stale** — last successful pull data; DOM values 0-3 days old |
| 6 | Cached JSON | 44134 | ❌ No prior data available |
| 7 | Cached JSON | 44130 | ❌ No prior data available |

**All live-data paths exhausted.** The 44129 table below is from the most recent successful pull. DOM counters may be off by 1-3 days. 44134 and 44130 have no cached data.

---

## Market Context: Cleveland-Elyria MSA → Parma Submarket

### Rent Anchors (FY2025 HUD Fair Market Rents — 40th percentile gross rent)

Parma adjustment: **90% of Cleveland-Elyria MSA** (working-class suburb discount).

| Unit | MSA FMR | Parma Est. (90%) | Annual |
|------|---------|-------------------|--------|
| Studio | $824 | $742 | $8,904 |
| 1BR | $903 | $813 | $9,756 |
| 2BR | $1,098 | $988 | $11,856 |
| **3BR** | **$1,553** | **$1,398** | **$16,776** |
| 4BR | $1,810 | $1,629 | $19,548 |

⚠️ Market-derived — NOT property-specific. Source: HUD FY2025 FMR.

### Buy Box Derivation ($190K Cap)

| Metric | Value |
|--------|-------|
| Target gross yield | 10%+ (cash buyer), 8%+ (financed) |
| Target GRM | ≤10 (cash), ≤12.5 (financed) |
| Basis ceiling (3BR @ $1,398/mo) | $168K (GRM 10), $134K (GRM 8) |
| Basis ceiling (2BR @ $988/mo) | $119K (GRM 10), $95K (GRM 8) |

**At $190K cap:** 3BR properties pencil at 8.8%+ gross yield — cash-flow positive but tight on a 75% LTV conventional loan. 2BR properties at $180K+ cannot pencil with Parma rents.

---

## 44129 — Parma West: Cached Listings ⚠️ STALE

**Source:** Prior Camofox `__NEXT_DATA__` extraction. DOM values may be 0-3 days stale.  
**Direct Zillow URL (live):** https://www.zillow.com/homes/for_sale/44129_rb/1-_beds/0-190000_price/pricea_sort/

| # | Address | Price | Beds | Baths | Sqft | $/Sqft | DOM | Notes | Est. Rent/yr | Gross Yield | Tax Gap | Verdict |
|---|---------|-------|------|-------|------|--------|-----|-------|-------------|-------------|---------|---------|
| 1 | 6006 Snow Rd, Cleveland | $165,000 | 3 | 2 | 1,188 | $139 | 8 | 2BA — rent premium | $16,776 | 10.2% | N/A | **TAKE** |
| 2 | 5814 Forest Ave, Parma | $170,000 | 3 | 1 | 1,092 | $156 | 1 | Two car garage; listed fresh | $16,776 | 9.9% | 14% | **TAKE** |
| 3 | 7611 Newport Ave, Parma | $174,900 | 3 | 1 | 1,092 | $160 | 10 | — | $16,776 | 9.6% | 33% ⚠️ | **NEGOTIATE** |
| 4 | 7514 Manhattan Ave, Parma | $175,000 | 3 | 1 | N/A | N/A | 0 | Listed day-of; no sqft data | $16,776 | 9.6% | 26% | **TAKE** |
| 5 | 8324 Ivandale Dr, Parma | $175,000 | 3 | 1 | 1,272 | $138 | 36 | 🔻 Price cut $24,900 (was $199,900) | $16,776 | 9.6% | 15% | **TAKE** |
| 6 | 5903 Bradley Ave, Parma | $179,900 | 3 | 1 | 1,685 | $107 | 3 | Detached garage | $16,776 | 9.3% | 27% ⚠️ | **NEGOTIATE** |
| 7 | 7101 Brownfield Dr, Parma | $180,000 | 3 | 1 | 2,186 | $82 | 18 | 🔻 Price cut $9,900; **BEST $/SQFT** | $16,776 | 9.3% | 13% | **NEGOTIATE** |
| 8 | 5821 Merkle Ave, Parma | $189,900 | 2 | 2 | 1,235 | $154 | 8 | 2BR — doesn't pencil at this price | $11,856 | 6.2% | 28% ⚠️ | **PASS** |
| 9 | 5597 W 54th St, Parma | $189,900 | 3 | 1 | 1,636 | $116 | 30 | Stale — 30 DOM | $16,776 | 8.8% | 17% | **NEGOTIATE** |
| 10 | 6040 W 54th St, Parma | $189,900 | 3 | 2 | 1,632 | $116 | 2 | 2BA — rent premium; fresh listing | $16,776 | 8.8% | 22% ⚠️ | **NEGOTIATE** |
| 11 | 6802 Ackley Rd, Parma | $189,900 | 3 | 2 | 1,244 | $153 | 72 | 2BA; 72 DOM — motivated seller | $16,776 | 8.8% | 9% ✓ | **NEGOTIATE ⚡** |
| 12 | 8107 Dartworth Dr, Parma | $189,900 | 3 | 1 | 1,399 | $136 | 18 | — | $16,776 | 8.8% | 15% | **NEGOTIATE** |
| 13 | 6311 Thornton Dr, Parma | $190,000 | 3 | 2 | 1,176 | $162 | 45 | 2BA; 45 DOM — motivated seller | $16,776 | 8.8% | 8% ✓ | **NEGOTIATE ⚡** |

### 44129 Verdict Summary

| Verdict | Count | Properties |
|---------|-------|------------|
| **TAKE** | 4 | #1 Snow Rd, #2 Forest Ave, #4 Manhattan Ave, #5 Ivandale Dr |
| **NEGOTIATE** | 7 | #3 Newport Ave, #6 Bradley Ave, #7 Brownfield Dr, #9 W 54th, #10 W 54th, #11 Ackley Rd, #12 Dartworth Dr, #13 Thornton Dr |
| **NEGOTIATE ⚡** | 2 | #11 Ackley Rd (72 DOM, 9% tax gap), #13 Thornton Dr (45 DOM, 8% tax gap) |
| **PASS** | 1 | #8 Merkle Ave (2BR at $190K — 6.2% yield, can't pencil) |

**Best SFR lead:** #5 Ivandale Dr — $175K, motivated seller ($24.9K cut), 36 DOM, 15% tax gap, $138/sqft.  
**Best cash-flow lead:** #1 Snow Rd — $165K, 10.2% gross yield, 2BA.  
**Best forced-appreciation:** #11 Ackley Rd — 72 DOM, 9% tax gap, 2BA. Offer $170K (GRM 10.1, 9.9% yield).

---

## 44134 — Parma South

**Status:** ❌ No data — Zillapi out of credits, Camofox captcha-blocked, no cached JSON.  
**Direct Zillow URL (live):** https://www.zillow.com/homes/for_sale/44134_rb/1-_beds/0-190000_price/pricea_sort/

### Submarket Profile (from prior sessions)

| Attribute | Assessment |
|-----------|------------|
| **Investor fit** | Value-add SFR; more entry-level price points, higher rehab likelihood |
| **Block quality** | Block-by-block variability — must inspect |
| **Price expectation** | Best chance at sub-$150K entries in the Parma cluster |
| **Verdict** | **Take selectively** — screen for block quality, verify rehab scope |

---

## 44130 — Parma Heights / Middleburg Heights Fringe

**Status:** ❌ No data — Zillapi out of credits, Camofox captcha-blocked, no cached JSON.  
**Direct Zillow URL (live):** https://www.zillow.com/homes/for_sale/44130_rb/1-_beds/0-190000_price/pricea_sort/

### Submarket Profile (from prior sessions)

| Attribute | Assessment |
|-----------|------------|
| **Investor fit** | Mixed; stretches into more commercial corridors, smaller housing stock |
| **Block quality** | Verify block quality before bidding |
| **Price expectation** | Similar to 44129 but smaller average sqft |
| **Verdict** | **Negotiate** — verify block quality before bidding |

---

## Cross-ZIP Comparison

| ZIP | Neighborhood | Best Investor Fit | Live Data? | Verdict |
|-----|-------------|-------------------|------------|---------|
| **44129** | Parma West | Stabilized SFR hold; 10% yields at $165-175K | ⚠️ Stale cache (13 props) | **Take selectively** |
| **44134** | Parma South | Value-add SFR; sub-$150K entries | ❌ None | **Take selectively** — inspect blocks |
| **44130** | Parma Hts / Midburg Hts | Mixed; smaller stock, commercial fringe | ❌ None | **Negotiate** — verify condition |

---

## Direct Zillow URLs (open in your browser)

| ZIP | URL (sorted by price, lowest first, ≤$190K) |
|-----|------|
| **44129** | https://www.zillow.com/homes/for_sale/44129_rb/1-_beds/0-190000_price/pricea_sort/ |
| **44134** | https://www.zillow.com/homes/for_sale/44134_rb/1-_beds/0-190000_price/pricea_sort/ |
| **44130** | https://www.zillow.com/homes/for_sale/44130_rb/1-_beds/0-190000_price/pricea_sort/ |

---

## Resolution

| Action | Expected Outcome |
|--------|------------------|
| Top up Zillapi credits | All 3 ZIPs pullable in one batch; credits restore instantly |
| Wait 24h for IP captcha cooldown | Camofox first navigation works again |
| Open URLs above in browser | Instant access to live listings from any IP |

**Preference:** Zillapi top-up is the fastest path — credits restore instantly, and all three ZIPs can be pulled in one shot.

---

*Status file: `/opt/data/parma-pull-status.txt`*  
*Cached 44129 data: `/opt/data/outputs/2026-10-04/parma-listings-under-190k/listings_44129.json`*