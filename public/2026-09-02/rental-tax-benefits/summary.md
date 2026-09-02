# Rental Property Tax Benefits — 2026 Federal Tax Guide

**Date:** September 2, 2026  
**Session:** rental-tax-benefits  
**Status:** Complete

## Overview

Comprehensive research on 16 federal tax benefits available to U.S. rental property owners for tax year 2026, plus a fully functional expense-tracking dashboard.

## Deliverables

### 1. Research Report
- **File:** `artifacts/csv/tax-benefits-research.md` (874 lines, ~50KB)
- **Contents:** All 16 tax benefits with eligibility, dollar limits, IRS forms, deadlines, and source URLs
- **Key finding:** Section 199A QBI deduction may have EXPIRED after 2025 — the most critical fact for 2026 planning

### 2. Dashboard Application
- **File:** `artifacts/exports/rental-tax-dashboard.html` (821 lines, self-contained)
- **Features:** Properties, income, expenses (13 categories), mileage log, depreciation tracker, tax reports, import/export, dark-themed responsive UI
- **Dependencies:** Chart.js (CDN), localStorage (no backend needed)

### 3. Supporting Files
- `summary.md` — This file
- `notes.md` — Session notes and methodology
- `sources.json` — Structured source list
- `decisions.md` — Design decisions
- `run-log.md` — Execution log

## Critical 2026 Tax Caveats

1. **QBI Deduction (Section 199A):** Per IRS, applies to tax years ending on or before December 31, 2025. May NOT be available for 2026 unless Congress extended it.
2. **TCJA individual provisions sunset:** Many individual tax provisions expired after 2025 (rates, standard deduction, SALT cap). Verity current law before filing.
3. **2026 inflation-adjusted figures:** Most thresholds listed use 2025 IRS figures; 2026 figures TBD when IRS publishes them (typically October-November 2026).

## How to Use the Dashboard

1. Open `rental-tax-dashboard.html` in any modern browser
2. Add properties first (address, purchase details)
3. Record income, expenses, mileage, and capital assets throughout the year
4. Use the Tax Reports tab to generate Schedule E and Form 4562 summaries
5. Export as JSON for backup or CSV for your CPA

All data stays in your browser's localStorage — no data leaves your computer.