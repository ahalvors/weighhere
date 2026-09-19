# WeighHere status — 18 Sep 2026

Compiled evening PT 18 Sep 2026 (nightly ship).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **123** | +1 (TA #0160 Buttonwillow); Love’s #230 Lost Hills re-checked |
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
| Central Valley (Kern+Fresno+Merced filter) | 11 | unchanged (Lost Hills still included) |
| Sacramento approaches | 4 | unchanged |
| Grapevine / I-5 mid-CA | 4 | unchanged |
| Hwy 99 / Stockton approaches | 4 | unchanged |
| Madera / Hwy 99 | 2 | unchanged |
| Tulare / Hwy 99 | 2 | unchanged |
| Salinas / US-101 | 2 | unchanged |
| Weed / Yreka / I-5 | 2 | unchanged |
| Corning / Orland / I-5 | 2 | unchanged |
| **Buttonwillow / Lost Hills / I-5** | **2** | new page (TA #0160 + Love’s #230) |
| Landfill / waste rows (sitewide) | 12 | unchanged |
| Dedicated / walk-up houses | 12–13 | unchanged |
| CAT / truck-stop cards | 56–59 | +1 Buttonwillow TA |
| Enforcement do-not-go | 2 | unchanged |

## What shipped tonight

**Buttonwillow / Lost Hills / I-5** (`/buttonwillow-lost-hills/`): mid-I-5 corridor page between Grapevine / Lebec and Santa Nella. Preferred Redding / Anderson mid-north target had only **one** own-page CAT (TA Redding #0057 on TA’s Knighton Rd page) — no second Love’s/Pilot/TA own-page CAT in Anderson / Red Bluff / Willows — so deferred that page rather than ship a one-stop filler.

- **TA #0160 Buttonwillow** — CAT Scale on TA’s own Lagoon Drive / I-5 Exit 257 page (new row)
- **Love’s #230 Lost Hills** — CAT Scales on Love’s own Highway 46 / I-5 Exit 278 page (existing row; re-verified)

No invented hours/fees/livestock. Store pages list Open 24 Hours / fuel 24/7; that is not a published CAT staffing schedule. CDFA Kern WAF-blocked. ScaleRegistry: no Buttonwillow / Lost Hills dedicated house on this compile.

## Sources used (this compile)

- TA #0160 Buttonwillow: https://www.ta-petro.com/location/ca/ta-buttonwillow/
- Love’s #230 Lost Hills: https://www.loves.com/locations/ca/lost-hills/loves-travel-stop-lost-hills-230
- TA Redding #0057 (verified, not shipped alone): https://www.ta-petro.com/location/ca/ta-redding/
- Petro Corning #0309 (CAT on own page; same Exit 630 cluster as Love’s #410 — not added tonight): https://www.ta-petro.com/location/ca/petro-corning/
- CAT Scale locator (linked, not republished): https://catscale.com/cat-scale-locator/
- CDFA Shasta / Tehama / Glenn / Kern: WAF-blocked (“Service unavailable” / request blocked)
- ScaleRegistry CA public-weighing list: no Redding / Anderson / Buttonwillow / Lost Hills dedicated house found on this compile
- Love’s all-locations CA list: no Redding / Anderson / Red Bluff / Willows / Temecula / Corona stores

## Gaps / deferred

- Redding / Anderson mid-north I-5: only TA Redding #0057 own-page CAT verified — need a second stop before `/redding-anderson/`
- Petro Corning #0309 CAT verified on TA page but not yet added (overlaps Corning Exit 630 with Love’s #410)
- No ScaleRegistry dedicated walk-up house in Buttonwillow / Lost Hills / Redding / Anderson
- CDFA Kern / Shasta / Tehama / Glenn facility grids still blocked
- Hours / fees / livestock unknown beyond store-listed 24h vs CAT staffing
- Temecula / Corona Love’s still deferred (no Love’s CA store pages for those cities)
- Ventura / Santa Barbara remain thin (industrial/quarry/ag only)
- Gilroy Garlic Farm / King City / Prunedale third-party CAT still omitted
- Earlimart / Goshen / Visalia third-party CAT still omitted
- Bay Area / Half Moon Bay Ox Mountain landfill scale is disposal-oriented — not featured as a general ticket shop
