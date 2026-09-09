# Parma West / Parma Listings Under $190K — Pull Blocked

**Date:** 2026-09-09  
**Target ZIPs:** 44129 (Parma West), 44134 (Parma), 44130 (Parma)  
**Price Cap:** $190,000  
**Status:** ❌ BLOCKED — Zillapi out of credits

---

## Sources Attempted

| Source | Tool | Result |
|---|---|---|
| Zillapi | `mcp_zillapi_search_listings` (44129 bbox) | **Out of credits** — "Top up or upgrade at https://zillapi.com/app/billing." |
| Zillapi | `mcp_zillapi_search_listings` (44134 bbox) | MCP server unreachable (44 consecutive failures) |
| Zillapi | `mcp_zillapi_search_listings` (44130 bbox) | MCP server unreachable (44 consecutive failures) |
| Zillow.com | web_search / web_extract / browser | Not attempted — known PerimeterX/Cloudflare block |
| Redfin | web_search / web_extract / browser | Not attempted — known PerimeterX/Cloudflare block |
| Trulia | web_search / web_extract / browser | Not attempted — known PerimeterX/Cloudflare block |
| Realtor.com | web_search / web_extract / browser | Not attempted — known PerimeterX/Cloudflare block |

---

## ZIP-Level Benchmarks (from prior Zillapi pull — cached data)

Data sourced from `/opt/data/cleveland_zip_stats.json` (last successful pull).

| ZIP | Area | Median Sale | Median Rent | Sale Count (prior) | Rent Count (prior) | GRM | Gross Yield |
|---|---|---|---|---|---|---|---|
| **44129** | Parma West | $190,000 | $1,950 | 16 | 30 | 8.1 | 12.32% |
| **44135** | Cleveland W (adjacent) | $139,000 | $1,295 | 12 | 3 | 8.9 | 11.18% |
| **44111** | West Park (adjacent) | $181,075 | $1,604 | 25 | 3 (rent Z) | 9.4 | 10.63% |

**Note:** ZIPs 44134 and 44130 were **not** captured in the cached Cleveland stats file. Only 44129 has benchmark data.

---

## 44129 (Parma West) — Prior Context

- **Median sale:** $190,000 (right at the $190K cap)
- **Median rent:** $1,950/mo
- **Gross yield at median:** 12.32% — solid for a B-class suburb
- **Parma investment thesis:** Strong tenant demand from stable working-class base, older housing stock (1940s–1960s) with value-add potential, low vacancy. Parma is one of Cleveland's largest inner-ring suburbs with strong rental demand and relatively affordable entry points.
- **Buy box fit at $190K:** At $190K with $1,950 rent, the GRM of 8.1 and 12.3% gross yield is **investable** for stabilized hold. Margin compresses quickly above $190K — at $210K+ the yield drops toward 11%, which is still workable but tighter.

---

## Direct Search URLs (Open in Your Browser)

- **ZIP 44129 under $190K:** https://www.zillow.com/homes/for_sale/44129/0-190000_price/0-372104_mp/
- **ZIP 44134 under $190K:** https://www.zillow.com/homes/for_sale/44134/0-190000_price/0-372022_mp/
- **ZIP 44130 under $190K:** https://www.zillow.com/homes/for_sale/44130/0-190000_price/0-371926_mp/

---

## Investor Verdict (Based on Cached Benchmarks Only)

| ZIP | Verdict | Rationale |
|---|---|---|
| **44129** | **Negotiate → Take** (with live confirmation) | 12.3% gross yield at median; at $160–180K the yield pushes 13–15%. Wait for credits to confirm current inventory. |
| **44134** | **Unknown** | No cached data. Parma-proper ZIP — likely similar profile to 44129 but needs live pull. |
| **44130** | **Unknown** | No cached data. Adjacent to 44129; similar housing stock likely. Needs live pull. |

---

## Next Steps

1. Top up Zillapi credits at https://zillapi.com/app/billing
2. Re-run the cron job — it will pull fresh listings for all three ZIPs
3. Output will save to `/opt/data/outputs/YYYY-MM-DD/parma-listings-under-190k/parma-listings.md`
4. `parma-latest-listings.md` will auto-update with the raw table

**Status file:** `/opt/data/parma-pull-status.txt`