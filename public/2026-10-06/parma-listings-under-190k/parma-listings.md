# Parma West (44129, 44134, 44130) — For-Sale Listings Under $190K

**Pull date:** 2026-10-06  
**Status:** ❌ BLOCKED — no live listing data available  
**Price cap:** $190,000 | **Beds:** 1+ | **Property type:** Houses (1-4 units)

---

## Blocker Summary

This pull could not complete. All three data tiers failed:

| Tier | Source | ZIP(s) | Result |
|------|--------|--------|--------|
| 1 | Zillapi MCP | 44129 | "This month's credits are used up" |
| 1 | Zillapi MCP | 44134 | MCP server unreachable after credit exhaustion |
| 1 | Zillapi MCP | 44130 | MCP server unreachable after credit exhaustion |
| 2 | Camofox browser → Zillow | 44129 | Cloudflare "Press & Hold" captcha — IP rate-limited |
| 2 | Camofox browser → Zillow | 44134 | Not attempted (would hit same captcha) |
| 2 | Camofox browser → Zillow | 44130 | Not attempted (would hit same captcha) |

---

## Rent Anchor (for reference when listings are available)

**Cleveland-Elyria MSA FY2025 FMRs (40th percentile gross rent):**

| Unit | MSA FMR | Parma Adj. (90%) |
|------|---------|-------------------|
| 1BR | $903 | $813 |
| 2BR | $1,098 | $988 |
| 3BR | $1,553 | $1,398 |
| 4BR | $1,810 | $1,629 |

⚠️ Market-derived — NOT property-specific. Parma adjustment: 90% of MSA FMR (working-class suburb).

---

## Buy Box Reference (from skill framework)

For when listings become available, screen against these thresholds:

| Property Type | Target All-In | Stretch All-In | Target Monthly Rent | Target Gross Yield | Rehab Tolerance |
|---------------|---------------|----------------|---------------------|--------------------|-----------------|
| 1-unit SFR | ≤$150K | ≤$190K | ≥$1,200 | ≥9.6% | ≤$30K |
| 2-unit duplex | ≤$130K | ≤$170K | ≥$1,800 ($900/unit) | ≥10.5% | ≤$40K |
| 3-unit | ≤$150K | ≤$190K | ≥$2,400 ($800/unit) | ≥11.4% | ≤$50K |
| 4-unit | ≤$170K | ≤$190K | ≥$2,800 ($700/unit) | ≥11.8% | ≤$60K |

*Yield computed at target all-in; stretch basis reduces headline yield.*

**Verdict filters (when listings are available):**
- **take** — below target basis, rents verify, condition acceptable
- **take selectively** — at target basis in preferred block
- **negotiate** — at stretch basis; needs price reduction or verified rent upside
- **pass** — over stretch basis, major systems deferred, or in avoid block

---

## Manual Follow-Up

Open these direct Zillow URLs in any browser:

| ZIP | Direct Link |
|-----|-------------|
| 44129 | https://www.zillow.com/homes/for_sale/44129_rb/1-_beds/0-190000_price/pricea_sort/ |
| 44134 | https://www.zillow.com/homes/for_sale/44134_rb/1-_beds/0-190000_price/pricea_sort/ |
| 44130 | https://www.zillow.com/homes/for_sale/44130_rb/1-_beds/0-190000_price/pricea_sort/ |

---

## Resolution

- **Zillapi:** Credits refresh at start of next monthly billing period, or top up at https://zillapi.com/app/billing
- **Camofox:** IP-based Cloudflare rate limit — typically clears within hours (not minutes). A fresh IP (VPN, restart router with dynamic IP) would allow a new first navigation.
- **Next cron run:** Will retry Zillapi first; if credits haven't refreshed, Camofox may work if the IP cooldown has passed.