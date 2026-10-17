# WeighHere status — 16 Oct 2026

Compiled evening PT 16 Oct 2026 (nightly ship).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **204** | +2 mid-WA I-90 CAT (Love’s #827 Moses Lake, Love’s #514 Ritzville) |
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
| Kingman / I-40 | 4 | unchanged |
| Tucson / Benson / Willcox / I-10 | 4 | unchanged |
| Flagstaff / Winslow / Holbrook / I-40 | 5 | unchanged |
| Mayer / Cordes Lakes / I-17 | 2 | unchanged |
| White Hills / Henderson / US-93 | 2 | unchanged |
| Lake Havasu / I-40 Exit 9 | 2 | unchanged |
| Las Vegas / I-15 | 5 | unchanged |
| Reno / Sparks / Fernley / I-80 | 5 | unchanged |
| Winnemucca / Elko / Wells / I-80 | 5 | unchanged |
| St. George / Cedar City / Parowan / I-15 | 3 | unchanged |
| Fillmore / Nephi / I-15 | 2 | unchanged |
| Springville / Salt Lake / I-15 | 5 | unchanged |
| Brigham / Ogden / I-15 | 3 | unchanged |
| McCammon / Idaho Falls / I-15 | 3 | unchanged |
| Boise / Treasure Valley / I-84 | 5 | unchanged |
| Twin Falls / Burley / I-84 | 3 | unchanged |
| Spokane / Post Falls / I-90 | 4 | unchanged |
| **Moses Lake / Ritzville / I-90** | **2** | **new page** — Love’s #827 Moses Lake, Love’s #514 Ritzville |
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
| CAT / truck-stop cards | 140 | +2 Moses Lake / Ritzville I-90 |
| Enforcement do-not-go | 2 | unchanged |

## What shipped tonight

**Moses Lake / Ritzville / I-90** (`/moses-lake-ritzville/`): Second Washington page, filling the mid-I-90 gap STATUS named after Spokane. Both stops verified CAT Scales on Love’s own store pages (amenities list “CAT Scales”; store Open 24-hours).

- **Love’s Travel Stop #827 Moses Lake** — 4315 Prichard Rd, Moses Lake WA 98837, I-90 Exit 174 (Grant County) — CAT Scales in Love’s amenities, store Open 24-hours; (509) 761-5419; geo 47.102584, -119.341493. Store hours ≠ published CAT staffing → `hours_24h: store_listed_24h`.
- **Love’s Travel Stop #514 Ritzville** — 1370 N Highway 261, Ritzville WA 99169, I-90 Exit 221 (Adams County) — CAT Scales in Love’s amenities, store Open 24-hours; (509) 659-1005; geo 47.11319, -118.36694. ~47 miles east of Moses Lake on I-90 toward Spokane.

Wiring: new `moses_lake_ritzville_i90_body()` + `write()` in `build.py`, NAV, footer, 404 lede, about-page line, Related on Spokane / Boise / Twin Falls / McCammon, `tools/seo.py` PLACES (`"moses-lake-ritzville": ("Moses Lake & Ritzville, WA", "Washington")`). `CHECKED_HUMAN` → 16 Oct 2026. Livestock unknown; no dedicated house verified.

### Candidates checked but not shipped tonight

- **TA Grandview WA** (I-82 Exit 73): TA own page amenities do **not** list CAT Scale — Tri-Cities page still needs a second own-page CAT besides Love’s #811 Pasco / #681 Prosser (both Love’s CAT-verified; held as a separate cluster for a future Tri-Cities / I-82 page).
- **TA Seattle East** (North Bend, I-90 Exit 34): CAT Scale on TA own page — lonely without a second Cascades stop tonight; Love’s #413 Ellensburg (I-90 Exit 106) is Love’s-own CAT-verified but ~70 miles east — held for a Cascades / Seattle-east cluster.
- **TA Express Blaine** (I-5 Exit 275): CAT Scale on TA own page — lonely; no second north-I-5 CAT cluster tonight.
- **Portland metro**: TA Troutdale (I-84 Exit 17) + TA Aurora (I-5 Exit 278) + Love’s #449 Troutdale all CAT-verified — strong OR cluster, deferred so tonight stays on the WA I-90 corridor after Spokane.
- **Ontario OR / I-84**: Love’s #372 Ontario (Exit 374) CAT-verified; TA Huntington still no CAT; Love’s #569 Baker City CAT-verified but farther west — held.
- **Love’s WA/OR state indexes**: still HTTP 500; store pages and `/api/fetch_stores` work.
- Prior holds unchanged: Twin Falls city CAT, Jerome 165/168, Eden 182, ONE9 #777 Boise / #1426 Nampa / #1429 Fruitland, TA Express Dubois #0940, Flying J #748 Willard, #774 Snowville, Tremonton, Carson City, Temecula / Corona, Redding, Beaver-gap stops, Love’s Fernley / Winnemucca / Carlin.

## Sources used (this compile)

- Love’s #827 Moses Lake: https://www.loves.com/locations/wa/moses-lake/loves-travel-stop-moses-lake-827
- Love’s #514 Ritzville: https://www.loves.com/locations/wa/ritzville/loves-travel-stop-ritzville-514
- Love’s locations API (discovery only): https://www.loves.com/api/fetch_stores
- TA Petro WA index: https://www.ta-petro.com/location/wa/
- TA Grandview (checked, no CAT): https://www.ta-petro.com/location/wa/ta-grandview/
- TA Seattle East (checked, CAT, held): https://www.ta-petro.com/location/wa/ta-seattle-east/
- TA Express Blaine (checked, CAT, held): https://www.ta-petro.com/location/wa/ta-express-blaine/
- TA Troutdale / Aurora / Coburg / Petro Phoenix OR (CAT verified, deferred): ta-petro.com OR location pages
- CAT Scale locator (linked, not republished): https://catscale.com/cat-scale-locator/
- ScaleRegistry public-weighing list: https://scaleregistry.com/public-scales.html

## Gaps / deferred

- Love’s #413 Ellensburg (I-90 Exit 106) — CAT on Love’s own page; hold for Cascades / Seattle-east with TA Seattle East
- Tri-Cities / I-82: Love’s #811 Pasco + Love’s #681 Prosser CAT-verified; TA Grandview still no CAT
- Portland / Troutdale / Aurora OR cluster (TA + Love’s) — ready when OR corridor is next
- Ontario OR / I-84 west of Fruitland: Love’s #372 has CAT; need a coherent second nearby or Baker City page
- Spokane: CAT staffing hours unpublished; Broadway hours conflict with Pilot’s listing; no dedicated house
- ONE9 #777 Boise, #1426 Nampa, #1429 Fruitland — hold until amenities list CAT Scale
- Love’s WA/OR/ID state indexes still HTTP 500 (store pages OK)
- Pocatello proper / Blackfoot — no own-page CAT stop found
- Flying J #748 Willard and Flying J #774 Snowville — FAQ-yes / amenities-omit CAT (held)
- Tremonton — no Love’s/Pilot/TA own-page CAT verified
- Mesquite / Beaver Dam gap: Flying J Dealer #1171 Mesquite still omits CAT from amenities
- Flying J Dealer #509 Beaver amenities omit CAT — gap between Parowan and Fillmore
- Carson City / US-395 / Truckee: no Pilot/Love’s/TA/Flying J/Petro own-page CAT yet (Maverik third-party only)
- Temecula / Corona / Murrieta: Pilot Perris #1458 alone — need a second own-page CAT before `/temecula-corona/`
- Redding / Anderson mid-north I-5: only TA Redding #0057 — need a second stop before `/redding-anderson/`
- Next candidates: Cascades / Seattle-east (TA Seattle East + Love’s #413 Ellensburg), Tri-Cities / I-82 (Pasco + Prosser), Portland / Troutdale / Aurora OR, Blaine if a second north-I-5 CAT appears, Ontario OR / Baker City I-84, Temecula / Corona (if a second CAT verifies), Carson City if a chain own-page CAT appears, Redding / Anderson second stop, Snowville / Willard if amenities catch up, ONE9 Boise/Nampa/Fruitland if amenities catch up, Ventura / Santa Barbara CDFA re-pull, Beaver if amenities catch up, Love’s Fernley / Winnemucca / Carlin as corridor extensions
- Elko / Winnemucca held: Flying J #692 Wells and Pilot #147 West Wendover (FAQ yes, amenities omit CAT)
- Las Vegas omitted ONE9s still amenities-omit CAT
- ONE9 #1424 Westley — visible amenities card still empty
- EZ Trip #1275 Madera Ave 12 — visible amenities still omit CAT
- Hours / fees / livestock unknown beyond store-listed fuel 24/7 vs CAT staffing
- Ventura / Santa Barbara remain thin
- CDFA Merced / Kern / Shasta / Tehama / Glenn / Fresno / Ventura / Santa Barbara / Sacramento facility grids still often WAF-blocked

## Weekly guides (`/guides/<slug>/`)

- 2026-10-14 — `/guides/ppm-weight-tickets/` How to get PPM weight tickets for a U-Haul move (DFAS, Military OneSource, Fort Hood, NAVSUP, CAT Scale DITY tips/FAQ, Weigh My Truck help). Linked from home hub, footer, `/ppm-dity-southern-california/`, `/public-scale-vs-weigh-station/`. `tools/seo.py` now adds `guides/*/` to the sitemap.
- Queue next: how much a CAT scale weigh costs and how it works → how to weigh an RV (axle/corner, GVWR) → horse/travel trailer + tongue weight → weigh stations vs public scales → GSC queries.
