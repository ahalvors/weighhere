# WeighHere status — 20 Oct 2026

Compiled evening PT 20 Oct 2026 (nightly ship).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **214** | +3 I-5 Oregon CAT (Love’s #728 Albany, TA Coburg #0482, Love’s #312 Roseburg) |
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
| **Albany / Eugene / Roseburg / I-5** | **3** | **new page** — Love’s #728 Albany (I-5 Exit 238), TA Coburg #0482 (I-5 Exit 199), Love’s #312 Roseburg (I-5 Exit 119) |
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
| CAT / truck-stop cards | 150 | +3 Albany / Coburg / Roseburg |
| Enforcement do-not-go | 2 | unchanged |

## What shipped tonight

**Albany / Eugene / Roseburg / I-5** (`/eugene-albany-roseburg/`): second Oregon page. Unlocks TA Coburg, held since 15–19 Oct as “lonely”: Love’s `/api/fetch_stores` showed two Oregon I-5 Love’s with CAT Scales either side of it, and all three were re-verified tonight on the operators’ own pages.

- **Love’s Travel Stop #728 Albany** — 6457 Old Salem Rd NE, Albany OR 97321, I-5 Exit 238/Old Salem Rd (Linn County; Love’s API preferredName “Millersburg”) — CAT Scales in amenities; store, Truck Care and Arby’s Open 24-hours; RV-friendly parking, RV mechanical/tires, bulk propane + exchange; (541) 928-1900; geo 44.698743, -123.055073.
- **TA Coburg #0482** — 32910 E. Pearl St., Coburg OR 97408, I-5 Exit 199 (Lane County) — CAT Scale in TA amenities, page says Open 24 Hours (truck service 6 AM–10 PM listed separately); (541) 868-2880; geo 44.13637, -123.05737 (TA page JSON-LD).
- **Love’s Travel Stop #312 Roseburg** — 280 Grant Smith Rd, Roseburg OR 97471, I-5 Exit 119 (Douglas County) — CAT Scales; store, Truck Care, Arby’s Open 24-hours; RV mechanical/tires, RV dump, propane exchange; (541) 679-1916; geo 43.150503, -123.367895.
- Albany→Coburg ≈ 39 interstate miles (Exit 238→199); Coburg→Roseburg ≈ 80 (Exit 199→119).

Wiring: new `eugene_albany_roseburg_i5_body()` + `write()` in `build.py`, NAV (`ear`), footer, 404 lede, about-page line, Portland page links south to it (what-we-need note + Related), `tools/seo.py` PLACES (`"eugene-albany-roseburg": ("Eugene, Albany & Roseburg, OR", "Oregon")`), ADDING_A_PAGE county-slug list (`linn` / `lane` / `douglas`). `CHECKED_HUMAN` → 20 Oct 2026. Livestock unknown; CAT staffing hours unpublished (store hours only); no dedicated house verified (ScaleRegistry lists none in Oregon).

### Candidates held (last checked 16 Oct unless noted)

- **Petro Phoenix #0324** (I-5 Exit 24, Medford area; CAT + Open 24 Hours re-checked 19 Oct): still lonely — Love’s API shows no Love’s between Roseburg (Exit 119) and the CA line; Love’s #823 Klamath Falls (US-97, CAT) is ~75 mi away by OR-140 and not an I-5 corridor partner. Grants Pass / Medford Pilot / Flying J own pages not searched tonight.
- **Other Oregon Love’s with CAT in API (20 Oct)**: #650 Boardman (I-84 Exit 159), #795 Madras (US-97/26), #823 Klamath Falls (US-97), #372 Ontario, #569 Baker City. #902 Aurora (I-5 Exit 278) API does **not** flag CAT.

- **TA Grandview WA** (I-82 Exit 73): not re-checked tonight; last check TA own page amenities did **not** list CAT Scale — kept off `/pasco-prosser/`.
- **Cascades / I-90**: shipped 19 Oct (TA Seattle East + Love’s #413). Pilot / Flying J own-page CAT closer to Seattle not checked (Pilot state index still 404).
- **TA Coburg #0482**: shipped 20 Oct on `/eugene-albany-roseburg/`.
- **TA Express Blaine** (I-5 Exit 275): CAT Scale on TA own page — lonely; no second north-I-5 CAT cluster tonight.
- **Portland metro**: shipped 18 Oct. Pilot / Flying J own-page CAT in the metro (e.g. Wilsonville, Portland) not yet searched — candidate additions.
- **Ontario OR / I-84**: Love’s #372 Ontario (Exit 374) CAT-verified; TA Huntington still no CAT; Love’s #569 Baker City CAT-verified but farther west — held.
- **Love’s WA/OR state indexes**: still HTTP 500; store pages and `/api/fetch_stores` work.
- Prior holds unchanged: Twin Falls city CAT, Jerome 165/168, Eden 182, ONE9 #777 Boise / #1426 Nampa / #1429 Fruitland, TA Express Dubois #0940, Flying J #748 Willard, #774 Snowville, Tremonton, Carson City, Temecula / Corona, Redding, Beaver-gap stops, Love’s Fernley / Winnemucca / Carlin.

## Sources used (this compile)

- Love’s #728 Albany: https://www.loves.com/locations/or/albany/loves-travel-stop-albany-728
- TA Coburg #0482: https://www.ta-petro.com/location/or/ta-coburg/
- Love’s #312 Roseburg: https://www.loves.com/locations/or/roseburg/loves-travel-stop-roseburg-312
- Love’s store API (OR filter): https://www.loves.com/api/fetch_stores
- Petro Phoenix #0324 (held): https://www.ta-petro.com/location/or/petro-phoenix/
- CAT Scale locator (linked, not republished): https://catscale.com/cat-scale-locator/
- ScaleRegistry public-weighing list: https://scaleregistry.com/public-scales.html

## Gaps / deferred

- Cascades: shipped 19 Oct; TA Seattle East hours unpublished (no 24-hour statement on TA page)
- Tri-Cities: shipped 17 Oct with Love’s Pasco + Prosser; TA Grandview not listed (no CAT on TA page at last check); Kennewick / Richland own-page CAT not yet searched
- Portland: shipped 18 Oct (TA Troutdale, Love’s #449, TA Aurora); Pilot / Flying J metro stops not yet checked; no dedicated house; CAT staffing hours unpublished
- Eugene / I-5: shipped 20 Oct (Love’s #728 Albany, TA Coburg, Love’s #312 Roseburg); no dedicated house; CAT staffing hours unpublished; Pilot / Flying J Willamette Valley own pages not searched
- Petro Phoenix #0324 (Medford) still lonely — candidate for a Medford / Klamath or Grants Pass page if a second own-page CAT appears
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
- Next candidates: Ontario / Baker City OR I-84 (both Love’s CAT in API 20 Oct, ~70 mi), Boardman OR I-84 (Love’s #650 CAT) possibly with Pasco/Hermiston, Madras / Bend US-97, Medford / Phoenix OR on I-5 if a partner appears, Blaine if a second north-I-5 CAT appears, Ontario OR / Baker City I-84, Temecula / Corona (if a second CAT verifies), Carson City if a chain own-page CAT appears, Redding / Anderson second stop, Snowville / Willard if amenities catch up, ONE9 Boise/Nampa/Fruitland if amenities catch up, Ventura / Santa Barbara CDFA re-pull, Beaver if amenities catch up, Love’s Fernley / Winnemucca / Carlin as corridor extensions
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
