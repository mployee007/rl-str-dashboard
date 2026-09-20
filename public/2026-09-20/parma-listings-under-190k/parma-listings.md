# Parma West Submarket: Live Listing Screen (Under $190K)

**Generated:** 2026-09-20 (cron run)
**Status:** ⚠️ Partial — ZIP-level aggregates only (Zillapi out of credits for live listing pull)
**Data source:** `cleveland_zip_stats.json` (prior pull aggregates)

---

## Bottom Line

**44129 (Parma West) is the yield leader** in the Parma cluster at 12.3% gross yield and an 8.1× price-to-rent ratio. However, its median sale of $190K sits right at the $190K cap — expect inventory below this threshold to be older/smaller stock. **44134** offers more volume (44 active sales) but at a thinner 10.0% yield with median $200K. **44130** is the smallest pool (7 sales) and weakest yield at 9.5%.

⚠️ **No individual property data is available** because Zillapi credits are exhausted. The tables below use ZIP-level aggregates. Live listing screens with addresses, zpids, beds/baths/sqft, and per-property verdicts will populate on the next successful crawl.

---

## 1) Ranked ZIP / Submarket Table

| ZIP | Neighborhood | Active Sales | Median Sale | Median Rent | Gross Yield | P/R Ratio | Investor Fit | Verdict |
|-----|-------------|-------------|-------------|-------------|-------------|-----------|-------------|---------|
| **44129** | Parma (W) | 16 | $190,000 | $1,950 | 12.32% | 8.1× | Stabilized SFR hold — yield leader in Parma cluster | **Take selectively** (if under $190K) |
| **44134** | Parma (E), Brooklyn Hts, Seven Hills | 44 | $200,000 | $1,675 | 10.05% | 10.0× | Value-add SFR — highest volume, but median above $190K cap | **Negotiate** (need below-median basis) |
| **44130** | Parma (mid) | 7 | $199,900 | $1,575 | 9.45% | 10.6× | Low inventory, weakest yield — limited opportunity set | **Pass** (unless outlier deal) |

---

## 2) Direct Zillow Search URLs

Open these in your browser to see live listings under $190K:

| ZIP | Direct Zillow Search |
|-----|---------------------|
| 44129 | https://www.zillow.com/homes/for_sale/44129_rb/0-190000_price/ |
| 44134 | https://www.zillow.com/homes/for_sale/44134_rb/0-190000_price/ |
| 44130 | https://www.zillow.com/homes/for_sale/44130_rb/0-190000_price/ |

---

## 3) Buy Box by Property Type (First Pass)

Using ZIP 44129 as the anchor (best yield), with $1,950 median rent:

| Property Type | Target Basis | Stretch Basis | Target Rent (mo) | Target Gross Yield | Rehab Tolerance | Avoid |
|--------------|-------------|---------------|-------------------|-------------------|-----------------|-------|
| 2-BR SFR | ≤ $160K | $175K | $1,500–$1,700 | 11.3%–12.8% | ≤ $20K | Foundation issues, knob & tube |
| 3-BR SFR | ≤ $175K | $190K | $1,700–$2,000 | 11.7%–13.7% | ≤ $25K | Major systems (roof/HVAC/plumbing stack) |
| Duplex | ≤ $170K/unit | $190K/unit | $1,200–$1,400/unit | 8.5%–9.9%/unit | ≤ $15K/unit | Shared utilities not separately metered |

---

## 4) Recommendations

| Category | Pick | Rationale |
|----------|------|-----------|
| **Best yield submarket** | 44129 (Parma West) | 12.3% gross yield at 8.1× P/R — strongest in Parma cluster |
| **Best volume submarket** | 44134 (Parma East) | 44 active sales = more deal flow, but need sub-$190K to pencil |
| **Best SFR play** | 44129 3-BR under $175K | If you can find one, the rent anchors support strong cash flow |
| **Avoid** | 44130 (Parma mid) | Thin pool (7 sales), weakest yield, median above cap |

**If you're buying one property tomorrow:** Hunt 44129 for a 3-BR SFR below $175K with cosmetic rehab only. At $170K all-in and $1,800/mo rent, that's a 12.7% gross yield.

---

## 5) Data Limitations

| Issue | Impact |
|-------|--------|
| No individual property data | Cannot produce listing-level address/zpid/beds/baths/sqft tables or per-property verdicts |
| ZIP-level medians only | Medians may mask outliers; actual sub-$190K inventory is likely smaller/older stock |
| Rent data is aggregate | Rent Zestimates from prior pull; no per-property rentZestimate available |
| Data age | `cleveland_zip_stats.json` is from a prior cycle — market may have shifted |

---

## Next Steps

1. **Top up Zillapi credits** at https://zillapi.com/app/billing
2. **Re-run the cron** to pull live listing data for all three ZIPs
3. Post-credits, this report auto-populates with property-level tables + per-property take/negotiate/pass verdicts

*Report: `outputs/2026-09-20/parma-listings-under-190k/parma-listings.md`*