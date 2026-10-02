# Parma West Area Listings — Under $190K

**Run date:** 2026-10-02 21:02 UTC  
**Status:** ⛔ BLOCKED — All data sources exhausted  
**Target ZIPs:** 44129 (Parma West), 44134 (Parma South), 44130 (Parma Hts / Middleburg)  
**Price cap:** $190,000  
**Property type:** For-sale houses, 1+ bedrooms  

---

## Source Attempts

| Source | Result |
|--------|--------|
| **Zillapi** (`mcp_zillapi_search_listings`) | ❌ **Out of credits.** First call returned clean error. Second and third calls hit MCP server unreachable (32 consecutive failures). Cannot retry. |
| **Camofox → Zillow** (`browser_navigate`) | ❌ **Cloudflare "Press & Hold" captcha.** IP is rate-limited (likely from prior session). Camofox cannot solve this challenge type (HTTP 422). No navigation succeeded. |
| **Rentdata.org** | ❌ Known unreliable — MSA URLs 404, agent_search falls through to Wikipedia. |
| **SearXNG / agent_search** | ❌ Not viable — Parma OH resolves to Parma, Italy regardless of qualifiers. |

---

## Rent Baselines (for when data comes through)

Cleveland-Elyria MSA FY2025 HUD Fair Market Rents (40th percentile gross):

| Unit | MSA FMR | Parma Adj (90%) |
|------|---------|-----------------|
| 1BR | $903 | $813 |
| 2BR | $1,098 | $988 |
| 3BR | $1,553 | $1,398 |
| 4BR | $1,810 | $1,629 |

⚠️ All rent figures are market-derived — NOT property-specific.

---

## Manual Follow-Up Links

Open these in your own browser to see live listings:

- **44129 (Parma West):** https://www.zillow.com/homes/for_sale/44129_rb/1-_beds/0-190000_price/pricea_sort/
- **44134 (Parma South):** https://www.zillow.com/homes/for_sale/44134_rb/1-_beds/0-190000_price/pricea_sort/
- **44130 (Parma Hts / Middleburg):** https://www.zillow.com/homes/for_sale/44130_rb/1-_beds/0-190000_price/pricea_sort/

---

## Investor Quick-Reference Buy Box (from FMR anchors)

Using Parma-adjusted FMRs at 90% of MSA with target gross yield ≥ 9%:

| Property Type | Target Basis Ceiling | Stretch Basis | Target Monthly Rent | Target GRM |
|---------------|---------------------|---------------|---------------------|------------|
| 2BR SFR | $132,000 | $145,000 | $988 | 11.1 |
| 3BR SFR | $186,000 | $205,000 | $1,398 | 11.1 |
| 2-unit (2×2BR) | $190,000 | $210,000 | $1,976 | 8.0 |
| 3-unit (3×2BR) | $285,000 | $315,000 | $2,964 | 8.0 |
| 4-unit (4×2BR) | $380,000 | $420,000 | $3,952 | 8.0 |

**Verdict at $190K cap:** The 2BR SFR and 3BR SFR segments work at the cap. Duplexes at $190K would need ~$1,980/mo gross to hit a 10%+ yield — tight but possible if both units rent near FMR. Small multifamily (3-4 units) won't fit under $190K in this market.

---

## Resolution

To unblock:
1. **Top up Zillapi credits** at https://zillapi.com/app/billing — then re-run this cron job.
2. Or **change the IP** for Camofox (VPN, proxy rotation, or wait for the Cloudflare rate limit to expire).
3. Or **open the manual Zillow links above** and copy listing data into a reply — I'll process it into the report format.

The pipeline infrastructure is intact — just needs a working data window.