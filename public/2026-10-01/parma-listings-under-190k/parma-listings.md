# Parma West Listings — Pull Status

**Pull date:** 2026-10-01  
**Target ZIPs:** 44129, 44134, 44130  
**Max price:** $190,000  
**Status: ❌ BLOCKED — all data sources exhausted**

---

## Source Status

| Tier | Source | Result |
|------|--------|--------|
| 1 | Zillapi MCP (`mcp_zillapi_search_listings`) | **Out of credits.** First call returned "Out of credits for this cycle." Subsequent calls returned "MCP server unreachable." |
| 2 | Camofox browser → Zillow search results | **Cloudflare "Press & Hold" captcha.** First navigation to `https://www.zillow.com/homes/for_sale/44129_rb/1-_beds/0-190000_price/pricea_sort/` hit captcha immediately — IP already flagged from prior Zillow activity. |
| 3 | SearXNG / agent_search | Not attempted — unreliable for Ohio cities with European names per skill guidance. |
| 4 | web_search / web_extract | Not attempted — requires firecrawl which is unavailable in cron. |

---

## Resolution

**Zillapi:** Credits refresh per billing cycle. Check status at https://zillapi.com/app/billing.

**Camofox:** IP-based Cloudflare rate limiting. Options:
- Wait for Cloudflare cooldown (typically 24 hours for a clean IP)
- Use a different IP (VPN rotation)
- Resume from a different network

---

## Direct Zillow URLs (open in your own browser)

These path-based URLs are pre-configured for each ZIP with the correct filters:

- **44129 (Parma West):** https://www.zillow.com/homes/for_sale/44129_rb/1-_beds/0-190000_price/pricea_sort/
- **44134 (Parma South):** https://www.zillow.com/homes/for_sale/44134_rb/1-_beds/0-190000_price/pricea_sort/
- **44130 (Parma Heights area):** https://www.zillow.com/homes/for_sale/44130_rb/1-_beds/0-190000_price/pricea_sort/

---

## Rent Anchors (for manual screening)

Cleveland-Elyria MSA FY2025 FMR (40th percentile), Parma adjustment = 90%:

| Unit | MSA FMR | Parma Est. |
|------|---------|------------|
| 2BR | $1,098 | $988 |
| 3BR | $1,553 | $1,398 |
| 4BR | $1,810 | $1,629 |

⚠️ Market-derived — NOT property-specific. Use as screening baseline.

---

## Next pull attempt

Recommend retrying on or after Zillapi credit refresh. The report template is ready — once data is available, the full ranked table with verdicts will populate immediately.