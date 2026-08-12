# Run log

- Initialized standard output files.
- Pulled Columbus ZIP references from `/opt/data/outputs/incoming/Top_Cities_List.md`.
- Ran Zillapi for-rent searches with multiple Columbus bounding boxes:
  - `-83.20,39.86,-82.80,40.12`
  - `-83.03,39.95,-82.97,40.02`
  - `-83.06,40.02,-82.97,40.09`
- Parsed Zillapi raw outputs saved under `/tmp/hermes-results/` and filtered to target ZIPs 43214, 43210, 43801, 43215.
- Navigated Craigslist Columbus furnished rentals with price filters.
- Applied Craigslist filters for furnished + beyond 30 days + house/townhouse.
- Re-ran Craigslist as a ZIP-centered search around 43215 within 15 miles.
- Craigslist result page showed `1 - 2 of 2` and `Zero local results found`; both hits were outside Columbus.
- Final strict shortlist count: 0.
