# WeighHere status — 1 Oct 2026

Compiled evening PT 1 Oct 2026 (nightly ship).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **154** | +5 Love’s #553 Williams + Pilot #180 Bellemont + Love’s #971 Winslow + Flying J #612 Winslow + TA #0246 Holbrook |
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
| **Flagstaff / Winslow / Holbrook / I-40** | **5** | **new page** — Love’s #553 Williams + Pilot #180 Bellemont + Love’s #971 Winslow + Flying J #612 Winslow + TA #0246 Holbrook |
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
| CAT / truck-stop cards | 90 | +5 Flagstaff / Winslow / Holbrook / I-40 corridor |
| Enforcement do-not-go | 2 | unchanged |

## What shipped tonight

**Flagstaff / Winslow / Holbrook / I-40** (`/flagstaff-winslow/`): new Coconino / Navajo County corridor page with five CAT Scales verified on Love’s / Pilot Flying J / TA *own* location pages (Love’s: visible `<span>CAT Scales</span>` + `catscales` `fieldValue: "true"`; Pilot/Flying J: `<li class="Amenities-item">CAT Scale</li>` + FAQ Yes; TA: `<li>CAT Scale</li>`). Meets the multi-stop CAT corridor bar. No ScaleRegistry dedicated Flagstaff/Winslow/Holbrook house. West-to-east on I-40 Exits 163, 185, 255 (×2), and 283.

- **Love’s #553 Williams** — 1055 N Grand Canyon Blvd, I-40 Exit 163 — CAT Scales on loves.com amenities
- **Pilot #180 Bellemont** — 12500 W I-40, I-40 Exit 185 — CAT Scale on Pilot amenities + FAQ
- **Love’s #971 Winslow** — 720 Transcon Ln, I-40 Exit 255 — CAT Scales on loves.com amenities
- **Flying J #612 Winslow** — 400 Transcon Ln, I-40 Exit 255 — CAT Scale on Pilot amenities + FAQ
- **TA #0246 Holbrook** — 3747 Express Drive, I-40 Exit 283 — CAT Scale on ta-petro.com amenities

Also re-checked deferred candidates (no ship): ONE9 Ash Fork and TA Ash Fork — no CAT on own pages (omitted). Love’s #722 Mayer still only own-page I-17 CAT (no second I-17 stop). Redding / Anderson still only TA #0057. Temecula / Corona / Murrieta still thin. TA Express White Hills (US-93) still needs a second verified US-93 / Vegas-approach stop. CDFA county grids not re-pulled as primary tonight (Flagstaff corridor stood on operator pages).

## Sources used (this compile)

- Love’s #553 Williams: https://www.loves.com/locations/az/williams/loves-travel-stop-williams-553
- Pilot #180 Bellemont: https://locations.pilotflyingj.com/us/az/bellemont/12500-w-i-40
- Love’s #971 Winslow: https://www.loves.com/locations/az/winslow/loves-travel-stop-winslow-971
- Flying J #612 Winslow: https://locations.pilotflyingj.com/us/az/winslow/400-transcon-ln
- TA #0246 Holbrook: https://www.ta-petro.com/location/az/ta-holbrook/
- CAT Scale locator (linked, not republished): https://catscale.com/cat-scale-locator/
- ScaleRegistry CA public-weighing list: https://scaleregistry.com/public-scales.html

## Gaps / deferred

- Temecula / Corona / Murrieta Love’s / Pilot — no official store/city pages found; keep deferred
- Redding / Anderson mid-north I-5: only TA Redding #0057 own-page CAT — need a second stop before `/redding-anderson/`
- ONE9 #1424 Westley — visible amenities card still empty; CAT in JSON/description only — re-check before Santa Nella / I-5 extension
- EZ Trip #1275 Madera Ave 12 — visible amenities still omit CAT (embedded JSON noise only); keep omitted from `/madera/`
- Love’s #722 Mayer (I-17 Exit 263) — own-page CAT verified; needs a second I-17 stop for a corridor page
- TA Express White Hills (US-93) own-page CAT — deferred to a US-93 / Vegas approach page (needs a second verified stop)
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
