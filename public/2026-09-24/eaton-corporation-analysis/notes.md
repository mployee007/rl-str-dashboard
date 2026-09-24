# Notes & Data Caveats — Eaton (ETN) Analysis

## Data provenance
- Prices & CAGRs: Yahoo Finance v8 Chart API `adjclose` (total-return, dividend-adjusted). Pulled 2026-09-24.
- Fundamentals/valuation: stockanalysis.com statistics pages (scraped via curl — clean HTML; the *browser* is Cloudflare-blocked on that domain, but curl is not).
- Eaton financial history: stockanalysis.com financials page (FY2021–FY2025 + TTM ending Jun 30, 2026).

## Caveats & flags
1. **Forward EPS is an estimate.** FY2026E EPS ~$11.9 is my estimate (~14% growth off FY2025's $10.45). stockanalysis.com reports "Forward PE 29.2x," which implies a higher forward EPS (~$15) than my anchor — this likely reflects a longer-dated consensus EPS. I used my own clean anchor and marked it clearly.
2. **TTM net-margin dip.** Eaton's TTM net income ($3.83B) is *below* FY2025 ($4.09B) even though revenue and operating income rose — a below-the-line item (higher interest on acquisition debt and/or one-time charges). Worth watching but not a thesis-breaker.
3. **Peer scope mismatches.** Siemens (SIEGY) includes Healthineers + Mobility (not pure electrical); ABB (ABBNY) includes robotics/process automation; Honeywell (HON) trailing P/E is distorted by one-time gains ahead of its 3-way split (its −16.7% forward growth reflects divestitures, not weakness).
4. **Schneider Electric** is absent from stockanalysis.com; revenue (€40.15B, 2025) confirmed via Wikipedia; market cap (~$175B) and P/E (~35x) are approximate.
5. **Segment mix is approximate** (FY2024): Electrical Americas ~43%, Electrical Global ~24%, Aerospace ~14.5%, Vehicle ~12%, eMobility ~3%. Proportions are stable and well-established but not pulled from a primary filing in this session.
6. **GE Vernova (GEV)** has only ~2.5 yrs of trading history (spun off April 2024) — its "10-yr CAGR" (21.5%) is meaningless; use 1–2 yr context only.
7. **Vertiv (VRT)** and **nVent (NVT)** have ~8 yrs of history, so their "10-yr CAGR" is actually ~8-yr CAGR.

## Assumptions used in projections
- Base year: FY2026E EPS $11.9.
- EPS CAGR: Bull 16%, Base 12–13%, Bear 6%.
- Exit forward P/E: Bull ~28x, Base ~24–25x, Bear ~17x.
- Probabilities: Bull 25% / Base 55% / Bear 20%.
