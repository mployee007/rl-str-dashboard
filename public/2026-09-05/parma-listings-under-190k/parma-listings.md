# Parma Listings Under $190K — Pull Failed

**Date:** 2026-09-05  
**Time:** ~UTC (cron execution)  
**Status:** BLOCKED — Zillapi out of credits

## Error Details

| Source | ZIP | Call | Result |
|--------|-----|------|--------|
| Zillapi MCP | 44129 | `search_listings(bbox=-81.78,41.37,-81.68,41.42, status=for_sale, price_max=190000)` | ❌ Out of credits |
| Zillapi MCP | 44134 | `search_listings(bbox=-81.72,41.35,-81.65,41.40, status=for_sale, price_max=190000)` | ❌ MCP server unreachable (9 consecutive failures) |
| Zillapi MCP | 44130 | `search_listings(bbox=-81.80,41.35,-81.73,41.41, status=for_sale, price_max=190000)` | ❌ MCP server unreachable (9 consecutive failures) |

All three pulls failed. No listings were fabricated.

## Direct Zillow Search URLs (open in browser)

| ZIP | Neighborhood | Direct Zillow Link |
|-----|-------------|-------------------|
| **44129** | Parma West | https://www.zillow.com/homes/for_sale/44129_rb/0-190000_price/0-1000000_mp/ |
| **44134** | Parma / Seven Hills | https://www.zillow.com/homes/for_sale/44134_rb/0-190000_price/0-1000000_mp/ |
| **44130** | Middleburg Heights / Parma Hts | https://www.zillow.com/homes/for_sale/44130_rb/0-190000_price/0-1000000_mp/ |

## Next Steps

1. **Top up Zillapi credits** at https://zillapi.com/app/billing
2. **Re-run this cron job** after credits refresh
3. This status file will be overwritten on next successful pull

## Sources Tried

| Source | Method | Result |
|--------|--------|--------|
| Zillapi MCP | `mcp_zillapi_search_listings` | Out of credits / unreachable |
| Zillow.com | Not attempted (known PerimeterX/Cloudflare captcha block) | N/A |
| Redfin | Not attempted (known captcha block) | N/A |
| Realtor.com | Not attempted (known captcha block) | N/A |
| Trulia | Not attempted (known captcha block) | N/A |
| web_search | Not attempted (known failure per skill) | N/A |
| web_extract | Not attempted (known failure per skill) | N/A |

*Per real-estate-submarket-screening skill: "Do not waste turns trying Zillow.com, Redfin, Trulia, Realtor.com, or other listing sites — they all block with captchas. Use Zillapi MCP exclusively."*