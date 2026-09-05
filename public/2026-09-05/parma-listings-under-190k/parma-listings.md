# Parma Listings Under $190K — Screen Blocked

**Run Date:** 2026-09-05  
**Status:** ❌ BLOCKED — Zillapi credits exhausted  

---

## Blocker Summary

Zillapi MCP returned **"Out of credits for this cycle"** on the first call (44129), and the MCP server became unreachable on subsequent calls. No listing data was retrieved.

| Attempt # | ZIP | Bounding Box | Result |
|-----------|-----|-------------|--------|
| 1 | 44129 | -81.78,41.37,-81.68,41.42 | Out of credits |
| 2 | 44134 | -81.72,41.35,-81.65,41.40 | MCP server unreachable |
| 3 | 44130 | -81.80,41.35,-81.73,41.41 | MCP server unreachable |

---

## Target Parameters

- **Price ceiling:** $190,000
- **Property type:** 1-4 unit homes (for-sale)
- **ZIPs:** 44129 (Parma West), 44134 (Parma East/Seven Hills), 44130 (Parma/Middleburg Heights)

---

## What You Can Do Now

### Option A: Top up Zillapi credits
Visit https://zillapi.com/app/billing and add credits. The next cron run will pick up the pull automatically.

### Option B: Manual browser search
Use these direct Zillow search links:

- **[ZIP 44129](https://www.zillow.com/homes/for_sale/44129_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%2244129%22%2C%22mapBounds%22%3A%7B%22west%22%3A-81.78%2C%22east%22%3A-81.68%2C%22south%22%3A41.37%2C%22north%22%3A41.42%7D%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A190000%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%7D)** — Parma West  
- **[ZIP 44134](https://www.zillow.com/homes/for_sale/44134_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%2244134%22%2C%22mapBounds%22%3A%7B%22west%22%3A-81.72%2C%22east%22%3A-81.65%2C%22south%22%3A41.35%2C%22north%22%3A41.40%7D%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A190000%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%7D)** — Parma East / Seven Hills  
- **[ZIP 44130](https://www.zillow.com/homes/for_sale/44130_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%2244130%22%2C%22mapBounds%22%3A%7B%22west%22%3A-81.80%2C%22east%22%3A-81.73%2C%22south%22%3A41.35%2C%22north%22%3A41.41%7D%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A190000%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%7D)** — Parma / Middleburg Heights  

---

## Status File
A persistent status file has been saved at `/opt/data/parma-pull-status.txt` with timestamps and error details.

## Next Cron Run
The automated pull will retry on the next scheduled execution. If credits are replenished before then, results will populate automatically.

---

*No listings were fabricated. All three Zillapi calls returned errors. See status file for full trace.*