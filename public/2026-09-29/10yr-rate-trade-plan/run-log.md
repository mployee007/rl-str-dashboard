# Run Log - 10yr-rate-trade-plan - 2026-09-29

| Step | Action | Result |
|---|---|---|
| 1 | curl Yahoo ^TNX 2mo daily | 10Y yield history: 4.617 → 5.255% |
| 2 | curl Yahoo ZN=F 2mo daily | ZN 108.86 → 104.42 |
| 3 | Computed MAs + changes | 10d SMA 5.076 > 20d SMA 4.964; uptrend confirmed |
| 4 | curl federalreserve.gov FOMC calendar | **BLOCKED** (timed out, no consent) |
| 5 | curl bls.gov schedule | **BLOCKED** (timed out, no consent) |
| 6 | curl Yahoo ^TYX/^FVX/^IRX | 30Y 5.594 / 5Y 5.063 / 13W 4.065 → bear steepener |
| 7 | browser → DDG lite "FOMC 2026 dates" | Oct 27-28, Dec 8-9 confirmed |
| 8 | browser → DDG lite "BLS Oct 2026 releases" | CPI Oct 14, 2026 |
| 9 | browser → DDG lite "jobs report Oct 2026" | NFP Oct 2, 2026 |
| 10 | Wrote build_tradeplan.py (fpdf2) | — |
| 11 | Ran build | PDF written, 2 pages, 6,183 bytes |
| 12 | pymupdf layout verification | 2 pages, **0 overflow** on both pages |

## Artifacts
- `artifacts/exports/10yr-rate-trade-plan.pdf` — deliverable
- `artifacts/exports/build_tradeplan.py` — reproducible generator
