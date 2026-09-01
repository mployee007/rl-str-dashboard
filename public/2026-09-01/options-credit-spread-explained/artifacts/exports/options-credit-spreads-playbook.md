# Options Credit Spreads Playbook

_Last updated: 2026-09-01_

This is the canonical living playbook for options credit spreads. When new research is done on credit spreads, the new material should be integrated here in a way that preserves structure, removes duplication, and keeps the document coherent enough to study from start to finish.

## What an options credit spread is

An options credit spread is a defined-risk vertical spread opened for a net credit.

You:
- sell one option,
- buy another option of the same type,
- use the same expiration,
- choose different strike prices,
- collect more premium on the short option than you pay for the long option.

The upfront credit is the **maximum possible profit** if the spread expires worthless.

The long option exists mainly to cap risk. That is what makes a credit spread different from selling a naked option.

## The two core structures

### 1) Bull put spread
Used when your view is **bullish to neutral**.

Structure:
- sell a put at a higher strike,
- buy a put at a lower strike,
- collect a net credit.

Best case:
- underlying stays above the short put strike,
- both puts expire worthless,
- you keep the full credit.

### 2) Bear call spread
Used when your view is **bearish to neutral**.

Structure:
- sell a call at a lower strike,
- buy a call at a higher strike,
- collect a net credit.

Best case:
- underlying stays below the short call strike,
- both calls expire worthless,
- you keep the full credit.

## Why traders use credit spreads

Credit spreads are popular because they combine:
- defined risk,
- upfront income,
- flexible directional expression,
- less capital exposure than naked short options.

Per OIC/OCC educational material, both bull put and bear call spreads are **limited-risk, limited-reward** strategies. The trade-off is straightforward: your upside is capped at the credit received, but your downside is capped by the long option.

## Core math you should know cold

Let:
- `width` = difference between strikes,
- `credit` = premium received from short leg minus premium paid for long leg.

### Bull put spread
- **Max profit** = credit received
- **Max loss** = spread width − credit
- **Breakeven** = short put strike − credit

### Bear call spread
- **Max profit** = credit received
- **Max loss** = spread width − credit
- **Breakeven** = short call strike + credit

### Contract conversion
One standard equity/ETF option contract usually controls **100 shares**.

So:
- `Dollar credit = credit × 100`
- `Dollar max loss = (width − credit) × 100`

## Payoff intuition

### Bull put spread payoff logic
- Above short put strike: full profit.
- Between strikes: profit decays into loss.
- Below long put strike: max loss.

### Bear call spread payoff logic
- Below short call strike: full profit.
- Between strikes: profit decays into loss.
- Above long call strike: max loss.

## Decision tree: which one fits the market view?

| Market view | Preferred credit spread |
|---|---|
| Mildly bullish | Bull put spread |
| Neutral but with downside support | Bull put spread |
| Mildly bearish | Bear call spread |
| Neutral but with upside resistance | Bear call spread |

## What the research says about setup

### OIC/OCC guidance
From OIC strategy pages:
- A bull put spread is built from a short put plus a lower-strike long put with the same expiration.
- A bear call spread is built from a short call plus a higher-strike long call with the same expiration.
- In both cases, the short leg generates income and the long leg limits assignment/upside or downside risk.
- Both strategies have precisely limited profit and loss potential.
- Both strategies can face **early assignment risk**.
- Both strategies can face **expiration risk**, including uncertainty around final assignment status until after expiration processing.

### Options Playbook heuristics
Options Playbook explicitly highlights two practical rules of thumb:
- Consider opening the spread around **30–45 days to expiration** to benefit from accelerating time decay as expiration approaches.
- Consider placing the short strike roughly **one standard deviation out of the money** to increase probability of success, understanding that farther OTM generally means less credit.

These are not laws. They are practical starting heuristics.

## Greeks and behavior

### Theta (time decay)
Research consistently frames credit spreads as **somewhat positive theta** positions.

Why:
- the short option loses value as time passes, which helps you,
- the long option also loses value, which offsets some of that benefit,
- net effect is usually favorable if price remains in your expected zone.

### Volatility
Both OIC and Options Playbook describe the volatility effect as generally **slight to moderate overall**, because you are short one option and long another of the same type and expiration.

Still, path matters:
- If the trade is working and price stays away from the short strike, lower implied volatility is usually helpful because both legs cheapen and the spread can collapse toward zero.
- If the trade is threatened and price moves toward or through the short strike, volatility changes become more important and mark-to-market swings can expand.

## Assignment risk and expiration risk

This is one of the most important parts of the playbook.

### Early assignment risk
OIC notes that early assignment is possible for both structures.

Practical implications:
- **Bull put spreads** can be assigned early if the short put is deep ITM or there are special circumstances around carrying value.
- **Bear call spreads** can be assigned early, especially around **ex-dividend dates** when short calls are ITM and remaining extrinsic value is low.

### Expiration risk
OIC specifically warns that traders may not know for sure whether they were assigned until processing after expiration. That means you can be exposed to weekend or after-hours gap risk if one leg expires or is assigned unexpectedly.

Practical takeaway:
- Do not let a challenged spread drift into expiration just because the theoretical max loss is defined.
- If price is near the short strike late in the cycle, closing early often reduces operational risk.

## How to think about strike selection

Strike selection changes almost everything:
- probability of profit,
- credit received,
- max loss,
- how often the trade is tested,
- emotional stress while holding it.

