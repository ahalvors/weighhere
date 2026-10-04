# WeighHere status — 3 Oct 2026

Compiled evening PT 3 Oct 2026 (nightly ship).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **158** | +2 TA Express White Hills #0292 + TA Express Henderson #0969 |
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
| **White Hills / Henderson / US-93** | **2** | **new page** — TA Express White Hills #0292 + TA Express Henderson #0969 |
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
| CAT / truck-stop cards | 94 | +2 White Hills / Henderson / US-93 corridor |
| Enforcement do-not-go | 2 | unchanged |

## What shipped tonight

**White Hills / Henderson / US-93** (`/white-hills/`): new Mohave / Clark corridor page with two CAT Scales verified on TravelCenters of America *own* location pages (both: visible `<li>CAT Scale</li>` on ta-petro.com food/amenities tab; JSON-LD GasStation with street address, phone, geo). Meets the multi-stop CAT corridor bar (same pattern as Mayer / Casa Grande). US-93 Vegas-approach pair long deferred until both own-page CAT partners re-verified tonight. Northbound White Hills (US-93 MM 29, AZ) then Henderson Railroad Pass (I-11 Exit 15A, NV).

- **TA Express White Hills #0292** — 19210 US Hwy 93, White Hills AZ 86445, US-93 MM 29 — CAT Scale on ta-petro.com amenities
- **TA Express Henderson #0969** — 1550 Railroad Pass Casino Road, Henderson NV 89002, I-11 Exit 15A — CAT Scale on ta-petro.com amenities

Also re-checked deferred candidates (no ship tonight as primary): Lake Havasu I-40 Exit 9 pair (Pilot #211 + Love’s #386) still deferred to a separate corridor. Pilot Willow Beach #1234 amenities omit CAT — omitted. Love’s #381 Black Canyon City — no own-page CAT confirmation used. Temecula / Corona / Murrieta still thin. Redding / Anderson still only TA #0057. CDFA county grids not re-pulled as primary tonight (US-93 corridor stood on operator pages).

## Sources used (this compile)

- TA Express White Hills #0292: https://www.ta-petro.com/location/az/ta-express-white-hills/
- TA Express Henderson #0969: https://www.ta-petro.com/location/nv/ta-express-henderson/
- CAT Scale locator (linked, not republished): https://catscale.com/cat-scale-locator/
- ScaleRegistry CA public-weighing list: https://scaleregistry.com/public-scales.html
- Also noted (deferred): https://locations.pilotflyingj.com/us/az/lake-havasu-city/14750-az-95 · https://www.loves.com/locations/az/lake-havasu-city/loves-travel-stop-lake-havasu-city-386

## Gaps / deferred

- Temecula / Corona / Murrieta Love’s / Pilot / TA — no official store/city pages treated as primary tonight; keep deferred
- Redding / Anderson mid-north I-5: only TA Redding #0057 own-page CAT — need a second stop before `/redding-anderson/`
- ONE9 #1424 Westley — visible amenities card still empty; CAT in JSON/description only — re-check before Santa Nella / I-5 extension
- EZ Trip #1275 Madera Ave 12 — visible amenities still omit CAT (embedded JSON noise only); keep omitted from `/madera/`
- Lake Havasu I-40 Exit 9 — Pilot #211 + Love’s #386 both previously own-page CAT; ship `/lake-havasu/` next when ready (re-verify first)
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
