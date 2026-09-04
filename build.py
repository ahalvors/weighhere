#!/usr/bin/env python3
"""Generate WeighHere static pages from data/stations.json."""
from __future__ import annotations

import json
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / "data/stations.json").read_text())
STATIONS = DATA["stations"]
CHECKED = DATA["generated"]  # 2026-09-03
CHECKED_HUMAN = "3 Sep 2026"

NAV = [
    ("/", "LA County", "la"),
    ("/orange-county/", "Orange County", "oc"),
    ("/inland-empire/", "Inland Empire", "ie"),
    ("/san-diego/", "San Diego County", "sd"),
    ("/phoenix/", "Phoenix metro", "phx"),
    ("/central-valley/", "Central Valley", "cv"),
    ("/how-to-weigh-an-rv/", "Weigh an RV", "rv"),
    ("/ppm-dity-southern-california/", "PPM / DITY", "ppm"),
    ("/horse-trailer/", "Horse trailer", "horse"),
    ("/dump-trailer/", "Dump trailer", "dump"),
    ("/cat-2000-lb-minimum/", "2,000 lb minimum", "catmin"),
    ("/public-scale-vs-weigh-station/", "Scale vs weigh station", "vs"),
    ("/about.html", "About", "about"),
]


def e(s):
    return html.escape("" if s is None else str(s), quote=True)


def maps_url(st):
    q = f"{st['address']}, {st['city']}, {st['state']} {st.get('zip') or ''}"
    return "https://maps.google.com/?q=" + html.escape(q, quote=True).replace(" ", "+")


def badge_type(st):
    t = st["type"]
    labels = {
        "dedicated_public": ("Dedicated public", "badge-ok"),
        "cat": ("CAT Scale", "badge-cat"),
        "truck_stop": ("Truck stop", "badge"),
        "landfill": ("Landfill / waste", "badge-call"),
        "quarry": ("Quarry / materials", "badge-call"),
        "industrial": ("Industrial / plant", "badge-call"),
        "recycling": ("Recycling / scrap", "badge-call"),
        "mill": ("Mill / grain", "badge-call"),
        "enforcement": ("Enforcement — do not go", "badge-warn"),
    }
    label, cls = labels.get(t, (t, "badge"))
    return f'<span class="badge {cls}">{e(label)}</span>'


def cert_label(v):
    return {"yes": "Likely (licensed weighmaster list / CAT)", "no": "No — not a ticket scale", "maybe": "Only if they accept you", "unknown": "Unknown"}.get(v, v)


def header(current, rel, title, description, extra_head=""):
    nav_items = []
    for href, label, key in NAV:
        cur = ' aria-current="page"' if key == current else ""
        nav_items.append(f'<li><a href="{e(href)}"{cur}>{e(label)}</a></li>')
    leaflet = ""
    if extra_head:
        leaflet = extra_head
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&family=IBM+Plex+Serif:wght@600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{rel}css/site.css">
{leaflet}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="mast">
  <div class="wrap mast-inner">
    <a class="brand" href="/">WeighHere<span>Public scales for U-Hauls, RVs, horse trailers, and PPM loads</span></a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
    <nav class="site-nav" id="site-nav">
      <ul>
        {''.join(nav_items)}
      </ul>
    </nav>
  </div>
</header>
<div class="stripe"><div class="wrap">Call ahead. Hours, fees, and walk-up rules change. WeighHere is not CDFA, CAT, or CHP.</div></div>
"""


def footer(rel="."):
    return f"""
<footer class="site">
  <div class="wrap">
    <nav aria-label="Footer">
      <ul>
        <li><a href="/">LA County</a></li>
        <li><a href="/orange-county/">Orange County</a></li>
        <li><a href="/inland-empire/">Inland Empire</a></li>
        <li><a href="/san-diego/">San Diego County</a></li>
        <li><a href="/phoenix/">Phoenix metro</a></li>
        <li><a href="/central-valley/">Central Valley</a></li>
        <li><a href="/how-to-weigh-an-rv/">How to weigh an RV</a></li>
        <li><a href="/ppm-dity-southern-california/">PPM / DITY</a></li>
        <li><a href="/horse-trailer/">Horse trailer</a></li>
        <li><a href="/dump-trailer/">Dump trailer / landfill</a></li>
        <li><a href="/cat-2000-lb-minimum/">CAT 2,000 lb minimum</a></li>
        <li><a href="/public-scale-vs-weigh-station/">Public scale vs weigh station</a></li>
        <li><a href="/about.html">About &amp; sources</a></li>
      </ul>
    </nav>
    <p>Independent directory compiled {CHECKED_HUMAN} from public CDFA county tables, CAT Scale public pages, operator sites, county/facility pages, ScaleRegistry, Caltrans, ADOT, and Arizona Department of Agriculture weighmaster licensing pages. Missing hours, fees, or livestock policy are left blank on purpose. CDFA’s own disclaimer: the Division makes no claims, promises, or guarantees about the absolute accuracy, completeness, or adequacy of the information on its public-scales list.</p>
    <p>This site does not give legal advice about overweight citations, who must stop at an open CHP scale, or PPM claim reimbursement. Confirm with the scale, your Transportation Office, or CHP Commercial Vehicle Section as needed.</p>
    <p>&copy; {CHECKED[:4]} WeighHere · <a href="/about.html">How we compile listings</a></p>
  </div>
</footer>
<script src="{rel}js/site.js"></script>
</body>
</html>
"""


def card(st):
    phone = ""
    if st.get("phone"):
        tel = "".join(ch for ch in st["phone"] if ch.isdigit())
        phone = f'<p class="phone"><a href="tel:+1{tel}">{e(st["phone"])}</a></p>'
    hours = st.get("hours_notes") or "Hours not verified — call."
    live = "Unknown — we do not invent livestock policy."
    h24 = {
        "unknown": "Unknown",
        "store_listed_24h": "Travel center listed 24h; confirm scale staffing",
        "no": "No",
        "yes": "Yes",
    }.get(st.get("hours_24h"), st.get("hours_24h") or "Unknown")
    ticket = cert_label(st.get("certified_ticket_likely"))
    src_name = st.get("source_name") or "Source"
    src = st.get("source_url") or "#"
    op = ""
    if st.get("operator_url"):
        op = f' · <a href="{e(st["operator_url"])}">Operator page</a>'
    zipc = st.get("zip") or ""
    addr = f"{st['address']}, {st['city']}, {st['state']} {zipc}".strip()
    rig = " ".join(st.get("rig") or [])
    call = '<span class="badge badge-call">Call first</span>' if st.get("call_first") else '<span class="badge badge-ok">Walk-up more likely</span>'
    extra_badge = '<span class="badge">Not a DOT station</span>'
    if st.get("do_not_go"):
        call = '<span class="badge badge-warn">Do not go for a ticket</span>'
        extra_badge = '<span class="badge badge-warn">CHP enforcement — not a ticket window</span>'
    return f"""
<article class="card" data-rig="{e(rig)}" data-type="{e(st['type'])}" id="{e(st['id'])}">
  <div class="badges">{badge_type(st)}{call}{extra_badge}</div>
  <h3>{e(st['name'])}</h3>
  <p class="addr">{e(addr)} · <a href="{maps_url(st)}">Map</a></p>
  {phone}
  <dl>
    <dt>Certified ticket</dt><dd>{e(ticket)}</dd>
    <dt>Livestock</dt><dd>{e(live)}</dd>
    <dt>24-hour</dt><dd>{e(h24)}</dd>
    <dt>Hours / access</dt><dd>{e(hours)}</dd>
  </dl>
  <p>{e(st.get('notes') or '')}</p>
  <p class="src">Source: <a href="{e(src)}">{e(src_name)}</a>{op} · Last checked {e(st.get('last_checked'))}</p>
</article>
"""


def compact_row(st):
    phone = e(st.get("phone") or "—")
    zipc = st.get("zip") or ""
    return f"""<tr data-rig="dump" id="{e(st['id'])}">
  <td><strong>{e(st['name'])}</strong><br>{e(st['address'])}, {e(st['city'])} {e(zipc)}</td>
  <td>{phone}</td>
  <td>{e(st['type'].replace('_',' '))}</td>
  <td>Call first</td>
</tr>"""


def map_script(stations):
    pts = []
    for s in stations:
        if s.get("lat") is None or s.get("lng") is None:
            continue
        pts.append({
            "name": s["name"],
            "city": s["city"],
            "type": s["type"] if s["type"] != "enforcement" else "enforcement",
            "lat": s["lat"],
            "lng": s["lng"],
        })
    return "<script>window.WEIGHHERE_POINTS = " + json.dumps(pts) + ";</script>\n"


LEAFLET = """<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin="">
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>
"""


def filters():
    return """
<div class="filters" data-filters>
  <button type="button" data-filter="all" aria-pressed="true">All listed</button>
  <button type="button" data-filter="uhaul">U-Haul / moving truck</button>
  <button type="button" data-filter="rv">RV / fifth-wheel</button>
  <button type="button" data-filter="horse">Horse trailer</button>
  <button type="button" data-filter="ppm">PPM / DITY</button>
  <button type="button" data-filter="car">Car / light trailer (under 2,000 lb)</button>
  <button type="button" data-filter="dump">Dump / boat trailer</button>
</div>
<p class="notice-small">Filters hide cards, not industrial rows. CAT will not weigh under 2,000 lb — use a dedicated house for cars and empty utility trailers.</p>
"""


def la_body():
    la = [s for s in STATIONS if s["county"] == "los-angeles"]
    dedicated = [s for s in la if s["display_group"] == "dedicated"]
    cat = [s for s in la if s["display_group"] == "cat"]
    call = [s for s in la if s["display_group"] == "call_first"]
    enf = [s for s in la if s["display_group"] == "enforcement"]
    cards_d = "\n".join(card(s) for s in dedicated)
    cards_c = "\n".join(card(s) for s in cat)
    rows = "\n".join(compact_row(s) for s in sorted(call, key=lambda x: (x["city"], x["name"])))
    enf_html = "\n".join(card(s) for s in enf)
    return f"""
<main id="main">
<section class="page-head">
  <div class="wrap">
    <p class="kicker">Los Angeles County · listings checked {CHECKED_HUMAN}</p>
    <h1>Public scales that will weigh a U-Haul, RV, or horse trailer</h1>
    <p class="lede">Google mixes CAT Scales with highway cop scales. CAT is built for truckers — 2,000 lb minimum, no corner weights. CDFA publishes names and phones but not hours, fees, or whether a plant will take a walk-up. This page answers: will this scale weigh <em>your</em> rig, today, with a ticket you can actually use.</p>
    <p class="meta-line">{len(dedicated)} dedicated / walk-up-more-likely houses · {len(cat)} CAT or truck-stop scales · {len(call)} call-first industrial listings from CDFA · 1 enforcement station you should not use for a ticket.</p>
  </div>
