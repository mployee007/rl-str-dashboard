# Decisions — Cheapest DDR4 UDIMM for HP Z4 G4 Memory

## 2026-08-27

### Decision: Recommend 8x32GB ECC UDIMM instead of chasing 64GB UDIMMs
- **Context:** User needs a 256GB kit that fits an HP Z4 G4 at the lowest price.
- **Options considered:** 8x32GB ECC UDIMM, 4x64GB ECC UDIMM, used marketplace listings.
- **Decision:** Use 8x32GB ECC UDIMM as the baseline cheapest path.
- **Consequence:** Lower total cost and wider compatibility for Xeon Z4 G4 systems.

### Decision: Treat the Z4 G4 CPU as a compatibility caveat
- **Context:** Z4 G4 memory ceiling differs by processor family.
- **Options considered:** Assume all Z4 G4s take 256GB, or state the CPU dependency explicitly.
- **Decision:** State the CPU dependency explicitly.
- **Consequence:** Avoids an overconfident recommendation on non-Xeon/Core X variants.
