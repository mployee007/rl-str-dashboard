# Parma-Area Listings Under $190K — Pull Report

**Generated:** 2026-09-12T04:11:36Z  
**Status:** ⚠️ ZILLAPI OUT OF CREDITS — 3rd consecutive failed attempt  
**Prior attempts:** 2026-09-06, 2026-09-09  
**Next refresh:** After Zillapi credit cycle resets (top up at https://zillapi.com/app/billing)

---

## What Was Requested

Active for-sale house listings (1–4 units) under **$190,000** in three ZIP codes:

| ZIP | Area | Bounding Box |
|-----|------|-------------|
| 44129 | Parma West | -81.78, 41.37, -81.68, 41.42 |
| 44134 | Parma South / Seven Hills | -81.72, 41.35, -81.65, 41.40 |
| 44130 | Middleburg Heights / Parma SW | -81.80, 41.35, -81.73, 41.41 |

---

## Blockers

| # | Source | Target | Result |
|---|--------|--------|--------|
| 1 | Zillapi MCP (`search_listings`, for_sale, max=$190K) | 44129 | **Out of credits** — "Top up or upgrade at https://zillapi.com/app/billing" |
| 2 | Zillapi MCP | 44134 | MCP server unreachable (59 consecutive failures, cascading from credit exhaustion) |
| 3 | Zillapi MCP | 44130 | MCP server unreachable (59 consecutive failures, cascading from credit exhaustion) |
| 4 | Zillow.com / Redfin / Trulia | — | Not attempted — known PerimeterX/Cloudflare captcha wall per skill protocol |

---

## Direct Zillow Links — Open in Your Browser

These URLs are pre-filtered (max $190K, houses only, sorted by relevance):

### 44129 — Parma West
🔗 [Zillow: 44129 homes under $190K](https://www.zillow.com/homes/for_sale/44129_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-81.78%2C%22south%22%3A41.37%2C%22east%22%3A-81.68%2C%22north%22%3A41.42%7D%2C%22mapZoom%22%3A14%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22price%22%3A%7B%22max%22%3A190000%7D%2C%22mp%22%3A%7B%22min%22%3A1%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22sch%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D)

### 44134 — Parma South / Seven Hills
🔗 [Zillow: 44134 homes under $190K](https://www.zillow.com/homes/for_sale/44134_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-81.72%2C%22south%22%3A41.35%2C%22east%22%3A-81.65%2C%22north%22%3A41.40%7D%2C%22mapZoom%22%3A14%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22price%22%3A%7B%22max%22%3A190000%7D%2C%22mp%22%3A%7B%22min%22%3A1%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22sch%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D)

### 44130 — Middleburg Heights / Parma SW
🔗 [Zillow: 44130 homes under $190K](https://www.zillow.com/homes/for_sale/44130_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-81.80%2C%22south%22%3A41.35%2C%22east%22%3A-81.73%2C%22north%22%3A41.41%7D%2C%22mapZoom%22%3A14%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22price%22%3A%7B%22max%22%3A190000%7D%2C%22mp%22%3A%7B%22min%22%3A1%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22sch%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D)

---

## Saved Files

| File | Path | Purpose |
|------|------|---------|
| Pull status | `/opt/data/parma-pull-status.txt` | Timestamped error log |
| This report | `/opt/data/outputs/2026-09-12/parma-listings-under-190k/parma-listings.md` | Full pull report |
| Quick-ref stub | `/opt/data/parma-latest-listings.md` | Stub — populated when live data arrives |

---

## Historical Context

This cron job has now attempted on 3 dates (Sep 6, Sep 9, Sep 12) with the same result. The Zillapi credit pool has been exhausted across all runs. No cached listing data exists from prior successful pulls — the earliest attempt also hit the credit wall.

**Zillapi credit budget note:** Each `search_listings` call deducts credits. The real-estate-submarket-screening skill budgets 2-3 calls per city. With 3 calls per run × 3 attempts, that's 9 credit-consuming calls attempted across this cycle. None succeeded.

---

## Action Required

| Priority | Action |
|----------|--------|
| 🔴 **Immediate** | Top up Zillapi credits at https://zillapi.com/app/billing |
| 🟡 **After top-up** | Re-run this cron job — it will auto-populate listing tables with investor verdicts |
| 🟢 **Right now** | Use the Zillow direct links above to manually screen listings in a browser |

### Auto-Resume Plan
When credits are restored, this job will:
- Pull all three ZIP codes (3 `search_listings` calls for_sale)
- Extract zpids and look up rent Zestimates
- Build markdown tables sorted by price with investor verdicts (take / negotiate / pass)
- Save raw JSON dumps (`parma_44129_raw.json`, etc.) for follow-up queries
- Update `parma-latest-listings.md` with the quick-ref table

---

*Report generated by Hermes Agent — Loki profile — real-estate-submarket-screening skill*