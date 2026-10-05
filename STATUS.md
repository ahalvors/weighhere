# WeighHere status — 4 Oct 2026

Compiled evening PT 4 Oct 2026 (nightly ship).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **160** | +2 Pilot #211 + Love’s #386 Lake Havasu City |
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
| **Lake Havasu / I-40 Exit 9** | **2** | **new page** — Pilot #211 + Love’s #386 |
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
| CAT / truck-stop cards | 96 | +2 Lake Havasu / I-40 Exit 9 |
| Enforcement do-not-go | 2 | unchanged |

## What shipped tonight

**Lake Havasu / I-40 Exit 9** (`/lake-havasu/`): new Mohave County page for the I-40 / AZ-95 junction north of Lake Havasu City, with two CAT Scales verified tonight on the operators’ *own* location pages. Long-deferred pair, now shipped as its own corridor page. Framed for boat trailers, RVs, toy haulers, U-Haul and PPM moves.

- **Pilot Travel Center #211** — 14750 AZ-95, Lake Havasu City AZ 86404, I-40/AZ-95 Exit 9 — Pilot page lists CAT Scale in amenities and FAQ answers yes; store Open 24 Hours; phone (928) 764-2410; geo 34.728256, -114.315209
- **Love’s Travel Stop #386** — 14875 AZ Hwy-95, Lake Havasu City AZ 86404, Exit 9 on I-40 — Love’s page lists CAT Scales among Select Amenities; store open 24 hours; phone (928) 764-1505; geo 34.724959, -114.315844

Cross-links added from Kingman, White Hills, Mayer, Flagstaff, Tucson and other AZ pages, nav, footer, home lede, and sitemap. Hours shown are store-listed 24h, not CAT staffing. Livestock unknown. No dedicated house verified.

## Sources used (this compile)

- Pilot #211 Lake Havasu City: https://locations.pilotflyingj.com/us/az/lake-havasu-city/14750-az-95
- Love’s #386 Lake Havasu City: https://www.loves.com/locations/az/lake-havasu-city/loves-travel-stop-lake-havasu-city-386
- CAT Scale locator (linked, not republished): https://catscale.com/cat-scale-locator/
- ScaleRegistry CA public-weighing list: https://scaleregistry.com/public-scales.html

## Gaps / deferred

- Temecula / Corona / Murrieta Love’s / Pilot / TA — no official store/city pages treated as primary tonight; keep deferred
- Redding / Anderson mid-north I-5: only TA Redding #0057 own-page CAT — need a second stop before `/redding-anderson/`
- ONE9 #1424 Westley — visible amenities card still empty; CAT in JSON/description only — re-check before Santa Nella / I-5 extension
- EZ Trip #1275 Madera Ave 12 — visible amenities still omit CAT (embedded JSON noise only); keep omitted from `/madera/`
- Lake Havasu City in-town / Parker AZ — no dedicated public scale house found on an operator page; Lake Havasu page has CAT only
- Next candidates: Temecula / Corona (needs official pages), Redding / Anderson (needs a second own-page CAT), Ventura / Santa Barbara CDFA re-pull
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
