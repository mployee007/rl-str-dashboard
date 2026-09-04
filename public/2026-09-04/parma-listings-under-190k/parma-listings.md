# Parma West Listings Under $190K — Pull Failed

**Date:** 2026-09-04
**ZIPs:** 44129, 44134, 44130
**Price Cap:** $190,000
**Status:** ❌ Zillapi credits exhausted / MCP server unreachable

---

## Blocker Summary

| Source | Attempt | Result |
|---|---|---|
| Zillapi MCP (44129) | `mcp_zillapi_search_listings` for_sale, bbox: -81.78,41.37,-81.68,41.42 | ❌ Out of credits |
| Zillapi MCP (44134) | `mcp_zillapi_search_listings` for_sale, bbox: -81.72,41.35,-81.65,41.40 | ❌ MCP server unreachable |
| Zillapi MCP (44130) | `mcp_zillapi_search_listings` for_sale, bbox: -81.80,41.35,-81.73,41.41 | ❌ MCP server unreachable |

**No live listing data was captured.** No fabricated data is presented.

---

## Direct Zillow Search URLs (Open in Your Browser)

These links will show active for-sale listings under $190K in each ZIP:

| ZIP | Direct Zillow Search |
|---|---|
| **44129** (Parma West) | https://www.zillow.com/homes/for_sale/44129_rb/0-190000_price/0-1736_mp/ |
| **44134** (Parma South) | https://www.zillow.com/homes/for_sale/44134_rb/0-190000_price/0-1736_mp/ |
| **44130** (Parma Heights) | https://www.zillow.com/homes/for_sale/44130_rb/0-190000_price/0-1736_mp/ |

---

## Next Steps

1. **Top up Zillapi credits** at https://zillapi.com/app/billing
2. **Re-run this pull** when the MCP server is back online
3. Status file saved at `/opt/data/parma-pull-status.txt` — check it on resume

---

## Context: Parma Market Anchors (from Prior Research)

For reference when the live data becomes available:

| Metric | Estimate |
|---|---|
| City median rent (Cleveland MSA) | ~$1,050/mo |
| Parma median home value | ~$175K–$190K |
| Typical SFR rent (3BR) | ~$1,200–$1,400/mo |
| Target GRM for buy-and-hold | ≤12× |
| Target gross yield | ≥8% |

At the $190K cap with ~$1,250/mo rent on a 3BR SFR, properties would need to pencil at roughly:
- **GRM:** $190K / ($1,250 × 12) = 12.7× (borderline)
- **Gross yield:** $15,000 / $190,000 = 7.9% (borderline)

The tighter the basis, the better the deal pencils in this ZIP band. The $130K–$160K range is where the math likely works best.

---

*Report will auto-resume when Zillapi credits are available. Status file: `/opt/data/parma-pull-status.txt`*