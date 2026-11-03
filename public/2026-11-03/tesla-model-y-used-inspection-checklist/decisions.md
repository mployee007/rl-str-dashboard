# Decisions

## D1 — Build a gating test around the battery, not a flat list of checks
**Decision:** Structure the checklist so one test (in-car Battery Health) gates the purchase, and everything else becomes a pricing input.
**Why:** The battery is the only component whose failure cost is unbounded relative to the car's value. Heat pumps, control arms, tires, and screens are all known, bounded, quotable expenses. A checklist that treats them as equals misleads the buyer about where the risk actually sits.

## D2 — Use NHTSA API recall counts instead of anecdotal "years to avoid" lists
**Decision:** Pull real per-model-year campaign counts from the NHTSA API and put them in the PDF as a table.
**Why:** The web is saturated with SEO content recycling the same vague claims about which Model Y years are bad. The NHTSA data is authoritative, free, current, and produces a genuinely useful signal (24 → 3 campaigns from 2020 to 2025) that changes the buying recommendation from "cheapest" to "newest you can afford."

## D3 — Verify sources despite a broken search backend
**Decision:** When `web_search` / `web_extract` failed on a missing `firecrawl-py` dependency and the system venv was write-protected, route around it via the `r.jina.ai` reader proxy rather than abandoning citation.
**Why:** The deliverable's value depends on the data being real. Degrading to invented "typical issues" content would have been worse than spending the extra calls. Tesla.com itself blocks all proxies (403), so warranty terms were confirmed through corroborated snippets rather than a single official fetch — flagged as such in `sources.json`.

## D4 — Deliver both a reference doc and a printable field checklist
**Decision:** Produce a thorough markdown reference *and* a designed 7-page PDF with checkboxes and write-in fields.
**Why:** The user's stated use case is standing in front of a car. A markdown file is wrong for that — you cannot hold it in one hand with a flashlight in the other. The PDF is the artifact that actually gets used; the markdown is what gets read beforehand.

## D5 — Keep price ranges and pack-replacement costs qualitative
**Decision:** Do not state "a 2022 Model Y sells for $X" or "a pack costs $Y."
**Why:** Both vary too widely by region, trim, and pack condition to state responsibly, and a wrong number would anchor the user's negotiation badly. The checklist instead gives them the *method* to price findings (a deduction table) plus one attributed residual-value statistic.

## D6 — Include a red-flag walk-away section
**Decision:** Add an explicit "do not negotiate, leave" list with a red boxed treatment in the PDF.
**Why:** In the moment, buyers negotiate with themselves. A pre-committed list of deal-enders, read before arriving, is the only thing that reliably prevents someone buying a car with a physically damaged pack because the price felt good.

## D7 — Fold in the deal-day account-transfer step
**Decision:** The final section includes transferring the Tesla account before leaving the driveway.
**Why:** This is the most common and most irritating post-purchase failure with used Teslas — the previous owner must remove the vehicle from their account or the new owner cannot add it. It has nothing to do with inspection but everything to do with a clean purchase, and no generic used-car checklist covers it.
