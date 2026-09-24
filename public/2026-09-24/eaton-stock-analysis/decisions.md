# Decisions & Methodology

1. **Scope:** Analyzed Eaton as an aerospace + tech (electrification/AI data-center power) name per user request. Emphasized Electrical (73% of revenue) and Aerospace (15.5%) segments; treated Vehicle/eMobility ("Mobility") as drags.

2. **Data sources:** Yahoo Finance (v8 chart API for price history; key-statistics + analysis pages via browser) and SEC EDGAR (submissions + XBRL company facts + FY2025 10-K for segment data). Yahoo v7/v10 quote endpoints returned Unauthorized, so used browser DOM extraction for valuation metrics (per financial-data-sourcing skill).

3. **Competitor set:** Chose 9 peers spanning electrical/power (Schneider, ABB, Emerson, Rockwell, Hubbell, nVent), data-center pure-play (Vertiv), and aerospace/motion (Honeywell, Parker-Hannifin). Delegated peer data collection to a subagent (browser-based scraping).

4. **Price-target framework:** EPS × exit-multiple, three scenarios (bull 25% / base 50% / bear 25%), probability-weighted. Anchored 2-yr near consensus (analyst 1-yr mean $479.57).

5. **EPS basis:** Used *adjusted* (non-GAAP) EPS throughout for targets and entry multiples, consistent with sell-side consensus; flagged GAAP figures separately.

6. **Entry prices:** Derived from applying fair-value multiples (24x/22x/20x) to 2027E adjusted EPS $16.13, cross-referenced with technical levels (200-day MA, 52-wk low) and analyst low target ($333).
