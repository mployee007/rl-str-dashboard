# Parma West Area Listings Under $190K — Pull Failed
**Generated:** 2026-09-29 | **Status:** BLOCKED — all data sources exhausted

---

## Blocked: No live listings available

| Source | ZIP 44129 | ZIP 44134 | ZIP 44130 |
|--------|-----------|-----------|-----------|
| **Zillapi (Tier 1)** | ❌ Out of credits | ❌ Server unreachable | ❌ Server unreachable |
| **Camofox → Zillow (Tier 2)** | ❌ Cloudflare captcha | ❌ Not attempted (IP blocked) | ❌ Not attempted (IP blocked) |
| **SearXNG (Tier 3)** | ❌ European namesake bias | ❌ Not attempted | ❌ Not attempted |
| **web_search/web_extract (Tier 4)** | ❌ firecrawl not installed | ❌ firecrawl not installed | ❌ firecrawl not installed |

---

## Manual follow-up URLs

Open these in a regular browser to see current listings:

| ZIP | Direct Zillow Link |
|-----|-------------------|
| **44129** (Parma West) | [zillow.com](https://www.zillow.com/homes/for_sale/44129_rb/1-_beds/0-190000_price/pricea_sort/) |
| **44134** (Parma South) | [zillow.com](https://www.zillow.com/homes/for_sale/44134_rb/1-_beds/0-190000_price/pricea_sort/) |
| **44130** (Middleburg Hts) | [zillow.com](https://www.zillow.com/homes/for_sale/44130_rb/1-_beds/0-190000_price/pricea_sort/) |

---

## What's needed to unblock

1. **Top up Zillapi credits** → https://zillapi.com/app/billing (then re-run this cron job)
2. **Run from a clean residential IP** → the Camofox proxy IP is Cloudflare-flagged
3. **Manual pull** → open the URLs above and paste results back into the conversation

---

## Context for when this resumes

- **MSA:** Cleveland-Elyria, OH MSA
- **FY2025 3BR FMR:** $1,553/mo (40th percentile, HUD)
- **Target ZIPs:** 44129 (Parma West), 44134 (Parma South), 44130 (Middleburg Heights)
- **Price cap:** $190,000
- **Strategy:** Value-add SFR / small multifamily in working-class Cleveland suburbs
- **Previous session context:** These ZIPs identified as viable submarkets in the Cleveland metro screen; need live pricing data to build the buy box

⚠️ **No listings were fabricated.** This report reflects genuine tool failures only.