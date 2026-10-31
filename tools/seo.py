#!/usr/bin/env python3
"""SEO pass. Run after build.py (build.py calls it; netlify.toml too).

For every scale-listing page (a <dir>/index.html with station cards):
  * search-matching <title> and meta description built from the stations on it
  * a short data-driven intro paragraph (only facts from data/stations.json)
  * "Nearby pages" links to the 3 geographically closest pages not already linked
  * JSON-LD ItemList of the listed locations (name + PostalAddress)
Then: rebuilds index.html as a region hub (distinct from /los-angeles/) and
regenerates sitemap.xml with only final canonical URLs + <lastmod>.

New nightly page: add its slug to PLACES below ("City / City, ST" — keep the
whole title <= ~60 chars). Unknown slugs fall back to the page's <h1>.
Idempotent.
"""
import html, json, math, os, re, sys
from collections import Counter
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://weighhere.com"
SEO_UPDATED = "2026-10-13"  # bump when this pass changes page content site-wide

# slug -> (place used in title/description, state label for hub grouping)
PLACES = {
    "los-angeles": ("Los Angeles County, CA", "California"),
    "orange-county": ("Orange County, CA", "California"),
    "inland-empire": ("the Inland Empire, CA", "California"),
    "i-15": ("Hesperia & Barstow, CA", "California"),
    "coachella": ("Palm Springs & Blythe, CA", "California"),
    "ontario": ("Ontario & Fontana, CA", "California"),
    "imperial": ("El Centro & Brawley, CA", "California"),
    "antelope-valley": ("Palmdale & Lancaster, CA", "California"),
    "mojave": ("Tehachapi & Boron, CA", "California"),
    "san-diego": ("San Diego, CA", "California"),
    "sacramento": ("Sacramento, CA", "California"),
    "grapevine": ("the Grapevine / I-5, CA", "California"),
    "highway-99": ("Stockton & Lodi, CA", "California"),
    "madera": ("Madera, CA", "California"),
    "tulare": ("Tulare, CA", "California"),
    "bakersfield": ("Bakersfield, CA", "California"),
    "fresno": ("Fresno, CA", "California"),
    "merced": ("Merced, CA", "California"),
    "salinas": ("Salinas, CA", "California"),
    "weed-yreka": ("Weed & Yreka, CA", "California"),
    "corning-orland": ("Corning & Orland, CA", "California"),
    "buttonwillow-lost-hills": ("Buttonwillow, CA", "California"),
    "wheeler-ridge": ("Wheeler Ridge, CA", "California"),
    "santa-nella": ("Santa Nella, CA", "California"),
    "central-valley": ("the Central Valley, CA", "California"),
    "phoenix": ("Phoenix, AZ", "Arizona"),
    "casa-grande-eloy": ("Casa Grande & Eloy, AZ", "Arizona"),
    "gila-bend-yuma": ("Gila Bend & Yuma, AZ", "Arizona"),
    "quartzsite-ehrenberg": ("Quartzsite, AZ", "Arizona"),
    "kingman": ("Kingman, AZ", "Arizona"),
    "tucson-benson": ("Tucson & Benson, AZ", "Arizona"),
    "flagstaff-winslow": ("Flagstaff & Winslow, AZ", "Arizona"),
    "mayer": ("Mayer & Cordes Lakes, AZ", "Arizona"),
    "white-hills": ("White Hills, AZ", "Arizona"),
    "lake-havasu": ("Lake Havasu City, AZ", "Arizona"),
    "las-vegas": ("Las Vegas, NV", "Nevada"),
    "reno-sparks": ("Reno & Sparks, NV", "Nevada"),
    "elko-winnemucca": ("Elko & Winnemucca, NV", "Nevada"),
    "st-george-cedar-city": ("St. George & Cedar City, UT", "Utah"),
    "fillmore-nephi": ("Fillmore & Nephi, UT", "Utah"),
    "springville-salt-lake": ("Salt Lake City, UT", "Utah"),
    "brigham-ogden": ("Ogden & Brigham City, UT", "Utah"),
    "mccammon-idaho-falls": ("McCammon & Idaho Falls, ID", "Idaho"),
    "boise-treasure-valley": ("Boise & Treasure Valley, ID", "Idaho"),
    "twin-falls-burley": ("Twin Falls & Burley, ID", "Idaho"),
    "spokane-post-falls": ("Spokane, WA & Post Falls, ID", "Washington"),
    "north-bend-ellensburg": ("North Bend & Ellensburg, WA", "Washington"),
    "moses-lake-ritzville": ("Moses Lake & Ritzville, WA", "Washington"),
    "pasco-prosser": ("Pasco & Prosser, WA", "Washington"),
    "portland-troutdale": ("Portland, Troutdale & Aurora, OR", "Oregon"),
    "eugene-albany-roseburg": ("Eugene, Albany & Roseburg, OR", "Oregon"),
    "ontario-baker-city": ("Ontario & Baker City, OR", "Oregon"),
    "madras-klamath-falls": ("Madras & Klamath Falls, OR", "Oregon"),
    "biggs-boardman-stanfield": ("Biggs, Boardman & Stanfield, OR", "Oregon"),
    "medford-central-point": ("Medford & Central Point, OR", "Oregon"),
    "gallup-milan": ("Gallup & Milan, NM", "New Mexico"),
    "albuquerque": ("Albuquerque, NM", "New Mexico"),
    "moriarty-santa-rosa": ("Moriarty & Santa Rosa, NM", "New Mexico"),
    "tucumcari-glenrio": ("Tucumcari & Glenrio, NM", "New Mexico"),
    "belen-truth-or-consequences": ("Belen & Truth or Consequences, NM", "New Mexico"),
    "las-cruces-deming-lordsburg": ("Las Cruces, Deming & Lordsburg, NM", "New Mexico"),
}
STATE_NAMES = {"CA": "California", "AZ": "Arizona", "NV": "Nevada", "UT": "Utah", "ID": "Idaho", "WA": "Washington", "OR": "Oregon"}

