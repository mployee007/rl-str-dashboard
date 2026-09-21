# Parma Listings Under $190K — Pull Failed (Out of Credits)

**Date:** 2026-09-21  
**Status:** ❌ Blocked — Zillapi out of credits for this cycle  
**ZIPs targeted:** 44129, 44134, 44130  
**Price cap:** $190,000

---

## Blocker Details

| Source | ZIP | Result |
|--------|-----|--------|
| Zillapi MCP (`search_listings`) | 44129 | ❌ "Out of credits for this cycle. Top up or upgrade at https://zillapi.com/app/billing." |
| Zillapi MCP (`search_listings`) | 44134 | ❌ MCP server unreachable (127 consecutive failures — follow-on from credit exhaustion) |
| Zillapi MCP (`search_listings`) | 44130 | ❌ MCP server unreachable (127 consecutive failures — follow-on from credit exhaustion) |

All web-based real estate sites (Zillow.com, Redfin, Trulia, Realtor.com) are known to block with captchas in this environment and were NOT attempted per the skill's data-source strategy.

---

## Manual Fallback — Direct Zillow Search URLs

Open these in your browser to view current listings:

- **44129 (Parma West) under $190K:**  
  https://www.zillow.com/homes/for_sale/44129_rb/0-190000_price/0-190000_mp/41.37,-81.68,41.42,-81.78_rect/13_zm/

- **44134 (Parma South/Central) under $190K:**  
  https://www.zillow.com/homes/for_sale/44134_rb/0-190000_price/0-190000_mp/41.35,-81.65,41.40,-81.72_rect/13_zm/

- **44130 (Parma Heights/Middleburg) under $190K:**  
  https://www.zillow.com/homes/for_sale/44130_rb/0-190000_price/0-190000_mp/41.35,-81.73,41.41,-81.80_rect/13_zm/

---

## Next Step

Resume when Zillapi credits refresh. The status file at `/opt/data/parma-pull-status.txt` records the blocker.