# Run log

- Initialized Gulfport output workspace.
- Gulfport was not present in the uploaded Top Cities List; used live Gulfport ZIP coverage from geocoding: 39501, 39503, 39505, 39507.
- Queried Zillapi rental search across Gulfport-area bounding boxes with beds >= 2 and price <= $3,000.
- Filtered raw Zillow/Zillapi results to single-family or townhouse listings in target ZIPs with rent $1,500-$3,000 and days on Zillow > 60.
- Identified 3 strict Zillapi candidates.
- Pulled Zillapi detail records for the strict candidates and verified all 3 had `furnished=false`.
- Queried Craigslist Gulfport furnished housing search with $1,500-$3,000 price filter; results existed, but visible posting dates were June-July 2026 only, so none were verifiable as >60 days old.
- Final qualifying count: 0.
