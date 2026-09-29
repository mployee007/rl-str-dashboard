# Run Log - 2026-09-29

| Time | Action | Result |
|---|---|---|
| — | `web_search` x4 | FAILED (firecrawl lazy-install disabled) |
| — | SearXNG search x4 | DEGRADED (Bing only, junk results) |
| — | `read_url` on CME pages | Returned unrelated text (Wikipedia) via search-about strategy |
| — | `browser_navigate` → lite.duckduckgo.com | **WORKED** — usable search results |
| — | browser → CME micro treasury futures page | Got authoritative MTN/10Y specs + margins |
| — | browser → CME ZN margins page + JS extract | Got ZN maintenance = $1,875; live quote ZNZ6 104'110 |
| — | browser → Ironbeam ZN specs, 10Y specs | Tick values, contract sizes |
| — | browser → Ironbeam margins page + JS extract | Full day vs overnight margin table (all asset classes) |
| — | Created output dir | `outputs/2026-09-29/10yr-bond-futures-1000-playbook/` |
| — | Wrote `build_cheatsheet.py` (fpdf2) | — |
| — | Patched: normalize table widths to 191mm; callout box 13→17mm | Fixed 0.1mm overflow + text spill |
| — | Ran build | PDF written, 2 pages, 6,870 bytes |
| — | `uv venv /tmp/pdfv` + `uv pip install pymupdf` | PEP 668 blocked --system; venv worked |
| — | pymupdf layout verification | 2 pages, no content overflow (footer only, by design) |

## Artifacts
- `artifacts/exports/10yr-bond-futures-1000-playbook.pdf` — final deliverable
- `artifacts/exports/build_cheatsheet.py` — reproducible generator
