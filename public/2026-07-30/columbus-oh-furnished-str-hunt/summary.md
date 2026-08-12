# Columbus OH furnished STR hunt

## Objective
Find furnished single-family homes or townhomes for rent in Columbus, Ohio target ZIP codes 43214, 43210, 43801, and 43215, priced $1,500-$3,000/month, listed more than 60 days, using Zillapi and Craigslist, and return only properties with estimated monthly STR spread over $1,000.

## Result
**No qualifying properties found** under the full filter set.

## What was checked
- **Zillapi / Zillow search** across Columbus target ZIP coverage with multiple bounding boxes
- **Craigslist** for furnished houses/townhouses, $1,500-$3,000, beyond 30 days, centered on ZIP 43215 within 15 miles

## Why nothing qualified
- Zillapi produced mainly apartment/building inventory in the target ZIPs.
- The only true house/townhome-style Zillapi hit in the target ZIPs with a spread over $1,000 was **39 Sunnyside Ln, Columbus, OH 43214**, but it was listed only **17 days** and was **not verified furnished**.
- Craigslist returned **zero local Columbus results** for the furnished house/townhouse + price-band + older-listing filter. The page explicitly showed **"Zero local results found"** and only wider-area results from outside Columbus.

## Near miss
- **39 Sunnyside Ln, Columbus, OH 43214** — house for rent, $1,600, 17 days on Zillow, estimated moderate STR revenue $2,925, spread **+$1,325**. Failed the >60 days requirement and furnished requirement.
