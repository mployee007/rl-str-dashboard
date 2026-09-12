# Parma West Area — Listings Under $190K

**Pull date:** 2026-09-12 (cron)
**Target ZIPs:** 44129, 44134, 44130
**Price ceiling:** $190,000

---

## ⛔ Pull Failed — Zillapi Out of Credits

This report could not be generated. Zillapi returned:

- **44129:** `Out of credits for this cycle.`
- **44134:** `MCP server unreachable`
- **44130:** `MCP server unreachable`

No listings were captured. No data was fabricated.

---

## Sources Attempted

| Source | Method | Result |
|---|---|---|
| Zillapi (44129) | `mcp_zillapi_search_listings` | Out of credits |
| Zillapi (44134) | `mcp_zillapi_search_listings` | Server unreachable (62 failures) |
| Zillapi (44130) | `mcp_zillapi_search_listings` | Server unreachable (62 failures) |
| Zillow.com | Not attempted — blocked by PerimeterX/Cloudflare (per skill guidance) |
| Redfin.com | Not attempted — blocked by captcha (per skill guidance) |
| Trulia.com | Not attempted — blocked by captcha (per skill guidance) |
| Realtor.com | Not attempted — blocked by captcha (per skill guidance) |

---

## Manual Fallback

Open these URLs in your browser to view current listings manually:

- **ZIP 44129 (Parma):** https://www.zillow.com/homes/for_sale/44129_rb/0-190000_price/0-10000000_mp/
- **ZIP 44134 (Parma):** https://www.zillow.com/homes/for_sale/44134_rb/0-190000_price/0-10000000_mp/
- **ZIP 44130 (Parma):** https://www.zillow.com/homes/for_sale/44130_rb/0-190000_price/0-10000000_mp/

---

## Next Automatic Attempt

This cron job will retry on the next scheduled run. To force a manual pull once credits are restored, top up at https://zillapi.com/app/billing and re-run.