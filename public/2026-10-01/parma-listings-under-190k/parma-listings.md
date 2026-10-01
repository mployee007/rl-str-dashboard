# Parma-Area Listings Under $190K — Pull Report

**Date:** 2026-10-01  
**Status:** BLOCKED — All data sources exhausted  
**ZIPs targeted:** 44129 (Parma West), 44134 (Parma South), 44130 (Parma Heights/Middleburg)  
**Search criteria:** 1+ beds, max $190,000, for-sale only

---

## Source status

| Tier | Source | Status | Detail |
|------|--------|--------|--------|
| 1 | Zillapi MCP | ❌ Out of credits | `"Out of credits for this cycle. Top up or upgrade at https://zillapi.com/app/billing."` |
| 2 | Camofox → Zillow | ❌ Captcha-blocked | Cloudflare "Press & Hold" challenge on first navigation (Ref ID `95b0e688-bd58-11f1-9a90-56c110b40746`). IP-level rate limit — browser restart does not help. |
| 3 | SearXNG / agent_search | ⛔ Unreliable | Returns European namesake cities (Parma, Italy) for Ohio ZIP queries. Not suitable for listing discovery. |
| 4 | web_search / web_extract | ⛔ Unavailable | `firecrawl-py` not installed; venv is locked in cron. Cannot install. |

---

## Direct Zillow links for manual review

Open these in your own browser:

- **44129 (Parma West):**  
  https://www.zillow.com/homes/for_sale/44129_rb/1-_beds/0-190000_price/pricea_sort/

- **44134 (Parma South):**  
  https://www.zillow.com/homes/for_sale/44134_rb/1-_beds/0-190000_price/pricea_sort/

- **44130 (Parma Heights / Middleburg Hts):**  
  https://www.zillow.com/homes/for_sale/44130_rb/1-_beds/0-190000_price/pricea_sort/

---

## Recommended next steps

1. **Top up Zillapi credits** — this is the cleanest path for automated, structured data extraction: https://zillapi.com/app/billing
2. **Wait for IP rotation** — if Camofox is on a VPS/dedicated IP, the Cloudflare rate limit may clear after 24+ hours
3. **Manual screen via the links above** — the path-based URLs are pre-configured for price-ascending sort under $190K

---

## Rent anchors for manual screening (FY2025 HUD FMR)

| Bedrooms | Cleveland-Elyria MSA FMR |
|----------|--------------------------|
| 1 BR | $993 |
| 2 BR | $1,234 |
| 3 BR | $1,553 |
| 4 BR | $1,871 |

**Parma-specific adjustment:** Apply ~88–92% of MSA FMR for 44129 (working-class inner-ring suburb).

| Bedrooms | Estimated Parma rent |
|----------|---------------------|
| 1 BR | ~$874–914 |
| 2 BR | ~$1,086–1,135 |
| 3 BR | ~$1,367–1,429 |
| 4 BR | ~$1,646–1,721 |

⚠️ These are market-derived estimates — NOT property-specific rent data.

---

## Quick underwriting thresholds (for manual screening)

These are the buy-box thresholds from the existing Parma submarket analysis:

| Property type | Max all-in basis | Target monthly rent | Target gross yield |
|---------------|-----------------|---------------------|-------------------|
| 1-unit (SFR) | $165,000 | $1,200+ | ~8.7%+ |
| 2-unit (duplex) | $190,000 | $2,000+ | ~12.6%+ |
| 3-unit | $225,000 | $2,700+ | ~14.4%+ |
| 4-unit | $280,000 | $3,400+ | ~14.6%+ |

---

*This pull will automatically retry on the next scheduled cron run. To force an immediate retry, top up Zillapi credits or rotate the Camofox IP.*