</section>
<div class="wrap prose">
  <div class="box box-ok">
    <h2>Start here</h2>
    <p>If you need a certified weighmaster ticket for a U-Haul, RV, horse trailer, dump trailer, boat trailer, or a military PPM/DITY load, try a <strong>dedicated public scale house</strong> first. Use CAT when you want axle weights at a truck stop and your combination is over 2,000 lb. In California, go inside for a <strong>printed</strong> ticket if you need a weighmaster certificate — CAT’s Weigh My Truck PDF is not valid for that in CA.</p>
    <p class="cite">CAT how-to: <a href="https://catscale.com/how-to-weigh/">catscale.com/how-to-weigh</a> · CAT CA certificate: <a href="https://catscale.com/faqs/when-do-i-need-a-california-weighmaster-certificate/">when do I need a California Weighmaster Certificate?</a> · Official CA list: <a href="https://apps1.cdfa.ca.gov/publicscales/view.aspx?c=19">CDFA Los Angeles County</a></p>
  </div>
  {filters()}
  <div id="map" role="region" aria-label="Map of listed Los Angeles County scales"></div>
  <p class="notice-small">Map uses OpenStreetMap. Green = dedicated public. Gold = CAT. Blue = truck stop. Brown/gray = call-first plant. Red = enforcement. A list is the source of truth if the map fails to load.</p>

  <div data-filter-section>
  <h2 class="section-h" id="dedicated">Dedicated public scale houses</h2>
  <p class="section-note">These are the places civilians actually get a ticket. Call anyway — a scale house can close a lane or turn away a livestock trailer without updating the internet.</p>
  <div class="cards two">{cards_d}</div>
  </div>

  <div data-filter-section>
  <h2 class="section-h" id="cat">CAT Scale and truck-stop scales</h2>
  <p class="section-note">CAT is the national certified truck-stop network. We list only LA County CAT/truck-stop sites that appear on CDFA or that we verified on the operator’s own location page — not CAT’s full national list. Use <a href="https://catscale.com/cat-scale-locator/">CAT’s locator</a> for other stops. 2,000 lb floor. No corner weights. Do not unload horses at a Pilot.</p>
  <div class="cards two">{cards_c}</div>
  </div>

  <div data-filter-section>
  <h2 class="section-h" id="call-first">Call first — plants, quarries, scrap, landfills</h2>
  <p class="section-note">CDFA’s public-scales list is privately owned facilities that <em>offer truck-weighing services</em>. That includes chemical plants, rock companies, and scrap yards. Many will not weigh a walk-up U-Haul. We are not inventing “livestock OK” or hours for these. If you have a dump trailer and a landfill scale is your only option, call and ask whether they issue a weighmaster certificate to the public.</p>
  <table class="compact">
    <caption>CDFA Los Angeles listings that look like plant / yard traffic</caption>
    <thead><tr><th>Place</th><th>Phone</th><th>Type</th><th>Walk-up</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>
  </div>

  <hr class="hazard">
  <div class="box box-warn" id="do-not-go">
    <h2>Do not go here for a ticket</h2>
    <p>The I-405 Carson weigh station is a CHP commercial vehicle enforcement facility. It is not a public scale. ScaleRegistry lists it under “not public — listed so you do not drive to them.” You will not buy a certified ticket for a move, an RV, or a horse trailer here.</p>
    {enf_html}
    <p class="cite">Sources: <a href="https://scaleregistry.com/public-scales.html">ScaleRegistry</a> · <a href="https://dot.ca.gov/programs/traffic-operations/cvef/weigh-stations">Caltrans — Weigh-Stations (Enforcement Facilities)</a></p>
  </div>

  <div class="related">
    <h2>Related</h2>
    <ul>
      <li><a href="/how-to-weigh-an-rv/">How to weigh an RV or fifth-wheel at a CAT Scale</a></li>
      <li><a href="/ppm-dity-southern-california/">Military PPM / DITY weight tickets in Southern California</a></li>
      <li><a href="/horse-trailer/">Horse trailer: CAT vs mill vs landfill</a></li>
      <li><a href="/dump-trailer/">Dump trailer &amp; landfill scales</a></li>
      <li><a href="/cat-2000-lb-minimum/">What CAT’s 2,000 lb minimum means</a></li>
      <li><a href="/public-scale-vs-weigh-station/">Public scale vs highway weigh station</a></li>
      <li><a href="/orange-county/">Orange County public scales</a></li>
      <li><a href="/inland-empire/">Inland Empire public scales</a></li>
      <li><a href="/san-diego/">San Diego County public scales</a></li>
      <li><a href="/phoenix/">Phoenix metro public scales</a></li>
    </ul>
  </div>
</div>
</main>
""" + map_script(la)


def oc_body():
    oc = [s for s in STATIONS if s["county"] == "orange"]
    rows = "\n".join(compact_row(s) for s in sorted(oc, key=lambda x: (x["city"], x["name"])))
    sfs = next(s for s in STATIONS if s["id"] == "santa-fe-springs-public-scale")
    return f"""
<main id="main">
<section class="page-head">
  <div class="wrap">
    <p class="kicker">Orange County · CDFA table loaded {CHECKED_HUMAN}</p>
    <h1>Orange County public scales</h1>
    <p class="lede">CDFA’s Orange County page lists seven privately owned facilities that offer truck-weighing services. None of them read as a dedicated civilian public-scale house like Certified Scales, Rawlins, or Santa Fe Springs. Until an operator page confirms walk-up tickets, treat every OC row as call-first.</p>
    <p class="meta-line">7 CDFA Orange County listings · 0 verified dedicated public houses in-county · nearest dedicated house we list is Santa Fe Springs (Los Angeles County, 605 / Slauson).</p>
  </div>
</section>
<div class="wrap prose">
  <div class="box box-ok">
    <h2>Nearest dedicated house we actually trust for a walk-up</h2>
    <p>Santa Fe Springs Public Scale sits just over the county line and publishes walk-up hours on the operator’s page. If you are in north Orange County and need a ticket today, start there — then call.</p>
  </div>
  {card(sfs)}
  <p>For a CAT ticket, use <a href="https://catscale.com/cat-scale-locator/">CAT’s own locator</a>. We are not republishing CAT’s national list. Pilot Castaic (LA County, I-5) is the nearest CAT stop we verified on both CDFA and Pilot’s location page.</p>
  <div id="map" role="region" aria-label="Map of CDFA Orange County scale listings"></div>
  <h2 class="section-h">CDFA Orange County list (c=30)</h2>
  <p class="section-note">Pulled {CHECKED_HUMAN} from <a href="https://apps1.cdfa.ca.gov/publicscales/view.aspx?c=30">apps1.cdfa.ca.gov/publicscales/view.aspx?c=30</a>. Names, addresses, and phones are CDFA’s. Hours, fees, rig type, and walk-up policy were not on that table. We did not invent them.</p>
  <table class="compact">
    <caption>Orange County — call first / walk-up not verified</caption>
    <thead><tr><th>Place</th><th>Phone</th><th>Type</th><th>Walk-up</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>
  <div class="box box-call">
    <h3>What we still need to verify</h3>
    <p>Whether any of these seven will weigh a U-Haul, RV, or horse trailer for a printed weighmaster certificate. CR&amp;R Stanton is a waste company with public buyback hours on their site — that is not the same as a public ticket scale. New World Van Lines, O’Neil Storage, Peter Auto Center, 941 Corporation, and Schorr Metals are industrial or company sites until proven otherwise.</p>
  </div>
  <p class="cite">CDFA disclaimer applies: the Division makes no claims about absolute accuracy of this list.</p>
</div>
</main>
""" + map_script(oc + [sfs])



def ie_body():
    ie = [s for s in STATIONS if s["county"] in ("riverside", "san-bernardino")]
    dedicated = [s for s in ie if s["display_group"] == "dedicated"]
    cat = [s for s in ie if s["display_group"] == "cat"]
    call = [s for s in ie if s["display_group"] == "call_first"]
    cards_d = "\n".join(card(s) for s in dedicated)
    cards_c = "\n".join(card(s) for s in cat)
    rows = "\n".join(compact_row(s) for s in sorted(call, key=lambda x: (x["city"], x["name"])))
    n_ie = len(ie)
    n_riv = sum(1 for s in ie if s["county"] == "riverside")
    n_sbd = sum(1 for s in ie if s["county"] == "san-bernardino")
    return f"""
<main id="main">
<section class="page-head">
  <div class="wrap">
    <p class="kicker">Inland Empire · Riverside &amp; San Bernardino · listings checked {CHECKED_HUMAN}</p>
    <h1>Public scales in the Inland Empire</h1>
    <p class="lede">Colton has a ScaleRegistry public house. Love’s Barstow and Coachella publish CAT Scales on their own location pages. Riverside County landfills have scales for dump traffic — call first, they are not ticket shops. CDFA’s Riverside (c=33) and San Bernardino (c=36) facility grids did not load on this compile, so this is not a full county table.</p>
    <p class="meta-line">{n_ie} verified listings · {n_sbd} San Bernardino County · {n_riv} Riverside County · 1 dedicated house · 2 CAT stops · {len(call)} call-first landfills · CDFA county grids not loaded</p>
  </div>
