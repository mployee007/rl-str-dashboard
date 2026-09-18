# Notes — High-Yield Savings Comparison

## User Context
- Hermes Tompkins, Chicago IL
- Real estate investor — R&L Collective Holdings LLC (pre-revenue)
- Needs somewhere to park property reserves, rehab escrow, operating cash
- Values structured, data-dense output with actionable recommendations

## Market Observations (9/18/2026)
- HYSA rates are compressed — most major online banks clustered at 3.00%
- CIT Bank stands out at 3.75% — 75 bps above the pack
- Discover has been fully absorbed into Capital One 360
- Fintech cash accounts (Wealthfront, Betterment) are competing with traditional bank HYSAs
- Bot protection (Cloudflare, Akamai) is widespread on bank sites — scraping is increasingly difficult

## Key Decisions
- Used hybrid scraping: curl for simpler pages, browser for JS-rendered pages
- Prioritized direct bank verification over third-party aggregators (to avoid stale data)
- Focused head-to-head on CIT vs Ally because they represent the two use cases: max yield vs best UX

## Observations
- Ally's "3% correct as of 09/16/26" found in HTML confirms rates update frequently
- Capital One's 3.00% was effective same day (9/18/2026) — indicates daily rate adjustments
- Synchrony and Marcus both use aggressive bot protection — would need residential proxies to scrape