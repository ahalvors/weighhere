# WeighHere status — 7 Sep 2026

Compiled evening PT 7 Sep 2026 (nightly ship).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **93** | +2 Madera Hwy 99 CAT stops |
| Los Angeles County | 45 | unchanged |
| Orange County | 7 | unchanged |
| Inland Empire | 9 | unchanged (2 San Bernardino + 7 Riverside) |
| San Diego County | 8 | unchanged |
| Phoenix metro / Maricopa | 4 | unchanged |
| Central Valley (Kern+Fresno+Merced filter) | 8 | unchanged (Lebec + Santa Nella also on Grapevine) |
| Sacramento approaches | 4 | unchanged |
| Grapevine / I-5 mid-CA | 4 | unchanged |
| Hwy 99 / Stockton approaches | 4 | unchanged |
| **Madera / Hwy 99** | **2** | new (both Madera County) |
| **Landfill / waste rows (sitewide)** | **12** | unchanged |
| Dedicated / walk-up houses | 11–12 | unchanged |
| CAT / truck-stop cards | 27–30 | +2 Madera corridor CAT |
| Enforcement do-not-go | 2 | unchanged (I-405 Carson + San Onofre) |

## What shipped tonight

**Madera / Hwy 99** (`/madera/`): two CAT Scales verified on Love’s and Pilot Flying J *own* location pages at the north-Madera CA-99 exits:

- Love’s #736 Madera (CA-99 Exit 157 / Avenue 17) — CAT Scales on Love’s page
- Pilot #365 Madera (CA-99 Exit 159 / Ave 18 1/2) — CAT Scale on Pilot’s page; coords from Pilot page

No ScaleRegistry dedicated house in Madera. CDFA Madera grid still WAF-blocked. EZ Trip #1275 (Ave 12) has no CAT amenity on Pilot’s page — omitted. Deferred from last night’s Hwy 99 / Stockton ship; kept as its own short corridor page rather than bloating `/highway-99/`.

## Sources used (this compile)

- Love’s #736 Madera: https://www.loves.com/locations/ca/madera/loves-travel-stop-madera-736
- Pilot #365 Madera: https://locations.pilotflyingj.com/us/ca/madera/22717-ave-18-1/2
- ScaleRegistry public scales: https://scaleregistry.com/public-scales.html
- CAT Scale locator (linked, not republished): https://catscale.com/cat-scale-locator/
- CDFA Madera (`view.aspx?c=20`): WAF blocked (HTTP 403)

Not used: Penske locator, Trucker Path, AllStays, Propane Atlas, MapQuest POIs, invented ticket fees, third-party-only CAT listings.

## Gaps (honest)

- **CDFA county grids** (Madera, Fresno, San Joaquin, Stanislaus, Kern, Merced, Sacramento corridor, Ventura, etc.): still WAF-blocked from this host.
- **Lat/lng:** still missing for Love’s Madera #736, Love’s Ripon, Love’s Lodi, Love’s Santa Nella, Love’s Patterson, Love’s Williams, Selma, Merced, most landfill rows.
- **Modesto Truck Plaza (Hwy 99 Exit 223) / Vanco Stockton (I-5 Exit 471):** third-party CAT directories only — omitted.
- **EZ Trip #1275 Madera (Ave 12):** Pilot’s own page lists no CAT amenity — omitted.
- **ONE9 #1424 Westley:** no CAT amenity on Pilot’s page — omitted.
- **West Sacramento CAT #3390:** still third-party only.
- **Walk-up weighmaster tickets at landfill gates:** still unverified.
- **Livestock:** unknown on most rows.
- **User reports form:** not built.
- **Affiliate IDs:** placeholder only.
- **Next geography candidates:** Ventura / Santa Barbara if CDFA loads; I-15 corridor CAT stops verified on Pilot/Love’s own pages; other Hwy 99 CAT between Madera and Ripon; or newly verified dedicated houses.

## Blockers

None for shipping this corridor page. Do not treat it as a complete Madera County inventory or as a Madera dedicated-house list.
