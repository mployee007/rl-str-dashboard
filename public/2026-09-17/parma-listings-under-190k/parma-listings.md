# Parma-Area Listings Under $190K — Status Report

**Date:** 2026-09-17  
**Status:** ❌ BLOCKED — Zillapi credits exhausted  

---

## Blocker Summary

Zillapi returned "Out of credits for this cycle" on the first call (ZIP 44129), and the MCP server became unreachable for subsequent calls. No live listing data could be retrieved.

### Sources Attempted

| Source | ZIP(s) | Result |
|--------|--------|--------|
| `mcp_zillapi_search_listings` | 44129 | "Out of credits for this cycle" |
| `mcp_zillapi_search_listings` | 44134 | MCP server unreachable |
| `mcp_zillapi_search_listings` | 44130 | MCP server unreachable |
| `web_search` (Firecrawl) | all | Lazy install disabled |
| Zillow.com / Redfin / Realtor.com / Homes.com | all | Blocked by captchas (known pattern — not attempted) |

---

## Direct Zillow Search Links (Open in Browser)

Until Zillapi credits refresh, use these direct Zillow searches to manually review listings:

- **[44129 — Parma West](https://www.zillow.com/homes/for_sale/44129_rb/?price_max=190000)** — houses under $190K
- **[44134 — Parma South](https://www.zillow.com/homes/for_sale/44134_rb/?price_max=190000)** — houses under $190K
- **[44130 — Middleburg Heights](https://www.zillow.com/homes/for_sale/44130_rb/?price_max=190000)** — houses under $190K

---

## Target Bounding Boxes (for reference)

| ZIP | Bbox (W,S,E,N) | Neighborhood |
|-----|-----------------|--------------|
| 44129 | -81.78, 41.37, -81.68, 41.42 | Parma West |
| 44134 | -81.72, 41.35, -81.65, 41.40 | Parma South |
| 44130 | -81.80, 41.35, -81.73, 41.41 | Middleburg Heights |

---

## Background: Why These ZIPs

These three ZIPs form the Parma/Middleburg Heights corridor — a dense, working-class Cleveland suburb with a high concentration of 1,200–1,600 sqft 3/1 and 3/2 bungalows and Cape Cods built 1940–1965. The $190K price cap targets:
- **Stabilized SFRs** in 44129/44130 at $150K–$190K
- **Value-add candidates** in 44134 at $120K–$170K
- **Potential duplexes** for small multifamily plays

Median rents in these ZIPs typically run $1,100–$1,400/month for a 3-bedroom, yielding 7–9% gross at the right basis.

---

## Next Steps

1. **Top up Zillapi credits** at [zillapi.com/app/billing](https://zillapi.com/app/billing)
2. **Re-run this pull** when credits are available
3. **Check for saved JSON** from prior Cleveland pulls in `/opt/data/outputs/` for cached data

---

*Status file: `/opt/data/parma-pull-status.txt`*  
*Report: `/opt/data/outputs/2026-09-17/parma-listings-under-190k/parma-listings.md`*