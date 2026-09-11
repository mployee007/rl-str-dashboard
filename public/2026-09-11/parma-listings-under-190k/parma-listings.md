# Parma West / Parma / Parma Heights — Listings Under $190K

**Pull attempt:** 2026-09-11  
**Status:** ❌ BLOCKED — Zillapi out of credits

---

## Blocker Report

Zillapi returned "Out of credits for this cycle" on the first call (44129), and the MCP server became unreachable on subsequent calls (44134, 44130). Zero listings were retrieved.

| Source | ZIP | Result |
|---|---|---|
| Zillapi (search_listings) | 44129 | ❌ Out of credits |
| Zillapi (search_listings) | 44134 | ❌ MCP server unreachable |
| Zillapi (search_listings) | 44130 | ❌ MCP server unreachable |

Per the `real-estate-submarket-screening` skill: all web-based listing sites (Zillow.com, Redfin, Trulia, Realtor.com) block automated access with captchas. The only path is Zillapi, which is dry.

---

## Direct Zillow Search URLs (open in your browser)

| ZIP | Neighborhood | Direct Zillow Search |
|---|---|---|
| 44129 | Parma West | [Zillow: 44129 ≤$190K](https://www.zillow.com/homes/for_sale/44129_rb/max-190000_price/) |
| 44134 | Parma | [Zillow: 44134 ≤$190K](https://www.zillow.com/homes/for_sale/44134_rb/max-190000_price/) |
| 44130 | Parma Heights | [Zillow: 44130 ≤$190K](https://www.zillow.com/homes/for_sale/44130_rb/max-190000_price/) |

---

## Next Steps

1. **Top up Zillapi credits** at https://zillapi.com/app/billing
2. **Re-run this cron job** — the script is idempotent and will pick up fresh listings
3. Status file at `/opt/data/parma-pull-status.txt` for monitoring