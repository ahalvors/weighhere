# WeighHere status — 8 Oct 2026

Compiled evening PT 8 Oct 2026 (nightly ship).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **178** | +3 St. George / Cedar City / Parowan / I-15 CAT (Pilot #775, Love’s #335, TA Express #0186) |
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
| **St. George / Cedar City / Parowan / I-15** | **3** | **new page** — Pilot #775 Saint George, Love’s #335 Cedar City, TA Express Parowan #0186 |
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
| CAT / truck-stop cards | 114 | +3 St. George / Cedar City / Parowan / I-15 |
| Enforcement do-not-go | 2 | unchanged |

## What shipped tonight

**St. George / Cedar City / Parowan / I-15** (`/st-george-cedar-city/`): new southwestern Utah page covering I-15 from St. George north through Cedar City to Parowan (Washington and Iron Counties UT), with three CAT Scales verified tonight on the operators’ *own* location pages. Continues northeast from `/las-vegas/` (Mesquite Flying J still held back).

- **Pilot Travel Center #775 Saint George** — 2841 S 60 E, Saint George UT 84790, I-15 Exit 4 — amenities list CAT Scale and FAQ answers yes; Open 24 Hours; (435) 319-4138; geo 37.0599477, -113.581869
- **Love’s Travel Stop #335 Cedar City** — 2645 N Canyon Ranch Dr, Cedar City UT 84720, I-15 Exit 62 — Love’s page lists CAT Scales; store and Truck Care open 24 hours; (435) 867-9888; geo 37.725785, -113.051367
- **TA Express Parowan #0186** — 1130 N. 100 W., Parowan UT 84761, I-15 Exit 78 — TA page lists CAT Scale (and RV Dump); gas/diesel 24/7; 435-477-3311; geo 37.8607, -112.8291

Cross-links added from Las Vegas and I-15 / High Desert Related lists, nav, footer, 404 lede, and sitemap. Hours shown are store-listed 24h, not CAT staffing. Livestock unknown. No dedicated house verified. Flying J #1171 Mesquite and Flying J #509 Beaver still omit CAT from amenities — held back.

## Sources used (this compile)

- Pilot #775 Saint George: https://locations.pilotflyingj.com/us/ut/saint-george/2841-s-60-e
- Love’s #335 Cedar City: https://www.loves.com/locations/ut/cedar-city/loves-travel-stop-cedar-city-335
- TA Express Parowan #0186: https://www.ta-petro.com/location/ut/ta-express-parowan/
- Re-check Flying J #1171 Mesquite (held): https://locations.pilotflyingj.com/us/nv/mesquite/1057-s.-lower-flat-top-drive
- Re-check Flying J Dealer #509 Beaver (held): https://locations.pilotflyingj.com/us/ut/beaver/653-w-1400-n
- CAT Scale locator (linked, not republished): https://catscale.com/cat-scale-locator/
- ScaleRegistry public-weighing list: https://scaleregistry.com/public-scales.html

## Gaps / deferred

- Mesquite / Beaver Dam gap: Flying J Dealer #1171 Mesquite (Exit 118) still omits CAT from amenities (re-checked 8 Oct 2026). No Love’s own-page CAT confirmed at Littlefield / Beaver Dam AZ or Hurricane UT. Corridor page starts at St. George Exit 4.
- Flying J Dealer #509 Beaver (I-15 Exit 112) amenities omit CAT — held back; north of Parowan, not on tonight’s page.
- Carson City / US-395 / Truckee: no own-page CAT yet; Reno Love’s northern NV still unchecked on Love’s own pages
- Temecula / Corona / Murrieta Love’s / Pilot / TA — still deferred pending own-page CAT
- Redding / Anderson mid-north I-5: only TA Redding #0057 own-page CAT — need a second stop before `/redding-anderson/`
- Next candidates: Carson City / US-395, Temecula / Corona, Redding / Anderson, Ventura / Santa Barbara CDFA re-pull, Beaver / Fillmore I-15 north of Parowan (if Flying J Beaver amenities catch up or another own-page CAT appears)
- Elko / Winnemucca held: Flying J #692 Wells and Pilot #147 West Wendover (FAQ yes, amenities omit CAT)
- Las Vegas omitted ONE9s (Jean / Cheyenne / Apex / Moapa / Searchlight) still amenities-omit CAT
- ONE9 #1424 Westley — visible amenities card still empty; CAT in JSON/description only
- EZ Trip #1275 Madera Ave 12 — visible amenities still omit CAT
- Hours / fees / livestock unknown beyond store-listed fuel 24/7 vs CAT staffing
- Ventura / Santa Barbara remain thin
- CDFA Merced / Kern / Shasta / Tehama / Glenn / Fresno / Ventura / Santa Barbara / Sacramento facility grids still often WAF-blocked
