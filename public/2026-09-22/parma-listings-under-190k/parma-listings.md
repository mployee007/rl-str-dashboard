# Parma Listings Under $190K — Zillapi Pull Failed

**Run date:** 2026-09-22
**Status:** ❌ FAILED — Zillapi credits exhausted

## Source Status

| # | Source | Tool | Result |
|---|--------|------|--------|
| 1 | Zillapi (44129) | `mcp_zillapi_search_listings` | **Out of credits** — top up at https://zillapi.com/app/billing |
| 2 | Zillapi (44134) | `mcp_zillapi_search_listings` | MCP server unreachable (15 consecutive failures) |
| 3 | Zillapi (44130) | `mcp_zillapi_search_listings` | MCP server unreachable (15 consecutive failures) |
| 4 | Web search | `web_search` | firecrawl unavailable (lazy installs disabled) |
| 5 | AgentSearch HTTP | `mcp_agent_search_http_search` | MCP server not connected |

## Target ZIPs

| ZIP | Area | Bounding Box | Price Cap |
|-----|------|-------------|-----------|
| 44129 | Parma West | -81.78,41.37,-81.68,41.42 | $190,000 |
| 44134 | Parma | -81.72,41.35,-81.65,41.40 | $190,000 |
| 44130 | Parma Heights / Middleburg Hts | -81.80,41.35,-81.73,41.41 | $190,000 |

## Direct Zillow Links (manual browser check)

- **44129:** [Zillow search](https://www.zillow.com/parma-oh-44129/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-81.78%2C%22east%22%3A-81.68%2C%22south%22%3A41.37%2C%22north%22%3A41.42%7D%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A190000%7D%2C%22isForSaleByAgent%22%3A%7B%22value%22%3Afalse%7D%2C%22isForSaleByOwner%22%3A%7B%22value%22%3Afalse%7D%2C%22isComingSoon%22%3A%7B%22value%22%3Afalse%7D%2C%22isAuction%22%3A%7B%22value%22%3Afalse%7D%2C%22isForeclosure%22%3A%7B%22value%22%3Afalse%7D%2C%22isNewConstruction%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isMapVisible%22%3Atrue%7D)
- **44134:** [Zillow search](https://www.zillow.com/parma-oh-44134/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-81.72%2C%22east%22%3A-81.65%2C%22south%22%3A41.35%2C%22north%22%3A41.40%7D%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A190000%7D%2C%22isForSaleByAgent%22%3A%7B%22value%22%3Afalse%7D%2C%22isForSaleByOwner%22%3A%7B%22value%22%3Afalse%7D%2C%22isComingSoon%22%3A%7B%22value%22%3Afalse%7D%2C%22isAuction%22%3A%7B%22value%22%3Afalse%7D%2C%22isForeclosure%22%3A%7B%22value%22%3Afalse%7D%2C%22isNewConstruction%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isMapVisible%22%3Atrue%7D)
- **44130:** [Zillow search](https://www.zillow.com/middleburg-heights-oh-44130/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-81.80%2C%22east%22%3A-81.73%2C%22south%22%3A41.35%2C%22north%22%3A41.41%7D%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A190000%7D%2C%22isForSaleByAgent%22%3A%7B%22value%22%3Afalse%7D%2C%22isForSaleByOwner%22%3A%7B%22value%22%3Afalse%7D%2C%22isComingSoon%22%3A%7B%22value%22%3Afalse%7D%2C%22isAuction%22%3A%7B%22value%22%3Afalse%7D%2C%22isForeclosure%22%3A%7B%22value%22%3Afalse%7D%2C%22isNewConstruction%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isMapVisible%22%3Atrue%7D)

## Action

Will retry on next cron cycle when Zillapi credits refresh. No fabricated listings included.