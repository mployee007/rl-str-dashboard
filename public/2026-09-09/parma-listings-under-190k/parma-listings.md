# Parma West Listings Under $190K — Pull Blocked (Retry)

**Date:** 2026-09-09  
**Attempt:** Retry #2 (prior attempt earlier today also blocked)  
**ZIPs:** 44129 (Parma West), 44134 (Parma South), 44130 (Parma East/Middleburg Hts)  
**Status:** ❌ BLOCKED — All data sources exhausted

---

## Full Source Attempt Matrix

| # | Source | Target | Result |
|---|--------|--------|--------|
| 1 | Zillapi MCP | 44129 | **Out of credits** — "Top up or upgrade at https://zillapi.com/app/billing" |
| 2 | Zillapi MCP | 44134 | MCP server unreachable (41 consecutive failures) |
| 3 | Zillapi MCP | 44130 | MCP server unreachable (41 consecutive failures) |
| 4 | web_search (firecrawl) | — | firecrawl-py not installed; lazy installs disabled |
| 5 | pip install firecrawl | — | Permission denied on /opt/hermes/.venv |
| 6 | web_extract (Zillow) | — | Same firecrawl dependency |
| 7 | Browser (Zillow.com) | — | Not attempted — PerimeterX captcha blocks automated access |

---

## Direct Zillow Search URLs (open in your browser)

- **44129 (Parma West):**  
  https://www.zillow.com/homes/for_sale/44129_rb/?searchQueryState={"pagination":{},"mapBounds":{"west":-81.78,"south":41.37,"east":-81.68,"north":41.42},"filterState":{"price":{"max":190000},"fsba":{"value":false},"fsbo":{"value":false},"nc":{"value":false},"fore":{"value":false},"cmsn":{"value":false},"auc":{"value":false},"pmf":{"value":false}},"isListVisible":true}

- **44134 (Parma South):**  
  https://www.zillow.com/homes/for_sale/44134_rb/?searchQueryState={"pagination":{},"mapBounds":{"west":-81.72,"south":41.35,"east":-81.65,"north":41.40},"filterState":{"price":{"max":190000},"fsba":{"value":false},"fsbo":{"value":false},"nc":{"value":false},"fore":{"value":false},"cmsn":{"value":false},"auc":{"value":false},"pmf":{"value":false}},"isListVisible":true}

- **44130 (Parma East / Middleburg Heights):**  
  https://www.zillow.com/homes/for_sale/44130_rb/?searchQueryState={"pagination":{},"mapBounds":{"west":-81.80,"south":41.35,"east":-81.73,"north":41.41},"filterState":{"price":{"max":190000},"fsba":{"value":false},"fsbo":{"value":false},"nc":{"value":false},"fore":{"value":false},"cmsn":{"value":false},"auc":{"value":false},"pmf":{"value":false}},"isListVisible":true}

---

## Resolution Paths

| Priority | Action | Effort |
|----------|--------|--------|
| 🔴 Immediate | Top up Zillapi credits at https://zillapi.com/app/billing | 2 min |
| 🟡 Medium | Install firecrawl-py: `sudo uv pip install firecrawl-py` into Hermes venv | 5 min |
| 🟢 Fallback | Use the Zillow URLs above manually in browser to screen | Ongoing |

---

## Artifact Files

| File | Path |
|------|------|
| Full report | `/opt/data/outputs/2026-09-09/parma-listings-under-190k/parma-listings.md` |
| Quick reference | `/opt/data/parma-latest-listings.md` |
| Status log | `/opt/data/parma-pull-status.txt` |