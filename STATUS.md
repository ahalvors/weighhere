# WeighHere status — 14 Oct 2026

Compiled evening PT 14 Oct 2026 (nightly ship).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **198** | +2 Love’s Magic Valley I-84 CAT, +1 Love’s Idaho Falls CAT |
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
| McCammon / Idaho Falls / I-15 | 3 | +1 Love’s #478 Idaho Falls (I-15 Exit 113) |
| Boise / Treasure Valley / I-84 | 5 | unchanged (now links east to Twin Falls / Burley) |
| **Twin Falls / Burley / I-84** | **3** | **new page** — Love’s #812 Bliss, Flying J #640 Jerome (shared with Boise page), Love’s #334 Heyburn |
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
| CAT / truck-stop cards | 134 | +3 Love’s Idaho (Bliss, Heyburn, Idaho Falls) |
| Enforcement do-not-go | 2 | unchanged |

## What shipped tonight

**Twin Falls / Burley / I-84** (`/twin-falls-burley/`): Idaho’s Magic Valley, east of last night’s Boise / Treasure Valley page. Love’s Idaho store pages loaded again tonight (the state index still returns HTTP 500, but the store pages return 200), so both Love’s CAT stops on this stretch were verified on Love’s *own* pages (amenities list CAT Scales).

- **Love’s Travel Stop #812 Bliss** — 680 US Hwy 30, Bliss ID 83314, I-84 Exit 141 / US-30 (Gooding County) — store Open 24-hours; (208) 536-7083; geo 42.924687, -114.940688. Love’s 2020 newsroom post for the Bliss opening also lists a CAT scale.
- **Flying J #640 Jerome** — existing row (I-84 Exit 173, US-93 to Twin Falls), now shown on both the Boise and Twin Falls pages.
- **Love’s Travel Stop #334 Heyburn** — 260 Centennial Dr., Heyburn ID 83336, I-84 Exit 211 / US-30 (Minidoka County, Burley / Rupert) — store Open 24-Hours; (208) 434-8777; geo 42.564532, -113.740836

Bonus row: **Love’s Travel Stop #478 Idaho Falls** — 6737 South 45th West, Idaho Falls ID 83402, I-15 Exit 113 (Bonneville County) — store Open 24-hours; (208) 529-1904; geo 43.436962, -112.119846. Added to `/mccammon-idaho-falls/` (now 3 stops; two at Exit 113).

Cross-links added from Boise, McCammon and every page that already linked to Boise (Related), nav, footer, 404 lede, about-page Utah/Idaho line, homepage hub (Idaho group via `tools/seo.py`), and sitemap. Hours are store-listed 24h, not CAT staffing. Livestock unknown. No dedicated house verified.

### Candidates checked but not shipped tonight

- **Twin Falls city CAT** (third-party lists show one at 3204 Kimberly Rd; a third-party site claims a "Pilot #392 Twin Falls"): no operator own page found (no Pilot Twin Falls store page turned up) — held.
- **Jerome Exit 165 / 168, Eden Exit 182**: third-party trucker lists show CAT scales; operators not identified on own pages — held.
- **Love’s #301 Post Falls** (I-90 Exit 2): own page lists CAT Scales, but it is a lone north-Idaho stop — held for a future Spokane / Coeur d’Alene / I-90 page once a Washington stop verifies.
- **Pilot Flying J site moved**: `locations.pilotflyingj.com` now 301s to `pilotcompany.com/locations/...`; store pages still resolve, state index pages 404. Existing source URLs still work via redirect.
- Prior holds unchanged: ONE9 #777 Boise / #1426 Nampa / #1429 Fruitland, TA Express Dubois #0940 (no CAT), Flying J #748 Willard, #774 Snowville, Tremonton, Carson City, Temecula / Corona, Redding, Beaver-gap stops, Love’s Fernley / Winnemucca / Carlin.

## Sources used (this compile)

- Love’s #812 Bliss: https://www.loves.com/locations/id/bliss/loves-travel-stop-bliss-812
- Love’s #334 Heyburn: https://www.loves.com/locations/id/heyburn/loves-travel-stop-heyburn-334
- Love’s #478 Idaho Falls: https://www.loves.com/locations/id/idaho-falls/loves-travel-stop-idaho-falls-478
- Love’s #301 Post Falls (checked, held): https://www.loves.com/locations/id/post-falls/loves-travel-stop-post-falls-301
- Love’s newsroom, Bliss opening (Dec 2020): https://www.loves.com/news/2020/december/loves-travel-stops-opens-four-new-locations-largest-location-ever-opens-in-idaho
- Flying J #640 Jerome: https://locations.pilotflyingj.com/us/id/jerome/5350-us-93 (redirects to pilotcompany.com)
- TA Petro Idaho index (only Boise + Dubois): https://www.ta-petro.com/location/id/
- CAT Scale locator (linked, not republished): https://catscale.com/cat-scale-locator/
- ScaleRegistry public-weighing list: https://scaleregistry.com/public-scales.html

## Gaps / deferred

- Twin Falls city CAT (Kimberly Rd) — no operator own page yet
- Spokane / Coeur d’Alene / I-90 — Love’s #301 Post Falls verified; need a Washington stop to make a page
- ONE9 #777 Boise, #1426 Nampa, #1429 Fruitland — hold until amenities list CAT Scale
- Love’s Idaho state index still HTTP 500 (store pages OK)
- Pocatello proper / Blackfoot — no own-page CAT stop found
- Flying J #748 Willard and Flying J #774 Snowville — FAQ-yes / amenities-omit CAT (held)
- Tremonton — no Love’s/Pilot/TA own-page CAT verified
- Mesquite / Beaver Dam gap: Flying J Dealer #1171 Mesquite still omits CAT from amenities
- Flying J Dealer #509 Beaver amenities omit CAT — gap between Parowan and Fillmore
- Carson City / US-395 / Truckee: no Pilot/Love’s/TA/Flying J/Petro own-page CAT yet (Maverik third-party only)
- Temecula / Corona / Murrieta: Pilot Perris #1458 alone — need a second own-page CAT before `/temecula-corona/`
- Redding / Anderson mid-north I-5: only TA Redding #0057 — need a second stop before `/redding-anderson/`
- Next candidates: Spokane / Post Falls / I-90 (if a WA own-page CAT verifies), Ontario OR / I-84 west of Fruitland, Temecula / Corona (if a second CAT verifies), Carson City if a chain own-page CAT appears, Redding / Anderson second stop, Snowville / Willard if amenities catch up, ONE9 Boise/Nampa/Fruitland if amenities catch up, Ventura / Santa Barbara CDFA re-pull, Beaver if amenities catch up, Love’s Fernley / Winnemucca / Carlin as corridor extensions
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
