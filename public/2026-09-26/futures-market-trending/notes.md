# Notes — Futures Market Trending

## Methodology Notes

1. **Trend definition:** A market was classified as "trending" if it showed consistent
   directional movement across 1-month, 3-month, and 6-month windows (or a clear accelerating
   momentum pattern like Crude Oil's V-shaped recovery from a 6-month low).

2. **Why not just price change:** Volume and open interest were used as confirmation. A
   market moving on thin volume is more likely to be erratic/noise. CL=F, SB=F, ZS=F all
   pass this filter with deep liquidity.

3. **6-month context is crucial on Crude Oil:** At a glance, a 6-month return of +2.35%
   doesn't look like a "trend." But the path matters — oil cratered, then rocketed back.
   The 3-month (+28.5%) and 1-month (+12.2%) windows show the momentum is real and
   accelerating. This is the definition of a trending market (strong directional bias).

## Data Caveats

- **BTC=F price and timing discrepancy:** The Yahoo Finance chart API shows BTC=F at $84,500
  with last timestamp 2026-09-26 00:08 UTC. The Yahoo Finance ticker bar shows "Bitcoin USD"
  at $83,936.23 (-$659.88, -0.78%). These differ because BTC=F is the CME Bitcoin *futures*
  contract, while the ticker shows spot. The futures contract was last updated earlier.

- **Commodity futures roll:** Front-month contracts roll periodically. 6-month price
  comparisons may span contract rolls and carry effects (contango/backwardation). The Yahoo
  v8 API's adjusted close attempts to account for this.

- **Sherlocking sites blocked:** Barchart, Finviz, CME Group, TradingView, and
  stockanalysis.com all bot-blocked. This is expected per the financial-data-sourcing skill.
  Yahoo Finance remains the most reliable accessible source.

## Observations

- VIX at 14.87 (-5.11%) — low fear, markets calm. Supports the "risk-on / momentum" thesis
  for trending markets.
- 10-year yield at 5.18% — elevated, which makes commodity carry trades more expensive.
  Something to watch for futures that require margin financing.
- Gold pulling back (-8% in 1 month) while oil surges — suggests this is a supply-driven oil
  story, not broad commodity inflation.