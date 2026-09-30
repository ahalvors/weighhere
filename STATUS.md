# WeighHere status — 29 Sep 2026

Compiled evening PT 29 Sep 2026 (nightly ship).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **145** | +4 Love’s #970 + TA #0094 + Flying J #610 + Petro #0315 Kingman |
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
| Phoenix metro / Maricopa | 5 | unchanged (explicit metro id filter) |
| Casa Grande / Eloy / I-10 | 2 | unchanged |
| Gila Bend / Yuma / I-8 | 3 | unchanged |
| Quartzsite / Ehrenberg / I-10 west | 4 | unchanged |
| **Kingman / I-40** | **4** | **new page** — Love’s #970 + TA #0094 + Flying J #610 + Petro #0315 |
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
| CAT / truck-stop cards | 81 | +4 Kingman / I-40 corridor |
| Enforcement do-not-go | 2 | unchanged |

## What shipped tonight

**Kingman / I-40** (`/kingman/`): new Mohave County corridor page with four CAT Scales verified on Love’s / TA / Pilot Flying J / Petro *own* location pages (Love’s: visible `<span>CAT Scales</span>` + `fieldValue: "true"`; TA/Petro: `<li>CAT Scale</li>`; Flying J: `<li class="Amenities-item">CAT Scale</li>` + FAQ Yes). Meets the multi-stop CAT corridor bar. No ScaleRegistry dedicated Kingman house. West-to-east on I-40 Exits 37, 48, 53, and 66.

- **Love’s #970 Kingman** — 3375 W Griffith Rd, I-40 Exit 37 — CAT Scales on loves.com amenities
- **TA #0094 Kingman** — 946 West Beale Street, I-40 Exit 48 — CAT Scale on ta-petro.com amenities
- **Flying J #610 Kingman** — 3300 E Andy Devine Ave, I-40 Exit 53 — CAT Scale on Pilot amenities + FAQ
- **Petro #0315 Kingman** — 970 South Blake Ranch Road, I-40 Exit 66 — CAT Scale on ta-petro.com amenities

Love’s #272 Kingman (I-40 Exit 59) does **not** list CAT on its own loves.com page — omitted (third-party pins ignored).

Also re-checked deferred candidates (no ship): Love’s #722 Mayer still only own-page I-17 CAT (no second I-17 stop found tonight — Love’s Black Canyon City #381 has no confirmed loves.com CAT URL verified). Redding / Anderson still only TA #0057. Temecula / Corona / Murrieta still thin/404. ONE9 #1424 Westley amenities still unclear. Love’s #280 Buckeye still no CAT. Sunmart #640 Ehrenberg still no primary operator page. Ventura / Santa Barbara still thin. CDFA county grids not re-pulled as primary tonight (Kingman corridor stood on operator pages). Pilot #593 Tucson + Love’s #460 Benson (I-10 south) and Pilot #180 Bellemont / Flying J Winslow / TA Holbrook (I-40 east) verified as future corridor seeds — not tonight’s page.

## Sources used (this compile)

- Love’s #970 Kingman: https://www.loves.com/locations/az/kingman/loves-travel-stop-kingman-970
- TA #0094 Kingman: https://www.ta-petro.com/location/az/ta-kingman/
- Flying J #610 Kingman: https://locations.pilotflyingj.com/us/az/kingman/3300-e-andy-devine-ave
- Petro #0315 Kingman: https://www.ta-petro.com/location/az/petro-kingman/
- Love’s #272 Kingman (omitted, no CAT): https://www.loves.com/locations/az/kingman/loves-travel-stop-kingman-272
- Love’s #722 Mayer (I-17, still deferred): https://www.loves.com/locations/az/mayer/loves-travel-stop-mayer-722
- CAT Scale locator (linked, not republished): https://catscale.com/cat-scale-locator/
- ScaleRegistry CA public-weighing list: https://scaleregistry.com/public-scales.html

## Gaps / deferred

- Temecula / Corona / Murrieta Love’s / Pilot — no official store/city pages found; keep deferred
- Redding / Anderson mid-north I-5: only TA Redding #0057 own-page CAT — need a second stop before `/redding-anderson/`
- ONE9 #1424 Westley — visible amenities card still empty; CAT in JSON/description only — re-check before Santa Nella / I-5 extension
- EZ Trip #1275 Madera Ave 12 — visible amenities still omit CAT (embedded JSON noise only); keep omitted from `/madera/`
- Love’s #722 Mayer (I-17 Exit 263) — own-page CAT verified; needs a second I-17 stop for a corridor page
- Tucson / I-10 south: Pilot #593 Tucson + Love’s #460 Benson own-page CAT verified tonight — candidate for a future `/tucson-benson/` (or similar) page; not shipped tonight
- Flagstaff / Bellemont / Winslow / Holbrook I-40 east: Pilot #180 Bellemont (+ others) for a future corridor
- TA Express White Hills (US-93) own-page CAT — deferred to a US-93 / Vegas approach page
- Sunmart #640 Ehrenberg / other third-party I-10 CAT pins — omitted until operator own page confirms
- Third-party Fresno / Fowler / Traver CAT pins omitted (no operator own page)
- CDFA Merced / Kern / Shasta / Tehama / Glenn / Fresno / Ventura / Santa Barbara / Sacramento facility grids still often WAF-blocked
- Hours / fees / livestock unknown beyond store-listed 24h vs CAT staffing
- Ventura / Santa Barbara remain thin
- Gilroy Garlic Farm / King City / Prunedale third-party CAT still omitted
- Earlimart / Goshen / Visalia third-party CAT still omitted
- TA Phoenix (Latham) “Scale” mention without CAT on TA’s own page — still omitted
- Love’s #272 Kingman — no CAT on own page; keep omitted
