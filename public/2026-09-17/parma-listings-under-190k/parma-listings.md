# Parma West Area — Listings Under $190K

**Pull Date:** 2026-09-17  
**Status:** ❌ BLOCKED — Zillapi credits exhausted

## What Happened

Three parallel Zillapi `search_listings` calls were dispatched for ZIPs 44129, 44134, and 44130 (max price $190K). All three failed:

| ZIP | Bounding Box | Error |
|-----|-------------|-------|
| 44129 (Parma West) | -81.78,41.37,-81.68,41.42 | **Out of credits** for this cycle |
| 44134 (Parma Central) | -81.72,41.35,-81.65,41.40 | MCP server unreachable (cascading from credit exhaustion) |
| 44130 (Parma Heights) | -81.80,41.35,-81.73,41.41 | MCP server unreachable (cascading from credit exhaustion) |

**No listings were retrieved. No data was fabricated.** The status file is at `/opt/data/parma-pull-status.txt`.

## Direct Zillow Search Links (Open in Your Browser)

These pre-filtered URLs show for-sale single-family homes / condos / townhomes under $190K in each ZIP. Open each in your own browser:

| ZIP | Neighborhood | Direct Zillow Link |
|-----|-------------|-------------------|
| **44129** | Parma West | [Zillow: 44129 ≤$190K](https://www.zillow.com/parma-oh-44129/houses/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-81.78%2C%22south%22%3A41.37%2C%22east%22%3A-81.68%2C%22north%22%3A41.42%7D%2C%22mapZoom%22%3A13%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22max%22%3A%7B%22value%22%3A190000%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A190000%7D%7D%2C%22isListVisible%22%3Atrue%7D) |
| **44134** | Parma Central | [Zillow: 44134 ≤$190K](https://www.zillow.com/parma-oh-44134/houses/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-81.72%2C%22south%22%3A41.35%2C%22east%22%3A-81.65%2C%22north%22%3A41.40%7D%2C%22mapZoom%22%3A13%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22max%22%3A%7B%22value%22%3A190000%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A190000%7D%7D%2C%22isListVisible%22%3Atrue%7D) |
| **44130** | Parma Heights | [Zillow: 44130 ≤$190K](https://www.zillow.com/parma-oh-44130/houses/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-81.80%2C%22south%22%3A41.35%2C%22east%22%3A-81.73%2C%22north%22%3A41.41%7D%2C%22mapZoom%22%3A13%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22max%22%3A%7B%22value%22%3A190000%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A190000%7D%7D%2C%22isListVisible%22%3Atrue%7D) |

## Next Steps

1. **Now:** Open the direct Zillow links above in a browser — they will show current live listings.
2. **When credits refresh:** Re-run this cron job (it will auto-pull from Zillapi and build the markdown tables with Zestimates, rent estimates, and investor verdicts).
3. **Top-up:** Visit https://zillapi.com/app/billing to add credits if you want to pull immediately.

## Files Written

| File | Content |
|------|---------|
| `/opt/data/parma-pull-status.txt` | Error log with timestamps |
| `/opt/data/outputs/2026-09-17/parma-listings-under-190k/parma-listings.md` | This report |
| `/opt/data/parma-latest-listings.md` | *Not written* (no data to populate) |