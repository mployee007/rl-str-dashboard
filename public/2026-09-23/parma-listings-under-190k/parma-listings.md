# Parma Listings Under $190K — FAILED PULL
**Date:** 2026-09-23
**Status:** ❌ BLOCKED — Zillapi credits exhausted

## What Happened
Attempted to pull active for-sale listings (max $190K) for all three target ZIPs. Zillapi returned "Out of credits for this cycle" on the first call, and the MCP server became unreachable on subsequent attempts.

## Target ZIPs
| ZIP | Neighborhood | Bounding Box | Result |
|-----|-------------|--------------|--------|
| 44129 | Parma West | -81.78,41.37,-81.68,41.42 | ❌ Out of credits |
| 44134 | Parma South | -81.72,41.35,-81.65,41.40 | ❌ Server unreachable |
| 44130 | Middleburg Hts/Parma Hts | -81.80,41.35,-81.73,41.41 | ❌ Server unreachable |

## Resolution Required
- Top up Zillapi credits: https://zillapi.com/app/billing
- Re-trigger this pull after credits are restored
- Alternatively, use the direct Zillow search links in `/opt/data/parma-pull-status.txt`

## Sources Tried
| Source | Method | Result |
|--------|--------|--------|
| Zillapi MCP | `mcp_zillapi_search_listings` | Out of credits |
| Zillapi MCP (retry) | `mcp_zillapi_search_listings` | Server unreachable |
| Zillow.com | Not attempted — blocked by PerimeterX/Cloudflare per known limitations |
| Redfin | Not attempted — blocked by captcha per known limitations |
| web_search | Not attempted — does not return structured listing data |

*No listings were fabricated. All three ZIP pulls are pending credit top-up.*