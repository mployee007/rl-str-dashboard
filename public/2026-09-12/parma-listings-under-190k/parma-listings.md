# Parma Listings Under $190K — Pull Status

**Run:** 2026-09-12T22:24:34Z (Saturday, September 12, 2026)

## BLOCKED — All data sources unavailable

This pull failed. See `/opt/data/parma-pull-status.txt` for full details.

### Summary of attempts

| Source | Status |
|--------|--------|
| Zillapi MCP (ZIPs 44129, 44134, 44130) | Out of credits + server unreachable |
| Web search | firecrawl dependency not installed |

### Manual fallback URLs

- [ZIP 44129 — Zillow under $190K](https://www.zillow.com/homes/for_sale/44129_rb/?price_max=190000)
- [ZIP 44134 — Zillow under $190K](https://www.zillow.com/homes/for_sale/44134_rb/?price_max=190000)
- [ZIP 44130 — Zillow under $190K](https://www.zillow.com/homes/for_sale/44130_rb/?price_max=190000)

### ZIP-Level Benchmarks (from most recent successful pull)

| ZIP | Area | Median Sale | Median Rent | P/R Ratio | Gross Yield |
|-----|------|-------------|-------------|-----------|-------------|
| 44129 | Parma (W) | $190,000 | $1,950 | 8.1 | 12.3% |
| 44134 | Parma (E), Brooklyn Hts, Seven Hills | $200,000 | $1,675 | 10.0 | 10.1% |
| 44130 | Parma (mid) | $199,900 | $1,575 | 10.6 | 9.5% |

**Note:** These are median aggregates, not individual live listings. The $190K cap may still yield individual properties below these medians — especially in 44129 where the median sits right at the cap.

No fabricated listings. Resume when Zillapi credits refresh.