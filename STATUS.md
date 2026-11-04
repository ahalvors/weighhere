# WeighHere status — 3 Nov 2026

Compiled evening PT 3 Nov 2026 (nightly ship).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **263** | +6 Far West Texas CAT (Pilot #209 Van Horn, Flying J #553 + Love’s #542 Fort Stockton, Pilot #1146 + Flying J #736 + Love’s #492 Pecos) |
| Van Horn / Fort Stockton / Pecos / I-10 · I-20 (TX) | 6 | new 3 Nov — third Texas page |
| Amarillo / I-40 (TX) | 6 | 2 Nov |
| El Paso / Anthony / Santa Teresa / I-10 (TX · NM) | 5 | 1 Nov — first Texas page |
| Clovis / Hobbs / Eunice (eastern NM) | 3 | 31 Oct |
| Belen / Truth or Consequences / I-25 (NM) | 2 | 30 Oct |
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
| CAT / truck-stop cards | 199 | +6 Far West Texas |
| Enforcement do-not-go | 2 | unchanged |

## What shipped tonight

**Van Horn / Fort Stockton / Pecos** (`/van-horn-fort-stockton-pecos/`): third Texas page (Culberson, Pecos and Reeves Counties; all six confirmed via the Census geocoder). All six verified tonight (3 Nov) on operators’ own pages; every one says the store is open 24 hours.

- **Pilot #209 Van Horn** — 501 Van Horn Dr, Van Horn TX 79855, I-10 Exit 140A — CAT (offering 318) in own offerings; status Open; is24Hours true; (915) 295-4150; geo 31.03603, -104.829483. County slug `culberson`.
- **Flying J #553 Fort Stockton** — 2571 N Front St, Fort Stockton TX 79735, I-10 Exit 259 — CAT 318 in own offerings; Open; 24h; (432) 336-3410; geo 30.905212, -102.885118. County slug `pecos`.
- **Love’s #542 Fort Stockton** — 2723 E US Highway 290, Fort Stockton TX 79735, I-10 Exit 261 — CAT Scales in amenities; Store Open 24-hours; RV dump; (432) 336-3622; geo 30.893377, -102.852146.
- **Pilot #1146 Pecos** — 2500 S Bickley Ave, Pecos TX 79772, I-20 Exit 39 — CAT 318 in own offerings; Open; 24h; (432) 445-0002; geo 31.400866, -103.520955. County slug `reeves`.
- **Flying J #736 Pecos** — 100 E Pinehurst St, Pecos TX 79772, I-20 Exit 42 — CAT 318 in own offerings; Open; 24h; (432) 294-6626; geo 31.401153, -103.485879.
- **Love’s #492 Pecos** — 5202 S Cedar St, Pecos TX 79772, I-20 Exit 42 — CAT Scales in amenities; Store Open 24-hours; RV dump; (432) 445-1490; geo 31.399839, -103.479374.
- Checked, no CAT: Love’s #256 Van Horn (I-10 Exit 140B). Xpress Fuel #1349 Van Horn lists no CAT on Pilot’s city index.
- Seen in a third-party fuel-stop list (not a source for listings), not yet own-page checked: Pilot #1134 Orla (US-285 & RM 652), Pilot #1227 Pyote (I-20 Exit 66), Pilot #1205 / #1207 Monahans — candidates for a Monahans / Odessa page with Love’s #339 Odessa (I-20 Exit 115) and TA Big Spring.

Wiring: new `van_horn_fort_stockton_pecos_body()` + `write()` in `build.py`, NAV (`vfp`), footer, 404 lede hub list, PPM guide Texas line, El Paso + Amarillo + other Related lists, `tools/seo.py` PLACES (region "Texas"), ADDING_A_PAGE county table. `CHECKED_HUMAN` → 3 Nov 2026.

Previous ship (2 Nov): `/amarillo/` — Love’s #250, Love’s #200, TA #0055, Petro #0307, Pilot #436, Flying J #723.

## Previous ship detail (2 Nov)

**Amarillo** (`/amarillo/`): second Texas page (Potter County; all six geocode to Potter via the Census geocoder). All six verified tonight (2 Nov) on operators’ own pages.

- **Love’s #250 Amarillo (west)** — 14701 I-40 W, Amarillo TX 79124, I-40 Exit 60 — CAT Scales in amenities; Store Open 24-Hours; RV hookup/dump; (806) 358-2551; geo 35.187837, -102.011289.
- **Love’s #200 Amarillo (east)** — 6930 I-40 E, Amarillo TX 79120, I-40 Exit 74 / Whitaker Rd — CAT Scales in amenities; Store + Truck Care Open 24-hours; (806) 373-7775; geo 35.191927, -101.760945.
- **TA Amarillo #0055** — 7000 E Interstate 40, Amarillo TX 79118, I-40 Exit 74 — CAT Scale under Other Amenities; fuel 24/7 only, no store-hours statement; (806) 342-3080; geo 35.1915, -101.7589.
- **Petro Amarillo #0307** — 8500 E I-40 at Lakeside Dr, Amarillo TX 79118, I-40 Exit 75 — CAT Scale under Other Amenities; fuel 24/7 only, no store-hours statement; (806) 372-4899; geo 35.1917, -101.7437.
- **Pilot #436 Amarillo** — 715 S Lakeside Dr, Amarillo TX 79118, I-40 Exit 75 — CAT (offering 318) in the store’s own offerings array (the Southern Tire Mart sub-listing at the same address has no CAT — ignore it); status Open; is24Hours true; (806) 335-3323; geo 35.195618, -101.741115.
- **Flying J #723 Amarillo** — 9601 E I-40, Amarillo TX 79118, I-40 Exit 76 — CAT (offering 318) in own offerings; status Open; is24Hours true; (806) 335-1475; geo 35.194246, -101.723823.
- Checked, no CAT: Love’s #261 Amarillo (I-27 Exit 115/116, Canyon Dr), Love’s #229 Claude (I-40 Exit 96). Love’s station-code list files Store 721 under Amarillo, but its own page is Alma TX (I-45) — ignore.
- Pilot’s nearby data shows Pilot 6555 US-385 (Vega area, I-40 / US-385, CAT 318) — candidate to extend `/amarillo/` west after an own-page check.

Wiring: new `amarillo_body()` + `write()` in `build.py`, NAV (`ama`), footer, 404 lede hub list, PPM guide Texas line, El Paso + Tucumcari Related, `tools/seo.py` PLACES (region "Texas"), ADDING_A_PAGE county table. `CHECKED_HUMAN` → 2 Nov 2026.

Previous ship (1 Nov): `/el-paso-santa-teresa/` — Love’s #817, Love’s #447, Pilot #435, Flying J #728, Petro El Paso.

## Previous ship detail (1 Nov)

**El Paso / Anthony / Santa Teresa** (`/el-paso-santa-teresa/`): first Texas page (El Paso County TX, plus Santa Teresa in Doña Ana County NM). All five verified tonight (1 Nov) on operators’ own pages.

- **Love’s #817 Santa Teresa** — 2401 Airport Rd, Santa Teresa NM 88008, NM-136 at Airport Road — CAT Scales in amenities; Store Open 24-Hours; (575) 619-6090; geo 31.862229, -106.687231. County slug `dona-ana`.
- **Love’s #447 Anthony TX** — 3000 Mountain Pass Blvd, Anthony TX 79821, I-10 Exit 0 — CAT Scales in amenities; Store Open 24-hours; (915) 886-3915; geo 31.997879, -106.581219. County slug `el-paso`.
- **Pilot #435 Anthony TX** — 2015 Antonio St, Anthony TX 79821, I-10 Exit 0 — CAT (offering 318) in the store’s own offerings array; Open 24 Hours; status Open; phone left blank (Pilot shows only toll-free (833) 260-7867); geo 31.9965, -106.5862.
- **Flying J #728 El Paso** — 1301 Horizon Blvd, El Paso TX 79928, I-10 Exit 37 — CAT (offering 318) in the store’s own offerings array; Open 24 Hours; (915) 852-4141; geo 31.6620526, -106.2380879.
- **Petro El Paso** — 1295 Horizon Blvd, El Paso TX 79927, I-10 Exit 37 — CAT Scale in amenities; fuel 24/7 only, no store-hours statement; (915) 790-4529; geo 31.6609, -106.2424. TA page shows no store number.
- Held: **Flying J #724 Anthony TX** (3001 Mountain Pass Blvd, I-10 Exit 0) lists CAT but Pilot’s data marks it "Temporarily Closed". Add when it reopens.

Wiring: new `el_paso_santa_teresa_body()` + `write()` in `build.py`, NAV (`eps`), footer, 404 lede hub list, PPM guide (new Texas line), Las Cruces Related, `tools/seo.py` PLACES (region "Texas"), ADDING_A_PAGE county table. `CHECKED_HUMAN` → 1 Nov 2026.


## Previous ship detail (31 Oct)

**Clovis / Hobbs / Eunice** (`/clovis-hobbs-eunice/`): seventh New Mexico page, first in eastern NM off the interstates (Curry and Lea Counties, Texas line). All three verified tonight (31 Oct) on operators’ own pages.

- **Love’s #329 Clovis** — 4700 Mabry Dr., Clovis NM 88101, US-60 at the County Road G exit — CAT Scales in amenities; Store Open 24-hours; (575) 762-2966; geo 34.394791, -103.144305. County slug `curry`.
- **Pilot #557 Hobbs** — 3710 W Carlsbad Hwy, Hobbs NM 88240, US-62 / US-180 — CAT Scale (offering code 318) in the store’s own offerings list on Pilot’s page (the visible "Services" text with CAT on that page belongs to nearby TX stores, so check the store’s own offerings array); Open 24 Hours; (575) 391-0120; geo 32.697805, -103.183759. County slug `lea`.
- **Love’s #760 Eunice** — 16 Andrews Hwy, Eunice NM 88231, NM-18 at the Hwy 234 / Andrews exit — CAT Scales in amenities; Store Open 24-Hours; RV hookups / dump; (575) 394-0015; geo 32.434398, -103.121134. County slug `lea`. Love’s all-locations list still files #760 under Clovis; its own page says Eunice.
- Found while checking (not on site yet): Love’s #614 Albuquerque (I-40 Exit 149) and Love’s #963 Albuquerque (I-25 Exit 221 / Sunport) both list CAT Scales — candidates to extend `/albuquerque/`. Love’s #257 Milan (I-40 Exit 79) lists CAT — candidate for `/gallup-milan/`. Love’s #817 Santa Teresa (NM-136) lists CAT — candidate for `/las-cruces-deming-lordsburg/` or a Santa Teresa / El Paso page. Love’s #210 Albuquerque (Exit 158) has no CAT.

Wiring: new `clovis_hobbs_eunice_body()` + `write()` in `build.py`, NAV (`che`), footer, 404 lede hub list, PPM guide New Mexico line, Tucumcari Related, `tools/seo.py` PLACES, ADDING_A_PAGE county table. `CHECKED_HUMAN` → 31 Oct 2026. stations.json 246 rows.

Previous ship (30 Oct): `/belen-truth-or-consequences/` — Love’s #726 Belen, Love’s #1045 Truth or Consequences.

## Sources used (this compile)

- Far West Texas stops (3 Nov): https://pilotcompany.com/locations/us/tx/van-horn/501-van-horn-dr · https://pilotcompany.com/locations/us/tx/fort-stockton/2571-n-front-st · https://www.loves.com/locations/tx/fort-stockton/loves-travel-stop-fort-stockton-542 · https://pilotcompany.com/locations/us/tx/pecos/2500-s-bickley-ave · https://pilotcompany.com/locations/us/tx/pecos/100-e-pinehurst-st · https://www.loves.com/locations/tx/pecos/loves-travel-stop-pecos-492 · no CAT: loves-travel-stop-van-horn-256 · county check: geocoding.geo.census.gov · Love’s TX state index returns HTTP 500 (store pages OK); Pilot city indexes at locations.pilotflyingj.com/us/tx/<city> work
- Amarillo stops (2 Nov): https://www.loves.com/locations/tx/amarillo/loves-travel-stop-amarillo-250 · https://www.loves.com/locations/tx/amarillo/loves-travel-stop-amarillo-200 · https://www.ta-petro.com/location/tx/ta-amarillo/ · https://www.ta-petro.com/location/tx/petro-amarillo/ · https://pilotcompany.com/locations/us/tx/amarillo/715-s-lakeside-dr · https://pilotcompany.com/locations/us/tx/amarillo/9601-e-i-40 · no CAT: loves-travel-stop-amarillo-261, loves-travel-stop-claude-229 · county check: geocoding.geo.census.gov
- El Paso stops (1 Nov): https://www.loves.com/locations/nm/santa-teresa/loves-travel-stop-santa-teresa-817 · https://www.loves.com/locations/tx/anthony/loves-travel-stop-anthony-447 · https://pilotcompany.com/locations/us/tx/anthony/2015-antonio-st · https://pilotcompany.com/locations/us/tx/el-paso/1301-horizon-blvd · https://www.ta-petro.com/location/tx/petro-el-paso/ · held: https://pilotcompany.com/locations/us/tx/anthony/3001-mountain-pass-blvd
- Love’s #329 Clovis: https://www.loves.com/locations/nm/clovis/loves-travel-stop-clovis-329
- Pilot #557 Hobbs: https://locations.pilotflyingj.com/us/nm/hobbs/3710-w-carlsbad-hwy (redirects to pilotcompany.com/locations/us/nm/hobbs/3710-w-carlsbad-hwy)
- Love’s #760 Eunice: https://www.loves.com/locations/nm/eunice/loves-travel-stop-eunice-760
- Love’s #614 / #963 Albuquerque, #257 Milan, #817 Santa Teresa (CAT, held for extensions); #210 Albuquerque (no CAT): loves.com/locations/nm/... store pages
- TA NM index (no eastern NM TA): https://www.ta-petro.com/location/nm/

## Gaps / deferred

- Van Horn / Fort Stockton / Pecos: shipped 3 Nov; no dedicated house; CAT staffing hours unpublished; livestock unknown; Sierra Blanca, Fort Hancock, Balmorhea, Monahans, Pyote, Orla, Kermit unchecked. Next Texas: Monahans / Odessa / Midland / Big Spring on I-20 (Pilot #1205/#1207/#1227, Love’s #339, TA Big Spring own-page checks), Pilot Vega + Dumas/Dalhart for the Panhandle, Flying J #724 Anthony if it reopens
- Amarillo: shipped 2 Nov; no dedicated house; CAT staffing hours unpublished; TA #0055 / Petro #0307 store hours unpublished; Canyon, Vega (Pilot 6555 US-385 candidate), Hereford, Dumas (Love’s #626), Vega, Dalhart (Love’s #836) unchecked. Still pending: Love’s #614 + #963 extend `/albuquerque/`, Love’s #257 extends `/gallup-milan/`; Van Horn / Pecos / Fort Stockton (Love’s #542) for more I-10 Texas
- El Paso / Anthony / Santa Teresa: shipped 1 Nov; no dedicated house; CAT staffing hours unpublished; Petro El Paso store hours unpublished; Flying J #724 Anthony temporarily closed (held); Clint / Fabens / Van Horn / Fort Hancock east on I-10 unchecked. Next: Love’s #614 + #963 extend `/albuquerque/`, Love’s #257 extends `/gallup-milan/`, then Van Horn / Pecos or Amarillo for more Texas pages
- Clovis / Hobbs / Eunice: shipped 31 Oct; no dedicated house; CAT staffing hours unpublished; Roswell, Artesia, Carlsbad, Portales, Lovington own-page CAT not verified (no TA in eastern NM; Pilot Roswell/Carlsbad not searched). Next NM: add Love’s #614 + #963 to Albuquerque, Love’s #257 to Gallup / Milan, Love’s #817 Santa Teresa to Las Cruces
- Belen / Truth or Consequences I-25: shipped 30 Oct; no dedicated house; CAT staffing hours unpublished; Los Lunas and Socorro own pages not checked; Pilot/TA have no verified central-I-25 NM CAT. I-25 north (Springer / Raton / Santa Fe) needs a second CAT stop beside TA Springer; Love’s Clovis #329 / Eunice #760 shipped 31 Oct on /clovis-hobbs-eunice/
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
- 2026-11-04 — `/guides/uhaul-truck-weight/` How much does a U-Haul truck weigh? Empty weight, max load and GVWR for pickup, cargo van, 10/15/20/26 ft (U-Haul equipment pages read 4 Nov 2026), PPM certified-ticket rule (DFAS, Military OneSource), CAT FAQ Q12/Q22 price + 2,000–200,000 lb range, FMCSA 26,001 lb Class B line. Original queue exhausted, Search Console queries not available to the bot, so topic picked for PPM/mover intent. Linked from home hub, footer nav, all regional Related lists, PPM/CAT/tongue guides.
- Queue next: how to weigh an RV (axle/corner, GVWR) → horse/travel trailer + tongue weight → weigh stations vs public scales → GSC queries.
