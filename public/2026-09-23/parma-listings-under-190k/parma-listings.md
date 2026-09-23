# Parma West Listings — Under $190K

**Pull date:** 2026-09-23
**Status:** ❌ BLOCKED — Zillapi out of credits
**Price cap:** $190,000
**Target ZIPs:** 44129 (Parma West), 44134 (Parma South), 44130 (Parma Heights)

---

## Blocker Report

| Source | Result |
|--------|--------|
| Zillapi MCP (`mcp_zillapi_search_listings`) | ❌ Out of credits for this cycle |
| Redfin / Zillow / Trulia / Realtor.com | ⛔ All block with Cloudflare/PerimeterX captchas — not attempted per skill instructions |
| Web search / web extract | ⛔ Known to fail for listing data — not attempted |

**Resolution:** Top up Zillapi credits at https://zillapi.com/app/billing — then re-run this pull.
**Estimated credit cost for this pull:** 3 calls (one per ZIP).

---

## Manual Fallback — Zillow Search URLs

Open these in your browser to see current listings under $190K:

### 44129 — Parma West
> https://www.zillow.com/homes/for_sale/44129_rb/?searchQueryState={"pagination":{},"usersSearchTerm":"44129","mapBounds":{"west":-81.81,"east":-81.65,"south":41.35,"north":41.44},"filterState":{"price":{"max":190000},"sort":{"value":"globalrelevanceex"},"sf":{"value":false},"tow":{"value":false},"con":{"value":false},"apa":{"value":false},"mf":{"value":false},"manu":{"value":false},"land":{"value":false},"lot":{"value":false}},"isListVisible":true}

### 44134 — Parma South
> https://www.zillow.com/homes/for_sale/44134_rb/?searchQueryState={"pagination":{},"usersSearchTerm":"44134","mapBounds":{"west":-81.75,"east":-81.62,"south":41.33,"north":41.42},"filterState":{"price":{"max":190000},"sort":{"value":"globalrelevanceex"},"sf":{"value":false},"tow":{"value":false},"con":{"value":false},"apa":{"value":false},"mf":{"value":false},"manu":{"value":false},"land":{"value":false},"lot":{"value":false}},"isListVisible":true}

### 44130 — Parma Heights
> https://www.zillow.com/homes/for_sale/44130_rb/?searchQueryState={"pagination":{},"usersSearchTerm":"44130","mapBounds":{"west":-81.83,"east":-81.70,"south":41.33,"north":41.43},"filterState":{"price":{"max":190000},"sort":{"value":"globalrelevanceex"},"sf":{"value":false},"tow":{"value":false},"con":{"value":false},"apa":{"value":false},"mf":{"value":false},"manu":{"value":false},"land":{"value":false},"lot":{"value":false}},"isListVisible":true}

---

## Next Steps

1. **Top up Zillapi credits** at https://zillapi.com/app/billing
2. **Re-run this cron job** — it will automatically pull all three ZIPs, produce listing tables with investor verdicts, and save the raw JSON dump for follow-up queries
3. The raw data will be saved to `cleveland_zip_stats.json` and `cleveland_clean.json` so subsequent queries (like "show me properties under $190K in ZIP 44129") won't need fresh credits

---

_Report saved at: `/opt/data/outputs/2026-09-23/parma-listings-under-190k/parma-listings.md`_
_Status file: `/opt/data/parma-pull-status.txt`_