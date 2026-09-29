# Research Notes - 2026-09-29

## Search infrastructure status
- `web_search` (firecrawl backend): **DOWN** — "Feature 'search.firecrawl' unavailable:
  lazy installs disabled".
- `web_extract` (firecrawl): **DOWN** — same cause.
- `mcp_agent_search_http_search` / `deep_search` (SearXNG): **DEGRADED** — only Bing responds,
  returns junk (dictionary definitions). brave/ddg/startpage all suspended/CAPTCHA.
- `mcp_agent_search_http_read_url`: unreliable — "search-about" strategy returns unrelated
  page text (got Wikipedia/World Wide Web for CME URLs).
- **WORKING PATH:** `browser_navigate` → `https://lite.duckduckgo.com/lite/?q=...` for search,
  and direct browser navigation to authoritative pages + `browser_console` JS extraction.

## Key facts gathered
### CME 10-Year T-Note futures (ZN)
- Contract: $100,000 face value; tick 1/32 = $31.25; symbol ZN.
- Live quote (29 Sep 2026, delayed): ZNZ6 = 104'110, -0'045.
- CME margins page: maintenance = **$1,875 USD** (CBT, product code 21, period 09/2026–06/2027).
- Initial margin ≈ 110% of maintenance ≈ ~$2,063.
- DV01 ≈ $64 / bp.

### CME Micro Treasury futures (authoritative CME product page)
| | Ultra 10Y (TN) | Micro Ultra 10Y (MTN) | 10-Year Yield (10Y) |
|---|---|---|---|
| Convention | price | price | yield |
| Settlement | physical | cash | cash |
| Contract size | $88 DV01 | $8.80 DV01 | $10 DV01 |
| Tick | $15.625 | $1.5625 | $1.00 (1/10 bp) |
| Initial margin | $3,000 | ~$300 (est) | ~$320 |

### Ironbeam margin table (day vs overnight, the crux)
Selected rows (Day / Overnight):
- Spot-quoted S&P QSPX $25 / $464 · Nasdaq QNDX $25 / $178
- 1-Ounce Gold 1OZ $25 / $264 · Nano BTC BIT $25 / $230 · Nano ETH ET $25 / $88
- MES $50 / $2,307 · MYM $50 / $1,505 · M2K $50 / $996 · MNQ $100 / $3,542
- Micro Gold MGC $100 / $2,640 · Micro Silver SIL $400 / $7,150
- Micro Crude MCL $200 / $416 · Micro NatGas MNG $50 / $452
- Micro yields 2YY/5YY/10Y/30Y: $50 day / $297–$363 overnight
- 10-Yr Note ZN $200 / $2,063 · 5-Yr ZF $150 / $1,430 · 2-Yr ZT $75 / $1,320
- 30-Yr Bond ZB $500 / $4,070 · Ultra Bond UB $500 / $5,665 · Ultra 10Y TN $300 / $2,860
- E-Mini ES $500 / $23,066 · YM $500 / $15,049 · RTY $500 / $9,962 · NQ $1,000 / $35,418
- Micro FX M6E $50 / $297, M6A $40 / $209, M6B $50 / $220, MCD $50 / $110, MJY $50 / $308, MSF $50 / $495
- Mini grains XC $50 / $215, XW $50 / $363, XK $100 / $440

### Critical nuance
Micro equity index futures (MES/MNQ/MYM) have **overnight** margins of $1,505–$3,542 —
**not holdable overnight on a $1,000 account**, even though their day margin is only $50–$100.

## Tooling notes (environment)
- fpdf2 present (Pillow missing → no images, text/vector only).
- No weasyprint, wkhtmltopdf, chromium, pandoc, poppler, imagemagick.
- pymupdf installable via `uv venv` (PEP 668 blocks `--system` installs) → used for
  programmatic layout verification (text-block bbox bounds check).
