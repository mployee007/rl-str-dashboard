# Parma Listings Under $190K — Pull Status

**Date:** 2026-09-14  
**Status:** ❌ BLOCKED — Zillapi out of credits  
**Run type:** Scheduled cron job  

---

## Target ZIPs

| ZIP | Area | Bounding Box | Price Cap |
|-----|------|-------------|-----------|
| 44129 | Parma West | -81.78, 41.37, -81.68, 41.42 | $190,000 |
| 44134 | Parma | -81.72, 41.35, -81.65, 41.40 | $190,000 |
| 44130 | Parma / Middleburg Hts | -81.80, 41.35, -81.73, 41.41 | $190,000 |

---

## Errors Encountered

| Call | ZIP | Error |
|------|-----|-------|
| 1 | 44129 | `Out of credits for this cycle. Top up or upgrade at https://zillapi.com/app/billing.` |
| 2 | 44134 | `MCP server 'zillapi' is unreachable after 9 consecutive failures.` |
| 3 | 44130 | `MCP server 'zillapi' is unreachable after 9 consecutive failures.` |

---

## Fallback Assessment

Per `real-estate-submarket-screening` skill instructions, all web-based listing sites (Zillow.com, Redfin, Trulia, Realtor.com, Homes.com, Movoto) aggressively block automated access with PerimeterX/Cloudflare captchas. No web scraping fallback was attempted — it would fail identically.

---

## Manual Browser Links

Open these in a browser to review listings directly:

### 44129 (Parma West)
```
https://www.zillow.com/homes/44129_rb/?searchQueryState={"pagination":{},"usersSearchTerm":"44129","mapBounds":{"west":-81.78,"east":-81.68,"south":41.37,"north":41.42},"filterState":{"price":{"max":190000}},"isListVisible":true}
```

### 44134 (Parma)
```
https://www.zillow.com/homes/44134_rb/?searchQueryState={"pagination":{},"usersSearchTerm":"44134","mapBounds":{"west":-81.72,"east":-81.65,"south":41.35,"north":41.40},"filterState":{"price":{"max":190000}},"isListVisible":true}
```

### 44130 (Parma / Middleburg Hts)
```
https://www.zillow.com/homes/44130_rb/?searchQueryState={"pagination":{},"usersSearchTerm":"44130","mapBounds":{"west":-81.80,"east":-81.73,"south":41.35,"north":41.41},"filterState":{"price":{"max":190000}},"isListVisible":true}
```

---

## Resolution

- **Status file saved:** `/opt/data/parma-pull-status.txt`
- **Next action:** Retry when Zillapi credits refresh (billing: https://zillapi.com/app/billing)
- **No listings were fabricated.** All tables are empty pending a successful pull.