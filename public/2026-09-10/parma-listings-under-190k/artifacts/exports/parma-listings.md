# Parma Area Listings Under $190K — Pull Report

**Date:** 2026-09-10  
**Status:** ❌ FAILED — Zillapi credits exhausted, MCP server unreachable  

---

## Blocker Summary

| Source | Target | Result |
|--------|--------|--------|
| `mcp_zillapi_search_listings` | ZIP 44129 (Parma West) | **Out of credits** — "Top up or upgrade at https://zillapi.com/app/billing." |
| `mcp_zillapi_search_listings` | ZIP 44134 (Parma) | **MCP server unreachable** — 50 consecutive failures |
| `mcp_zillapi_search_listings` | ZIP 44130 (Middleburg Heights) | **MCP server unreachable** — 50 consecutive failures |
| `web_search` (Firecrawl backend) | Zillow.com 44129 | **Backend unavailable** — firecrawl-py not installed |
| `web_extract` / browser | Zillow.com, Redfin, Trulia, etc. | **Not attempted** — known to block with PerimeterX/Cloudflare per skill docs |

---

## What Was Requested

- ZIP 44129 — Active for-sale ≤ $190K
- ZIP 44134 — Active for-sale ≤ $190K
- ZIP 44130 — Active for-sale ≤ $190K

Bounding boxes used:
- 44129: `-81.78,41.37,-81.68,41.42`
- 44134: `-81.72,41.35,-81.65,41.40`
- 44130: `-81.80,41.35,-81.73,41.41`

---

## Direct Zillow Search URLs

Open these in a browser to manually view current listings:

| ZIP | Area | Direct URL |
|-----|------|------------|
| 44129 | Parma West | https://www.zillow.com/homes/for_sale/44129_rb/0-190000_price/0-169_mp/ |
| 44134 | Parma | https://www.zillow.com/homes/for_sale/44134_rb/0-190000_price/0-169_mp/ |
| 44130 | Middleburg Heights | https://www.zillow.com/homes/for_sale/44130_rb/0-190000_price/0-169_mp/ |

---

## Next Steps

1. **Top up Zillapi credits** at https://zillapi.com/app/billing — the MCP integration works when credits are available.
2. **Retry pull** once credits refresh — all three bounding boxes are defined and ready to go.
3. **Manual fallback** — user can browse the direct Zillow URLs above in the meantime.

---

*No listings were fabricated. This report reflects the actual state of tool availability at pull time.*