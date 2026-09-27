# WeighHere status — 26 Sep 2026

Compiled evening PT 26 Sep 2026 (nightly ship).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **134** | +2 Love’s #265 + #972 Eloy |
| Los Angeles County | 46 | unchanged |
| Orange County | 7 | unchanged |
| Inland Empire (Riverside + San Bernardino filter) | 23 | unchanged |
| Coachella Valley / I-10 | 6 | unchanged |
| Ontario / I-10 West | 6 | unchanged |
| Imperial Valley / Hwy 86 | 3 | unchanged |
| Antelope Valley / Pearblossom | 4 | unchanged |
| Mojave / Hwy 58 | 4 | unchanged |
| I-15 / High Desert | 4 | unchanged |
| San Diego County | 8 | unchanged |
| Phoenix metro / Maricopa | 5 | unchanged |
| **Casa Grande / Eloy / I-10** | **2** | **new page** — Love’s #265 + #972 |
| Central Valley (Kern+Fresno+Merced filter) | 19 | unchanged |
| Sacramento approaches | 4 | unchanged |
| Grapevine / I-5 mid-CA | 4 | unchanged |
| Hwy 99 / Stockton approaches | 4 | unchanged |
| Madera / Hwy 99 | 2 | unchanged |
| Tulare / Hwy 99 | 2 | unchanged |
| Bakersfield / Hwy 99 | 2 | unchanged |
| Fresno / Hwy 99 · I-5 | 2 | unchanged |
| Merced / Hwy 99 | 2 | unchanged |
| Salinas / US-101 | 2 | unchanged |
| Weed / Yreka / I-5 | 2 | unchanged |
| Corning / Orland / I-5 | 3 | unchanged |
| Buttonwillow / Lost Hills / I-5 | 2 | unchanged |
| Wheeler Ridge / I-5 | 2 | unchanged |
| Santa Nella / I-5 | 3 | unchanged |
| Landfill / waste rows (sitewide) | 12 | unchanged |
| Dedicated / walk-up houses | 12–13 | unchanged |
| CAT / truck-stop cards | 67–70 | +2 Love’s Eloy |
| Enforcement do-not-go | 2 | unchanged |

## What shipped tonight

**Casa Grande / Eloy / I-10** (`/casa-grande-eloy/`): new Pinal County corridor page with two Love’s CAT Scales verified on Love’s *own* location pages (visible `<span>CAT Scales</span>` amenity + `fieldValue: true`). Meets the multi-stop CAT corridor bar. No ScaleRegistry dedicated Pinal house. South of Phoenix metro on I-10 (Exits 200 and 203).

- **Love’s #265 Casa Grande / Eloy** — 5000 N Sunland Gin Rd, I-10 Exit 200 — CAT Scales on loves.com amenities
- **Love’s #972 Eloy** — 2950 N Toltec Rd, I-10 Exit 203 — CAT Scales on loves.com amenities

Also re-checked deferred candidates (no ship): Redding / Anderson still only TA #0057 own-page CAT; Temecula / Corona / Murrieta Love’s / Pilot city indexes 404; ONE9 #1424 Westley still lacks visible Amenities-item CAT (CAT only in embedded JSON / `c_pagesAmenities1` strings — no `c_pagesAmenities` list and no FAQ Yes); Ventura / Oxnard / Santa Barbara operator city pages 404; CDFA county grids (Ventura/Shasta/Santa Barbara/etc.) WAF-blocked 403. Love’s #280 Buckeye still no CAT. Love’s Gila Bend #296 / Yuma #349 / Quartzsite #286 / Mayer #722 do list CAT on own pages — deferred as separate I-8 / other corridors, not mixed into tonight’s I-10 Eloy cluster.

## Sources used (this compile)

- Love’s #265 Casa Grande/Eloy: https://www.loves.com/locations/az/eloy/loves-travel-stop-eloy-265
- Love’s #972 Eloy: https://www.loves.com/locations/az/eloy/loves-travel-stop-eloy-972
- Love’s all-locations (CA/AZ index): https://www.loves.com/location-and-fuel-price-search/all-locations
- CAT Scale locator (linked, not republished): https://catscale.com/cat-scale-locator/
- ScaleRegistry CA public-weighing list: https://scaleregistry.com/public-scales.html
- TA Redding #0057 (still alone for Redding / Anderson): https://www.ta-petro.com/location/ca/ta-redding/
- ONE9 #1424 Westley (still deferred): https://locations.pilotflyingj.com/us/ca/westley/7051-mccracken-rd
- Love’s #280 Buckeye (no CAT): https://www.loves.com/locations/az/buckeye/loves-travel-stop-buckeye-280
- CDFA publicscales index + county grids: WAF-blocked tonight

## Gaps / deferred

- Temecula / Corona / Murrieta Love’s / Pilot — no official store/city pages found tonight; keep deferred
- Redding / Anderson mid-north I-5: only TA Redding #0057 own-page CAT — need a second stop before `/redding-anderson/`
- ONE9 #1424 Westley — visible amenities card still empty; CAT in JSON/description only — re-check before Santa Nella / I-5 extension
- EZ Trip #1275 Madera Ave 12 — visible amenities still omit CAT (embedded JSON noise only); keep omitted from `/madera/`
- Love’s Gila Bend #296, Yuma #349, Quartzsite #286, Mayer #722 — own-page CAT verified tonight; optional future I-8 / other AZ corridor pages
- Third-party Fresno / Fowler / Traver CAT pins omitted (no operator own page)
- CDFA Merced / Kern / Shasta / Tehama / Glenn / Fresno / Ventura / Santa Barbara / Sacramento facility grids still blocked
- Hours / fees / livestock unknown beyond store-listed 24h vs CAT staffing
- Ventura / Santa Barbara remain thin
- Gilroy Garlic Farm / King City / Prunedale third-party CAT still omitted
- Earlimart / Goshen / Visalia third-party CAT still omitted
- TA Phoenix (Latham) “Scale” mention without CAT on TA’s own page — still omitted
