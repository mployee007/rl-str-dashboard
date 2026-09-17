# Parma Submarket Screening — 44129 / 44134 / 44130
## Pull Date: 2026-09-17 | Status: FAILED

---

## Blocker Summary

Zillapi is **out of credits** for this billing cycle and the MCP server entered an unreachable state after 102 consecutive failures. Per the real-estate-submarket-screening skill protocol:

> "If Zillapi is out of credits AND all web sources are blocked: report the blocker immediately — do not loop."

No listing data was retrieved. No listings were fabricated.

---

## Sources Attempted

| # | Source | Target | Result |
|---|---|---|---|
| 1 | Zillapi MCP | ZIP 44129, for_sale, ≤$190K, beds≥1 | `Error: Out of credits` |
| 2 | Zillapi MCP | ZIP 44134, for_sale, ≤$190K, beds≥1 | MCP server unreachable (102 failures) |
| 3 | Zillapi MCP | ZIP 44130, for_sale, ≤$190K, beds≥1 | MCP server unreachable (102 failures) |
| — | Zillow.com / Redfin / Trulia / Realtor.com | (any) | Not attempted — all block with captchas per known skill constraints |

---

## Manual Fallback URLs

Open these directly in a browser to view current listings:

- **44129:** https://www.zillow.com/homes/44129_rb/?searchQueryState={"pagination":{},"usersSearchTerm":"44129","mapBounds":{"west":-81.78,"east":-81.68,"south":41.37,"north":41.42},"regionSelection":[{"regionId":81158,"regionType":7}],"filterState":{"price":{"max":190000},"sort":{"value":"globalrelevanceex"},"ah":{"value":true}},"isMapVisible":true}

- **44134:** https://www.zillow.com/homes/44134_rb/?searchQueryState={"pagination":{},"usersSearchTerm":"44134","mapBounds":{"west":-81.72,"east":-81.65,"south":41.35,"north":41.40},"regionSelection":[{"regionId":81168,"regionType":7}],"filterState":{"price":{"max":190000},"sort":{"value":"globalrelevanceex"},"ah":{"value":true}},"isMapVisible":true}

- **44130:** https://www.zillow.com/homes/44130_rb/?searchQueryState={"pagination":{},"usersSearchTerm":"44130","mapBounds":{"west":-81.80,"east":-81.73,"south":41.35,"north":41.41},"regionSelection":[{"regionId":81165,"regionType":7}],"filterState":{"price":{"max":190000},"sort":{"value":"globalrelevanceex"},"ah":{"value":true}},"isMapVisible":true}

---

## Recovery Path

1. Top up Zillapi credits at https://zillapi.com/app/billing
2. Rerun this cron job, or re-trigger with: "Pull Parma listings under $190K"
3. The job will populate `parma-listings.md` with ranked tables and investor verdicts once credits are available

---

## Files Written

| File | Purpose |
|---|---|
| `/opt/data/parma-pull-status.txt` | Machine-readable status + error details |
| `/opt/data/parma-latest-listings.md` | Quick-reference (empty — no data) |
| `/opt/data/outputs/2026-09-17/parma-listings-under-190k/parma-listings.md` | This report |