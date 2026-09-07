# WeighHere status — 6 Sep 2026

Compiled evening PT 6 Sep 2026 (nightly ship).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **91** | +4 Hwy 99 / Stockton approach CAT stops |
| Los Angeles County | 45 | unchanged |
| Orange County | 7 | unchanged |
| Inland Empire | 9 | unchanged (2 San Bernardino + 7 Riverside) |
| San Diego County | 8 | unchanged |
| Phoenix metro / Maricopa | 4 | unchanged |
| Central Valley (Kern+Fresno+Merced filter) | 8 | unchanged (Lebec + Santa Nella also on Grapevine) |
| Sacramento approaches | 4 | unchanged (ID-filtered; Ripon/ONE9/Love's Lodi moved off this page) |
| Grapevine / I-5 mid-CA | 4 | unchanged |
| **Hwy 99 / Stockton approaches** | **4** | new (all San Joaquin) |
| **Landfill / waste rows (sitewide)** | **12** | unchanged |
| Dedicated / walk-up houses | 11–12 | unchanged |
| CAT / truck-stop cards | 25–28 | +4 corridor CAT |
| Enforcement do-not-go | 2 | unchanged (I-405 Carson + San Onofre) |

## What shipped tonight

**Hwy 99 / Stockton approaches** (`/highway-99/`): four CAT Scales verified on Pilot Flying J and Love's *own* location pages for the CA-99 / Stockton corridor:

- Flying J #618 Ripon (San Joaquin, CA-99 Exit 237) — previously deferred from Grapevine
- Love's #223 Ripon (San Joaquin, CA-99 Exit 237B)
- ONE9 Dealer #1361 Lodi (San Joaquin, I-5 Exit 485) — CAT on Pilot's ONE9 page
- Love's #538 Lodi (San Joaquin, I-5 Exit 485)

No ScaleRegistry dedicated house in Stockton / Manteca / Ripon / Modesto. CDFA San Joaquin / Stanislaus grids still WAF-blocked. Sacramento approaches page now ID-filters its original four I-5 anchors so the new San Joaquin rows do not clutter that page.

## Sources used (this compile)

- Flying J #618 Ripon: https://locations.pilotflyingj.com/us/ca/ripon/1501-n-jack-tone-rd
- Love's #223 Ripon: https://www.loves.com/locations/ca/ripon/loves-travel-stop-ripon-223
- ONE9 #1361 Lodi: https://locations.pilotflyingj.com/us/ca/lodi/14749-thornton-rd
- Love's #538 Lodi: https://www.loves.com/locations/ca/lodi/loves-travel-stop-lodi-538
- ScaleRegistry public scales: https://scaleregistry.com/public-scales.html
- CAT Scale locator (linked, not republished): https://catscale.com/cat-scale-locator/

Not used: Penske locator, Trucker Path, AllStays, Propane Atlas, MapQuest POIs, invented ticket fees, third-party-only CAT listings (Modesto Truck Plaza, Vanco Stockton).

## Gaps (honest)

- **CDFA county grids** (San Joaquin, Stanislaus, Kern, Merced, Sacramento corridor, Ventura, etc.): still WAF-blocked from this host.
- **Lat/lng:** still missing for Love's Ripon, Love's Lodi, Love's Santa Nella, Love's Patterson, Love's Williams, Selma, Merced, most landfill rows.
- **Modesto Truck Plaza (Hwy 99 Exit 223) / Vanco Stockton (I-5 Exit 471):** third-party CAT directories only — omitted.
- **Love's #736 Madera / Pilot #365 Madera:** own pages list CAT on Hwy 99 farther south — candidates for a longer Hwy 99 corridor page; not duplicated tonight.
- **ONE9 #1424 Westley:** no CAT amenity on Pilot's page — omitted.
- **West Sacramento CAT #3390:** still third-party only.
- **Walk-up weighmaster tickets at landfill gates:** still unverified.
- **Livestock:** unknown on most rows.
- **User reports form:** not built.
- **Affiliate IDs:** placeholder only.
- **Next geography candidates:** Ventura / Santa Barbara if CDFA loads; I-15 corridor; Madera Hwy 99 pair; or newly verified dedicated houses.

## Blockers

None for shipping this corridor page. Do not treat it as a complete San Joaquin / Stanislaus inventory or as a Stockton dedicated-house list.
