# Parma Area Listings Under $190K — Pull Failed (Zillapi Unavailable)

**Date:** 2026-09-10
**Target ZIPs:** 44129 (Parma West), 44134 (Parma South), 44130 (Parma East/Middleburg Hts)
**Price cap:** $190,000
**Status:** No data retrieved

---

## Blocker Summary

| Source | Result |
|---|---|
| Zillapi MCP — 44129 bbox | Out of credits for this cycle |
| Zillapi MCP — 44134 bbox | MCP server unreachable (49 consecutive failures) |
| Zillapi MCP — 44130 bbox | MCP server unreachable (49 consecutive failures) |

Root cause: Zillapi credits exhausted + MCP server degraded. No listings were retrieved.

---

## Manual Fallback — Direct Zillow Search URLs

| ZIP | Zillow URL |
|---|---|
| 44129 (Parma West) | https://www.zillow.com/homes/for_sale/44129_rb/0-190000_price/0-1753_mp/ |
| 44134 (Parma South) | https://www.zillow.com/homes/for_sale/44134_rb/0-190000_price/0-1502_mp/ |
| 44130 (Parma E / Middleburg Hts) | https://www.zillow.com/homes/for_sale/44130_rb/0-190000_price/0-1381_mp/ |

---

## Bounding Boxes Used

| ZIP | West | South | East | North |
|---|---|---|---|---|
| 44129 | -81.78 | 41.37 | -81.68 | 41.42 |
| 44134 | -81.72 | 41.35 | -81.65 | 41.40 |
| 44130 | -81.80 | 41.35 | -81.73 | 41.41 |

---

## Parma Market Context (from prior thesis)

- 44129 (Parma West): Dense bungalow/cape cod stock, 1940s-60s builds, 900-1,400 sqft typical. Entry-level SFR zone. Median home value ~$175K-$195K.
- 44134 (Parma South) Similar stock, slightly lower price band (~$155K-$180K median). Good value-add SFR hunting ground.
- 44130 (Middleburg Heights / east Parma): Slightly newer stock (1960s-80s), more ranches and split-levels. Median ~$190K-$210K.

Verdict thresholds when data arrives: GRM < 10 = take, 10-13 = take selectively, 13-16 = negotiate, >16 = pass.

---

## Next Steps

1. Recharge Zillapi credits at https://zillapi.com/app/billing
2. Waitt for MCP server to recover
3. Re-run this cron job
4. When data arrives, listings saved to this directory pluss /opt/data/parma-latest-listings.md

Status file: /opt/data/parma-pull-status.txt
