# Parma West — Active Listings Under $190K

**Pull date:** 2026-10-05  
**ZIP codes:** 44129 (Parma West), 44134 (Parma SE), 44130 (Parma SW)  
**Price cap:** $190,000  
**Status:** ❌ BLOCKED — no listings captured

---

## Blocker Summary

| Source | ZIP | Result |
|--------|-----|--------|
| Zillapi MCP | 44129 | Out of credits |
| Zillapi MCP | 44134 | MCP server unreachable (credit cascade) |
| Zillapi MCP | 44130 | MCP server unreachable (credit cascade) |
| Camofox → Zillow | 44129 | Cloudflare "Press & Hold" captcha |
| Camofox → Zillow | 44134 | Not attempted (IP rate-limited) |
| Camofox → Zillow | 44130 | Not attempted (IP rate-limited) |

---

## Rent Anchors for Manual Screening

Use these when evaluating listings manually. From HUD FY2025 Fair Market Rents (Cleveland-Elyria MSA), adjusted to Parma submarket (90%):

| Unit Size | MSA FMR | Parma Adjusted | Est. Monthly |
|-----------|---------|----------------|--------------|
| 2BR | $1,098 | 90% | ~$988 |
| 3BR | $1,553 | 90% | ~$1,398 |
| 4BR | $1,810 | 90% | ~$1,629 |

⚠️ All rent figures are market-derived estimates — NOT property-specific.

---

## Buy Box Reference (from prior Parma thesis)

| Property Type | Target Basis | Stretch Basis | Target Rent/mo | Target Gross Yield |
|--------------|-------------|---------------|----------------|-------------------|
| 2BR SFR | ≤$140K | ≤$165K | ≥$988 | ≥8.5% |
| 3BR SFR | ≤$160K | ≤$190K | ≥$1,398 | ≥10.5% |
| Duplex | ≤$170K | ≤$190K | ≥$850/unit | ≥12% |
| 3-4 Unit | ≤$190K | ≤$220K | ≥$750/unit | ≥14% |

---

## Direct Zillow URLs (open in your own browser)

- **44129:** https://www.zillow.com/homes/for_sale/44129_rb/1-_beds/0-190000_price/pricea_sort/
- **44134:** https://www.zillow.com/homes/for_sale/44134_rb/1-_beds/0-190000_price/pricea_sort/
- **44130:** https://www.zillow.com/homes/for_sale/44130_rb/1-_beds/0-190000_price/pricea_sort/

---

## Next Steps

1. **Open the three URLs above** in a non-flagged browser to manually screen.
2. **Re-run this cron job** after Zillapi credits refresh — both tiers should recover.
3. **Consider a residential proxy or different IP** for Camofox if captcha persists.

---

*Status file: /opt/data/parma-pull-status.txt*