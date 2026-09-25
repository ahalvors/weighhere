# WeighHere status — 24 Sep 2026

Compiled evening PT 24 Sep 2026 (nightly ship).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **131** | +1 TA Livingston #0170 |
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
| Phoenix metro / Maricopa | 4 | unchanged |
| Central Valley (Kern+Fresno+Merced filter) | 19 | +1 Livingston (also on Merced page) |
| Sacramento approaches | 4 | unchanged |
| Grapevine / I-5 mid-CA | 4 | unchanged |
| Hwy 99 / Stockton approaches | 4 | unchanged |
| Madera / Hwy 99 | 2 | unchanged |
| Tulare / Hwy 99 | 2 | unchanged |
| Bakersfield / Hwy 99 | 2 | unchanged |
| Fresno / Hwy 99 · I-5 | 2 | unchanged |
| **Merced / Hwy 99** | **2** | **new** — Highway 59 dedicated + TA #0170 Livingston |
| Salinas / US-101 | 2 | unchanged |
| Weed / Yreka / I-5 | 2 | unchanged |
| Corning / Orland / I-5 | 3 | unchanged |
| Buttonwillow / Lost Hills / I-5 | 2 | unchanged |
| Wheeler Ridge / I-5 | 2 | unchanged |
| Santa Nella / I-5 | 3 | unchanged |
| Landfill / waste rows (sitewide) | 12 | unchanged |
| Dedicated / walk-up houses | 12–13 | Highway 59 re-checked |
| CAT / truck-stop cards | 64–67 | +1 TA Livingston |
| Enforcement do-not-go | 2 | unchanged |

## What shipped tonight

**Merced / Hwy 99** (`/merced/`): new Merced-focused page pairing the existing Highway 59 Scales dedicated house with newly verified TA Livingston #0170 CAT (SR 99 Exit 203 / Winton Parkway). Meets the ≥1 dedicated + CAT bar. No Love’s / Pilot / Petro own city pages in Merced / Livingston / Atwater / Los Banos / Gustine / Chowchilla / Turlock listed CAT on this compile.

- **TA Livingston #0170** — CAT Scale on TA’s own Livingston page (amenities list); new row
- **Highway 59 Scales** — re-verified on ScaleRegistry company + public list (phone updated to (209) 383-1033; lat/lng added); existing row

ONE9 #1424 Westley still deferred (CAT in Pilot JSON/description strings; visible amenities card still not clear enough). Redding / Anderson still only TA #0057. No invented hours/fees/livestock. Store page lists fuel 24/7; that is not a published CAT staffing schedule. CDFA Merced grid WAF-blocked.

## Sources used (this compile)

- TA Livingston #0170: https://www.ta-petro.com/location/ca/ta-livingston/
- Highway 59 Scales (re-verified): https://scaleregistry.com/companies/highway-59-scales
- ScaleRegistry CA public-weighing list: https://scaleregistry.com/public-scales.html
- CAT Scale locator (linked, not republished): https://catscale.com/cat-scale-locator/
- CDFA Merced: WAF 403 / not loaded
- ONE9 #1424 Westley (still deferred): https://locations.pilotflyingj.com/us/ca/westley/7051-mccracken-rd
- Love’s / Pilot city indexes: no Merced / Livingston / Atwater / Los Banos / Gustine / Chowchilla / Turlock store pages
- TA Redding #0057 (still alone for Redding / Anderson): https://www.ta-petro.com/location/ca/ta-redding/

## Gaps / deferred

- Redding / Anderson mid-north I-5: only TA Redding #0057 own-page CAT — need a second stop before `/redding-anderson/`
- ONE9 #1424 Westley — CAT in Pilot page JSON/description; visible amenities incomplete — re-check before Santa Nella / I-5 extension
- Pilot Dealer #1399 Litchfield Park, AZ — CAT on Pilot’s own page; deferred Phoenix extension
- EZ Trip #1275 Madera Ave 12 — visible amenities still omit CAT (embedded JSON noise only); keep omitted from `/madera/`
- Third-party Fresno / Fowler / Traver CAT pins omitted (no operator own page)
- CDFA Merced / Kern / Shasta / Tehama / Glenn / Fresno facility grids still blocked
- Hours / fees / livestock unknown beyond store-listed 24h vs CAT staffing
- Temecula / Corona Love’s still deferred
- Ventura / Santa Barbara remain thin
- Gilroy Garlic Farm / King City / Prunedale third-party CAT still omitted
- Earlimart / Goshen / Visalia third-party CAT still omitted
