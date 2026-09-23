# Parma Area Listings Under $190K — Pull Blocked

**Date:** 2026-09-23  
**Status:** ❌ Zillapi credits exhausted — no live data pulled  

---

## What We Tried

| Source | Method | Result |
|---|---|---|
| Zillapi MCP (`mcp_zillapi_search_listings`) | Three bounding-box calls (44129, 44134, 44130) | ❌ Out of credits |
| Zillow.com | N/A — skipped per skill guidance | 🚫 PerimeterX/Cloudflare captcha wall |
| Redfin, Trulia, Realtor.com, Movoto | N/A — skipped per skill guidance | 🚫 All known to block automated access |

## Direct Zillow Search URLs (Open in Your Browser)

- **[ZIP 44129 — Parma West, max $190K](https://www.zillow.com/parma-oh-44129/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-81.78%2C%22south%22%3A41.37%2C%22east%22%3A-81.68%2C%22north%22%3A41.42%7D%2C%22mapZoom%22%3A13%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22price%22%3A%7B%22max%22%3A190000%7D%7D%2C%22isListVisible%22%3Atrue%7D)**
- **[ZIP 44134 — Parma SE / Seven Hills area, max $190K](https://www.zillow.com/parma-oh-44134/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-81.72%2C%22south%22%3A41.35%2C%22east%22%3A-81.65%2C%22north%22%3A41.40%7D%2C%22mapZoom%22%3A13%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22price%22%3A%7B%22max%22%3A190000%7D%7D%2C%22isListVisible%22%3Atrue%7D)**
- **[ZIP 44130 — Middleburg Heights / Parma Hts, max $190K](https://www.zillow.com/middleburg-heights-oh-44130/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-81.80%2C%22south%22%3A41.35%2C%22east%22%3A-81.73%2C%22north%22%3A41.41%7D%2C%22mapZoom%22%3A13%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22price%22%3A%7B%22max%22%3A190000%7D%7D%2C%22isListVisible%22%3Atrue%7D)**

## Next Step

Credits must be topped up at https://zillapi.com/app/billing. This cron job will retry on its next cycle. The status file is at:

```
/opt/data/parma-pull-status.txt
```

The full report path (empty pending pull) is at:

```
/opt/data/outputs/2026-09-23/parma-listings-under-190k/parma-listings.md
```