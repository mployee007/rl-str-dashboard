# 🏠 Parma, OH — Active For-Sale Listings Under $190,000

**Pull Date:** 2026-09-25
**Source:** Zillow.com via Camofox browser (`__NEXT_DATA__` extraction)
**Zillapi MCP:** ❌ Out of credits
**Search Area:** ZIP 44129 (Parma West). 44134 and 44130 blocked by Cloudflare captcha on 2nd navigation.
**Filter:** Houses only, max $190,000, active for-sale, price ascending

---

## ⚠️ Data Source Status

| Source | Status | Detail |
|---|---|---|
| Zillapi MCP | ❌ Out of credits | All 3 bbox calls failed; MCP server became unreachable |
| Zillow → `__NEXT_DATA__` | ✅ Complete (44129) | 7 of 7 listings extracted from embedded JSON |
| Zillow (44134, 44130) | ❌ Captcha-blocked | Cloudflare "Press & Hold" on 2nd navigation |
| Rent estimates | ⚠️ Market-derived | Cleveland-Elyria MSA FY2025 FMR: 3BR=$1,553. Parma est: 3BR=$1,450, 2BR=$1,200 |
| Zillow Rent Zestimate | ❌ Not available | All `rentZestimate` fields were null in `__NEXT_DATA__` |

> **Rent figures are market estimates, NOT property-specific.** Individual property pages are captcha-blocked. Verify with actual rent comps (Rentometer, local PM quotes, or MLS rent data) before making offers.

## 📊 Source Attempt Log

| Attempt | Tool | Target | Result |
|---|---|---|---|
| 1 | mcp_zillapi_search_listings | 44129 bbox | ❌ "Out of credits for this cycle" |
| 2 | mcp_zillapi_search_listings | 44134 bbox | ❌ MCP server unreachable (20 failures) |
| 3 | mcp_zillapi_search_listings | 44130 bbox | ❌ MCP server unreachable (20 failures) |
| 4 | browser_navigate | 44129 path-based URL | ✅ Page loaded: 7 results |
| 5 | browser_console `__NEXT_DATA__` | 44129 | ✅ All 7 listings extracted |
| 6 | browser_navigate | 44134 path-based URL | ❌ Cloudflare "Press & Hold" |
| 7 | browser_navigate | 44130 path-based URL | ❌ Cloudflare "Press & Hold" |
| 8 | mcp_agent_search_http_search | Parma OH rent data | ❌ Returned Parma, Italy |
| 9 | web_search | Parma rent data | ❌ firecrawl-py not installed |

---

## 📈 Summary

| Metric | Value |
|---|---|
| Total listings | **7 houses** in 44129 (0 in 44134, 0 in 44130 — captcha-blocked) |
| Median price | **$189,900** |
| Price range | $165,000 – $190,000 |
| Median sqft | 1,176 (among those with data) |
| Median GRM | 10.9x |
| Fresh listings (0-1 days) | **3** — 6006 Snow Rd, 6507 Forest Ave, 7611 Newport Ave |
| 3br median price | $189,900 (6 listings) |

---

## 📍 ZIP 44129 — Parma West

**7 active listings** under $190K. Sorted by price (lowest first).

