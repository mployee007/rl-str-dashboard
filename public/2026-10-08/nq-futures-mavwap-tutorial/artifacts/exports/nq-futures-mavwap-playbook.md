# NQ/MNQ EMA Stack + VWAP Futures Playbook

_Last updated: 2026-10-08_

This is the canonical living playbook for trading Nasdaq-100 index futures (NQ/MNQ) using a three-EMA stack with session-anchored VWAP. When new research, trade reviews, or refinements are added, the material should be integrated here in a way that preserves structure, removes duplication, and keeps the document coherent enough to study from start to finish.

---

## 1. What this strategy is

This is a **directional intraday futures strategy** built on three filters that must agree before any entry:

1. **EMA stack alignment** — 72, 210, and 420-period EMAs in proper order
2. **VWAP confirmation** — price on the correct side of the session-anchored VWAP
3. **Rejection candle** — price touches a key EMA and closes back in the direction of the trend

The strategy trades only the New York cash session (roughly 8:30–11:30 AM ET) and does not hold overnight. It is designed for the Nasdaq-100 futures contract: **NQ** (full-size, $20/point) or **MNQ** (micro, $2/point). Trade MNQ until the system proves itself on live data.

The edge is not the moving averages alone — it is the discipline of waiting for all three filters to agree, then sizing conservatively.

---

## 2. Why futures (and why NQ)

### Futures vs. equities for this approach

| Attribute | Futures | Equities |
|---|---|---|
| Leverage | Built-in (notional exposure far exceeds margin) | Requires margin account |
| Pattern reliability | High — indices respect MA/VWAP stacks in cash hours | Stock-specific noise |
| Overnight risk | Avoided by rule (flatten before close) | Gaps are routine |
| Tax treatment | Section 1256: 60/40 long-term/short-term | Standard capital gains |
| Hours | Nearly 24-hour, but we only trade RTH | 9:30–4:00 ET |

NQ (Nasdaq-100 E-mini) is the chosen instrument because:
- High liquidity — tight bid/ask spreads
- Strong trending behavior during NY cash hours
- Respects moving-average stacks when volume is present
- MNQ micro contract allows small-dollar risk while learning

### Contract specifications at a glance

| Contract | Tick size | Point value | Notional at 20,000 index |
|---|---|---|---|
| NQ | 0.25 index points | $20/point | ~$400,000 |
| MNQ | 0.25 index points | $2/point | ~$40,000 |

**Key takeaway:** A 10-point stop on 1 NQ contract = $200. A 10-point stop on 1 MNQ contract = $20. Start with MNQ.

---

## 3. Chart setup

### Platform setup

Apply these to a **5-minute candlestick chart**:

| Indicator | Period | Color / style |
|---|---|---|
| EMA 72 | 72 | Blue or white |
| EMA 210 | 210 | Gold or yellow |
| EMA 420 | 420 | Red or pink |
| VWAP | Session-anchored | Reset at RTH open (9:30 AM ET) |

### Critical: RTH-only session template

Most platforms default to a 24-hour chart (ETH + RTH combined). You **must** use a **Regular Trading Hours (RTH) session template** so that:
- The 420 EMA reflects only cash-session volume, not thin overnight drift
- VWAP anchors to the 9:30 AM ET open
- Candles outside RTH are excluded from all calculations

If your platform does not support RTH-only templates, the minimum workaround is to set VWAP to session-anchored and mentally discount overnight action near the 420 EMA.

### Why the 420 EMA is special

On a 5-minute RTH chart, 420 periods span roughly **6–7 trading days**. This is a **multi-day trend anchor**, not a daily trigger. You might touch the 420 EMA once a week on NQ. When it does get touched and holds, it is the highest-conviction dip buy in the system — but it is not something you wait for every day.

---

## 4. When to trade (session rules)

### Trading window

| Parameter | Rule |
|---|---|
| Session | New York cash session only |
| Window | ~8:30 AM – 11:30 AM ET |
| First 5 minutes | Skip — let MAs and VWAP set after the cash open |
| After 11:30 AM | Degraded signal quality; reduce size or sit out |
| Overnight | **No overnight holds.** Flatten before 4:00 PM ET close |

