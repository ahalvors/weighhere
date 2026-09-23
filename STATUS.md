# WeighHere status — 22 Sep 2026

Compiled evening PT 22 Sep 2026 (nightly ship).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **130** | +1 (Petro #0309 Corning); Love’s #410 + Pilot #1019 re-verified |
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
| Central Valley (Kern+Fresno+Merced filter) | 18 | unchanged (includes Bakersfield Love’s/Pilot) |
| Sacramento approaches | 4 | unchanged |
| Grapevine / I-5 mid-CA | 4 | unchanged |
| Hwy 99 / Stockton approaches | 4 | unchanged |
| Madera / Hwy 99 | 2 | unchanged |
| Tulare / Hwy 99 | 2 | unchanged |
| Bakersfield / Hwy 99 | 2 | unchanged (shipped 21 Sep) |
| Salinas / US-101 | 2 | unchanged |
| Weed / Yreka / I-5 | 2 | unchanged |
| **Corning / Orland / I-5** | **3** | +1 Petro #0309 (was Love’s #410 + Pilot #1019) |
| Buttonwillow / Lost Hills / I-5 | 2 | unchanged |
| Wheeler Ridge / I-5 | 2 | unchanged |
| Santa Nella / I-5 | 3 | unchanged |
| Landfill / waste rows (sitewide) | 12 | unchanged |
| Dedicated / walk-up houses | 12–13 | unchanged |
| CAT / truck-stop cards | 63–66 | +1 Petro Corning |
| Enforcement do-not-go | 2 | unchanged |

## What shipped tonight

**Corning / Orland / I-5** (`/corning-orland/`): extended existing mid-north I-5 page with Petro #0309 Corning (Exit 630 / South Ave), pairing with Love’s #410 on the same exit. Preferred Redding / Anderson mid-north target still has only **one** own-page CAT (TA Redding #0057) — no Love’s Anderson / Pilot Redding own-page CAT — so deferred `/redding-anderson/` rather than ship a one-stop filler.

- **Petro #0309 Corning** — CAT Scale on Petro’s own South Avenue / I-5 Exit 630 page (new row)
- **Love’s #410 Corning** — re-verified CAT Scales on Love’s own South Ave / I-5 Exit 630 page (existing; notes updated)
- **Pilot #1019 Orland** — re-verified CAT Scale on Pilot’s own Commerce Ln / I-5 Exit 619 page (existing; notes updated)

No invented hours/fees/livestock. Store pages list fuel/store 24/7; that is not a published CAT staffing schedule. CDFA Tehama / Glenn WAF-blocked. Lat/lng for Petro Corning left null.

**Note on 2026-09-21:** contrary to a stale local STATUS (still dated 20 Sep Santa Nella), origin/main already had **Bakersfield / Hwy 99** (`44a777f`, Love’s #830 + Pilot #613, 129 rows). Tonight builds on that tip.

## Sources used (this compile)

- Petro #0309 Corning: https://www.ta-petro.com/location/ca/petro-corning/
- Love’s #410 Corning (re-verified): https://www.loves.com/locations/ca/corning/loves-travel-stop-corning-410
- Pilot #1019 Orland (re-verified): https://locations.pilotflyingj.com/us/ca/orland/4444-commerce-ln
- CAT Scale locator (linked, not republished): https://catscale.com/cat-scale-locator/
- ScaleRegistry CA public-weighing list: no Tehama / Glenn / Corning / Orland dedicated house
- CDFA Tehama / Glenn: WAF-blocked on prior compiles — not re-scraped tonight
- TA Redding #0057 (still alone for Redding / Anderson): https://www.ta-petro.com/location/ca/ta-redding/
- Love’s / Pilot own-site search: no Anderson or Redding second CAT location page found

## Gaps / deferred

- Redding / Anderson mid-north I-5: only TA Redding #0057 own-page CAT verified — need a second stop before `/redding-anderson/`
- Lat/lng for Petro Corning still null
- No ScaleRegistry dedicated walk-up house in Corning / Orland
- CDFA Merced / Kern / Shasta / Tehama / Glenn facility grids still blocked
- Hours / fees / livestock unknown beyond store-listed 24h vs CAT staffing
- Temecula / Corona Love’s still deferred (no Love’s CA store pages for those cities)
- Ventura / Santa Barbara remain thin (industrial/quarry/ag only)
- Gilroy Garlic Farm / King City / Prunedale third-party CAT still omitted
- Earlimart / Goshen / Visalia third-party CAT still omitted
- Bay Area / Half Moon Bay Ox Mountain landfill scale is disposal-oriented — not featured as a general ticket shop
