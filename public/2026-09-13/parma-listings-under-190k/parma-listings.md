# Parma, OH — For-Sale Listings Under $190K

**Pull date:** 2026-09-13 (cron)  
**Status:** ❌ FAILED — Zillapi out of credits  
**ZIPs targeted:** 44129, 44134, 44130  
**Price cap:** $190,000  

---

## Blocker: Zillapi Credit Exhaustion

All three Zillapi calls failed. The credit pool for this billing cycle is depleted.

| Source | ZIP | Bounding Box | Result |
|--------|-----|-------------|--------|
| Zillapi MCP | 44129 | -81.78,41.37,-81.68,41.42 | Out of credits |
| Zillapi MCP | 44134 | -81.72,41.35,-81.65,41.40 | MCP server unreachable |
| Zillapi MCP | 44130 | -81.80,41.35,-81.73,41.41 | MCP server unreachable |
| Zillow.com (web) | — | — | Not attempted (PerimeterX captcha) |
| Redfin (web) | — | — | Not attempted (known blocker) |
| Trulia (web) | — | — | Not attempted (known blocker) |

---

## Direct Zillow Search URLs

Open these in your own browser to view current listings:

- **[ZIP 44129 — Under $190K](https://www.zillow.com/homes/for_sale/44129_rb/pricea_sort/41.417795,-81.678869,41.380286,-81.725947_rect/13_zm/0-190000_price/0-1891_mp/)**  
- **[ZIP 44134 — Under $190K](https://www.zillow.com/homes/for_sale/44134_rb/pricea_sort/41.40145,-81.651658,41.364573,-81.698121_rect/14_zm/0-190000_price/0-1253_mp/)**  
- **[ZIP 44130 — Under $190K](https://www.zillow.com/homes/for_sale/44130_rb/pricea_sort/41.411309,-81.734671,41.378002,-81.779947_rect/13_zm/0-190000_price/0-1891_mp/)**  

---

## Next Steps

1. Top up Zillapi credits at https://zillapi.com/app/billing  
2. Re-run this job (cron or manual trigger)  
3. Alternative: manually screenshot the Zillow links above and feed results back  

---

*Last updated: 2026-09-13 cron cycle*