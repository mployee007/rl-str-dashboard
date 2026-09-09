# Parma West Listings Under $190K — Pull Blocked

**Date:** 2026-09-09  
**ZIPs:** 44129 (Parma West), 44134 (Parma South), 44130 (Parma East/Middleburg Hts)  
**Status:** ❌ Zillapi out of credits — no live data pulled

---

## Blocker Summary

| Source | ZIP | Result |
|---|---|---|
| Zillapi MCP | 44129 | **Out of credits** — "Top up or upgrade at https://zillapi.com/app/billing" |
| Zillapi MCP | 44134 | MCP server unreachable (40 consecutive failures, triggered by credit exhaustion) |
| Zillapi MCP | 44130 | MCP server unreachable (same) |
| Zillow.com (web) | — | Not attempted — PerimeterX/Cloudflare captcha blocks all browser/curl access |
| Redfin/Trulia/Realtor.com | — | Not attempted — same captcha block, per skill guidance |

---

## Direct Zillow Search URLs (open in your browser)

These will show all active for-sale listings under $190K in each ZIP on Zillow.com:

- **44129 (Parma West):**  
  https://www.zillow.com/homes/for_sale/44129_rb/?searchQueryState={"pagination":{},"mapBounds":{"west":-81.78,"south":41.37,"east":-81.68,"north":41.42},"filterState":{"price":{"max":190000},"fsba":{"value":false},"fsbo":{"value":false},"nc":{"value":false},"fore":{"value":false},"cmsn":{"value":false},"auc":{"value":false},"pmf":{"value":false},"fore":{"value":false}},"isListVisible":true}

- **44134 (Parma South):**  
  https://www.zillow.com/homes/for_sale/44134_rb/?searchQueryState={"pagination":{},"mapBounds":{"west":-81.72,"south":41.35,"east":-81.65,"north":41.40},"filterState":{"price":{"max":190000},"fsba":{"value":false},"fsbo":{"value":false},"nc":{"value":false},"fore":{"value":false},"cmsn":{"value":false},"auc":{"value":false},"pmf":{"value":false},"fore":{"value":false}},"isListVisible":true}

- **44130 (Parma East / Middleburg Heights):**  
  https://www.zillow.com/homes/for_sale/44130_rb/?searchQueryState={"pagination":{},"mapBounds":{"west":-81.80,"south":41.35,"east":-81.73,"north":41.41},"filterState":{"price":{"max":190000},"fsba":{"value":false},"fsbo":{"value":false},"nc":{"value":false},"fore":{"value":false},"cmsn":{"value":false},"auc":{"value":false},"pmf":{"value":false},"fore":{"value":false}},"isListVisible":true}

---

## Next Steps

1. **Top up Zillapi credits** at https://zillapi.com/app/billing
2. **Re-run this job** — the cron task will pick up fresh data automatically
3. **Manual fallback:** Use the Zillow URLs above in your own browser to screen deals immediately

---

## Status File

Saved to `/opt/data/parma-pull-status.txt` — timestamped blocker record.