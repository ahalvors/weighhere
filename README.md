# WeighHere

Static directory of **public vehicle scales for civilians** — U-Haul and moving trucks, RVs, horse trailers, boat/dump trailers, and military PPM/DITY loads — with a certified ticket when they need one, and a red flag on highway enforcement weigh stations.

Homepage **is** the Los Angeles County page. Orange County is a thinner, honest CDFA table. Inland Empire is ScaleRegistry Colton + Love’s CAT + Riverside County landfills (CDFA grids not loaded).

## Live

- https://weighhere.netlify.app
- Source: https://github.com/ahalvors/weighhere

## Build

```bash
python3 build.py
```

Pages are generated from `data/stations.json`. See `ADDING_A_PAGE.md`.

## Nightly

One new county or guide page ships around 8pm PT.
