# Decisions — agent-search-mcp-test-2

## 2026-08-04

### Decision: Use Zillow/Zillapi-first with web fallback
- **Context:** Need furnished rental listings with age-on-market filtering across many cities.
- **Options considered:** Zillapi only, web-only, mixed-source search.
- **Decision:** Use mixed-source approach with Zillapi/web/craigslist fallbacks.
- **Consequence:** Better coverage with explicit sourcing.

### Decision: Keep only fully evidenced matches in final table
- **Context:** Many candidates met price/type but lacked furnished or age proof.
- **Decision:** Exclude partials from verified-match table; list them separately.
- **Consequence:** Lower count, higher confidence.
