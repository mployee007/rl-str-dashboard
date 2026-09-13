# Parma Listings Under $190K — Pull Status

**Run:** 2026-09-13T00:00:00Z (Sunday, September 13, 2026)

## BLOCKED — 3rd consecutive day with no data

All data sources remain unavailable. No new listings retrieved.

### Sources attempted

| # | Source | Method | Result |
|---|--------|--------|--------|
| 1 | Zillapi MCP — ZIP 44129 | `mcp_zillapi_search_listings(bbox=-81.78,41.37,-81.68,41.42, price_max=190000)` | **Out of credits.** |
| 2 | Web extract — Zillow 44129 | `web_extract(zillow.com/homes/for_sale/44129_rb/)` | **firecrawl unavailable.** |
| 3 | Web search | `web_search("Parma OH homes for sale under $190000")` | **firecrawl unavailable.** |

### Manual fallback URLs

- [ZIP 44129 — Zillow under $190K](https://www.zillow.com/homes/for_sale/44129_rb/?price_max=190000)
- [ZIP 44134 — Zillow under $190K](https://www.zillow.com/homes/for_sale/44134_rb/?price_max=190000)
- [ZIP 44130 — Zillow under $190K](https://www.zillow.com/homes/for_sale/44130_rb/?price_max=190000)

### ZIP-Level Benchmarks (last known, unchanged since 9/10 pull)

| ZIP | Area | Median Sale | Median Rent | P/R Ratio | Gross Yield |
|-----|------|-------------|-------------|-----------|-------------|
| 44129 | Parma (W) | $190,000 | $1,950 | 8.1 | 12.3% |
| 44134 | Parma (E), Brooklyn Hts, Seven Hills | $200,000 | $1,675 | 10.0 | 10.1% |
| 44130 | Parma (mid) | $199,900 | $1,575 | 10.6 | 9.5% |

### Action required

Top up Zillapi credits at https://zillapi.com/app/billing. This is the **3rd consecutive day** of blocked pulls. No individual property data exists for any of the three target ZIPs.