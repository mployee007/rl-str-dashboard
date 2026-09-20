# Parma West Area — Active Listings Under $190K

**Pull date:** Sunday, September 20, 2026
**ZIPs:** 44129 (Parma West), 44134, 44130
**Max Price:** $190,000

---

## ⛔ STATUS: BLOCKED — Zillapi Out of Credits

All three Zillapi `search_listings` calls failed. The account has exhausted its credit cycle.

| Source | ZIP | Result |
|--------|-----|--------|
| Zillapi MCP | 44129 | ❌ Out of credits |
| Zillapi MCP | 44134 | ❌ MCP server unreachable (125 failures) |
| Zillapi MCP | 44130 | ❌ MCP server unreachable (125 failures) |

**Web fallback assessment:** Not attempted. Zillow.com, Redfin, Trulia, Realtor.com, and Homes.com all block programmatic access with PerimeterX/Cloudflare captchas. `web_search` and `web_extract` fail consistently on listing data for the same reason. Per the `real-estate-submarket-screening` skill, looping on web alternatives only wastes turns.

---

## Manual Search Links

The user can open these in a browser to screen directly:

- **[ZIP 44129 — Zillow: Homes Under $190K](https://www.zillow.com/parma-oh-44129/houses/0-190000_att/)**
- **[ZIP 44134 — Zillow: Homes Under $190K](https://www.zillow.com/parma-oh-44134/houses/0-190000_att/)**
- **[ZIP 44130 — Zillow: Homes Under $190K](https://www.zillow.com/parma-oh-44130/houses/0-190000_att/)**

---

## Next Steps

1. Top up Zillapi credits at https://zillapi.com/app/billing
2. Re-run this job (same instruction) — it will pull all three ZIPs, compute medians, save raw JSON, and produce investor verdicts
3. I'll save `parma_zip_stats.json` and the full listing dump for follow-up queries