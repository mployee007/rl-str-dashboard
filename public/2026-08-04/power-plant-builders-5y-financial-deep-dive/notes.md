# Notes — Power Plant Builders 5Y Financial Deep Dive

## User Context
- User asked for a deep dive on companies specializing in building out power plants.
- User explicitly requested use of the agent-search MCP server and the deep_search tool.

## Method
- Used `agent-search-http.deep_search` for discovery.
- Used `agent-search-http.read_url` for company/market pages and financial extracts.
- Used `agent-search-http.read_batch` / `search` selectively for cross-checks.
- Used Yahoo chart API in terminal for exact five-year adjusted-close return calculations.

## Selection logic
- Included only publicly traded names with meaningful power-generation / power-infrastructure exposure and full five-year stock histories.
- Excluded major private leaders like Bechtel and Kiewit from the ranked table because they do not have public equity performance.

## Observations
- Agent-search discovery quality degraded on generic EPC queries because search engines over-weighted the word `public`.
- StockAnalysis financial pages were the most reliable source for recent 5Y revenue / profit snapshots.
- CompaniesMarketCap worked well for some stock-history pages but was inconsistent on slugs; Yahoo chart API was more reliable for exact return math.
