# Run Log — High-Yield Savings Comparison

## 2026-09-18

### 15:41 UTC — Session start
- User asked: "Can you find me a high yield savings account"
- Attempted web_search — failed (firecrawl not installed)
- Attempted to install firecrawl — permission denied on /opt/hermes/.venv

### 15:42 UTC — Switched to direct scraping
- Attempted Bankrate, NerdWallet, Investopedia — all returned errors (Bankrate 404, NerdWallet wrong turn, Investopedia blocked)
- Attempted Google search via browser — blocked (IP flagged)
- Switched to DuckDuckGo — hit CAPTCHA

### 15:43 UTC — Switched to curl
- Forbes: blocked (captcha-delivery.com)
- Ally: Successful! Extracted rate from HTML meta — 3.00% APY as of 9/16/26
- Marcus: blocked (Cloudflare challenge)
- Capital One: extracted 3.33% (later found to be non-savings rate)
- Discover: got keywords but not rate number (JS-rendered)
- SoFi: 3.10% APY confirmed
- Synchrony: got keywords, no rate number
- CIT Bank: 3.75% APY confirmed
- Betterment: 3.25% APY confirmed
- Wealthfront: 3.55% APY confirmed

### 15:44 UTC — Browser verification
- Capital One 360: 3.00% APY (effective 9/18/26) — Discover now absorbed into CapOne
- American Express: 3.00% APY confirmed
- Synchrony: Access Denied
- Marcus: Cloudflare challenge

### 15:45 UTC — Deliverable creation
- Created output structure: outputs/2026-09-18/high-yield-savings-comparison/
- Wrote: head-to-head-cit-vs-ally.md, account-opening-checklist.md, sources.json, summary.md, notes.md, decisions.md, run-log.md

### Final verified results
1. CIT Bank: 3.75% ✅
2. Wealthfront: 3.55% ✅
3. Betterment: 3.25% ✅
4. SoFi: 3.10% ✅
5. Ally: 3.00% ✅
6. Capital One 360: 3.00% ✅
7. American Express: 3.00% ✅
8. Marcus: ❌ blocked
9. Synchrony: ❌ blocked