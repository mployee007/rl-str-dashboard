# Run Log — Fort Lauderdale furnished STR hunt

## 2026-07-31
- Initialized output workspace under `outputs/2026-07-31/fort-lauderdale-furnished-str-hunt/`.
- Read `/opt/data/outputs/incoming/Top_Cities_List.md`; reference row for Ft. Lauderdale listed ZIPs `33316, 33308, 33313` and hospital `Broward Health Medical Center (Level I Trauma)`.
- Confirmed live geodata for Fort Lauderdale via Open-Meteo geocoding.
- Ran two Fort Lauderdale-area Zillapi `for_rent` searches with `beds_min=2` and `price_max=3000`.
- Parsed the raw Zillapi output saved under `/tmp/hermes-results/` and filtered to target ZIPs plus non-apartment house/townhouse inventory.
- Found one strict Zillapi candidate: `2244 NW 52nd Ave, Fort Lauderdale, FL 33313`.
- Pulled Zillapi property detail for `2244 NW 52nd Ave`; detail fields showed `daysOnZillow=12` and `resoFacts.furnished=false`.
- Opened the South Florida Craigslist housing feed with `query=furnished`, `min_price=1500`, `max_price=3000`, `min_bedrooms=2`, sorted by `dateoldest`.
- Extracted 193 Craigslist rows from the page DOM and reviewed Fort Lauderdale / Broward house-like matches.
- Verified the oldest visible Craigslist result in the result set was dated `6/15/2026`, with Fort Lauderdale house-like rows on `7/14`, `7/29`, and `7/30`; none were older than 60 days.
- Final qualifying count: 0.
- Expanded B-pass to Fort Lauderdale + Hollywood + Dania + 33304 corridor while keeping all original strict filters.
- Craigslist oldest Broward/South Florida furnished search result remained 6/15/2026, still short of the 60-day requirement as of 2026-07-31.
- Reviewed additional broader-area near misses: Hollywood furnished house (~1 month old), Dania furnished 2/2 (~1 month old, apartment, short availability window), and Las Olas furnished house with pool (23 days old, ZIP 33304).
- Extracted contact mechanics for the Hollywood and Dania follow-up listings.
- Sent outreach email to the Hollywood Craigslist relay address on 2026-07-31T19:06:15Z; Dania contact remained gated behind Craigslist hCaptcha with no direct email/phone exposed.
