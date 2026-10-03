# Parma West Area Listings — Under $190K

**Run date:** 2026-10-03 UTC  
**Status:** ⛔ BLOCKED — All data sources exhausted (same as 10/02)  
**Target ZIPs:** 44129 (Parma West), 44134 (Parma South), 44130 (Parma Hts / Middleburg)  
**Price cap:** $190,000  
**Property type:** For-sale houses, 1+ bedrooms  

---

## Source Attempts

| Source | Result |
|--------|--------|
| **Zillapi** (`mcp_zillapi_search_listings`) | ❌ **Out of credits.** 44129 returned clean error. 44134/44130 hit MCP server unreachable (57 consecutive failures). |
| **Camofox → Zillow** (`browser_navigate` → 44129) | ❌ **Cloudflare "Press & Hold" captcha.** Reference ID `794a0758-bed7-11f1-aaf5-494ef97db904`. Page title: "Access to this page has been denied". IP rate-limited. |
| **Rentdata.org** | ❌ Known unreliable — MSA URLs 404, agent_search falls through to Wikipedia. |
| **SearXNG / agent_search** | ❌ Not viable — Parma OH resolves to Parma, Italy regardless of qualifiers. |
| **web_search / web_extract** | ❌ firecrawl not installable in cron (locked venv, os error 13). |

---

## Rent Baselines

Cleveland-Elyria MSA FY2025 HUD Fair Market Rents (40th percentile gross):

| Unit | MSA FMR | Parma Adj (90%) |
|------|---------|-----------------|
| 1BR | $903 | $813 |
| 2BR | $1,098 | **$988** |
| 3BR | $1,553 | **$1,398** |
| 4BR | $1,810 | $1,629 |

⚠️ All rent figures are market-derived — NOT property-specific.

---

## Most Recent Available Data: 44129 (from 2026-10-02 pull — 1 day stale)

The table below reflects the **last successful pull** on 2026-10-02. Listings may have gone pending, sold, or changed price since then. Treat this as a directional reference only.