</section>
<div class="wrap prose">
  {filters()}
  <div data-filter-section>
  <h2 class="section-h" id="dedicated">Dedicated public scale</h2>
  <p class="section-note">ScaleRegistry lists Superior Scale House in Colton the same way it lists the Lancaster 80' house we already carry. It does not publish hours, fees, or a phone. We did not fill those from Yellow Pages or other third-party dumps. Call before you drive.</p>
  <div class="cards">{cards_d}</div>
  </div>

  <div data-filter-section>
  <h2 class="section-h" id="cat">CAT Scale at Love’s</h2>
  <p class="section-note">We list only Inland Empire CAT stops verified on the operator’s own location page. Love’s Barstow (I-15) and Coachella (I-10) both list CAT Scales as an amenity. Pilot Flying J Fontana (14320 Slover Ave) and Mira Loma (11053 Riverside Dr) did <em>not</em> list CAT Scale in the amenity list we fetched, so they are not on this page. Use <a href="https://catscale.com/cat-scale-locator/">CAT’s locator</a> for other stops. 2,000 lb floor. No corner weights. Do not unload horses at a truck stop.</p>
  <div class="cards two">{cards_c}</div>
  </div>

  <div data-filter-section>
  <h2 class="section-h" id="call-first">Call first — Riverside County landfills</h2>
  <p class="section-note">These are dump sites with a scale at the gate. Riverside County Waste Resources publishes operating hours. That is not a promise they will issue a weighmaster certificate to a walk-up U-Haul, RV, or horse trailer. San Bernardino County’s landfill-hours table did not come through as a usable list on this compile, so those sites are omitted rather than guessed.</p>
  <table class="compact">
    <caption>Riverside County landfills — dump traffic, walk-up ticket not verified</caption>
    <thead><tr><th>Place</th><th>Phone</th><th>Type</th><th>Walk-up</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>
  </div>

  <div class="box box-call">
    <h3>What we still need to verify</h3>
    <p>CDFA Riverside (c=33) and San Bernardino (c=36) public-scale grids: blocked on this compile; we did not scrape Penske, Trucker Path, or AllStays to fill them. Hours, fees, and livestock policy at Superior Scale House. Whether any Riverside County landfill will sell a civilian weighmaster ticket. CAT staffing at Love’s (store is listed 24h; scale is not independently sourced). Pilot / Flying J CAT in Fontana, Ontario, and Mira Loma — not listed until Pilot’s own page says CAT Scale.</p>
  </div>
  <p class="cite">Sources: <a href="https://scaleregistry.com/public-scales.html">ScaleRegistry</a> · <a href="https://www.loves.com/locations/ca/barstow/loves-travel-stop-barstow-374">Love’s #374 Barstow</a> · <a href="https://www.loves.com/locations/ca/coachella/loves-travel-stop-coachella-207">Love’s #207 Coachella</a> · <a href="https://rcwaste.org/routine-waste">Riverside County Waste Resources</a> · <a href="https://catscale.com/cat-scale-locator/">CAT Scale locator</a> (linked, not republished)</p>
  <div class="related">
    <h2>Related</h2>
    <ul>
      <li><a href="/los-angeles/">Los Angeles County public scales</a></li>
      <li><a href="/orange-county/">Orange County public scales</a></li>
      <li><a href="/san-diego/">San Diego County public scales</a></li>
      <li><a href="/phoenix/">Phoenix metro public scales</a></li>
      <li><a href="/how-to-weigh-an-rv/">How to weigh an RV or fifth-wheel at a CAT Scale</a></li>
      <li><a href="/ppm-dity-southern-california/">Military PPM / DITY weight tickets in Southern California</a></li>
      <li><a href="/public-scale-vs-weigh-station/">Public scale vs highway weigh station</a></li>
    </ul>
  </div>
</div>
</main>
""" + map_script(ie)


def sd_body():
    sd = [s for s in STATIONS if s["county"] == "san-diego"]
    dedicated = [s for s in sd if s["display_group"] == "dedicated"]
    cat = [s for s in sd if s["display_group"] == "cat"]
    call = [s for s in sd if s["display_group"] == "call_first"]
    enf = [s for s in sd if s["display_group"] == "enforcement"]
    cards_d = "\n".join(card(s) for s in dedicated)
    cards_c = "\n".join(card(s) for s in cat)
    rows = "\n".join(compact_row(s) for s in sorted(call, key=lambda x: (x["city"], x["name"])))
    enf_html = "\n".join(card(s) for s in enf)
    n = len(sd)
    return f"""
<main id="main">
<section class="page-head">
  <div class="wrap">
    <p class="kicker">San Diego County · listings checked {CHECKED_HUMAN}</p>
    <h1>Public scales in San Diego County</h1>
    <p class="lede">Three dedicated public houses publish walk-up weighmaster tickets (Allstate Poway and Oceanside, Eckert’s San Marcos). Pilot Otay Mesa lists a CAT Scale on Pilot’s own location page. EDCO La Mesa, Truck Net Otay, and Miramar Landfill are call-first. San Onofre on I-5 is CHP enforcement — not a ticket window. CDFA’s San Diego grid (c=37) did not load on this compile.</p>
    <p class="meta-line">{n} verified listings · {len(dedicated)} dedicated houses · {len(cat)} CAT stop · {len(call)} call-first · {len(enf)} enforcement do-not-go · CDFA county grid not loaded</p>
  </div>
</section>
<div class="wrap prose">
  {filters()}
  <div data-filter-section>
  <h2 class="section-h" id="dedicated">Dedicated public scales</h2>
  <p class="section-note">Operator pages describe Weighmaster certificates for DMV and military PPM/DITY. Allstate’s shared public-scales page lists a $25 certified-weight fee; Eckert’s public-scale page lists $10 empty+heavy on the same ticket. Livestock policy is still unknown. Call ahead — hours move.</p>
  <div class="cards">{cards_d}</div>
  </div>

  <div data-filter-section>
  <h2 class="section-h" id="cat">CAT Scale at Pilot</h2>
  <p class="section-note">We list only San Diego County CAT stops verified on the operator’s own location page. Pilot #343 Otay Mesa (Piper Ranch Rd) lists CAT Scale as an amenity. Love’s URLs marketed as San Diego / Otay / Alpine / Pala / San Marcos did not resolve to San Diego County stores on this compile, so no Love’s CAT is listed. Use <a href="https://catscale.com/cat-scale-locator/">CAT’s locator</a> for other stops. 2,000 lb floor. No corner weights. Do not unload horses at a truck stop.</p>
  <div class="cards two">{cards_c}</div>
  </div>

  <div data-filter-section>
  <h2 class="section-h" id="call-first">Call first — transfer, industrial, landfill</h2>
  <p class="section-note">EDCO La Mesa advertises a public scale for Weighmaster Certificates on its own facility page, but it is still a transfer/disposal site. Truck Net Otay publishes a certified scale without walk-up hours. Miramar Landfill scales weigh dump traffic for city fees — not a published ticket shop.</p>
  <table class="compact">
    <caption>San Diego County — call first / walk-up ticket not fully verified</caption>
    <thead><tr><th>Place</th><th>Phone</th><th>Type</th><th>Walk-up</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>
  </div>

  <hr class="hazard">
  <div class="box box-warn" id="do-not-go">
    <h2>Do not go here for a ticket</h2>
    <p>San Onofre on I-5 (near Oceanside) is a pair of CHP commercial vehicle enforcement facilities on the Caltrans CVEF list. It is not a public scale. You will not buy a certified ticket for a move, an RV, or a horse trailer here.</p>
    {enf_html}
    <p class="cite">Source: <a href="https://dot.ca.gov/programs/traffic-operations/cvef/weigh-stations">Caltrans — Weigh-Stations (Enforcement Facilities)</a></p>
  </div>

  <div class="box box-call">
    <h3>What we still need to verify</h3>
    <p>CDFA San Diego (c=37) public-scale grid: WAF-blocked on curl this compile; no browser extract. Phones for Allstate Poway/Oceanside (not on the operator scale pages we fetched). Exact street number for Eckert’s Bent St entrance. Love’s / TA / other Pilot CAT stops inside the county on their own amenity lists. Whether Miramar or Otay Landfill will sell a civilian weighmaster ticket. Livestock policy everywhere.</p>
  </div>
  <p class="cite">Sources: <a href="https://amove.com/resource-center/public-scales/">Allstate Logistics public scales</a> · <a href="https://eckertsmoving.com/services/public-scale/">Eckert’s public scale</a> · <a href="https://locations.pilotflyingj.com/us/ca/san-diego/1497-piper-ranch-rd">Pilot #343 Otay Mesa</a> · <a href="https://poway.edcodisposal.com/public-facilities/edco-station-la-mesa/">EDCO La Mesa</a> · <a href="https://www.trucknetllc.com/service/scale-3">Truck Net</a> · <a href="https://www.sandiego.gov/environmental-services/miramar">Miramar Landfill</a> · <a href="https://catscale.com/cat-scale-locator/">CAT Scale locator</a> (linked, not republished) · <a href="https://dot.ca.gov/programs/traffic-operations/cvef/weigh-stations">Caltrans CVEF</a></p>
  <div class="related">
    <h2>Related</h2>
    <ul>
      <li><a href="/los-angeles/">Los Angeles County public scales</a></li>
      <li><a href="/orange-county/">Orange County public scales</a></li>
      <li><a href="/inland-empire/">Inland Empire public scales</a></li>
      <li><a href="/phoenix/">Phoenix metro public scales</a></li>
      <li><a href="/how-to-weigh-an-rv/">How to weigh an RV or fifth-wheel at a CAT Scale</a></li>
      <li><a href="/ppm-dity-southern-california/">Military PPM / DITY weight tickets in Southern California</a></li>
      <li><a href="/public-scale-vs-weigh-station/">Public scale vs highway weigh station</a></li>
    </ul>
  </div>
</div>
</main>
""" + map_script(sd)




def phoenix_body():
    phx = [s for s in STATIONS if s["county"] == "maricopa"]
    dedicated = [s for s in phx if s["display_group"] == "dedicated"]
    cat = [s for s in phx if s["display_group"] == "cat"]
    call = [s for s in phx if s["display_group"] == "call_first"]
    enf = [s for s in phx if s["display_group"] == "enforcement"]
    cards_d = "\n".join(card(s) for s in dedicated) if dedicated else ""
    cards_c = "\n".join(card(s) for s in cat)
    rows = "\n".join(compact_row(s) for s in sorted(call, key=lambda x: (x["city"], x["name"]))) if call else ""
    enf_html = "\n".join(card(s) for s in enf) if enf else ""
    n = len(phx)
    if dedicated:
        dedicated_block = f"""
  <div data-filter-section>
  <h2 class="section-h" id="dedicated">Dedicated public scales</h2>
  <p class="section-note">Operator pages that publish walk-up weighmaster tickets for civilians.</p>
  <div class="cards two">{cards_d}</div>
  </div>
"""
    else:
        dedicated_block = """
  <div class="box box-call" id="dedicated">
    <h2>No verified dedicated public scale house</h2>
    <p>ScaleRegistry’s public-weighing page lists Colton, Lancaster, Merced, and Selma for California — <strong>no Phoenix / Maricopa dedicated house</strong>. Arizona Department of Agriculture publishes weighmaster <em>licensing</em> how-to, not a facility directory like California’s CDFA county grids. We are not inventing a walk-up house from industrial scale vendors or third-party trucker directories.</p>
  </div>
"""
    if call:
        call_block = f"""
  <div data-filter-section>
  <h2 class="section-h" id="call-first">Call first</h2>
  <p class="section-note">Industrial / landfill / transfer rows only when an official page mentions public weighing.</p>
  <table class="compact">
    <caption>Phoenix metro — call first</caption>
    <thead><tr><th>Place</th><th>Phone</th><th>Type</th><th>Walk-up</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>
  </div>
