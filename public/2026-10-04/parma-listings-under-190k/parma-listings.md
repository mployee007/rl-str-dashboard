# Parma West Listings Under $190K — Pull Failed

**Date:** 2026-10-04  
**Target ZIPs:** 44129, 44134, 44130  
**Price cap:** $190,000  
**Status:** ❌ ALL TIERS EXHAUSTED — No listings pulled

---

## Source Status

| Tier | Source | Result |
|------|--------|--------|
| 1 | Zillapi MCP (`search_listings`) | ❌ Out of credits |
| 2 | Camofox → Zillow (path-based URL) | ❌ Cloudflare "Press & Hold" captcha |
| 3 | SearXNG / agent_search | ⏭️ Skipped (unreliable for Parma, OH — returns Parma, Italy) |
| 4 | web_search / web_extract | ⏭️ Skipped (firecrawl blocked in cron locked-venv) |

---

## Manual Follow-Up URLs

Open these in your own browser (no captcha for human sessions):

| ZIP | Zillow Search URL |
|-----|-------------------|
| 44129 | https://www.zillow.com/homes/for_sale/44129_rb/1-_beds/0-190000_price/pricea_sort/ |
| 44134 | https://www.zillow.com/homes/for_sale/44134_rb/1-_beds/0-190000_price/pricea_sort/ |
| 44130 | https://www.zillow.com/homes/for_sale/44130_rb/1-_beds/0-190000_price/pricea_sort/ |

---

## Resumption Path

1. **If Zillapi credits refresh** — re-run the three `mcp_zillapi_search_listings` calls with the same bounding boxes
2. **If IP rotates** (new network/VPN) — Camofox navigation will succeed once
3. **Manual workaround** — open the URLs above, copy listing data, and feed it back to Hermes