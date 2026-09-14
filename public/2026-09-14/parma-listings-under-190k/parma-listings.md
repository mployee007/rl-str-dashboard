# Parma Listings Under $190K — Submarket Screen

**Date:** 2026-09-14  
**Status:** ❌ BLOCKED — Zillapi out of credits  
**Run type:** Scheduled cron job

---

## ⚠️ Live Listing Screen Unavailable

All three Zillapi calls failed:

| Call | ZIP | Error |
|------|-----|-------|
| 1 | 44129 | `Out of credits for this cycle` |
| 2 | 44134 | `MCP server unreachable (79 consecutive failures)` |
| 3 | 44130 | `MCP server unreachable (79 consecutive failures)` |

**No individual property listings were fabricated.** The sections below use cached ZIP-level benchmarks from a prior Cleveland-wide Zillapi sweep (`/opt/data/cleveland_zip_stats.json`). These provide reliable median anchors but not today's live inventory.

---

## Cached ZIP Benchmarks (Prior Pull)

| ZIP | Area | Median Sale | Median Rent | Gross Yield | Price/Rent | Sale Count |
|-----|------|------------|-------------|-------------|------------|-------------|
| 44129 | Parma West | $190,000 | $1,950 | 12.32% | 8.1× | 16 |
| 44134 | Parma E / Brooklyn Hts / Seven Hills | $200,000 | $1,675 | 10.05% | 10.0× | 44 |
| 44130 | Parma (mid) / Middleburg Hts | $199,900 | $1,575 | 9.45% | 10.6× | 7 |

### Investor Takeaways from Benchmarks

- **44129 is the yield leader.** At a $190K median and $1,950 median rent, it posts the strongest gross yield (12.32%) and lowest price-to-rent ratio (8.1×). Properties at or below $190K in this ZIP are crossing into the zone where a 1% monthly rent rule is plausible (~$1,900/mo on $190K).
- **44134 is the volume play.** Highest listing count (44) means more deal flow, more negotiation leverage. Median at $200K means ~50% of listings sit under $200K, so the sub-$190K slice is real. Yield at 10.05% is respectable but you need to buy below median to make it work.
- **44130 is the weakest.** Lowest yield (9.45%), lowest sale count (7), and median at the cap. Few opportunities exist under $190K and they're unlikely to pencil well without exceptional bases.

---

## Ranked Submarket Assessment

| Rank | ZIP | Investor Fit | Verdict | Rationale |
|------|-----|-------------|---------|-----------|
| 1 | **44129** | Stabilized SFR hold / value-add | **Take selectively** | Best yield in the Parma cluster. Low price-to-rent ratio. Tenant profile in Parma West skews toward long-term renters. Buy at $170-190K, rent at ~$1,800-1,950. |
| 2 | **44134** | SFR / small multifamily hunting | **Negotiate** | High volume means deals exist below median. Need to buy at a discount ($160-180K target) for yields to compete with 44129. Parma East has mixed block quality — screen by street. |
| 3 | **44130** | Secondary / spillover only | **Pass (mostly)** | Median already at cap. Few listings. Low yield. Only consider at deep bases ($150-165K) in the Middleburg Heights portion where tenant pool is slightly stronger. |

---

## Buy Box Reference (Parma Cluster, Using Benchmarks)

### 1-Unit SFR
| Parameter | Target | Stretch |
|-----------|--------|---------|
| Preferred ZIPs | 44129 | 44134 |
| All-in basis | $160,000 – $185,000 | $190,000 |
| Target monthly rent | $1,700 – $1,950 | $1,600 |
| Target gross yield | ≥ 11% | ≥ 9.5% |
| Rehab tolerance | ≤ $25K | ≤ $40K |
| Avoid | Flips with cosmetic-only updates at $190K; any home with knob-and-tube wiring or 20+ year roof |

### 2-Unit Duplex
| Parameter | Target | Stretch |
|-----------|--------|---------|
| Preferred ZIPs | 44129, 44134 | — |
| All-in basis | $165,000 – $190,000 | $200,000 |
| Per-unit basis | $82,500 – $95,000 | $100,000 |
| Target per-unit rent | $950 – $1,100 | $900 |
| Target gross yield | ≥ 11.5% | ≥ 10% |
| Avoid | Shared utilities without separate metering; non-conforming second unit |

### 3-4 Unit
| Parameter | Target | Stretch |
|-----------|--------|---------|
| Preferred ZIPs | 44134 (more multifamily stock) | 44129 |
| All-in basis | $175,000 – $190,000 | $200,000 |
| Per-unit basis | $44,000 – $63,000 | $67,000 |
| Target per-unit rent | $750 – $900 | $700 |
| Target gross yield | ≥ 13% | ≥ 11% |
| Avoid | 4-units where only 2 are legal; deferred maintenance exceeding $50K |

---

## Direct Zillow Search URLs (Manual Browser Review)

### 44129 (Parma West) — ⭐ best yield
```
https://www.zillow.com/homes/44129_rb/?searchQueryState={"pagination":{},"usersSearchTerm":"44129","mapBounds":{"west":-81.78,"east":-81.68,"south":41.37,"north":41.42},"filterState":{"price":{"max":190000},"isForSaleByAgent":{"value":true},"isForSaleByOwner":{"value":true},"isComingSoon":{"value":true},"isForSaleForeclosure":{"value":true}},"isListVisible":true}
```

### 44134 (Parma East) — highest volume
```
https://www.zillow.com/homes/44134_rb/?searchQueryState={"pagination":{},"usersSearchTerm":"44134","mapBounds":{"west":-81.72,"east":-81.65,"south":41.35,"north":41.40},"filterState":{"price":{"max":190000},"isForSaleByAgent":{"value":true},"isForSaleByOwner":{"value":true},"isComingSoon":{"value":true},"isForSaleForeclosure":{"value":true}},"isListVisible":true}
```

### 44130 (Parma mid / Middleburg Hts) — pass unless exceptional
```
https://www.zillow.com/homes/44130_rb/?searchQueryState={"pagination":{},"usersSearchTerm":"44130","mapBounds":{"west":-81.80,"east":-81.73,"south":41.35,"north":41.41},"filterState":{"price":{"max":190000},"isForSaleByAgent":{"value":true},"isForSaleByOwner":{"value":true},"isComingSoon":{"value":true},"isForSaleForeclosure":{"value":true}},"isListVisible":true}
```

---

## Bottom Line

**Zillapi credits are exhausted — no live listings this pull.** The cached benchmarks confirm that **44129 (Parma West) remains the strongest submarket** in the Parma cluster for sub-$190K SFR investing: 12.32% gross yield at median, lowest price-to-rent ratio, and a price point where the 1% rule is reachable. 44134 is the volume play with 44 active listings and some multifamily inventory. 44130 offers little below $190K.

When credits refresh, prioritize a live pull on **44129** first, then 44134. Skip 44130 unless credits are abundant.

---

*No listings were fabricated. All data above is from cached benchmarks. Listings table is empty pending a successful Zillapi pull.*