# WeighHere status — 30 Oct 2026

Compiled evening PT 30 Oct 2026 (nightly ship).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **243** | +2 Belen / Truth or Consequences CAT (Love’s #726, Love’s #1045) |
| Belen / Truth or Consequences / I-25 (NM) | 2 | new 30 Oct |
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
| Biggs / Boardman / Stanfield / I-84 (OR) | 3 | shipped 23 Oct |
| Medford / Central Point / Phoenix / I-5 (OR) | 2 | shipped 24 Oct |
| Gallup / Jamestown / Milan / I-40 (NM) | 3 | shipped 25 Oct |
| Albuquerque / I-40 · I-25 (NM) | 3 | page 26 Oct — Flying J #689 (I-40 Exit 153), TA Albuquerque #0081 (I-40 Exit 159A/D), Pilot #1106 (I-25 Exit 215) |
| Moriarty / Santa Rosa / I-40 (NM) | 3 | shipped 27 Oct |
| Las Cruces / Deming / Lordsburg / I-10 (NM) | 7 | shipped 28 Oct |
| **Tucumcari / Glenrio / I-40 (NM)** | **2** | **new page 29 Oct** — Love’s #262 Tucumcari (I-40 Exit 333), TA Glenrio #0471 (Exit 369) |
| CAT / truck-stop cards | 177 | +2 Tucumcari / Glenrio |
| Enforcement do-not-go | 2 | unchanged |

## What shipped tonight

**Belen / Truth or Consequences / I-25** (`/belen-truth-or-consequences/`): sixth New Mexico page, first on central I-25, fills the Albuquerque–Las Cruces gap. Both verified tonight (30 Oct) on Love’s own pages.

- **Love’s #726 Belen** — 1903 Camino Del Llano, Belen NM 87002, I-25 Exit 191 — CAT Scales in amenities; Store Open 24-hours, Truck Care 6 a.m.–11 p.m.; (505) 864-6107; geo 34.652601, -106.793411. County slug `valencia`.
- **Love’s #1045 Truth or Consequences** — 224 Dr Hubble Rd, Truth or Consequences NM 87901, I-25 Exit 79 — CAT Scales in amenities; Store Open 24-hours; (575) 297-6012; geo 33.155286, -107.258575. County slug `sierra`.
- Checked, no CAT in amenities: Love’s #733 Las Vegas NM (I-25 Exit 347), Love’s #22 Clayton (US-87).
- TA Springer (I-25 Exit 419) own page confirmed CAT Scale tonight but held — needs a second north-I-25 stop before an I-25 north page (Las Vegas NM has no CAT).

Wiring: new `belen_truth_or_consequences_body()` + `write()` in `build.py`, NAV (`btc`), footer, 404 lede hub list, PPM guide New Mexico line, Flagstaff related, Albuquerque and Las Cruces gap notes + Related, `tools/seo.py` PLACES, ADDING_A_PAGE county table. `CHECKED_HUMAN` → 30 Oct 2026. stations.json 243 rows.

Previous ship (29 Oct): `/tucumcari-glenrio/` — Love’s #262 Tucumcari, TA Glenrio #0471.

## Sources used (this compile)

- Love’s #726 Belen: https://www.loves.com/locations/nm/belen/loves-travel-stop-belen-726
- Love’s #1045 Truth or Consequences: https://www.loves.com/locations/nm/truth-or-consequences/loves-travel-stop-truth-or-consequences-1045
- Love’s #733 Las Vegas NM (no CAT): https://www.loves.com/locations/nm/las-vegas/loves-travel-stop-las-vegas-733
- Love’s #22 Clayton (no CAT): https://www.loves.com/locations/nm/clayton/loves-travel-stop-clayton-22
- TA Springer (CAT, held): https://www.ta-petro.com/location/nm/ta-springer/

## Gaps / deferred

- Belen / Truth or Consequences I-25: shipped 30 Oct; no dedicated house; CAT staffing hours unpublished; Los Lunas and Socorro own pages not checked; Pilot/TA have no verified central-I-25 NM CAT. I-25 north (Springer / Raton / Santa Fe) needs a second CAT stop beside TA Springer; Love’s Clovis #329/#760 still unchecked
- Las Cruces / Deming / Lordsburg I-10: shipped 28 Oct; no dedicated house; CAT staffing hours unpublished; TA Las Cruces / Petro Deming publish only fuel 24/7 (no store statement); ONE9 #1489 Deming lists no amenities; I-25 Los Lunas / Socorro / T or C unchecked; TA Glenrio #0471 (I-40 Exit 369, CAT in amenities) and TA Springer seen on TA’s NM index — candidates for an east-I-40 / I-25 north page
- Gallup / Milan I-40 NM: shipped 25 Oct; no dedicated house; CAT staffing hours unpublished; TA Gallup / Petro Milan publish no 24-hour store statement; ONE9 #1358 Gallup held (FAQ yes, own offerings omit CAT); Love’s #215 Gallup lists no CAT
- Albuquerque: shipped 26 Oct; no dedicated house; CAT staffing hours unpublished; TA #0081 publishes no 24-hour store statement; Los Lunas / Socorro / Las Cruces on I-25 unchecked
- Tucumcari / Glenrio I-40: shipped 29 Oct; no dedicated house; CAT staffing hours unpublished; TA Glenrio publishes only restaurant hours; San Jon (Roady’s Chisum) not checked; Love’s Belen #726, Truth or Consequences #1045, Las Vegas NM #733, Clayton #22, Clovis #329/#760 own pages not yet checked. TA Springer (I-25 Exit 419, CAT in amenities seen 29 Oct) is a candidate for an I-25 north page (Springer / Raton / Las Vegas NM)
- Moriarty / Santa Rosa I-40: shipped 27 Oct; Love’s #285 Santa Rosa checked 29 Oct (no CAT); no dedicated house; CAT staffing hours unpublished; TA Moriarty / TA Santa Rosa publish no 24-hour store statement; Pilot Flying J has no Tucumcari / Santa Rosa store pages (404) and TA has no Tucumcari page; Love’s Santa Rosa / Tucumcari and Clines Corners own pages not yet searched. Next NM: Tucumcari CAT check (extend this page or ship with San Jon), then I-25 south (Los Lunas / Socorro / Las Cruces)
- Madras / Klamath Falls US-97: shipped 22 Oct; no dedicated house; CAT staffing hours unpublished; no Bend / Redmond CAT verified; Pilot / Flying J / TA Petro US-97 own pages not searched
- Biggs / Boardman / Stanfield I-84: shipped 23 Oct; Stanfield store work underway (amenities may be unavailable); CAT staffing hours unpublished; no dedicated house; Flying J #934 La Grande held (live offerings omit CAT); EZ Trip #1226 Biggs offerings omit CAT; no Pendleton / Hermiston CAT
- Cascades: shipped 19 Oct; TA Seattle East hours unpublished (no 24-hour statement on TA page)
- Tri-Cities: shipped 17 Oct with Love’s Pasco + Prosser; TA Grandview not listed (no CAT on TA page at last check); Kennewick / Richland own-page CAT not yet searched
- Portland: shipped 18 Oct (TA Troutdale, Love’s #449, TA Aurora); Pilot / Flying J metro stops not yet checked; no dedicated house; CAT staffing hours unpublished
- Eugene / I-5: shipped 20 Oct (Love’s #728 Albany, TA Coburg, Love’s #312 Roseburg); no dedicated house; CAT staffing hours unpublished; Pilot / Flying J Willamette Valley own pages not searched
- Medford / Central Point I-5: shipped 24 Oct; no dedicated house; CAT staffing hours unpublished; no Grants Pass / Ashland own-page CAT searched
- Pilot #504 Klamath Falls (US-97) shows CAT Scale in Pilot’s nearby-store data (seen 24 Oct) — candidate to add to `/madras-klamath-falls/` after an own-page check
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
- Next candidates: La Grande if Flying J #934 offerings add CAT, Pilot #232 Ontario OR (Exit 376A) own-page check, Pilot #504 Klamath Falls own-page check (extend Madras / Klamath Falls), Chemult own-page check, Grants Pass if an own-page CAT appears, Blaine if a second north-I-5 CAT appears, Temecula / Corona (if a second CAT verifies), Carson City if a chain own-page CAT appears, Redding / Anderson second stop, Snowville / Willard if amenities catch up, ONE9 Boise/Nampa/Fruitland if amenities catch up, Ventura / Santa Barbara CDFA re-pull, Beaver if amenities catch up, Love’s Fernley / Winnemucca / Carlin as corridor extensions
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
- 2026-10-29 (catch-up for missed Wed 28 Oct run) — `/guides/tongue-weight/` How to weigh a travel trailer and check tongue weight at a CAT Scale (CAT How To Weigh, Oregon DOT/NHTSA Towing a Trailer PDF, Nissan 2026 Towing Guide). Linked from home hub, footer nav, CAT cost guide, RV, horse-trailer page, regional Related lists. Skipped RV/horse/vs topics: top-level pages already exist.
- Queue next: how to weigh an RV (axle/corner, GVWR) → horse/travel trailer + tongue weight → weigh stations vs public scales → GSC queries.
