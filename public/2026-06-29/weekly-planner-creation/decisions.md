# Decisions — Weekly Planner Creation

## 2026-06-29

### Decision: Use trycloudflare.com quick tunnel (temporary)
- **Context:** cloudflared tunnel login kept returning 404s in user's browser; headless browser hit Cloudflare bot detection
- **Option considered:** Permanent tunnel with API token (blocked by security prompts), quick tunnel (works instantly)
- **Decision:** Quick tunnel for now, revisit permanent tunnel later
- **Consequence:** URL changes on restart, but works immediately

### Decision: Output structure at outputs/YYYY-MM-DD/<session-title>/
- **Context:** User wants standardized per-session output organization
- **Files:** summary.md, notes.md, sources.json, decisions.md, run-log.md + artifacts/{charts,csv,images,exports}
- **Also:** inputs/raw/ for raw data, inputs/reference/ for reusable references
- **Rule:** Never save final outputs in repo root