"""
    else:
        call_block = ""
    enf_block = f"""
  <hr class="hazard">
  <div class="box box-warn" id="do-not-go">
    <h2>Do not go here for a ticket</h2>
    <p>ADOT Enforcement and Compliance runs ports of entry and virtual truck-screening sites. Those are for commercial vehicle enforcement — not a place to buy a civilian weighmaster ticket for a U-Haul, RV, horse trailer, or PPM load.</p>
    <ul>
      <li><strong>Sacaton Rest Area (I-10 between Phoenix and Casa Grande)</strong> — ADOT virtual port / weigh-in-motion screening for commercial vehicles.</li>
      <li><strong>I-10 Ehrenberg and San Simon ports of entry</strong> — state POEs on the California and New Mexico ends of I-10 (far from metro Phoenix; still not ticket shops).</li>
    </ul>
    {enf_html}
    <p class="cite">Sources: <a href="https://azdot.gov/mvd/services/enforcement/commercial-vehicle-permits/virtual-port-technology">ADOT — Virtual Port Technology</a> · <a href="https://azdot.gov/mvd/services/enforcement/port-entry-locations">ADOT — Port of Entry Locations</a></p>
  </div>
"""
    return f"""
<main id="main">
<section class="page-head">
  <div class="wrap">
    <p class="kicker">Phoenix metro · Maricopa County · listings checked {CHECKED_HUMAN}</p>
    <h1>Public scales in Phoenix metro</h1>
    <p class="lede">Arizona has no CDFA-style public county scale grid. ScaleRegistry lists no Phoenix dedicated house. What we can verify tonight: four CAT Scales on Pilot Flying J and Love’s <em>own</em> location pages along I-10 (Avondale, Tolleson, Phoenix Latham, Chandler). City of Phoenix / Maricopa landfill pages describe disposal weigh stations for facility traffic — not a published walk-up weighmaster ticket shop — so they are omitted rather than guessed.</p>
    <p class="meta-line">{n} verified listings · {len(dedicated)} dedicated houses · {len(cat)} CAT stops · {len(call)} call-first · AZ facility grid: none published like CDFA</p>
  </div>
</section>
<div class="wrap prose">
  {filters()}
  {dedicated_block}

  <div data-filter-section>
  <h2 class="section-h" id="cat">CAT Scale at Pilot / Flying J and Love’s</h2>
  <p class="section-note">We list only Maricopa County CAT stops verified on the operator’s own location page. Flying J #611 (Phoenix / Latham), Pilot #459 (Avondale), Love’s #659 (Tolleson), and Love’s #328 (Chandler) each list CAT Scale / CAT Scales as an amenity. Pilot’s Phoenix city list also shows #1433 and #1194 — those rows do <strong>not</strong> list CAT, so they are not here. Love’s #280 Buckeye amenities on loves.com did not include CAT Scales on this compile. Use <a href="https://catscale.com/cat-scale-locator/">CAT’s locator</a> for other stops. 2,000 lb floor. No corner weights. Do not unload horses at a truck stop.</p>
  <div class="cards two">{cards_c}</div>
  </div>

  {call_block}
  {enf_block}

  <div class="box box-call">
    <h3>What we still need to verify</h3>
    <p>Any dedicated public scale house in Maricopa with an operator page that sells walk-up weighmaster certificates. TA Phoenix (Latham) newsroom mentions a “Scale” but not CAT Scale — omitted until TA’s own location page confirms CAT. Other Pilot / Love’s / TA metro stores on their amenity lists. Whether a City of Phoenix or Maricopa transfer/landfill gate will sell a civilian weighmaster ticket (official pages we checked describe disposal permits and facility weigh-ins, not public ticket shops). Livestock policy everywhere. Arizona printed-ticket quirks vs California Weighmaster Certificate rules for PPM movers crossing state lines.</p>
  </div>
  <p class="cite">Sources: <a href="https://locations.pilotflyingj.com/us/az/phoenix/6700-w-latham-st">Flying J #611 Phoenix</a> · <a href="https://locations.pilotflyingj.com/us/az/avondale/900-n-99th-ave">Pilot #459 Avondale</a> · <a href="https://www.loves.com/locations/az/tolleson/loves-travel-stop-tolleson-659">Love’s #659 Tolleson</a> · <a href="https://www.loves.com/locations/az/chandler/loves-travel-stop-chandler-328">Love’s #328 Chandler</a> · <a href="https://catscale.com/cat-scale-locator/">CAT Scale locator</a> (linked, not republished) · <a href="https://scaleregistry.com/public-scales.html">ScaleRegistry public scales</a> · <a href="https://agriculture.az.gov/weights-measures/licensing/weighmaster">AZ Ag weighmaster licensing</a> · <a href="https://azdot.gov/mvd/services/enforcement/commercial-vehicle-permits/virtual-port-technology">ADOT Virtual Port</a></p>
  <div class="related">
    <h2>Related</h2>
    <ul>
      <li><a href="/los-angeles/">Los Angeles County public scales</a></li>
      <li><a href="/san-diego/">San Diego County public scales</a></li>
      <li><a href="/inland-empire/">Inland Empire public scales</a></li>
      <li><a href="/how-to-weigh-an-rv/">How to weigh an RV or fifth-wheel at a CAT Scale</a></li>
      <li><a href="/ppm-dity-southern-california/">Military PPM / DITY weight tickets in Southern California</a></li>
      <li><a href="/public-scale-vs-weigh-station/">Public scale vs highway weigh station</a></li>
    </ul>
  </div>
</div>
</main>
""" + map_script(phx)



def cv_body():
    cv = [s for s in STATIONS if s["county"] in ("kern", "fresno", "merced")]
    dedicated = [s for s in cv if s["display_group"] == "dedicated"]
    cat = [s for s in cv if s["display_group"] == "cat"]
    call = [s for s in cv if s["display_group"] == "call_first"]
    enf = [s for s in cv if s["display_group"] == "enforcement"]
    cards_d = "\n".join(card(s) for s in dedicated)
    cards_c = "\n".join(card(s) for s in cat)
    rows = "\n".join(compact_row(s) for s in sorted(call, key=lambda x: (x["city"], x["name"]))) if call else ""
    n = len(cv)
    n_kern = sum(1 for s in cv if s["county"] == "kern")
    n_fresno = sum(1 for s in cv if s["county"] == "fresno")
    n_merced = sum(1 for s in cv if s["county"] == "merced")
    call_block = ""
    if call:
        call_block = f"""
  <div data-filter-section>
  <h2 class="section-h" id="call-first">Call first</h2>
  <p class="section-note">Industrial / landfill / plant rows only when an official page mentions public weighing.</p>
  <table class="compact">
    <caption>Central Valley — call first</caption>
    <thead><tr><th>Place</th><th>Phone</th><th>Type</th><th>Walk-up</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>
  </div>
"""
    return f"""
<main id="main">
<section class="page-head">
  <div class="wrap">
    <p class="kicker">Central Valley · Kern · Fresno · Merced · listings checked {CHECKED_HUMAN}</p>
    <h1>Public scales in California’s Central Valley</h1>
    <p class="lede">Two dedicated public houses on ScaleRegistry (Selma with an operator site; Merced with address and phone only), plus four CAT Scales verified on Pilot Flying J and Love’s <em>own</em> location pages in Kern County (Bakersfield Zachary, Bakersfield Taft Hwy, Lost Hills I-5, Tehachapi Hwy 58). CDFA Kern (c=15), Fresno, and Merced facility grids did not load on this compile (WAF blocked), so this is not a full county table.</p>
    <p class="meta-line">{n} verified listings · {n_kern} Kern · {n_fresno} Fresno · {n_merced} Merced · {len(dedicated)} dedicated houses · {len(cat)} CAT stops · CDFA county grids not loaded</p>
  </div>
</section>
<div class="wrap prose">
  {filters()}

  <div data-filter-section>
  <h2 class="section-h" id="dedicated">Dedicated public scales</h2>
  <p class="section-note">Selma’s operator site sells certified weights to professional drivers. Highway 59 Scales in Merced is on ScaleRegistry the same way Colton and Lancaster are — address and phone, no published hours. Call before you drive either house with a civilian rig.</p>
  <div class="cards two">{cards_d}</div>
  </div>

  <div data-filter-section>
  <h2 class="section-h" id="cat">CAT Scale at Pilot and Love’s (Kern)</h2>
  <p class="section-note">We list only Central Valley CAT stops verified on the operator’s own location page. Pilot #613 (Bakersfield / Zachary) publishes CAT Scale in its amenity list. Love’s #830 (Bakersfield / Taft Hwy), #230 (Lost Hills), and #392 (Tehachapi) each list CAT Scales. Two other Bakersfield Pilot/dealer pages on the city list did not publish CAT amenities on this compile, so they are omitted. Use <a href="https://catscale.com/cat-scale-locator/">CAT’s locator</a> for other stops. 2,000 lb floor. No corner weights. Do not unload horses at a truck stop. In California, go inside for a printed weighmaster certificate when you need one.</p>
  <div class="cards two">{cards_c}</div>
  </div>

  {call_block}

  <hr class="hazard">
  <div class="box box-warn" id="do-not-go">
    <h2>Do not go here for a ticket</h2>
    <p>California Commercial Vehicle Enforcement Facilities (CHP weigh stations) are for commercial enforcement — not a place to buy a civilian weighmaster ticket for a U-Haul, RV, horse trailer, or PPM load. See Caltrans’ weigh-station primer and follow posted signs; do not treat this directory as a bypass guide.</p>
    <p class="cite">Source: <a href="https://dot.ca.gov/programs/traffic-operations/cvef/weigh-stations">Caltrans — Weigh-Stations (Enforcement Facilities)</a></p>
  </div>

  <div class="box box-call">
    <h3>What we still need to verify</h3>
    <p>Full CDFA Kern (c=15), Fresno, and Merced public-scale grids (blocked on this compile). Hours, fees, and livestock policy at Highway 59 Scales. Whether Selma will weigh a walk-up U-Haul / horse trailer / PPM (operator site speaks to professional truck drivers). Other Pilot / Flying J / Love’s / TA CAT stops on I-5 and Hwy 99 whose own pages list CAT. Kern / Fresno / Merced landfill or transfer gates that publish a civilian weighmaster ticket — omitted until an official page says so. Lat/lng for Selma and Merced houses.</p>
  </div>
  <p class="cite">Sources: <a href="https://selmacertifiedpublicscale.com/">Selma Certified Public Scale</a> · <a href="https://scaleregistry.com/public-scales.html">ScaleRegistry public scales</a> · <a href="https://locations.pilotflyingj.com/us/ca/bakersfield/17047-zachary-ave">Pilot #613 Bakersfield</a> · <a href="https://www.loves.com/locations/ca/bakersfield/loves-travel-stop-bakersfield-830">Love’s #830 Bakersfield</a> · <a href="https://www.loves.com/locations/ca/lost-hills/loves-travel-stop-lost-hills-230">Love’s #230 Lost Hills</a> · <a href="https://www.loves.com/locations/ca/tehachapi/loves-travel-stop-tehachapi-392">Love’s #392 Tehachapi</a> · <a href="https://catscale.com/cat-scale-locator/">CAT Scale locator</a> (linked, not republished) · CDFA Kern/Fresno/Merced grids: blocked</p>
  <div class="related">
    <h2>Related</h2>
    <ul>
      <li><a href="/los-angeles/">Los Angeles County public scales</a></li>
      <li><a href="/inland-empire/">Inland Empire public scales</a></li>
      <li><a href="/phoenix/">Phoenix metro public scales</a></li>
      <li><a href="/how-to-weigh-an-rv/">How to weigh an RV or fifth-wheel at a CAT Scale</a></li>
      <li><a href="/ppm-dity-southern-california/">Military PPM / DITY weight tickets in Southern California</a></li>
      <li><a href="/public-scale-vs-weigh-station/">Public scale vs highway weigh station</a></li>
    </ul>
  </div>
