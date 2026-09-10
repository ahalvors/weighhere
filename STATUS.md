# WeighHere status — 9 Sep 2026

Compiled evening PT 9 Sep 2026 (nightly ship).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **103** | +6 (Blythe dedicated + 3 Coachella Valley CAT + Rialto + Perris); Love’s Coachella coords refreshed |
| Los Angeles County | 45 | unchanged |
| Orange County | 7 | unchanged |
| Inland Empire (Riverside + San Bernardino filter) | 19 | +6 new Riverside/SB rows vs prior IE view (was 13) |
| **Coachella Valley / I-10** | **6** | new (Blythe dedicated + 4 CAT + Blythe landfill call-first) |
| I-15 / High Desert | 4 | unchanged |
| San Diego County | 8 | unchanged |
| Phoenix metro / Maricopa | 4 | unchanged |
| Central Valley (Kern+Fresno+Merced filter) | 8 | unchanged |
| Sacramento approaches | 4 | unchanged |
| Grapevine / I-5 mid-CA | 4 | unchanged |
| Hwy 99 / Stockton approaches | 4 | unchanged |
| Madera / Hwy 99 | 2 | unchanged |
| **Landfill / waste rows (sitewide)** | **12** | unchanged |
| Dedicated / walk-up houses | 12–13 | + Blythe Public Scales |
| CAT / truck-stop cards | 36–39 | +5 new CAT rows |
| Enforcement do-not-go | 2 | unchanged (I-405 Carson + San Onofre) |

## What shipped tonight

**Coachella Valley / I-10 East** (`/coachella/`): CDFA Riverside (c=33) loaded this compile. Dedicated house + four CAT Scales on the I-10 Coachella Valley corridor:

- **Blythe Public Scales, LLC** (dedicated) — CDFA Riverside public-scales list; coords from CDFA pin; hours/fees not published
- Love’s #207 Coachella — already listed; lat/lng set from CDFA Riverside pin
- Flying J #765 Thousand Palms — CAT on Pilot’s own page; FAQ confirms
- Pilot #307 North Palm Springs — CAT on Pilot’s own page; FAQ confirms
- Pilot Dealer #1384 Mecca — CAT Scale on Pilot amenities list
- Blythe Landfill (call-first) — already in JSON; shown on this corridor page

Also appended for **Inland Empire** (county filter; not on Coachella page):

- Pilot #1328 Rialto (CA-210 Exit 68) — CAT; FAQ confirms
- Pilot Dealer #1458 Perris (I-215 / Cajalco) — CAT among amenities

## Sources used (this compile)

- CDFA Riverside: https://apps1.cdfa.ca.gov/publicscales/view.aspx?c=33
- Love’s #207 Coachella: https://www.loves.com/locations/ca/coachella/loves-travel-stop-coachella-207
- Flying J #765 Thousand Palms: https://locations.pilotflyingj.com/us/ca/thousand-palms/72235-varner-rd
- Pilot #307 North Palm Springs: https://locations.pilotflyingj.com/us/ca/north-palm-springs/6605-n-indian-canyon-dr
- Pilot Dealer #1384 Mecca: https://locations.pilotflyingj.com/us/ca/mecca/90480-66th-ave
- Pilot #1328 Rialto: https://locations.pilotflyingj.com/us/ca/rialto/2325-sierra-lakes-pkwy
- Pilot Dealer #1458 Perris: https://locations.pilotflyingj.com/us/ca/perris/23261-cajalco-expressway
- Riverside County Waste Resources: https://rcwaste.org/routine-waste
- ScaleRegistry public scales: https://scaleregistry.com/public-scales.html
- CAT Scale locator (linked, not republished): https://catscale.com/cat-scale-locator/

Not used: Penske locator, Trucker Path, AllStays, Propane Atlas, MapQuest POIs, invented ticket fees, third-party-only CAT listings (TA Coachella).

## Gaps (honest)

- **CDFA San Bernardino (c=36)** and most other county grids: still WAF-blocked from this host. Riverside loaded this compile.
- **Blythe Public Scales:** hours, fees, livestock, and operator site still unknown / unpublished on CDFA.
- **TA Coachella:** third-party CAT directories only — omitted.
- **Temecula Love’s / other I-15 south CAT:** no Love’s/Pilot own-page CAT confirmation used tonight — deferred.
- **Ventura:** CDFA industrial call-first only — deferred as thin for walk-up users.
- **Flying J Mira Loma / Jurupa Valley:** still omitted until Pilot’s own page is the primary source here.
- **Walk-up weighmaster tickets at landfill gates:** still unverified.
- **Livestock:** unknown on most rows (including new ones).
- **User reports form:** not built.
- **Affiliate IDs:** placeholder only.
- **Next geography candidates:** Ventura / Santa Barbara if a dedicated or strong walk-up row appears; I-15 south (Temecula/Corona) CAT on operator pages; more CDFA counties if grids load.

## Blockers

None for shipping this corridor page. Do not treat it as a complete Riverside County inventory or as a promise of 24h CAT staffing.
