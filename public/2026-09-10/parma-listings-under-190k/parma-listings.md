# Parma Listings Under $190K — Pull Blocked (Zillapi Out of Credits)

**Date:** 2026-09-10 (latest re-attempt)
**Target ZIPs:** 44129 (Parma West), 44134 (Parma), 44130 (Parma mid)
**Price Cap:** $190,000
**Status:** ❌ BLOCKED — Zillapi out of credits. No fresh listings pulled.

---

## Bottom Line

No live listing screen can be produced this cycle — the Zillapi account has no credits remaining, so every `search_listings` call returned an out-of-credits error (and the MCP server is also intermittently unreachable). Per the data-integrity rule, **no listings were fabricated.** Cached ZIP-level benchmarks from a prior successful pull are shown below so the screen still has a usable analytical anchor, but they are **stale and must not be treated as current inventory.**

---

## Sources Attempted

| Source | Tool | Result |
|---|---|---|
| Zillapi | `mcp_zillapi_search_listings` (44129 bbox) | **Out of credits** — "Top up or upgrade at https://zillapi.com/app/billing." |
| Zillapi | `mcp_zillapi_search_listings` (44134 bbox) | MCP server unreachable (47 consecutive failures) |
| Zillapi | `mcp_zillapi_search_listings` (44130 bbox) | MCP server unreachable (47 consecutive failures) |
| Zillow.com | `web_search` (Firecrawl backend) | Firecrawl disabled (`lazy_installs=false`) |
| Redfin / Trulia / Realtor.com | web / browser | Not attempted — known PerimeterX/Cloudflare block |

---

## Cached ZIP-Level Benchmarks (prior successful pull — STALE)

Source: `/opt/data/cleveland_zip_stats.json`

| ZIP | Area | Median Sale | Median Rent | Sale Count (prior) | Rent Count (prior) | GRM | Gross Yield |
|---|---|---|---|---|---|---|---|
| **44129** | Parma West | $190,000 | $1,950 | 16 | 30 | 8.1 | 12.32% |
| **44134** | Parma E / Brooklyn Hts / Seven Hills | $200,000 | $1,675 | 44 | 32 | 10.0 | 10.05% |
| **44130** | Parma (mid) | $199,900 | $1,575 | 7 | 0 (2 rent-Z) | 10.6 | 9.45% |

> ⚠️ These medians reflect a prior sample window, not today's active inventory. Median sale for 44134 and 44130 sits **at/above** the $190K cap, meaning the sub-$190K subset in those ZIPs skews to smaller/older/rehab stock.

---

## Investor Verdict (cached benchmarks only — confirm with live pull)

| ZIP | Verdict | Rationale |
|---|---|---|
| **44129** | **Negotiate → Take** | 12.3% gross yield / 8.1 GRM at median is the best of the three. Sub-$190K entry pushes yield toward 13–15%. Strongest stabilized-hold profile. |
| **44134** | **Take selectively** | 10.0% yield / 10.0 GRM; largest sale sample (44) but median at $200K. Only sub-$190K outliers pencil — target the low end of the block band. |
| **44130** | **Negotiate** | 9.45% yield / 10.6 GRM is weakest; thin inventory (7 prior sales). Needs meaningfully below-median basis to clear the yield bar. |

---

## Direct Search URLs (open in your own browser)

- **44129 under $190K:** https://www.zillow.com/homes/for_sale/44129/0-190000_price/0-372104_mp/
- **44134 under $190K:** https://www.zillow.com/homes/for_sale/44134/0-190000_price/0-372022_mp/
- **44130 under $190K:** https://www.zillow.com/homes/for_sale/44130/0-190000_price/0-371926_mp/

---

## Next Steps

1. Top up Zillapi credits at https://zillapi.com/app/billing
2. Re-run the cron job — it will pull fresh listings for all three ZIPs and produce the live price-sorted table with per-property verdicts.
3. Output will save to `/opt/data/outputs/YYYY-MM-DD/parma-listings-under-190k/parma-listings.md`; `parma-latest-listings.md` auto-updates with the raw table.

**Status file:** `/opt/data/parma-pull-status.txt`