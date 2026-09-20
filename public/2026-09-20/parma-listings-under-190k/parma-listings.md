# Parma West Submarket: Live Listing Screen (Under $190K)

**Generated:** 2026-09-20 (cron run, attempt #2)  
**Status:** ❌ Zillapi credits exhausted — no individual listings available  
**Prior pull:** ZIP-level aggregates from `cleveland_zip_stats.json`  
**Last successful listing-level pull:** before 2026-09-19

---

## Attempt Log (This Run)

| # | Source | Details | Result |
|---|--------|---------|--------|
| 1 | Zillapi MCP — 44129 bbox | `-81.78,41.37,-81.68,41.42`, `beds_min=2`, `price_max=190000` | ❌ "Out of credits for this cycle" |
| 2 | Zillapi MCP — 44134 bbox | `-81.72,41.35,-81.65,41.40`, `beds_min=2`, `price_max=190000` | ❌ MCP server unreachable (122 failures) |
| 3 | Zillapi MCP — 44130 bbox | `-81.80,41.35,-81.73,41.41`, `beds_min=2`, `price_max=190000` | ❌ MCP server unreachable (122 failures) |

---

## ZIP-Level Aggregates (Fallback — from prior successful crawl)

| ZIP | Area | Active Sales | Median Sale | Median Rent | Gross Yield | P/R Ratio | Verdict |
|-----|------|-------------|-------------|-------------|-------------|-----------|---------|
| **44129** | Parma (W) | 16 | $190,000 | $1,950 | 12.32% | 8.1× | **Take selectively** |
| **44134** | Parma (E) / Brooklyn Hts | 44 | $200,000 | $1,675 | 10.05% | 10.0× | **Negotiate** |
| **44130** | Parma (mid) | 7 | $199,900 | $1,575 | 9.45% | 10.6× | **Pass** |

⚠️ Median sale prices for 44134 and 44130 sit above the $190K cap, meaning sub-$190K inventory in those ZIPs will be below-median (older, smaller, or rougher condition).

---

## Direct Zillow Search URLs (Open in Browser)

| ZIP | Zillow Link |
|-----|------------|
| 44129 | https://www.zillow.com/homes/for_sale/44129_rb/0-190000_price/ |
| 44134 | https://www.zillow.com/homes/for_sale/44134_rb/0-190000_price/ |
| 44130 | https://www.zillow.com/homes/for_sale/44130_rb/0-190000_price/ |

---

## Buy Box (First Pass — Using 44129 Anchors)

| Property Type | Target Basis | Stretch Basis | Target Rent (mo) | Gross Yield | Rehab Tolerance | Avoid |
|--------------|-------------|---------------|-------------------|-------------|-----------------|-------|
| 2-BR SFR | ≤ $160K | $175K | $1,500–$1,700 | 11.3%–12.8% | ≤ $20K | Foundation issues, knob & tube |
| 3-BR SFR | ≤ $175K | $190K | $1,700–$2,000 | 11.7%–13.7% | ≤ $25K | Roof/HVAC/plumbing stack replacement |
| Duplex | ≤ $170K/unit | $190K/unit | $1,200–$1,400/unit | 8.5%–9.9%/unit | ≤ $15K/unit | Shared utilities, unpermitted 2nd unit |

---

## Recommendations (Aggregate-Level)

| Category | Pick | Rationale |
|----------|------|-----------|
| **Best yield** | 44129 (Parma West) | 12.3% gross yield at 8.1× P/R — strongest in Parma cluster |
| **Best volume** | 44134 (Parma East) | 44 active sales = most deal flow, but need sub-$190K to pencil |
| **Avoid** | 44130 (Parma mid) | Thin pool (7 sales), weakest yield, median above cap |
| **If buying tomorrow** | Hunt 44129 for a 3-BR SFR below $175K | At $170K all-in and $1,800/mo rent = 12.7% gross yield |

---

## Data Limitations

| Issue | Impact |
|-------|--------|
| No individual listing data | Cannot produce address/zpid/beds/baths/sqft tables or per-property take/negotiate/pass |
| ZIP medians only | Actual sub-$190K inventory is likely older/smaller/rougher than medians suggest |
| Rent data is aggregate | No per-property rentZestimate available |
| Data staleness | `cleveland_zip_stats.json` is from a prior cycle — market may have shifted in 1+ weeks |

---

## Next Steps

1. **Top up Zillapi credits** at https://zillapi.com/app/billing
2. **Re-run the cron** — individual listing tables will auto-populate
3. Post-credits, this report populates with: property addresses, zpids, beds/baths/sqft, rent estimates, and per-property take/negotiate/pass verdicts

*Report: `outputs/2026-09-20/parma-listings-under-190k/parma-listings.md`*  
*Status: `/opt/data/parma-pull-status.txt`*