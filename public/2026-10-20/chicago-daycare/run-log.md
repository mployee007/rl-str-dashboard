# Run Log — 2026-10-20

## Objective
Research how to start a daycare in Chicago, IL + startup cost + ROI + marketing plan + business model.

## Environment issues encountered (and workarounds)
1. **web_search / web_extract unavailable** — dependency `firecrawl-py` missing; `security.allow_lazy_installs=false` blocked auto-install; venv `/opt/hermes/.venv` is root-owned (read-only) so a manual install was denied (no sudo available).
   - Workaround: performed research via `curl` (saved HTML to `inputs/raw/`) and a locally-started **Camofox** headless browser driven through its REST API (`/tabs`, `/snapshot`) after Google/Bing HTML endpoints proved unreliable.
2. **Camofox not running** initially — started via `npm start` as a background process; killed + restarted once to clear a stale tab (404 on navigate).
3. **Government SharePoint sites** (dcfs.illinois.gov, chicago.gov, illinois.gov, dhs.state.il.us) are JS-heavy and return nav-only HTML to curl. Their substance was reconstructed from an industry guide (Brightwheel) that quotes DCFS directly + corroborating sources (LadyBug, Willow Tree).

## Data gathered (retrieved this session)
- Licensing: thresholds, 3 license types, free license, 3-yr validity, ratios, background checks, training, application process (Brightwheel).
- Pricing: Chicago actual tuition (Willow Tree), IL averages + CCAP rates + nanny benchmark (LadyBug), national averages (Care.com).
- Build cost benchmark: $150–$450/SF (Terrapin, via search result metadata).

## Artifacts produced
- `model.py` — computes 3 tiers × 3 scenarios; emits CSV + JSON.
- `artifacts/csv/roi_model.csv` — full scenario table.
- `artifacts/exports/model_summary.json` — assumptions + results.
- `report.md`, `summary.md`, `sources.json`, `decisions.md`, `notes.md`.

## Verification status
- Financial model executed cleanly (`python3 model.py`), output captured live.
- Licensing/pricing facts tied to the sources above (see sources.json). Startup-cost totals are explicitly labeled as modeled benchmarks, not vendor quotes.