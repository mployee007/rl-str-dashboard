# Parma Under-$190K Listing Pull — FAILED
**Run date:** 2026-09-29
**Status:** BLOCKED — No data retrieved

---

## ⛔ Pull Failed — All Data Sources Blocked

### Tier 1: Zillapi MCP
**Result:** ❌ Out of credits
**Error:** `"Out of credits for this cycle. Top up or upgrade at https://zillapi.com/app/billing."`
Subsequent calls returned `"MCP server 'zillapi' is unreachable after 43 consecutive failures."`

### Tier 2: Camofox Browser → Zillow.com
**Result:** ❌ Cloudflare "Press & Hold" captcha on first navigation
**URL attempted:** `https://www.zillow.com/homes/for_sale/44129_rb/1-_beds/0-190000_price/pricea_sort/`
**Error:** Reference ID `f498481c-bc25-11f1-afab-3019973295bd` — IP rate-limited. Cannot solve programmatically.

### Tier 3 & 4
Not attempted — Tiers 1 and 2 already confirmed the block.

---

## What's needed to unblock

| Blocker | Fix |
|---------|-----|
| Zillapi credits exhausted | Top up at https://zillapi.com/app/billing |
| Zillow IP captcha-blocked | Rotate IP (VPN, proxy, ISP DHCP renew) before next Camofox attempt |

---

## Manual lookup URLs (open in your own browser)

| ZIP | Area | Zillow Link |
|-----|------|-------------|
| **44129** | Parma West | [View listings](https://www.zillow.com/homes/for_sale/44129_rb/1-_beds/0-190000_price/pricea_sort/) |
| **44134** | Parma East / Seven Hills | [View listings](https://www.zillow.com/homes/for_sale/44134_rb/1-_beds/0-190000_price/pricea_sort/) |
| **44130** | Middleburg Heights / Parma Heights | [View listings](https://www.zillow.com/homes/for_sale/44130_rb/1-_beds/0-190000_price/pricea_sort/) |

All URLs pre-filtered: 1+ beds, ≤$190K, sorted by price (lowest first).

---

## Next scheduled run
This cron job will retry on its next cycle. If Zillapi credits have been refreshed by then, pull will proceed normally. If Camofox IP is still blocked, the browser tier will also fail.

Status file: `/opt/data/parma-pull-status.txt`
Report file: `/opt/data/outputs/2026-09-29/parma-listings-under-190k/parma-listings.md`