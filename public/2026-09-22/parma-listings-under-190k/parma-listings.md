# Parma-Area Listings Under $190K — Pull Blocked

**Date:** 2026-09-22 (retry #2 same day)  
**Status:** ❌ Zillapi out of credits — no live data pulled

---

## Targeted ZIP Codes

| ZIP | Area | Bounding Box | Status |
|-----|------|-------------|--------|
| 44129 | Parma West | -81.78,41.37,-81.68,41.42 | ❌ Out of credits |
| 44134 | Parma / Seven Hills | -81.72,41.35,-81.65,41.40 | ❌ MCP unreachable |
| 44130 | Middleburg Heights / Parma | -81.80,41.35,-81.73,41.41 | ❌ MCP unreachable |

**Price cap:** $190,000  
**Listing type:** For-sale houses

---

## Error Detail

```
Zillapi call #1 (44129): "Out of credits for this cycle. Top up or upgrade at https://zillapi.com/app/billing."
Zillapi calls #2-3 (44134, 44130): "MCP server unreachable after 17 consecutive failures."
```

---

## Stale Cached Benchmarks (from prior cycle)

⚠️ **These are summary statistics only — not live data. No individual property details available.**

| ZIP | Area | Sale Count | Median Sale | Median Rent | Price/Rent | Gross Yield |
|-----|------|-----------|-------------|-------------|-----------|-------------|
| 44129 | Parma West | 16 (old) | $190,000 | $1,950 | 8.1 | 12.32% |
| 44134 | Parma E / Seven Hills | 44 (old) | $200,000 | $1,675 | 10.0 | 10.05% |
| 44130 | Middleburg Hts / Parma | 7 (old) | $199,900 | $1,575 | 10.6 | 9.45% |

**Key observation:** At the $190K cap, 44129 is the only ZIP where the *median* falls at or below the threshold (and exactly at it — $190K). 44134 and 44130 medians sit above $190K, meaning **only the lower half of inventory in those ZIPs is in play**. 44129 also carries the strongest gross yield (12.32%) and lowest price-to-rent ratio (8.1x) of the three.

---

## Direct Zillow Search URLs (Open in Your Browser)

### 44129 — Parma West
🔗 [Zillow: 44129 for-sale, max $190K](https://www.zillow.com/homes/for_sale/44129_rid/0-190000_price/0-178_mp/)

### 44134 — Parma / Seven Hills
🔗 [Zillow: 44134 for-sale, max $190K](https://www.zillow.com/homes/for_sale/44134_rid/0-190000_price/0-177_mp/)

### 44130 — Middleburg Heights / Parma
🔗 [Zillow: 44130 for-sale, max $190K](https://www.zillow.com/homes/for_sale/44130_rid/0-190000_price/0-179_mp/)

---

## Attempted Sources (All Failed)

| Source | Method | Result |
|--------|--------|--------|
| Zillapi MCP | `mcp_zillapi_search_listings` (3 calls) | Out of credits + MCP unreachable |
| Zillow.com | Blocked by PerimeterX/Cloudflare | Not attempted (per skill guidance) |
| Redfin | Blocked by captcha | Not attempted |
| Realtor.com | Blocked by captcha | Not attempted |

---

## Next Steps

1. **Top up Zillapi credits** at https://zillapi.com/app/billing
2. **Or wait for credits to refresh** on the next billing cycle
3. **Re-run this pull** and the report will auto-populate with live listings
4. **Manual fallback:** Use the direct Zillow search URLs above in a browser now

When credits are available, the automated pull will:
- Pull active for-sale listings per ZIP
- Sort by price (lowest first)
- Attach Zestimates and rent Zestimates
- Apply investor verdicts (take / negotiate / pass)
- Save full report + quick-reference table