# Parma Area Listings Under $190K — Pull Failed

**Date:** 2026-09-18  
**Status:** ❌ BLOCKED — Zillapi credits exhausted

## What was attempted

| ZIP | Bounding Box | Status | Error |
|-----|-------------|--------|-------|
| 44129 (Parma West) | -81.78,41.37,-81.68,41.42 | ❌ | Out of credits for this cycle |
| 44134 (Parma South) | -81.72,41.35,-81.65,41.40 | ❌ | MCP server unreachable (107 failures) |
| 44130 (Parma Heights) | -81.80,41.35,-81.73,41.41 | ❌ | MCP server unreachable (107 failures) |

## Why no web fallback

Per the real-estate-submarket-screening skill: all major listing sites (Zillow.com, Redfin, Trulia, Realtor.com, Homes.com, Movoto) block automated access with PerimeterX/Cloudflare captchas. `web_search` and `web_extract` will not return usable listing data. Attempting them wastes turns without producing results.

## What you can do right now

Open these direct Zillow search URLs in your browser:

- **44129** — [Zillow: 44129 under $190K](https://www.zillow.com/parma-oh-44129/houses/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-81.78%2C%22south%22%3A41.37%2C%22east%22%3A-81.68%2C%22north%22%3A41.42%7D%2C%22mapZoom%22%3A13%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A190000%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%7D)

- **44134** — [Zillow: 44134 under $190K](https://www.zillow.com/parma-oh-44134/houses/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-81.72%2C%22south%22%3A41.35%2C%22east%22%3A-81.65%2C%22north%22%3A41.40%7D%2C%22mapZoom%22%3A13%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A190000%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%7D)

- **44130** — [Zillow: 44130 under $190K](https://www.zillow.com/parma-oh-44130/houses/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-81.80%2C%22south%22%3A41.35%2C%22east%22%3A-81.73%2C%22north%22%3A41.41%7D%2C%22mapZoom%22%3A13%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A190000%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%7D)

## Next step

Resume when Zillapi credits refresh: top up at https://zillapi.com/app/billing, then re-run this job. Raw JSON dumps will be saved alongside this report so follow-up queries (e.g., "show me properties under $190K in ZIP 44129") can be answered from cache.