# WeighHere status — 21 Sep 2026

Compiled evening PT 21 Sep 2026 (nightly ship).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **129** | +2 (Love's #830 + Pilot #613 Bakersfield) |
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
| Central Valley (Kern+Fresno+Merced filter) | 18 | +2 Bakersfield Love's/Pilot (Kern; also on dedicated page) |
| Sacramento approaches | 4 | unchanged |
| Grapevine / I-5 mid-CA | 4 | unchanged (Love's #441 dual-listed with Santa Nella page) |
| Hwy 99 / Stockton approaches | 4 | unchanged |
| Madera / Hwy 99 | 2 | unchanged |
| Tulare / Hwy 99 | 2 | unchanged |
| **Bakersfield / Hwy 99** | **2** | new page (Love's #830 + Pilot #613) |
| Salinas / US-101 | 2 | unchanged |
| Weed / Yreka / I-5 | 2 | unchanged |
| Corning / Orland / I-5 | 2 | unchanged |
| Buttonwillow / Lost Hills / I-5 | 2 | unchanged |
| Wheeler Ridge / I-5 | 2 | unchanged |
| Santa Nella / I-5 | 3 | unchanged |
| Landfill / waste rows (sitewide) | 12 | unchanged |
| Dedicated / walk-up houses | 12–13 | unchanged |
| CAT / truck-stop cards | 62–65 | +2 Bakersfield Love's/Pilot |
| Enforcement do-not-go | 2 | unchanged |

## What shipped tonight

**Bakersfield / Hwy 99** (`/bakersfield/`): Southern Hwy 99 corridor in Kern County. Two verified CAT Scales from operator own-pages: Love's #830 (Exit 18 / Taft Hwy) and Pilot #613 (Exit 39 / Zachary Ave). Fills the Hwy 99 gap south of Tulare. Redding / Anderson mid-north I-5 still deferred (only TA #0057 verified — no second own-page CAT).

- **Love's #830 Bakersfield** — CAT Scales on Love's own Hwy 99 Exit 18 / Taft Hwy page (new row)
- **Pilot #613 Bakersfield** — CAT Scale confirmed in FAQ on Pilot Flying J's own Hwy 99 Exit 39 / Zachary Ave page (new row)

No invented hours/fees/livestock. Store pages list fuel/store 24h; that is not a published CAT staffing schedule. CDFA Kern grid WAF-blocked. ScaleRegistry: Selma / Merced remain the Central Valley dedicated houses — no Bakersfield / Kern dedicated house verified.

## Sources used (this compile)

- Love's #830 Bakersfield: https://www.loves.com/locations/ca/bakersfield/loves-travel-stop-bakersfield-830
- Pilot #613 Bakersfield: https://locations.pilotflyingj.com/us/ca/bakersfield/17047-zachary-ave
- CAT Scale locator (linked, not republished): https://catscale.com/cat-scale-locator/
- ScaleRegistry CA public-weighing list: Selma / Merced / Lancaster / Colton — no Bakersfield / Kern dedicated house
- CDFA Kern: WAF-blocked ("Service unavailable" / request blocked) — noted and moved on
- Petro Corning #0309 (CAT on own page; Exit 630 with Love's #410 — still not added): https://www.ta-petro.com/location/ca/petro-corning/
- TA Redding #0057 (still alone for Redding / Anderson): https://www.ta-petro.com/location/ca/ta-redding/

## Gaps / deferred

- Redding / Anderson mid-north I-5: only TA Redding #0057 own-page CAT verified — need a second stop before `/redding-anderson/`
- Petro Corning #0309 CAT verified on TA page but not yet added (overlaps Corning Exit 630 with Love's #410)
- Lat/lng for Bakersfield Love's #830 and Pilot #613 still null
- Lat/lng for Santa Nella TA / Petro / Love's still null
- No ScaleRegistry dedicated walk-up house in Bakersfield / Kern or Santa Nella
- CDFA Merced / Kern / Shasta / Tehama / Glenn facility grids still blocked
- Hours / fees / livestock unknown beyond store-listed 24h vs CAT staffing
- Temecula / Corona Love's still deferred (no Love's CA store pages for those cities)
- Ventura / Santa Barbara remain thin (industrial/quarry/ag only)
- Gilroy Garlic Farm / King City / Prunedale third-party CAT still omitted
- Earlimart / Goshen / Visalia / Delano third-party CAT still omitted
- Bay Area / Half Moon Bay Ox Mountain landfill scale is disposal-oriented — not featured as a general ticket shop
