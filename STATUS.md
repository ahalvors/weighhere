# WeighHere status — 5 Oct 2026

Compiled evening PT 5 Oct 2026 (nightly ship).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **165** | +5 Las Vegas / I-15 CAT (Flying J #513, TA #0108, Pilot #341, Petro #0331, Love’s #340) |
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
| **Las Vegas / I-15** | **5** | **new page** — Flying J #513 Jean, TA #0108, Pilot #341, Petro #0331, Love’s #340 |
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
| CAT / truck-stop cards | 101 | +5 Las Vegas / I-15 |
| Enforcement do-not-go | 2 | unchanged |

## What shipped tonight

**Las Vegas / I-15** (`/las-vegas/`): new Clark County NV page covering I-15 through the Las Vegas valley, Primm to Apex, with five CAT Scales verified tonight on the operators’ *own* location pages. First Nevada metro page; pairs with `/white-hills/` (US-93 / I-11 Henderson approach) and `/i-15/` (Barstow / High Desert side).

- **Flying J #513 Jean / Primm** — 115 West Primm Blvd, Jean NV 89019, I-15 Exit 1 — own amenities list CAT Scale; Open 24 Hours; (702) 679-6666; geo 35.6097184, -115.3917507
- **TA Las Vegas #0108** — 8050 Dean Martin Drive, Las Vegas NV 89139, I-15 Blue Diamond Exit 33 — TA page lists CAT Scale; fuel 24/7; (702) 361-1176; geo 36.0433, -115.1873
- **Pilot Travel Center #341 North Las Vegas** — 3812 E Craig Rd, North Las Vegas NV 89031, I-15 Exit 48 — amenities list CAT Scale and FAQ answers yes; Open 24 Hours; (702) 644-1600; geo 36.2409528, -115.0978424
- **Petro North Las Vegas #0331** — 6595 North Hollywood Blvd, North Las Vegas NV 89115, I-15 Exit 54 (Speedway Blvd) — Petro page lists CAT Scale; fuel 24/7; (702) 632-2640; geo 36.2797, -115.0261
- **Love’s Travel Stop #340 Las Vegas (Apex)** — 12501 Apex Great Basin Pkwy, Las Vegas NV 89165, Exit 64 on I-15 — Love’s page lists CAT Scales among amenities; store and Truck Care open 24 hours; (702) 643-7398; geo 36.381561, -114.896529

Cross-links added from White Hills, Lake Havasu, I-15 / High Desert and other pages’ Related lists, nav, footer, home lede, and sitemap. Hours shown are store-listed 24h, not CAT staffing. Livestock unknown. No dedicated house verified.

## Sources used (this compile)

- Flying J #513 Jean: https://locations.pilotflyingj.com/us/nv/jean/115-west-primm-blvd.
- TA Las Vegas #0108: https://www.ta-petro.com/location/nv/ta-las-vegas/
- Pilot #341 North Las Vegas: https://locations.pilotflyingj.com/us/nv/north-las-vegas/3812-e-craig-rd
- Petro North Las Vegas #0331: https://www.ta-petro.com/location/nv/petro-north-las-vegas/
- Love’s #340 Las Vegas: https://www.loves.com/locations/nv/las-vegas/loves-travel-stop-las-vegas-340
- CAT Scale locator (linked, not republished): https://catscale.com/cat-scale-locator/
- ScaleRegistry CA public-weighing list: https://scaleregistry.com/public-scales.html

## Gaps / deferred

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
