# Decisions — Nvidia Latest Earnings Transcript Research

## 2026-08-27

### Decision: Use task slug as session folder
- **Context:** Current session title in state.db was blank.
- **Options considered:** Use literal `session` vs. task-derived slug.
- **Decision:** Use `nvidia-latest-earnings-transcript-research`.
- **Consequence:** Outputs remain organized and retrievable.

### Decision: Treat NVIDIA release as primary quantitative source
- **Context:** Earnings transcripts are useful for nuance, but official releases are more reliable for exact figures.
- **Options considered:** Transcript-only analysis vs. transcript + official release.
- **Decision:** Use transcript for narrative/Q&A and NVIDIA release for exact metrics/guidance.
- **Consequence:** Summary is grounded in both management commentary and official reported figures.
