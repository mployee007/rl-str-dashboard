# Parma, OH — Active For-Sale Listings Under $190K

**Pull date:** 2026-10-04  
**Target ZIPs:** 44129 (Parma West), 44134 (Parma SE), 44130 (Parma SW)  
**Price cap:** $190,000  
**Status:** ⛔ BLOCKED — all automated data sources unavailable

## Source Attempt Summary

| # | Source | Result |
|---|--------|--------|
| 1 | Zillapi MCP `search_listings` | ❌ Out of credits — 44129 returned credit exhaustion; 44134/44130 unreachable |
| 2 | Camofox Browser → Zillow | ❌ Cloudflare "Press & Hold" captcha on first navigation (HTTP 422 on click) |
| 3 | AgentSearch `browser_fetch` | ❌ HTTP 403 PerimeterX "Access Denied" |
| 4 | Direct `curl` | ❌ PerimeterX JS captcha page |

**Root cause:** IP-level rate limiting by Zillow/Cloudflare + Zillapi credit pool exhausted.

## Parma Market Context (from cached data)

For reference while listings are unavailable:

| Metric | Value |
|--------|-------|
| MSA | Cleveland-Elyria, OH |
| MSA 3BR FMR (FY2025) | $1,553/mo (40th percentile) |
| Parma-adjusted 3BR est. | ~$1,398/mo (90% of MSA) |
| Parma-adjusted 2BR est. | ~$988/mo (90% of MSA) |
| Parma ZIP median home values | $150K–$220K range (ZORI, est.) |
| Investor profile | Working-class suburb, stabilized rental hold / light value-add SFR |

**⚠️ Rent estimates are market-derived — NOT property-specific.**

## Manual Follow-Up URLs

Open these in a standard browser (not blocked):

| ZIP | Direct Zillow Search |
|-----|----------------------|
| **44129** | [Parma West — under $190K, 1+ bed](https://www.zillow.com/homes/for_sale/44129_rb/1-_beds/0-190000_price/pricea_sort/) |
| **44134** | [Parma SE — under $190K, 1+ bed](https://www.zillow.com/homes/for_sale/44134_rb/1-_beds/0-190000_price/pricea_sort/) |
| **44130** | [Parma SW — under $190K, 1+ bed](https://www.zillow.com/homes/for_sale/44130_rb/1-_beds/0-190000_price/pricea_sort/) |

## Next Steps

1. **Manual pull:** Open the URLs above in a browser, copy listing data into the report.
2. **Zillapi credits:** Top up at https://zillapi.com/app/billing — then re-run this cron job.
3. **IP rotation:** If Camofox needs a different exit IP, configure a proxy or VPN before the next pull.
4. **Resume:** Once data is available, the processing pipeline (filter → verdict → markdown table → buy box) is ready and will produce the standard deliverable.

---

*Status file: `/opt/data/parma-pull-status.txt`*  
*Fallback timestamp: 2026-10-04T00:00:00Z*