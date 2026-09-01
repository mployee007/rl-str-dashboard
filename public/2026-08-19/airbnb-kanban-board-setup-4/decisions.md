# Decisions — airbnb-kanban-board-setup-4

## 2026-08-19

### Decision: Market ranking framework
- **Context:** The request could be answered with generic housing forecasts or with a more actionable investor lens.
- **Options considered:** National appreciation ranking only; hottest markets list only; balanced investor ranking.
- **Decision:** Built a balanced ranking for 1-4 unit investors using macro housing conditions, metro-level demand/growth, supply pressure, and liquidity.
- **Consequence:** Final answer prioritizes actionable market selection rather than a one-metric list.

### Decision: Split markets into large/liquid vs. small/cash-flow buckets
- **Context:** The best big metros and the best small high-cap-rate metros are not the same thing.
- **Options considered:** One mixed list; separate strategy buckets.
- **Decision:** Present a main ranked list plus a separate small-market cash-flow shortlist.
- **Consequence:** Easier for the user to match the ranking to strategy and risk tolerance.

### Decision: Rockford verdict framing
- **Context:** Rockford screened well on market lists, but city-level socioeconomic data introduced obvious risk flags.
- **Options considered:** Treat Rockford as a broad buy; treat Rockford as a pass; treat Rockford as a selective buy.
- **Decision:** Classified Rockford as a selective TAKE for 1-4 unit cash-flow investing.
- **Consequence:** The final recommendation emphasizes block-by-block underwriting, basis discipline, and management quality instead of citywide enthusiasm.

### Decision: Use city-level median value/rent as a yield proxy
- **Context:** Search results for some private market-report pages were degraded or noisy.
- **Options considered:** Skip quantitative yield framing; infer from qualitative rankings only; use Census median rent/value with Buildium market stats.
- **Decision:** Used Census QuickFacts plus Buildium metrics to compute rough GRM and gross-yield proxies.
- **Consequence:** The Rockford memo includes grounded, interpretable underwriting context even with imperfect source coverage.

### Decision: Rank Rockford by submarket function, not just headline quality
- **Context:** The best area to live in Rockford is not automatically the best area to buy 1-4 unit rentals.
- **Options considered:** Rank ZIPs only by neighborhood quality; rank only by cheapness; split into stabilized-hold vs value-add functions.
- **Decision:** Ranked Rockford ZIPs by investor utility: stronger east/northeast corridors for stabilized holds and older in-town corridors for value-add small multifamily.
- **Consequence:** The next-layer memo distinguishes between where to hold quality rentals and where to hunt forced appreciation.

### Decision: Use live Zillapi screens as acquisition examples
- **Context:** The user asked to go to the next layer, which called for actionable submarket and deal-level screening instead of another abstract memo.
- **Options considered:** Stay high-level; build a buy box only; combine ZIP ranking, live screens, and buy-box thresholds.
- **Decision:** Combined current live listings, ranked ZIPs, and explicit basis ceilings into a single Rockford acquisition screen.
- **Consequence:** The deliverable can be used immediately to sort real leads into take / negotiate / pass buckets.
