# Parma Listings Under $190K — Pull Report

**Date:** 2026-09-21
**Status:** ❌ FAILED

## Summary

The scheduled pull for ZIP codes **44129**, **44134**, and **44130** (max price $190,000) could not be completed. Zillapi is out of credits, and the MCP server became unreachable during the batch attempt.

---

## Error Details

| ZIP | Bounding Box | Error |
|-----|-------------|-------|
| 44129 | `-81.78,41.37,-81.68,41.42` | Zillapi: "Out of credits for this cycle." |
| 44134 | `-81.72,41.35,-81.65,41.40` | MCP server unreachable (13 failures) |
| 44130 | `-81.80,41.35,-81.73,41.41` | MCP server unreachable (13 failures) |

---

## Sources Tried

| Source | Outcome |
|--------|---------|
| Zillapi MCP (primary) | Credits exhausted + server unreachable |
| Zillow.com | Blocked by captcha (known) |
| Redfin | Blocked by captcha (known) |
| Realtor.com / Trulia / Homes.com | Blocked by captcha (known) |

---

## Fallback: Direct Zillow Links

Open these in your browser to view current listings manually:

- **[44129 – Parma West](https://www.zillow.com/parma-oh-44129/houses/under-190000_sort/)** (under $190K)
- **[44134 – Parma South](https://www.zillow.com/parma-oh-44134/houses/under-190000_sort/)** (under $190K)
- **[44130 – Middleburg Heights / Parma Heights](https://www.zillow.com/middleburg-heights-oh-44130/houses/under-190000_sort/)** (under $190K)

---

## Action Required

1. **Top up Zillapi credits** at https://zillapi.com/app/billing
2. **Re-run** the cron job (or trigger manually) — the bounding boxes, output paths, and formatting are all pre-configured
3. The job will auto-populate `/opt/data/parma-latest-listings.md` with the live table on success

No listings were fabricated. No manual fallback succeeded.