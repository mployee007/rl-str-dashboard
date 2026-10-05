# Parma West Active For-Sale Listings — Under $190K

**Pull date:** 2026-10-05  
**ZIP codes:** 44129, 44134, 44130  
**Max price:** $190,000  
**Min beds:** 1  
**Status:** ❌ BLOCKED — No live data retrieved

---

## Source Tier Results

| Tier | Source | Result |
|------|--------|--------|
| 1 | Zillapi MCP | Out of monthly credits (1,000 exhausted) |
| 2 | Camofox → Zillow.com | Cloudflare "Press & Hold" captcha (ref: `930f0d5d-c0ba-11f1-b5d6-c260894df449`) |
| 3 | SearXNG / agent_search | Skipped — unreliable for Ohio city names |
| 4 | web_search / web_extract | Skipped — firecrawl-py unavailable in cron |

---

## Rent Context (FY2025 HUD FMR — Cleveland-Elyria MSA)

Used for yield estimation when listings become available:

| Unit Size | MSA FMR | Parma Adj. (90%) |
|-----------|---------|-------------------|
| 1BR | $903 | $813 |
| 2BR | $1,098 | $988 |
| 3BR | $1,553 | $1,398 |
| 4BR | $1,810 | $1,629 |

⚠️ Market-derived — NOT property-specific.

---

## Direct Zillow Search URLs (Manual Follow-Up)

Open these in your own browser to view current listings:

| ZIP | Link |
|-----|------|
| **44129** (Parma West) | [Zillow →](https://www.zillow.com/homes/for_sale/44129_rb/1-_beds/0-190000_price/pricea_sort/) |
| **44134** (Parma East/Seven Hills) | [Zillow →](https://www.zillow.com/homes/for_sale/44134_rb/1-_beds/0-190000_price/pricea_sort/) |
| **44130** (Middleburg Hts / SW Parma) | [Zillow →](https://www.zillow.com/homes/for_sale/44130_rb/1-_beds/0-190000_price/pricea_sort/) |

---

## Verdict Framework (for when data is available)

Using Cleveland-Elyria MSA FY2025 FMRs with 90% Parma adjustment:

| Bedrooms | Est. Monthly Rent | Annual Gross | Target Yield | Max Basis at Yield |
|----------|------------------:|-------------:|:------------:|--------------------:|
| 2BR | $988 | $11,856 | 9.5%+ | $124,800 |
| 3BR | $1,398 | $16,776 | 9.5%+ | $176,600 |
| 4BR | $1,629 | $19,548 | 9.5%+ | $205,800 |

**Verdict logic:**
- **TAKE:** Yield ≥ 9.5%, tax gap < 30%, DOM < 60 days
- **NEGOTIATE:** Yield 8.0–9.4%, or tax gap 30–40%, or DOM > 60 days
- **PASS:** Yield < 8.0%, or tax gap > 40%, or 2BR priced > $180K

---

## Next Steps

1. **Retry when Zillapi credits refresh** — the monthly cycle resets at the billing date.
2. **Manual browser pull** — open the direct Zillow URLs above and paste the listing table back.
3. **Camofox cooldown** — the IP-based Cloudflare rate limit may clear after 30–60 minutes.

Status file: `/opt/data/parma-pull-status.txt`