# Parma (44129, 44134, 44130) — Listings Under $190K

**Pull Date:** 2026-09-11  
**Status:** ❌ FAILED — Zillapi credits exhausted

---

## Blocker Summary

| Source | Attempted? | Result |
|--------|-----------|--------|
| Zillapi (44129) | ✅ | "Out of credits for this cycle" |
| Zillapi (44134) | ✅ | "MCP server unreachable (57 consecutive failures)" |
| Zillapi (44130) | ✅ | "MCP server unreachable (57 consecutive failures)" |
| Zillow.com / Redfin / Trulia | ⛔ Skipped | All block with PerimeterX/Cloudflare captchas per skill playbook |
| web_search / web_extract | ⛔ Skipped | Known to fail on listing sites per skill playbook |

---

## Manual Fallback URLs

Open these in your own browser to see current listings:

- **44129 (Parma West):** [Zillow search](https://www.zillow.com/parma-oh-44129/houses/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%2244129%22%2C%22mapBounds%22%3A%7B%22west%22%3A-81.78%2C%22east%22%3A-81.68%2C%22south%22%3A41.37%2C%22north%22%3A41.42%7D%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A190000%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%7D)
- **44134 (Parma South):** [Zillow search](https://www.zillow.com/parma-oh-44134/houses/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%2244134%22%2C%22mapBounds%22%3A%7B%22west%22%3A-81.72%2C%22east%22%3A-81.65%2C%22south%22%3A41.35%2C%22north%22%3A41.40%7D%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A190000%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%7D)
- **44130 (Parma Heights / Middleburg):** [Zillow search](https://www.zillow.com/parma-oh-44130/houses/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%2244130%22%2C%22mapBounds%22%3A%7B%22west%22%3A-81.80%2C%22east%22%3A-81.73%2C%22south%22%3A41.35%2C%22north%22%3A41.41%7D%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A190000%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%7D)

---

## Resolution

1. **Top up Zillapi credits** at https://zillapi.com/app/billing
2. **Re-run** this cron job or trigger manually
3. No listings were fabricated — this report reflects a genuine credit-outage, not a zero-result market condition

---

*Status file: `/opt/data/parma-pull-status.txt`*  
*Report: `/opt/data/outputs/2026-09-11/parma-listings-under-190k/parma-listings.md`*