# WeighHere status — 3 Sep 2026

Compiled evening PT 3 Sep 2026.

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **79** | unchanged (guide page, no new station rows) |
| Los Angeles County | 45 | unchanged |
| Orange County | 7 | unchanged |
| Inland Empire | 9 | unchanged (2 San Bernardino + 7 Riverside) |
| San Diego County | 8 | unchanged |
| Phoenix metro / Maricopa | 4 | unchanged |
| Central Valley | 6 | unchanged |
| **Landfill / waste rows (sitewide)** | **12** | re-checked Riverside + Miramar hours; table on new guide |
| Dedicated / walk-up houses | 11–12 | unchanged |
| CAT / truck-stop cards | 13–16 | unchanged |
| Enforcement do-not-go | 2 | unchanged (I-405 Carson + San Onofre) |

## What shipped tonight

**Dump trailer & landfill scales guide** (`/dump-trailer/`): briefed guide page (deferred after Phoenix / Central Valley geography ships). Explains dedicated house vs CAT vs landfill gate; call-ahead script; table of all 12 landfill/waste rows already in `stations.json`.

Re-verified tonight (no hour changes from prior compile):

- Riverside County Waste Resources landfill gate hours — Badlands, Blythe, Desert Center, Lamb Canyon, Oasis, El Sobrante (WM) still match `rcwaste.org/routine-waste`.
- Miramar Landfill — Mon–Sat 7 a.m.–4 p.m.; self-dumping until 4:30 p.m.; closed Sundays — matches City of San Diego page.
- CAT how-to — 2,000 lb floor + truck/trailer platform positioning still published.

No new station rows added. Transfer stations listed as courtesy on the Riverside page (Coachella, Edom Hill, Moreno Valley, Perris, Nelson, mountain-community sites) were **not** added — they are privately operated disposal sites without a published civilian weighmaster-ticket claim on the county page.

## Sources used (this compile)

- Riverside County Waste Resources locations/hours: https://rcwaste.org/routine-waste
- City of San Diego Miramar Landfill & Greenery: https://www.sandiego.gov/environmental-services/miramar
- CAT Scale how-to: https://catscale.com/how-to-weigh/
- CAT Scale locator (linked, not republished): https://catscale.com/cat-scale-locator/
- Existing CDFA / ScaleRegistry / operator citations already on landfill and dedicated rows

Not used: Penske locator, Trucker Path, AllStays, Propane Atlas, MapQuest POIs, invented ticket fees.

## Gaps (honest)

- **Walk-up weighmaster tickets at landfill gates:** still unverified everywhere we list them.
- **CDFA county grids** (Kern, Fresno, Merced, Ventura, San Joaquin, etc.): still WAF-blocked from this host.
- **San Bernardino County landfill hours table:** still not a usable public list in our compile — omitted.
- **Riverside private transfer stations:** phones published by county as courtesy; hours/rates "call facility" — not added as ticket shops.
- **Lat/lng:** still missing for Selma and Merced (and most landfill rows).
- **Livestock:** unknown on landfill and most dedicated rows.
- **User reports form:** not built.
- **Affiliate IDs:** placeholder only.
- **Next geography candidates:** Ventura / Santa Barbara / Sacramento area if CDFA loads; or newly verified CAT stops on I-5 / I-15.

## Blockers

None for shipping this guide. Do not treat the landfill table as a complete Southern California dump-site inventory or as ticket-shop endorsements.
