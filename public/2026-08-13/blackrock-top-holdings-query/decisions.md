# Decisions — BlackRock Top Holdings Query

## 2026-08-13

### Decision: Save the BLK report as a dashboard session artifact
- **Context:** User explicitly requested that the report be saved to the dashboard.
- **Options considered:** leave as chat-only output; save only as a raw note; save as a structured outputs session and rebuild dashboard.
- **Decision:** Save the report under outputs/2026-08-13/blackrock-top-holdings-query/ and rebuild the dashboard archive.
- **Consequence:** The report becomes retrievable through the completed-work dashboard and future artifact lookups.

### Decision: Use SEC 10-Q as the canonical quarterly-report source
- **Context:** Investor-relations search results were noisy and partially blocked.
- **Options considered:** Yahoo Finance summaries, BlackRock IR pages, SEC filing.
- **Decision:** Use the SEC 10-Q filing as the primary source of truth.
- **Consequence:** Financial and filing-date claims are grounded in the official filing.
