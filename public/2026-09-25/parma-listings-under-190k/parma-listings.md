# Parma Listings Pull — BLOCKED

**Date:** 2026-09-25 00:00 UTC (cron run)
**Target:** Active for-sale house listings in ZIPs 44129, 44134, 44130 under $190,000

## Source Status

| # | Source | Result | Detail |
|---|--------|--------|--------|
| 1 | **Zillapi MCP** (Tier 1) | ❌ BLOCKED | Out of credits for this cycle. Top up at https://zillapi.com/app/billing |
| 2 | **Zillapi retry** | ❌ UNREACHABLE | MCP server unreachable after 17 consecutive failures |
| 3 | **Camofox → Zillow** (Tier 2) | ❌ BLOCKED | First navigation resolved to "Winchester KS 66097" instead of Parma OH 44129 (Zillow misrouted the searchQueryState URL). Second navigation hit Cloudflare "Press & Hold" captcha. IP-based rate limit — no further Zillow navigations possible from this IP until captcha cooldown clears. |
| 4 | **web_search** (Tier 4) | ❌ BLOCKED | firecrawl-py not installed; lazy installs disabled (`security.allow_lazy_installs=false`). Cannot install in cron. |
| 5 | **SearXNG / agent_search** (Tier 3) | ❌ WRONG RESULTS | Returned FC Barcelona results. "Parma" → Parma, Italy in Bing. Exactly the European-namesake problem this skill warns about. All other engines down (Brave rate-limited, DuckDuckGo captcha, Startpage captcha, AOL HTTP error). |

## Recommendation

**Wait for Zillapi credit refresh** (typically monthly cycle), then re-run. This is the most reliable path. Camofox workaround is unreliable for multi-ZIP pulls in cron because of the single-page-load-per-IP captcha limitation.

## Direct Zillow URLs (open in your own browser)

- **44129 (Parma West):** https://www.zillow.com/homes/for_sale/44129_rb/1-_beds/0-190000_price/pricea_sort/
- **44134 (Parma):** https://www.zillow.com/homes/for_sale/44134_rb/1-_beds/0-190000_price/pricea_sort/
- **44130 (Parma/Middleburg Hts):** https://www.zillow.com/homes/for_sale/44130_rb/1-_beds/0-190000_price/pricea_sort/

## What the Camofox page did capture (DOM scrape, wrong area — Cleveland 44105)

These were "similar results nearby" to the misrouted search. Included for reference only — they are NOT in target ZIPs:

| Address | Price | Beds | Baths | Sqft | ZIP | Type | Days on Zillow | URL |
|---------|-------|------|-------|------|-----|------|----------------|-----|
| 4133 E 59th St, Cleveland | $9,999 | 3 | 1 | 1,440 | 44105 | House | 29 | [link](https://www.zillow.com/homedetails/4133-E-59th-St-Cleveland-OH-44105/33424631_zpid/) |
| 4309 E 73rd St, Cleveland | $29,900 | 4 | 1 | 1,760 | 44105 | Foreclosure | — | [link](https://www.zillow.com/homedetails/4309-E-73rd-St-Cleveland-OH-44105/33426592_zpid/) |
| 8111 Force Ave, Cleveland | $39,900 | 3 | 1 | 1,248 | 44105 | House | — | [link](https://www.zillow.com/homedetails/8111-Force-Ave-Cleveland-OH-44105/33426925_zpid/) |
| 7908 Vineyard Ave, Cleveland | $39,900 | 2 | 1 | 804 | 44105 | House | — | [link](https://www.zillow.com/homedetails/7908-Vineyard-Ave-Cleveland-OH-44105/33427576_zpid/) |
| 4339 E 72nd St, Cleveland | $42,500 | 1 | 1 | — | 44105 | House | 376 | [link](https://www.zillow.com/homedetails/4339-E-72nd-St-Cleveland-OH-44105/33426610_zpid/) |
| 6100 Gertrude Ave, Cleveland | $44,900 | 3 | 1 | 1,724 | 44105 | House | — | [link](https://www.zillow.com/homedetails/6100-Gertrude-Ave-Cleveland-OH-44105/33423729_zpid/) |
| 2700 Brookpark Rd Trlr 101, Cleveland | $45,000 | 3 | 2 | — | **44134** | Manufactured | — | [link](https://www.zillow.com/homedetails/2700-Brookpark-Rd-TRAILER-101-Cleveland-OH-44134/144421796_zpid/) |
| 8209 Russel Ln, Cleveland | $46,000 | 2 | 1 | — | 44144 | House | — | [link](https://www.zillow.com/homedetails/8209-Russell-Ln-Cleveland-OH-44144/441567958_zpid/) |
| 7813 Harvard Ave, Cleveland | $49,900 | 3 | 1 | 1,364 | 44105 | House (Price cut $8,600) | — | [link](https://www.zillow.com/homedetails/7813-Harvard-Ave-Cleveland-OH-44105/33425498_zpid/) |

⚠️ **Only one listing (2700 Brookpark Rd) is in ZIP 44134**, and it's a manufactured home/trailer — not a conventional house. None are in 44129 or 44130.

## Next Steps

1. Wait for Zillapi credit refresh (check https://zillapi.com/app/billing)
2. Re-run the cron job — it will use Zillapi first before falling back to Camofox
3. Alternatively, open the direct Zillow URLs above in a regular browser to screen manually