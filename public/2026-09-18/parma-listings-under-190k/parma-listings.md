# Parma Area Listings Under $190K — Pull Report

**Date:** 2026-09-18 (Friday, automated cron run)
**Target ZIPs:** 44129 (Parma West), 44134 (Parma South), 44130 (Parma Heights)
**Price Cap:** $190,000
**Status:** ❌ **BLOCKED — Zillapi out of credits (Day 15 of consecutive failure)**

---

## Blocker Summary

| Source | Attempted | Result |
|--------|-----------|--------|
| **Zillapi MCP** — 44129 bbox | ✅ | "Out of credits for this cycle" |
| **Zillapi MCP** — 44134 bbox | ✅ | "MCP server unreachable after 111 consecutive failures" |
| **Zillapi MCP** — 44130 bbox | ✅ | "MCP server unreachable after 111 consecutive failures" |
| **Zillow.com** | ❌ Not attempted | Blocked by PerimeterX/Cloudflare (per skill protocol) |
| **Redfin** | ❌ Not attempted | Blocked by captchas (per skill protocol) |
| **Realtor.com** | ❌ Not attempted | Blocked by captchas (per skill protocol) |

---

## ⚠️ Escalation: 15 Consecutive Days of Failure

This pull has failed every single day since at least **September 4, 2026** — 15 consecutive failures:

| Date | Status |
|------|--------|
| 2026-09-04 | ❌ Out of credits |
| 2026-09-05 | ❌ Out of credits |
| 2026-09-06 | ❌ Out of credits |
| 2026-09-07 | ❌ Out of credits |
| 2026-09-08 | ❌ Out of credits |
| 2026-09-09 | ❌ Out of credits |
| 2026-09-10 | ❌ Out of credits |
| 2026-09-12 | ❌ Out of credits |
| 2026-09-13 | ❌ Out of credits |
| 2026-09-14 | ❌ Out of credits |
| 2026-09-15 | ❌ Out of credits |
| 2026-09-16 | ❌ Out of credits |
| 2026-09-17 | ❌ Out of credits |
| **2026-09-18** | **❌ Out of credits (today)** |

**No successful listing pull exists in the output history.** The Zillapi credit pool has been exhausted for over two weeks.

---

## Manual Workaround

Until Zillapi credits are restored, use these direct Zillow search URLs in a browser:

- **[44129 — Parma West, under $190K](https://www.zillow.com/parma-west-parma-oh-44129/houses/?searchQueryState={"pagination":{},"isMapVisible":true,"mapBounds":{"west":-81.78,"south":41.37,"east":-81.68,"north":41.42},"filterState":{"price":{"max":190000},"sort":{"value":"globalrelevanceex"}},"isListVisible":true})**

- **[44134 — Parma South, under $190K](https://www.zillow.com/parma-oh-44134/houses/?searchQueryState={"pagination":{},"isMapVisible":true,"mapBounds":{"west":-81.72,"south":41.35,"east":-81.65,"north":41.40},"filterState":{"price":{"max":190000},"sort":{"value":"globalrelevanceex"}},"isListVisible":true})**

- **[44130 — Parma Heights, under $190K](https://www.zillow.com/parma-heights-oh-44130/houses/?searchQueryState={"pagination":{},"isMapVisible":true,"mapBounds":{"west":-81.80,"south":41.35,"east":-81.73,"north":41.41},"filterState":{"price":{"max":190000},"sort":{"value":"globalrelevanceex"}},"isListVisible":true})**

---

## Next Steps

1. **Top up Zillapi credits** at https://zillapi.com/app/billing
2. The cron job will resume pulling on the next scheduled run automatically once credits are available
3. Consider upgrading the plan if this is a recurring issue — 15 days of missed data creates a significant gap for deal screening

---

*Status file saved to: `/opt/data/parma-pull-status.txt`*