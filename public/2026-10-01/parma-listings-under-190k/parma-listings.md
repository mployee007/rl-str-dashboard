# 🔴 Parma Listings Pull — BLOCKED

**Date:** 2026-10-01
**Task:** Pull active for-sale house listings in ZIPs 44129, 44134, 44130 (max $190K)
**Status:** ALL DATA PATHS EXHAUSTED — NO LISTINGS RETRIEVED

---

## Source Attempts

| # | Source | Tool | Result |
|---|--------|------|--------|
| 1 | **Zillapi MCP** | `mcp_zillapi_search_listings` (44129 bbox) | ❌ "Out of credits for this cycle" |
| 2 | **Zillapi MCP** | `mcp_zillapi_search_listings` (44134 bbox) | ❌ MCP server unreachable (53 consecutive failures) — triggered by first retry after credit exhaustion |
| 3 | **Zillapi MCP** | `mcp_zillapi_search_listings` (44130 bbox) | ❌ MCP server unreachable (same cascading failure) |
| 4 | **Camofox Browser → Zillow** | `browser_navigate` to `https://www.zillow.com/homes/for_sale/44129_rb/1-_beds/0-190000_price/pricea_sort/` | ❌ Cloudflare "Press & Hold" captcha — IP already burned from prior sessions |
| 5 | **agent_search browser_fetch** | `mcp_agent_search_http_browser_fetch` (same URL) | ❌ HTTP 403 "Access to this page has been denied" |
| 6 | **agent_search read_url** | `mcp_agent_search_http_read_url` (same URL) | ❌ Fell through to Wikipedia "World Wide Web" article (search-about fallback) |

---

## Rent Anchors (FY2025 HUD FMR — Available)

The Cleveland-Elyria MSA FMR baselines are available for valuation when listings become accessible:

| Unit | MSA FMR | Parma Adj. (90%) |
|------|---------|-------------------|
| 1BR | $903 | $813 |
| 2BR | $1,098 | $988 |
| 3BR | $1,553 | $1,398 |
| 4BR | $1,810 | $1,629 |

⚠️ Market-derived — NOT property-specific.

---

## Direct Zillow URLs (Open in Your Browser)

Copy-paste these URLs to pull listings manually:

| ZIP | URL |
|-----|-----|
| **44129** (Parma West) | https://www.zillow.com/homes/for_sale/44129_rb/1-_beds/0-190000_price/pricea_sort/ |
| **44134** (Parma South) | https://www.zillow.com/homes/for_sale/44134_rb/1-_beds/0-190000_price/pricea_sort/ |
| **44130** (Middleburg Hts / Parma) | https://www.zillow.com/homes/for_sale/44130_rb/1-_beds/0-190000_price/pricea_sort/ |

---

## Resolution Paths

1. **Wait for Zillapi credits to refresh** — the next cycle should restore access. This is the preferred path since Zillapi returns structured data with rent estimates and can pull all three ZIPs in parallel.
2. **VPN / IP rotation for Camofox** — if Camofox runs on a fresh IP, the first Zillow navigation will succeed and `__NEXT_DATA__` extraction captures all listings. This works once per fresh IP.
3. **Manual pull** — open the direct URLs above in a browser and forward the listings for processing. I have the FMR baselines ready for GRM/verdict computation.

**Next scheduled run will automatically retry Tier 1 (Zillapi).**