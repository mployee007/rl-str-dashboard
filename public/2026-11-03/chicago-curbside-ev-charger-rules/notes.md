# Notes — research trail

## Search backend still broken
`web_search` / `web_extract` remain down (`search.firecrawl` unavailable, lazy installs disabled, system venv not writable). All research this session ran through `curl https://r.jina.ai/<url>` as a reader proxy, plus direct fetches to City Clerk and American Legal Publishing. Worked reliably at HTTP 200 for every target except a councilmatic PDF proxy link.

## The two-step that mattered
1. **Councilmatic** showed the ordinance with history entries only for 5/20/2026 (Introduced, Referred). Easy to conclude "pending."
2. **City Clerk record** showed three actions including `7/15/2026 City Council Passed`. The councilmatic page was stale.

Lesson: for Chicago legislation, the City Clerk ELS record is the authority on status. Councilmatic is better for reading and worse for currency.

## The document that decided it
The enrolled ordinance PDF is a **scanned image** — 205 KB, 3 pages, 2 extractable characters. Rendered at 140 dpi and read with the vision tool. The operative language:

> "The term 'electric vehicle charging station' means any facility or equipment that is owned by the City of Chicago and operated for public use to charge a battery or other energy storage device of an electric vehicle."

That definition is the whole answer. The program is City-owned public charging, not a residential permitting scheme.

## Chicago's electrical code on cords — full text worth knowing
§ 14X-7-705.3 prohibits, among other things:
- using extension cords as a substitute for permanent wiring
- affixing cords to structures
- extending cords through walls, ceilings, floors, or under doors/floor coverings
- subjecting cords to environmental damage or physical impact
- **using indoor-rated cords outdoors**
- using cords for anything other than **portable appliances**
- plugging into anything but a permanent receptacle, one appliance per cord

A car is not a portable appliance. That line alone kills the porch-outlet-to-curb plan.

## Numbers worth keeping
- Unpermitted charger fine: **200% of initial permit fee + $200–500/day**
- City service targets: permit issuance **5 business days**, inspection **10 business days**
- Chicago EVSE-ready definition: **40A, 208/240V, dedicated branch circuit terminating within 3 ft of the space**
- 100% of off-street spaces serving dwelling units must be EVSE-ready for permits filed on/after **Nov 1, 2023**
- Curbside pilot sunset: **June 30, 2030**
- ComEd curbside pilot municipalities: **Dixon, Oswego, Sandwich**

## Open items
- Federal 30C status is a genuine conflict between Chicago.gov (still linking it) and the 2025 tax legislation (terminated for property placed in service after 6/30/2026). Flagged rather than resolved.
- Chicago permit fee is scope-dependent — not quantifiable without the City's fee calculator and actual project details.
- Curb-cut feasibility is block-by-block and alderman-dependent.