### Days to sit out (or reduce size)

| Event | Rule |
|---|---|
| FOMC announcement day | Sit out entirely |
| CPI release day | Sit out entirely |
| NFP (non-farm payrolls) day | Sit out entirely |
| If you must trade these days | Halve position size, double stop distance |

Overnight futures drift does not respect the EMA stack the way cash-session volume does. Trades outside the NY window are not part of this system.

---

## 5. Entry rules (the three-filter system)

All three filters must agree. If any one filter is missing, **sit out**.

### Filter 1: EMA stack alignment

**Bullish (longs only):**
- 72 EMA > 210 EMA > 420 EMA
- EMAs are sloping upward or at minimum flat (not rolling over)

**Bearish (shorts only):**
- 72 EMA < 210 EMA < 420 EMA
- EMAs are sloping downward or at minimum flat

**No trade:** The stack is tangled, flattening, or crossing.

### Filter 2: VWAP confirmation

**Bullish:** Price is **above** session VWAP
**Bearish:** Price is **below** session VWAP

VWAP is your intraday truth-teller. If price is on the wrong side of VWAP for your direction, do not take the trade — even if the EMA stack looks perfect.

### Filter 3: Rejection candle at a key EMA

Wait for price to pull back to one of the EMAs and **reject** — meaning a candle touches (or comes very close to) the EMA, then closes back in the direction of the trend.

**What counts as a rejection candle:**
- A wick through the EMA that closes back above (for longs) or below (for shorts)
- A hammer, dragonfly doji, or bullish engulfing at the EMA (longs)
- A shooting star, gravestone doji, or bearish engulfing at the EMA (shorts)

**What does NOT count:**
- A candle that touches the EMA and keeps going through it
- A touch followed by consolidation with no directional close
- A 1-minute spike — use the 5-minute close, not the intra-candle wick alone

### Priority of EMA touches (longs)

| EMA touched | Conviction | Typical frequency |
|---|---|---|
| 72 EMA | Standard setup | Daily or near-daily |
| 210 EMA | Higher conviction | A few times per week |
| 420 EMA | Highest conviction — trend anchor | Once a week or less |

For shorts, mirror the logic: rejection at the 72 EMA from below is the standard short setup.

### Entry execution

Enter **on the close of the rejection candle** or on a break of that candle's high (longs) / low (shorts). Do not enter while the candle is still forming — you need the close to confirm rejection.

---

## 6. Exit rules

### Scale-out structure

Split your position into two halves:

| Half | Exit target | Logic |
|---|---|---|
| First half (50%) | 1:1 reward-to-risk **or** prior session high/low | Bank the high-probability win |
| Second half (runner, 50%) | 2:1 reward-to-risk **or** trail behind the 72 EMA | Let the trend work |

### Hard exit — VWAP violation

**If price closes on the wrong side of VWAP against your position, exit immediately.** No exceptions.

- Long: price closes **below** VWAP → exit
- Short: price closes **above** VWAP → exit

VWAP is the intraday truth-teller. When it flips against you, the odds have shifted. Do not wait for the stop to get hit.

### Stop placement

The stop goes just beyond the rejection candle's low (for longs) or high (for shorts) — not at an arbitrary dollar distance.

- Long stop: a few ticks below the rejection candle's low
- Short stop: a few ticks above the rejection candle's high

This gives the trade room to breathe while keeping the stop tied to price structure, not a random number.

### End-of-session

Flatten all positions before 4:00 PM ET. No overnight holds.

---

## 7. Risk rules (the part that keeps you alive)

### The cardinal rule

**Risk a fixed dollar amount per trade — 1% of account max.** Size the contract count from the stop distance, never the other way around.

### Contract-sizing math

```
Contracts = floor(risk_dollars / (stop_distance_points × point_value))
```

**Worked example — MNQ ($2/point, $5,000 account):**

- 1% risk = $50
- Stop distance = 10 points
- Dollar risk per contract = 10 × $2 = $20
- Contracts = floor($50 / $20) = **2 MNQ contracts**
- Total risk = 2 × $20 = $40 (0.8% of account)

