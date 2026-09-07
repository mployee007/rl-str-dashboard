# Parma Submarket Live Listing Screen — Under $190K

**Pull date:** 2026-09-07  
**ZIPs:** 44129 (Parma West), 44134 (Parma SE), 44130 (Parma SW)  
**Price cap:** $190,000  
**Status:** ❌ BLOCKED — Zillapi out of credits

---

## Blocker Report

| Source | Result |
|---|---|
| Zillapi MCP (`mcp_zillapi_search_listings`) | **Out of credits** — "Out of credits for this cycle. Top up or upgrade at https://zillapi.com/app/billing" |
| Zillapi MCP server health | **Unreachable** — 24 consecutive failures; auto-retry available after cooldown |
| Zillow.com (web) | Not attempted per skill protocol — PerimeterX/Cloudflare captcha blocks all web/browser access |
| Redfin / Trulia / Realtor.com | Not attempted per skill protocol — all known to block with captchas |

---

## Direct Zillow Search URLs (Open in Your Browser)

These URLs will show you the current listings directly on Zillow:

- **[44129 — Parma West, under $190K](https://www.zillow.com/parma-oh-44129/houses/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-81.78%2C%22south%22%3A41.37%2C%22east%22%3A-81.68%2C%22north%22%3A41.42%7D%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A190000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isMapVisible%22%3Atrue%2C%22mapZoom%22%3A13%7D)**
- **[44134 — Parma SE, under $190K](https://www.zillow.com/parma-oh-44134/houses/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-81.72%2C%22south%22%3A41.35%2C%22east%22%3A-81.65%2C%22north%22%3A41.40%7D%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A190000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isMapVisible%22%3Atrue%2C%22mapZoom%22%3A13%7D)**
- **[44130 — Parma SW, under $190K](https://www.zillow.com/parma-oh-44130/houses/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-81.80%2C%22south%22%3A41.35%2C%22east%22%3A-81.73%2C%22north%22%3A41.41%7D%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A190000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isMapVisible%22%3Atrue%2C%22mapZoom%22%3A13%7D)**

---

## Next Steps

1. **Top up Zillapi credits** at https://zillapi.com/app/billing
2. Once credits are restored and the server is reachable, re-run this pull
3. The pull script targets these bounding boxes:
   - 44129: `-81.78,41.37,-81.68,41.42`
   - 44134: `-81.72,41.35,-81.65,41.40`
   - 44130: `-81.80,41.35,-81.73,41.41`
4. Output will be saved to this directory with raw JSON stats files for follow-up queries

Status file: `/opt/data/parma-pull-status.txt`