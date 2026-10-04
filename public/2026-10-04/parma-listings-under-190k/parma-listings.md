# Parma Area Listings Screen — BLOCKED

**Date:** 2026-10-04  
**ZIPs:** 44129 (Parma West), 44134 (Parma South), 44130 (Parma Heights area)  
**Max Price:** $190,000  
**Sort:** Price (Lowest First)  
**Status:** ❌ No data pulled — all sources blocked

---

## Source Attempts

| # | Source | Tool | Target | Result |
|---|--------|------|--------|--------|
| 1 | Zillapi MCP | `mcp_zillapi_search_listings` | 44129 | **Out of credits** — "Top up or upgrade at zillapi.com/app/billing" |
| 2 | Zillapi MCP | `mcp_zillapi_search_listings` | 44134 | **MCP unreachable** — 64 consecutive failures after credit exhaustion |
| 3 | Zillapi MCP | `mcp_zillapi_search_listings` | 44130 | **MCP unreachable** — 64 consecutive failures after credit exhaustion |
| 4 | Camofox → Zillow | `browser_navigate` | 44129 | **Captcha blocked** — Cloudflare "Press & Hold" challenge, HTTP 422 unsolvable |

---

## Direct Zillow URLs (open in your own browser)

These path-based URLs sort by price (lowest first) and filter to ≤$190K:

| ZIP | URL |
|-----|-----|
| **44129** | https://www.zillow.com/homes/for_sale/44129_rb/1-_beds/0-190000_price/pricea_sort/ |
| **44134** | https://www.zillow.com/homes/for_sale/44134_rb/1-_beds/0-190000_price/pricea_sort/ |
| **44130** | https://www.zillow.com/homes/for_sale/44130_rb/1-_beds/0-190000_price/pricea_sort/ |

---

## Market Context (from prior session data)

For reference while waiting — Parma-area baselines from the Cleveland-Elyria MSA:

| Metric | Value |
|--------|-------|
| MSA 3BR FMR (FY2025) | $1,553/mo (40th percentile) |
| Parma 2BR FMR (FY2025) | $1,188/mo |
| Parma 3BR FMR (FY2025) | $1,468/mo |
| Target gross yield | 8–10% (working-class suburbs) |
| GRM target range | 10–12.5x (implied by 8–10% yield) |
| Basis ceiling (3BR SFR @ $1,468/mo) | ~$176K @ 10% yield, ~$220K @ 8% yield |
| Basis ceiling (2BR SFR @ $1,188/mo) | ~$143K @ 10% yield, ~$178K @ 8% yield |

At a $190K cap with local FMR rents, properties should pencil at or near the 8% yield floor — cash-flow positive but tight on a 20%-down conventional loan.

---

## Resolution

| Action | Expected Outcome |
|--------|------------------|
| Top up Zillapi credits | `mcp_zillapi_search_listings` resumes working immediately |
| Wait 24h for IP captcha cooldown | Camofox first navigation works again |
| Open URLs above in browser | Instant access to live listings from any IP |

**Preference:** Zillapi top-up is the fastest path — credits restore instantly, and all three ZIPs can be pulled in one shot.

---

*Status file saved at: `/opt/data/parma-pull-status.txt`*  
*Blocked report saved at: `/opt/data/outputs/2026-10-04/parma-listings-under-190k/parma-listings.md`*