### General trade-off
- **Closer short strike to spot** → more credit, lower probability, higher test frequency.
- **Farther OTM short strike** → less credit, higher probability, smaller reward.
- **Wider spread width** → larger max risk in dollars, usually more credit, larger loss capacity.
- **Narrower spread width** → smaller capital at risk, but often lower absolute credit.

## A simple selection framework

Use this sequence:
1. Start with your directional view: bullish/neutral or bearish/neutral.
2. Choose expiration, often beginning with the 30–45 DTE heuristic.
3. Find a short strike where you would still be comfortable if price moved closer to it.
4. Buy the protective long strike at a width that fits your account risk tolerance.
5. Calculate credit, max loss, and breakeven before entering.
6. Reject the trade if the max loss is too large relative to the reward or your position size rules.

## Management framework

### Before entry
Checklist:
- thesis is clear,
- max loss is acceptable,
- breakeven is understood,
- assignment/expiration mechanics are understood,
- position size is small enough that a full max loss is survivable.

### While open
Monitor:
- distance from spot to short strike,
- percentage of max profit captured,
- days to expiration,
- volatility expansion,
- event risk such as earnings, Fed releases, CPI, ex-dividend dates, or major macro headlines.

### At exit
Three common outcomes:
- **Winner:** buy back the spread for less than you sold it for.
- **Scratch/manage:** close early if the thesis weakens.
- **Loser:** close before expiration or accept a defined loss if the move invalidates the trade.

## Common mistakes

1. **Confusing high win rate with low risk.**
   Credit spreads often win frequently but can lose much more than they make on each winner.

2. **Selling too close to the money for too little edge.**
   The premium may look attractive, but the short strike gets tested much more often.

3. **Ignoring assignment risk.**
   Defined risk does not mean zero operational complexity.

4. **Holding into expiration just to squeeze the last few cents.**
   This can create asymmetric hassle relative to the remaining reward.

5. **Oversizing.**
   Because max loss is defined, traders sometimes get careless and stack too many spreads.

## Live SPY example captured in this session

_Source: Yahoo Finance SPY options chain viewed in browser on 2026-08-31 around 1:25 PM EDT. Quotes are delayed and will change._

### Example: SPY bull put spread
- SPY spot: **765.73**
- Expiration: **2026-08-31**
- Sell **765 put** at **0.44 bid**
- Buy **760 put** at **0.03 ask**
- Net credit: **0.41**

### Math
- Spread width = `765 - 760 = 5.00`
- Max profit = `0.41 × 100 = $41`
- Max loss = `(5.00 - 0.41) × 100 = $459`
- Breakeven = `765 - 0.41 = 764.59`

### Interpretation
This is a real example of a same-day-style bull put spread that is **very close to the money**.

What it teaches:
- The credit is real and immediate.
- Risk is capped.
- A spread can still be risky even though loss is defined.
- Small distance between spot and short strike means the position can flip from likely winner to stressed trade quickly.

### Outcome map
| SPY at expiration | Result |
|---|---|
| Above 765 | Full profit: keep $41 |
| 764.59 | Breakeven |
| Between 760 and 765 | Partial loss |
| At or below 760 | Max loss: $459 |

## Comparing credit spreads to debit spreads

A useful mental shortcut:
- **Credit spread:** you are primarily betting the underlying will **not breach** your short strike by expiration.
- **Debit spread:** you are primarily betting the underlying **will move enough** in your favor to create value.

Another way to say it:
- credit spreads monetize being roughly right,
- debit spreads usually need more movement.

## Best-use cases

Credit spreads tend to fit best when:
- you have a directional lean but not an explosive forecast,
- you want defined risk,
- implied volatility is not so low that premium is trivial,
- you are comfortable managing short option risk.

## When not to use them

Avoid or be cautious when:
- you do not understand assignment/exercise mechanics,
- major event risk can violently gap the underlying,
- liquidity is poor and bid/ask spreads are wide,
- the reward is tiny compared with the dollar risk,
- you are tempted to hold to expiration for pennies.

## Terms to memorize

| Term | Meaning |
|---|---|
| Short strike | The option you sold; main income driver |
| Long strike | The protective option you bought |
| Width | Difference between strikes |
| Net credit | Premium in minus premium out |
| Breakeven | Price where expiration P/L is zero |
| Max profit | The upfront credit |
| Max loss | Width minus credit |
| OTM | Out of the money |
| ITM | In the money |
| DTE | Days to expiration |

## Study drills

1. Take a bull put spread and calculate max profit, max loss, and breakeven without notes.
2. Do the same for a bear call spread.
3. Look at a live chain and explain why one spread pays more than another.
4. Explain assignment risk in plain English.
5. Compare a credit spread and debit spread on the same ticker and expiration.

## Update protocol for future research

When adding future research:
1. Keep this file as the canonical source.
2. Integrate new material into the relevant section instead of dumping raw notes at the bottom.
3. Add genuinely new sections only when the concept does not fit the existing outline.
4. Preserve examples, formulas, and warnings that improve the document as a teaching resource.
5. If new research contradicts older content, revise the old section and note the change in the session output files.

## Sources used in this version
- OIC/OCC bull put spread: https://www.optionseducation.org/strategies/all-strategies/bull-put-spread-credit-put-spread
- OIC/OCC bear call spread: https://www.optionseducation.org/strategies/all-strategies/bear-call-spread-credit-call-spread
- Options Playbook short put spread: https://www.optionsplaybook.com/option-strategies/short-put-spread
- Options Playbook short call spread: https://www.optionsplaybook.com/option-strategies/short-call-spread
- Yahoo Finance SPY options chain: https://finance.yahoo.com/quote/SPY/options/
