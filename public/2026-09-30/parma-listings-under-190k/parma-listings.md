# Parma West Under-$190K Listing Pull — FAILED
**Date:** 2026-09-30 (cron run)  
**Target ZIPs:** 44129, 44134, 44130  
**Price Cap:** $190,000  
**Status:** BLOCKED — no data retrieved

## Source Status

| Tier | Source | Result |
|------|--------|--------|
| 1 | Zillapi MCP | Out of credits for this cycle |
| 2 | Camofox → Zillow path-based URL (44129) | Cloudflare "Press & Hold" captcha — page blocked |
| 2 | Camofox → Zillow (44134, 44130) | Not attempted (captcha is IP-based; subsequent navigations blocked) |
| 3 | SearXNG/agent_search | Not attempted (unreliable for Ohio cities per skill docs) |
| 4 | web_search/web_extract | Not attempted (firecrawl unavailable in cron; captcha-prone) |

## Rent Anchor (FY2025 HUD FMR)
For reference when listings become available:

| ZIP | MSA Adjustment | Est. 3BR Rent | Est. 2BR Rent |
|-----|---------------|---------------|---------------|
| 44129 | 90% of Cleveland-Elyria MSA | ~$1,398/mo | ~$988/mo |
| 44134 | 90% of Cleveland-Elyria MSA | ~$1,398/mo | ~$988/mo |
| 44130 | 90% of Cleveland-Elyria MSA | ~$1,398/mo | ~$988/mo |

⚠️ All rent figures are market-derived, NOT property-specific.

## Manual Zillow Links
Open in your own browser (not captcha-blocked for residential IPs):

- **44129 (Parma):** https://www.zillow.com/homes/for_sale/44129_rb/1-_beds/0-190000_price/pricea_sort/
- **44134 (Parma):** https://www.zillow.com/homes/for_sale/44134_rb/1-_beds/0-190000_price/pricea_sort/
- **44130 (Parma):** https://www.zillow.com/homes/for_sale/44130_rb/1-_beds/0-190000_price/pricea_sort/

## Next Steps
- Resume when Zillapi credits refresh at https://zillapi.com/app/billing
- Or run from a residential IP where Camofox can pass Cloudflare
- Or manually pull listings from the Zillow links above and feed them back in