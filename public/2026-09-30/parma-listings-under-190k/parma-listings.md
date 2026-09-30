# Parma Listings Under $190K — Pull Blocker Report

**Date:** 2026-09-30  
**Status:** ❌ BLOCKED — All data sources exhausted  
**ZIPs targeted:** 44129 (Parma West), 44134 (Parma SE), 44130 (Parma NE)

---

## Source Failure Report

| Tier | Source | Attempt | Result |
|------|--------|---------|--------|
| 1 | Zillapi MCP (`mcp_zillapi_search_listings`) | 44129 → out of credits; 44134/44130 → MCP unreachable (23 failures) | **Credit exhausted** — no retry possible this cycle |
| 2 | Camofox browser → Zillow.com | `https://www.zillow.com/homes/for_sale/44129_rb/1-_beds/0-190000_price/pricea_sort/` | **Cloudflare "Press & Hold" captcha** (Ref ID: f4b78e26-bcf2-11f1-aa15-0753c6d34d1d) — IP rate-limited; cannot solve |
| 3 | SearXNG / agent_search | `"44129 Parma Ohio homes for sale under 190000 2026"` | **Irrelevant results** — Bing returned Amazon/Firestick Reddit threads, not Zillow listings. 6 engines down (Brave/DuckDuckGo/Startpage captcha'd, AOL/KarmaSearch errors) |
| 4 | web_search / web_extract | Zillow URL direct | **firecrawl unavailable** — lazy installs disabled, cannot install in cron |

---

## Direct Zillow Links (open in your browser)

| ZIP | URL |
|-----|-----|
| 44129 (Parma West) | [Zillow: 44129 ≤$190K](https://www.zillow.com/homes/for_sale/44129_rb/1-_beds/0-190000_price/pricea_sort/) |
| 44134 (Parma SE) | [Zillow: 44134 ≤$190K](https://www.zillow.com/homes/for_sale/44134_rb/1-_beds/0-190000_price/pricea_sort/) |
| 44130 (Parma NE) | [Zillow: 44130 ≤$190K](https://www.zillow.com/homes/for_sale/44130_rb/1-_beds/0-190000_price/pricea_sort/) |

---

## Next Steps

1. **Zillapi credits refresh** — resume automated pulls when the billing cycle resets (https://zillapi.com/app/billing)
2. **Camofox IP rotation** — the Cloudflare captcha is IP-based. A new IP (VPN rotation, server restart with new IP) would give one clean page load per ZIP
3. **Manual browser** — use the direct Zillow links above to review listings immediately

The Parma submarket screening can resume automatically once any data source becomes available again.