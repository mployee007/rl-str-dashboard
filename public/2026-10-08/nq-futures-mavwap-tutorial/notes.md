# Session Notes

## Strategy source
The strategy was provided verbatim by the user. Key structural adaptations for futures (vs. equities):
- Contract sizing from stop distance (not shares)
- RTH-only session template requirement for EMA accuracy
- Section 1256 tax treatment
- Explicit MNQ → NQ transition plan
- Point-value math throughout ($20 NQ, $2 MNQ)

## Design decisions
- Followed the same canonical playbook structure as `options-credit-spreads-playbook.md` for consistency
- Added futures-specific sections: contract specs, platform setup, Section 1256
- Emphasized the "three filters must agree" rule as the central discipline
- Included worked contract-sizing examples at two account levels
- Added study drills so the user can practice the math and pattern recognition
- Made the "sit out" days (FOMC/CPI/NFP) explicit with a fallback rule

## Open items / future additions
- Live trade examples (need real MNQ trades with screenshots)
- Win-rate and expectancy tracking after 20+ trades
- Potential integration with a price-alert cron job (similar to the credit spreads trigger-price-alerts skill)