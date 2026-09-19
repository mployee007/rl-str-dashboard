# Run Log — Parma Listings Under $190K

## 2026-09-19

### ~00:00 UTC — Pull initiated
- Created output directory structure: `outputs/2026-09-19/parma-listings-under-190k/`
- Called `mcp_zillapi_search_listings` for ZIPs 44129, 44134, 44130 in parallel
- All three Zillapi calls failed

### ~00:00 UTC — Fallback attempted
- Called `web_search` (firecrawl backend) for all three ZIPs
- All three failed: `firecrawl-py` not installed, lazy installs disabled

### ~00:00 UTC — Blocker saved
- Wrote `/opt/data/parma-pull-status.txt` with full error table and direct Zillow links
- Wrote `/opt/data/parma-latest-listings.md` with status summary
- Wrote blocker report to `outputs/2026-09-19/parma-listings-under-190k/artifacts/exports/`
- **Status: BLOCKED — Zillapi out of credits. Will retry next cycle.**