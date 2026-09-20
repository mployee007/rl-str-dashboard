# Parma Listings Under $190K — BLOCKED

**Generated:** 2026-09-20T21:28:27Z  
**Status:** ❌ Zillapi credits exhausted

---

## Blocker Summary

Zillapi returned `"Out of credits for this cycle"` on the first pull attempt for ZIP 44129. The two subsequent parallel calls for 44134 and 44130 failed with `"MCP server unreachable"` (126 consecutive failures). Per the `real-estate-submarket-screening` skill protocol, no alternate sites were attempted — Zillow.com, Redfin, Trulia, and all other listing sites block automated access with captchas.

## Sources Tried

| Source | Result |
|---|---|
| Zillapi MCP (`search_listings`, bbox for 44129) | ❌ Out of credits |
| Zillapi MCP (`search_listings`, bbox for 44134) | ❌ MCP server unreachable |
| Zillapi MCP (`search_listings`, bbox for 44130) | ❌ MCP server unreachable |

## Manual Fallback — Direct Zillow Links

Open in your browser to run the same screen manually:

- **ZIP 44129 (Parma West):** [Zillow: Houses under $190K](https://www.zillow.com/parma-west-parma-oh-44129/houses/0-190000/)
- **ZIP 44134 (Parma East):** [Zillow: Houses under $190K](https://www.zillow.com/parma-oh-44134/houses/0-190000/)
- **ZIP 44130 (Middleburg Heights / Parma SW):** [Zillow: Houses under $190K](https://www.zillow.com/middleburg-heights-oh-44130/houses/0-190000/)

## Resolution

1. Top up Zillapi credits at https://zillapi.com/app/billing
2. Re-run this cron job — it will pick up fresh listings automatically
3. Status file at `/opt/data/parma-pull-status.txt` will be overwritten on success