# Parma, OH — Active Listings Under $190K

**Date:** 2026-10-06  
**Status:** ⛔ BLOCKED — All data sources exhausted  
**Target ZIPs:** 44129 (Parma West), 44134 (Parma SE), 44130 (Parma/Brooklyn border)

---

## Source Status

| Source | Result | Detail |
|--------|--------|--------|
| **Zillapi MCP** | ❌ Out of credits | "This month's credits are used up." Server unreachable after first credit-exhaustion response. |
| **Camofox → Zillow** | ❌ Captcha | Cloudflare "Press & Hold" on first navigation (Ref: 47e84903). IP rate-limited — cannot solve. |
| **SearXNG** | ⛔ Skipped | "Parma" → Parma, Italy results. Unusable for US listings. |
| **web_search / web_extract** | ⛔ Skipped | firecrawl-py not installed; cannot install in cron/locked-venv. |

---

## Manual Follow-Up URLs

Open these in a browser to screen listings directly:

| ZIP | Zillow Search URL |
|-----|-------------------|
| **44129** (Parma West) | [Zillow →](https://www.zillow.com/homes/for_sale/44129_rb/1-_beds/0-190000_price/pricea_sort/) |
| **44134** (Parma SE) | [Zillow →](https://www.zillow.com/homes/for_sale/44134_rb/1-_beds/0-190000_price/pricea_sort/) |
| **44130** (Parma/Brooklyn) | [Zillow →](https://www.zillow.com/homes/for_sale/44130_rb/1-_beds/0-190000_price/pricea_sort/) |

---

## Rent Anchors (for underwriting when listings are available)

**Cleveland-Elyria MSA FY2025 FMR (40th percentile):**

| Unit | MSA FMR | Parma Adj (90%) |
|------|--------:|----------------:|
| 2BR | $1,098 | $988 |
| 3BR | $1,553 | $1,398 |
| 4BR | $1,810 | $1,629 |

⚠️ All rent figures are **market-derived, NOT property-specific**. Verify against actual rent comps.

---

## Parma Submarket Context (from prior screening)

- **44129** — Classic Parma SFR; 1950s-60s bungalows, stable blocks, strong rental demand. Best all-around submarket.
- **44134** — Value-add zone; more mixed block quality, lower basis opportunities, watch block-by-block.
- **44130** — Southern Parma / Brooklyn border; mixed condo/SFR inventory, HOA-heavy in spots.

---

## Next Steps

1. When Zillapi credits refresh (monthly), re-run automated pull.
2. Open the manual URLs above to screen listings in the meantime.
3. Apply these verdict heuristics to any listings found:
   - **TAKE:** GRM < 10 (i.e., $140K purchase / $1,400/mo rent), or $/sqft < $90
   - **NEGOTIATE:** GRM 10–12, price cut > 8%, DOM > 30 days
   - **PASS:** GRM > 14, tax gap > 40%, 2BR at > $180K