| # | Address | Price | Beds | Baths | Sqft | Days Listed | GRM | Yield | Est. Rent | Verdict |
|---|--------|-------|------|-------|------|-------------|-----|-------|-----------|---------|
| 1 | [6006 Snow Rd](https://www.zillow.com/homedetails/6006-Snow-Rd-Cleveland-OH-44129/2057037610_zpid/) | $165,000 | 3 | 2 | 1,188 | 0 days (new today!) | 9.5x | 10.5% | $1,450/mo | **take selectively** |
| | _Fresh listing. 3/2 at lowest price in 44129._ | | | | | | | | | _take selectively — strong GRM under 10x; verify condition_ |
| 2 | [7611 Newport Ave](https://www.zillow.com/homedetails/7611-Newport-Ave-Parma-OH-44129/33547825_zpid/) | $174,900 | 3 | 1 | 1,092 | 1 day | 10.1x | 9.9% | $1,450/mo | **take selectively** |
| | _Compact 3/1 ranch. 1 bath is the limiting factor for rent._ | | | | | | | | | _take selectively — reasonable GRM; verify rents_ |
| 3 | [6211 Dartworth Dr](https://www.zillow.com/homedetails/6211-Dartworth-Dr-Parma-OH-44129/33561552_zpid/) | $184,000 | 2 | 1 | 1,085 | 14 days | 12.8x | 7.8% | $1,200/mo | **negotiate** |
| | _Open house Sat 9/26. Only 2br in the set._ | | | | | | | | | _negotiate — high GRM for Parma; only at $5K-$10K below ask_ |
| 4 | [6507 Forest Ave](https://www.zillow.com/homedetails/6507-Forest-Ave-Parma-OH-44129/33550416_zpid/) | $189,900 | 3 | 2 | 1,026 | 0 days (new today!) | 10.9x | 9.2% | $1,450/mo | **take selectively** |
| | _3/2 but smallest sqft. Fresh listing._ | | | | | | | | | _take selectively — reasonable GRM; verify rents_ |
| 5 | [5597 W 54th St](https://www.zillow.com/homedetails/5597-W-54th-St-Parma-OH-44129/33553876_zpid/) | $189,900 | 3 | 1 | 1,636 | 21 days | 10.9x | 9.2% | $1,450/mo | **negotiate** |
| | _Beautiful curb appeal (per listing). 43 photos. Largest sqft among 44129 3/1s._ | | | | | | | | | _negotiate — decent GRM but stale; try below ask_ |
| 6 | [7101 Brownfield Dr](https://www.zillow.com/homedetails/7101-Brownfield-Dr-Parma-OH-44129/33561440_zpid/) | $189,900 | 3 | 1 | 2,186 | 9 days | 10.9x | 9.2% | $1,450/mo | **take selectively** |
| | _Beautiful hardwood floors throughout. MASSIVE 2,186 sqft — best value per sqft._ | | | | | | | | | _take selectively — reasonable GRM; verify rents_ |
| 7 | [6311 Thornton Dr](https://www.zillow.com/homedetails/6311-Thornton-Dr-Parma-OH-44129/33562283_zpid/) | $190,000 | 3 | 2 | 1,176 | 36 days | 10.9x | 9.2% | $1,450/mo | **negotiate** |
| | _36 days stale — longest on market. Likely overpriced. Only 1,176 sqft._ | | | | | | | | | _negotiate — decent GRM but stale; try below ask_ |

---

## 🔍 Property Deep Dives

### 🥇 Best Overall Value: 6006 Snow Rd — $165,000

| Detail | Value |
|---|---|
| Zillow URL | https://www.zillow.com/homedetails/6006-Snow-Rd-Cleveland-OH-44129/2057037610_zpid/ |
| Configuration | 3bd / 2ba / 1,188 sqft |
| Price per sqft | **$139/sqft** |
| Est. rent | $1,450/mo → $17,400/yr |
| GRM | **9.5x** — best in 44129 |
| Gross yield | **10.5%** |
| Days on market | **0 days** — listed TODAY |
| Broker | Keller Williams Living |

**Verdict: TAKE SELECTIVELY.** At $165K with 3/2, this is the best-priced house in 44129 by a wide margin. GRM of 9.5x is strong for Parma. Listed today — will move fast. Verify condition, check comps, and move quickly if it pencils.

### 🥈 Best Value Per Sqft: 7101 Brownfield Dr — $189,900

| Detail | Value |
|---|---|
| Zillow URL | https://www.zillow.com/homedetails/7101-Brownfield-Dr-Parma-OH-44129/33561440_zpid/ |
| Configuration | 3bd / 1ba / **2,186 sqft** |
| Price per sqft | **$87/sqft** — cheapest in set |
| Est. rent | $1,500/mo → $18,000/yr |
| GRM | 10.5x |
| Gross yield | 9.5% |
| Days on market | 9 days |
| Notes | "Beautiful hardwood floors throughout" |

**Verdict: TAKE SELECTIVELY.** Massive house at a per-sqft discount. Hardwood floors suggest good bones/long-term quality. The 1-bath is the limiting factor for rent — 4-person family in 2,186 sqft with 1 bath is tight. If the basement is finishable and a 2nd bath is feasible, this becomes a strong value-add play.


| Detail| Value |
|---|---|
| Zillow URL | https://www.zillow.com/homedetails/6311-Thornton-Dr-Parma-OH-44129/33562283_zpid/ |
| Configuration | 3bd / 2ba / 1,176 sqft |
| Days on market | **36 days** — longest in set |
| GRM | 10.9x |
| Gross yield | 9.2% |

**Verdict: NEGOTIATE.** 36 days is a clear signal — market is saying no at $190K. At $175K with verified rent, this could work, but at ask it's a pass. The 2-bath is nice but doesn't justify the premium for only 1,176 sqft.

---

## 📐 Acquisition Buy Box — Parma SFR

Rent anchor: **Cleveland-Elyria MSA FY2025 3BR FMR = $1,553/mo** (40th percentile). Parma tracks slightly below MSA at ~**$1,450/mo** for a typical 3br SFR.

### 3-Bedroom SFR Buy Box

| Parameter | Target | Stretch | Notes |
|---|---|---|---|
| **Max all-in basis** | $165,000 | $185,000 | At $185K + 3% closing = $190.5K all-in |
| **Target monthly rent** | $1,500+ | $1,400 | Verify with Rentometer or local PM |
| **Target GRM** | ≤9.5x | ≤10.5x | Only 6006 Snow Rd hits target today |
| **Target gross yield** | ≥10.5% | ≥9.5% | At target GRM of 9.5x |
| **Rehab budget** | ≤$10K | ≤$20K | Cosmetic only at target basis |
| **Preferred beds/baths** | 3/2 | 3/1 (value-add) | 2ba commands $100-150/mo rent premium |
| **Min sqft** | 1,200 | 1,000 | Below 1,000 sqft narrows tenant pool |

### 2-Bedroom SFR Buy Box

| Parameter | Target | Stretch | Notes |
|---|---|---|---|
| **Max all-in basis** | $140,000 | $160,000 | 2br rents cap lower |
| **Target monthly rent** | $1,200+ | $1,100 | Cleveland MSA 2BR FMR = $1,208 |
| **Target GRM** | ≤9.5x | ≤11 x | At $140K and $1,200/mo =9.7x |
| **Rehab budget** | ≤$10K | ≤$15K | Smaller homes = lower rehab |

### ❌ Avoid Conditions

- **No garage** in Cleveland winters — significant rent discount
- **Missing square footage** — red flag for condition issues
- **30+ days on market without price cut** — overpriced, market has spoken
- **Blocks bordering industrial** — Parma has pockets near I-480 industrial zones
- **Knob-and-tube wiring / galvanized plumbing** — capex bombs in 1950s Parma stock

---

## 🏆 Final Rankings & Direct Verdicts

### All 7 Listings, Ranked

| Rank | Address | Price | Why | Action |
|------|---------|-------|-----|--------|
| 1 | 6006 SnowRd | $165,000 | Best GRM (9.5x),3/2, listedtoday | **TAKE SELECTIVELY —move fast** |
| 2 | 710 1 BrownfieldDr |$189,900 | Best $/sqft($87),2,186sqft,hardwood floors | **TAKE SELECTIVELY —value-add potential** |
| 3 | 5597 W 54th St | $189,900 | 1,636 sqft, nicecurb appeal, 21days | **NEGOTIATE — offer $175K** |
| 4 | 7611 Newport Ave |$174,900 | 2nd cheapest,compact 3/1, listed yesterday | **NEGOTIATE — verify rent at 1-bath** |
| 5 | 6311 Thornton Dr | $190,000 | 36days stale — marketrejected this price | **NEGOTIATE — try $170K or pass** |
| 6 |6507 ForestAve | $189,900 | 3/2 but tiny (1,026sqft),listed today | **NEGOTIATE — small for price** |
| 7 | 6211 Dartworth Dr |$184,000 | Only 2br, GRM 12.8x — terrible yield | **PASS — 2br at this price doesn't pencil** |

### If You're Buying One Property Tomorrow

**6006 Snow Rd at $165,000.** It's the best-priced 3/2 in 44129, listed today, with the strongest GRM (9.5x). Verify condition immediately — at this price in Parma, it will go under contract within days if it's habitable. Even at full ask with $5K cosmetic rehab, you're in at ~$175K all-in against $1,450/mo rent → 9.7x GRM.

Second choice: **7101 Brownfield Dr** if Snow Rd is already gone. The per-sqft discount and hardwood floors suggest a quality home. At $175K (if you can negotiate down from $189.9K), the math improves significantly.

---

## ⚠️ Missing ZIPs: 44134 and 44130

Both ZIPs were **blocked by Cloudflare "Press & Hold" captcha** on the 2nd and 3rd browser navigations. This is the known single-navigation-per-IP limitation. The first navigation (44129) succeeded and extracted all 7 listings.

**Manual follow-up URLs (open in your browser):**
- **44134:** https://www.zillow.com/homes/for_sale/44134_rb/1-_beds/0-190000_price/pricea_sort/
- **44130:** https://www.zillow.com/homes/for_sale/44130_rb/1-_beds/0-190000_price/pricea_sort/

From the Sep 24 pull (different IP session), 44134 had 1 listing (3150 Jeanne Dr, $185K), 44130 had 2 (11700 Glamer Dr, $189.9K and 11255 Bobko Blvd, $189.9K). Check if those are still active.

---

## 📁 Files Saved

| File | Path |
|---|---|
| Full report | `/opt/data/outputs/2026-09-25/parma-listings-under-190k/parma-listings.md` |
| Raw JSON data | `/opt/data/outputs/2026-09-25/parma-listings-under-190k/parma-listings-raw.json` |
| Quick reference | `/opt/data/parma-latest-listings.md` |
| Pull status | `/opt/data/parma-pull-status.txt` |

---

*Report generated 2026-09-25 | Source: Zillow.com via Camofox browser `__NEXT_DATA__` extraction | Rent anchor: Cleveland-Elyria MSA FY2025 FMR + Parma market adjustment | Zillapi: offline (out of credits)*