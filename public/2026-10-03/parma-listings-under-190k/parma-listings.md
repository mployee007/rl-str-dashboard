# Parma Sub-$190K Listing Screen — BLOCKED

**Date:** 2026-10-03  
**ZIPs:** 44129 (Parma West), 44134 (Parma SE), 44130 (Parma SW)  
**Price cap:** $190,000  
**Status:** ❌ All data sources exhausted — zero listings retrieved

---

## Source Exhaustion Table

| Tier | Source | Status | Detail |
|------|--------|--------|--------|
| 1 | **Zillapi MCP** | ❌ Out of credits | First call: "Out of credits for this cycle." Calls 2-3: MCP server unreachable (62+ consecutive failures). |
| 2 | **Camofox browser → Zillow** | ❌ Cloudflare captcha | "Press & Hold" challenge on first navigation (44129). Cannot solve — HTTP 422. IP-based rate limiting. |
| 3 | **SearXNG (agent_search)** | ❌ Wrong geography | Bing returned Parma, Italy results. site:zillow.com filter returned zero listing results. All other engines down (Brave, DDG, Startpage — captchas/rate limits). |
| 4 | **web_search / web_extract** | ❌ firecrawl missing | `firecrawl-py` unavailable; `security.allow_lazy_installs=false` in cron prevents install. |

---

## Direct Zillow URLs (Manual Follow-Up)

These are path-based URLs with `pricea_sort` (ascending price) — paste directly into a browser:

| ZIP | Neighborhood | URL |
|-----|-------------|-----|
| **44129** | Parma West | [Zillow →](https://www.zillow.com/homes/for_sale/44129_rb/1-_beds/0-190000_price/pricea_sort/) |
| **44134** | Parma SE | [Zillow →](https://www.zillow.com/homes/for_sale/44134_rb/1-_beds/0-190000_price/pricea_sort/) |
| **44130** | Parma SW | [Zillow →](https://www.zillow.com/homes/for_sale/44130_rb/1-_beds/0-190000_price/pricea_sort/) |

---

## Rent Anchor (For Verdict Reference)

Per the skill's hardcoded FY2025 HUD FMR baselines — **Cleveland-Elyria MSA**:

| Unit Size | MSA FMR | Parma Adj (90%) |
|-----------|---------|-----------------|
| Studio | $824 | $742 |
| 1BR | $903 | $813 |
| 2BR | $1,098 | $988 |
| 3BR | $1,553 | $1,398 |
| 4BR | $1,810 | $1,629 |

**Buy-box quick reference at $190K cap and 90% FMR:**

| Property Type | Target GRM | Implied Rent Needed | Verdict Threshold |
|---------------|-----------|---------------------|-------------------|
| 2BR SFR (2BR FMR $988) | 12× | $190K ÷ $988 × 12 = GRM 16.0 | Negotiate — GRM > 14 |
| 3BR SFR (3BR FMR $1,398) | 12× | $190K ÷ $1,398 × 12 = GRM 11.3 | Take selectively — GRM < 12 |
| Duplex (2× 2BR $1,976) | 10× | $190K ÷ $1,976 × 12 = GRM 8.0 | Take — strong cash flow |
| 3-4 unit | 8-10× | Depends on unit mix | Take if per-unit basis < $50K |

⚠️ **NOTE:** All rent figures are market-derived (HUD FMR × Parma adjustment), NOT property-specific. Actual rentZestimates were unavailable from all data sources. Diligence individual properties before underwriting.

---

## Next Steps

1. **Refresh Zillapi credits** at [zillapi.com/app/billing](https://zillapi.com/app/billing) — re-run this cron job or manually trigger the pull.
2. **Manual browser pull:** Open the direct Zillow URLs above in a non-Cloudflare-flagged browser session.
3. **Camofox IP rotation:** If rotating IPs is possible, a fresh IP may bypass the Zillow captcha for one navigation.
4. **Resume when credits refresh:** This cron job will re-attempt on next schedule. The skill workflow is fully scripted — it will auto-detect credit availability and route accordingly.

---

## Files Saved

- `/opt/data/parma-pull-status.txt` — error summary
- `/opt/data/outputs/2026-10-03/parma-listings-under-190k/parma-listings.md` — this report
- `/opt/data/parma-latest-listings.md` — NOT written (no listing data to populate)