**Worked example — NQ ($20/point, $25,000 account):**

- 1% risk = $250
- Stop distance = 8 points
- Dollar risk per contract = 8 × $20 = $160
- Contracts = floor($250 / $160) = **1 NQ contract**
- Total risk = $160 (0.64% of account)

### Pre-entry checklist

Run this math before every entry:

1. Account size: $______
2. 1% of account: $______ (max risk)
3. Stop distance in points: ______
4. Point value (MNQ=$2, NQ=$20): $______
5. Risk per contract: ______ × $______ = $______
6. Contracts allowed: $______ / $______ = ______

If contracts < 1, **you cannot take the trade.** Reduce stop distance only if it still respects the price structure.

### Additional risk rules

| Rule | Detail |
|---|---|
| Max risk per trade | 1% of account |
| Max risk per day | 2% of account (two full losses and you're done) |
| Overnight holds | **None.** Flatten before close |
| FOMC/CPI/NFP days | Sit out, or halve size + double stop |
| Leverage awareness | 1 MNQ at 20,000 notional ≈ $40,000 exposure — know what you're controlling |

### The real refinement

> Futures reward you for trading less. This stack will give you maybe one clean setup a day on NQ. The edge isn't the lines — it's waiting for all three filters (stack + VWAP + rejection candle) to agree, then sizing like you expect to be wrong.

---

## 8. Daily routine

### Pre-market (before 8:30 AM ET)

1. Load the RTH-only 5-minute chart with 72/210/420 EMAs + session VWAP
2. Note the EMA stack order and slope
3. Note where VWAP sits relative to price
4. Mark prior session high and low
5. Check economic calendar — is today FOMC, CPI, or NFP?

### During the session (8:30–11:30 AM ET)

1. Wait until 9:35 AM ET (skip first 5 minutes)
2. Monitor for pullbacks to the 72 EMA
3. When price touches the 72 EMA, check:
   - Stack aligned? ✓/✗
   - Price on correct side of VWAP? ✓/✗
   - Rejection candle forming? ✓/✗
4. If all three: calculate position size, enter on candle close
5. Set stop, set scale-out targets
6. Log the trade immediately

### Post-session

1. Review every trade taken (and every near-miss skipped)
2. Screenshot the setup
3. Note any filter violation — did you take a trade without all three?
4. Update running P/L and win rate

---

## 9. Trade log template

Keep this for every trade:

```
Date: _______________
Time (ET): _______________
Direction: LONG / SHORT
Contract: MNQ / NQ
Contracts: ______

Setup:
  EMA stack: 72___ 210___ 420___  ✓ Aligned? ___
  VWAP: Price above/below VWAP? ___
  Rejection candle at which EMA? ___
  Candle type: ___________________

Entry price: _______________
Stop price: _______________
Stop distance (points): ______
Risk per contract: $______
Total dollar risk: $______
% of account: ______

Exit 1 (half) target: _______________  Hit? ___
Exit 2 (runner) target: _______________  Hit? ___

Result: WIN / LOSS / BREAKEVEN
P/L: $______

Notes (what went right/wrong):
___________________________________________________
```

---

## 10. Common mistakes

1. **Taking a trade without all three filters aligned.**
   Stack looks good but VWAP is on the wrong side? That is not a valid setup. Two out of three is zero.

2. **Entering before the rejection candle closes.**
   You need the confirmation of the close. Entering mid-candle is guessing.

3. **Sizing contracts first, then fitting the stop.**
   This is backwards. The stop distance determines contract count, not the other way around. A 20-point stop you chose to fit 3 contracts is not a trade — it's a gamble.

4. **Holding through a VWAP flip.**
   VWAP is your intraday truth-teller. If price closes on the wrong side against your position, the trade is invalid. Exit.

5. **Trading outside the NY window.**
   Overnight drift does not respect the EMA stack. Trades after 11:30 AM ET degrade in quality.

6. **Trading FOMC/CPI/NFP normally.**
   These events produce volatility that blows through EMA stops. Sit out or reduce size dramatically.

7. **Overtrading — forcing setups that aren't there.**
   This system may produce zero or one clean setup per day. Days with no trade are wins too.

8. **Using a 24-hour chart template.**
   Thin overnight action dilutes the 420 EMA. RTH-only keeps the stack honest.

---

## 11. Transition plan: MNQ → NQ

Start with MNQ until you can answer "yes" to all of these:

- [ ] 20+ live trades taken with full journal entries
- [ ] Win rate and expectancy calculated from real data (not simulation)
- [ ] No filter-violation trades in the last 10 trades
- [ ] 1% risk rule followed on every trade
- [ ] At least one clean rejection-at-210-EMA trade taken successfully

When you transition to NQ:
- Recalculate position size from the new $20/point value
- Expect the same number of contracts or fewer
- The system does not change — only the dollar risk per point

---

## 12. Study drills

1. Pull up a 5-minute RTH NQ chart from any recent trading day. Find every 72 EMA touch. Count how many had all three filters aligned. You will see how rare clean setups are.

2. Calculate position size: account = $8,000, stop = 12 MNQ points. How many contracts? (Answer: floor($80 / $24) = 3 MNQ)

3. Calculate position size: account = $30,000, stop = 15 NQ points. How many contracts? (Answer: floor($300 / $300) = 1 NQ)

4. On a chart, find a VWAP flip — a candle that closes on the opposite side of VWAP. Imagine you were in a trade in the prior direction. Would you have exited?

5. Identify a rejection candle vs. a continuation-through candle at the 72 EMA. Explain the difference in your own words.

---

## 13. Terms to memorize

| Term | Meaning |
|---|---|
| EMA | Exponential Moving Average — weights recent price more heavily |
| VWAP | Volume-Weighted Average Price — the day's true average price, volume-adjusted |
| RTH | Regular Trading Hours — 9:30 AM – 4:00 PM ET |
| Rejection candle | Price touches a level and closes back in the direction of the trend |
| Scale out | Closing part of the position at one target, leaving the rest to run |
| Runner | The second half of the position, targeting a larger move |
| Point value | Dollar gain/loss per one index-point move (NQ=$20, MNQ=$2) |
| Notional value | Total dollar exposure of the contract (index level × point value) |
| Section 1256 | IRS rule giving futures 60% long-term / 40% short-term capital gains treatment |

---

## 14. Platform-specific notes

### If your platform supports RTH session templates

Use them. Set the chart to RTH-only so all EMA and VWAP calculations use cash-session data only. This is the intended configuration.

### If your platform does NOT support RTH-only

Workarounds, in order of preference:
1. Set VWAP to session-anchored at 9:30 AM ET (most platforms support this)
2. Mentally discount overnight candles near the 420 EMA
3. Consider switching to a platform that supports RTH templates (TradingView, Sierra Chart, NinjaTrader)

### VWAP anchoring

Ensure VWAP resets at the RTH open (9:30 AM ET), not at midnight or the globex open. A VWAP that includes overnight volume is not useful for this strategy.

---

## 15. Update protocol for future research

When adding future research:
1. Keep this file as the canonical source.
2. Integrate new material into the relevant section instead of dumping raw notes at the bottom.
3. Add genuinely new sections only when the concept does not fit the existing outline.
4. Preserve examples, formulas, checklists, and warnings that improve the document as a teaching resource.
5. If new research contradicts older content, revise the old section and note the change in the session output files.
6. If live trade data suggests adjusting a rule (e.g., stop placement, session window), add the evidence before the rule change.

---

## Sources and references

- Strategy provided by the user, adapted from their existing equities EMA/VWAP system
- CME Group NQ contract specifications: https://www.cmegroup.com/markets/equities/nasdaq/e-mini-nasdaq-100.contractSpecs.html
- CME Group MNQ contract specifications: https://www.cmegroup.com/markets/equities/nasdaq/micro-e-mini-nasdaq-100.contractSpecs.html
- IRS Section 1256: https://www.irs.gov/taxtopics/tc429

---

_This playbook is a living document. It is not investment advice. Futures trading involves substantial risk of loss and is not suitable for all investors._