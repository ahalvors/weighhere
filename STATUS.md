# WeighHere status — 23 Sep 2026

Compiled evening PT 23 Sep 2026 (nightly ship).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **130** | +1 unique (EZ Trip #1277 Huron); removed duplicate Love’s #830 that inflated tip’s 130→129 unique |
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
| Phoenix metro / Maricopa | 4 | unchanged |
| Central Valley (Kern+Fresno+Merced filter) | 18 | +1 Huron (also on Fresno page); tip’s 18 included a Love’s #830 dup |
| Sacramento approaches | 4 | unchanged |
| Grapevine / I-5 mid-CA | 4 | unchanged |
| Hwy 99 / Stockton approaches | 4 | unchanged |
| Madera / Hwy 99 | 2 | unchanged |
| Tulare / Hwy 99 | 2 | unchanged |
| Bakersfield / Hwy 99 | 2 | unchanged |
| **Fresno / Hwy 99 · I-5** | **2** | **new** — Selma dedicated + EZ Trip #1277 Huron |
| Salinas / US-101 | 2 | unchanged |
| Weed / Yreka / I-5 | 2 | unchanged |
| Corning / Orland / I-5 | 3 | unchanged |
| Buttonwillow / Lost Hills / I-5 | 2 | unchanged |
| Wheeler Ridge / I-5 | 2 | unchanged |
| Santa Nella / I-5 | 3 | unchanged |
| Landfill / waste rows (sitewide) | 12 | unchanged |
| Dedicated / walk-up houses | 12–13 | Selma re-checked |
| CAT / truck-stop cards | 63–66 | +1 EZ Trip Huron (net after Love’s #830 dedupe) |
| Enforcement do-not-go | 2 | unchanged |

## What shipped tonight

**Fresno County** (`/fresno/`): new Fresno-focused page pairing the existing Selma dedicated house with newly verified EZ Trip #1277 Huron CAT (I-5 Exit 319). Redding / Anderson still has only one own-page CAT (TA #0057) — deferred. Willows / Red Bluff / Maxwell / Arbuckle: no Love’s, Pilot, or TA/Petro own location pages found. No Fresno / Fowler / Kingsburg / Clovis / Firebaugh / Coalinga Love’s or Pilot city store pages with CAT.

- **EZ Trip #1277 Huron** — CAT Scale on Pilot Flying J’s own Huron page (amenities + FAQ); new row
- **Selma Certified Public Scale** — re-verified on operator site + ScaleRegistry (existing; `last_checked` bumped)

Also removed a duplicate `loves-830-bakersfield` row that was already on tip (tip reported 130 rows / 129 unique). No invented hours/fees/livestock. Store pages list fuel/store 24/7; that is not a published CAT staffing schedule. CDFA Fresno (c=10) WAF-blocked (403).

## Sources used (this compile)

- EZ Trip #1277 Huron: https://locations.pilotflyingj.com/us/ca/huron/44779-s.-lassen-avenue
- Selma Certified Public Scale (re-verified): https://selmacertifiedpublicscale.com/
- ScaleRegistry CA public-weighing list: Selma (no second Fresno dedicated house)
- CAT Scale locator (linked, not republished): https://catscale.com/cat-scale-locator/
- CDFA Fresno c=10: WAF 403 tonight
- TA Redding #0057 (still alone for Redding / Anderson): https://www.ta-petro.com/location/ca/ta-redding/
- Love’s CA all-locations list: no Willows / Red Bluff / Maxwell / Arbuckle / Anderson / Fresno city stores
- Pilot Flying J CA city index: no Redding / Anderson / Willows / Fresno / Fowler / Kingsburg / Clovis

## Gaps / deferred

- Redding / Anderson mid-north I-5: only TA Redding #0057 own-page CAT — need a second stop before `/redding-anderson/`
- TA Livingston #0170 (Hwy 99 Exit 203, Merced County) — CAT on TA’s own page; deferred for a Merced corridor page
- Pilot Dealer #1399 Litchfield Park, AZ — CAT on Pilot’s own page; deferred Phoenix extension
- ONE9 #1424 Westley — CAT appears in Pilot page amenity JSON; visible HTML amenities incomplete tonight — re-check before Santa Nella / I-5 extension
- EZ Trip #1275 Madera Ave 12 — visible amenities still omit CAT (embedded JSON noise only); keep omitted from `/madera/`
- Third-party Fresno / Fowler / Traver CAT pins omitted (no operator own page)
- CDFA Merced / Kern / Shasta / Tehama / Glenn / Fresno facility grids still blocked
- Hours / fees / livestock unknown beyond store-listed 24h vs CAT staffing
- Temecula / Corona Love’s still deferred
- Ventura / Santa Barbara remain thin
- Gilroy Garlic Farm / King City / Prunedale third-party CAT still omitted
- Earlimart / Goshen / Visalia third-party CAT still omitted
