# Parma West Listings Under $190K — Pull Status

**Run date:** 2026-09-16  
**Status:** ❌ FAILED — Zillapi credits exhausted / MCP server unreachable

---

## Blocker Summary

| Source | Action | Result |
|---|---|---|
| **Zillapi MCP** (primary) | `search_listings` for 44129, 44134, 44130 | Out of credits + MCP server unreachable (92 consecutive failures) |
| **Zillow.com** (web) | Not attempted | Per skill: blocked by PerimeterX/Cloudflare captchas — known failure path |
| **Redfin** (web) | Not attempted | Per skill: blocked by captchas |
| **Realtor.com / Trulia / Movoto** | Not attempted | Per skill: all blocked by captchas |

---

## Direct Zillow Search URLs (Manual Fallback)

Open these in your own browser to view current listings:

- **44129 (Parma West):**  
  https://www.zillow.com/homes/for_sale/44129_rb/0-190000_price/0-611_mp/

- **44134 (Parma South):**  
  https://www.zillow.com/homes/for_sale/44134_rb/0-190000_price/0-611_mp/

- **44130 (Parma Heights / Middleburg Heights area):**  
  https://www.zillow.com/homes/for_sale/44130_rb/0-190000_price/0-611_mp/

---

## Bounding Boxes Used

| ZIP | West | South | East | North |
|---|---|---|---|---|
| 44129 | -81.78 | 41.37 | -81.68 | 41.42 |
| 44134 | -81.72 | 41.35 | -81.65 | 41.40 |
| 44130 | -81.80 | 41.35 | -81.73 | 41.41 |

---

## Next Steps

1. Top up Zillapi credits at https://zillapi.com/app/billing
2. Re-run this pull (same bounding boxes, same $190K cap)
3. Report will auto-generate tables with investor verdicts per the screening framework

*No listings were fabricated. All fields are empty pending a successful pull.*