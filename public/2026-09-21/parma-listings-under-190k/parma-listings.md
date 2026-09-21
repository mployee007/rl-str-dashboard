# Parma Listings Under $190K — BLOCKED

**Generated:** 2026-09-21T03:31:34Z  
**Status:** ❌ Zillapi credits exhausted — 18th consecutive day of this block

---

## Blocker Summary

Zillapi `search_listings` returned `"Out of credits for this cycle"` on the first pull attempt for ZIP 44129. The two subsequent parallel calls for 44134 and 44130 failed with `"MCP server unreachable"` (128 consecutive failures). Per the `real-estate-submarket-screening` skill protocol, no alternate sites were attempted — Zillow.com, Redfin, Trulia, and all other listing sites block automated access with captchas.

---

## Sources Tried

| Source | Result |
|---|---|
| Zillapi MCP (`search_listings`, `for_sale`, bbox for 44129) | ❌ Out of credits |
| Zillapi MCP (`search_listings`, `for_sale`, bbox for 44134) | ❌ MCP server unreachable (follow-on) |
| Zillapi MCP (`search_listings`, `for_sale`, bbox for 44130) | ❌ MCP server unreachable (follow-on) |

---

## Cached ZIP Benchmarks (from prior successful pulls)

These are aggregate stats from the last successful Zillapi sweep — **not** live today, but useful for context:

| ZIP | Neighborhood | Sale Count (last pull) | Median Sale | Median Rent | GRM | Gross Yield |
|---|---|---|---|---|---|---|
| **44129** | Parma (W) | 16 | $190,000 | $1,950 | 8.1 | 12.3% |
| **44134** | Parma (E), Brooklyn Hts, Seven Hills | 44 | $200,000 | $1,675 | 10.0 | 10.1% |
| **44130** | Parma (mid) | 7 | $199,900 | $1,575 | 10.6 | 9.5% |

### Investor Read (from cached benchmarks)

| ZIP | Fit | Verdict |
|---|---|---|
| **44129** | Best gross yield of the three. Median ask at the $190K cap. Rents strong at $1,950. Lower listing volume suggests tight inventory — act fast when something comes up. | **Take selectively** — best stabilized SFR hold candidate |
| **44134** | Highest listing volume (44) = most selection. Median $200K is slightly above cap but plenty under $190K. Yield ~10% is solid for a B-class suburb. Seven Hills and Brooklyn Hts pockets are stronger subsections. | **Take selectively** — best hunting ground for volume |
| **44130** | Smallest pool (7 listings). Median $199,900 near cap. Weakest yield at 9.5%. Higher price-to-rent ratio. | **Negotiate** — only compelling below $170K basis |

---

## Manual Fallback — Direct Zillow Links

Open these in your browser to run the screen manually today:

- **ZIP 44129 (Parma West):** [Zillow: Houses under $190K](https://www.zillow.com/homes/for_sale/44129_rb/0-190000_price/0-190000_mp/41.37,-81.68,41.42,-81.78_rect/13_zm/)
- **ZIP 44134 (Parma East / Seven Hills):** [Zillow: Houses under $190K](https://www.zillow.com/homes/for_sale/44134_rb/0-190000_price/0-190000_mp/41.35,-81.65,41.40,-81.72_rect/13_zm/)
- **ZIP 44130 (Middleburg Heights / Parma SW):** [Zillow: Houses under $190K](https://www.zillow.com/homes/for_sale/44130_rb/0-190000_price/0-190000_mp/41.35,-81.73,41.41,-81.80_rect/13_zm/)

---

## Buy Box Reference (Parma Submarket)

Based on cached benchmarks, the rough buy box for this submarket:

| Property Type | Target Basis | Stretch Basis | Target Rent/Mo | Target Yield | Rehab Tolerance | Preferred ZIPs |
|---|---|---|---|---|---|---|
| 1-unit SFR | $140K–$170K | $190K | $1,600–$1,950 | 11–14% | < $15K cosmetics | 44129, 44134 |
| 2-unit | $160K–$185K | $200K | $2,600–$3,200 total | 10–12% | < $25K, systems check | 44129, 44134 |
| 3-4 unit | $180K–$230K | $260K | $3,800–$5,000 total | 9–11% | < $35K, verify utilities | 44134 |

### Avoid conditions
- Foundation or major structural issues
- Properties within 500 ft of commercial/industrial (noise, tenant friction)
- Single-bathroom SFH (harder to rent)
- Knob-and-tube wiring still active
- Flood zone AE properties (insurance cost kills yield)

---

## Resolution

1. **Top up Zillapi credits** at https://zillapi.com/app/billing
2. Re-run this cron job — it will pick up fresh listings automatically
3. Status file at `/opt/data/parma-pull-status.txt` will be overwritten on success
4. Until credits restore, use the manual Zillow links above for same-day screening