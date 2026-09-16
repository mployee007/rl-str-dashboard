# Parma Submarket Listing Screen — Under $190K
**Date:** 2026-09-16
**Status:** ⛔ BLOCKED — Zillapi credits exhausted

---

## Source Attempts

| Source | Method | Result |
|---|---|---|
| Zillapi (primary) | `mcp_zillapi_search_listings` | ❌ Out of credits |
| Zillapi retry 1 | `mcp_zillapi_search_listings` | ❌ MCP server unreachable |
| Zillapi retry 2 | `mcp_zillapi_search_listings` | ❌ MCP server unreachable |

No web-based alternatives were attempted — Zillow.com, Redfin, Trulia, Realtor.com, and Homes.com all block automated access with PerimeterX/Cloudflare captchas and are known failures per the skill playbook.

---

## Direct Zillow Search URLs (Manual Fallback)

Open these in your own browser to view current listings:

- **ZIP 44129 (Parma West):** https://www.zillow.com/homes/for_sale/44129_house_type/0-190000_price/0-2800_mp/
- **ZIP 44134 (Parma):** https://www.zillow.com/homes/for_sale/44134_house_type/0-190000_price/0-2473_mp/
- **ZIP 44130 (Middleburg Heights):** https://www.zillow.com/homes/for_sale/44130_house_type/0-190000_price/0-2595_mp/

---

## Next Steps

1. **Top up Zillapi credits** at https://zillapi.com/app/billing
2. **Re-run this cron job** — it will auto-resume and populate the listing tables
3. Status file at `/opt/data/parma-pull-status.txt` will be updated on next successful run

No listings were fabricated. All fields are empty pending a successful Zillapi pull.