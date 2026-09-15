# WeighHere status — 14 Sep 2026

Compiled evening PT 14 Sep 2026 (nightly ship).

## Listing counts

| Bucket | Count | Notes |
|---|---|---|
| **Total rows in `data/stations.json`** | **116** | +2 (Love’s #382 Tulare, Flying J #1071 Tulare) |
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
| Central Valley (Kern+Fresno+Merced filter) | 11 | unchanged |
| Sacramento approaches | 4 | unchanged |
| Grapevine / I-5 mid-CA | 4 | unchanged |
| Hwy 99 / Stockton approaches | 4 | unchanged |
| Madera / Hwy 99 | 2 | unchanged |
| **Tulare / Hwy 99** | **2** | new page (Love’s #382 + Flying J #1071) |
| Landfill / waste rows (sitewide) | 12 | unchanged |
| Dedicated / walk-up houses | 12–13 | unchanged |
| CAT / truck-stop cards | 49–52 | +2 Tulare Exit 85 |
| Enforcement do-not-go | 2 | unchanged |

## What shipped tonight

**Tulare / Hwy 99** (`/tulare/`): corridor page at CA-99 Exit 85 in Tulare. Two new CAT rows verified on operator own pages.

- **Love’s #382 Tulare** — CAT Scales on Love’s own Hwy 99 / Blackstone page (new row)
- **Flying J #1071 Tulare** — CAT Scale on Pilot Flying J’s own Paige Ave / Exit 85 page (new row)

No invented hours/fees/livestock. Earlimart / Goshen / Visalia third-party CAT rows omitted. CDFA Tulare (c=54) WAF-blocked.

## Sources used (this compile)

- Love’s #382 Tulare: https://www.loves.com/locations/ca/tulare/loves-travel-stop-tulare-382
- Flying J #1071 Tulare: https://locations.pilotflyingj.com/us/ca/tulare/979-e-paige-ave
- CAT Scale locator (linked, not republished): https://catscale.com/cat-scale-locator/
- CDFA Tulare (c=54): still WAF-blocked from this compile path

## Gaps / deferred

- No ScaleRegistry dedicated walk-up house verified in Tulare / Visalia
- CDFA Tulare facility grid still blocked
- Hours / fees / livestock unknown beyond store-listed 24h vs CAT staffing
- Earlimart Big B’s / Goshen Travel Plaza appear on third-party CAT lists only — omitted
- Temecula / Corona Love’s still deferred (no own-page CAT confirmation used)
- Ventura / Santa Barbara remain thin (industrial/quarry/ag only)
- US-101 Salinas / I-5 Weed CAT rows researched (Pilot #237 Salinas, Pilot #137 Weed) — not shipped tonight (single-stop corridors)
- Bay Area / Half Moon Bay Ox Mountain landfill scale is disposal-oriented — not featured as a general ticket shop
