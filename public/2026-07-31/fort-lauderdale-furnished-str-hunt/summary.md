# Fort Lauderdale furnished STR hunt

## Result
No properties qualified under the full filter set.

## Filters used
- Target ZIPs: 33316, 33308, 33313
- Property type: single-family home or townhouse
- Rent: $1,500-$3,000/month
- Furnished required
- Listing age: more than 60 days
- Only keep properties with projected spread over $1,000/month

## Why none qualified
### Zillapi / Zillow
- The Fort Lauderdale Zillapi rental search returned mostly apartment inventory in the target ZIPs.
- Only **one strict house/townhouse candidate** surfaced after filtering out apartments and condo-style inventory:
  - **2244 NW 52nd Ave, Fort Lauderdale, FL 33313** — townhouse — $1,750
  - Zillapi property detail showed **daysOnZillow = 12** and **furnished = false**
  - Zillow link: https://www.zillow.com/homedetails/2244-NW-52nd-Ave-Fort-Lauderdale-FL-33313/2062530579_zpid/
- Because it failed the furnished and 60+ day filters, it did not advance to the final qualifying set.

### Craigslist
- I searched the South Florida Craigslist housing feed for **furnished** rentals in the Broward / Fort Lauderdale area, sorted by **oldest first**.
- The oldest visible result in the search set was dated **6/15/2026**, which is still **less than 60 days old** as of 2026-07-31.
- Fort Lauderdale-specific house-like results I reviewed were dated **7/14, 7/29, and 7/30**, so none met the 60+ day requirement.

## Reviewed near-miss examples
1. **2244 NW 52nd Ave, Fort Lauderdale, FL 33313** — townhouse — $1,750 — failed: not furnished, only 12 days on Zillow
2. **SPACIOUS SINGLE FAMILY HOME READY NOW!!!** — Craigslist — $1,580 — Fort Lauderdale — posted 7/14 — failed: not 60+ days old
3. **Residential Las Olas 2 bed 1 bath house w pool for lease #2** — Craigslist — $2,600 — Fort Lauderdale — posted 7/30 — failed: not 60+ days old

## Output artifacts
- `artifacts/csv/zillapi-strict-candidates.json`
- `artifacts/csv/zillapi-strict-candidates.csv`
- `artifacts/csv/craigslist-reviewed.json`
- `artifacts/csv/craigslist-reviewed.csv`
- `artifacts/csv/qualifying-properties.json`
- `artifacts/csv/qualifying-properties.csv`
