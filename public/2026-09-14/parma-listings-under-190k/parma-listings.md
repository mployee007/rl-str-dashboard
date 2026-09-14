# Parma West Area — Active Listings Under $190K

**Pull Date:** 2026-09-14
**Status:** ❌ BLOCKED — Zillapi credits exhausted
**ZIPs:** 44129 (Parma West), 44134 (Parma NE), 44130 (Parma SE / Middleburg Hts)

---

## Blocker Details

All three Zillapi calls failed:

| ZIP | Bounding Box | Result |
|-----|-------------|--------|
| 44129 | -81.78,41.37,-81.68,41.42 | **Out of credits** |
| 44134 | -81.72,41.35,-81.65,41.40 | MCP server unreachable (76 failures) |
| 44130 | -81.80,41.35,-81.73,41.41 | MCP server unreachable (76 failures) |

**Root cause:** The Zillapi account has exhausted its credit allocation for the current billing cycle. Top up at: https://zillapi.com/app/billing

---

## Manual Fallback — Direct Zillow Search Links

Open these in a browser to manually review listings:

| ZIP | Direct Zillow Search |
|-----|----------------------|
| **44129** (Parma West) | [Zillow: 44129 under $190K](https://www.zillow.com/homes/for_sale/44129/0-190000_price/0-427_mp/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-81.78%2C%22east%22%3A-81.68%2C%22south%22%3A41.37%2C%22north%22%3A41.42%7D%2C%22mapZoom%22%3A13%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A60021%2C%22regionType%22%3A7%7D%5D%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A190000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22sort%22%3A%7B%22value%22%3A%22priced%22%7D%7D%2C%22isListVisible%22%3Atrue%7D) |
| **44134** (Parma NE) | [Zillow: 44134 under $190K](https://www.zillow.com/homes/for_sale/44134/0-190000_price/0-427_mp/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-81.72%2C%22east%22%3A-81.65%2C%22south%22%3A41.35%2C%22north%22%3A41.4%7D%2C%22mapZoom%22%3A13%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A60198%2C%22regionType%22%3A7%7D%5D%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A190000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22sort%22%3A%7B%22value%22%3A%22priced%22%7D%7D%2C%22isListVisible%22%3Atrue%7D) |
| **44130** (Parma SE / Middleburg Hts) | [Zillow: 44130 under $190K](https://www.zillow.com/homes/for_sale/44130/0-190000_price/0-427_mp/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-81.8%2C%22east%22%3A-81.73%2C%22south%22%3A41.35%2C%22north%22%3A41.41%7D%2C%22mapZoom%22%3A13%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A60253%2C%22regionType%22%3A7%7D%5D%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A190000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22sort%22%3A%7B%22value%22%3A%22priced%22%7D%7D%2C%22isListVisible%22%3Atrue%7D) |

---

## Recovery Plan

1. **Top up Zillapi credits** at https://zillapi.com/app/billing
2. **Re-run** this cron job — the pull will resume automatically from the same bounding boxes
3. **Or manually** open the Zillow links above to review listings in-browser
4. The report template is ready — data populates directly into the markdown tables once Zillapi responds

---

## Files Saved

| File | Path |
|------|------|
| This report | `/opt/data/outputs/2026-09-14/parma-listings-under-190k/parma-listings.md` |
| Status file | `/opt/data/parma-pull-status.txt` |
| Quick-ref stub | `/opt/data/parma-latest-listings.md` |

*No listings were fabricated. All rows above reflect only real tool output.*