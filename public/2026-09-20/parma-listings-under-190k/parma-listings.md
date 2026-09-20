# Parma Listings Under $190K — Pull Failed
**Run:** 2026-09-20 | **Status:** BLOCKED

## Blocker Summary

Zillapi is out of credits and all web fallbacks (Zillow.com, Redfin, web_search, web_extract) are unavailable due to captcha blocking and missing Firecrawl dependency. No live listing data was retrieved.

## Sources Tried

| # | Source | Method | Result |
|---|--------|--------|--------|
| 1 | Zillapi MCP | `search_listings` for 44129 | Out of credits |
| 2 | Zillapi MCP | `search_listings` for 44134 | MCP server unreachable (119 failures) |
| 3 | Zillapi MCP | `search_listings` for 44130 | MCP server unreachable (119 failures) |
| 4 | Web search | `web_search` (Zillow) | Firecrawl unavailable |
| 5 | Web extract | `web_extract` (Zillow) | Firecrawl unavailable |

## Direct Zillow Search URLs

- [44129 homes under $190K](https://www.zillow.com/parma-oh-44129/houses/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-81.78%2C%22east%22%3A-81.68%2C%22south%22%3A41.37%2C%22north%22%3A41.42%7D%2C%22mapZoom%22%3A13%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A190000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22sort%22%3A%7B%22value%22%3A%22priced%22%7D%7D%7D)
- [44134 homes under $190K](https://www.zillow.com/parma-oh-44134/houses/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-81.72%2C%22east%22%3A-81.65%2C%22south%22%3A41.35%2C%22north%22%3A41.40%7D%2C%22mapZoom%22%3A13%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A190000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22sort%22%3A%7B%22value%22%3A%22priced%22%7D%7D%7D)
- [44130 homes under $190K](https://www.zillow.com/parma-heights-oh-44130/houses/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-81.80%2C%22east%22%3A-81.73%2C%22south%22%3A41.35%2C%22north%22%3A41.41%7D%2C%22mapZoom%22%3A13%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A190000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22sort%22%3A%7B%22value%22%3A%22priced%22%7D%7D%7D)

## Resolution

Will retry on next scheduled run after Zillapi credits are topped up. Status file saved at `/opt/data/parma-pull-status.txt`.