INTRO_RE = re.compile(r'\n?<p class="seo-intro">.*?</p>', re.S)
LD_RE = re.compile(r'\n?<script type="application/ld\+json" data-seo>.*?</script>', re.S)
NEAR_RE = re.compile(r'\n?<li class="seo-near">.*?</li>', re.S)


def esc(s):
    return html.escape(s or "", quote=True)


def short(st):
    name = st["name"].split(" — ")[0]
    brand = re.split(r" Travel| Truck| Express| #", name)[0].strip()
    num = re.search(r"#\s?\d+", name)
    lab = f"{brand} {num.group(0)}" if num else name
    m = re.search(r"\b((?:I|US|UT|AZ|CA|NV)-\d+\w*|Hwy \d+)[^()]{0,25}?Exit (\d+\w?)", st.get("notes") or "")
    m2 = m or re.search(r"Exit (\d+\w?)", st.get("notes") or "")
    ex = f" (Exit {m2.groups()[-1]})" if m2 else ""
    return f"{lab} {st['city']}{ex}" if num else f"{lab}{ex}"


def page_stations(text, by_id):
    ids = re.findall(r'<(?:article class="card"|tr data-rig="[^"]*")[^>]*\bid="([^"]+)"', text)
    seen, out = set(), []
    for i in ids:
        if i in by_id and i not in seen:
            seen.add(i)
            out.append(by_id[i])
    return out


def describe(place, sts):
    good = [s for s in sts if not s.get("do_not_go")]
    lead = [s for s in good if s["type"] in ("cat", "dedicated_public", "truck_stop")] or good
    tail = " For RV, U-Haul, trailer & PPM weigh tickets."
    head = f"{len(good)} truck scales near {place}: "
    names, budget = [], 165 - len(head) - len(tail)
    for s in lead:
        t = short(s)
        if len(", ".join(names + [t])) > budget:
            break
        names.append(t)
    more = len(good) - len(names)
    body = ", ".join(names) + (f" + {more} more." if more > 0 else ".")
    return head + body + tail


