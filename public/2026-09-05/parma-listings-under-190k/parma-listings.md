# Parma Area Listings Screen — Under $190K
**Pull date:** 2026-09-05  
**Status:** ❌ BLOCKED — Zillapi credits exhausted

---

## Blocker Summary

Zillapi returned **"Out of credits for this cycle"** on the first bounding-box call (44129). The two subsequent calls (44134, 44130) hit MCP server unreachable errors — likely a cascade from the credit exhaustion.

| Source | Attempt | Result |
|---|---|---|
| Zillapi MCP (`mcp_zillapi_search_listings`) | 44129 bbox | **Out of credits** |
| Zillapi MCP (`mcp_zillapi_search_listings`) | 44134 bbox | Server unreachable |
| Zillapi MCP (`mcp_zillapi_search_listings`) | 44130 bbox | Server unreachable |

Per the skill's data-source strategy: Zillapi is the **only reliable path** for live listings in this environment. All web-based real estate sites (Zillow.com, Redfin, Trulia, Realtor.com, Homes.com, Movoto) block with captchas. No alternative was attempted.

---

## Direct Zillow Search URLs (open in your browser)

These URLs filter Zillow to each ZIP, max $190K, house/condo/townhome only:

- **44129 (Parma West):**  
  `https://www.zillow.com/homes/for_sale/44129_zip/0-190000_price/0-2856_mp/41.416,-81.678,41.366,-81.776_rect/14_zm/`

- **44134 (Parma East / Seven Hills):**  
  `https://www.zillow.com/homes/for_sale/44134_zip/0-190000_price/0-2750_mp/41.405,-81.647,41.35,-81.721_rect/14_zm/`

- **44130 (Middleburg Heights / Parma Heights):**  
  `https://www.zillow.com/homes/for_sale/44130_zip/0-190000_price/0-3022_mp/41.41,-81.73,41.347,-81.804_rect/14_zm/`

---

## Credit Refresh

Zillapi billing/credit dashboard: **https://zillapi.com/app/billing**

---

## Status File

Full blocker details saved to: `/opt/data/parma-pull-status.txt`