</div>
</main>
""" + map_script(cv)



def page_rv():
    return """
<main id="main">
<section class="page-head">
  <div class="wrap">
    <p class="kicker">How-to · CAT Scale</p>
    <h1>How to weigh an RV or fifth-wheel at a CAT Scale</h1>
    <p class="lede">CAT Scale will give you steer, drive, and trailer axle weights plus a gross. It will not give you corner or individual wheel weights. The scale will not run under 2,000 lb. In California, pick up a printed ticket if you need a weighmaster certificate.</p>
  </div>
</section>
<div class="wrap prose">
  <h2>What CAT actually measures</h2>
  <p>A CAT Scale is three platforms. CAT’s own diagrams put the steer axle on platform 1, the drive axle on platform 2, and the trailer (or tow car) on platform 3. For a motorhome, CAT says the coach must be completely on the scale, steer on 1, drive on 2, platform 3 likely empty. Same idea for a truck and fifth-wheel: truck on 1 and 2, trailer on 3.</p>
  <blockquote>Our scales can give you axle weights and a total gross weight, however, they cannot weigh each corner of the vehicle. We cannot provide individual wheel weights and, to prevent damage to your vehicle as well as our scales, do not allow that type of weighing.<cite> — CAT Scale, How To Weigh (motorhome)</cite></blockquote>
  <p>If you need corner weights for tire loading or a weight-distribution hitch setup, CAT is the wrong tool. Dedicated public houses sometimes offer axle splits; portable wheel scales are a different product. RV owners on the Grand Design owners’ forum work around CAT’s three-platform limit by weighing the truck alone, then the combination, and subtracting to get pin or tongue weight — that is owner math, not a CAT corner-weight service.</p>
  <p class="cite">Sources: <a href="https://catscale.com/how-to-weigh/">catscale.com/how-to-weigh</a> · <a href="https://www.mygrandrv.com/threads/weighing-on-a-cat-scale.52312/">Weighing on a CAT Scale? (Grand Design forum, 2020)</a></p>

  <h2>The 2,000 lb floor</h2>
  <p>CAT: “Our scales are set to a weight threshold of 2,000 lbs. If your vehicle or combination is estimated to be lighter than 2,000 lbs, please call our 24-Hour Help Desk.” A toad-less class B, an empty motorcycle trailer, or a car on the way to the DMV may not register. For those, use a dedicated public scale house (see <a href="/cat-2000-lb-minimum/">What CAT’s 2,000 lb minimum means</a>).</p>
  <p>CAT’s FAQ also states a CAT Scale can weigh vehicles between 2,000 lb and 200,000 lb.</p>

  <h2>Positioning, in plain language</h2>
  <ul>
    <li><strong>Motorhome:</strong> whole coach on the scale; steer platform 1, drive platform 2.</li>
    <li><strong>Motorhome + tow car:</strong> coach on 1 and 2, toad on 3.</li>
    <li><strong>Truck + fifth-wheel or travel trailer:</strong> steer 1, drive 2, trailer 3. Combination must be completely on the scale.</li>
    <li><strong>Truck + boat:</strong> CAT publishes a truck-and-boat diagram — trailer on platform 3.</li>
    <li><strong>Tag-axle motorhome:</strong> CAT says call 1-877-228-7225 ext. 6 rather than guessing.</li>
  </ul>
  <p>Use the intercom on the scale. Then go inside for the ticket. CAT will not alter a ticket after it is printed.</p>

  <h2>Printed ticket in California</h2>
  <p>If you are being paid by weight or registering a vehicle with the California DMV, CAT says you need a California Weighmaster Certificate, not only the guaranteed CAT ticket. CAT published these CA prices on its FAQ (checked 29 Aug 2026): Weighmaster Certificate $30.50 first weigh / $10.50 reweigh at the same location within 24 hours; California Guaranteed ticket $15.25 / $5.25. Confirm at the booth — prices move.</p>
  <p>The Weigh My Truck app PDF is <strong>not</strong> a California Weighmaster Certificate. CAT and the Weigh My Truck help page both say California requires information the app does not capture. Go inside and get the printed certificate.</p>
  <p class="cite"><a href="https://catscale.com/faqs/when-do-i-need-a-california-weighmaster-certificate/">CAT: When do I need a California Weighmaster Certificate?</a> · <a href="https://weighmytruck.com/Help">Weigh My Truck Help/FAQ</a></p>

  <h2>Where to do this in Los Angeles County</h2>
  <p>Verified on this site: Montebello CAT Scale (on the CDFA list) and Pilot Castaic (CDFA + Pilot location page lists CAT Scale). Harbor, Bandini, and Commerce are CDFA truck-stop scales that may not be CAT-branded — call. For a house that will weigh a light RV or a toad under 2,000 lb, use Certified Scales, Rawlins, Santa Fe Springs, or Allstate Logistics instead.</p>
  <p><a href="/los-angeles/">Los Angeles County listings</a> · <a href="https://catscale.com/cat-scale-locator/">CAT Scale locator</a></p>
</div>
</main>
"""


def page_ppm():
    return """
<main id="main">
<section class="page-head">
  <div class="wrap">
    <p class="kicker">Southern California · military move</p>
    <h1>PPM / DITY weight tickets in Southern California</h1>
    <p class="lede">A Personally Procured Move pays on the difference between empty and full certified weights. In California, that usually means a printed weighmaster certificate with a weighmaster signature — not a phone PDF. Confirm every field with your Transportation Office before you pull onto a scale.</p>
  </div>
</section>
<div class="wrap prose">
  <div class="box box-call">
    <p>This page describes how public scales and CAT talk about tickets. It is not legal advice and it is not a substitute for your branch’s PPM instructions. If a ticket is wrong, finance offices are not gentle. Start with your Transportation Office, then weigh.</p>
  </div>

  <h2>Empty, then full, same combination</h2>
  <p>You need at least two tickets: empty (tare) before household goods go on, and full (gross) after. Same vehicle and trailer combination both times. Fuel the same way both times. People and pets out. CAT’s DITY FAQ says no appointment is required at a CAT Scale: split the vehicle on platforms 1 and 2, use the intercom, then go inside for the ticket and check the weighmaster signature before you leave the lot.</p>

  <h2>What CAT will print for a military move</h2>
  <p>CAT publishes the prompts the cashier asks and the answers many service members use (verify with your TO — branches differ):</p>
  <ul>
    <li>Truck/Tractor # — license plate</li>
    <li>Company name — branch of service</li>
    <li>Trailer # — rank</li>
    <li>Commodity — name and last four of SSN</li>
  </ul>
  <p>CAT: the weighmaster must sign; signatures usually print automatically; tickets cannot be edited after printing. If you lose a CAT ticket, CAT says it keeps electronic records of sold tickets for seven years and has a ticket-copy request form.</p>
  <p class="cite">Source: <a href="https://catscale.com/contact-us/faq/">CAT Scale FAQ, “What do I need printed on my scale ticket for a Military Move (DITY Move)?”</a></p>

  <h2>California printed certificate vs Weigh My Truck PDF</h2>
  <p>Weigh My Truck will email a PDF that CAT says is certified in every state <strong>except California</strong>. California Weighmaster Certificates need information the app does not capture. If you weigh in California for a PPM, go inside and get the printed California Weighmaster Certificate. CAT’s CA FAQ (checked 29 Aug 2026) lists $30.50 for a first weighmaster certificate and $10.50 for a same-location reweigh within 24 hours. Confirm the number on the booth sign.</p>
  <p class="cite"><a href="https://weighmytruck.com/Help">weighmytruck.com/Help</a> · <a href="https://catscale.com/faqs/when-do-i-need-a-california-weighmaster-certificate/">CAT California Weighmaster Certificate FAQ</a></p>

  <h2>CAT vs CDFA public house vs on-base</h2>
  <ul>
    <li><strong>CAT (Montebello, Pilot Castaic):</strong> axle weights, national brand, often the easiest Saturday option if you are over 2,000 lb. Get the printed CA certificate. Do not treat the app PDF as enough in California.</li>
    <li><strong>Dedicated CDFA public houses</strong> (Certified Scales LLC, Rawlins, Santa Fe Springs, Allstate Logistics): licensed weighmasters on the state list; better for light combinations and for people who want a clerk used to DMV and military certificates. Allstate’s operator page explicitly lists DITY/PPM. Certified Scales’ operator site mentions military DITY/PPT certificates. Hours are weekday-heavy — Rawlins Mon–Fri 6–6, Santa Fe Springs Mon–Fri 8 a.m.–midnight, Allstate North Hollywood Mon–Fri 8–5.</li>
    <li><strong>On-base scales:</strong> often free and familiar to finance, with short hours and peak-season lines. Ask your TO. We do not list installation scales here.</li>
  </ul>
  <p>Industrial CDFA listings (Covestro, Linde, quarries, scrap) are a poor PPM plan. They may refuse you, and a handwritten or incomplete ticket is a claim problem.</p>

  <h2>A longer independent guide</h2>
  <p>PCS Pay It Forward publishes a detailed walkthrough of certified weight tickets for a PPM, including branch quirks and common mistakes. Read it as a guide; we are not copying their text into this page. Your Transportation Office still owns the requirement.</p>
  <p><a href="https://pcspayitforward.com/certified-weight-tickets-ppm-move/">pcspayitforward.com — How to Get Certified Weight Tickets for a PPM Move</a></p>

  <p><a href="/los-angeles/">Los Angeles County scales</a> · <a href="/how-to-weigh-an-rv/">How CAT platforms work</a></p>
</div>
</main>
"""


def page_horse():
    return """
<main id="main">
<section class="page-head">
  <div class="wrap">
    <p class="kicker">Livestock trailers · call first</p>
    <h1>Horse trailer: CAT vs grain mill vs landfill</h1>
    <p class="lede">You need real numbers — empty trailer, then a travel-day load — because manufacturer dry weight is a starting point, not a plan. CAT will weigh a combination over 2,000 lb. A mill or landfill might. A Pilot parking lot is not a place to unload horses.</p>
  </div>
