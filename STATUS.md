# WeighHere status — 4 Sep 2026

Compiled evening CT 4 Sep 2026 (routine fire ~10:05 PM CT).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **83** | +4 Sacramento-approach CAT stops |
| Los Angeles County | 45 | unchanged |
| Orange County | 7 | unchanged |
| Inland Empire | 9 | unchanged (2 San Bernardino + 7 Riverside) |
| San Diego County | 8 | unchanged |
| Phoenix metro / Maricopa | 4 | unbroken |
| Central Valley | 6 | unchanged |
| **Sacramento approaches** | **4** | new (1 Yolo + 1 Colusa + 2 San Joaquin) |
| **Landfill / waste rows (sitewide)** | **12** | unchanged |
| Dedicated / walk-up houses | 11–12 | unchanged |
| CAT / truck-stop cards | 17–20 | +4 corridor CAT |
| Enforcement do-not-go | 2 | unchanged (I-405 Carson + San Onofre) |

## What shipped tonight

**Sacramento approaches** (`/sacramento/`): four CAT Scales verified on Pilot Flying J and Love’s *own* location pages on the I-5 corridor that serves Sacramento:

- Pilot #168 Dunnigan (Yolo, I-5 Exit 554)
- Love’s #652 Williams (Colusa, I-5 Exit 578)
- Flying J #617 Lodi (San Joaquin, I-5 Exit 485; address spelling *Thorton* as published on Pilot)
- Flying J #1017 Lathrop (San Joaquin, I-5 Exit 465)

No ScaleRegistry dedicated house for Sacramento / West Sacramento / Stockton. CDFA Sacramento / Yolo / Colusa / San Joaquin grids still WAF-blocked. Pilot Dealer #879 (El Centro Rd, Sacramento) omits CAT Scale on Pilot’s amenity list — not listed. West Sacramento CAT #3390 only seen on third-party trucker pages — omitted. Nearby Ripon / Santa Nella / Patterson CAT stops noted in gaps, not duplicated tonight.

## Sources used (this compile)

- Pilot #168 Dunnigan: https://locations.pilotflyingj.com/us/ca/dunnigan/30035-county-road-8
- Love’s #652 Williams: https://www.loves.com/locations/ca/williams/loves-travel-stop-williams-652
- Flying J #617 Lodi: https://locations.pilotflyingj.com/us/ca/lodi/15100-thorton-rd
- Flying J #1017 Lathrop: https://locations.pilotflyingj.com/us/ca/lathrop/345-roth-rd
- ScaleRegistry public scales: https://scaleregistry.com/public-scales.html
- CAT Scale locator (linked, not republished): https://catscale.com/cat-scale-locator/

Not used: Penske locator, Trucker Path, AllStays, Propane Atlas, MapQuest POIs, invented ticket fees, third-party CAT #3390 West Sacramento listings.

## Gaps (honest)

- **CDFA county grids** (Sacramento, Yolo, Colusa, San Joaquin, Kern, Fresno, Merced, Ventura, etc.): still WAF-blocked from this host.
- **No Sacramento dedicated walk-up house** on ScaleRegistry.
- **West Sacramento CAT #3390:** third-party only — omitted until CAT/operator page confirms.
- **Lat/lng:** still missing for Love’s Williams (and Selma, Merced, most landfill rows).
- **Nearby CAT not yet listed:** Flying J Ripon #618, ONE9 Lodi #1361, Love’s Santa Nella #441, Love’s Patterson #807, Flying J Lebec #616 (Grapevine), etc.
- **Walk-up weighmaster tickets at landfill gates:** still unverified.
- **Livestock:** unknown on most rows.
- **User reports form:** not built.
- **Affiliate IDs:** placeholder only.
- **Next geography candidates:** Ventura / Santa Barbara if CDFA loads; Grapevine Flying J Lebec + more I-5/I-15 CAT; or newly verified dedicated houses.

## Blockers

None for shipping this corridor page. Do not treat it as a complete Northern California inventory or as a metro-Sacramento walk-up house list.
