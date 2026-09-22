# Parma-Area Listings Under $190K — Pull Blocked

**Date:** 2026-09-22  
**Status:** ❌ Zillapi out of credits — no live data pulled

---

## Targeted ZIP Codes

| ZIP | Area | Bounding Box | Status |
|-----|------|-------------|--------|
| 44129 | Parma West | -81.78,41.37,-81.68,41.42 | No data (credits exhausted) |
| 44134 | Parma / Seven Hills | -81.72,41.35,-81.65,41.40 | No data (MCP unreachable) |
| 44130 | Middleburg Heights / Parma | -81.80,41.35,-81.73,41.41 | No data (MCP unreachable) |

**Price cap:** $190,000  
**Listing type:** For-sale houses

---

## Error Detail

```
Zillapi: "Out of credits for this cycle. Top up or upgrade at https://zillapi.com/app/billing."
Subsequent: MCP server unreachable (4 consecutive failures)
```

---

## Direct Zillow Search URLs (Open in Your Browser)

These links will show active for-sale listings under $190K in each ZIP:

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
3. **Re-run this pull** and the report will auto-populate
4. **Manual fallback:** Use the direct Zillow search URLs above in a browser now

When credits are available, the automated pull will:
- Pull 50 listings per ZIP
- Sort by price (lowest first)
- Attach Zestimates and rent Zestimates
- Apply investor verdicts (take / negotiate / pass)
- Save to `/opt/data/parma-latest-listings.md`