# Decisions — Options Credit Spread Explained

## 2026-09-01

### Decision: Create a canonical options credit spreads playbook in inputs/reference
- **Context:** The user wants a reusable learning resource that can be expanded over time.
- **Options considered:** Keep session-only notes in `outputs/`; create a long-lived reference document in `inputs/reference/`.
- **Decision:** Store the canonical playbook at `inputs/reference/options-credit-spreads-playbook.md` and mirror a snapshot into this session's output exports.
- **Consequence:** Future research can be integrated into one stable document while preserving dated retrieval through session outputs.

### Decision: Use OIC/OCC and Options Playbook as core research sources for the first version
- **Context:** Some data-fetch tools were unavailable and Fidelity blocked access.
- **Options considered:** Delay the playbook; proceed with accessible educational sources; rely only on prior knowledge.
- **Decision:** Proceed with accessible, directly inspected sources plus a live SPY options-chain example.
- **Consequence:** The playbook is grounded in actual source material and can be expanded later without losing coherence.
