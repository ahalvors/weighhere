# WeighHere status — 13 Oct 2026

Compiled evening PT 13 Oct 2026 (nightly ship).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **195** | +5 Boise / Treasure Valley / I-84 CAT |
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
| McCammon / Idaho Falls / I-15 | 2 | unchanged (now links west to Treasure Valley) |
| **Boise / Treasure Valley / I-84** | **5** | **new page** — ONE9 #1428 Caldwell, Flying J #638 Caldwell, TA #0167 Boise, Pilot #350 Mountain Home, Flying J #640 Jerome |
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
| CAT / truck-stop cards | 131 | +5 Boise / Treasure Valley / I-84 |
| Enforcement do-not-go | 2 | unchanged |

## What shipped tonight

**Boise / Treasure Valley / I-84** (`/boise-treasure-valley/`): southwestern Idaho I-84 corridor, west of last night’s McCammon / Idaho Falls I-15 page. Five CAT Scales verified tonight on the operators’ *own* location pages (amenities list CAT Scale; Flying J / Pilot FAQ also yes where present).

- **ONE9 Dealer #1428 Caldwell** — 122 W Simplot Blvd, Caldwell ID 83605, I-84 business loop at W Simplot Blvd (Canyon County) — Open 24 Hours; (208) 459-0027; geo 43.6699588, -116.6997722
- **Flying J Travel Center #638 Caldwell** — 3512 Franklin Rd, Caldwell ID 83605, I-84 Exit 29 (Canyon County) — Open 24 Hours; (208) 453-9225; geo 43.6616509, -116.6546368
- **TA Boise #0167** — 4115 Broadway Ave, Boise ID 83705, I-84 Exit 54 (Ada County) — (208) 344-1091; geo 43.5656, -116.1994
- **Pilot Travel Center #350 Mountain Home** — 1050 US-20, Mountain Home ID 83647, I-84/US-20 Exit 95 (Elmore County) — Open 24 Hours; (208) 587-4465; geo 43.14257813, -115.6629562
- **Flying J Travel Center #640 Jerome** — 5350 US-93, Jerome ID 83338, I-84 Exit 173 (Jerome County) — Open 24 Hours; (208) 324-3454; geo 42.6495296, -114.4429066

Cross-links added from McCammon / Idaho Falls and other pages that already linked to McCammon (Related), nav, footer, 404 lede, homepage hub (Idaho group via `tools/seo.py`), and sitemap. Hours shown are store-listed 24h where published, not CAT staffing. Livestock unknown. No dedicated house verified.

### Candidates checked but not shipped tonight

- **ONE9 Dealer #777 Boise** (3353 Federal Way, I-84 Exit 54): own page amenities list omits CAT Scale (CAT appears only in opaque JSON / services text dump) — held (same rule as Willard / Snowville).
- **ONE9 Dealer #1426 Nampa** (612 Northside Blvd): no visible Amenities card on own page tonight — held.
- **ONE9 Dealer #1429 Fruitland** (2001 Hwy 30 W): no visible Amenities card on own page tonight — held.
- **Love’s Idaho**: loves.com Idaho locations still HTTP 500; no Love’s Idaho own page verified.
- Prior holds unchanged: TA Express Dubois #0940 (no CAT), Flying J #748 Willard, #774 Snowville (FAQ-yes / amenities-omit), Tremonton, Carson City, Temecula / Corona, Redding, Beaver-gap stops, Love’s Fernley / Winnemucca / Carlin.

## Sources used (this compile)

- ONE9 #1428 Caldwell: https://locations.pilotflyingj.com/us/id/caldwell/122-w-simplot-blvd
- Flying J #638 Caldwell: https://locations.pilotflyingj.com/us/id/caldwell/3512-franklin-rd
- TA Boise #0167: https://www.ta-petro.com/location/id/ta-boise/
- Pilot #350 Mountain Home: https://locations.pilotflyingj.com/us/id/mountain-home/1050-us-20
- Flying J #640 Jerome: https://locations.pilotflyingj.com/us/id/jerome/5350-us-93
- ONE9 #777 Boise (checked, amenities omit CAT): https://locations.pilotflyingj.com/us/id/boise/3353-federal-way
- ONE9 #1426 Nampa (checked, no amenities card): https://locations.pilotflyingj.com/us/id/nampa/612-northside-blvd
- ONE9 #1429 Fruitland (checked, no amenities card): https://locations.pilotflyingj.com/us/id/fruitland/2001-hwy-30-w
- Pilot Flying J Idaho index: https://locations.pilotflyingj.com/us/id
- TA Petro Idaho index: https://www.ta-petro.com/location/id/
- CAT Scale locator (linked, not republished): https://catscale.com/cat-scale-locator/
- ScaleRegistry public-weighing list: https://scaleregistry.com/public-scales.html

## Gaps / deferred

- Twin Falls / Burley / I-84 east of Jerome — next Idaho corridor candidate if a second own-page CAT verifies near Twin Falls
- ONE9 #777 Boise, #1426 Nampa, #1429 Fruitland — hold until amenities list CAT Scale
- Love’s Idaho pages unreachable (HTTP 500)
- Pocatello proper / Blackfoot — no own-page CAT stop found
- Flying J #748 Willard and Flying J #774 Snowville — FAQ-yes / amenities-omit CAT (held)
- Tremonton — no Love’s/Pilot/TA own-page CAT verified
- Mesquite / Beaver Dam gap: Flying J Dealer #1171 Mesquite still omits CAT from amenities
- Flying J Dealer #509 Beaver amenities omit CAT — gap between Parowan and Fillmore
- Carson City / US-395 / Truckee: no Pilot/Love’s/TA/Flying J/Petro own-page CAT yet (Maverik third-party only)
- Temecula / Corona / Murrieta: Pilot Perris #1458 alone — need a second own-page CAT before `/temecula-corona/`
- Redding / Anderson mid-north I-5: only TA Redding #0057 — need a second stop before `/redding-anderson/`
- Next candidates: Twin Falls / Burley (if own-page CAT cluster), Temecula / Corona (if a second CAT verifies), Carson City if a chain own-page CAT appears, Redding / Anderson second stop, Snowville / Willard if amenities catch up, ONE9 Boise/Nampa/Fruitland if amenities catch up, Ventura / Santa Barbara CDFA re-pull, Beaver if amenities catch up, Love’s Fernley / Winnemucca / Carlin as corridor extensions
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
