# Parma Listings Under $190K — BLOCKED

**Pull Date:** 2026-09-12
**Status:** ❌ Zillapi credits exhausted

## Why This Report Is Empty

All three Zillapi MCP calls failed:

| ZIP | Bounding Box | Error |
|-----|-------------|-------|
| 44129 | `-81.78,41.37,-81.68,41.42` | Out of credits |
| 44134 | `-81.72,41.35,-81.65,41.40` | MCP server unreachable |
| 44130 | `-81.80,41.35,-81.73,41.41` | MCP server unreachable |

Per the STR skill data-source strategy: Zillapi is the **only reliable path** for live property data. All web-based real estate sites (Zillow.com, Redfin, Trulia, etc.) block browser/curl access. No listings were fabricated.

## Resolution

Top up Zillapi credits at https://zillapi.com/app/billing and re-run. The pull parameters are saved and ready.

## Direct Search URLs (Manual Fallback)

| ZIP | Link |
|-----|------|
| 44129 (Parma West) | https://www.zillow.com/homes/for_sale/44129/0-190000_price/house_type/ |
| 44134 (Parma East) | https://www.zillow.com/homes/for_sale/44134/0-190000_price/house_type/ |
| 44130 (Parma South) | https://www.zillow.com/homes/for_sale/44130/0-190000_price/house_type/ |

---

*Report saved to `/opt/data/outputs/2026-09-12/parma-listings-under-190k/parma-listings.md`*