# Summary — Used Tesla Model Y Inspection Checklist

**Session:** 2026-11-03
**Request:** Checklist for inspecting a used Tesla Model Y before purchase.
**Deliverable status:** Complete and verified.

## What was delivered

| File | Purpose |
|---|---|
| `model-y-inspection-checklist.md` | Full reference version — 11 sections, sourced, with rationale for every check |
| `artifacts/model-y-inspection-checklist.pdf` | **Printable 7-page field checklist** with write-in boxes, verdict tables, and a red-flag walk-away section |
| `artifacts/model-y-inspection-checklist-ipad.pdf` | **Interactive iPad edition** — 12 pages, 122 tappable checkboxes, 7 fillable text fields, 12 outline bookmarks, 14.5pt touch targets |
| `artifacts/build_pdf.py` | Reproducible build script (print edition) |
| `artifacts/build_ipad_pdf.py` | Reproducible build script (iPad interactive edition) |
| `artifacts/verify_ipad.py` | Validates form fields, field sizes, and outline on the interactive build |
| `artifacts/nhtsa_recalls.py` | Pulls live recall-campaign counts from the NHTSA API |
| `sources.json` | Every source used, with what it supported |

**Reader requirement for the iPad edition:** Apple Books and the Files preview will render it but will not let you tick the boxes. Adobe Acrobat Reader (free) or PDF Expert are needed for the form fields. Markup or GoodNotes work if you'd rather draw on it.

## The thesis

A used Model Y is usually a good buy with one enormous tail risk: **the high-voltage battery**. Everything else on the car — heat pump, suspension, tires, screens — is a known, bounded, negotiable expense. A pack out of warranty is not. So the checklist is built around one gating test and treats everything else as pricing inputs.

Order of operations follows the same logic: **eliminate remotely → verify paperwork → test the battery → measure the mechanicals → drive it cold → price the findings.**

## Key verified data points

- **Recall exposure drops sharply by model year.** NHTSA API campaign counts for Model Y: 2020 = 24, 2021 = 23, 2022 = 20, 2023 = 17, 2024 = 5, 2025 = 3. This single chart reframes the used-market question from "lowest mileage" to "newest year."
- **The battery health test is now an in-car feature**, not a third-party hack — Controls → Service → Battery Health, requires software 2025.8.4+, takes 15–20 minutes, car parked and plugged in.
- **Warranty transfers.** Basic 4 yr/50,000 mi; battery and drive unit 8 yr/100,000–120,000 mi with 70% minimum capacity retention. Both follow the vehicle to subsequent owners, but buyers must check the *date* and *mileage* axes separately.
- **The AP4 computer failure** on 2024–2025 cars is the newest thing to ask about specifically — it blacks out cameras and driver aids.

## Verdict framework given to the user

| Battery retention | Action |
|---|---|
| ≥92% | Buy, subject to mechanicals |
| 88–91% | Buy with a negotiated discount |
| 85–87% | Only with meaningful warranty remaining, and money off |
| <85% | Hard pass unless the price is dramatically discounted |

## What the user should do next

1. Shortlist 2–3 candidates in the 2023–2024 range rather than paying less for a 2020–2021.
2. Run the VIN on nhtsa.gov/recalls on every candidate before driving out.
3. Take the printed PDF to each inspection and record the battery retention number on the cover.
4. If a car passes inspection, the deal-day sequence in §11 (especially the Tesla account transfer) is the closing checklist.
