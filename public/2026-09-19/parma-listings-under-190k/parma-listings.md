# Parma West Listings Under $190K — 2026-09-19

## ⚠️ Pull Failed — Zillapi Out of Credits

| ZIP | Source | Result |
|-----|--------|--------|
| 44129 | Zillapi MCP | ❌ Out of credits |
| 44134 | Zillapi MCP | ❌ Server unreachable (117 failures) |
| 44130 | Zillapi MCP | ❌ Server unreachable (117 failures) |
| — | web_search (firecrawl) | ❌ firecrawl-py not installed |
| — | Zillow.com browser | ❌ PerimeterX/Cloudflare captcha |
| — | Redfin | ❌ Cloudflare captcha |
| — | Realtor.com | ❌ Bot-blocked |
| — | Trulia | ❌ PerimeterX captcha |
| — | Homes.com | ❌ Bot-blocked |

## Direct Zillow Search URLs (Open in Browser)

Use these with a real browser to manually review the listings:

- **ZIP 44129 under $190K:**  
  https://www.zillow.com/parma-oh-44129/houses/under-190000_sort/

- **ZIP 44134 under $190K:**  
  https://www.zillow.com/parma-oh-44134/houses/under-190000_sort/

- **ZIP 44130 under $190K:**  
  https://www.zillow.com/parma-oh-44130/houses/under-190000_sort/

## Bounding Boxes Used (for reference)

| ZIP | West | South | East | North |
|-----|------|-------|------|-------|
| 44129 | -81.78 | 41.37 | -81.68 | 41.42 |
| 44134 | -81.72 | 41.35 | -81.65 | 41.40 |
| 44130 | -81.80 | 41.35 | -81.73 | 41.41 |

## Next Steps

1. **Top up Zillapi credits** at https://zillapi.com/app/billing
2. **Or wait** for the next credit cycle refresh
3. **Re-run** this cron job — it will pick up fresh listings automatically
4. The report will populate the tables below once data is available

---

## Expected Table Template (will populate on next successful pull)

### ZIP 44129 — Parma West

| # | Address | Price | Beds | Baths | Sqft | ZPID | Rent Zest | MoRent/Unit | GRM | Verdict |
|---|---------|-------|------|-------|------|------|-----------|-------------|-----|---------|
| — | *pending data* | — | — | — | — | — | — | — | — | — |

### ZIP 44134 — Parma South

| # | Address | Price | Beds | Baths | Sqft | ZPID | Rent Zest | MoRent/Unit | GRM | Verdict |
|---|---------|-------|------|-------|------|------|-----------|-------------|-----|---------|
| — | *pending data* | — | — | — | — | — | — | — | — | — |

### ZIP 44130 — Parma East / Middleburg Hts

| # | Address | Price | Beds | Baths | Sqft | ZPID | Rent Zest | MoRent/Unit | GRM | Verdict |
|---|---------|-------|------|-------|------|------|-----------|-------------|-----|---------|
| — | *pending data* | — | — | — | — | — | — | — | — | — |

---

*Report will auto-populate on next successful Zillapi pull. Status file at `/opt/data/parma-pull-status.txt`.*