</section>
<div class="wrap prose">
  <div class="box box-warn">
    <h2>Do not unload horses at a Pilot</h2>
    <p>Truck-stop lots are diesel traffic, dogs, and noise. Equine writers who send people to CAT for payload math are explicit: do the second weigh with horses on board without unhooking, because horses have opinions about truck-stop parking lots. If a scale will not take a loaded horse trailer, leave and call a dedicated house or a mill — do not improvise a hitch in the fuel island.</p>
    <p class="cite">See <a href="https://equineexchangestore.com/blogs/news/know-before-you-tow">Equine Exchange Store, “Know Before You Tow”</a> (payload / CAT / grain-elevator advice, June 2026).</p>
  </div>

  <h2>Three kinds of scale, three kinds of risk</h2>
  <h3>1. CAT Scale (Montebello, Pilot Castaic)</h3>
  <p>Best documented axle/gross weights. 2,000 lb minimum. No corner weights. You stay hooked. Tell the cashier you have a horse trailer so they are not surprised. Livestock policy is not published by CAT on the how-to page — call the 24-hour desk (1-877-228-7225 ext. 6) or the site if you are unsure they will let a loaded stock trailer on the platform. Get a printed ticket in California if you need a weighmaster certificate.</p>
  <h3>2. Dedicated public scale house</h3>
  <p>Certified Scales, Rawlins, Santa Fe Springs, Allstate Logistics. These are the civilian ticket shops. None of the operator pages we checked say “livestock OK.” That field is unknown until you call. Ask: Will you weigh a bumper-pull / gooseneck horse trailer with horses on board? Do we stay on the truck? Is there a safe place to wait that is not the scale deck?</p>
  <h3>3. Grain mill / landfill / quarry</h3>
  <p>CDFA lists Romberg Milling in Paramount, plus rock companies and waste yards. Horse people are sometimes told “use a grain elevator.” That is a maybe: mills and landfills weigh their own traffic. They may refuse a walk-up, refuse live animals, or only weigh during receiving hours. We are not marking any of them livestock-OK. Call, then decide.</p>

  <h2>Call-ahead script</h2>
  <div class="script">
    <p>“Hi — I’m a civilian, not a freight account. I have a [bumper-pull / gooseneck] horse trailer, about [N] feet, estimated [empty / loaded] weight around [X] pounds. I need a certified weighmaster ticket. Can you weigh that combination today? Do I need an account? Can the horses stay on the trailer? Where do I enter, and is there a fee I should know about?”</p>
    <p>If they hesitate: “If you don’t take livestock trailers, that’s fine — can you name a public scale that does?”</p>
  </div>
  <p>Write down the person’s name, the hours they quoted, and whether they said printed certificate. If they cannot promise a ticket, do not drive there with horses.</p>

  <h2>What to weigh, and in what order</h2>
  <ol>
    <li>Empty trailer (or empty truck + trailer) on a quiet day — true empty, not brochure dry weight.</li>
    <li>Travel-day load: horses on, hay, water, tack. Stay hooked. CAT will not give per-corner numbers; pin/tongue weight is a second weigh of the truck or owner math.</li>
    <li>Compare truck GVWR, payload (door sticker), trailer GVWR, and GCWR. Close is not fine.</li>
  </ol>
  <p>CAT cannot legally-for-trade a corner weight. Do not try to perch one wheel on a CAT platform.</p>

  <h2>Gear (no fake affiliate links)</h2>
  <p>Weight-distribution hitches, tongue-weight gauges, and portable wheel scales are sold at farm and hitch shops, including Tractor Supply. WeighHere does not have a live Tractor Supply, Amazon, or U-Haul affiliate ID on this page. If those links appear later, they will be disclosed on <a href="/about.html">About</a>. We are not inventing partner IDs.</p>
  <p class="cite">Tractor Supply’s public affiliate program page: <a href="https://www.tractorsupply.com/tsc/cms/policies-information/affiliate-program">tractorsupply.com affiliate program</a></p>
  <p><a href="/los-angeles/">LA County listings</a> · <a href="/cat-2000-lb-minimum/">Under 2,000 lb?</a></p>
</div>
</main>
"""



def page_dump():
    landfills = [s for s in STATIONS if s["type"] == "landfill"]
    landfills = sorted(landfills, key=lambda x: (x["county"], x["city"], x["name"]))
    county_label = {
        "los-angeles": "Los Angeles",
        "orange": "Orange",
        "riverside": "Riverside",
        "san-bernardino": "San Bernardino",
        "san-diego": "San Diego",
        "maricopa": "Maricopa",
        "kern": "Kern",
        "fresno": "Fresno",
        "merced": "Merced",
    }
    rows = []
    for s in landfills:
        phone = e(s.get("phone") or "—")
        hours = e(s.get("hours_notes") or "Hours not verified — call.")
        zipc = e(s.get("zip") or "")
        county = e(county_label.get(s["county"], s["county"]))
        src = e(s.get("source_url") or "#")
        src_name = e(s.get("source_name") or "Source")
        rows.append(f"""<tr id="{e(s['id'])}">
  <td><strong>{e(s['name'])}</strong><br>{e(s['address'])}, {e(s['city'])} {zipc}<br><span class="meta-line">{county} County</span></td>
  <td>{phone}</td>
  <td>{hours}</td>
  <td>Call first — dump traffic, not a published ticket shop</td>
  <td><a href="{src}">{src_name}</a></td>
</tr>""")
    table_rows = "\n".join(rows)
    n = len(landfills)
    return f"""
<main id="main">
<section class="page-head">
  <div class="wrap">
    <p class="kicker">Dump / landscape trailers · call first</p>
    <h1>Dump trailer &amp; landfill scales</h1>
    <p class="lede">You need a number for dirt, rock, green waste, or a buyer. A dedicated public scale house is usually the ticket shop. CAT will weigh a loaded dump trailer over 2,000 lb at a truck stop. A landfill gate scale weighs dump traffic for disposal fees — that is not the same as a walk-up weighmaster certificate.</p>
  </div>
</section>
<div class="wrap prose">
  <div class="box box-warn">
    <h2>Landfill scale ≠ public ticket shop</h2>
    <p>County and city landfill pages publish gate hours so you can dump. They do <strong>not</strong> advertise selling a civilian weighmaster certificate for a U-Haul, RV, horse trailer, or empty/loaded dump trailer that is not disposing material. We list those gates as call-first. If you only need a certified weight and are not dumping, start with a dedicated house or CAT.</p>
    <p class="cite">Riverside County Waste Resources: <a href="https://rcwaste.org/routine-waste">rcwaste.org/routine-waste</a> · Miramar: <a href="https://www.sandiego.gov/environmental-services/miramar">sandiego.gov Miramar Landfill</a></p>
  </div>

  <h2>Three places people try</h2>
  <h3>1. Dedicated public scale house</h3>
  <p>Best first call when you need a California weighmaster certificate and you are not dumping. Certified Scales, Rawlins, Santa Fe Springs, Allstate (NoHo / Poway / Oceanside), Eckert’s San Marcos, Selma, Merced Highway 59, Colton Superior. Ask: Will you weigh a dump trailer / utility trailer with a pickup? Do I need an account? Printed certificate? Fee?</p>
  <h3>2. CAT Scale at a truck stop</h3>
  <p>Loaded dump trailers are usually well over CAT’s 2,000 lb floor. CAT’s how-to page covers truck &amp; boat / trailer positioning (steer on platform 1, drive on 2, trailer on 3). Axle and gross weights, not corner weights. In California, go inside for a <strong>printed</strong> ticket if you need a weighmaster certificate — CAT’s Weigh My Truck PDF is not valid for that in CA. Link the locator; we do not republish CAT’s national file.</p>
  <p class="cite"><a href="https://catscale.com/how-to-weigh/">catscale.com/how-to-weigh</a> · <a href="https://catscale.com/cat-scale-locator/">CAT Scale locator</a></p>
  <h3>3. Landfill / transfer / quarry gate</h3>
  <p>These scales exist to charge by the ton for material going in (or out). CDFA’s public-scales list includes waste yards and rock companies that offer truck-weighing services — many will refuse a walk-up that is not their customer. Quarries and scrap yards are the same bucket. Call first. Do not invent hours, fees, or “they’ll give you a ticket.”</p>

  <h2>Call-ahead script</h2>
  <div class="script">
    <p>“Hi — I’m a civilian with a [size] dump trailer and a [pickup / truck]. I need a certified weighmaster ticket for [empty / loaded / both] weight. I am [dumping material at your facility / not dumping, just need the ticket]. Can you weigh that combination today? Do I need an account? Is there a fee? Do I get a printed certificate?”</p>
    <p>If they hesitate: “If you only weigh disposal traffic, that’s fine — can you point me to a public scale house that sells civilian tickets?”</p>
  </div>

  <h2>What to weigh</h2>
  <ol>
    <li>Empty trailer (or truck + empty trailer) on a quiet day — true empty, not the brochure weight.</li>
    <li>Loaded combination if you need net material weight or payload math. Stay hooked unless the scale tells you otherwise.</li>
    <li>Compare trailer GVWR, truck payload, and tongue weight. Close is not fine for a overloaded axle.</li>
  </ol>
  <p>Empty utility trailers under about 2,000 lb total combination belong at a dedicated house, not CAT.</p>

  <h2 class="section-h" id="landfills">Landfill / waste gates we list ({n})</h2>
  <p class="section-note">Compiled from CDFA waste rows, Riverside County Waste Resources, and City of San Diego Miramar pages. Gate hours below are dump-site hours where published — not a promise of a walk-up weighmaster ticket. Last re-checked {CHECKED_HUMAN} for Riverside County and Miramar.</p>
  <div class="table-wrap">
  <table>
    <caption>Call-first landfill / waste scales — dump traffic</caption>
    <thead>
      <tr><th>Site</th><th>Phone</th><th>Published gate hours</th><th>Ticket?</th><th>Source</th></tr>
    </thead>
    <tbody>
{table_rows}
    </tbody>
  </table>
  </div>

  <h2>County directories</h2>
  <ul>
    <li><a href="/los-angeles/">Los Angeles County</a> — dedicated houses + call-first waste/quarry rows</li>
    <li><a href="/orange-county/">Orange County</a> — CR&amp;R Stanton call-first; nearest walk-up often Santa Fe Springs</li>
    <li><a href="/inland-empire/">Inland Empire</a> — Colton Superior + Riverside County landfill gates</li>
    <li><a href="/san-diego/">San Diego County</a> — Allstate / Eckert’s + Miramar Landfill</li>
    <li><a href="/central-valley/">Central Valley</a> — Selma + Merced houses; landfills omitted until an official page claims public tickets</li>
    <li><a href="/phoenix/">Phoenix metro</a> — CAT only tonight; AZ landfill gates omitted (disposal weigh-ins, not published ticket shops)</li>
  </ul>

  <h2>What we could not verify tonight</h2>
  <ul>
    <li>Whether any Riverside County or Miramar gate will sell a civilian weighmaster certificate without disposing material.</li>
    <li>Fees at those gates for a ticket-only weigh (not published on the pages we checked).</li>
    <li>CDFA Ventura / Santa Barbara / San Joaquin facility grids (still WAF-blocked from this compile host).</li>
    <li>San Bernardino County landfill-hours table as a usable public list (still omitted rather than guessed).</li>
  </ul>
  <p><a href="/horse-trailer/">Horse trailer guide</a> · <a href="/cat-2000-lb-minimum/">Under 2,000 lb?</a> · <a href="/public-scale-vs-weigh-station/">Public scale vs weigh station</a></p>