| # | Address | Price | Beds | Baths | Sqft | $/Sqft | DOM | Tax Assessed | Tax Gap | Est. Rent/mo | Est. Yield | GRM | Verdict |
|---|---------|-------|------|-------|------|--------|-----|-------------|---------|-------------|-----------|-----|---------|
| 1 | [6006 Snow Rd, Cleveland](https://www.zillow.com/homedetails/6006-Snow-Rd-Cleveland-OH-44129/2057037610_zpid/) | $165,000 | 3 | 2 | 1,188 | $139 | 6 | — | — | $1,398 | 10.2% | 9.8 | **TAKE** |
| 2 | [7611 Newport Ave, Parma](https://www.zillow.com/homedetails/7611-Newport-Ave-Parma-OH-44129/33547825_zpid/) | $174,900 | 3 | 1 | 1,092 | $160 | 8 | $117,500 | 32.8% | $1,398 | 9.6% | 10.4 | **NEGOTIATE** |
| 3 | [8324 Ivandale Dr, Parma](https://www.zillow.com/homedetails/8324-Ivandale-Dr-Parma-OH-44129/33564869_zpid/) | $175,000 | 3 | 1 | 1,272 | $138 | 34 | $148,400 | 15.2% | $1,398 | 9.6% | 10.4 | **NEGOTIATE** |
| 4 | [5903 Bradley Ave, Parma](https://www.zillow.com/homedetails/5903-Bradley-Ave-Parma-OH-44129/33551238_zpid/) | $179,900 | 3 | 1 | 1,685 | $107 | 1 | $132,200 | 26.5% | $1,398 | 9.3% | 10.7 | **NEGOTIATE** |
| 5 | [7101 Brownfield Dr, Parma](https://www.zillow.com/homedetails/7101-Brownfield-Dr-Parma-OH-44129/33561440_zpid/) | $180,000 | 3 | 1 | 2,186 | $82 | 15 | $156,500 | 13.1% | $1,398 | 9.3% | 10.7 | **NEGOTIATE** |
| 6 | [5821 Merkle Ave, Parma](https://www.zillow.com/homedetails/5821-Merkle-Ave-Parma-OH-44129/33551587_zpid/) | $189,900 | 2 | 2 | 1,235 | $154 | 6 | $135,800 | 28.5% | $988 | 6.2% | 16.0 | **PASS** |
| 7 | [5597 W 54th St, Parma](https://www.zillow.com/homedetails/5597-W-54th-St-Parma-OH-44129/33553876_zpid/) | $189,900 | 3 | 1 | 1,636 | $116 | 28 | $156,900 | 17.4% | $1,398 | 8.8% | 11.3 | **NEGOTIATE** |
| 8 | [6040 W 54th St, Parma](https://www.zillow.com/homedetails/6040-W-54th-St-Parma-OH-44129/33561761_zpid/) | $189,900 | 3 | 2 | 1,632 | $116 | 1 | $147,400 | 22.4% | $1,398 | 8.8% | 11.3 | **NEGOTIATE** |
| 9 | [6802 Ackley Rd, Parma](https://www.zillow.com/homedetails/6802-Ackley-Rd-Parma-OH-44129/33561977_zpid/) | $189,900 | 3 | 2 | 1,244 | $153 | 70 | $172,200 | 9.3% | $1,398 | 8.8% | 11.3 | **NEGOTIATE** |
| 10 | [8107 Dartworth Dr, Parma](https://www.zillow.com/homedetails/8107-Dartworth-Dr-Parma-OH-44129/33563840_zpid/) | $189,900 | 3 | 1 | 1,399 | $136 | 16 | $162,000 | 14.7% | $1,398 | 8.8% | 11.3 | **NEGOTIATE** |
| 11 | [6311 Thornton Dr, Parma](https://www.zillow.com/homedetails/6311-Thornton-Dr-Parma-OH-44129/33562283_zpid/) | $190,000 | 3 | 2 | 1,176 | $162 | 43 | $174,700 | 8.1% | $1,398 | 8.8% | 11.3 | **NEGOTIATE** |

**⚠️ CAVEAT: 1-day stale.** 6006 Snow Rd (the #1 TAKE) was 6 DOM on 10/02 — likely 7 DOM now. 5903 Bradley Ave and 6040 W 54th were 1 DOM — now 2 DOM. Verify all before acting.

---

## Tax Gap Analysis (10/02 data)

| Address | Ask | Tax Assessed | Gap % | Flag |
|---------|-----|-------------|-------|------|
| 6311 Thornton Dr | $190,000 | $174,700 | 8.1% | ✅ Tight — seller aligned with county |
| 6802 Ackley Rd | $189,900 | $172,200 | 9.3% | ✅ Tight |
| 7101 Brownfield Dr | $180,000 | $156,500 | 13.1% | ✅ Reasonable |
| 8107 Dartworth Dr | $189,900 | $162,000 | 14.7% | ✅ Reasonable |
| 8324 Ivandale Dr | $175,000 | $148,400 | 15.2% | ✅ Reasonable |
| 5597 W 54th St | $189,900 | $156,900 | 17.4% | ⚠️ Moderate |
| 6040 W 54th St | $189,900 | $147,400 | 22.4% | ⚠️ Moderate |
| 5903 Bradley Ave | $179,900 | $132,200 | 26.5% | 🔴 Large gap |
| 5821 Merkle Ave | $189,900 | $135,800 | 28.5% | 🔴 Large gap |
| 7611 Newport Ave | $174,900 | $117,500 | 32.8% | 🔴 Largest gap |

---

## Buy Box — 44129 Single-Family

| Parameter | Target | Stretch |
|-----------|--------|---------|
| **ZIPs** | 44129 | 44134, 44130 (data pending) |
| **Bedrooms** | 3+ | 2 (only if price < $160K) |
| **All-in basis** | ≤ $170,000 | ≤ $185,000 |
| **Target monthly rent** | ≥ $1,398 (3BR) | ≥ $988 (2BR) |
| **Target gross yield** | ≥ 9.5% | ≥ 8.5% |
| **Target GRM** | ≤ 10.5 | ≤ 11.8 |
| **Rehab tolerance** | ≤ $25K (cosmetic) | ≤ $40K (systems) |
| **Tax gap ceiling** | ≤ 20% | ≤ 25% |
| **Avoid** | 2BR above $170K, tax gap >30%, major foundation/roof issues |

---

## 44134 & 44130 Status

| ZIP | Status | Manual URL |
|-----|--------|-----------|
| 44134 | ❌ Never pulled — captcha-blocked on every attempt | [Zillow 44134](https://www.zillow.com/homes/for_sale/44134_rb/1-_beds/0-190000_price/pricea_sort/) |
| 44130 | ❌ Never pulled — captcha-blocked on every attempt | [Zillow 44130](https://www.zillow.com/homes/for_sale/44130_rb/1-_beds/0-190000_price/pricea_sort/) |

These ZIPs have never been successfully pulled by this pipeline. Parma South (44134) and Parma Hts/Middleburg (44130) are both working-class suburbs with similar rent profiles to 44129 — FMR anchors and buy box thresholds are identical.

---

## Direct Recommendations (from 10/02 data)

**🏆 Best SFR lead (buy today):**  
**[6006 Snow Rd](https://www.zillow.com/homedetails/6006-Snow-Rd-Cleveland-OH-44129/2057037610_zpid/)** — $165,000, 3bd/2ba, 1,188 sqft. 10.2% estimated yield, GRM 9.8. 3 DOM as of 10/02. If still active and condition passes inspection, this is the best cash-flow entry in 44129 sub-$190K. ⚠️ Verify it hasn't gone pending.

**🔨 Best value-add candidate:**  
**[7101 Brownfield Dr](https://www.zillow.com/homedetails/7101-Brownfield-Dr-Parma-OH-44129/33561440_zpid/)** — $180,000, 3bd/1ba, 2,186 sqft. $82/sqft is deepest value in the pool. 13.1% tax gap = reasonable. Already reduced $9,900 (9/26). 15 DOM as of 10/02.

**🛑 Avoid:**  
- **5821 Merkle Ave** — 2BR at $190K, 6.2% yield, 28.5% tax gap. Triple fail.
- **Any 2BR above $170K** — Parma 2BR rents (~$988) can't service the debt.

**📋 44134 / 44130:** Open the manual Zillow links above. If you find anything, reply with the address list and I'll score them against the same buy box.

---

## Resolution

To unblock the automated pipeline:
1. **Top up Zillapi credits** at https://zillapi.com/app/billing
2. **Change the IP** for Camofox (VPN, proxy rotation, or wait for Cloudflare rate limit to expire)
3. Or **manually pull** from the Zillow links above and paste listing data — I'll format it

The pipeline infrastructure is intact — just needs a working data window.