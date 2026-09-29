# Research Notes - 10yr-rate-trade-plan - 2026-09-29

## Data retrieved (live)
Yahoo Finance chart API (curl worked; federalreserve.gov + bls.gov curl BLOCKED - used browser/DDG instead):

| Tenor | Symbol | Level |
|---|---|---|
| 13-week | ^IRX | 4.065% |
| 5-year | ^FVX | 5.063% |
| 10-year | ^TNX | 5.255% |
| 30-year | ^TYX | 5.594% |
| 10Y futures | ZN=F | 104.42 |

10Y yield daily path (last 10 sessions): 4.947, 4.998, 4.963, 4.968, 5.114, 5.162, 5.184, 5.240, 5.255.
→ Sharp acceleration from Sep 23 (5.114) onward.

ZN daily path: 106.41 (Sep 17) → 104.42 (Sep 29). −4.36 pts since Aug 25.

## Curve analysis
- 10Y − 13W = +119 bp (positively sloped, no inversion)
- 10Y − 5Y = +19 bp
- 30Y − 10Y = +34 bp
→ Bear steepener: long end leading the selloff.

## Macro context (CNBC / CNN, Sep 23-25 2026)
- "10-year Treasury yield rockets to 19-year high" — highest since 2007.
- 30-year at 5.398% (Sep 23), highest since June 2007.
- Cause: strong business activity data + intensifying inflation concerns.
- Sep 25 snapshot: 10Y 5.17%, 2Y 4.81%.

## FOMC 2026 remaining meetings
- Sep 15-16 (concluded), **Oct 27-28**, **Dec 8-9**. Decisions 2:00pm ET second day.
- Source: federalreserve.gov FOMC calendar (via DDG results), cross-checked with fedratecalc + atgpress.

## BLS releases
- Employment Situation (Sep 2026): **Fri Oct 2, 2026, 8:30 ET**.
- CPI (Sep 2026): **Wed Oct 14, 2026, 8:30 ET**.

## Environment gotchas
- `curl` to federalreserve.gov and bls.gov **timed out / blocked** (tool asked for consent and timed out).
  finance.yahoo.com curl works fine.
- Workflow that works: `lite.duckduckgo.com/lite/?q=` via browser for search; Yahoo chart API via curl for prices.
