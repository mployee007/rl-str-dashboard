# Parma, OH — Listings Under $190K: 44129 / 44134 / 44130

**Pull date:** 2026-09-09 03:23 UTC  
**Status:** ❌ BLOCKED — Unable to retrieve live listings  
**Target:** For-sale single-family houses, price cap $190,000

---

## Block Summary

All three Zillapi bounding-box queries failed:

| ZIP | Bounding Box | Result |
|-----|-------------|--------|
| 44129 | `-81.78,41.37,-81.68,41.42` | **Out of credits** |
| 44134 | `-81.72,41.35,-81.65,41.40` | MCP server unreachable (38 failures) |
| 44130 | `-81.80,41.35,-81.73,41.41` | MCP server unreachable (38 failures) |

### Sources attempted

| Source | Method | Result |
|--------|--------|--------|
| Zillapi MCP | `mcp_zillapi_search_listings` | Out of credits |
| Zillapi MCP server | Retry | 38 consecutive failures — unreachable |
| Prior saved JSON | Filesystem search (`*44129*`, `*parma*`, `*cleveland*`) | No prior dumps found |
| Zillow.com | Not attempted | Blocked by PerimeterX captchas (per skill guidance) |
| Redfin/Trulia/Realtor | Not attempted | Blocked by Cloudflare/captchas (per skill guidance) |

---

## Direct Browser Links

Open these in your own browser to view current listings:

| ZIP | URL |
|-----|-----|
| **44129** (Parma West) | [zillow.com/homes/for_sale/44129_house/max_price,190000](https://www.zillow.com/homes/for_sale/44129_house/max_price,190000/) |
| **44134** (Parma South) | [zillow.com/homes/for_sale/44134_house/max_price,190000](https://www.zillow.com/homes/for_sale/44134_house/max_price,190000/) |
| **44130** (Parma East) | [zillow.com/homes/for_sale/44130_house/max_price,190000](https://www.zillow.com/homes/for_sale/44130_house/max_price,190000/) |

---

## Recovery Plan

1. **Top up Zillapi credits** at [zillapi.com/app/billing](https://zillapi.com/app/billing)
2. **Next cron cycle** will automatically retry if credits are available
3. **No data fabrication** — all tables above are intentionally empty

---

*Status file: `/opt/data/parma-pull-status.txt`*  
*Summary file: `/opt/data/parma-latest-listings.md`*