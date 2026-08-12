# Multi-City STR Arbitrage Scan

**Date:** 2026-08-10
**Criteria:** furnished single-family homes/townhomes, $2,000-$3,800/mo, target spread > $1,300/mo
**Method:** Craigslist listing collection + first-pass 3-scenario STR underwriting using the loaded STR-arbitrage skill rate bands. Reference ZIPs from uploaded file were used where available; fallback core-city ZIP handling used where the uploaded file lacked the requested city.

## ZIP focus from uploaded file

| City | ZIP strategy |
|---|---|
| Jacksonville | 32224, 32218, 32207, 32204, 32250 |
| Scottsdale | 85251, 85260, 85259 |
| Phoenix | 85006, 85027, 85054, 85013 |
| Memphis | 38104, 38103, 38120, 38105 |
| Portland | 97239, 97225, 97227, 97216 |
| St. Petersburg, Tempe, Eugene, Henderson, Myrtle Beach, Virginia Beach, Norfolk | uploaded file had no exact city row; searched city generally and recorded listing ZIPs when visible |

## Qualified candidates (moderate spread > $1,300)

| Rank | City | Property | Rent | Cons. Revenue / Spread | Moderate Revenue / Spread | Optimistic Revenue / Spread | Verdict | ZIP fit |
|---:|---|---|---:|---:|---:|---:|---|---|
| 1 | Virginia Beach, VA | [5 bedroom available 2 minutes from the beach !!](https://www.craigslist.org/view/d/virginia-beach-bedroom-available/wrbjPkAECU2K9yjPHPGhe5) | $3,400 | $5,445 / $2,045 | $7,200 / $3,800 | $9,360 / $5,960 | **take** | not shown (fallback) |
| 2 | Virginia Beach, VA | [Short term rental available till December](https://www.craigslist.org/view/d/virginia-beach-short-term-rental/ddmek9Mmxc8xZmhBePUSyx) | $3,100 | $4,950 / $1,850 | $6,480 / $3,380 | $8,385 / $5,285 | **take** | not shown (fallback) |
| 3 | Phoenix, AZ | [House for Lease (Biltmore/Camel Back)](https://www.craigslist.org/view/d/phoenix-house-for-lease/phEYUjAu7L7EK6XGiB9Tib) | $2,680 | $3,960 / $1,280 | $5,400 / $2,720 | $7,410 / $4,730 | **take** | ~85016 (adjacent) |
| 4 | Tempe, AZ | [Comfortable Family House / Centrally Located](https://www.craigslist.org/view/d/tempe-comfortable-family-house/sMDg9Z3RRZhz9ujR2SG6rn) | $2,450 | $3,465 / $1,015 | $4,500 / $2,050 | $5,850 / $3,400 | **take** | 85283 (fallback) |
| 5 | Phoenix, AZ | [Historic Furnished Home – 2bed/1 bath – Midtown Phoenix](https://www.craigslist.org/view/d/phoenix-historic-furnished-home-2bed/6YJGYjo4QHneySmyiYmLbf) | $2,150 | $2,970 / $820 | $4,050 / $1,900 | $5,265 / $3,115 | **take** | ~85006 (likely target/adjacent) |
| 6 | Phoenix, AZ | [Smart & Modern Townhome](https://www.craigslist.org/view/d/phoenix-smart-modern-townhome/7AdJsruO8RGdOZI0fAUsWQ) | $2,250 | $3,135 / $885 | $4,140 / $1,890 | $5,362 / $3,112 | **take** | 85018 (adjacent) |
| 7 | Henderson, NV | [Furnished Henderson, Nv home for rent $2500](https://www.craigslist.org/view/d/henderson-furnished-henderson-nv-home/c1wxHAjoW6bcVi6x3fQsBA) | $2,500 | $3,135 / $635 | $4,320 / $1,820 | $5,655 / $3,155 | **take** | ~89002 (fallback) |
| 8 | Scottsdale, AZ | [Stylish and spacious 3BR/2BA townhome near Old Town Scottsdale](https://www.craigslist.org/view/d/scottsdale-stylish-and-spacious-3br-2ba/ihl8njh_8RGOCr3M6rCRQw) | $3,250 | $3,713 / $463 | $5,040 / $1,790 | $6,630 / $3,380 | **negotiate** | 85251 (target) |
| 9 | Tempe, AZ | [I would live here. Great Tempe location](https://www.craigslist.org/view/d/tempe-would-live-here-great-tempe/0jw5ejOU8RGFypc66B7Oew) | $2,900 | $3,630 / $730 | $4,680 / $1,780 | $6,240 / $3,340 | **negotiate** | 85281 (fallback) |
| 10 | Saint Petersburg, FL | [Furnished 3 BEDROOMS 2.5 BATH with a garage townhouse! Welcome home](https://www.craigslist.org/view/d/saint-petersburg-furnished-bedrooms-25/CATZJ-6O8RGDm7QrAimHNQ) | $2,950 | $3,630 / $680 | $4,680 / $1,730 | $6,240 / $3,290 | **negotiate** | 33716 (fallback-nearby) |

## Market-by-market verdicts

### Virginia Beach, VA — 5 bedroom available 2 minutes from the beach !!
- **Rent:** $3,400 | **Type:** SFH | **Beds/Baths:** 5BR/2.5BA
- **Listing:** https://www.craigslist.org/view/d/virginia-beach-bedroom-available/wrbjPkAECU2K9yjPHPGhe5
- **3-scenario screen:** conservative $2,045, moderate $3,800, optimistic $5,960
- **Verdict:** **take**
- **Why:** 2 blocks from ocean/boardwalk; short-term Aug-Dec window from listing
- **Reg note:** Beach economics are strong, but verify local zoning/permit rules before pursuing lease-up.

### Virginia Beach, VA — Short term rental available till December
- **Rent:** $3,100 | **Type:** SFH | **Beds/Baths:** 4BR/2.5BA
- **Listing:** https://www.craigslist.org/view/d/virginia-beach-short-term-rental/ddmek9Mmxc8xZmhBePUSyx
- **3-scenario screen:** conservative $1,850, moderate $3,380, optimistic $5,285
- **Verdict:** **take**
- **Why:** 3-min walk to beach/boardwalk; short-term through Dec
- **Reg note:** Beach economics are strong, but verify local zoning/permit rules before pursuing lease-up.

### Phoenix, AZ — House for Lease (Biltmore/Camel Back)
- **Rent:** $2,680 | **Type:** SFH | **Beds/Baths:** 4BR/2BA
- **Listing:** https://www.craigslist.org/view/d/phoenix-house-for-lease/phEYUjAu7L7EK6XGiB9Tib
- **3-scenario screen:** conservative $1,280, moderate $2,720, optimistic $4,730
- **Verdict:** **take**
- **Why:** Prime Biltmore/Camelback positioning supports higher ADR band
- **Reg note:** Arizona remains one of the strongest statewide STR-preemption markets; Phoenix/Scottsdale/Tempe are economically viable for landlord-permission arbitrage, subject to registration/compliance.

### Tempe, AZ — Comfortable Family House / Centrally Located
- **Rent:** $2,450 | **Type:** SFH | **Beds/Baths:** 3BR/2BA
- **Listing:** https://www.craigslist.org/view/d/tempe-comfortable-family-house/sMDg9Z3RRZhz9ujR2SG6rn
- **3-scenario screen:** conservative $1,015, moderate $2,050, optimistic $3,400
- **Verdict:** **take**
- **Why:** Family-size furnished house in core Tempe
- **Reg note:** Arizona remains one of the strongest statewide STR-preemption markets; Phoenix/Scottsdale/Tempe are economically viable for landlord-permission arbitrage, subject to registration/compliance.

### Phoenix, AZ — Historic Furnished Home – 2bed/1 bath – Midtown Phoenix
- **Rent:** $2,150 | **Type:** SFH | **Beds/Baths:** 2BR/1BA
- **Listing:** https://www.craigslist.org/view/d/phoenix-historic-furnished-home-2bed/6YJGYjo4QHneySmyiYmLbf
- **3-scenario screen:** conservative $820, moderate $1,900, optimistic $3,115
- **Verdict:** **take**
- **Why:** Midtown / medical corridor proximity
- **Reg note:** Arizona remains one of the strongest statewide STR-preemption markets; Phoenix/Scottsdale/Tempe are economically viable for landlord-permission arbitrage, subject to registration/compliance.

### Phoenix, AZ — Smart & Modern Townhome
- **Rent:** $2,250 | **Type:** Townhome | **Beds/Baths:** 2BR/1BA
- **Listing:** https://www.craigslist.org/view/d/phoenix-smart-modern-townhome/7AdJsruO8RGdOZI0fAUsWQ
- **3-scenario screen:** conservative $885, moderate $1,890, optimistic $3,112
- **Verdict:** **take**
- **Why:** Arcadia Lite / close-in Phoenix
- **Reg note:** Arizona remains one of the strongest statewide STR-preemption markets; Phoenix/Scottsdale/Tempe are economically viable for landlord-permission arbitrage, subject to registration/compliance.

### Henderson, NV — Furnished Henderson, Nv home for rent $2500
- **Rent:** $2,500 | **Type:** SFH | **Beds/Baths:** 3BR/3BA
- **Listing:** https://www.craigslist.org/view/d/henderson-furnished-henderson-nv-home/c1wxHAjoW6bcVi6x3fQsBA
- **3-scenario screen:** conservative $635, moderate $1,820, optimistic $3,155
- **Verdict:** **take**
- **Why:** Former model home; Vegas-area demand proxy
- **Reg note:** Verify Henderson short-term rental permitting/HOA restrictions before treating the deal as actionable.

### Scottsdale, AZ — Stylish and spacious 3BR/2BA townhome near Old Town Scottsdale
- **Rent:** $3,250 | **Type:** Townhome | **Beds/Baths:** 3BR/2BA
- **Listing:** https://www.craigslist.org/view/d/scottsdale-stylish-and-spacious-3br-2ba/ihl8njh_8RGOCr3M6rCRQw
- **3-scenario screen:** conservative $463, moderate $1,790, optimistic $3,380
- **Verdict:** **negotiate**
- **Why:** Old Town-adjacent; strongest Scottsdale ZIP match
- **Reg note:** Arizona remains one of the strongest statewide STR-preemption markets; Phoenix/Scottsdale/Tempe are economically viable for landlord-permission arbitrage, subject to registration/compliance.

### Tempe, AZ — I would live here. Great Tempe location
- **Rent:** $2,900 | **Type:** Townhouse | **Beds/Baths:** 3BR/2.5BA
- **Listing:** https://www.craigslist.org/view/d/tempe-would-live-here-great-tempe/0jw5ejOU8RGFypc66B7Oew
- **3-scenario screen:** conservative $730, moderate $1,780, optimistic $3,340
- **Verdict:** **negotiate**
- **Why:** Gated townhome near ASU/downtown Tempe
- **Reg note:** Arizona remains one of the strongest statewide STR-preemption markets; Phoenix/Scottsdale/Tempe are economically viable for landlord-permission arbitrage, subject to registration/compliance.

### Saint Petersburg, FL — Furnished 3 BEDROOMS 2.5 BATH with a garage townhouse! Welcome home
- **Rent:** $2,950 | **Type:** Townhouse | **Beds/Baths:** 3BR/2.5BA
- **Listing:** https://www.craigslist.org/view/d/saint-petersburg-furnished-bedrooms-25/CATZJ-6O8RGDm7QrAimHNQ
- **3-scenario screen:** conservative $680, moderate $1,730, optimistic $3,290
- **Verdict:** **negotiate**
- **Why:** St. Pete listing; uploaded file had Madeira Beach/St. Petersburg-adjacent rows, not city row
- **Reg note:** Florida is generally workable for STRs, but property-level HOA/lease restrictions and local tax registration still need confirmation.

## Cities screened out / no clean winner

- **Jacksonville, FL** — Trendy San Marco + Mth to Mth Furnished Utilities Included ($2,990). Good furnished house, but moderate spread screens below $1,300 using first-pass urban ADR assumptions.
- **Memphis, TN** — Downtown Executive Home ($3,400). Local Craigslist SFH inventory found, but furnishing was not explicit and economics looked weaker.
- **Portland, OR** — Multiple furnished houses found from $2,000-$3,700 ($2,000). Economics were mixed and Portland is a restrictive STR market; not a clean arbitrage target.
- **Eugene, OR** — No clean explicit-furnished Eugene-core SFH/townhome match in budget (—). Results were mostly outside Eugene proper or not clearly furnished houses/townhomes.
- **Myrtle Beach, SC** — No clear furnished SFH/townhome winner from first page (—). Results skewed to condos; one Murrells Inlet SFH appeared but furnished status was not clear.
- **Norfolk, VA** — Small furnished carriage-house / unit listings only ($3,000). No true detached SFH/townhome winner in the target range from the Norfolk search.

## Bottom line

- **Best immediate take candidates:** Virginia Beach beach houses, Phoenix Biltmore/Camelback house, Tempe 3BR house, Phoenix Arcadia townhome, Phoenix Midtown house.
- **Best ZIP-accurate candidate from uploaded file:** Scottsdale townhome in **85251**.
- **Best Florida candidate:** St. Petersburg townhouse at **$2,950** if landlord/HOA permit STR use.
- **Markets to deprioritize from this scan:** Jacksonville, Memphis, Eugene, Myrtle Beach, Norfolk, Portland.
- **Next move:** contact the top 5 and confirm lease term, STR permission, HOA restrictions, and utility setup before underwriting furnishing / cleaning / platform fees in detail.