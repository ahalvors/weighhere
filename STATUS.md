# WeighHere status — 15 Oct 2026

Compiled evening PT 15 Oct 2026 (nightly ship).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **202** | +3 Spokane-area WA CAT (Petro, 2× Broadway Flying J), +1 Love’s #301 Post Falls ID CAT |
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
| **Spokane / Post Falls / I-90** | **4** | **new page, first Washington page** — Petro Spokane #0339, Broadway Flying J Spokane (ONE9 Dealer #963), Broadway Flying J Spokane Valley (Pilot Dealer #967), Love’s #301 Post Falls ID |
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
| CAT / truck-stop cards | 138 | +4 Spokane / Post Falls I-90 |
| Enforcement do-not-go | 2 | unchanged |

## What shipped tonight

**Spokane / Post Falls / I-90** (`/spokane-post-falls/`): WeighHere’s first Washington page, and the Spokane / Coeur d’Alene gap from last night’s STATUS. TA Petro’s WA index surfaced Petro Spokane with CAT Scale on its own page, which made Love’s #301 Post Falls (held since Oct 14) shippable, and Broadway Group (the Flying J dealer operator) lists CAT Scales on its own pages for both Spokane plazas.

- **Petro Spokane #0339** — 10506 West Aero Road, Spokane WA 99224, I-90 Exit 272 at Medical Lake Road — CAT Scale in TA Petro amenities; (509) 842-1100; geo 47.5906, -117.5612. Fuel 24/7; no CAT staffing hours published → `hours_24h: unknown`.
- **Broadway Flying J Travel Plaza Spokane (Pilot: ONE9 Dealer #963)** — 3709 S Geiger Blvd, Spokane WA 99224, I-90 Exit 276 — CAT Scales on Broadway Group’s own page; (509) 456-8843 (Broadway; Pilot lists (509) 215-5016); geo 47.620534, -117.5069479. Hours conflict: Pilot says Open 24 Hours, Broadway says 24h Wed–Sun, 6 AM–10 PM Mon–Tue → `hours_24h: unknown`, call-ahead note.
- **Broadway Flying J Travel Plaza Spokane Valley (Pilot Dealer #967)** — 6606 E Broadway Ave, Spokane Valley WA 99212, I-90 Exit 286 — CAT Scales on Broadway Group’s own page and in Pilot Company’s listing; (509) 535-3028 (Broadway; Pilot lists (509) 215-4765); geo 47.6632867, -117.3160041. Store 24h.
- **Love’s Travel Stop #301 Post Falls** — 4208 W Expo Pkwy, Post Falls ID 83854, I-90 Exit 2 (Kootenai County) — CAT Scales in Love’s amenities, store Open 24-hours; (208) 773-4577; geo 47.711161, -117.00409.

Wiring: new `spokane_post_falls_i90_body()` + `write()` in `build.py`, NAV, footer, 404 lede, about-page line (now “Utah, Idaho and Washington”), Related on Boise / Twin Falls / McCammon, `tools/seo.py` PLACES (`"spokane-post-falls": ("Spokane, WA & Post Falls, ID", "Washington")`), `STATE_NAMES` + hub region list gain Washington, homepage kicker/meta now name Washington. `CHECKED_HUMAN` → 15 Oct 2026. Livestock unknown; no dedicated house verified.

### Candidates checked but not shipped tonight

- **Pilot Company own-store amenities for ONE9 #963**: pilotcompany.com renders the store’s own amenity list client-side; the raw page only shows #967’s CAT Scale (in Nearby). #963 is verified via Broadway Group (operator) instead.
- **TA Huntington OR** (I-84 Exit 353): TA page amenities do not list CAT Scale — not added. Ontario OR / I-84 west page still lacks a verified CAT.
- **TA Express Biggs Junction OR** (I-84 Exit 104): no CAT Scale in amenities.
- **Love’s OR / WA state indexes**: HTTP 500 (store pages may still work).
- Prior holds unchanged: Twin Falls city CAT, Jerome 165/168, Eden 182, ONE9 #777 Boise / #1426 Nampa / #1429 Fruitland, TA Express Dubois #0940, Flying J #748 Willard, #774 Snowville, Tremonton, Carson City, Temecula / Corona, Redding, Beaver-gap stops, Love’s Fernley / Winnemucca / Carlin.

## Sources used (this compile)

- Petro Spokane #0339: https://www.ta-petro.com/location/wa/petro-spokane/
- TA Petro WA / OR indexes: https://www.ta-petro.com/location/wa/ · https://www.ta-petro.com/location/or/
- TA Huntington (checked, no CAT): https://www.ta-petro.com/location/or/ta-huntington/
- Broadway Flying J Spokane (Exit 276): https://broadwaygroup.com/locations/spokane-truck-stop/
- Broadway Flying J Spokane Valley (Exit 286): https://broadwaygroup.com/locations/spokane-valley-truck-stop/
- Pilot Company ONE9 Dealer #963: https://pilotcompany.com/locations/us/wa/spokane/3709-s-geiger-blvd
- Pilot Company Pilot Dealer #967: https://pilotcompany.com/locations/us/wa/spokane/6606-e-broadway-ave
- Love’s #301 Post Falls: https://www.loves.com/locations/id/post-falls/loves-travel-stop-post-falls-301
- CAT Scale locator (linked, not republished): https://catscale.com/cat-scale-locator/
- ScaleRegistry public-weighing list: https://scaleregistry.com/public-scales.html

## Gaps / deferred

- Twin Falls city CAT (Kimberly Rd) — no operator own page yet
- Spokane: CAT staffing hours unpublished; Broadway hours conflict with Pilot’s listing; no dedicated house
- Ontario OR / I-84 west of Fruitland: TA Huntington lacks CAT; need an own-page CAT
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
- Next candidates: Moses Lake / Ritzville / I-90 or Tri-Cities WA (TA Grandview I-82 to check), Seattle east (TA Seattle East), Blaine, Ontario OR / I-84 west of Fruitland, Temecula / Corona (if a second CAT verifies), Carson City if a chain own-page CAT appears, Redding / Anderson second stop, Snowville / Willard if amenities catch up, ONE9 Boise/Nampa/Fruitland if amenities catch up, Ventura / Santa Barbara CDFA re-pull, Beaver if amenities catch up, Love’s Fernley / Winnemucca / Carlin as corridor extensions
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
