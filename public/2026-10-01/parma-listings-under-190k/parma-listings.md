# Parma West Listings Screen — Under $190K
**Date:** 2026-10-01 UTC  
**Run type:** Scheduled cron  
**Status: ❌ BLOCKED — NO DATA RETRIEVED**

## Executive Summary

All five data sources failed. Zillapi is out of credits, the IP is Cloudflare-captcha'd on Zillow's web UI, AgentSearch misroutes Ohio queries to other states, and web_search requires firecrawl (unavailable in cron). Zero listings were retrieved across all three target ZIPs (44129, 44134, 44130).

## Source Failure Log

| Tier | Source | Tool | Error |
|------|--------|------|-------|
| 1 | Zillapi MCP | `mcp_zillapi_search_listings` | Out of credits (first call). MCP server unreachable after (calls 2–3). |
| 2 | Zillow + Camofox | `browser_navigate` | Cloudflare "Press & Hold" captcha — Reference ID `1f557e05-bd8b-11f1-b822-eaf11a746896` |
| 2 | Zillow + AgentSearch | `browser_fetch` | HTTP 403 "Access to this page has been denied" |
| 3 | SearXNG (Bing) | `mcp_agent_search_http_search` | Returned Baltimore MD listings — "Parma Ohio" query misrouted |
| 4 | web_search | `web_search` | Blocked — `firecrawl-py` not installed, lazy installs disabled |

## Rent Anchors (FY2025 HUD FMR)

For reference when listings are available, the Cleveland-Elyria MSA Fair Market Rents:

| Bedrooms | MSA FMR | Parma Adjusted (90%) |
|----------|---------|---------------------|
| 1BR | $903 | $813 |
| 2BR | $1,098 | $988 |
| 3BR | $1,553 | $1,398 |
| 4BR | $1,810 | $1,629 |

These are the buy-box rent anchors for screening when data becomes available. ⚠️ Market-derived — NOT property-specific.

## Direct Zillow Links (Manual Follow-Up)

Open these in your browser to view current listings:

- **44129:** https://www.zillow.com/homes/for_sale/44129_rb/1-_beds/0-190000_price/pricea_sort/
- **44134:** https://www.zillow.com/homes/for_sale/44134_rb/1-_beds/0-190000_price/pricea_sort/
- **44130:** https://www.zillow.com/homes/for_sale/44130_rb/1-_beds/0-190000_price/pricea_sort/

## Resolution

1. **Zillapi credits:** Top up at https://zillapi.com/app/billing — the credit pool covers all three bounding-box calls
2. **IP rotation:** If the VPS IP is permanently flagged, Camofox won't work until the IP changes
3. **Next run:** The cron will retry this task. Status file at `/opt/data/parma-pull-status.txt`

## File Manifest

| File | Path |
|------|------|
| Full report | `/opt/data/outputs/2026-10-01/parma-listings-under-190k/parma-listings.md` |
| Quick ref | `/opt/data/parma-latest-listings.md` |
| Status log | `/opt/data/parma-pull-status.txt` |