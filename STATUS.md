# WeighHere status — 2 Oct 2026

Compiled evening PT 2 Oct 2026 (nightly ship).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **156** | +2 Pilot #1175 Mayer + Love’s #722 Mayer |
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
| **Mayer / Cordes Lakes / I-17** | **2** | **new page** — Pilot #1175 Mayer + Love’s #722 Mayer |
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
| CAT / truck-stop cards | 92 | +2 Mayer / Cordes Lakes / I-17 corridor |
| Enforcement do-not-go | 2 | unchanged |

## What shipped tonight

**Mayer / Cordes Lakes / I-17** (`/mayer/`): new Yavapai County corridor page with two CAT Scales verified on Pilot Flying J and Love’s *own* location pages (Pilot: `<li class="Amenities-item">CAT Scale</li>` + FAQ Yes; Love’s: visible `<span>CAT Scales</span>` + `catscales` `fieldValue: "true"`). Meets the multi-stop CAT corridor bar (same pattern as Casa Grande / Eloy). Unlocks the long-deferred Love’s #722 Mayer stop once Pilot #1175 at adjacent Exit 262 verified. No ScaleRegistry dedicated Mayer/Cordes Lakes house. Northbound on I-17 Exits 262 then 263 between Phoenix and Flagstaff.

- **Pilot #1175 Mayer / Cordes Lakes** — 14905 Cordes Lake Road, I-17 Exit 262 — CAT Scale on Pilot amenities + FAQ
- **Love’s #722 Mayer** — 14414 S Cross L Rd, I-17 Exit 263 / Arcosanti Rd — CAT Scales on loves.com amenities

Also re-checked deferred candidates (no ship tonight as primary): TA Express White Hills #0292 (US-93 MM 29) own-page CAT + TA Express Henderson #0969 (I-11 Exit 15A / Railroad Pass) own-page CAT — ready for a US-93 / Vegas-approach page later. Lake Havasu I-40 Exit 9 pair (Pilot #211 + Love’s #386) both own-page CAT — deferred to a separate corridor. Pilot Willow Beach #1234 amenities omit CAT — omitted. Love’s #381 Black Canyon City — no own-page CAT confirmation used. Temecula / Corona / Murrieta still thin (no loves.com / ta-petro Temecula/Murrieta pages treated as primary tonight). Redding / Anderson still only TA #0057. CDFA county grids not re-pulled as primary tonight (Mayer corridor stood on operator pages).

## Sources used (this compile)

- Pilot #1175 Mayer: https://locations.pilotflyingj.com/us/az/mayer/14905-cordes-lake-road
- Love’s #722 Mayer: https://www.loves.com/locations/az/mayer/loves-travel-stop-mayer-722
- CAT Scale locator (linked, not republished): https://catscale.com/cat-scale-locator/
- ScaleRegistry CA public-weighing list: https://scaleregistry.com/public-scales.html
- Also noted (deferred): https://www.ta-petro.com/location/az/ta-express-white-hills/ · https://www.ta-petro.com/location/nv/ta-express-henderson/ · https://locations.pilotflyingj.com/us/az/lake-havasu-city/14750-az-95 · https://www.loves.com/locations/az/lake-havasu-city/loves-travel-stop-lake-havasu-city-386

## Gaps / deferred

- Temecula / Corona / Murrieta Love’s / Pilot / TA — no official store/city pages treated as primary tonight; keep deferred
- Redding / Anderson mid-north I-5: only TA Redding #0057 own-page CAT — need a second stop before `/redding-anderson/`
- ONE9 #1424 Westley — visible amenities card still empty; CAT in JSON/description only — re-check before Santa Nella / I-5 extension
- EZ Trip #1275 Madera Ave 12 — visible amenities still omit CAT (embedded JSON noise only); keep omitted from `/madera/`
- TA Express White Hills #0292 + TA Express Henderson #0969 — both own-page CAT verified tonight; ship `/white-hills/` or US-93 / Vegas-approach next when ready
- Lake Havasu I-40 Exit 9 — Pilot #211 + Love’s #386 both own-page CAT verified tonight; ship `/lake-havasu/` next when ready
- Pilot Willow Beach #1234 — amenities omit CAT; keep omitted
- Love’s #381 Black Canyon City — no own-page CAT confirmation used; keep omitted
- ONE9 Ash Fork / TA Ash Fork — no CAT on own pages; keep omitted from `/flagstaff-winslow/`
- Sunmart #640 Ehrenberg / other third-party I-10 CAT pins — omitted until operator own page confirms
- Third-party Fresno / Fowler / Traver CAT pins omitted (no operator own page)
- CDFA Merced / Kern / Shasta / Tehama / Glenn / Fresno / Ventura / Santa Barbara / Sacramento facility grids still often WAF-blocked
- Hours / fees / livestock unknown beyond store-listed 24h vs CAT staffing
- Ventura / Santa Barbara remain thin
- Gilroy Garlic Farm / King City / Prunedale third-party CAT still omitted
- Earlimart / Goshen / Visalia third-party CAT still omitted
- TA Phoenix (Latham) “Scale” mention without CAT on TA’s own page — still omitted
- Love’s #272 Kingman — no CAT on own page; keep omitted
- Love’s #280 Buckeye — no CAT on own page; keep omitted
