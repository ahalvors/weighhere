# WeighHere status — 10 Oct 2026

Compiled evening PT 10 Oct 2026 (nightly ship).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **185** | +5 Springville / Salt Lake / I-15 CAT (Love’s #518, Flying J #746, Love’s #436, Flying J #772, TA #0060) |
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
| **Springville / Salt Lake / I-15** | **5** | **new page** — Love’s #518 Springville, Flying J #746 SLC, Love’s #436 SLC, Flying J #772 North Salt Lake, TA Tooele #0060 |
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
| CAT / truck-stop cards | 121 | +5 Springville / Salt Lake / I-15 |
| Enforcement do-not-go | 2 | unchanged |

## What shipped tonight

**Springville / Salt Lake / I-15** (`/springville-salt-lake/`): new Wasatch Front page covering I-15 / I-80 from Springville (Utah County) through Salt Lake City and North Salt Lake, plus TA Tooele on I-80 west (Tooele County). Continues northeast from `/fillmore-nephi/` (Nephi Exit 222). Five CAT Scales verified tonight on the operators’ *own* location pages.

- **Love’s Travel Stop #518 Springville** — 358 South 2200 West, Springville UT 84663, I-15 Exit 260 — Love’s page lists CAT Scales; store Open 24-hours; (801) 489-8746; geo 40.162271, -111.651681
- **Flying J Travel Center #746 Salt Lake City** — 2025 S 900 W, Salt Lake City UT 84104, I-15 & I-80 / SR-201 Exit 17 — amenities list CAT Scale and FAQ answers yes; Open 24 Hours; (801) 972-3711; geo 40.726649, -111.915592
- **Love’s Travel Stop #436 Salt Lake City** — 25 N. Redwood Rd., Salt Lake City UT 84116, I-80 Exit 118 — Love’s page lists CAT Scales; store Open 24-Hours; (801) 239-1100; geo 40.769949, -111.939921
- **Flying J Travel Center #772 North Salt Lake** — 885 North Pointe Cir, North Salt Lake UT 84054, I-215 Exit 27 — amenities list CAT Scale and FAQ answers yes; Open 24 Hours; (801) 936-1408; geo 40.836158, -111.934078
- **TA Tooele #0060** — 8836 North Highway 40, Salt Lake City UT 84074 (Tooele County / Lake Point area), I-80 Exit 99 — TA page lists CAT Scale; Shell gas/diesel 24/7; (801) 250-8585; geo 40.6899, -112.2629

Cross-links added from Fillmore / Nephi, St. George / Cedar City, Las Vegas, and I-15 / High Desert Related lists, nav, footer, 404 lede, and sitemap. Hours shown are store-listed 24h, not CAT staffing. Livestock unknown. No dedicated house verified.

### Candidates checked but not shipped as own pages tonight

- **Love’s #686 Brigham City** (I-15 Exit 363): own page lists CAT Scales — held for a separate Brigham / northern Utah corridor rather than stretching this metro page.
- **Carson City / US-395**: Maverik third-party CAT only — still held.
- **Temecula / Corona / Murrieta**: Pilot Dealer #1458 Perris still alone — need a second own-page CAT.
- **Redding / Anderson**: still only TA Redding #0057.
- **Beaver / Fillmore gap stops**: Flying J #509 Beaver, TA Fillmore #0519, Flying J Scipio #510, ONE9 Fillmore #1479, Flying J Richfield #773, TA Express Salina — amenities still omit CAT (not re-fetched tonight; held from 9 Oct).
- **Love’s Fernley #246**, **Love’s Winnemucca #797**, **Love’s Carlin #978**: optional future adds to existing Reno / Elko corridor pages.

## Sources used (this compile)

- Love’s #518 Springville: https://www.loves.com/locations/ut/springville/loves-travel-stop-springville-518
- Flying J #746 Salt Lake City: https://locations.pilotflyingj.com/us/ut/salt-lake-city/2025-s-900-w
- Love’s #436 Salt Lake City: https://www.loves.com/locations/ut/salt-lake-city/loves-travel-stop-salt-lake-city-436
- Flying J #772 North Salt Lake: https://locations.pilotflyingj.com/us/ut/north-salt-lake/885-north-pointe-cir
- TA Tooele #0060: https://www.ta-petro.com/location/ut/ta-tooele/
- Love’s #686 Brigham City (held for next north page): https://www.loves.com/locations/ut/brigham-city/loves-travel-stop-brigham-city-686
- CAT Scale locator (linked, not republished): https://catscale.com/cat-scale-locator/
- ScaleRegistry public-weighing list: https://scaleregistry.com/public-scales.html

## Gaps / deferred

- Love’s #686 Brigham City own-page CAT — next northern Utah I-15 candidate (with Snowville / Tremonton if verified)
- Mesquite / Beaver Dam gap: Flying J Dealer #1171 Mesquite still omits CAT from amenities
- Flying J Dealer #509 Beaver amenities omit CAT — gap between Parowan and Fillmore
- Carson City / US-395 / Truckee: no Pilot/Love’s/TA/Flying J/Petro own-page CAT yet (Maverik third-party only)
- Temecula / Corona / Murrieta: Pilot Perris #1458 alone — need a second own-page CAT before `/temecula-corona/`
- Redding / Anderson mid-north I-5: only TA Redding #0057 — need a second stop before `/redding-anderson/`
- Next candidates: Brigham / northern Utah (Love’s #686 + more), Temecula / Corona (if a second CAT verifies), Carson City if a chain own-page CAT appears, Redding / Anderson second stop, Ventura / Santa Barbara CDFA re-pull, Beaver if amenities catch up, Love’s Fernley / Winnemucca / Carlin as corridor extensions
- Elko / Winnemucca held: Flying J #692 Wells and Pilot #147 West Wendover (FAQ yes, amenities omit CAT)
- Las Vegas omitted ONE9s still amenities-omit CAT
- ONE9 #1424 Westley — visible amenities card still empty
- EZ Trip #1275 Madera Ave 12 — visible amenities still omit CAT
- Hours / fees / livestock unknown beyond store-listed fuel 24/7 vs CAT staffing
- Ventura / Santa Barbara remain thin
- CDFA Merced / Kern / Shasta / Tehama / Glenn / Fresno / Ventura / Santa Barbara / Sacramento facility grids still often WAF-blocked
