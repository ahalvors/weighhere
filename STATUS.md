# WeighHere status — 6 Oct 2026

Compiled evening PT 6 Oct 2026 (nightly ship).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **170** | +5 Reno / Sparks / Fernley / I-80 CAT (TA #0172, Petro #0338, ONE9 #1359, Pilot #340, Flying J #1005) |
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
| **Reno / Sparks / Fernley / I-80** | **5** | **new page** — TA #0172, Petro #0338, ONE9 #1359, Pilot #340, Flying J #1005 |
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
| CAT / truck-stop cards | 106 | +5 Reno / Sparks / Fernley / I-80 |
| Enforcement do-not-go | 2 | unchanged |

## What shipped tonight

**Reno / Sparks / Fernley / I-80** (`/reno-sparks/`): new northern Nevada page covering I-80 from Sparks east to Fernley (Washoe, Storey and Lyon Counties), with five CAT Scales verified tonight on the operators’ *own* location pages. Pairs with `/sacramento/` (Donner / I-80 California side) and `/las-vegas/`.

- **TA Sparks #0172** — 200 North McCarren (as published), Sparks NV 89431, I-80 Exit 19 — TA page lists CAT Scale; fuel 24/7; 775-359-0550; geo 39.5351, -119.7361
- **Petro Sparks #0338** — 1950 East Greg St, Sparks NV 89431, I-80 Exit 21 — Petro page lists CAT Scale; fuel 24/7; 775-355-8888; geo 39.5233, -119.7087
- **ONE9 Travel Center #1359 Sparks** — 400 USA Parkway (Hwy 439), Sparks NV 89437 (Storey County), I-80 Exit 32 — amenities list CAT Scale and FAQ answers yes; Open 24 Hours; (775) 316-7002; geo 39.5590145, -119.4898624
- **Pilot Travel Center #340 Fernley** — 465 Pilot Rd, Fernley NV 89408, I-80 Exit 46 — amenities list CAT Scale and FAQ answers yes; Open 24 Hours; (775) 575-5115; geo 39.6137157, -119.2658856 (page also showed a limited-fuel notice tonight; not reflected in listing)
- **Flying J Travel Center #1005 Fernley** — 480 Truck Inn Way, Fernley NV 89408, I-80 Exit 48 — amenities list CAT Scale and FAQ answers yes; Open 24 Hours; (775) 575-5919; geo 39.6149587, -119.21674

Cross-links added from Las Vegas, Sacramento, White Hills, Kingman, Flagstaff, Mayer, I-15 Related lists, nav, footer, 404, and sitemap. Hours shown are store-listed 24h, not CAT staffing. Livestock unknown. No dedicated house verified.

## Sources used (this compile)

- TA Sparks #0172: https://www.ta-petro.com/location/nv/ta-sparks/
- Petro Sparks #0338: https://www.ta-petro.com/location/nv/petro-sparks/
- ONE9 #1359 Sparks: https://locations.pilotflyingj.com/us/nv/sparks/400-usa-parkway-(hwy-439)
- Pilot #340 Fernley: https://locations.pilotflyingj.com/us/nv/fernley/465-pilot-rd
- Flying J #1005 Fernley: https://locations.pilotflyingj.com/us/nv/fernley/480-truck-inn-way
- CAT Scale locator (linked, not republished): https://catscale.com/cat-scale-locator/
- ScaleRegistry public-weighing list: https://scaleregistry.com/public-scales.html

## Gaps / deferred

- Reno: no dedicated walk-up public scale house found on an operator page; Love’s northern Nevada locations not checked on Love’s own pages (loves.com state list did not render server-side); Carson City / US-395 and Truckee have no own-page CAT yet
- Other NV I-80 Pilot/TA stops (Winnemucca, Mill City, Carlin, Wells, West Wendover) are candidates for a future Elko / Winnemucca page

- Las Vegas omitted (own amenities list does not show CAT): ONE9 #1395 Jean Exit 12, ONE9 #1488 Cheyenne Ave, ONE9 #1492 Apex Exit 58, ONE9 #1477 Moapa, Flying J #1171 Mesquite, ONE9 #1504 Searchlight; Petro Henderson (no CAT on TA Petro page)
- No Las Vegas / Clark County dedicated walk-up house found on an operator page; Nevada has no CDFA-style grid we can cite
- Next candidates: Mesquite / St. George I-15 (needs own-page CAT), Temecula / Corona, Redding / Anderson, Ventura / Santa Barbara CDFA re-pull
- Temecula / Corona / Murrieta Love’s / Pilot / TA — no official store/city pages treated as primary tonight; keep deferred
- Redding / Anderson mid-north I-5: only TA Redding #0057 own-page CAT — need a second stop before `/redding-anderson/`
- ONE9 #1424 Westley — visible amenities card still empty; CAT in JSON/description only — re-check before Santa Nella / I-5 extension
- EZ Trip #1275 Madera Ave 12 — visible amenities still omit CAT (embedded JSON noise only); keep omitted from `/madera/`
- Lake Havasu City in-town / Parker AZ — no dedicated public scale house found on an operator page; Lake Havasu page has CAT only
- Pilot Willow Beach #1234 — amenities omit CAT; keep omitted
- Love’s #381 Black Canyon City — no own-page CAT confirmation used; keep omitted
- ONE9 Ash Fork / TA Ash Fork — no CAT on own pages; keep omitted from `/flagstaff-winslow/`
- Sunmart #640 Ehrenberg / other third-party I-10 CAT pins — omitted until operator own page confirms
- Third-party Fresno / Fowler / Traver CAT pins omitted (no operator own page)
- CDFA Merced / Kern / Shasta / Tehama / Glenn / Fresno / Ventura / Santa Barbara / Sacramento facility grids still often WAF-blocked
- Hours / fees / livestock unknown beyond store-listed fuel 24/7 vs CAT staffing
- Ventura / Santa Barbara remain thin
- Gilroy Garlic Farm / King City / Prunedale third-party CAT still omitted
- Earlimart / Goshen / Visalia third-party CAT still omitted
- TA Phoenix (Latham) “Scale” mention without CAT on TA’s own page — still omitted
- Love’s #272 Kingman — no CAT on own page; keep omitted
- Love’s #280 Buckeye — no CAT on own page; keep omitted