def intro(place, sts):
    good = [s for s in sts if not s.get("do_not_go")]
    c = Counter(s.get("display_group") for s in good)
    t = Counter(s["type"] for s in good)
    parts = []
    if t["cat"] or t["truck_stop"]:
        parts.append(f"{t['cat'] + t['truck_stop']} CAT or truck-stop scale{'s' if t['cat'] + t['truck_stop'] != 1 else ''}")
    if t["dedicated_public"]:
        parts.append(f"{t['dedicated_public']} dedicated public scale house{'s' if t['dedicated_public'] != 1 else ''}")
    if c["call_first"]:
        parts.append(f"{c['call_first']} call-first site{'s' if c['call_first'] != 1 else ''} (landfills, quarries, recyclers)")
    cities = []
    for s in good:
        if s["city"] not in cities:
            cities.append(s["city"])
    s1 = f"This page lists {len(good)} places to weigh near {place}: " + ", ".join(parts) + "."
    s2 = (f"They are in {', '.join(cities[:-1])} and {cities[-1]}." if len(cities) > 1 else f"All are in {cities[0]}.") if cities else ""
    yes = sum(1 for s in good if s.get("certified_ticket_likely") == "yes")
    s3 = (f"{yes} {'is' if yes == 1 else 'are'} listed as likely to print a certified weight ticket, the kind PPM movers and RV owners checking weight ratings usually need. "
          "CAT platforms have a 2,000 lb minimum and do not give corner weights.") if yes else "Call ahead before driving over; none is confirmed to sell walk-up certified tickets."
    if len(cities) > 6:
        s2 = f"They are spread across {len(cities)} towns, including {', '.join(cities[:4])}."
    return " ".join(x for x in (s1, s2, s3) if x)


def jsonld(slug, title, sts):
    items = []
    for n, s in enumerate([s for s in sts if not s.get("do_not_go")], 1):
        addr = {"@type": "PostalAddress", "streetAddress": s["address"], "addressLocality": s["city"],
                "addressRegion": s["state"], "addressCountry": "US"}
        if s.get("zip"):
            addr["postalCode"] = s["zip"]
        place = {"@type": "Place", "name": s["name"].split(" — ")[0], "address": addr,
                 "url": f"{BASE}/{slug}/#{s['id']}"}
        if s.get("lat") is not None and s.get("lng") is not None:
            place["geo"] = {"@type": "GeoCoordinates", "latitude": s["lat"], "longitude": s["lng"]}
        items.append({"@type": "ListItem", "position": n, "item": place})
    data = {"@context": "https://schema.org", "@type": "ItemList", "name": title.split(" | ")[0],
            "url": f"{BASE}/{slug}/", "numberOfItems": len(items), "itemListElement": items}
    return '<script type="application/ld+json" data-seo>' + json.dumps(data, ensure_ascii=False).replace("</", "<\\/") + "</script>"


def centroid(sts):
    p = [(s["lat"], s["lng"]) for s in sts if s.get("lat") is not None and s.get("lng") is not None]
    return (sum(a for a, _ in p) / len(p), sum(b for _, b in p) / len(p)) if p else None


def dist(a, b):
    return math.hypot(a[0] - b[0], (a[1] - b[1]) * math.cos(math.radians(a[0])))


