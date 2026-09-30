# Parma West Listings — Pull Blocked

**Date:** 2026-09-30
**Task:** Pull active for-sale house listings in ZIPs 44129, 44134, 44130 (max $190K)
**Status:** ❌ ALL SOURCES BLOCKED — zero listings retrieved

---

## Source Status Table

| Tier | Source | Result |
|------|--------|--------|
| 1 | **Zillapi MCP** | Out of credits. First call returned clean error; subsequent calls unreachable (MCP server down after 49 consecutive failures). |
| 2 | **Camofox → Zillow search results** | Cloudflare "Press & Hold" captcha on first navigation. IP is rate-limited from prior sessions. Cannot solve captcha. |
| 3 | **agent_search / SearXNG** | Returns Parma, Italy results. "Parma Ohio" qualifier ignored. Bing-only engine; all others (Brave, DuckDuckGo, Startpage) rate-limited/captcha'd. |
| 4 | **web_search / web_extract** | firecrawl-py not installed. `security.allow_lazy_installs=false` prevents auto-install in cron mode. |

## Direct Zillow URLs (manual follow-up)

The user can open these in their own browser:

- **ZIP 44129**: https://www.zillow.com/homes/for_sale/44129_rb/1-_beds/0-190000_price/pricea_sort/
- **ZIP 44134**: https://www.zillow.com/homes/for_sale/44134_rb/1-_beds/0-190000_price/pricea_sort/
- **ZIP 44130**: https://www.zillow.com/homes/for_sale/44130_rb/1-_beds/0-190000_price/pricea_sort/

## Rent Anchor (for screening when listings become available)

Cleveland-Elyria MSA FY2025 FMR, Parma adjustment (90% of MSA):

| Unit | MSA FMR | Parma Est. |
|------|---------|------------|
| 2BR | $1,098 | ~$988 |
| 3BR | $1,553 | ~$1,398 |
| 4BR | $1,810 | ~$1,629 |

## Next Steps

- Resume when Zillapi credits refresh (https://zillapi.com/app/billing)
- OR when Camofox gets a fresh IP (captcha is IP-based, not session-based)
- The direct Zillow URLs above can be used for manual screening