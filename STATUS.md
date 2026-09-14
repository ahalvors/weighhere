# WeighHere status — 13 Sep 2026

Compiled evening PT 13 Sep 2026 (nightly ship).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **114** | +3 (Pilot #1094 Tehachapi, Love’s #755 Boron, Pilot #200 Boron) |
| Los Angeles County | 46 | unchanged |
| Orange County | 7 | unchanged |
| Inland Empire (Riverside + San Bernardino filter) | 23 | unchanged |
| Coachella Valley / I-10 | 6 | unchanged |
| Ontario / I-10 West | 6 | unchanged |
| Imperial Valley / Hwy 86 | 3 | unchanged |
| Antelope Valley / Pearblossom | 4 | unchanged (Boron held-line removed; ships on Mojave) |
| **Mojave / Hwy 58** | **4** | new page (3 new CAT + Love’s #392 reused) |
| I-15 / High Desert | 4 | unchanged (Barstow cluster not re-added) |
| San Diego County | 8 | unchanged |
| Phoenix metro / Maricopa | 4 | unchanged |
| Central Valley (Kern+Fresno+Merced filter) | 11 | +3 Kern Hwy 58 CAT (also on Mojave page) |
| Sacramento approaches | 4 | unchanged |
| Grapevine / I-5 mid-CA | 4 | unchanged |
| Hwy 99 / Stockton approaches | 4 | unchanged |
| Madera / Hwy 99 | 2 | unchanged |
| Landfill / waste rows (sitewide) | 12 | unchanged |
| Dedicated / walk-up houses | 12–13 | unchanged |
| CAT / truck-stop cards | 47–50 | +3 Hwy 58 CAT |
| Enforcement do-not-go | 2 | unchanged |

## What shipped tonight

**Mojave / Hwy 58** (`/mojave/`): corridor page Tehachapi → Boron on CA-58. Three new CAT rows verified on operator own pages; Love’s #392 Tehachapi reused (already on Central Valley).

- **Pilot #1094 Tehachapi** — CAT on Pilot’s own CA-58 Exit 151 page (new row)
- **Love’s #392 Tehachapi** — existing Kern CAT (reused)
- **Love’s #755 Boron** — CAT Scales on Love’s own Hwy 58 Exit 199 page (new row)
- **Pilot #200 Boron** — CAT on Pilot’s own US-395 & CA-58 page (new row; previously held from Antelope Valley compile)

No invented hours/fees/livestock. Barstow I-15 cluster stays on `/i-15/` only.

## Sources used (this compile)

- Pilot #1094 Tehachapi: https://locations.pilotflyingj.com/us/ca/tehachapi/1668-e-tehachapi-blvd
- Love’s #392 Tehachapi: https://www.loves.com/locations/ca/tehachapi/loves-travel-stop-tehachapi-392 (prior verify; reused)
- Love’s #755 Boron: https://www.loves.com/locations/ca/boron/loves-travel-stop-boron-755
- Pilot #200 Boron: https://locations.pilotflyingj.com/us/ca/boron/5725-ca-58
- CAT Scale locator (linked, not republished): https://catscale.com/cat-scale-locator/
- CDFA Kern (c=15): still WAF-blocked from this compile path

## Gaps / deferred

- No ScaleRegistry dedicated walk-up house verified on Tehachapi / Mojave / Boron stretch
- CDFA Kern facility grid still blocked
- Hours / fees / livestock unknown beyond store-listed 24h vs CAT staffing
- Temecula / Corona Love’s still deferred (no own-page CAT confirmation used)
- Ventura / Santa Barbara remain thin (industrial/quarry/ag only)
- US-101 Salinas / Hwy 99 Tulare / I-5 Weed CAT rows researched earlier, not shipped tonight
- Bay Area / Half Moon Bay Ox Mountain landfill scale is disposal-oriented — not featured as a general ticket shop
