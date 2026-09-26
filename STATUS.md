# WeighHere status — 25 Sep 2026

Compiled evening PT 25 Sep 2026 (nightly ship).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **132** | +1 Pilot Dealer #1399 Litchfield Park |
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
| **Phoenix metro / Maricopa** | **5** | **+1** Pilot #1399 Litchfield Park |
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
| CAT / truck-stop cards | 65–68 | +1 Pilot #1399 |
| Enforcement do-not-go | 2 | unchanged |

## What shipped tonight

**Phoenix metro extension** (`/phoenix/`): added Pilot Dealer #1399 Litchfield Park (Hwy 303 & Camelback) — CAT Scale listed in the visible amenities on Pilot Flying J’s own location page. Page now has five own-page CAT stops (I-10 Avondale / Tolleson / Latham / Chandler + Loop 303 Litchfield Park). Meets the multi-stop CAT corridor bar. No dedicated Maricopa walk-up house found (ScaleRegistry still CA-only for those houses).

- **Pilot Dealer #1399 Litchfield Park** — CAT Scale on Pilot’s own amenities list; new row

Temecula / Corona Love’s: no `loves.com/locations/ca/{temecula,corona,fallbrook,eastvale,murrieta,rainbow,pala}` store pages (404). ONE9 #1424 Westley still has empty visible amenities card (CAT only in embedded JSON/description strings). Redding / Anderson still only TA #0057. No invented hours/fees/livestock. Store page lists open 24 hours; that is not a published CAT staffing schedule.

## Sources used (this compile)

- Pilot Dealer #1399 Litchfield Park: https://locations.pilotflyingj.com/us/az/litchfield-park/15112-west-camelback-road
- Existing Phoenix CAT pages (unchanged rows): Flying J #611, Pilot #459, Love’s #659, Love’s #328
- CAT Scale locator (linked, not republished): https://catscale.com/cat-scale-locator/
- ScaleRegistry CA public-weighing list: https://scaleregistry.com/public-scales.html
- ONE9 #1424 Westley (still deferred): https://locations.pilotflyingj.com/us/ca/westley/7051-mccracken-rd
- Love’s city indexes Temecula / Corona / Fallbrook / Eastvale / Murrieta / Rainbow / Pala: 404
- TA Redding #0057 (still alone for Redding / Anderson): https://www.ta-petro.com/location/ca/ta-redding/

## Gaps / deferred

- Temecula / Corona Love’s — no official loves.com store pages found tonight; keep deferred
- Redding / Anderson mid-north I-5: only TA Redding #0057 own-page CAT — need a second stop before `/redding-anderson/`
- ONE9 #1424 Westley — visible amenities card still empty; CAT in JSON/description only — re-check before Santa Nella / I-5 extension
- EZ Trip #1275 Madera Ave 12 — visible amenities still omit CAT (embedded JSON noise only); keep omitted from `/madera/`
- Third-party Fresno / Fowler / Traver CAT pins omitted (no operator own page)
- CDFA Merced / Kern / Shasta / Tehama / Glenn / Fresno facility grids still blocked
- Hours / fees / livestock unknown beyond store-listed 24h vs CAT staffing
- Ventura / Santa Barbara remain thin
- Gilroy Garlic Farm / King City / Prunedale third-party CAT still omitted
- Earlimart / Goshen / Visalia third-party CAT still omitted
- TA Phoenix (Latham) “Scale” mention without CAT on TA’s own page — still omitted
