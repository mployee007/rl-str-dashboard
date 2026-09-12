# Parma Listings Under $190K — Pull Status

**Run:** 2026-09-12T19:21:45Z (Saturday, September 12, 2026)

## BLOCKED — All data sources unavailable

This pull failed. See `/opt/data/parma-pull-status.txt` for full details.

### Summary of attempts

| Source | Status |
|--------|--------|
| Zillapi MCP (ZIPs 44129, 44134, 44130) | Out of credits + server unreachable |
| Web search via Firecrawl | Dependency not installed |
| Direct Zillow web extract | Blocked by Firecrawl dependency |

### Manual fallback URLs

- [ZIP 44129 — Zillow under $190K](https://www.zillow.com/homes/for_sale/44129_rb/?price_max=190000)
- [ZIP 44134 — Zillow under $190K](https://www.zillow.com/homes/for_sale/44134_rb/?price_max=190000)
- [ZIP 44130 — Zillow under $190K](https://www.zillow.com/homes/for_sale/44130_rb/?price_max=190000)

No fabricated listings. Resume when Zillapi credits refresh or firecrawl is installed.