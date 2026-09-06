# WeighHere status — 5 Sep 2026

Compiled evening CT 5 Sep 2026.

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **91** | +8 tonight (4 Sacramento + 4 Grapevine) |
| Los Angeles County | 45 | unchanged |
| Orange County | 7 | unchanged |
| Inland Empire | 9 | unchanged (2 San Bernardino + 7 Riverside) |
| San Diego County | 8 | unchanged |
| Phoenix metro / Maricopa | 4 | unchanged |
| Central Valley | 6 | unchanged (Kern + Fresno + Merced) |
| **Sacramento approaches** | **4** | new (1 Yolo + 1 Colusa + 2 San Joaquin) |
| **Grapevine / I-5 mid-CA** | **8** | new (1 Kern Lebec + 1 Merced Santa Nella + 2 Stanislaus Patterson); total Kern now 7 |
| **Landfill / waste rows (sitewide)** | **12** | unchanged |
| Dedicated / walk-up houses | 11–12 | unchanged |
| CAT / truck-stop cards | 25–28 | +8 corridor CAT (4 Sacramento + 4 Grapevine) |
| Enforcement do-not-go | 2 | unchanged (I-405 Carson + San Onofre) |

## What shipped tonight

**Sacramento approaches** (`/sacramento/`): four CAT Scales verified on Pilot Flying J and Love's *own* location pages on the I-5 corridor that serves Sacramento:

- Pilot #168 Dunnigan (Yolo, I-5 Exit 554)
- Love's #652 Williams (Colusa, I-5 Exit 578)
- Flying J #617 Lodi (San Joaquin, I-5 Exit 485; address spelling *Thorton* as published on Pilot)
- Flying J #1017 Lathrop (San Joaquin, I-5 Exit 465)

No ScaleRegistry dedicated house for Sacramento / West Sacramento / Stockton. CDFA Sacramento / Yolo / Colusa / San Joaquin grids still WAF-blocked. Pilot Dealer #879 (El Centro Rd, Sacramento) omits CAT Scale on Pilot's amenity list — not listed. West Sacramento CAT #3390 only seen on third-party trucker pages — omitted.

**Grapevine / I-5 mid-CA corridor** (`/grapevine/`): four CAT Scales verified on Pilot Flying J and Love's *own* location pages on the Grapevine I-5 climb and mid–Central Valley I-5 corridor:

- Flying J #616 Lebec / Grapevine (Kern, I-5 Exit 205 — south-of-Bakersfield climb between LA and the Central Valley)
- Love's #441 Santa Nella (Merced, I-5 Exit 407 — mid–Central Valley between Grapevine and Tracy / Patterson)
- Love's #807 Patterson (Stanislaus, I-5 Exit 434 / Sperry Ave)
- Flying J #1080 Patterson (Stanislaus, I-5 Exit 434 / Sperry Ave)

No dedicated walk-up house on the Grapevine / mid-CA I-5 corridor. CDFA Kern / Merced / Stanislaus grids still WAF-blocked or not yet compiled. Nearby Ripon CA-99 and additional I-5 CAT stops noted in gaps, not duplicated tonight.

## Sources used (this compile)

**Sacramento:**
- Pilot #168 Dunnigan: https://locations.pilotflyingj.com/us/ca/dunnigan/30035-county-road-8
- Love's #652 Williams: https://www.loves.com/locations/ca/williams/loves-travel-stop-williams-652
- Flying J #617 Lodi: https://locations.pilotflyingj.com/us/ca/lodi/15100-thorton-rd
- Flying J #1017 Lathrop: https://locations.pilotflyingj.com/us/ca/lathrop/345-roth-rd

**Grapevine:**
- Flying J #616 Lebec: https://locations.pilotflyingj.com/us/ca/lebec/42810-frazier-mountain-park-rd
- Love's #441 Santa Nella: https://www.loves.com/locations/ca/santa-nella/loves-travel-stop-santa-nella-441
- Love's #807 Patterson: https://www.loves.com/locations/ca/patterson/loves-travel-stop-patterson-807
- Flying J #1080 Patterson: https://locations.pilotflyingj.com/us/ca/patterson/2275-sperry-ave

**Additional:**
- ScaleRegistry public scales: https://scaleregistry.com/public-scales.html
- CAT Scale locator (linked, not republished): https://catscale.com/cat-scale-locator/

Not used: Penske locator, Trucker Path, AllStays, Propane Atlas, MapQuest POIs, invented ticket fees, third-party CAT #3390 West Sacramento listings, third-party Ripon / additional I-5 CAT listings.

## Gaps (honest)

- **CDFA county grids** (Sacramento, Yolo, Colusa, San Joaquin, Kern, Fresno, Merced, Stanislaus, Ventura, etc.): still WAF-blocked from this host.
- **No Sacramento dedicated walk-up house** on ScaleRegistry (checked 5 Sep 2026).
- **No Grapevine / mid-CA I-5 corridor dedicated walk-up house** on ScaleRegistry or operator pages.
- **West Sacramento CAT #3390:** third-party only — omitted until CAT/operator page confirms.
- **Lat/lng:** missing for Pilot Dunnigan, Love's Williams, Flying J Lodi, Flying J Lathrop, Love's Santa Nella, Love's Patterson (and Selma, Merced, most landfill rows).
- **Nearby CAT not yet listed:** Flying J Ripon #618, ONE9 Lodi #1361, and other nearby I-5 / CA-99 CAT stops whose own pages may list CAT.
- **Walk-up weighmaster tickets at landfill gates:** still unverified.
- **Livestock:** unknown on most rows.
- **User reports form:** not built.
- **Affiliate IDs:** placeholder only.
- **Next geography candidates:** Ventura / Santa Barbara if CDFA loads; additional I-5 / CA-99 CAT stops; or newly verified dedicated houses.

## Blockers

None for shipping these two corridor pages. Do not treat them as complete Northern California inventory or as metro-Sacramento / Grapevine dedicated walk-up house lists.
