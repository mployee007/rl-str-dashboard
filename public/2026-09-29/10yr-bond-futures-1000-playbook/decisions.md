# Decisions - 2026-09-29

1. **Answer framing.** The user asked "how to invest in the 10-year bond futures market
   with $1,000." Decided the honest, highest-value answer is a *capability map* (what is
   actually tradeable at this size), not a directional market call — because $1,000 cannot
   meet ZN's overnight margin at all.

2. **Primary instrument recommendation.** Chose the **Micro 10-Year Yield futures (10Y)**
   as the starter instrument: $330 overnight margin, $10/bp, cash-settled, directly tied to
   the user's stated 10-year thesis. Alternative offered: day-trade 1× ZN ($200 day margin)
   for deeper liquidity.

3. **Cheat sheet format = PDF.** User profile notes a preference for "polished visuals" and
   "retrievable deliverables." Built a 2-page A4/Letter PDF via fpdf2 (only viable PDF tool
   in this environment).

4. **No non-ASCII characters.** fpdf2 core fonts are latin-1; avoided en-dashes, arrows,
   bullets, and "≥" to prevent encoding errors.

5. **Layout verification method.** No PDF renderer/vision tool available. Instead of
   eyeballing, verified programmatically with pymupdf: page count, and every text block's
   bounding box checked against page margins to catch overflow/clipping.

6. **Numbers sourced, not assumed.** All margins pulled from live CME and Ironbeam pages on
   2026-09-29 rather than recalled, and the "day vs overnight" distinction is explicitly
   flagged as broker-specific and volatility-sensitive.
