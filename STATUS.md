# WeighHere status — 22 Oct 2026

Compiled evening PT 22 Oct 2026 (nightly ship).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **218** | +2 US-97 central Oregon CAT (Love’s #795 Madras, Love’s #823 Klamath Falls) |
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
| **Madras / Klamath Falls / US-97 (OR)** | **2** | **new page 22 Oct** — Love’s #795 Madras (Hall Rd exit), Love’s #823 Klamath Falls (Dan O’Brien Way exit) |
| CAT / truck-stop cards | 154 | +2 Madras / Klamath Falls |
| Enforcement do-not-go | 2 | unchanged |

## What shipped tonight

**Madras / Klamath Falls / US-97** (`/madras-klamath-falls/`): fourth Oregon page, first in central Oregon. Both stops verified tonight (22 Oct) on Love’s own location pages.

- **Love’s Travel Stop #795 Madras** — 1678 SE Highway 97, Madras OR 97741, US-97 / US-26 Hall Rd exit (Jefferson County) — CAT Scales in amenities; store Open 24-Hours (Arby’s 7 a.m.–10 p.m.); RV-friendly parking, RV dump, bulk propane, propane tank exchange; (541) 675-6008; geo 44.61226, -121.137633.
- **Love’s Travel Stop #823 Klamath Falls** — 250 Dan O’Brien Way, Klamath Falls OR 97601, US-97 Dan O’Brien Way exit (Klamath County) — CAT Scales; store Open 24-Hours; RV-friendly parking, RV dump, bulk propane; (541) 363-4499; geo 42.258046, -121.799445.

Wiring: new `madras_klamath_falls_us97_body()` + `write()` in `build.py`, NAV (`mkf`), footer, 404 lede hub list, PPM guide + CAT cost guide Oregon lines, Eugene and Ontario pages Related links to it, `tools/seo.py` PLACES (`"madras-klamath-falls": ("Madras & Klamath Falls, OR", "Oregon")`), ADDING_A_PAGE county-slug list (`jefferson` / `klamath`). `CHECKED_HUMAN` → 22 Oct 2026. Livestock unknown; CAT staffing hours unpublished (store hours only); no dedicated house verified (ScaleRegistry lists none in Oregon). No Bend / Redmond CAT verified. Love’s #650 Boardman (I-84 Exit 159) re-checked tonight: CAT Scales + store/Truck Care Open 24-hours, (541) 481-2934 — still lonely, held for a Boardman / Pendleton / Hermiston page.

Previous ship (21 Oct): `/ontario-baker-city/` — Love’s #372 Ontario (I-84 Exit 374) + Love’s #569 Baker City (I-84 Exit 304).

## Sources used (this compile)

- Love’s #795 Madras: https://www.loves.com/locations/or/madras/loves-travel-stop-madras-795
- Love’s #823 Klamath Falls: https://www.loves.com/locations/or/klamath-falls/loves-travel-stop-klamath-falls-823
- Love’s #650 Boardman (held): https://www.loves.com/locations/or/boardman/loves-travel-stop-boardman-650

Prior compile (21 Oct):

- Love’s #372 Ontario: https://www.loves.com/locations/or/ontario/loves-travel-stop-ontario-372
- Love’s #569 Baker City: https://www.loves.com/locations/or/baker-city/loves-travel-stop-baker-city-569

## Gaps / deferred

- Madras / Klamath Falls US-97: shipped 22 Oct; no dedicated house; CAT staffing hours unpublished; no Bend / Redmond CAT verified; Pilot / Flying J / TA Petro US-97 own pages not searched
- Love’s #650 Boardman (I-84 Exit 159): CAT + 24h re-verified 22 Oct — lonely; need Pendleton / Hermiston / La Grande own-page CAT partner
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
- Next candidates: Boardman OR I-84 (Love’s #650 CAT) with a Pendleton/Hermiston partner, Medford / Phoenix OR on I-5 if a partner appears, Blaine if a second north-I-5 CAT appears, Temecula / Corona (if a second CAT verifies), Carson City if a chain own-page CAT appears, Redding / Anderson second stop, Snowville / Willard if amenities catch up, ONE9 Boise/Nampa/Fruitland if amenities catch up, Ventura / Santa Barbara CDFA re-pull, Beaver if amenities catch up, Love’s Fernley / Winnemucca / Carlin as corridor extensions
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
