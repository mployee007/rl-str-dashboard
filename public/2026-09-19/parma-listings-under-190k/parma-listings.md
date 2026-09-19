# Parma-Area Listings Under $190K — Pull Failure Report

**Date:** 2026-09-19
**Run type:** Scheduled cron job
**Target ZIPs:** 44129 (Parma West), 44134 (Parma SE / Seven Hills), 44130 (Parma SW / Middleburg Hts)
**Price cap:** $190,000

---

## Pull Status: ❌ FAILED

All three bounding-box searches failed. Zillapi returned an **out of credits** error for 44129, and the MCP server was unreachable for 44134 and 44130.

### Attempted Sources

| # | Source | ZIP | Method | Result |
|---|--------|-----|--------|--------|
| 1 | Zillapi MCP | 44129 | `mcp_zillapi_search_listings` | **Out of credits** — "Top up or upgrade at https://zillapi.com/app/billing." |
| 2 | Zillapi MCP | 44134 | `mcp_zillapi_search_listings` | MCP server unreachable (115 consecutive failures) |
| 3 | Zillapi MCP | 44130 | `mcp_zillapi_search_listings` | MCP server unreachable (115 consecutive failures) |
| — | Zillow.com / Redfin / Trulia / Realtor.com | all | Web search / browser / web_extract | **Not attempted** — known captcha/PerimeterX blocks per skill instructions |

### Bounding Boxes Used

| ZIP | Bbox (west,south,east,north) |
|-----|------------------------------|
| 44129 | -81.78, 41.37, -81.68, 41.42 |
| 44134 | -81.72, 41.35, -81.65, 41.40 |
| 44130 | -81.80, 41.35, -81.73, 41.41 |

---

## Manual Fallback: Direct Zillow Search URLs

While Zillapi credits are exhausted, you can open these in a browser to view current listings:

- **[ZIP 44129 — Parma West](https://www.zillow.com/homes/for_sale/44129_rb/0-190000_price/0-471_mp/41.422902,-81.669031,41.364615,-81.797474_rect/12_zm/)** — houses under $190K
- **[ZIP 44134 — Parma SE / Seven Hills](https://www.zillow.com/homes/for_sale/44134_rb/0-190000_price/0-471_mp/41.404096,-81.644521,41.346964,-81.72482_rect/13_zm/)** — houses under $190K
- **[ZIP 44130 — Parma SW / Middleburg Hts](https://www.zillow.com/homes/for_sale/44130_rb/0-190000_price/0-471_mp/41.411908,-81.725254,41.345305,-81.80402_rect/14_zm/)** — houses under $190K

---

## Next Steps

1. **Top up Zillapi credits** at https://zillapi.com/app/billing
2. **Re-run this cron job** or manually trigger: `"Pull active for-sale house listings in ZIP 44129, 44134, 44130 under $190K"`
3. When data returns, the report will be saved to `/opt/data/outputs/YYYY-MM-DD/parma-listings-under-190k/parma-listings.md`

---

## Files Written

| File | Path |
|------|------|
| Status / error log | `/opt/data/parma-pull-status.txt` |
| This report | `/opt/data/outputs/2026-09-19/parma-listings-under-190k/parma-listings.md` |
| Quick-ref stub | `/opt/data/parma-latest-listings.md` |

*No listings were fabricated. All data is real and sourced only from tool output.*