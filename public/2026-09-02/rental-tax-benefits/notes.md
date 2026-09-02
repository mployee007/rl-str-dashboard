# Notes — Methodology & Caveats

## Research Approach

Research was conducted by a delegated subagent that fetched content from IRS.gov via curl and browser navigation. All primary sources are IRS publications, topic pages, and tax forms. Secondary sources (BiggerPockets, Investopedia, Nolo) were cross-referenced but primary IRS sources took precedence.

## Key Caveats

### 1. Section 199A QBI — EXPIRATION RISK
The IRS QBI page (updated May 12, 2026) states the deduction applies to tax years "ending on or before December 31, 2025." Unless Congress enacted an extension between May and September 2026, this deduction is NOT available for tax year 2026. This is the single most important finding in the report.

### 2. TCJA Sunset — 2026 is a Transition Year
Many individual provisions of the Tax Cuts and Jobs Act expired after December 31, 2025:
- Individual income tax rates revert to pre-TCJA levels
- Standard deduction roughly halves
- SALT deduction cap may be removed
- Personal exemptions return
- Pease limitation returns

### 3. No 2026 Inflation-Adjusted Figures
The IRS typically publishes tax-year inflation adjustments in October-November of the preceding year. As of this report date (September 2026), final 2026 figures for Section 179, excess business loss limits, and other inflation-indexed thresholds have not been confirmed. The report uses 2025 figures with explicit caveats.

### 4. Dashboard Mileage Rate
The 2026 standard mileage rate is estimated at $0.70/mile. The actual rate is established by the IRS annually (typically December). Update in the dashboard when the official rate is published.

## Verification Status

| Source | Verified | Method |
|--------|----------|--------|
| IRS Pub 527 | ✅ | Browser navigation to live page |
| IRS Topic 425 | ✅ | curl fetch (April 2026 update) |
| IRS QBI page | ✅ | curl fetch (May 2026 update) |
| Form 4562 instructions | ✅ | curl fetch |
| Tangible property regs | ✅ | curl fetch |
| BiggerPockets deductions | ✅ | curl fetch |
| 2026 inflation figures | ❌ | Not yet published by IRS |