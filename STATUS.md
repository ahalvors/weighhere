# WeighHere status — 11 Oct 2026

Compiled evening PT 11 Oct 2026 (nightly ship).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **188** | +3 Brigham / Ogden / I-15 CAT (Flying J #744, ONE9 #294, Love’s #686) |
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
| **Brigham / Ogden / I-15** | **3** | **new page** — Flying J #744 Ogden, ONE9 #294 Ogden, Love’s #686 Brigham City |
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
| CAT / truck-stop cards | 124 | +3 Brigham / Ogden / I-15 |
| Enforcement do-not-go | 2 | unchanged |

## What shipped tonight

**Brigham / Ogden / I-15** (`/brigham-ogden/`): new northern Utah page covering I-15 from Ogden (Weber County) through Brigham City (Box Elder County), continuing northeast from `/springville-salt-lake/` (North Salt Lake). Three CAT Scales verified tonight on the operators’ *own* location pages (amenities list CAT; FAQ-yes alone is not enough).

- **Flying J Travel Center #744 Ogden** — 1172 West 21st Street, Ogden UT 84401, I-15 Exit 343 — amenities list CAT Scale and FAQ answers yes; Open 24 Hours; (801) 849-3414; geo 41.2306945, -112.0076735
- **ONE9 Travel Center #294 Ogden** — 1670 W 12th St, Ogden UT 84404, I-15 & UT-39 Exit 344 — amenities list CAT Scale and FAQ answers yes; Open 24 Hours; (801) 731-2900; geo 41.245305720861744, -112.01938527116394
- **Love’s Travel Stop #686 Brigham City** — 20 South 1550 West St, Brigham City UT 84302, I-15 Exit 363 — Love’s page lists CAT Scales; store Open 24-hours; (435) 723-1789; geo 41.508809, -112.053738

Cross-links added from Springville / Salt Lake, Fillmore / Nephi, St. George / Cedar City, Las Vegas, and I-15 / High Desert Related lists, nav, footer, 404 lede, and sitemap. Hours shown are store-listed 24h, not CAT staffing. Livestock unknown. No dedicated house verified. Slug is `/brigham-ogden/` (not tremonton) because no Tremonton Love’s own-page location was found tonight.

### Candidates checked but not shipped as own pages tonight

- **Flying J #748 Willard** (I-15 Exit 357): FAQ answers yes to CAT scale, but visible amenities omit CAT Scale — held (same FAQ-yes / amenities-omit pattern).
- **Flying J #774 Snowville** (I-84 Exit 7): FAQ answers yes; amenities omit CAT Scale — held.
- **Love’s Tremonton**: no loves.com own location page found for Tremonton UT (third-party directories only — not used).
- **Carson City / US-395**: Maverik third-party CAT only — still held.
- **Temecula / Corona / Murrieta**: Pilot Dealer #1458 Perris still alone — need a second own-page CAT.
- **Redding / Anderson**: still only TA Redding #0057.
- **Beaver / Fillmore gap stops**: Flying J #509 Beaver, TA Fillmore #0519, Flying J Scipio #510, ONE9 Fillmore #1479, Flying J Richfield #773, TA Express Salina — amenities still omit CAT (not re-fetched tonight; held from prior nights).
- **Love’s Fernley #246**, **Love’s Winnemucca #797**, **Love’s Carlin #978**: optional future adds to existing Reno / Elko corridor pages.

## Sources used (this compile)

- Flying J #744 Ogden: https://locations.pilotflyingj.com/us/ut/ogden/1172-west-21st-street
- ONE9 #294 Ogden: https://locations.pilotflyingj.com/us/ut/ogden/1670-w-12th-st
- Love’s #686 Brigham City: https://www.loves.com/locations/ut/brigham-city/loves-travel-stop-brigham-city-686
- Flying J #748 Willard (held): https://locations.pilotflyingj.com/us/ut/willard/600-w-750-n
- Flying J #774 Snowville (held): https://locations.pilotflyingj.com/us/ut/snowville/90-s-stone-rd
- CAT Scale locator (linked, not republished): https://catscale.com/cat-scale-locator/
- ScaleRegistry public-weighing list: https://scaleregistry.com/public-scales.html

## Gaps / deferred

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
