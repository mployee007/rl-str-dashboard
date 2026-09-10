# Parma Listings Under $190K — Pull Report

**Date:** 2026-09-10
**Status:** ❌ BLOCKED — Zillapi credits exhausted

---

## Target ZIP Codes

| ZIP | Area | Bounding Box | Price Cap |
|-----|------|--------------|-----------|
| 44129 | Parma West, OH | `-81.78,41.37,-81.68,41.42` | $190,000 |
| 44134 | Parma, OH | `-81.72,41.35,-81.65,41.40` | $190,000 |
| 44130 | Parma / Middleburg Heights, OH | `-81.80,41.35,-81.73,41.41` | $190,000 |

---

## Source Results

| Source | Attempt | Result |
|--------|---------|--------|
| **Zillapi MCP** — 44129 | Called | ❌ "Out of credits for this cycle. Top up or upgrade at https://zillapi.com/app/billing." |
| **Zillapi MCP** — 44134 | Called (parallel) | ❌ "MCP server 'zillapi' is unreachable after 7 consecutive failures" |
| **Zillapi MCP** — 44130 | Called (parallel) | ❌ "MCP server 'zillapi' is unreachable after 7 consecutive failures" |
| Zillow.com | Skipped | ⛔ Known PerimeterX/Cloudflare captcha block |
| Redfin | Skipped | ⛔ Known captcha block |
| Realtor.com | Skipped | ⛔ Known captcha block |
| Trulia | Skipped | ⛔ Known captcha block |
| web_search | Skipped | ⛔ Skill instructs not to waste turns on blocked sources |

---

## Historical Context

A cron job (`Pull 44129 listings when Zillapi credits refresh`) has been running since 2026-09-04 with 3-hour intervals. **Every single run** has hit the same "out of credits" error. The credit pool has not refreshed in 6+ days.

---

## Direct Zillow Search URLs

Open these in your browser to view listings directly:

- **44129:** https://www.zillow.com/homes/for_sale/44129_rb/1-_beds/0-190000_price/
- **44134:** https://www.zillow.com/homes/for_sale/44134_rb/1-_beds/0-190000_price/
- **44130:** https://www.zillow.com/homes/for_sale/44130_rb/1-_beds/0-190000_price/

---

## Next Steps

1. **Top up Zillapi credits** at https://zillapi.com/app/billing
2. Consider disabling or pausing the cron job until credits are restored — it has been burning runs for 6 days with zero data retrieved
3. Delete `/opt/data/parma-pull-status.txt` on first successful pull

**No fabricated listings. No data was invented.**