# Parma Listings Under $190K — Partial Pull
**Date:** 2026-09-24  
**Status:** ⚠️ PARTIAL — 9 of 56 results captured before Cloudflare captcha blocked Zillow  
**Data source:** Camofox browser → Zillow search results page (single successful load)  

---

## Status Summary

| Source | Result |
|--------|--------|
| Zillapi MCP | ❌ Out of credits |
| Camofox → Zillow combined bbox | ✅ 9 listings captured (first load) |
| Camofox → Zillow ZIP 44129 | ❌ Cloudflare "Press & Hold" captcha |
| Camofox → Zillow retry | ❌ Cloudflare "Press & Hold" captcha |
| SearXNG/agent_search | ⛔ Skipped (known Europe-return for "Parma,OH") |

**How to resume:** Wait for Zillapi credit refresh (next cycle) OR wait for Zillow session to cool down (captcha session timed out) and retry from Camofox. The combined bbox URL that worked once:  
`https://www.zillow.com/homes/for_sale/0-190000_price/0-5000_mp/41.35,-81.80,41.42,-81.65_rect/11_zm/`

---

## Market Context (Parma, OH)

Parma is the largest Cleveland suburb (~78K pop), predominantly C-to-B class working-class housing stock. Median home value ~$175K on Zillow ZHVI. Typical 3bd rent $1,100–$1,400/mo depending on condition and exact block. Strong rental demand from Cleveland workers priced out of closer-in neighborhoods.

**Rent estimates used below:** $1,200/mo for 3/1, $1,350/mo for 3/2, $1,000/mo for 2bd condo. These are conservative Cleveland-market comps (not Zillow rentZestimate — unavailable due to captcha).

---

## ZIP 44129 — Parma West (1 listing captured of unknown total)