</div>
</main>
"""


def page_catmin():
    return """
<main id="main">
<section class="page-head">
  <div class="wrap">
    <p class="kicker">CAT Scale rule</p>
    <h1>What CAT Scale’s 2,000 lb minimum means</h1>
    <p class="lede">If the combination is estimated under 2,000 pounds, CAT’s scale is set not to weigh it. Cars, empty utility trailers, motorcycle trailers, and some small boat trailers belong at a dedicated public scale house, not at a Pilot CAT.</p>
  </div>
</section>
<div class="wrap prose">
  <blockquote>Our scales are set to a weight threshold of 2,000 lbs. If your vehicle or combination is estimated to be lighter than 2,000 lbs, please call our 24-Hour Help Desk for assistance. 1-877-CAT-SCALE (228-7225), ext. 6.<cite> — CAT Scale, How To Weigh</cite></blockquote>
  <p>CAT’s FAQ repeats the band: vehicles between 2,000 lb and 200,000 lb. This is not a rude clerk. It is how the platform is set.</p>

  <h2>What usually fails the floor</h2>
  <ul>
    <li>A passenger car or small SUV for a DMV unladen certificate</li>
    <li>An empty 4×6 or 5×8 utility trailer, alone or behind a light truck if the combination still looks light to the scale</li>
    <li>A motorcycle trailer</li>
    <li>A small aluminum boat on a single-axle trailer</li>
    <li>Some camper vans and empty travel trailers that look heavier than they are</li>
  </ul>
  <p>A loaded 26-foot U-Haul, a fifth-wheel, a three-horse gooseneck, or a dump trailer with dirt is usually well over the floor. When in doubt, CAT says call the help desk before you occupy a truck-stop scale.</p>

  <h2>Where to go instead in Los Angeles County</h2>
  <p>Dedicated houses exist specifically for civilians who need a weighmaster certificate:</p>
  <ul>
    <li><a href="/los-angeles/#allstate-logistics-noho">Allstate Logistics, North Hollywood</a> — operator page says cars, motorcycles, trailers, RVs, boats; 70-foot in-ground scale; weekday 8–5; they publish a $25 certified-weight price (confirm).</li>
    <li><a href="/los-angeles/#certified-scales-llc">Certified Scales LLC, Jefferson Blvd</a> — CDFA list; operator site talks DMV and military certificates. Hours not posted on the page we checked. Call.</li>
    <li><a href="/los-angeles/#rawlins-public-scales">Rawlins Public Scales</a> — Mon–Fri 6 a.m.–6 p.m. on the operator site; 65-foot deck.</li>
    <li><a href="/los-angeles/#santa-fe-springs-public-scale">Santa Fe Springs Public Scale</a> — Mon–Fri 8 a.m.–midnight; first come, first served.</li>
  </ul>
  <p>Do not drive to the I-405 Carson CHP weigh station with a Honda and a hope. That is enforcement, not a $25 ticket.</p>
  <p class="cite"><a href="https://catscale.com/how-to-weigh/">catscale.com/how-to-weigh</a> · <a href="https://catscale.com/contact-us/faq/">CAT FAQ Q22 (weight threshold)</a> · <a href="https://amove.com/resource-center/public-scales/">Allstate public scales</a></p>
</div>
</main>
"""


def page_vs():
    return """
<main id="main">
<section class="page-head">
  <div class="wrap">
    <p class="kicker">Not legal advice · California</p>
    <h1>Public scale vs highway weigh station</h1>
    <p class="lede">One sells you a ticket. The other is CHP. Google Maps labels both “truck scale.” That mix-up burns a Saturday and can put a rental truck in an enforcement lane that cannot help you weigh a move.</p>
  </div>
</section>
<div class="wrap prose">
  <div class="box box-warn">
    <p><strong>This is a description of published agency pages, not advice about your citation, your U-Haul, or whether you must stop.</strong> For your vehicle, read Caltrans’ weigh-station page and ask CHP Commercial Vehicle Section, (916) 843-3400, or the facility listed on the Caltrans location PDF.</p>
  </div>

  <h2>Two different machines</h2>
  <p><strong>Public / CAT / dedicated scale house:</strong> a privately owned, licensed-weighmaster scale. You pay. You get a certificate. CDFA lists these for California. CAT operates a national truck-stop network. You go because you need a number for a PPM, a dump load, an RV payload, or a DMV unladen weight.</p>
  <p><strong>Highway weigh station / CVEF:</strong> California’s “Commercial Vehicle Enforcement Facilities,” run by the California Highway Patrol, not Caltrans. Caltrans publishes a primer because people call them by mistake. Signs tell commercial traffic to enter when the station is open. This is not a customer counter. ScaleRegistry lists the I-405N Carson station under “not public — listed so you do not drive to them.”</p>

  <h2>The U-Haul GVWR mix-up</h2>
  <p>Rental box trucks are often in a weight class people do not expect from the word “U-Haul.” Caltrans’ public FAQ says a rental truck (U-Haul, Ryder, Budget, Enterprise, and similar) is a motor truck under CVC 410 and must stop at weigh stations when signs require it, unless it is actually a pickup as defined in CVC 471. Caltrans also notes that most scale facilities post signs like “All Daily Rental/Moving Trucks Must Stop At Scales When Open.”</p>
  <p>That is about <em>enforcement stops when a CHP scale is open</em>. It is not a way to purchase a certified ticket for your PPM or to check whether the load is legal before you see an officer. If you want a ticket, go to a public scale or CAT. If you are approaching an open CHP station, follow the signs and CHP’s instructions — do not treat this directory as a bypass guide.</p>
  <p class="cite">Source: <a href="https://dot.ca.gov/programs/traffic-operations/cvef/weigh-stations">Caltrans, Weigh-Stations (Enforcement Facilities)</a> — CVC 2813, 260, 410, 471 discussion; rental-truck paragraph.</p>

  <h2>When you need a paid ticket</h2>
  <ul>
    <li>Military PPM / DITY empty and full weights</li>
    <li>DMV unladen / out-of-state truck registration in California</li>
    <li>RV payload, pin weight, axle weights</li>
    <li>Dump, landscape, or boat-trailer weight for your own records or a buyer</li>
  </ul>
  <p>CAT and dedicated houses exist for that. The Carson I-405 facility does not.</p>

  <h2>How to tell them apart on a map</h2>
  <ul>
    <li>CDFA public-scales list and CAT’s black-and-gold sign: ticket.</li>
    <li>Caltrans/CHP “weigh station” / CVEF: enforcement.</li>
    <li>If the pin sits on a freeway shoulder with CHP parking and no cashier booth you can walk up to, it is not WeighHere’s kind of listing.</li>
  </ul>
  <p><a href="/los-angeles/#do-not-go">Carson I-405 — do not go for a ticket</a> · <a href="/los-angeles/">LA public scales</a></p>
</div>
</main>
"""


def page_about():
    la = [s for s in STATIONS if s["county"] == "los-angeles"]
    oc = [s for s in STATIONS if s["county"] == "orange"]
    ie = [s for s in STATIONS if s["county"] in ("riverside", "san-bernardino")]
    sd = [s for s in STATIONS if s["county"] == "san-diego"]
    phx = [s for s in STATIONS if s["county"] == "maricopa"]
    cv = [s for s in STATIONS if s["county"] in ("kern", "fresno", "merced")]
    return f"""
<main id="main">
<section class="page-head">
  <div class="wrap">
    <p class="kicker">Directory notes</p>
    <h1>About WeighHere</h1>
    <p class="lede">An independent directory of places that will weigh a civilian rig and, when the operator is in the business of it, issue a certified ticket. Not a trucker app. Not CHP. Not CDFA.</p>
  </div>
