# Parma Listings Under $190K — PULL FAILED (2026-09-16)

## Bottom Line
❌ **No data retrieved.** Zillapi is out of credits and the MCP server is unreachable. No live listings were pulled for any of the three target ZIPs.

---

## Blocker Details

| Source | Target | Result |
|---|---|---|
| Zillapi MCP | 44129 (Parma West) | `Out of credits for this cycle` |
| Zillapi MCP | 44134 (Parma South) | `MCP server unreachable (90 failures)` |
| Zillapi MCP | 44130 (Parma Heights) | `MCP server unreachable (90 failures)` |
| Zillow.com | Any | ⛔ Not attempted — PerimeterX/Cloudflare block (known) |
| Redfin, Trulia, Realtor.com | Any | ⛔ Not attempted — captcha-blocked (known) |
| web_search / web_extract | Any | ⛔ Not attempted — known to fail on listing sites |

---

## Direct Zillow Search Links (manual browser)
| ZIP | Area | Live Zillow Link |
|---|---|---|
| 44129 | Parma West | [View listings](https://www.zillow.com/homes/for_sale/44129_rb/0-190000_price/0-2513_mp/) |
| 44134 | Parma South | [View listings](https://www.zillow.com/homes/for_sale/44134_rb/0-190000_price/0-2513_mp/) |
| 44130 | Parma Heights / Middleburg | [View listings](https://www.zillow.com/homes/for_sale/44130_rb/0-190000_price/0-2513_mp/) |

---

## Recovery Plan
1. **Top up credits:** https://zillapi.com/app/billing
2. **Verify MCP server:** Check Zillapi MCP connectivity (`mcp_zillapi_search_listings` should return data, not unreachable errors)
3. **Re-run:** Either let the cron job pick up on next cycle or trigger manually
4. **Resume from status:** `/opt/data/parma-pull-status.txt` tracks the last attempt timestamp

---

## Files Written
- `/opt/data/parma-pull-status.txt` — detailed error log
- `/opt/data/parma-latest-listings.md` — summary + direct links
- `/opt/data/outputs/2026-09-16/parma-listings-under-190k/parma-listings.md` — this file