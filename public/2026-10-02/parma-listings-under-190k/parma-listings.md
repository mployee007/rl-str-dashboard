# Parma West Submarket Listings — Under $190K

**Pull Date:** 2026-10-02
**Status:** ❌ BLOCKED — All data sources exhausted

## Source Attempts

| # | Source | Target | Result |
|---|--------|--------|--------|
| 1 | Zillapi MCP `search_listings` | 44129 (bbox: -81.78,41.37,-81.68,41.42) | **"Out of credits for this cycle"** |
| 2 | Zillapi MCP `search_listings` | 44134 (bbox: -81.72,41.35,-81.65,41.40) | MCP server unreachable (post-exhaustion) |
| 3 | Zillapi MCP `search_listings` | 44130 (bbox: -81.80,41.35,-81.73,41.41) | MCP server unreachable (post-exhaustion) |
| 4 | Camofox browser → Zillow path URL | 44129 (`/44129_rb/1-_beds/0-190000_price/pricea_sort/`) | Cloudflare "Press & Hold" captcha |
| 5 | Camofox browser → Zillow path URL | 44134 (`/44134_rb/1-_beds/0-190000_price/pricea_sort/`) | Cloudflare "Press & Hold" captcha |

## Blockers

1. **Zillapi** — credits exhausted. Top up at https://zillapi.com/app/billing
2. **Camofox / Zillow** — IP-based Cloudflare rate limit. The "Press & Hold" captcha is not solvable programmatically. Requires IP rotation (VPN/proxy) to get a fresh session.

## Direct Links (Manual Follow-Up)

| ZIP | Zillow Link |
|-----|-------------|
| 44129 | https://www.zillow.com/homes/for_sale/44129_rb/1-_beds/0-190000_price/pricea_sort/ |
| 44134 | https://www.zillow.com/homes/for_sale/44134_rb/1-_beds/0-190000_price/pricea_sort/ |
| 44130 | https://www.zillow.com/homes/for_sale/44130_rb/1-_beds/0-190000_price/pricea_sort/ |

## Rent Anchors (For Verdict Calculation)

Cleveland-Elyria MSA FY2025 FMR, Parma-adjusted (90% of MSA):
- 2BR: ~$1,200/mo → GRM ≤12 implies max basis ~$173K
- 3BR: ~$1,398/mo → GRM ≤12 implies max basis ~$201K
- 4BR: ~$1,629/mo → GRM ≤12 implies max basis ~$235K

## Buyer's Box (Pre-computed)

| Property Type | Target Basis | Stretch Basis | Target Rent | Target GRM | Target Yield |
|---------------|-------------|---------------|-------------|------------|-------------|
| 2BR SFR | ≤$130K | ≤$160K | ≥$1,200/mo | ≤11 | ≥9.2% |
| 3BR SFR | ≤$150K | ≤$180K | ≥$1,398/mo | ≤11 | ≥9.3% |
| 4BR SFR | ≤$170K | ≤$190K | ≥$1,629/mo | ≤11 | ≥9.4% |
| Duplex | ≤$180K | ≤$210K | ≥$2,200/mo | ≤9.5 | ≥10.5% |

⚠️ All rent figures are market-derived (HUD FY2025 FMR × 90% Parma adjustment), NOT property-specific.

## Resolution

This cron job will succeed on next run after either:
1. Zillapi credits are topped up, OR
2. Camofox gets a fresh IP (VPN rotation)

No listings were fabricated. Status files saved at:
- `/opt/data/parma-pull-status.txt`
- `/opt/data/parma-latest-listings.md`
- `/opt/data/outputs/2026-10-02/parma-listings-under-190k/parma-listings.md`