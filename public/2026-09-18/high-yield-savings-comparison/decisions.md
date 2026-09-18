# Decisions — High-Yield Savings Comparison

## 2026-09-18

### Decision: Research methodology — direct bank scraping vs aggregators
- **Context:** web_search and web_extract were unavailable (firecrawl not installed, permissions blocked)
- **Options considered:** Fix firecrawl install, use browser on aggregators, scrape banks directly
- **Decision:** Scrape bank websites directly via curl + browser as fallback
- **Consequence:** Got 7 verified rates but couldn't verify 2 (Marcus, Synchrony). Data is fresher than aggregators but took more effort.

### Decision: Head-to-head focus — CIT Bank vs Ally
- **Context:** User asked for comparison and checklist after initial ranking
- **Options considered:** Compare all 7, compare top 2, compare top vs "best UX"
- **Decision:** CIT Bank (highest rate @ 3.75%) vs Ally (best UX with savings buckets for real estate)
- **Consequence:** Clear recommendation matrix — user can pick based on priorities: yield or bookkeeping features.

### Decision: No cron job for rate monitoring
- **Context:** User didn't ask for ongoing monitoring, just a one-time comparison
- **Decision:** Did not create a rate-monitoring cron job
- **Consequence:** If user wants automated rate tracking, should revisit and schedule via cronjob action='create'