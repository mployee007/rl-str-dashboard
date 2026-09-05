# Parma, OH — Listings Under $190K

**Pull Date:** 2026-09-05  
**Status:** ❌ FAILED — Zillapi credits exhausted  
**ZIPs Targeted:** 44129 (Parma West), 44134 (Parma), 44130 (Parma South)  
**Price Cap:** $190,000  

---

## ⚠️ Zillapi Out of Credits

All three Zillapi search calls failed:

| ZIP | Bounding Box | Error |
|-----|-------------|-------|
| 44129 | -81.78,41.37,-81.68,41.42 | Out of credits for this cycle |
| 44134 | -81.72,41.35,-81.65,41.40 | MCP server unreachable (16 consecutive failures) |
| 44130 | -81.80,41.35,-81.73,41.41 | MCP server unreachable (16 consecutive failures) |

---

## Manual Workaround: Direct Zillow Search Links

Open these in your own browser to view active listings under $190K:

| ZIP | Direct Zillow Search |
|-----|----------------------|
| **44129** | https://www.zillow.com/homes/for_sale/44129_rb/?searchQueryState={"pagination":{},"usersSearchTerm":"44129","mapBounds":{"west":-81.80,"east":-81.66,"south":41.36,"north":41.44},"filterState":{"price":{"max":190000},"sort":{"value":"globalrelevanceex"},"fsba":{"value":false},"fsbo":{"value":false},"nc":{"value":false},"fore":{"value":false},"cmsn":{"value":false},"auc":{"value":false},"pmf":{"value":false},"pf":{"value":false},"mf":{"value":false},"con":{"value":false},"tow":{"value":false},"manu":{"value":false},"apco":{"value":false},"land":{"value":false}},"isListVisible":true} |
| **44134** | https://www.zillow.com/homes/for_sale/44134_rb/?searchQueryState={"pagination":{},"usersSearchTerm":"44134","mapBounds":{"west":-81.74,"east":-81.63,"south":41.34,"north":41.42},"filterState":{"price":{"max":190000},"sort":{"value":"globalrelevanceex"},"fsba":{"value":false},"fsbo":{"value":false},"nc":{"value":false},"fore":{"value":false},"cmsn":{"value":false},"auc":{"value":false},"pmf":{"value":false},"pf":{"value":false},"mf":{"value":false},"con":{"value":false},"tow":{"value":false},"manu":{"value":false},"apco":{"value":false},"land":{"value":false}},"isListVisible":true} |
| **44130** | https://www.zillow.com/homes/for_sale/44130_rb/?searchQueryState={"pagination":{},"usersSearchTerm":"44130","mapBounds":{"west":-81.82,"east":-81.71,"south":41.34,"north":41.43},"filterState":{"price":{"max":190000},"sort":{"value":"globalrelevanceex"},"fsba":{"value":false},"fsbo":{"value":false},"nc":{"value":false},"fore":{"value":false},"cmsn":{"value":false},"auc":{"value":false},"pmf":{"value":false},"pf":{"value":false},"mf":{"value":false},"con":{"value":false},"tow":{"value":false},"manu":{"value":false},"apco":{"value":false},"land":{"value":false}},"isListVisible":true} |

---

## Parma Market Context (from prior research anchors)

For reference when listings do load:

- **44129 (Parma West):** Dense post-war bungalow stock, strong rental demand, median SFR ~$170-190K. Best for stabilized SFR holds and value-add bungalows.
- **44134 (Central Parma):** Mix of bungalows and capes, slightly lower medians. Good duplex/duplex-conversion hunting ground.
- **44130 (Parma South):** Similar to 44129 but slightly wider price band. Watch for blocks near Brookpark Rd for noise discount.

**Rough buy-box guardrails for Parma (from Cleveland metro anchors):**
- Target all-in basis: $140-175K (SFR)
- Target rent: $1,300-1,600/mo (SFR)
- Target gross yield: 8-10%+
- GRM target: sub-12

---

## Next Steps

1. **Top up Zillapi credits** at https://zillapi.com/app/billing
2. **Re-run this cron job** — it will pick up where it left off
3. Or **open the direct Zillow links above** for immediate manual review

Status file saved at: `/opt/data/parma-pull-status.txt`