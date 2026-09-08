# Parma Listings Under $190K — 2026-09-08
**Status:** ❌ BLOCKED — Zillapi credits exhausted

No live listings could be retrieved. The Zillapi account is out of credits for this billing cycle and the MCP server was also unreachable for two of the three ZIP code queries.

## ZIP Codes Targeted
| ZIP | Area | Price Cap | Status |
|-----|------|-----------|--------|
| 44129 | Parma West | ≤$190K | Out of credits |
| 44134 | Parma South | ≤$190K | Server unreachable |
| 44130 | Parma/Middleburg | ≤$190K | Server unreachable |

## What Was Attempted
- Three parallel `mcp_zillapi_search_listings` calls, one per ZIP bounding box, all with `price_max=190000`, `beds_min=1`, `status=for_sale`
- Zillapi returned "Out of credits for this cycle" for 44129, and the MCP server was unreachable for 44134 and 44130 after multiple attempts

## Fallback Sources Considered & Rejected
Per the `real-estate-submarket-screening` skill, all web-based listing sites (Zillow.com, Redfin, Trulia, Realtor.com, Homes.com, Movoto) are blocked by PerimeterX/Cloudflare captchas in this environment. `web_search` and `web_extract` are known to fail on these domains. Per the skill, I am not wasting turns attempting them.

## Manual Browser Fallback URLs
The user can open these in their own browser:
- **[44129](https://www.zillow.com/homes/for_sale/Parma-OH-44129/house_type/190000-_max/1-_beds/)**
- **[44134](https://www.zillow.com/homes/for_sale/Parma-OH-44134/house_type/190000-_max/1-_beds/)**
- **[44130](https://www.zillow.com/homes/for_sale/Parma-OH-44130/house_type/190000-_max/1-_beds/)**

## Resolution
- Top up credits at https://zillapi.com/app/billing and re-run
- OR use the Zillow manual links above to screen listings in a browser
- Status file saved at `/opt/data/parma-pull-status.txt`