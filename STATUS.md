# WeighHere status — 12 Oct 2026

Compiled evening PT 12 Oct 2026 (nightly ship).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **190** | +2 McCammon / Idaho Falls / I-15 CAT (Flying J #641, Flying J #1043) — first Idaho rows |
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
| Brigham / Ogden / I-15 | 3 | unchanged (now links north to Idaho) |
| **McCammon / Idaho Falls / I-15** | **2** | **new page** — Flying J #641 McCammon, Flying J #1043 Idaho Falls |
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
| CAT / truck-stop cards | 126 | +2 McCammon / Idaho Falls / I-15 |
| Enforcement do-not-go | 2 | unchanged |

## What shipped tonight

**McCammon / Idaho Falls / I-15** (`/mccammon-idaho-falls/`): first Idaho page, continuing I-15 north from `/brigham-ogden/`. Two CAT Scales verified tonight on Flying J’s *own* location pages (amenities list CAT Scale and FAQ answers yes).

- **Flying J Travel Center #641 McCammon** — 587 E US-30, McCammon ID 83250, I-15 Exit 47 (Bannock County) — Open 24 Hours; (208) 845-0866; geo 42.6599760, -112.2066968
- **Flying J Travel Center #1043 Idaho Falls** — 6485 W Overland Dr, Idaho Falls ID 83402, I-15 Exit 113 (Bonneville County) — Open 24 Hours; (208) 522-4149; geo 43.4395888, -112.1153279

Cross-links added from Brigham / Ogden (lede + Related), Springville / Salt Lake, Fillmore / Nephi, St. George / Cedar City, Las Vegas and I-15 / High Desert Related lists, nav, footer, 404 lede, homepage hub (new Idaho group via `tools/seo.py` STATE_NAMES), and sitemap. Hours shown are store-listed 24h, not CAT staffing. Livestock unknown. No dedicated house verified.

### Candidates checked but not shipped tonight

- **TA Express Dubois #0940** (I-15 Exit 137): own TA page lists no CAT Scale — not included.
- **Love’s Idaho**: loves.com state locations page returned HTTP 500 tonight; no Love’s Idaho own page verified.
- **Pocatello proper / Blackfoot**: no Pilot/Flying J/TA own-page location in Pilot’s Idaho list.
- **Boise / Treasure Valley (next candidate)**: Pilot’s Idaho list shows ONE9 Dealer #777 Boise (3353 Federal Way), ONE9 Dealer #1426 Nampa, ONE9 Dealer #1428 Caldwell, ONE9 Dealer #1429 Fruitland, Pilot #350 Mountain Home, Flying J #640 Jerome — all show CAT Scale in their own-page amenities on a first pass tonight; not yet shipped (need exits/addresses/geo recorded). TA Boise also exists (not checked).
- Prior holds unchanged: Flying J #748 Willard, #774 Snowville (FAQ-yes / amenities-omit), Tremonton, Carson City, Temecula / Corona, Redding, Beaver-gap stops, Love’s Fernley / Winnemucca / Carlin.

## Sources used (this compile)

- Flying J #641 McCammon: https://locations.pilotflyingj.com/us/id/mccammon/587-e-us-30
- Flying J #1043 Idaho Falls: https://locations.pilotflyingj.com/us/id/idaho-falls/6485-w-overland-dr
- TA Express Dubois #0940 (checked, no CAT listed): https://www.ta-petro.com/location/id/ta-express-dubois/
- Pilot Flying J Idaho index: https://locations.pilotflyingj.com/us/id
- CAT Scale locator (linked, not republished): https://catscale.com/cat-scale-locator/
- ScaleRegistry public-weighing list: https://scaleregistry.com/public-scales.html

## Gaps / deferred

- Boise / Treasure Valley / Mountain Home / Jerome (Idaho I-84) — strong next candidate (6 Pilot-family own pages show CAT Scale)
- Pocatello proper / Blackfoot — no own-page CAT stop found; Love’s Idaho pages unreachable tonight (HTTP 500)
- Flying J #748 Willard and Flying J #774 Snowville — FAQ-yes / amenities-omit CAT (held)
- Tremonton — no Love’s/Pilot/TA own-page CAT verified tonight
- Mesquite / Beaver Dam gap: Flying J Dealer #1171 Mesquite still omits CAT from amenities
- Flying J Dealer #509 Beaver amenities omit CAT — gap between Parowan and Fillmore
- Carson City / US-395 / Truckee: no Pilot/Love’s/TA/Flying J/Petro own-page CAT yet (Maverik third-party only)
- Temecula / Corona / Murrieta: Pilot Perris #1458 alone — need a second own-page CAT before `/temecula-corona/`
- Redding / Anderson mid-north I-5: only TA Redding #0057 — need a second stop before `/redding-anderson/`
- Next candidates: Temecula / Corona (if a second CAT verifies), Carson City if a chain own-page CAT appears, Redding / Anderson second stop, Snowville / Willard if amenities catch up, Ventura / Santa Barbara CDFA re-pull, Beaver if amenities catch up, Love’s Fernley / Winnemucca / Carlin as corridor extensions
- Elko / Winnemucca held: Flying J #692 Wells and Pilot #147 West Wendover (FAQ yes, amenities omit CAT)
- Las Vegas omitted ONE9s still amenities-omit CAT
- ONE9 #1424 Westley — visible amenities card still empty
- EZ Trip #1275 Madera Ave 12 — visible amenities still omit CAT
- Hours / fees / livestock unknown beyond store-listed fuel 24/7 vs CAT staffing
- Ventura / Santa Barbara remain thin
- CDFA Merced / Kern / Shasta / Tehama / Glenn / Fresno / Ventura / Santa Barbara / Sacramento facility grids still often WAF-blocked
