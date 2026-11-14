# Run Log — HVAC Contractors Chicago

## 2026-11-14

### Approach
1. web_search (failed — firecrawl not installed, venv read-only)
2. Bing browser search (drifted to NJ due to server geolocation)
3. BBB.org curl → JSON-LD extraction (success)
4. Yelp, HomeAdvisor, YellowPages (all blocked by bot protection)
5. Google scrape attempts (no structured review data returned)

### Key Decision
Pivoted to BBB as primary source after all review sites and Google blocked. BBB data is high-quality (A+ ratings, verified addresses, phones) but lacks Google/Yelp review volume context.

### Deliverable
- summary.md: Ranked call list with action plan
- sources.json: Source metadata