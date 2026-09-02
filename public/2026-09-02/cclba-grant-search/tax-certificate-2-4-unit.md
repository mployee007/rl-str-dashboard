# 2022 Scavenger Sale — 2-4 Unit Tax Certificate Parcels

**Date:** September 2, 2026
**Source:** CCLBA 2022 Scavenger Sale Bids PDF (1,951 parcels), parsed + cross-verified against Zillow
**Request:** Identify 2-4 unit properties in the tax certificate (scavenger sale) pool

---

## Headline Result

**461 parcels** out of the 1,951 scavenger-sale tax certificates are 2-4 unit residential buildings.

| Metric | Value |
|--------|-------|
| Total scavenger sale parcels | 1,951 |
| **2-4 unit parcels** | **461** (23.6%) |
| Chicago | 281 |
| Suburbs (Harvey, Dolton, Calumet City, etc.) | 180 |
| **Total delinquent tax on 461 parcels** | **$18.0M** (all forgiven via Tax Certificate Program) |
| Chicago delinquent tax | $5.9M |
| Avg delinquent per Chicago parcel | ~$21,079 |

---

## How 2-4 Unit Properties Were Identified

The PDF carries a **CC Land Use Code** for each parcel. Cross-referenced against Zillow property data, the 2-4 unit (multi-family residential) codes are:

| Code | Parcels | Meaning (verified) | Zillow confirmation |
|------|---------|--------------------|---------------------|
| **2-03** | 233 | Two-to-six unit apartment building | — |
| **2-11** | 189 | Two-to-six unit apartment (attached/garden) | 9411 S Champlain = MULTI_FAMILY |
| **2-04** | 10 | Multi-family (larger) | 5206 S Wells St = MULTI_FAMILY |
| **2-12** | 29 | Mixed use (storefront + 2-4 apartments) | 2541 W 63rd St = MULTI_FAMILY 4,500 sqft |

**Excluded** (verified single-family, NOT 2-4 unit): 2-01, 2-02, 2-05 (6615 S Aberdeen = SINGLE_FAMILY), 2-34 (split level), 2-95 (townhome), 2-99 (condo).

---

## Chicago 2-4 Unit Parcels by Neighborhood (281 total)

| Neighborhood | Parcels |
|-------------|---------|
| **Roseland** | 69 |
| **Englewood West** | 54 |
| **West Pullman** | 39 |
| **Englewood East** | 29 |
| **South Chicago** | 28 |
| New City | 9 |
| Greater Grand Crossing | 7 |
| Auburn Gresham | 5 |
| Austin | 5 |
| Fuller Park | 5 |
| North Lawndale | 4 |
| Pullman | 4 |
| Riverdale | 3 |
| South Shore | 3 |
| Washington Heights | 3 |
| Burnside / Chicago Lawn / Morgan Park / Washington Park / Woodlawn | 2 each |
| Ashburn / Avalon Park / Chatham / West Garfield Park | 1 each |

### Your OZ ZIP Areas (60616 / 60637 / 60653)

| Address | Neighborhood | Ward | Code | Delinquent (forgiven) |
|---------|-------------|------|------|----------------------|
| **6556 S Champlain Ave** | Woodlawn (60637) | 20 | 2-03 | $13,023 |
| **6312 S St Lawrence Ave** | Woodlawn (60637) | 20 | 2-11 | $35,743 |

*Your Englewood focus (60621/60636) has **83** parcels — the densest concentration.*

---

## Top 15 Chicago Parcels by Tax Write-Off (biggest savings)

| Delinquent Tax | Address | Neighborhood | Ward | Code |
|---------------|---------|-------------|------|------|
| $191,351 | 5200 W Chicago Ave | Austin | 37 | 2-12 |
| $121,395 | 4245 W Cermak Rd | North Lawndale | 22 | 2-12 |
| $117,616 | 5517 W Chicago Ave | Austin | 37 | 2-12 |
| $86,679 | 138 E 118th St | West Pullman | 9 | 2-04 |
| $86,484 | 9411 S Champlain Ave | Roseland | 9 | 2-11 |
| $80,293 | 153 E 107th St | Roseland | 9 | 2-11 |
| $63,884 | 11314 S Michigan Ave | Roseland | 9 | 2-12 |
| $60,548 | 10454 S Maryland Ave | Pullman | 9 | 2-11 |
| $59,271 | 10952 S Michigan Ave | Roseland | 9 | 2-12 |
| $58,462 | 5229 W Ferdinand St | Austin | 37 | 2-11 |
| $52,504 | 10914 S Indiana Ave | Roseland | 9 | 2-11 |
| $51,192 | 12143 S Green St | West Pullman | 34 | 2-11 |
| $51,104 | 344 E Kensington Ave | West Pullman | 9 | 2-11 |
| $49,734 | 11331 S Edbrooke Ave | Roseland | 9 | 2-11 |
| $48,621 | 7953 S Escanaba Ave | South Chicago | 7 | 2-11 |

---

## Who Controls These Parcels

| Entity Bidding On Behalf | Parcels | Notes |
|--------------------------|---------|-------|
| CCLBA – Focus Community (City) | 144 | Standard CCLBA pipeline |
| CCLBA – Focus Community (Suburbs) | 89 | Suburban pipeline |
| **South Suburban Land Bank (SSLBDA)** | 75 | Separate south-suburb land bank |
| CCLBA – Invest South/West (½ mile buffer) | 44 | ISW initiative parcels |
| CCLBA – Residential Structures | 43 | Residential-designated |
| CCLBA – Roseland Focus | 20 | Roseland-specific |
| Village of Dolton | 11 | Municipal |
| CCLBA – City of Chicago MMRP | 10 | Municipal marketing |
| Others (CTA Red Line, DPD, United Power, etc.) | 25 | Various |

⚠️ **Key nuance:** Not every bid is held by CCLBA. 75 are SSLBDA (South Suburban Land Bank), and others belong to municipalities/agencies. Only the CCLBA-held parcels flow through CCLBA's Tax Certificate Program described earlier. Verify the holding entity before pursuing any specific parcel.

---

## Files Produced

| File | Description |
|------|-------------|
| `tax_certificate_2_4_unit_parcels.csv` | All 461 parcels (full detail: PIN, address, city, ward, delinquent, code, entity) |
| `tax_certificate_2_4_unit_chicago.csv` | 281 Chicago parcels, sorted by neighborhood |
| `scav_sale_parcels.csv` | All 1,950 parsed scavenger-sale parcels (complete reference) |

**Contact to pursue:** (312) 603-8015 | Info@CookCountyLandBank.org
**Portal:** https://public-cclba.epropertyplus.com → "2022 Scavenger Sale – CCLBA Tax Certificates Bids" layer
