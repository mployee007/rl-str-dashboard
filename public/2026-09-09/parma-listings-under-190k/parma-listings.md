# Parma Listings Under $190K — Fallback Report

**Generated:** 2026-09-09T15:32:13Z  
**Status:** ❌ BLOCKED — Zillapi unavailable  
**ZIPs attempted:** 44129, 44134, 44130  
**Price cap:** $190,000

---

## Blocker Details

| Source | ZIP | Error |
|---|---|---|
| Zillapi MCP (`search_listings`) | 44129 | Out of credits for this cycle |
| Zillapi MCP (`search_listings`) | 44134 | MCP server unreachable (42 failures) |
| Zillapi MCP (`search_listings`) | 44130 | MCP server unreachable (42 failures) |

No listings were retrieved. Zillapi is both out of credits and the MCP server is unreachable.

Web-based fallbacks (Zillow.com, Redfin, Trulia, Realtor.com, Homes.com, Movoto) were not attempted because all of these sites block automated access with PerimeterX/Cloudflare captchas — as documented in the `real-estate-submarket-screening` skill.

---

## Action Required

1. **Recharge Zillapi credits:** https://zillapi.com/app/billing
2. **Verify MCP server health:** The `zillapi` MCP server needs to be restarted or checked — it had 42 consecutive failures.
3. **Re-run this cron job** once both issues are resolved. The job will auto-save to:
   - Full report: `/opt/data/outputs/YYYY-MM-DD/parma-listings-under-190k/parma-listings.md`
   - Quick reference: `/opt/data/parma-latest-listings.md`
   - Status: `/opt/data/parma-pull-status.txt` (this file was also updated)

---

## Manual Workaround

Open these Zillow searches in your browser:

- **ZIP 44129 (Parma West):** [Zillow search](https://www.zillow.com/homes/for_sale/Parma-OH/pmf,pf_pt/41.37,-81.68,41.42,-81.78_rect/X1-SS1005gadf57mrhn_9ohqk_sse14_menu/)
- **ZIP 44134 (Parma):** [Zillow search](https://www.zillow.com/homes/for_sale/Parma-OH/pmf,pf_pt/41.35,-81.65,41.40,-81.72_rect/X1-SS1005gadf57mrhn_9ohqk_sse14_menu/)
- **ZIP 44130 (Middleburg Hts / Parma Hts):** [Zillow search](https://www.zillow.com/homes/for_sale/Middleburg-Heights-OH/pmf,pf_pt/41.35,-81.73,41.41,-81.80_rect/X1-SS1005gadf57mrhn_9ohqk_sse14_menu/)

**No listings were fabricated.** This report reflects the actual tool outcomes.