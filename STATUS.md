# WeighHere status — 30 Sep 2026

Compiled evening PT 30 Sep 2026 (nightly ship).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **149** | +4 Pilot #593 + Pilot Express #1178 Tucson + Love’s #460 Benson + TA #0226 Willcox |
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
| **Tucson / Benson / Willcox / I-10** | **4** | **new page** — Pilot #593 + Pilot Express #1178 + Love’s #460 + TA #0226 |
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
| CAT / truck-stop cards | 85 | +4 Tucson / Benson / Willcox / I-10 corridor |
| Enforcement do-not-go | 2 | unchanged |

## What shipped tonight

**Tucson / Benson / Willcox / I-10** (`/tucson-benson/`): new Pima / Cochise County corridor page with four CAT Scales verified on Pilot Flying J / Love’s / TA *own* location pages (Pilot: `<li class="Amenities-item">CAT Scale</li>` + FAQ Yes; Love’s: visible `<span>CAT Scales</span>` + `catscales` `fieldValue: "true"`; TA: `<li>CAT Scale</li>`). Meets the multi-stop CAT corridor bar. No ScaleRegistry dedicated Tucson/Benson/Willcox house. West-to-east on I-10 Exits 268, 273, 302, and 340.

- **Pilot #593 Tucson** — 5570 E Travel Plaza Way, I-10 Exit 268 — CAT Scale on Pilot amenities + FAQ
- **Pilot Express #1178 Tucson** — 9255 S Rita Rd, I-10 Exit 273 — CAT Scale on Pilot amenities + FAQ
- **Love’s #460 Benson** — 643 S. Highway 90, I-10 Exit 302 — CAT Scales on loves.com amenities
- **TA #0226 Willcox** — 1501 North Fort Grant Road, I-10 Exit 340 — CAT Scale on ta-petro.com amenities

Also re-checked deferred candidates (no ship): Love’s #722 Mayer still only own-page I-17 CAT (no second I-17 stop). Redding / Anderson still only TA #0057. Temecula / Corona / Murrieta still thin. ONE9 #1424 Westley amenities still unclear. Love’s #280 Buckeye still no CAT. Love’s #272 Kingman still no CAT. Sunmart #640 Ehrenberg still no primary operator page. Ventura / Santa Barbara still thin. Flagstaff / Bellemont / Winslow / Holbrook I-40 east and TA Express White Hills (US-93) remain deferred corridor seeds. CDFA county grids not re-pulled as primary tonight (Tucson corridor stood on operator pages).

## Sources used (this compile)

- Pilot #593 Tucson: https://locations.pilotflyingj.com/us/az/tucson/5570-e-travel-plaza-way
- Pilot Express #1178 Tucson: https://locations.pilotflyingj.com/us/az/tucson/9255-s-rita-rd
- Love’s #460 Benson: https://www.loves.com/locations/az/benson/loves-travel-stop-benson-460
- TA #0226 Willcox: https://www.ta-petro.com/location/az/ta-willcox/
- CAT Scale locator (linked, not republished): https://catscale.com/cat-scale-locator/
- ScaleRegistry CA public-weighing list: https://scaleregistry.com/public-scales.html

## Gaps / deferred

- Temecula / Corona / Murrieta Love’s / Pilot — no official store/city pages found; keep deferred
- Redding / Anderson mid-north I-5: only TA Redding #0057 own-page CAT — need a second stop before `/redding-anderson/`
- ONE9 #1424 Westley — visible amenities card still empty; CAT in JSON/description only — re-check before Santa Nella / I-5 extension
- EZ Trip #1275 Madera Ave 12 — visible amenities still omit CAT (embedded JSON noise only); keep omitted from `/madera/`
- Love’s #722 Mayer (I-17 Exit 263) — own-page CAT verified; needs a second I-17 stop for a corridor page
- Flagstaff / Bellemont / Winslow / Holbrook I-40 east: Pilot #180 Bellemont (+ others) for a future corridor
- TA Express White Hills (US-93) own-page CAT — deferred to a US-93 / Vegas approach page (needs a second verified stop)
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
