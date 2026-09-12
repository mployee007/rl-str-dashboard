# Decisions Log

## Decision 1: Period Selection
**Choice:** Calendar years 2016–2025 (10 full calendar years)
**Rationale:** The user asked for "the last ten years." Using calendar years 2016-2025 provides clean, complete annual data that is widely available from all sources.

## Decision 2: Inflation Benchmark
**Choice:** US CPI-U (all items, all urban consumers, not seasonally adjusted), annual averages
**Rationale:** This is the standard headline inflation measure. Using BLS data from usinflationcalculator.com. Cumulative: 35.6%, annualized: 3.09%.

## Decision 3: Asset Universe
**Choice:** 13 investable asset classes spanning equities, fixed income, real assets, commodities, and crypto
**Rationale:** Cast a wide net to capture traditional and alternative assets. Excluded: private equity (no public daily pricing), collectibles (no standardized index), venture capital (illiquid, no standardized returns).

## Decision 4: Return Calculation
**Choice:** Total return (price appreciation + reinvested dividends/interest), geometrically compounded
**Rationale:** This is the standard method for comparing investment returns across asset classes. Simple/arithmetic averages would overstate returns.