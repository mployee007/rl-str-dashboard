# Parma Listings Under $190K — Pull Report
**Date:** 2026-09-13
**ZIPs:** 44129, 44134, 44130
**Price Cap:** $190,000

---

## BLOCKED — Zillapi Credits Exhausted

This pull could not complete. Zillapi returned "Out of credits for this cycle" for 44129, and the MCP server became unreachable (72 consecutive failures) for 44134 and 44130.

No listings were fabricated. No fallback data is available — per the skill's data-source strategy, all web-based real estate sites (Zillow.com, Redfin, Trulia, Realtor.com) block automated access with captchas, and Zillapi is the only reliable path.

---

## Sources Attempted

| # | Source | Tool | Target | Result |
|---|---|---|---|---|
| 1 | Zillapi | mcp_zillapi_search_listings | ZIP 44129, bbox -81.78/41.37/-81.68/41.42 | ❌ Out of credits |
| 2 | Zillapi | mcp_zillapi_search_listings | ZIP 44134, bbox -81.72/41.35/-81.65/41.40 | ❌ Server unreachable |
| 3 | Zillapi | mcp_zillapi_search_listings | ZIP 44130, bbox -81.80/41.35/-81.73/41.41 | ❌ Server unreachable |

---

## Manual Workaround

Open these direct Zillow search URLs in a browser:

| ZIP | URL |
|---|---|
| 44129 | https://www.zillow.com/homes/for_sale/44129_rid/0-190000_price/0-555_mp/ |
| 44134 | https://www.zillow.com/homes/for_sale/44134_rid/0-190000_price/0-555_mp/ |
| 44130 | https://www.zillow.com/homes/for_sale/44130_rid/0-190000_price/0-555_mp/ |

---

## Recovery Plan

1. Top up Zillapi credits at https://zillapi.com/app/billing
2. The scheduled cron job will retry on its next cycle
3. Status file saved at `/opt/data/parma-pull-status.txt`
4. This report saved at `/opt/data/outputs/2026-09-13/parma-listings-under-190k/parma-listings.md`