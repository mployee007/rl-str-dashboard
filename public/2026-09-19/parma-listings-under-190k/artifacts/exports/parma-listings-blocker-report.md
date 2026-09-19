# Parma Listings Under $190K — Blocker Report

**Date:** 2026-09-19
**Task:** Pull active for-sale house listings in ZIPs 44129, 44134, 44130 (max $190K)
**Status:** ❌ ALL SOURCES EXHAUSTED

---

## Source Attempts

| # | Source | Target | Result |
|---|--------|--------|--------|
| 1 | `mcp_zillapi_search_listings` | ZIP 44129 bbox | ❌ `Out of credits for this cycle.` |
| 2 | `mcp_zillapi_search_listings` | ZIP 44134 bbox | ❌ `MCP server 'zillapi' unreachable (116 failures)` |
| 3 | `mcp_zillapi_search_listings` | ZIP 44130 bbox | ❌ `MCP server 'zillapi' unreachable (116 failures)` |
| 4 | `web_search` (firecrawl) | ZIP 44129 query | ❌ `firecrawl-py not installed` |
| 5 | `web_search` (firecrawl) | ZIP 44134 query | ❌ `firecrawl-py not installed` |
| 6 | `web_search` (firecrawl) | ZIP 44130 query | ❌ `firecrawl-py not installed` |

## Direct Zillow Search URLs

Copy these into your browser to view listings manually:

- **ZIP 44129 (Parma West):** https://www.zillow.com/homes/for_sale/44129_rb/0-190000_price/0-464_mp/
- **ZIP 44134:** https://www.zillow.com/homes/for_sale/44134_rb/0-190000_price/0-464_mp/
- **ZIP 44130:** https://www.zillow.com/homes/for_sale/44130_rb/0-190000_price/0-464_mp/

## Root Cause

1. **Zillapi credits exhausted** — the account has hit its cycle limit. Top up at https://zillapi.com/app/billing
2. **MCP server degraded** — after the first credit-rejection, subsequent calls return "unreachable" (likely rate-limit cooldown from the failed calls)
3. **web_search unavailable** — `firecrawl-py==4.17.0` is not installed and `security.allow_lazy_installs=false` blocks auto-install

## Resolution Paths

| Priority | Action | Expected Result |
|----------|--------|-----------------|
| 1 | Top up Zillapi credits | Immediate unblock — Zillapi is the only reliable source |
| 2 | Install firecrawl: `uv pip install firecrawl-py==4.17.0` | Enables web_search (but Zillow/Redfin will still captcha-block) |
| 3 | Wait for next cron cycle | Automatic retry when Zillapi credits refresh |

---

_Report saved to `/opt/data/parma-pull-status.txt` and `/opt/data/parma-latest-listings.md`_