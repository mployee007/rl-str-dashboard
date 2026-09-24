# Parma Under-$190K Listing Screen — 2026-09-24

## Bottom Line

Three properties surfaced from the target ZIPs (44129, 44134, 44130) via a single Camofox Zillow browser pull at ≤$190K. ZIP **44129 returned zero listings** in the rendered DOM sample (9 of 1,161 results pages). ZIPs **44130 and 44134** each had 1–2 listings, all 3bd/2ba SFRs at $185K–$190K. At Cleveland-Elyria MSA 3bd FMR of **$1,553/mo**, these yield GRMs of 9.9–10.5 (gross yields ~9.5–10.1%) — **negotiate territory**. None are automatic buys at this price when sqft is unknown for 2 of 3 listings.

> ⚠️ **DATA LIMITATION**: Zillapi was out of credits. Camofox loaded Zillow once successfully but rendered only 9 of 1,161 listings due to DOM virtualization. Rent estimates are MSA-level FY2025 FMR (40th percentile) — not property-specific. Actual property-level rent zestimates and tax data were unavailable. Treat these as first-pass screens; diligence requires individual property visits and verified rent comps.

---

## Source Status

| Source | Status | Details |
|---|---|---|
| Zillapi MCP | ❌ Out of credits | "Out of credits for this cycle" — all 3 bbox calls failed |
| Camofox → Zillow | ✅ Partial | 1,161 results reported; 9 cards rendered; 3 in target ZIPs |
| rentdata.org (FMR) | ✅ | Cleveland-Elyria MSA FY2025 FMR retrieved |
| SearXNG search | ❌ Wrong locale | Returned Parma, Italy results |
| web_search | ❌ firecrawl missing | `security.allow_lazy_installs=false` |

---

## 1. Ranked Submarket Summary

| ZIP | Neighborhood | Listings Found | Median Ask | Investor Fit | Verdict |
|---|---|---|---|---|---|
| **44130** | Middleburg Hts / SW Parma | 2 | $189,900 | Value-add SFR | **Negotiate** |
| **44134** | Parma (SE) | 1 | $185,000 | Value-add SFR | **Negotiate** |
| **44129** | Parma (West) | 0 | — | Unknown — need more data | **Insufficient data** |

---

## 2. Live Listing Screen

### ZIP 44130

| # | Address | Price | Beds | Baths | Sqft | Type | zpID | Zillow URL | Est. Rent (FMR) | GRM | Gross Yield | Notes | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 11700 Glamer Dr, Parma, OH 44130 | $189,900 | 3 | 2 | 1,596 | House | 33575682 | [link](https://www.zillow.com/homedetails/11700-Glamer-Dr-Parma-OH-44130/33575682_zpid/) | $1,553 | 10.19 | 9.8% | Brick exterior, known sqft. Most complete of the three. | **Take selectively** |
| 2 | 11255 Bobko Blvd, Parma, OH 44130 | $189,900 | 3 | 2 | -- | House | 33575371 | [link](https://www.zillow.com/homedetails/11255-Bobko-Blvd-Parma-OH-44130/33575371_zpid/) | $1,553 | 10.19 | 9.8% | Detached 2-car garage. Missing sqft — red flag. | **Negotiate** |

### ZIP 44134

| # | Address | Price | Beds | Baths | Sqft | Type | zpID | Zillow URL | Est. Rent (FMR) | GRM | Gross Yield | Notes | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | 3150 Jeanne Dr, Parma, OH 44134 | $185,000 | 3 | 2 | -- | House | 33567976 | [link](https://www.zillow.com/homedetails/3150-Jeanne-Dr-Parma-OH-44134/33567976_zpid/) | $1,553 | 9.93 | 10.1% | Partially fenced yard. Lowest price in sample. Missing sqft — red flag. | **Negotiate** |

### ZIP 44129

**No listings found.** Zero properties ≤$190K from the rendered DOM sample. This ZIP may have:
- Very few active listings at this price point
- Listings below the fold (not rendered in the first 9 of 1,161)
- Properties that sold quickly

Recommendation: monitor ZIP 44129 separately or expand the price ceiling slightly for this ZIP.

---

## 3. Acquisition Buy Box

Rent anchor: Cleveland-Elyria MSA FY2025 3bd FMR = **$1,553/mo** (40th percentile). For Parma 3bd SFRs, assume $1,450–$1,600/mo market rent depending on condition and block.

### 3-Bedroom SFR Buy Box (Parma)

| Parameter | Target | Stretch | Notes |
|---|---|---|---|
| **Max all-in basis** | $170,000 | $190,000 | Above $190K: GRM exceeds 11 at $1,450/mo |
| **Target monthly rent** | $1,500+ | $1,400 | Verified rent comps required |
| **Target GRM** | ≤10 | ≤12 | Current listings at 9.9–10.2 |
| **Target gross yield** | ≥10% | ≥8.5% | At FMR, current listings yield 9.8–10.1% |
| **Rehab budget** | ≤$15K | ≤$25K | Brick exteriors (Glamer Dr) typically lower maintenance |
| **Preferred ZIPs** | 44130, 44134 | 44129 | 44129 needs more data |

### Avoid conditions
- Missing square footage that can't be explained (2 of 3 listings have this issue)
- No garage in Cleveland winters
- Blocks bordering industrial/commercial zones
- Properties that need roof/HVAC/foundation work exceeding the rehab budget

---

## 4. Final Direct Verdicts

| Category | Pick | Detail |
|---|---|---|
| **Best single lead** | 11700 Glamer Dr, 44130 | $189.9K, 3/2, 1,596 sqft, brick. Only listing with known sqft. GRM 10.2 at FMR. |
| **Best value lead** | 3150 Jeanne Dr, 44134 | $185K — lowest ask. Needs sqft verified. GRM 9.9 if rents check out. |
| **Best submarket** | 44130 | Most listings, diverse inventory, Middleburg Hts has decent tenant profile. |
| **Data gap** | 44129 | Zero listings surfaced. Expand search or widen price band for this ZIP. |

### If buying one property tomorrow:
**11700 Glamer Dr** at $189.9K is the strongest lead — brick exterior, known square footage, and price in the target band. Offer $175K and verify actual rent comps before proceeding. If rent clears $1,500/mo, this pencils at a 10+% gross yield.

---

## 5. Raw Data Files

| File | Description |
|---|---|
| `parma-listings.md` | This report |
| `/opt/data/parma-latest-listings.md` | Quick-reference listing table only |
| `/opt/data/parma-pull-status.txt` | Pull status log |

*Raw JSON: not saved separately due to small sample size (3 properties) — all data embedded above.*

---

*Generated: 2026-09-24 | Sources: Camofox → Zillow (partial), rentdata.org (Cleveland-Elyria MSA FY2025 FMR) | Zillapi: OUT OF CREDITS | SearXNG: European namesake interference*