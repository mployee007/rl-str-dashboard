# Decisions — hermes-task-dashboard

## 2026-08-12

### Decision: Build a file-backed dashboard over outputs/
- **Context:** User wants easy access to completed work and artifacts
- **Options considered:** Session DB-only view vs outputs archive view
- **Decision:** Use outputs archive as primary source and expose via simple dashboard API
- **Consequence:** Dashboard will surface real saved deliverables and be easy to extend
