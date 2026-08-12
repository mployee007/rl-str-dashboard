# Notes — Dynamic SQLite Property Dashboard

## User Context
- User wants the current static property dashboard turned into a dynamic app.
- They specifically asked for SQLite-backed save/manage capability for property entries.

## Observations
- Existing repo: `/opt/data/rl-str-dashboard`
- Existing data source: `/opt/data/rl-str-dashboard/properties.json`
- Port 8765 is occupied in this environment, so the new server auto-falls back to 8766/8767.
- The frontend now supports two modes:
  - live SQLite mode when served from the local Python server
  - static read-only fallback when opened from GitHub Pages or any static host

## Railway deployment notes
- Railway CLI is not authenticated in this environment (`Unauthorized. Please login with railway login`).
- Git push succeeded after preparing deployment files.
- Recommended Railway volume mount path: `/data` with `APP_DATA_DIR=/data`.