def main():
    st = json.load(open(os.path.join(ROOT, "data", "stations.json"), encoding="utf-8"))["stations"]
    by_id = {s["id"]: s for s in st}
    pages = {}
    for d in sorted(os.listdir(ROOT)):
        f = os.path.join(ROOT, d, "index.html")
        if not os.path.isfile(f):
            continue
        text = open(f, encoding="utf-8").read()
        sts = page_stations(text, by_id)
        if not sts or "leaflet" not in text:
            continue
        h1 = re.search(r"<h1>(.*?)</h1>", text, re.S)
        h1t = html.unescape(re.sub("<[^>]+>", "", h1.group(1))) if h1 else d
        if d in PLACES:
            place, region = PLACES[d]
        else:
            stc = Counter(s["state"] for s in sts).most_common(1)[0][0]
            place = re.sub(r"^Public scales (in|on|at|near) (the )?", "", h1t).strip() + f", {stc}"
            region = STATE_NAMES.get(stc, stc)
            print(f"seo: WARN {d} not in PLACES; using '{place}'", file=sys.stderr)
        pages[d] = dict(path=f, text=text, sts=sts, place=place, region=region, h1=h1t, c=centroid(sts))

    for d, p in pages.items():
        text, place, sts = p["text"], p["place"], p["sts"]
        title = f"CAT & Public Truck Scales near {place} | WeighHere"
        if len(title) > 62:
            title = f"CAT & Truck Scales near {place} | WeighHere"
        if len(title) > 62:
            title = f"Truck Scales near {place} | WeighHere"
        if len(title) > 62:
            title = f"CAT & Truck Scales near {place}"
        desc = describe(place, sts)
        text = re.sub(r"<title>.*?</title>", f"<title>{esc(title)}</title>", text, count=1, flags=re.S)
        text = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{esc(desc)}">', text, count=1)
        text = LD_RE.sub("", text)
        text = text.replace("</head>", jsonld(d, title, sts) + "\n</head>", 1)
        text = INTRO_RE.sub("", text)
        text = re.sub(r'(<p class="lede">.*?</p>)', lambda m: m.group(1) + f'\n    <p class="seo-intro">{esc(intro(place, sts))}</p>', text, count=1, flags=re.S)
        text = NEAR_RE.sub("", text)
        if p["c"]:
            others = sorted((dist(p["c"], q["c"]), k) for k, q in pages.items() if k != d and q["c"])
            add = [k for _, k in others if f'href="/{k}/"' not in text][:3]
            # only link real neighbours (within ~250 km)
            add = [k for k in add if dist(p["c"], pages[k]["c"]) < 2.3]
            lis = "".join(f'\n      <li class="seo-near"><a href="/{k}/">Nearby: {esc(pages[k]["h1"])}</a></li>' for k in add)
            if lis:
                if '<div class="related">' in text:
                    text = re.sub(r'(<div class="related">.*?<ul>)', lambda m: m.group(1) + lis, text, count=1, flags=re.S)
                else:
                    text = text.replace("</div>\n</main>", f'<div class="related"><h2>Nearby</h2><ul>{lis}\n</ul></div>\n</div>\n</main>', 1)
        open(p["path"], "w", encoding="utf-8").write(text)
        p["title"] = title

    # ---- homepage hub (distinct from /los-angeles/) ----
    idx = os.path.join(ROOT, "index.html")
    text = open(idx, encoding="utf-8").read()
    groups = {}
    for d, p in pages.items():
        groups.setdefault(p["region"], []).append((p["place"], d, len([s for s in p["sts"] if not s.get("do_not_go")])))
    total = len({s["id"] for p in pages.values() for s in p["sts"] if not s.get("do_not_go")})
    sec = []
    for region in ["California", "Arizona", "Nevada", "Utah", "Idaho", "Washington", "Oregon"] + sorted(set(groups) - set(STATE_NAMES.values())):
        if region not in groups:
            continue
        lis = "".join(f'<li><a href="/{d}/">{esc(pl)}</a> · {n} listing{"s" if n != 1 else ""}</li>' for pl, d, n in sorted(groups[region], key=lambda x: x[0].lower().replace("the ", "")))
        sec.append(f'<h2 class="section-h">{region}</h2>\n  <ul class="hub-list">{lis}</ul>')
    hub = f"""<main id="main">
<section class="page-head">
  <div class="wrap">
    <p class="kicker">California · Arizona · Nevada · Utah · Idaho · Washington · Oregon</p>
    <h1>Find a CAT scale or public truck scale near you</h1>
    <p class="lede">WeighHere lists {total} scales that will weigh a U-Haul, RV, travel trailer, horse trailer, or PPM move: CAT Scales at truck stops, dedicated public scale houses, and call-first plants. Pick the area you are driving through. Every listing links to its source, and we tell you which highway weigh stations not to use for a ticket.</p>
  </div>
</section>
<div class="wrap prose">
  {chr(10).join(sec)}
  <div class="related">
    <h2>Guides</h2>
    <ul>
      <li><a href="/guides/ppm-weight-tickets/">How to get PPM weight tickets for a U-Haul move</a></li>
      <li><a href="/guides/cat-scale-cost/">How much does a CAT Scale cost? Prices and how it works</a></li>
      <li><a href="/guides/tongue-weight/">How to weigh a travel trailer and check tongue weight</a></li>
      <li><a href="/how-to-weigh-an-rv/">How to weigh an RV or fifth-wheel at a CAT Scale</a></li>
      <li><a href="/ppm-dity-southern-california/">PPM / DITY weight tickets</a></li>
      <li><a href="/horse-trailer/">Weighing a horse trailer</a></li>
      <li><a href="/dump-trailer/">Dump trailer &amp; landfill scales</a></li>
      <li><a href="/cat-2000-lb-minimum/">CAT Scale 2,000 lb minimum</a></li>
      <li><a href="/public-scale-vs-weigh-station/">Public scale vs highway weigh station</a></li>
    </ul>
  </div>
</div>
</main>
"""
    text = re.sub(r'<main id="main">.*?(?=<footer)', lambda m: hub, text, count=1, flags=re.S)
    text = re.sub(r"<title>.*?</title>", "<title>CAT Scales &amp; Public Truck Scales Near You | WeighHere</title>", text, count=1, flags=re.S)
    text = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="Find a CAT scale or public truck scale near you in California, Arizona, Nevada, Utah, Idaho, Washington and Oregon. {total} listings for RVs, U-Haul moves, trailers and PPM weigh tickets.">', text, count=1)
    text = text.replace('<li><a href="/los-angeles/" aria-current="page">', '<li><a href="/los-angeles/">')
    text = re.sub(r'<link rel="stylesheet" href="https://unpkg.com/leaflet[^\n]*\n<script src="https://unpkg.com/leaflet[^\n]*\n', "", text)
    open(idx, "w", encoding="utf-8").write(text)

    # ---- sitemap ----
    old = {}
    sm = os.path.join(ROOT, "sitemap.xml")
    if os.path.exists(sm):
        for loc, lm in re.findall(r"<loc>([^<]+)</loc>\s*<lastmod>([^<]+)</lastmod>", open(sm).read()):
            old[loc] = lm
    urls = [BASE + "/"]
    order = re.findall(r"<loc>([^<]+)</loc>", open(sm).read()) if os.path.exists(sm) else []
    found = []
    for d in sorted(os.listdir(ROOT)):
        if d.startswith((".", "_")) or d in ("css", "js", "data", "tools", "node_modules"):
            continue
        if os.path.isfile(os.path.join(ROOT, d, "index.html")):
            found.append(f"{BASE}/{d}/")
        elif d.endswith(".html") and d not in ("index.html", "404.html"):
            found.append(f"{BASE}/{d}")
    gdir = os.path.join(ROOT, "guides")
    if os.path.isdir(gdir):
        for g in sorted(os.listdir(gdir)):
            if os.path.isfile(os.path.join(gdir, g, "index.html")):
                found.append(f"{BASE}/guides/{g}/")
    found = [u for u in order if u in found] + [u for u in found if u not in order]
    urls += [u for u in found if u != BASE + "/"]
    out = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        slug = u[len(BASE) + 1:].rstrip("/")
        lm = max(old.get(u, date.today().isoformat() if old else SEO_UPDATED), SEO_UPDATED)
        if slug in pages:
            lm = max([lm] + [s.get("last_checked") or "" for s in pages[slug]["sts"]])
        out.append(f"  <url><loc>{u}</loc><lastmod>{lm[:10]}</lastmod></url>")
    out.append("</urlset>")
    open(sm, "w").write("\n".join(out) + "\n")
    print(f"seo: {len(pages)} listing pages updated; sitemap {len(urls)} URLs")


if __name__ == "__main__":
    main()
