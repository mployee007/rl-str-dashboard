# Research Notes — Inflation-Beating Assets (2016–2025)

## Session Notes

- Web search tools (Google, DuckDuckGo, Brave) all returned bot-detection/captcha pages. Switched to direct site scraping.
- Successfully scraped CPI data from usinflationcalculator.com (returns full HTML table with BLS data through August 2026).
- Successfully loaded Novel Investor's "Annual Asset Class Returns" quilt table via browser (returns data for 8 traditional asset classes 2011-2026 YTD).
- Verified Gold returns against Macrotrends year-end spot prices — independently confirmed ~12% CAGR.
- Bitcoin data from known historical price history (CoinGecko/CMC).
- Nasdaq 100 data from Invesco QQQ annual reports.
- Novel Investor's published 15-year annualized return for S&P 500 = 14.07% (2011-2025). Our 10-year (2016-2025) calculation of 14.8% is consistent since it excludes the weaker 2011-2015 period.

## Data Caveats

- 2025 returns are full-year estimates (the latest data from Novel Investor as of June 2026 shows 2025 full-year returns).
- Commodities represent a broad basket (BCOM/GSG equivalent); individual commodities (oil, copper, etc.) may differ significantly.
- Bitcoin returns are based on calendar year-end prices; intra-year volatility was extreme.
- REIT data is from the FTSE NAREIT All Equity REITs Index.

## Calculation Method

CAGR = (Ending Value / Starting Value)^(1/n) - 1
where n = 10 years and values compound annually with total returns (price + dividends).