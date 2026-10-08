# NQ / MNQ Futures — EMA Stack + VWAP Day Trading Playbook

**Last updated:** 2026-10-08
**Instrument:** NQ (E-mini Nasdaq-100) / MNQ (Micro E-mini Nasdaq-100)
**Timeframe:** 5-minute chart, RTH-only session template
**Strategy type:** Trend-continuation pullback, intraday only

---

## 1. What This Strategy Is (Plain English)

You are trading in the direction of the intraday trend — nothing else. Three exponential moving averages (72, 210, 420) define the trend stack. A session-anchored VWAP tells you whether price is trading above or below the volume-weighted fair value for the day. You wait for price to pull back into the trend stack, confirm with a rejection candle, and enter.

You are **not** predicting reversals. You are **not** fading moves. You are waiting for all three filters — stack alignment, VWAP position, and rejection candle — to agree. On most days, that gives you zero or one trade. That is the edge.

---

## 2. The Instrument: NQ vs MNQ

### 2.1 Contract Specifications

| Spec | NQ (E-mini) | MNQ (Micro) |
|---|---|---|
| **Contract Unit** | $20 × Nasdaq-100 Index | $2 × Nasdaq-100 Index |
| **Min Tick** | 0.25 index points = $5.00 | 0.25 index points = $0.50 |
| **1 Point Value** | $20.00 | $2.00 |
| **Tick / Point Ratio** | 4 ticks = 1 point | 4 ticks = 1 point |
| **Product Code** | NQ | MNQ |
| **Settlement** | Financial (cash) | Financial (cash) |
| **Listing Cycle** | Quarterly (Mar, Jun, Sep, Dec) | Quarterly (Mar, Jun, Sep, Dec) |
| **Trading Hours** | Sun 6pm – Fri 5pm ET (23h/day, 1h maint) | Same as NQ |
| **Termination** | 9:30am ET, 3rd Friday of contract month | Same as NQ |
| **Source** | [CME NQ Specs](https://www.cmegroup.com/markets/equities/nasdaq/e-mini-nasdaq-100.contractSpecs.html) | [CME MNQ Specs](https://www.cmegroup.com/markets/equities/nasdaq/micro-e-mini-nasdaq-100.contractSpecs.html) |

### 2.2 Which Contract to Trade

**Start with MNQ.** MNQ is 1/10th the size of NQ — $2/point instead of $20/point. Until this system has a verified positive expectancy in your own trade log (minimum 30 live trades), trading NQ is oversized gambling.

| Metric | MNQ | NQ |
|---|---|---|
| 1 contract, 10-pt stop | $20 risk | $200 risk |
| 1 contract, 20-pt stop | $40 risk | $400 risk |
| 10 MNQ = 1 NQ equivalent | — | — |

**Scaling rule:** Graduate to NQ only after 30+ MNQ trades with ≥55% win rate and a profit factor ≥1.5. Even then, scale contract count from risk — do not jump from 10 MNQ to 1 NQ and call it the same thing.

---

## 3. Chart Setup

### 3.1 Indicators

Add these to a **5-minute chart**:

| Indicator | Settings | Purpose |
|---|---|---|
| **72 EMA** | 72-period exponential | Short-term trend / primary pullback entry zone |
| **210 EMA** | 210-period exponential | Medium-term trend / second-layer support |
| **420 EMA** | 420-period exponential | Multi-day trend anchor (highest-conviction dip zone) |
| **VWAP** | Session-anchored, reset daily | Intraday fair value; truth-teller for bias |

Color convention (suggested):
- 72 EMA: blue or white
- 210 EMA: gold or yellow
- 420 EMA: red
- VWAP: dashed orange or purple

### 3.2 RTH-Only Session Template

**Critical:** Use a **regular trading hours (RTH)** session template, not a 24-hour (ETH) chart.

The 420 EMA on a 24-hour chart averages thin overnight Globex action into the calculation. Overnight futures drift at low volume does not reflect where real money traded. An RTH-only chart keeps all three MAs honest — they only incorporate data from the cash session (9:30am–4:00pm ET on prior days).

Most platforms (TradingView, ThinkorSwim, Sierra Chart, NinjaTrader) support RTH-only or "cash session" chart templates. If your platform does not, switch platforms before trading this system — this is not optional.

### 3.3 VWAP Note

Use a **session-anchored VWAP** that resets at the start of each regular trading session (9:30am ET), not a rolling or anchored-to-earnings VWAP. The standard "VWAP" indicator on most platforms does this by default when the chart is RTH-only.

---

## 4. When to Trade

### 4.1 Trading Window

| Window | Action |
|---|---|
| **Pre-8:30am ET** | Do not trade. Overnight drift does not respect MA stacks. |
| **8:30 – 9:30am ET** | Watch only. Let pre-market action print. |
| **9:30 – 9:35am ET** | **Stand aside.** First 5 minutes after cash open. Let MAs and VWAP settle. |
| **9:35 – 11:30am ET** | **Prime trading window.** This is where the setups live. |
| **11:30am – 4:00pm ET** | Marginal. Volume thins. Only take if the setup is textbook-perfect and you have not traded yet. |
| **After 4:00pm ET** | Do not trade. Flatten any open position. |

### 4.2 Days to Sit Out (or Adjust)

| Event | Rule |
|---|---|
| **FOMC announcement day** | Sit out entirely. No exceptions. |
| **CPI release day** | Sit out entirely. No exceptions. |
| **NFP (Non-Farm Payrolls) day** | Sit out entirely. No exceptions. |
| **OPEX (monthly options expiration)** | Tradeable, but expect choppier VWAP behavior — halve size. |
| **Holiday half-day** | Sit out. Thin volume breaks the MA stack logic. |

**Minimum adjustment rule:** If you absolutely must trade an event day (you should not), halve contract count **and** double the stop distance. The market's range expands on these days and your normal stop becomes noise.

---

## 5. Entry Rules

### 5.1 Bullish Setup (Long)

**Prerequisites — ALL must be true:**

1. **EMA Stack aligned:** 72 EMA > 210 EMA > 420 EMA (all three stacked in order, sloping up or at minimum not crossed against you).
2. **Price above VWAP:** The session VWAP must be below current price. VWAP is your intraday truth-teller — if price is below it, you are fighting the day's order flow.
3. **Pullback to 72 EMA:** Price retraces down and touches (or comes within ~2 points of) the 72 EMA.
4. **Rejection candle confirmation:** The pullback candle — or the one immediately after — closes back **up**, off the EMA. Look for:
   - A candle with a long lower wick that closes near its high
   - A bullish engulfing candle after a red candle that touched the EMA
   - A hammer or dragonfly doji at the 72 EMA

**Entry trigger:** Enter on the **close of the rejection candle** or on a break of that candle's high by 1 tick. Do not enter mid-candle. Do not "anticipate" the touch.

**The 420 EMA touch (highest conviction):** If price pulls all the way back to the 420 EMA, this is your strongest long signal — but it is a **multi-day average on a 5-minute chart**, so treat it as a trend-line anchor zone, not a daily trigger. It fires rarely; when it does and all other filters agree, it deserves full size.

### 5.2 Bearish Setup (Short)

Exact mirror of the long setup:

1. **EMA Stack aligned:** 72 EMA < 210 EMA < 420 EMA.
2. **Price below VWAP.**
3. **Pullback (rally) to 72 EMA.**
4. **Rejection candle closes back down** (long upper wick, bearish engulfing, shooting star).

### 5.3 The Three-Filter Checklist

Before **every** entry, verify:

| Filter | Question | ✓ |
|---|---|---|
| **Stack** | Are 72 / 210 / 420 EMAs stacked in my direction? | ☐ |
| **VWAP** | Is price on the right side of VWAP for my bias? | ☐ |
| **Candle** | Did a rejection candle close off the 72 EMA? | ☐ |

**If any box is unchecked, do not enter.** The edge is not the lines — it is waiting for all three to agree.

### 5.4 What "Sit Out" Looks Like

- Stack aligned but price never pulls back? → Sit out.
- Pullback to 72 EMA but no rejection candle? → Sit out.
- Rejection candle but stack is flat/crossed? → Sit out.
- Everything lines up but it is 11:45am and volume is dead? → Sit out.

---

## 6. Exit Rules

### 6.1 Scale-Out Structure

Every trade is two halves:

| Half | Target | Logic |
|---|---|---|
| **First 50%** | 1:1 reward-to-risk **or** prior session high/low (whichever is tighter) | De-risk the trade. You are now free-rolling. |
| **Runner 50%** | 2:1 reward-to-risk **or** trail behind 72 EMA | Let the trend work. |

**Example (long):** Entry at 31,200, stop at 31,190 (10-pt risk).
- First target: 31,210 (1:1, +10 pts) or prior session high at 31,205 (tighter) → take 31,205.
- Runner: trail stop at 72 EMA value each 5-min candle close, or take profit at 31,220 (2:1).

### 6.2 VWAP Hard Exit

**If price closes on the wrong side of VWAP against your position, exit immediately.** No waiting, no "maybe it reverses."

- Long: a 5-minute candle **closes** below VWAP → exit the full position at market.
- Short: a 5-minute candle **closes** above VWAP → exit the full position at market.

VWAP is your intraday truth-teller. When it flips against you, the day's order flow has changed and your original thesis is invalid.

### 6.3 Trailing the 72 EMA (Runner)

After the first half is off, trail the runner's stop at the 72 EMA value:

- On each 5-minute candle close, update the stop to the current 72 EMA value.
- If the 72 EMA is rising (long) or falling (short), the trail naturally tightens.
- If price closes back through the 72 EMA, you are stopped out — this is the same signal that invalidated your entry, and exiting here preserves profit.

### 6.4 End-of-Day Flattening

**No overnight holds.** Period. Flatten everything before 4:00pm ET. Futures gap risk is real — you cannot manage a position you cannot close.

---

## 7. Risk Rules

### 7.1 The Golden Rule

> **Risk the dollar amount first. Contracts follow from the stop distance. Never the other way around.**

### 7.2 Position Sizing Formula

```
Max risk per trade = Account size × 1%
Contracts = Max risk per trade ÷ (Stop distance in points × Point value per contract)
```

Round contracts **down**, never up.

### 7.3 Worked Examples

**Scenario A: $10,000 account, trading MNQ ($2/point)**

- Max risk: $10,000 × 1% = **$100**
- Stop distance: 10 points
- Risk per contract: 10 × $2 = $20
- Contracts: $100 ÷ $20 = **5 MNQ**

**Scenario B: $10,000 account, tighter stop (5 points)**

- Max risk: $100
- Risk per contract: 5 × $2 = $10
- Contracts: $100 ÷ $10 = **10 MNQ**

**Scenario C: $50,000 account, trading NQ ($20/point)**

- Max risk: $50,000 × 1% = **$500**
- Stop distance: 10 points
- Risk per contract: 10 × $20 = $200
- Contracts: $500 ÷ $200 = **2 NQ** (2.5 rounded down)

**Scenario D: $50,000 account, wider stop (20 points)**

- Max risk: $500
- Risk per contract: 20 × $20 = $400
- Contracts: $500 ÷ $400 = **1 NQ**

### 7.4 Risk Sizing Table (Quick Reference — MNQ)

| Account | 1% Risk | 5-pt Stop | 10-pt Stop | 15-pt Stop | 20-pt Stop |
|---|---|---|---|---|---|
| $5,000 | $50 | 5 MNQ | 2 MNQ | 1 MNQ | 1 MNQ |
| $10,000 | $100 | 10 MNQ | 5 MNQ | 3 MNQ | 2 MNQ |
| $25,000 | $250 | 25 MNQ | 12 MNQ | 8 MNQ | 6 MNQ |
| $50,000 | $500 | 50 MNQ | 25 MNQ | 16 MNQ | 12 MNQ |

### 7.5 Risk Sizing Table (Quick Reference — NQ)

| Account | 1% Risk | 5-pt Stop | 10-pt Stop | 15-pt Stop | 20-pt Stop |
|---|---|---|---|---|---|
| $25,000 | $250 | 2 NQ | 1 NQ | —* | —* |
| $50,000 | $500 | 5 NQ | 2 NQ | 1 NQ | 1 NQ |
| $100,000 | $1,000 | 10 NQ | 5 NQ | 3 NQ | 2 NQ |
| $250,000 | $2,500 | 25 NQ | 12 NQ | 8 NQ | 6 NQ |

*\*Stop distance exceeds 1% risk for 1 contract — account too small for NQ at that stop width.*

### 7.6 Daily Loss Limit

Once you are down **2% of the account** in a single day (two full-R losses), **stop trading**. Walk away. The market will be there tomorrow. Your account may not be if you chase.

### 7.7 No Overnight Holds

Flatten **all** positions before 4:00pm ET. Futures gap overnight — sometimes violently. You are trading an intraday MA-stack system; holding through the close converts a structured trade into an unmanaged bet.

---

## 8. Pre-Trade Checklist

Use this before **every** session:

| # | Check | ✓ |
|---|---|---|
| 1 | Is today an event day (FOMC / CPI / NFP)? If yes, sit out or halve size + double stop. | ☐ |
| 2 | Chart set to 5-min, RTH-only session template? | ☐ |
| 3 | 72 EMA, 210 EMA, 420 EMA, and session VWAP all visible? | ☐ |
| 4 | Trading window confirmed? (No entries before 9:35am ET.) | ☐ |
| 5 | Daily max loss (2% of account) calculated and written down? | ☐ |
| 6 | Position size formula ready? (1% risk ÷ (stop × point value) = contracts) | ☐ |
| 7 | Exit plan for both halves written down before entry? | ☐ |

---

## 9. Session Journal Template

After each session, fill this out:

```
Date:
Contract Traded (MNQ/NQ):
Number of Trades:
- Trade 1: Long/Short, Entry ___, Stop ___, Target 1 ___, Target 2 ___, Result ___
- Trade 2: ...
P&L: +$___ / -$___
Setups Seen vs Taken:
Mistakes:
Notes:
```

Track every session — even the ones where you sat out. "No trade taken, no setups" is data.

---

## 10. Common Mistakes

| Mistake | Why It Hurts | Fix |
|---|---|---|
| **Entering before the rejection candle closes** | You are guessing, not confirming | Wait for the candle to close. The close is the confirmation. |
| **Trading when the EMA stack is flat/crossed** | No trend = random walks | If 72/210/420 aren't clearly ordered, sit out. |
| **Ignoring VWAP** | Fighting the day's order flow | VWAP is not optional. Wrong side of VWAP = no trade. |
| **Starting with NQ instead of MNQ** | Over-sizing before system is proven | 30-trade minimum on MNQ before touching NQ. |
| **Sizing contracts before stop distance** | Inconsistent risk | Risk dollar amount first. Contracts follow. |
| **Moving the stop wider mid-trade** | Converts a defined loss into an undefined one | The stop is the stop. If it hits, you were wrong. Accept it. |
| **Holding through 4:00pm ET** | Overnight gap risk | Flatten everything. Futures gaps do not care about your EMA stack. |
| **Trading FOMC/CPI/NFP** | Noise destroys MA-stack signals | Sit out. These days are for long-term investors, not 5-min chart traders. |
| **Overtrading — forcing setups that aren't there** | Eats capital through commissions and tilt | One clean setup per day is a good day. Zero is fine. |
| **Using a 24-hour chart** | 420 EMA polluted by thin overnight data | RTH-only template. No exceptions. |

---

## 11. Terms to Memorize

| Term | Definition |
|---|---|
| **EMA** | Exponential Moving Average — weights recent price more heavily than older price |
| **VWAP** | Volume-Weighted Average Price — the average price weighted by volume for the session |
| **RTH** | Regular Trading Hours — the cash equity session (9:30am–4:00pm ET) |
| **ETH** | Electronic Trading Hours — the full Globex session including overnight |
| **Rejection candle** | A candle that tests a level and closes back in the opposite direction (wick rejection) |
| **Stack** | The relative ordering of 72 / 210 / 420 EMAs |
| **Scale out** | Exiting a position in pieces (e.g., half at first target, half at second) |
| **Runner** | The portion of a position left open after the first scale-out |
| **Point value** | Dollar value of a 1-point move in the index (NQ = $20, MNQ = $2) |
| **Tick** | Minimum price increment (NQ/MNQ = 0.25 points) |
| **R-multiple** | Profit or loss expressed as a multiple of initial risk (e.g., +1R, -1R) |

---

## 12. Sources

- CME Group — E-mini Nasdaq-100 Contract Specifications: https://www.cmegroup.com/markets/equities/nasdaq/e-mini-nasdaq-100.contractSpecs.html
- CME Group — Micro E-mini Nasdaq-100 Contract Specifications: https://www.cmegroup.com/markets/equities/nasdaq/micro-e-mini-nasdaq-100.contractSpecs.html
- CME Group — Equity Index Trading Hours: https://www.cmegroup.com/markets/equities/nasdaq.html
- Strategy provided by Hermes Tompkins (October 2026)

---

## 13. Update Protocol

This is a **canonical reference** — not a session scratchpad. When new information arrives:

1. Integrate it into the matching section above.
2. If the new material changes the structure, rewrite for coherence.
3. Mirror the updated version to `outputs/YYYY-MM-DD/<session>/artifacts/exports/`.
4. Update the "Last updated" line.
5. Never append raw research notes to the bottom.