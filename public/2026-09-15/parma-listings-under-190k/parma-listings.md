# Parma Listings Pull Status
**Timestamp:** 2026-09-15T02:00:10Z
**Task:** Pull active for-sale listings <= $190K in ZIPs 44129, 44134, 44130

## Result: BLOCKED

### Zillapi MCP — FAILED
- **44129** (bbox: -81.78,41.37,-81.68,41.42): Out of credits for this cycle.
- **44134** (bbox: -81.72,41.35,-81.65,41.40): MCP server unreachable (80 consecutive failures).
- **44130** (bbox: -81.80,41.35,-81.73,41.41): MCP server unreachable (80 consecutive failures).

### All Sources Summary
| Source | Result |
|--------|--------|
| Zillapi MCP (all 3 ZIPs) | Out of credits + server unreachable |
| Zillow.com / Redfin / Trulia / Realtor.com | Known PerimeterX/Cloudflare block (not attempted per skill protocol) |

### Direct Zillow Search URLs (open in your browser)
- [44129 — Parma West, under $190K, houses](https://www.zillow.com/parma-oh-44129/houses/190000-_price/)
- [44134 — Parma, under $190K, houses](https://www.zillow.com/parma-oh-44134/houses/190000-_price/)
- [44130 — Parma, under $190K, houses](https://www.zillow.com/parma-oh-44130/houses/190000-_price/)

**Next step:** Resume when Zillapi credits refresh. Use saved bboxes and price cap to re-pull.
