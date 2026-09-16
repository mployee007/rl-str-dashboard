# Parma Listings Under $190K — Blocked (Zillapi Credits Exhausted)

**Date:** 2026-09-16  
**Status:** ❌ No data — Zillapi credits exhausted  
**Target ZIPs:** 44129 (Parma West), 44134 (Parma SE), 44130 (Parma SW)

---

## What happened

| Source | ZIP | Result |
|---|---|---|
| Zillapi (MCP) | 44129 | **Out of credits** — top up at https://zillapi.com/app/billing |
| Zillapi (MCP) | 44134 | Server unreachable (rate-limited after prior failure) |
| Zillapi (MCP) | 44130 | Server unreachable (rate-limited after prior failure) |

All web-based listing sites (Zillow.com, Redfin, Trulia, Realtor.com, Homes.com, Movoto) block with captchas from this environment and cannot be used as fallbacks.

---

## Direct links — open in your browser

These are the Zillow searches you can run manually right now:

- **[44129 | ≤$190K](https://www.zillow.com/homes/for_sale/44129/0-190000_price/0-10000_mp/)** — Parma West
- **[44134 | ≤$190K](https://www.zillow.com/homes/for_sale/44134/0-190000_price/0-10000_mp/)** — Parma SE
- **[44130 | ≤$190K](https://www.zillow.com/homes/for_sale/44130/0-190000_price/0-10000_mp/)** — Parma SW

---

## Next steps

1. Top up Zillapi credits at https://zillapi.com/app/billing
2. Re-run this cron job or manually trigger: `hermes cron run parma-listings`
3. When credits are available, the job will pull all three ZIPs, produce the full markdown report with investor verdicts, and update `parma-latest-listings.md`

---

## File inventory

| File | Purpose |
|---|---|
| `/opt/data/parma-pull-status.txt` | Blocker status + timestamp |
| `/opt/data/outputs/2026-09-16/parma-listings-under-190k/parma-listings.md` | This report |
| `/opt/data/parma-latest-listings.md` | Will be updated when data arrives (currently unchanged) |