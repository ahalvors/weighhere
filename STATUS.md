# WeighHere status — 27 Sep 2026

Compiled evening PT 27 Sep 2026 (nightly ship).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **137** | +3 Love’s #296 + Pilot #1243 Gila Bend + Love’s #349 Yuma |
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
| Phoenix metro / Maricopa | 5 | unchanged (explicit metro id filter; Gila Bend Maricopa rows stay on I-8 page) |
| Casa Grande / Eloy / I-10 | 2 | unchanged |
| **Gila Bend / Yuma / I-8** | **3** | **new page** — Love’s #296 + Pilot #1243 + Love’s #349 |
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
| CAT / truck-stop cards | 73 | +3 I-8 corridor |
| Enforcement do-not-go | 2 | unchanged |

## What shipped tonight

**Gila Bend / Yuma / I-8** (`/gila-bend-yuma/`): new Maricopa + Yuma County corridor page with three CAT Scales verified on Love’s / Pilot Flying J *own* location pages (Love’s: visible `<span>CAT Scales</span>` + `fieldValue: "true"`; Pilot: `<li class="Amenities-item">CAT Scale</li>` + FAQ Yes). Meets the multi-stop CAT corridor bar. No ScaleRegistry dedicated Gila Bend / Yuma house. West of Phoenix metro on I-8 (Exits 115, 119, and 3).

- **Love’s #296 Gila Bend** — 820 W Pima St, I-8 Exit 115 — CAT Scales on loves.com amenities
- **Pilot #1243 Gila Bend** — 3006 S Butterfield Trl, I-8 Exit 119 — CAT Scale on Pilot amenities + FAQ
- **Love’s #349 Yuma** — 2931 E Gila Ridge Rd, I-8 Exit 3 — CAT Scales on loves.com amenities

Phoenix metro page now filters by an explicit five-stop metro id list so the new Maricopa (Gila Bend) rows do not appear on `/phoenix/`.

Also re-checked deferred candidates (no ship): Redding / Anderson still only TA #0057 own-page CAT; Temecula / Corona / Murrieta Love’s / Pilot city indexes still thin/404; ONE9 #1424 Westley still lacks visible Amenities-item CAT; Ventura / Santa Barbara still thin; CDFA county grids WAF-blocked 403. Love’s #286 Quartzsite is on **I-10** Exit 17 (own-page CAT verified) — kept for a later I-10 west corridor, not mixed into I-8. Love’s #722 Mayer is on **I-17** Exit 263 (own-page CAT) — elsewhere. ONE9 #1244 Gila Bend has no CAT — omitted. Love’s #280 Buckeye still no CAT.

## Sources used (this compile)

- Love’s #296 Gila Bend: https://www.loves.com/locations/az/gila-bend/loves-travel-stop-gila-bend-296
- Pilot #1243 Gila Bend: https://locations.pilotflyingj.com/us/az/gila-bend/3006-s-butterfield-trl
- Love’s #349 Yuma: https://www.loves.com/locations/az/yuma/loves-travel-stop-yuma-349
- Love’s #286 Quartzsite (I-10, deferred): https://www.loves.com/locations/az/quartzsite/loves-travel-stop-quartzsite-286
- Love’s #722 Mayer (I-17, deferred): https://www.loves.com/locations/az/mayer/loves-travel-stop-mayer-722
- ONE9 #1244 Gila Bend (no CAT): https://locations.pilotflyingj.com/us/az/gila-bend/942-e-pima-st
- CAT Scale locator (linked, not republished): https://catscale.com/cat-scale-locator/
- ScaleRegistry CA public-weighing list: https://scaleregistry.com/public-scales.html
- TA Redding #0057 (still alone for Redding / Anderson): https://www.ta-petro.com/location/ca/ta-redding/
- CDFA publicscales index + county grids: WAF-blocked tonight

## Gaps / deferred

- Temecula / Corona / Murrieta Love’s / Pilot — no official store/city pages found; keep deferred
- Redding / Anderson mid-north I-5: only TA Redding #0057 own-page CAT — need a second stop before `/redding-anderson/`
- ONE9 #1424 Westley — visible amenities card still empty; CAT in JSON/description only — re-check before Santa Nella / I-5 extension
- EZ Trip #1275 Madera Ave 12 — visible amenities still omit CAT (embedded JSON noise only); keep omitted from `/madera/`
- Love’s #286 Quartzsite (I-10 Exit 17, La Paz) — own-page CAT verified; optional future I-10 west corridor (not I-8)
- Love’s #722 Mayer (I-17 Exit 263) — own-page CAT verified; not this corridor
- Third-party Fresno / Fowler / Traver CAT pins omitted (no operator own page)
- CDFA Merced / Kern / Shasta / Tehama / Glenn / Fresno / Ventura / Santa Barbara / Sacramento facility grids still blocked
- Hours / fees / livestock unknown beyond store-listed 24h vs CAT staffing
- Ventura / Santa Barbara remain thin
- Gilroy Garlic Farm / King City / Prunedale third-party CAT still omitted
- Earlimart / Goshen / Visalia third-party CAT still omitted
- TA Phoenix (Latham) “Scale” mention without CAT on TA’s own page — still omitted
