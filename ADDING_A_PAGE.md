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

`county` slug must match a page: `los-angeles`, `orange`, `riverside`, `san-bernardino` (Inland Empire page filters the last two), `san-diego`, `maricopa` (Phoenix page), or `kern` / `fresno` / `merced` (Central Valley page filters those three). New counties need a new folder (step 3).

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
- Do not put live affiliate IDs on the page until the program is actually approved; keep the About placeholder.

## 5. Optional map

If `lat` and `lng` are present, county pages plot Leaflet + OSM. Missing coords just omit the pin. The list is the product.
