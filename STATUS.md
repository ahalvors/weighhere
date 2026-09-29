# WeighHere status — 28 Sep 2026

Compiled evening PT 28 Sep 2026 (nightly ship).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **141** | +4 TA #0225 Tonopah + Love’s #286 Quartzsite + Pilot #328 Quartzsite + Flying J #608 Ehrenberg |
| Los Angeles County | 46 | unchanged |
| Orange County | 7 | unchanged |
| Inland Empire (Riverside + San Bernardino filter) | 23 | unchanged |
| Coachella Valley / I-10 | 6 | unchanged (Blythe dedicated stays here; not double-counted on Quartzsite page) |
| Ontario / I-10 West | 6 | unchanged |
| Imperial Valley / Hwy 86 | 3 | unchanged |
| Antelope Valley / Pearblossom | 4 | unchanged |
| Mojave / Hwy 58 | 4 | unchanged |
| I-15 / High Desert | 4 | unchanged |
| San Diego County | 8 | unchanged |
| Phoenix metro / Maricopa | 5 | unchanged (explicit metro id filter; Tonopah Maricopa row stays on I-10 west page) |
| Casa Grande / Eloy / I-10 | 2 | unchanged |
| Gila Bend / Yuma / I-8 | 3 | unchanged |
| **Quartzsite / Ehrenberg / I-10 west** | **4** | **new page** — TA #0225 + Love’s #286 + Pilot #328 + Flying J #608 |
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
| CAT / truck-stop cards | 77 | +4 I-10 west corridor |
| Enforcement do-not-go | 2 | unchanged |

## What shipped tonight

**Quartzsite / Ehrenberg / I-10 west** (`/quartzsite-ehrenberg/`): new Maricopa + La Paz County corridor page with four CAT Scales verified on TA / Love’s / Pilot Flying J *own* location pages (TA: `<li>CAT Scale</li>`; Love’s: visible `<span>CAT Scales</span>` + `fieldValue: "true"`; Pilot/Flying J: `<li class="Amenities-item">CAT Scale</li>` + FAQ Yes). Meets the multi-stop CAT corridor bar. No ScaleRegistry dedicated Tonopah / Quartzsite / Ehrenberg house — Blythe Public Scales (CDFA Riverside) stays on `/coachella/` only. West of Phoenix metro on I-10 (Exits 103, 17, and 1).

- **TA #0225 Tonopah** — 1010 N. 339th Avenue, I-10 Exit 103 — CAT Scale on ta-petro.com amenities
- **Love’s #286 Quartzsite** — 760 S. Quartzsite Blvd., I-10 Exit 17 — CAT Scales on loves.com amenities
- **Pilot #328 Quartzsite** — 1201 W Main St, I-10/US-95 Exit 17 — CAT Scale on Pilot amenities + FAQ
- **Flying J #608 Ehrenberg** — I-10 Exit 1 Frontage Road N., Ehrenberg — CAT Scale on Flying J amenities + FAQ

Phoenix metro page keeps its explicit five-stop metro id list so the new Maricopa (Tonopah) row does not appear on `/phoenix/`.

Also re-checked deferred candidates (no ship): Redding / Anderson still only TA #0057 own-page CAT; Temecula / Corona / Murrieta Love’s / Pilot city indexes still thin/404; ONE9 #1424 Westley still lacks visible Amenities-item CAT; Ventura / Santa Barbara still thin; CDFA county grids WAF-blocked 403. Love’s #722 Mayer is on **I-17** Exit 263 (own-page CAT) — still needs a second I-17 stop. Love’s #280 Buckeye still no CAT. Sunmart #640 Ehrenberg omitted (no operator own page we treat as primary).

## Sources used (this compile)

- TA #0225 Tonopah: https://www.ta-petro.com/location/az/ta-tonopah/
- Love’s #286 Quartzsite: https://www.loves.com/locations/az/quartzsite/loves-travel-stop-quartzsite-286
- Pilot #328 Quartzsite: https://locations.pilotflyingj.com/us/az/quartzsite/1201-w-main-st
- Flying J #608 Ehrenberg: https://locations.pilotflyingj.com/us/az/ehrenberg/i-10-exit-1-frontage-road-n.
- Love’s #722 Mayer (I-17, deferred): https://www.loves.com/locations/az/mayer/loves-travel-stop-mayer-722
- CAT Scale locator (linked, not republished): https://catscale.com/cat-scale-locator/
- ScaleRegistry CA public-weighing list: https://scaleregistry.com/public-scales.html
- TA Redding #0057 (still alone for Redding / Anderson): https://www.ta-petro.com/location/ca/ta-redding/
- CDFA publicscales index + county grids: WAF-blocked tonight

## Gaps / deferred

- Temecula / Corona / Murrieta Love’s / Pilot — no official store/city pages found; keep deferred
- Redding / Anderson mid-north I-5: only TA Redding #0057 own-page CAT — need a second stop before `/redding-anderson/`
- ONE9 #1424 Westley — visible amenities card still empty; CAT in JSON/description only — re-check before Santa Nella / I-5 extension
- EZ Trip #1275 Madera Ave 12 — visible amenities still omit CAT (embedded JSON noise only); keep omitted from `/madera/`
- Love’s #722 Mayer (I-17 Exit 263) — own-page CAT verified; needs a second I-17 stop for a corridor page
- Sunmart #640 Ehrenberg / other third-party I-10 CAT pins — omitted until operator own page confirms
- Third-party Fresno / Fowler / Traver CAT pins omitted (no operator own page)
- CDFA Merced / Kern / Shasta / Tehama / Glenn / Fresno / Ventura / Santa Barbara / Sacramento facility grids still blocked
- Hours / fees / livestock unknown beyond store-listed 24h vs CAT staffing
- Ventura / Santa Barbara remain thin
- Gilroy Garlic Farm / King City / Prunedale third-party CAT still omitted
- Earlimart / Goshen / Visalia third-party CAT still omitted
- TA Phoenix (Latham) “Scale” mention without CAT on TA’s own page — still omitted
