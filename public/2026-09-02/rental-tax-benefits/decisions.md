# Design Decisions — Rental Tax Dashboard

## Architecture

**Single-page HTML + localStorage** — chosen because:
- No backend/server needed (runs entirely in browser)
- No data privacy concerns (data never leaves user's computer)
- Zero setup (open file in browser)
- Fully self-contained (no build tools, no npm)
- Data persists between sessions via localStorage

## Tech Stack Decisions

| Decision | Rationale |
|----------|-----------|
| **Vanilla JS (no framework)** | Minimizes file size, no build step, easier maintenance |
| **Chart.js CDN** | Industry standard charting lib, small footprint, CDN-hosted |
| **Dark theme (slate/navy)** | Professional appearance, low eye strain for frequent use |
| **localStorage** | Browser-native, no backend, persists across sessions, ~5MB limit adequate |
| **Base64 receipt storage** | Simpler than IndexedDB for small files; 5MB limit noted in UI |
| **13 expense categories** | Mapped directly to IRS Schedule E line items for seamless tax prep |

## Why Not...

- **React/Vue/Svelte:** Overkill for this scope. Vanilla JS kept it under 65KB.
- **IndexedDB:** localStorage is simpler and sufficient for typical rental portfolios.
- **Server-side:** Adds deployment complexity, hosting costs, and data privacy concerns.
- **Multi-page app:** Single-page with tab navigation is snappier and keeps data access simple.

## Depreciation Calculation

Uses simplified straight-line calculation (Cost / Recovery Period). For Form 4562 purposes, this approximates the MACRS mid-month convention. Actual tax filing should use Form 4562 instructions for precise calculations including the first-year mid-month convention adjustment. The dashboard provides a close estimate intended for planning purposes.