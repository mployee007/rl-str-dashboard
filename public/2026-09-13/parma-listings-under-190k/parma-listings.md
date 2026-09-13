# Parma Area Listings Under $190K — Pull Attempt

**Date:** $(date +"%Y-%m-%d %H:%M:%S UTC")
**Status:** ❌ BLOCKED — Zillapi credits exhausted

---

## Target ZIP Codes

| ZIP | Neighborhood | Bounding Box | Price Cap |
|-----|-------------|--------------|-----------|
| 44129 | Parma West | -81.78,41.37,-81.68,41.42 | $190,000 |
| 44134 | Parma South / Seven Hills | -81.72,41.35,-81.65,41.40 | $190,000 |
| 44130 | Middleburg Heights / Parma Hts | -81.80,41.35,-81.73,41.41 | $190,000 |

---

## Source Results

| Source | Status | Detail |
|--------|--------|--------|
| **Zillapi (MCP)** | ❌ FAILED | "Out of credits for this cycle" |
| **Zillapi (server)** | ❌ FAILED | MCP server unreachable (68 consecutive failures) |
| **Zillow.com web** | ⛔ SKIPPED | Skill rule: blocked by PerimeterX/Cloudflare captcha |
| **Redfin web** | ⛔ SKIPPED | Skill rule: blocked by captcha |
| **Realtor.com web** | ⛔ SKIPPED | Skill rule: blocked by captcha |

---

## Action Required

Zillapi credits must be topped up at https://zillapi.com/app/billing before this pull can complete.

### Direct Zillow Search URLs (manual fallback)

- **ZIP 44129:** https://www.zillow.com/homes/for_sale/44129_rb/0-190000_price/
- **ZIP 44134:** https://www.zillow.com/homes/for_sale/44134_rb/0-190000_price/
- **ZIP 44130:** https://www.zillow.com/homes/for_sale/44130_rb/0-190000_price/

---

## Investor Context (from prior Cleveland/Parma thesis)

While we wait for fresh data, here's the standing framework for these ZIPs:

| ZIP | Submarket Type | Investor Fit | Notes |
|-----|---------------|-------------|-------|
| 44129 | Value-add SFR zone | Take selectively | Older bungalows, stable blocks, strong rental demand |
| 44134 | Value-add SFR / small MF | Take selectively | Mix of Parma and Seven Hills inventory |
| 44130 | Stabilized hold / value-add | Negotiate | Middleburg Hts has stronger schools, Parma Hts more affordable |

---

## Buy Box Reminder (under $190K Parma cap)

| Property Type | Target Basis | Monthly Rent Target | Gross Yield |
|--------------|-------------|---------------------|-------------|
| 2BR SFR | $130K–$170K | $1,200–$1,500 | 8.5%–14% |
| 3BR SFR | $140K–$190K | $1,400–$1,700 | 8.8%–14.5% |
| Duplex | $150K–$190K | $1,800–$2,200 total | 11%–18% |

*All-in basis caps assume 10-20% rehab reserve on top of purchase price.*

---

## Next Steps

1. Replenish Zillapi credits at https://zillapi.com/app/billing
2. Re-run cron — the pull will pick up fresh listings automatically
3. Status file for this attempt saved at: `/opt/data/parma-pull-status.txt`
