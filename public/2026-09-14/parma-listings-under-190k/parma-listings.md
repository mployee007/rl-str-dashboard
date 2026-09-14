# Parma Listings Under $190K — Pull Failed (Out of Credits)

**Date:** 2026-09-14 04:43 UTC  
**Status:** ❌ Zillapi credits exhausted

## Blockers

| Source | Result |
|---|---|
| Zillapi MCP | Out of credits |
| Zillapi MCP (retries) | Server unreachable after initial credit rejection |
| Web scraping (Zillow, Redfin, Trulia, etc.) | Not attempted — all known to block with captchas |

## Direct Zillow Links

Open these in a browser to manually review:

- **[44129 — Parma West, under $190K](https://www.zillow.com/homes/for_sale/44129/0-190000_price/0-2000_mp/)**
- **[44134 — Parma, under $190K](https://www.zillow.com/homes/for_sale/44134/0-190000_price/0-2000_mp/)**
- **[44130 — Parma, under $190K](https://www.zillow.com/homes/for_sale/44130/0-190000_price/0-2000_mp/)**

## To Resume

Top up credits at https://zillapi.com/app/billing — the cron job will re-run and produce the full listing table with investor verdicts automatically.

---
*No listings were fabricated. This report reflects actual tool results.*