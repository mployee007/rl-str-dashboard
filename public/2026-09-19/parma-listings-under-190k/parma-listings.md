# Parma Listings Under $190K — Pull Report
**Date:** 2026-09-19  
**Status:** ❌ FAILED — Zillapi out of credits

---

## Blocker Summary

| Source | Status | Detail |
|---|---|---|
| Zillapi MCP (44129) | ❌ Out of credits | "Out of credits for this cycle. Top up or upgrade at https://zillapi.com/app/billing." |
| Zillapi MCP (44134) | ❌ Server unreachable | MCP server 'zillapi' unreachable after 112 consecutive failures |
| Zillapi MCP (44130) | ❌ Server unreachable | MCP server 'zillapi' unreachable after 112 consecutive failures |
| Zillow.com | ⛔ Blocked (captcha) | PerimeterX/Cloudflare — known blocker per skill docs |
| Redfin.com | ⛔ Blocked (captcha) | Same captcha wall — known blocker |
| Realtor.com | ⛔ Blocked (captcha) | Same captcha wall — known blocker |

---

## No Listings Retrieved

Zero listings were pulled for any ZIP. **No data was fabricated.**

---

## Direct Zillow Search URLs (open in browser)

These are the equivalent searches on Zillow — open manually while Zillapi recovers:

- **44129:** `https://www.zillow.com/homes/for_sale/44129_zip/1-_beds/0-190000_price/0-1000000_mp/pricea_sort/`
- **44134:** `https://www.zillow.com/homes/for_sale/44134_zip/1-_beds/0-190000_price/0-1000000_mp/pricea_sort/`
- **44130:** `https://www.zillow.com/homes/for_sale/44130_zip/1-_beds/0-190000_price/0-1000000_mp/pricea_sort/`

---

## Target Parameters (for reference)

| ZIP | Neighborhood | Bounding Box | Beds Min | Price Cap |
|---|---|---|---|---|
| 44129 | Parma West | `-81.78,41.37,-81.68,41.42` | 1+ | $190,000 |
| 44134 | Parma East | `-81.72,41.35,-81.65,41.40` | 1+ | $190,000 |
| 44130 | Parma South | `-81.80,41.35,-81.73,41.41` | 1+ | $190,000 |

---

## Next Steps

1. Wait for Zillapi credit refresh (top up at https://zillapi.com/app/billing)
2. Verify MCP server is reachable
3. Re-run this pull — the script is idempotent
4. Status file at `/opt/data/parma-pull-status.txt` will be updated on next run