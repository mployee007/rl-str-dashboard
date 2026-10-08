# Notes — NQ Futures EMA/VWAP Tutorial

## User Context
- Hermes Tompkins (Solomon) — building trading strategy educational resources
- Previously built options credit spreads playbook (inputs/reference/options-credit-spreads-playbook.md)
- This is the futures counterpart — same pedagogical approach, different instrument

## Key Observations
- Strategy is trend-continuation, not mean-reversion — designed for 0-1 trades per day
- Edge comes from patience (three-filter agreement), not frequency
- Position sizing formula is the most important section — "size contracts from risk, not risk from contracts"
- NQ at ~31,200 (Oct 2026) means 10-point stop = $200/contract — non-trivial for small accounts
- RTH-only chart template is non-negotiable per the strategy author

## Future Research Ideas (not yet requested)
- Backtesting framework for EMA stack setups
- Adding ES (S&P 500 futures) as a correlated confirmation filter
- Integrating economic calendar API for automatic event-day warnings