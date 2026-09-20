# Parma Listings Under $190K — Pull Failed
**Date:** 2026-09-20
**Status:** ❌ BLOCKED — Zillapi out of credits, all web sources unavailable

## Source Grid

| Source | ZIP 44129 | ZIP 44134 | ZIP 44130 |
|--------|:---------:|:---------:|:---------:|
| Zillapi MCP (primary) | ❌ No credits | ❌ Server unreachable | ❌ Server unreachable |
| web_search (Firecrawl) | ❌ Not installed | ❌ Not installed | ❌ Not installed |
| Zillow.com (browser) | ⛔ Captcha-blocked | ⛔ Captcha-blocked | ⛔ Captcha-blocked |
| Redfin/Realtor/Trulia | ⛔ Captcha-blocked | ⛔ Captcha-blocked | ⛔ Captcha-blocked |

## No data was recovered. Zero listings available.

Direct search URLs for manual browser review:
- [44129 under $190K](https://www.zillow.com/homes/for_sale/44129_rb/0-190000_price/0-407_mp/)
- [44134 under $190K](https://www.zillow.com/homes/for_sale/44134_rb/0-190000_price/0-407_mp/)
- [44130 under $190K](https://www.zillow.com/homes/for_sale/44130_rb/0-190000_price/0-407_mp/)

## Resolution
1. Top up Zillapi credits at https://zillapi.com/app/billing
2. Verify MCP server connectivity (`hermes mcp list`)
3. Re-run this cron job or trigger manually with `"re-run parma pull"`