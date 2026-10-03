# Parma Listings Screen — Under $190K

**Date:** 2026-10-03 (automated cron)
**Target ZIPs:** 44129, 44134, 44130
**Status:** ⚠️ BLOCKED — No live listing data available

---

## Data Source Status

| Source | Result |
|--------|--------|
| **Zillapi MCP** (`mcp_zillapi_search_listings`) | ❌ Out of credits. "Out of credits for this cycle. Top up or upgrade at https://zillapi.com/app/billing" |
| **Zillapi MCP** (subsequent calls) | ❌ MCP server unreachable (34 consecutive failures after credit exhaustion) |
| **Camofox → Zillow search results** | ❌ IP rate-limited. Cloudflare "Press & Hold" captcha on first navigation to `https://www.zillow.com/homes/for_sale/44129_rb/1-_beds/0-190000_price/pricea_sort/`. Reference ID `33d126bd-bf70-11f1-8dd7-962db5c62b8f`. Camofox cannot solve Press & Hold challenges. |
| **SearXNG / agent_search** | ⛔ Not attempted — unreliable for Ohio cities with European namesakes; listing sites all captcha-blocked |
| **web_search / web_extract** | ⛔ Not attempted — requires firecrawl (unavailable in cron) |

**All three tiers exhausted.** Resuming requires: either Zillapi credit top-up, a fresh IP for Camofox, or manual browser lookups.

---

## Market Context: Cleveland-Elyria MSA → Parma Submarket

### Rent Anchors (FY2025 HUD Fair Market Rents — 40th percentile gross rent)

Cleveland-Elyria MSA baseline with Parma adjustment (90% of MSA):

| Unit | MSA FMR | Parma Est. (90%) |
|------|---------|-------------------|
| Studio | $824 | $742 |
| 1BR | $903 | $813 |
| 2BR | $1,098 | $988 |
| **3BR** | **$1,553** | **$1,398** |
| 4BR | $1,810 | $1,629 |

⚠️ Market-derived — NOT property-specific. FMRs are 40th percentile gross rents; actual property-level rents vary by condition, block quality, and unit mix.

---

## Buy Box Derivation (Under $190K Cap)

Using the 3BR Parma-adjusted FMR of $1,398/mo as the benchmark:

### Target Metrics

| Metric | Value |
|--------|-------|
| **Annual gross rent (3BR)** | $16,776 |
| **Target GRM** | 8–10 (Midwest working-class suburb) |
| **Target basis (GRM 8)** | ~$134,000 |
| **Stretch basis (GRM 10)** | ~$168,000 |
| **Target gross yield** | 10%–12.5% |
| **Cash buyer target** | GRM ≤ 8 (≈ $134K on 3BR) |
| **Financed target** | GRM ≤ 10 (≈ $168K on 3BR) |

### By Property Type

| Type | MSA Rent Est. (Parma adj.) | Target Basis (GRM 8) | Stretch Basis (GRM 10) | Gross Yield at $190K |
|------|---------------------------|----------------------|------------------------|------------------------|
| 1BR | $813/mo | ~$78,000 | ~$97,500 | 5.1% |
| 2BR | $988/mo | ~$95,000 | ~$118,500 | 6.2% |
| 3BR | $1,398/mo | ~$134,000 | ~$168,000 | 8.8% |
| 4BR | $1,629/mo | ~$156,000 | ~$195,000 | 10.3% |

**Key takeaway:** At the $190K cap, only 3BR and 4BR properties approach viable gross yields. 1BR and 2BR at $190K are almost certainly **pass** unless rents significantly exceed FMR estimates (unlikely for Parma).

---

## ZIP-Level Direct Zillow URLs

Open these in your own browser to see live listings:

### 44129 — Parma West
**URL:** https://www.zillow.com/homes/for_sale/44129_rb/1-_beds/0-190000_price/pricea_sort/

### 44134 — Parma South
**URL:** https://www.zillow.com/homes/for_sale/44134_rb/1-_beds/0-190000_price/pricea_sort/

### 44130 — Parma Heights / Middleburg Heights area
**URL:** https://www.zillow.com/homes/for_sale/44130_rb/1-_beds/0-190000_price/pricea_sort/

---

## Submarket Ranking (from prior thesis context)

| ZIP | Area | Investor Fit | Verdict |
|-----|------|-------------|---------|
| **44129** | Parma West | Stabilized SFR hold; older housing stock (1940s-60s), decent block quality, strong rental demand | **Negotiate selectively** — target GRM ≤ 10 |
| **44134** | Parma South | Value-add SFR; more entry-level price points, higher rehab likelihood, block-by-block variability | **Take selectively** — best chance at sub-$150K entries |
| **44130** | Parma Hts / Midburg Hts fringe | Mixed; stretches into more commercial corridors, smaller housing stock | **Negotiate** — verify block quality before bidding |

---

## Verdict Logic (for manual review)

When looking at live listings, apply these filters:

- **Pass** immediately if:
  - GRM > 12 at asking price (e.g., 3BR at $190K renting < $1,320/mo)
  - Major systems deferred (roof, HVAC, foundation) with no rehab discount
  - Block has >2 visibly distressed properties within 3 doors
  - Price cut > 60 days without contract — market is telling you something

- **Negotiate** if:
  - GRM 10–12 and property is in solid mechanical condition
  - Recent price cut and DOM > 30 days
  - Occupied with below-market tenant (can reposition at turnover)

- **Take** if:
  - GRM ≤ 8 with verified rents (rare at current pricing)
  - Off-market or pre-MLS at wholesale pricing
  - Distressed property with clear rehab path and 70% ARV basis

---

## Next Steps

1. **Top up Zillapi credits** at https://zillapi.com/app/billing and re-run the cron job
2. **Or use a fresh IP** for Camofox — the current IP is rate-limited by Cloudflare
3. **Manual review** — open the direct Zillow URLs above and apply the buy-box filters
4. **Re-run** when either data path is restored: `parma-listings-under-190k` cron

---

*Report generated by Hermes Agent (Loki profile) — 2026-10-03*
*Rent anchors: U.S. HUD FY2025 Fair Market Rents, Cleveland-Elyria MSA*