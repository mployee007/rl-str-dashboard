# Session Summary — NQ Futures EMA Stack + VWAP Tutorial

**Date:** 2026-10-08
**Request:** Create a tutorial/playbook for NQ/MNQ futures using a three-EMA stack (72/210/420) with session-anchored VWAP strategy.

**Deliverable:**
- Canonical playbook created at `inputs/reference/nq-futures-mavwap-playbook.md`
- Snapshot mirrored to this session's `artifacts/exports/`

**What was built:**
A 15-section living playbook covering:
1. Strategy definition
2. Why futures and why NQ
3. Chart setup (RTH-only, EMA stack, VWAP anchoring)
4. Session rules and trading window
5. Three-filter entry system (EMA stack + VWAP + rejection candle)
6. Scale-out exit rules and VWAP hard-exit
7. Risk rules with contract-sizing math and worked examples
8. Daily routine (pre-market, session, post-session)
9. Trade log template
10. Common mistakes
11. MNQ → NQ transition plan
12. Study drills with answer keys
13. Terminology reference
14. Platform-specific notes (RTH templates, VWAP anchoring)
15. Update protocol and sources