</section>
<div class="wrap prose">
  <h2>What this is</h2>
  <p>WeighHere lists public and truck-stop scales for people who are not running a CDL for a living: U-Haul and moving trucks, RVs, horse trailers, boat and dump trailers, military PPM/DITY loads. The product is the filter Google does not have — will they weigh <em>this</em> rig, can you walk up, do you get a ticket you can use, and is this actually a cop scale.</p>
  <p>As of {CHECKED_HUMAN} the live geography is Los Angeles County (solid), Orange County (CDFA table, walk-up not verified), Inland Empire (ScaleRegistry Colton, two Love’s CAT stops, Riverside County landfills; CDFA Riverside/San Bernardino grids not loaded), San Diego County (Allstate Poway/Oceanside, Eckert’s San Marcos, Pilot Otay Mesa CAT, call-first transfer/landfill rows, San Onofre enforcement; CDFA San Diego c=37 grid not loaded), Phoenix metro / Maricopa (four CAT stops on Pilot/Flying J and Love’s own pages; no ScaleRegistry dedicated house; no AZ CDFA-equivalent facility grid), and Central Valley (Selma + Merced dedicated houses, four Kern CAT stops on Pilot/Love’s own pages; CDFA Kern/Fresno/Merced grids not loaded). Guide pages now include dump-trailer / landfill scales (call-first gate scales vs dedicated ticket shops).</p>

  <h2>Sources</h2>
  <ul>
    <li>California Department of Food and Agriculture, Division of Measurement Standards, public scales listing — county tables for Los Angeles (c=19) and Orange (c=30). Riverside (c=33), San Bernardino (c=36), San Diego (c=37), and Kern (c=15) URLs are known; the ASPX grids did not load on recent compiles (WAF / stripped grid): <a href="https://apps1.cdfa.ca.gov/publicscales/">apps1.cdfa.ca.gov/publicscales</a></li>
    <li>CAT Scale public how-to, FAQ, California Weighmaster Certificate page, and locator (we link the locator; we do not republish CAT’s full national list): <a href="https://catscale.com/how-to-weigh/">how-to-weigh</a>, <a href="https://catscale.com/cat-scale-locator/">locator</a></li>
    <li>Weigh My Truck help page on California PDFs: <a href="https://weighmytruck.com/Help">weighmytruck.com/Help</a></li>
    <li>Operator pages we fetched: Rawlins, Gabriel Container / Santa Fe Springs, Allstate Logistics / amove.com (North Hollywood, Poway, Oceanside), Pilot Flying J Castaic, Otay Mesa (#343), Phoenix Flying J #611, and Avondale #459, publicscales.net, Love’s #374 Barstow, Love’s #207 Coachella, Love’s #659 Tolleson, Love’s #328 Chandler, Love’s #830 Bakersfield, Love’s #230 Lost Hills, Love’s #392 Tehachapi, Pilot #613 Bakersfield, Selma Certified Public Scale, Eckert’s Moving San Marcos public scale, EDCO Station La Mesa, Truck Net Otay</li>
    <li>ScaleRegistry’s public-weighing page, including the Carson I-405 “not public” warning: <a href="https://scaleregistry.com/public-scales.html">scaleregistry.com/public-scales.html</a> (lists Selma and Merced among CA dedicated houses; no San Diego or Phoenix dedicated houses on that page as of this compile)</li>
    <li>Caltrans weigh-station (enforcement) primer and CVEF location list (San Onofre I-5): <a href="https://dot.ca.gov/programs/traffic-operations/cvef/weigh-stations">dot.ca.gov/…/weigh-stations</a></li>
    <li>City of Stanton / CR&amp;R facility hours (office hours, not a ticket promise)</li>
    <li>Riverside County Waste Resources landfill hours: <a href="https://rcwaste.org/routine-waste">rcwaste.org/routine-waste</a></li>
    <li>City of San Diego Miramar Landfill &amp; Greenery: <a href="https://www.sandiego.gov/environmental-services/miramar">sandiego.gov/…/miramar</a></li>
    <li>Arizona Department of Agriculture weighmaster licensing (not a facility list): <a href="https://agriculture.az.gov/weights-measures/licensing/weighmaster">agriculture.az.gov/…/weighmaster</a></li>
    <li>ADOT virtual port / POE enforcement pages (Sacaton I-10, Ehrenberg, San Simon): <a href="https://azdot.gov/mvd/services/enforcement/commercial-vehicle-permits/virtual-port-technology">Virtual Port Technology</a> · <a href="https://azdot.gov/mvd/services/enforcement/port-entry-locations">Port of Entry Locations</a></li>
  </ul>
  <p>We do not scrape Penske’s publicscaleslocator.com, Trucker Path, or AllStays. We do not copy competitor datasets.</p>

  <h2>CDFA accuracy</h2>
  <p>CDFA prints this on every county page: the Division attempts to maintain the highest accuracy of content but makes no claims, promises, or guarantees about the absolute accuracy, completeness, or adequacy of the information provided and expressly disclaims liability for errors and omissions. WeighHere is a compilation of that list plus public operator pages. Plants get sold. Hours rot. A quarry that weighed a dump truck in 2024 may wave you off in 2026.</p>

  <h2>Call ahead</h2>
  <p>Every useful listing still starts with a phone call. We flag industrial CDFA rows as call-first / may refuse walk-ups. We leave livestock and 24-hour as unknown unless a primary source said so. Missing is better than fake.</p>
  <p>Listings in this build: {len(la)} Los Angeles County rows (including one ScaleRegistry extra and one enforcement station), {len(oc)} Orange County CDFA rows, {len(ie)} Inland Empire rows (ScaleRegistry Colton, two Love’s CAT, Riverside County landfills), {len(sd)} San Diego County rows (three dedicated houses, one Pilot CAT, three call-first, one enforcement), and {len(phx)} Phoenix metro / Maricopa rows (four CAT stops), and {len(cv)} Central Valley rows (Selma + Merced dedicated, four Kern CAT). Last compiled {CHECKED_HUMAN}.</p>

  <h2>Affiliate disclosure (placeholder)</h2>
  <p>This site may later include affiliate links. Programs under consideration, not live, not verified here: U-Haul via CJ Affiliate, Amazon Associates, Tractor Supply via Partnerize/Pepperjam, Camping World via FlexOffers. There is no CAT Scale consumer affiliate program that we found. No affiliate IDs are embedded in this build. When links go live they will be marked.</p>

  <h2>Corrections</h2>
  <p>If a house turned you away, changed hours, or will weigh livestock, that is the data this directory is for. A public report form is not shipping in this build. Check the last-checked date on each listing. Nightly additions are documented in ADDING_A_PAGE.md in the source repo.</p>
</div>
</main>
"""


def write(path: Path, title, desc, current, rel, body, extra_head=""):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(header(current, rel, title, desc, extra_head) + body + footer(rel), encoding="utf-8")
    print("wrote", path.relative_to(ROOT))


def main():
    leaflet = LEAFLET
    write(
        ROOT / "index.html",
        "Public scales in Los Angeles County — U-Haul, RV, horse trailer | WeighHere",
        "Dedicated public scale houses, CAT and truck-stop scales, call-first plants, and the I-405 Carson weigh station you should not use for a ticket.",
        "la",
        "",
        la_body(),
        leaflet,
    )
    write(
        ROOT / "los-angeles" / "index.html",
        "Public scales in Los Angeles County — U-Haul, RV, horse trailer | WeighHere",
        "Dedicated public scale houses, CAT and truck-stop scales, call-first plants, and the I-405 Carson weigh station you should not use for a ticket.",
        "la",
        "../",
        la_body(),
        leaflet,
    )
    write(
        ROOT / "orange-county" / "index.html",
        "Orange County public scales | WeighHere",
        "CDFA Orange County public-scale list: seven call-first facilities, no verified dedicated civilian house in-county. Santa Fe Springs is the nearest walk-up we list.",
        "oc",
        "../",
        oc_body(),
        leaflet,
    )
    write(
        ROOT / "inland-empire" / "index.html",
        "Inland Empire public scales — Colton, Barstow, Coachella | WeighHere",
        "Superior Scale House in Colton, Love’s CAT Scales in Barstow and Coachella, and Riverside County landfill gates. CDFA Riverside and San Bernardino grids not loaded.",
        "ie",
        "../",
        ie_body(),
        leaflet,
    )
    write(
        ROOT / "san-diego" / "index.html",
        "San Diego County public scales — Poway, Oceanside, San Marcos, Otay Mesa | WeighHere",
        "Allstate Poway and Oceanside, Eckert’s San Marcos, Pilot Otay Mesa CAT Scale, EDCO La Mesa, Miramar Landfill, and San Onofre CHP enforcement. CDFA San Diego grid not loaded.",
        "sd",
        "../",
        sd_body(),
        leaflet,
    )
    write(
        ROOT / "phoenix" / "index.html",
        "Phoenix metro public scales — Pilot, Flying J, Love’s CAT | WeighHere",
        "Four CAT Scales verified on Pilot Flying J and Love’s own pages in Maricopa County. No ScaleRegistry dedicated house; no Arizona CDFA-equivalent facility grid.",
        "phx",
        "../",
        phoenix_body(),
        leaflet,
    )
    write(
        ROOT / "central-valley" / "index.html",
        "Central Valley public scales — Selma, Merced, Bakersfield CAT | WeighHere",
        "Selma Certified Public Scale, Highway 59 Scales in Merced, and Kern County CAT Scales at Pilot #613 and Love’s #830 / #230 / #392. CDFA Kern/Fresno/Merced grids not loaded.",
        "cv",
        "../",
        cv_body(),
        leaflet,
    )
    write(
        ROOT / "how-to-weigh-an-rv" / "index.html",
        "How to weigh an RV or fifth-wheel at a CAT Scale | WeighHere",
        "CAT platforms, no corner weights, 2,000 lb minimum, printed California weighmaster ticket. Cited from CAT’s how-to page.",
        "rv",
        "../",
        page_rv(),
    )
    write(
        ROOT / "ppm-dity-southern-california" / "index.html",
        "PPM / DITY weight tickets in Southern California | WeighHere",
        "Empty and full certified tickets, weighmaster signature, California printed certificate vs Weigh My Truck PDF. CAT, CDFA public houses, on-base.",
        "ppm",
        "../",
        page_ppm(),
    )
    write(
        ROOT / "horse-trailer" / "index.html",
        "Weigh a horse trailer: CAT vs mill vs landfill | WeighHere",
        "Do not unload horses at a Pilot. Call-ahead script. CAT vs dedicated public house vs grain mill. Livestock unknown unless sourced.",
        "horse",
        "../",
        page_horse(),
    )
    write(
        ROOT / "dump-trailer" / "index.html",
        "Dump trailer & landfill scales — call-first gates vs ticket shops | WeighHere",
        "When to use a dedicated public scale, CAT, or a landfill gate for a dump trailer. Riverside County and Miramar gate hours; walk-up tickets not verified.",
        "dump",
        "../",
        page_dump(),
    )
    write(
        ROOT / "cat-2000-lb-minimum" / "index.html",
        "CAT Scale 2,000 lb minimum — cars and light trailers | WeighHere",
        "CAT will not weigh under 2,000 lb. Where to take a car, empty utility trailer, motorcycle trailer, or small boat trailer in Los Angeles County.",
        "catmin",
        "../",
        page_catmin(),
    )
    write(
        ROOT / "public-scale-vs-weigh-station" / "index.html",
        "Public scale vs highway weigh station | WeighHere",
        "CAT and dedicated houses sell tickets. CHP weigh stations are enforcement. U-Haul GVWR mix-up described from Caltrans, not as legal advice.",
        "vs",
        "../",
        page_vs(),
    )
    write(
        ROOT / "about.html",
        "About WeighHere — sources, CDFA disclaimer, affiliate placeholder",
        "Independent public-scale directory. How listings are compiled, CDFA accuracy disclaimer, call-ahead policy, affiliate disclosure placeholder.",
        "about",
        "",
        page_about(),
    )

    (ROOT / "404.html").write_text(
        header("about", "", "Not found | WeighHere", "Page not found.")
        + """<main id="main"><section class="page-head"><div class="wrap">
        <h1>No page at this address</h1>
        <p class="lede">Start with <a href="/">Los Angeles County public scales</a>, <a href="/san-diego/">San Diego County</a>, <a href="/phoenix/">Phoenix metro</a>, <a href="/central-valley/">Central Valley</a>, <a href="/dump-trailer/">Dump trailer</a>, <a href="/inland-empire/">Inland Empire</a>, or <a href="/about.html">About</a>.</p>
        </div></section></main>"""
        + footer(""),
        encoding="utf-8",
    )
    print("wrote 404.html")


if __name__ == "__main__":
    main()
