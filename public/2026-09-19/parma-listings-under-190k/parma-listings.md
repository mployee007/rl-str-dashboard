# Parma Listings Under $190K — Pull Report

**Date:** September 19, 2026  
**Status:** ❌ BLOCKED — Zillapi out of credits + MCP server unreachable  
**ZIPs targeted:** 44129, 44134, 44130  
**Price cap:** $190,000

---

## Source Attempts

| # | Source | ZIP(s) | Result |
|---|--------|--------|--------|
| 1 | Zillapi MCP `search_listings` | 44129 | **Out of credits** — "Top up or upgrade at https://zillapi.com/app/billing" |
| 2 | Zillapi MCP `search_listings` | 44134 | **MCP server unreachable** — 114 consecutive failures, retry in ~58s |
| 3 | Zillapi MCP `search_listings` | 44130 | **MCP server unreachable** — 114 consecutive failures, retry in ~58s |

No web fallback attempted per skill guidance (Zillow/Redfin/Trulia all block with captchas).

---

## Manual Fallback — Direct Zillow Links

Open these in a browser to manually screen while credits are down:

| ZIP | Neighborhood | Zillow Search |
|-----|-------------|---------------|
| 44129 | Parma West | [Zillow →](https://www.zillow.com/homes/for_sale/44129_house_type/190000-_price/0_singlestory/) |
| 44134 | Parma South / Seven Hills | [Zillow →](https://www.zillow.com/homes/for_sale/44134_house_type/190000-_price/0_singlestory/) |
| 44130 | Parma Heights / Middleburg | [Zillow →](https://www.zillow.com/homes/for_sale/44130_house_type/190000-_price/0_singlestory/) |

---

## Required to Resume

1. **Top up Zillapi credits** at https://zillapi.com/app/billing
2. **Verify MCP server** — the `zillapi` MCP server has 114+ consecutive failures and may need a restart or reconnection
3. **Re-run this cron job** once both are green

Status file saved at: `/opt/data/parma-pull-status.txt`