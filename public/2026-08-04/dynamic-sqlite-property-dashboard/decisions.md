# Decisions — Dynamic SQLite Property Dashboard

## 2026-08-04

### Decision: Use Python stdlib HTTP server instead of FastAPI
- **Context:** FastAPI/uvicorn were not installed in the environment.
- **Options considered:** install new dependencies vs build with Python stdlib only.
- **Decision:** Use `BaseHTTPRequestHandler` + `ThreadingHTTPServer`.
- **Consequence:** No extra dependencies; easier local startup.

### Decision: Keep `properties.json` as an exported compatibility file
- **Context:** The existing dashboard and GitHub Pages workflow already depend on `properties.json`.
- **Options considered:** DB-only storage vs DB plus JSON export sync.
- **Decision:** Sync `properties.json` from SQLite after every change.
- **Consequence:** Local app is dynamic, while static hosts can still render the latest exported data in read-only mode.

### Decision: Auto-fallback ports
- **Context:** Default port 8765 was already occupied in this environment.
- **Options considered:** hard fail on bind vs try nearby ports.
- **Decision:** Attempt 8765, then 8766, then 8767.
- **Consequence:** Server starts more reliably without manual port edits.
