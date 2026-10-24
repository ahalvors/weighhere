# WeighHere status — 23 Oct 2026

Compiled evening PT 23 Oct 2026 (nightly ship).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **221** | +3 I-84 Columbia River CAT (Pilot #195 Biggs, Love’s #650 Boardman, Pilot #390 Stanfield) |
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
| Moses Lake / Ritzville / I-90 | 2 | unchanged |
| Pasco / Prosser / Tri-Cities | 2 | unchanged |
| Portland / Troutdale / Aurora OR | 3 | unchanged |
| North Bend / Ellensburg / I-90 | 2 | unchanged |
| Albany / Eugene / Roseburg / I-5 | 3 | unchanged |
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
| Ontario / Baker City / I-84 (OR) | 2 | unchanged |
| Madras / Klamath Falls / US-97 (OR) | 2 | unchanged |
| **Biggs / Boardman / Stanfield / I-84 (OR)** | **3** | **new page 23 Oct** — Pilot #195 Biggs Junction (Exit 104), Love’s #650 Boardman (Exit 159), Pilot #390 Stanfield (Exit 188) |
| CAT / truck-stop cards | 157 | +3 Biggs / Boardman / Stanfield |
| Enforcement do-not-go | 2 | unchanged |

## What shipped tonight

**Biggs / Boardman / Stanfield / I-84** (`/biggs-boardman-stanfield/`): fifth Oregon page, first on the Columbia River stretch of I-84 (Sherman, Morrow & Umatilla Counties). All three stops verified tonight (23 Oct) on the operators’ own pages.

- **Pilot Travel Center #195 Biggs Junction** — 91485 Biggs Rufus Hwy, Wasco OR 97065, I-84 Exit 104 at US-97 (Sherman County) — CAT Scale in the store’s own offerings; Open 24 Hours; cylinder propane; (541) 739-2174; geo 45.6695, -120.8349.
- **Love’s Travel Stop #650 Boardman** — 78665 Tower Road, Boardman OR 97818, I-84 Exit 159 (Morrow County) — CAT Scales; store + Truck Care Open 24-hours; RV-friendly parking, bulk propane, tank exchange; (541) 481-2934; geo 45.825166, -119.798742.
- **Pilot Travel Center #390 Stanfield** — 2115 S Hwy 395, Stanfield OR 97875, I-84 Exit 188 at US-395 (Umatilla County) — CAT Scale in own offerings; Open 24 Hours; bulk + cylinder propane; (541) 449-1403; geo 45.765135, -119.205112. Pilot posts “store enhancements underway — some amenities temporarily unavailable”; flagged call-ahead in hours_notes.

Wiring: new `biggs_boardman_stanfield_i84_body()` + `write()` in `build.py`, NAV (`bbs`), footer, guide Oregon lines, 404 lede hub list, Ontario / Madras / Portland pages Related links, `tools/seo.py` PLACES, ADDING_A_PAGE county-slug list (`sherman` / `morrow` / `umatilla`). `CHECKED_HUMAN` → 23 Oct 2026. Held: Flying J #934 La Grande (Exit 265) — live page offerings omit CAT Scale (CAT only appears in its nearby-stops list; search-index snapshot said yes). No Pendleton / Hermiston operator-page CAT.

Previous ship (22 Oct): `/madras-klamath-falls/` — Love’s #795 Madras + Love’s #823 Klamath Falls.

## Sources used (this compile)

- Pilot #195 Biggs Junction: https://locations.pilotflyingj.com/us/or/wasco/91485-biggs-rufus-hwy
- Love’s #650 Boardman: https://www.loves.com/locations/or/boardman/loves-travel-stop-boardman-650
- Pilot #390 Stanfield: https://locations.pilotflyingj.com/us/or/stanfield/2115-s-hwy-395
- Flying J #934 La Grande (held): https://locations.pilotflyingj.com/us/or/la-grande/63276-or-203

## Gaps / deferred

- Madras / Klamath Falls US-97: shipped 22 Oct; no dedicated house; CAT staffing hours unpublished; no Bend / Redmond CAT verified; Pilot / Flying J / TA Petro US-97 own pages not searched
- Biggs / Boardman / Stanfield I-84: shipped 23 Oct; Stanfield store work underway (amenities may be unavailable); CAT staffing hours unpublished; no dedicated house; Flying J #934 La Grande held (live offerings omit CAT); EZ Trip #1226 Biggs offerings omit CAT; no Pendleton / Hermiston CAT
- Cascades: shipped 19 Oct; TA Seattle East hours unpublished (no 24-hour statement on TA page)
- Tri-Cities: shipped 17 Oct with Love’s Pasco + Prosser; TA Grandview not listed (no CAT on TA page at last check); Kennewick / Richland own-page CAT not yet searched
- Portland: shipped 18 Oct (TA Troutdale, Love’s #449, TA Aurora); Pilot / Flying J metro stops not yet checked; no dedicated house; CAT staffing hours unpublished
- Eugene / I-5: shipped 20 Oct (Love’s #728 Albany, TA Coburg, Love’s #312 Roseburg); no dedicated house; CAT staffing hours unpublished; Pilot / Flying J Willamette Valley own pages not searched
- Petro Phoenix #0324 (Medford) still lonely — candidate for a Medford / Klamath or Grants Pass page if a second own-page CAT appears
- Ontario / Baker City I-84: shipped 21 Oct; no dedicated house; CAT staffing hours unpublished; La Grande / Pendleton own-page CAT not searched; Pilot / Flying J eastern Oregon not checked
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
- Next candidates: La Grande if Flying J #934 offerings add CAT, Pilot #232 Ontario OR (Exit 376A) own-page check, Pilot Central Point / Chemult / Klamath Falls OR own-page checks (could unlock Medford with Petro Phoenix), Medford / Phoenix OR on I-5 if a partner appears, Blaine if a second north-I-5 CAT appears, Temecula / Corona (if a second CAT verifies), Carson City if a chain own-page CAT appears, Redding / Anderson second stop, Snowville / Willard if amenities catch up, ONE9 Boise/Nampa/Fruitland if amenities catch up, Ventura / Santa Barbara CDFA re-pull, Beaver if amenities catch up, Love’s Fernley / Winnemucca / Carlin as corridor extensions
- Elko / Winnemucca held: Flying J #692 Wells and Pilot #147 West Wendover (FAQ yes, amenities omit CAT)
- Las Vegas omitted ONE9s still amenities-omit CAT
- ONE9 #1424 Westley — visible amenities card still empty
- EZ Trip #1275 Madera Ave 12 — visible amenities still omit CAT
- Hours / fees / livestock unknown beyond store-listed fuel 24/7 vs CAT staffing
- Ventura / Santa Barbara remain thin
- CDFA Merced / Kern / Shasta / Tehama / Glenn / Fresno / Ventura / Santa Barbara / Sacramento facility grids still often WAF-blocked

## Weekly guides (`/guides/<slug>/`)

- 2026-10-14 — `/guides/ppm-weight-tickets/` How to get PPM weight tickets for a U-Haul move (DFAS, Military OneSource, Fort Hood, NAVSUP, CAT Scale DITY tips/FAQ, Weigh My Truck help). Linked from home hub, footer, `/ppm-dity-southern-california/`, `/public-scale-vs-weigh-station/`. `tools/seo.py` now adds `guides/*/` to the sitemap.
- 2026-10-21 — `/guides/cat-scale-cost/` How much does a CAT Scale cost, and how does it work? (CAT FAQ Q12/Q13/Q21, How To Weigh, DITY tips, Weigh My Truck help; prices checked 21 Oct 2026). Linked from home hub, footer nav, PPM guide, `/cat-2000-lb-minimum/`, `/how-to-weigh-an-rv/`, regional Related lists. Added `.prose table` CSS.
- Queue next: how to weigh an RV (axle/corner, GVWR) → horse/travel trailer + tongue weight → weigh stations vs public scales → GSC queries.
