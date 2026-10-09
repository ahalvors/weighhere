# Adding a county or a handful of stations

One useful page per night. Do not rewrite the CSS or the LA template unless the schema changes.

## 1. Add rows to `data/stations.json`

Each station object:

```json
{
  "id": "kebab-case-unique",
  "name": "Operator name as published",
  "address": "Street",
  "city": "City",
  "state": "CA",
  "zip": "90000",
  "county": "los-angeles",
  "phone": "(000) 000-0000",
  "type": "dedicated_public",
  "certified_ticket_likely": "yes",
  "livestock": "unknown",
  "hours_24h": "unknown",
  "hours_notes": null,
  "walkup": "likely",
  "call_first": false,
  "do_not_go": false,
  "featured": true,
  "display_group": "dedicated",
  "rig": ["uhaul", "rv", "horse", "dump", "boat", "car", "ppm"],
  "notes": "Plain-language access notes. Not a DOT station.",
  "source_name": "CDFA DMS public scales — County",
  "source_url": "https://apps1.cdfa.ca.gov/publicscales/view.aspx?c=NN",
  "operator_url": null,
  "last_checked": "2026-08-30",
  "lat": 34.0,
  "lng": -118.0
}
```

**`type`:** `dedicated_public` | `cat` | `truck_stop` | `landfill` | `quarry` | `industrial` | `recycling` | `mill` | `enforcement`

**`display_group`:** `dedicated` (full cards, top of county page) | `cat` (CAT / truck-stop cards) | `call_first` (compact table) | `enforcement` (red box)

**`certified_ticket_likely`:** `yes` | `no` | `maybe` | `unknown`

**`rig` tags** (space-separated on the card for filters): `uhaul` `rv` `horse` `dump` `boat` `car` `ppm`

Leave `hours_notes`, `phone`, `zip`, `lat`/`lng` null rather than guessing. `livestock` stays `"unknown"` unless a primary source says otherwise.

