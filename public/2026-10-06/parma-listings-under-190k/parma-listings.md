# Parma, Ohio — Listings Under $190K (44129, 44134, 44130)

**Pull Date:** 2026-10-06  
**Status:** ❌ ALL DATA SOURCES BLOCKED — NO LIVE LISTINGS RETRIEVED

---

## Source Failure Summary

| Tier | Source | Attempt | Result |
|------|--------|---------|--------|
| **1** | Zillapi MCP | `search_listings` (44129, 44134, 44130 bboxes, ≤$190K) | ❌ Monthly credits exhausted. MCP server unreachable after first call. |
| **2** | Camofox browser → Zillow | `44129_rb/` path-based URL, `pricea_sort` | ❌ Cloudflare "Press & Hold" captcha (Ref: `24d50d0f-c186-11f1-bf36-1d3950932a90`). IP-based rate limit — cannot solve. |
| **3** | SearXNG / agent_search | "Parma Ohio 44129 homes for sale under $190,000" | ❌ 8/10 results are Parma, Italy. Zero real estate listings returned. |
| **4** | web_search | site:zillow.com queries for 44129/44134/44130 | ❌ `firecrawl-py` not installed; `security.allow_lazy_installs=false`. |

**Total sources attempted:** 4  
**Live listings retrieved:** 0  

---

## Rent Baseline (for buy-box reference)

Using Cleveland-Elyria MSA FY2025 HUD Fair Market Rents (40th percentile gross rent). Parma submarket adjustment: 90% of MSA.

| Unit Size | MSA FMR | Parma Estimate (90%) |
|-----------|---------|---------------------|
| 1BR | $903 | $813 |
| 2BR | $1,098 | $988 |
| 3BR | $1,553 | $1,398 |
| 4BR | $1,810 | $1,629 |

⚠️ **All rent figures are MSA-derived estimates — NOT property-specific.** Verify against actual rent rolls and comps.

---

## Direct Zillow URLs (Manual Follow-Up)

Open these in your own browser to see current listings:

| ZIP | Direct Link |
|-----|-------------|
| **44129** (Parma West) | https://www.zillow.com/homes/for_sale/44129_rb/1-_beds/0-190000_price/pricea_sort/ |
| **44134** (Parma South) | https://www.zillow.com/homes/for_sale/44134_rb/1-_beds/0-190000_price/pricea_sort/ |
| **44130** (Parma/Brooklyn border) | https://www.zillow.com/homes/for_sale/44130_rb/1-_beds/0-190000_price/pricea_sort/ |

---

## Buy Box Framework (Parma, ≤$190K)

Using rent baselines above, here are the first-pass screening thresholds. Apply these when live data becomes available:

### 1-Unit SFR
| Metric | Threshold |
|--------|-----------|
| Max all-in basis | $190,000 |
| Target all-in basis | $140,000 – $165,000 |
| Target 3BR monthly rent | $1,398 (90% MSA FMR) |
| Target gross yield | 8.9% – 10.2% (at target basis) |
| GRM target | ≤ 12 |
| Avoid | 1BR under $813/mo expected rent; anything over $175K without rent upside |

### 2-Unit (Duplex)
| Metric | Threshold |
|--------|-----------|
| Max all-in basis | $190,000 |
| Target all-in basis | $150,000 – $175,000 |
| Target monthly rent (combined) | $1,800 – $2,100 |
| Target gross yield | ≥ 11% |
| Per-unit basis | $75K – $87.5K |
| Avoid | Single meter; unpermitted second unit; combined rent below $1,500 |

### 3-4 Unit
| Metric | Threshold |
|--------|-----------|
| Max all-in basis | $190,000 |
| Target all-in basis | $160,000 – $190,000 |
| Target monthly rent (combined) | $2,700 – $3,600 |
| Target gross yield | ≥ 15% |
| Per-unit basis | $40K – $63K |
| Avoid | Shared utilities; deferred systems capex; vacant units at purchase |

---

## Recommendation

**No actionable leads available this pull.** All four data tiers are blocked. The Parma ZIPs (44129/44134/44130) are the right hunting ground for sub-$190K 1-4 unit plays, with 3BR FMR of ~$1,398/mo providing a credible rent anchor for underwriting. But live listing data is unavailable.

**Next steps:**
1. Wait for Zillapi monthly credits to refresh and re-run the `search_listings` calls
2. Or manually browse the direct Zillow URLs above and feed listing data back
3. Camofox IP-based rate limiting may clear after a cooldown period — retry in 24+ hours

---

*Generated: 2026-10-06 by Hermes Agent (Loki profile) — real-estate-submarket-screening skill, cron job*