| # | Address | Price | Beds | Baths | Sqft | Type | ZPID | URL | Est. Rent/mo | GRM | Gross Yield | Verdict |
|---|---------|-------|------|-------|------|------|------|-----|-------------|-----|------------|---------|
| 1 | 7611 Newport Ave | $174,900 | 3 | 1 | 1,092 | House | 33547825 | [zillow.com/homedetails/33547825_zpid](https://www.zillow.com/homedetails/33547825_zpid) | $1,200 | 12.1 | 8.2% | **negotiate** |

**44129 Verdict:** Only 1 listing captured. Newport Ave sits in the denser southern section of 44129 near Snow Rd. At $174,900 with 1,092 sqft, it's a compact ranch/colonial — the 3/1 layout limits rent upside. Negotiate toward $155-160K to get GRM under 11. **Risk: incomplete data — assume 3-6 more listings exist in this ZIP.**

---

## ZIP 44134 — Parma Central (3 listings captured)

| # | Address | Price | Beds | Baths | Sqft | Type | ZPID | URL | Est. Rent/mo | GRM | Gross Yield | Verdict |
|---|---------|-------|------|-------|------|------|------|-----|-------------|-----|------------|---------|
| 1 | 5565 Treetop Ct #132 | $159,900 | 2 | 3 | 1,674 | Condo | 33556015 | [zillow.com/homedetails/33556015_zpid](https://www.zillow.com/homedetails/33556015_zpid) | $1,100 | 12.1 | 8.3% | **pass** |
| 2 | 4431 Redfern Rd | $179,900 | 3 | 2 | 1,200 | House | 33560046 | [zillow.com/homedetails/33560046_zpid](https://www.zillow.com/homedetails/33560046_zpid) | $1,350 | 11.1 | 9.0% | **take selectively** |
| 3 | 3150 Jeanne Dr | $185,000 | 3 | 2 | — | House | 33567976 | [zillow.com/homedetails/33567976_zpid](https://www.zillow.com/homedetails/33567976_zpid) | $1,350 | 11.4 | 8.8% | **negotiate** |

**44134 Verdict:** Redfern Rd is the best house lead — 3/2 at $180K with 1,200 sqft and GRM of 11.1 is workable for a B-class Parma hold. Jeanne Dr has unknown sqft (red flag — likely a flip with detail stripped). Treetop Ct condo is a pass: HOA fees unknown, condo financing hurdles, weak yield for a condo. **Risk: incomplete — estimate 4-8 more listings in 44134.**

---

## ZIP 44130 — Parma Heights / SW Parma (4 listings captured)

| # | Address | Price | Beds | Baths | Sqft | Type | ZPID | URL | Est. Rent/mo | GRM | Gross Yield | Verdict |
|---|---------|-------|------|-------|------|------|------|-----|-------------|-----|------------|---------|
| 1 | 10366 Manorford Dr, Cleveland | $119,900 | 2 | 1 | 928 | Condo | 457454693 | [zillow.com/homedetails/457454693_zpid](https://www.zillow.com/homedetails/457454693_zpid) | $1,000 | 10.0 | 10.0% | **negotiate** |
| 2 | 6331 Alderwood Rd, Parma Heights | $173,000 | 3 | 1 | 1,218 | House | 33578008 | [zillow.com/homedetails/33578008_zpid](https://www.zillow.com/homedetails/33578008_zpid) | $1,200 | 12.0 | 8.3% | **negotiate** |
| 3 | 11255 Bobko Blvd, Parma | $189,900 | 3 | 2 | — | House | 33575371 | [zillow.com/homedetails/33575371_zpid](https://www.zillow.com/homedetails/33575371_zpid) | $1,350 | 11.7 | 8.5% | **negotiate** |
| 4 | 11700 Glamer Dr, Parma | $189,900 | 3 | 2 | 1,596 | House | 33575682 | [zillow.com/homedetails/33575682_zpid](https://www.zillow.com/homedetails/33575682_zpid) | $1,350 | 11.7 | 8.5% | **negotiate** |

**44130 Verdict:** Manorford Dr condo has the best GRM (10.0) but is a 2/1 condo in the Cleveland section of 44130 — HOA fees are the make-or-break. Glamer Dr (1,596 sqft, brick exterior, 3/2) is the strongest house lead if rent can be pushed to $1,375+. Alderwood at $173K is fine at $155-160K. Bobko Blvd unknown sqft is a caution flag. **Risk: incomplete — estimate 5-10 more listings in 44130.**

---

## Outside Target ZIPs (excluded but noted)

| Address | Price | ZIP | Type | Note |
|---------|-------|-----|------|------|
| 6334 W 130th St, Brookpark | $139,900 | 44142 | House | Price cut $10,100 on 9/1; outside scope |

---

## Buy Box → Actionable Thresholds

Using observed listings and Parma comps:

| Property Type | Target Basis | Stretch Basis | Target Rent | Target GRM | Preferred ZIPs |
|---------------|-------------|---------------|-------------|------------|----------------|
| 3/1 SFR | ≤$160K | ≤$175K | $1,200 | ≤11.0 | 44129, 44130 |
| 3/2 SFR | ≤$175K | ≤$190K | $1,350 | ≤11.5 | 44134, 44130 |
| 2bd Condo | ≤$110K | ≤$130K | $1,000 | ≤10.0 | 44130 (only if HOA <$250) |

---

## Direct Recommendations

| Category | Pick | Rationale |
|----------|------|-----------|
| **Best SFR lead** | 4431 Redfern Rd, 44134 ($179,900) | Best GRM among houses (11.1), 3/2 layout, verified sqft |
| **Best value lead** | 10366 Manorford Dr, 44130 ($119,900) | Lowest price, GRM 10.0 — but verify HOA before pursuing |
| **Best overall ZIP** | 44134 | Most listings found, best GRM profile |
| **Avoid** | 5565 Treetop Ct #132, 44134 | Condo with weak yield + unknown HOA burden |

---

## ⚠️ Critical Caveats

1. **This is a partial pull.** 47 of 56 results in the bounding box were not captured. The missing listings may include better deals in 44129 and lower-priced entries in 44134.
2. **Rent estimates are market comps, not verified.** Without Zillow rentZestimate access (captcha-blocked individual property pages), these are conservative Parma-market estimates.
3. **No days-on-market data captured.** Zillow search cards didn't expose DOM data for this via the extraction script.
4. **No property condition assessments.** Without individual property page access, rehab cost estimates are unavailable.
5. **Full pull needed for confident ranking.** Resume when Zillapi credits refresh or Zillow session cools down.

**Zillow direct search link (open in your browser):**  
[https://www.zillow.com/homes/for_sale/0-190000_price/41.35,-81.80,41.42,-81.65_rect/11_zm/](https://www.zillow.com/homes/for_sale/0-190000_price/41.35,-81.80,41.42,-81.65_rect/11_zm/)