`county` slug must match a page: `los-angeles`, `orange`, `riverside`, `san-bernardino` (Inland Empire page filters the last two), `san-diego`, `maricopa` (Phoenix page), or `pinal` (`/casa-grande-eloy/` filters specific station ids — Love’s #265 + Love’s #972), or `yuma` / additional `maricopa` I-8 rows (`/gila-bend-yuma/` filters specific station ids — Love’s #296 + Pilot #1243 Gila Bend + Love’s #349 Yuma; Phoenix metro keeps an explicit metro id list so Gila Bend does not appear there), or `la-paz` / additional `maricopa` I-10 west rows (`/quartzsite-ehrenberg/` filters specific station ids — TA #0225 Tonopah + Love’s #286 Quartzsite + Pilot #328 Quartzsite + Flying J #608 Ehrenberg; Phoenix metro keeps an explicit metro id list so Tonopah does not appear there; Blythe Public Scales stays on `/coachella/` only), or `mohave` (`/kingman/` filters specific station ids — Love’s #970 + TA #0094 + Flying J #610 + Petro #0315 Kingman), or `pima` / `cochise` (`/tucson-benson/` filters specific station ids — Pilot #593 Tucson + Pilot Express #1178 Tucson + Love’s #460 Benson + TA #0226 Willcox), or `coconino` / `navajo` (`/flagstaff-winslow/` filters specific station ids — Love’s #553 Williams + Pilot #180 Bellemont + Love’s #971 Winslow + Flying J #612 Winslow + TA #0246 Holbrook), or `yavapai` (`/mayer/` filters specific station ids — Pilot #1175 Mayer + Love’s #722 Mayer), or additional `mohave` / `clark` rows (`/white-hills/` filters specific station ids — TA Express White Hills #0292 + TA Express Henderson #0969; Kingman I-40 Mohave rows stay on `/kingman/` only), or additional `mohave` rows at I-40 / AZ-95 Exit 9 (`/lake-havasu/` filters specific station ids — Pilot #211 + Love’s #386 Lake Havasu City), or additional `clark` NV rows on I-15 (`/las-vegas/` filters specific station ids — Flying J #513 Jean + TA #0108 Las Vegas + Pilot #341 North Las Vegas + Petro #0331 North Las Vegas + Love’s #340 Apex; TA Express Henderson #0969 stays on `/white-hills/` only), or `washoe` / `storey` / `lyon` NV rows on I-80 (`/reno-sparks/` filters specific station ids — TA Sparks #0172 + Petro Sparks #0338 + ONE9 #1359 USA Parkway + Pilot #340 Fernley + Flying J #1005 Fernley), or `pershing` / `humboldt` / `elko` NV rows on I-80 (`/elko-winnemucca/` filters specific station ids — TA Mill City #0181 + Pilot #485 Winnemucca + Flying J #770 Winnemucca + ONE9 #387 Carlin + Petro Wells #0392), or `washington` / `iron` UT rows on I-15 (`/st-george-cedar-city/` filters specific station ids — Pilot #775 Saint George + Love’s #335 Cedar City + TA Express Parowan #0186), or `yolo` / `colusa` / `san-joaquin` (Sacramento approaches and Hwy 99 / Stockton pages filter specific station ids in those counties), or `madera` (Madera / Hwy 99 page), or `tulare` (`/tulare/` filters specific station ids — Love’s #382 + Flying J #1071), or Fresno County (`/fresno/` filters specific station ids — Selma dedicated + EZ Trip #1277 Huron), or Merced County (`/merced/` filters specific station ids — Highway 59 Scales + TA Livingston #0170), or `monterey` (`/salinas/` filters specific station ids — Love’s #898 + Pilot #237), or `siskiyou` (`/weed-yreka/` filters specific station ids — Pilot #137 Weed + EZ Trip #1343 Yreka), or `tehama` / `glenn` (`/corning-orland/` filters specific station ids — Love’s #410 Corning + Petro #0309 Corning + Pilot #1019 Orland), or `kern` rows on Buttonwillow / Lost Hills / I-5 (`/buttonwillow-lost-hills/` filters specific station ids — TA #0160 Buttonwillow + Love’s #230 Lost Hills; Lost Hills also appears on Central Valley) or Wheeler Ridge / I-5 (`/wheeler-ridge/` filters specific station ids — TA #0239 + Petro #0327), or `merced` rows on Santa Nella / I-5 (`/santa-nella/` filters specific station ids — TA #0163 + Petro #0346 + Love’s #441; Love’s #441 also appears on Grapevine), or I-15 / High Desert (`/i-15/`) which filters specific San Bernardino station ids, or Coachella Valley / I-10 (`/coachella/`) which filters specific `riverside` station ids (Blythe dedicated + I-10 CAT cluster; Rialto/Perris stay on Inland Empire only), or Ontario / I-10 West (`/ontario/`) which filters specific San Bernardino/Riverside station ids (Superior Colton + TA/Petro Ontario + Mira Loma + Pilot Colton + Flying J Fontana), or `imperial` (`/imperial/`) which filters specific station ids (Love’s Westmorland + Pilot Brawley + ONE9 El Centro), or Antelope Valley (`/antelope-valley/`) which filters specific Los Angeles station ids (Lancaster dedicated/walk-up + Palmdale CAT + Hi-Grade call-first), or `kern` / `fresno` / `merced` (Central Valley page filters those three; Lebec and Santa Nella also appear on Grapevine), or Grapevine / I-5 mid-CA (`/grapevine/`), Hwy 99 / Stockton (`/highway-99/`), and Madera / Hwy 99 (`/madera/`) which filter specific station ids (including `stanislaus` Patterson rows on Grapevine, Ripon/Lodi San Joaquin rows on Hwy 99). New counties need a new folder (step 3).

## 2. Rebuild

```bash
cd /workspace/weighhere
python3 build.py
```

County pages read JSON. Guide pages (`how-to-weigh-an-rv`, PPM, horse, 2,000 lb, public-vs-station, about) are copy in `build.py` — edit the `page_*` functions if the prose must change, then rebuild.

## 3. New county (nightly ship)

1. Fetch the CDFA county table (`view.aspx?c=NN`) with curl — WebFetch often strips the ASPX grid. Parse `ctl00_Main_gridScales` and the `infoWindow.setContent` markers for lat/lng.
2. Classify: dedicated public houses and CAT/truck stops as featured cards; plants/quarries/scrap/landfills as `call_first`; CHP/CVEF as `enforcement` / `do_not_go`.
3. Fetch **operator pages** (not Maps POI dumps) only for the dedicated houses you will recommend. Cite the URL. Do not invent hours.
4. Copy the Orange County pattern in `build.py`: a `*_body()` that filters `STATIONS` by `county`, plus `write(ROOT / "slug" / "index.html", ...)`.
5. Add the county to the `NAV` list, footer, `sitemap.xml`, and this table.
6. For CAT: link [catscale.com/cat-scale-locator](https://catscale.com/cat-scale-locator/). List only stops that appear on the state W&M list or that you verified on CAT/Pilot/Love’s **own** location page. Do not paste CAT’s national file into `stations.json`.
7. Update `STATUS.md` with counts, sources, and gaps. Set `last_checked` to today’s date (`YYYY-MM-DD`).
8. Commit generated HTML + JSON together so Netlify can serve even if `build.py` is skipped.

## 4. What not to do

- Do not scrape Penske publicscaleslocator.com, Trucker Path, or AllStays.
- Do not copy Propane Atlas or other competitor datasets.
- Do not mark livestock OK, 24-hour, or a fee unless the operator or CAT published it.
- Do not send people to a highway weigh station for a ticket.
- Do not give legal advice about overweight citations or PPM claims.
- Do not add affiliate programs other than Amazon Associates (tag `weighhere-20`) until the program is actually approved; U-Haul, Tractor Supply, Camping World stay "under consideration" on `/disclosure.html`.
- Do not invent ASINs or product IDs. Gear links are Amazon **search** links (`https://www.amazon.com/s?k=...&tag=weighhere-20`) with `rel="sponsored nofollow noopener"` and `target="_blank"`.

## 5. Towing gear box (Amazon Associates)

Every scale-listing page gets a "Towing gear that helps before you weigh" box of Amazon search links plus the visible line "As an Amazon Associate, WeighHere earns from qualifying purchases." (linked to `/disclosure.html`). You do not add it by hand: `write()` in `build.py` injects `gear_block()` into any page written with the `leaflet` head, just above `<div class="related">` (or at the end of the prose column if there is no Related list). So a new county page that follows step 3 — `write(..., county_body(), leaflet)` — inherits it automatically. Pass `gear=False` to opt a page out, or `gear=True` to force it on a page without a map. Edit the items in `GEAR_ITEMS` in `build.py`, never in generated HTML.

## 6. Optional map

If `lat` and `lng` are present, county pages plot Leaflet + OSM. Missing coords just omit the pin. The list is the product.
