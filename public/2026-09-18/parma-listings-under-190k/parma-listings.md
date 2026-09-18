# Parma West / Parma East / Middleburg Heights — Active Listings Under $190K

> **Status: BLOCKED — 2026-09-18**
>
> This report could not be generated because Zillapi is out of credits and the MCP server is unreachable.
> No fabricated or cached listing data is available. The report will be populated on the next successful pull.

---

## Source Attempts

| # | Source | Target | Error |
|---|--------|--------|-------|
| 1 | Zillapi `search_listings` — ZIP 44129 bbox | `-81.78,41.37,-81.68,41.42` | Out of credits |
| 2 | Zillapi `search_listings` — ZIP 44134 bbox | `-81.72,41.35,-81.65,41.40` | Server unreachable (104 failures) |
| 3 | Zillapi `search_listings` — ZIP 44130 bbox | `-81.80,41.35,-81.73,41.41` | Server unreachable (104 failures) |

## Direct Zillow Search Links

These URLs will show active for-sale houses under $190K in each ZIP. Open in your browser for a live screen:

| ZIP | Area | Link |
|-----|------|------|
| **44129** | Parma West | [zillow.com/homes/for_sale/44129_house_type/0-190000_price/](https://www.zillow.com/homes/for_sale/44129_house_type/0-190000_price/0-715_mp/) |
| **44134** | Parma East | [zillow.com/homes/for_sale/44134_house_type/0-190000_price/](https://www.zillow.com/homes/for_sale/44134_house_type/0-190000_price/0-715_mp/) |
| **44130** | Middleburg Hts / SW Parma | [zillow.com/homes/for_sale/44130_house_type/0-190000_price/](https://www.zillow.com/homes/for_sale/44130_house_type/0-190000_price/0-715_mp/) |

---

## Next Steps

1. **Top up Zillapi credits** at https://zillapi.com/app/billing
2. Verify the MCP server is reachable
3. Re-run: *"Pull Parma listings under $190K again"* or wait for the next scheduled cron

---

*Report generated: 2026-09-18 | Output directory: `/opt/data/outputs/2026-09-18/parma-listings-under-190k/`*