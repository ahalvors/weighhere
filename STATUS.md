# WeighHere status — 11 Sep 2026

Compiled evening PT 11 Sep 2026 (nightly ship).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **110** | +3 (Love’s Westmorland, Pilot Brawley, ONE9 El Centro) |
| Los Angeles County | 45 | unchanged |
| Orange County | 7 | unchanged |
| Inland Empire (Riverside + San Bernardino filter) | 23 | unchanged |
| Coachella Valley / I-10 | 6 | unchanged |
| Ontario / I-10 West | 6 | unchanged |
| **Imperial Valley / Hwy 86** | **3** | new (Love’s #749, Pilot #1132, ONE9 #1447) |
| I-15 / High Desert | 4 | unchanged |
| San Diego County | 8 | unchanged |
| Phoenix metro / Maricopa | 4 | unchanged |
| Central Valley (Kern+Fresno+Merced filter) | 8 | unchanged |
| Sacramento approaches | 4 | unchanged |
| Grapevine / I-5 mid-CA | 4 | unchanged |
| Hwy 99 / Stockton approaches | 4 | unchanged |
| Madera / Hwy 99 | 2 | unchanged |
| Landfill / waste rows (sitewide) | 12 | unchanged |
| Dedicated / walk-up houses | 12–13 | unchanged (no Imperial dedicated) |
| CAT / truck-stop cards | 43–46 | +3 new Imperial CAT rows |
| Enforcement do-not-go | 2 | unchanged |

## What shipped tonight

**Imperial Valley / Hwy 86** (`/imperial/`): three CAT Scales verified on Love’s and Pilot Flying J own location pages. CDFA Imperial (c=13) WAF-blocked this compile — no invented dedicated houses.

- **Love’s #749 Westmorland** — CAT on Love’s own page (Hwy 86 / Martin Rd)
- **Pilot #1132 Brawley** — CAT on Pilot’s own page (Ben Hulse Hwy / Hwy 111–78)
- **ONE9 Dealer #1447 El Centro** — CAT on Pilot Flying J ONE9 page (I-8 Exit 115 / Wake Ave)

Blythe Public Scales (dedicated) remains on the Coachella Valley / I-10 page. No ScaleRegistry dedicated Imperial house used tonight.

## Sources used (this compile)

- Love’s #749 Westmorland: https://www.loves.com/locations/ca/westmorland/loves-travel-stop-westmorland-749
- Pilot #1132 Brawley: https://locations.pilotflyingj.com/us/ca/brawley/234-ben-hulse-hwy
- ONE9 #1447 El Centro: https://locations.pilotflyingj.com/us/ca/el-centro/550-wake-ave
- CDFA Imperial (c=13): https://apps1.cdfa.ca.gov/publicscales/view.aspx?c=13 — **WAF-blocked** this compile
- CAT Scale locator (linked, not republished): https://catscale.com/cat-scale-locator/
- ScaleRegistry public scales: https://scaleregistry.com/public-scales.html (no Imperial dedicated house used)

## Gaps / deferred

- CDFA Imperial c=13 still WAF-blocked from this box — no dedicated Imperial walk-up house from CDFA tonight
- No ScaleRegistry dedicated Imperial Valley house featured
- Livestock / fees unknown on all three new CAT rows
- CAT staffing: store listed 24h ≠ published scale schedule
- ONE9 dealer hours after dark — call ahead
- Temecula / Corona Love’s still deferred (no own-page CAT confirmation used)
- Ventura / Santa Barbara remain thin (industrial/quarry/ag only)
