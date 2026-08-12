# Decisions Log

## Methodology
- **Scoring:** 1-5 rating on two axes (Regulatory Friendliness × Income Potential)
- **Regulatory scoring factors:** STR permit requirements, caps, minimum stays, owner-occupancy, state preemption
- **Income scoring factors:** Tourist volume, nightly rates, occupancy %, seasonal patterns

## Market Selection Criteria
1. Must have minimal or no STR-specific restrictions (score 4+ on regulatory)
2. Must demonstrate strong STR income potential (score 4+ on income)
3. Must have available property inventory at viable entry prices (<$500K)

## Data Philosophy
- Used Zillapi MCP for real property-level data where possible
- Supplemented with knowledge of regulations and market dynamics
- STR income estimates derived by applying a 2-3x multiplier to long-term rent zestimate based on industry benchmarks for beach/resort markets

## Report Output
- Summary report provides actionable, ranked recommendations
- Zillapi data included to show real, verifiable numbers
- Regulation data organized by state vs. city to help identify broader opportunity zones

## Future Enhancement Opportunities
1. Run actual AirDNA API or Mashvisor data for precise STR income projections
2. Search for specific STR-eligible properties in top 3 markets using Zillapi
3. Set up cron job to monitor new listings in target markets
4. Create Zoho CRM integration (tabled from earlier discussion) to capture leads generated from this research