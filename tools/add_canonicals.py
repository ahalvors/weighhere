#!/usr/bin/env python3
"""Ensure every public HTML page has a self-referencing rel=canonical on the
https://weighhere.com host, matching the URL form listed in sitemap.xml.

  /index.html            -> https://weighhere.com/
  /<dir>/index.html      -> https://weighhere.com/<dir>/
  /<page>.html           -> https://weighhere.com/<page>.html

Idempotent: an existing canonical is replaced with the correct one.
Run after build.py (wired into netlify.toml).
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://weighhere.com"
SKIP = {"404.html"}
CANON_RE = re.compile(r'[ \t]*<link rel="canonical"[^>]*>\n?', re.I)

def url_for(rel):
    if rel == "index.html":
        return BASE + "/"
    if rel.endswith("/index.html"):
        return f"{BASE}/{rel[:-len('index.html')]}"
    return f"{BASE}/{rel}"

def main():
    changed = 0
    for dirpath, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if not d.startswith(".") and d not in ("node_modules", "tools", "data")]
        for f in files:
            if not f.endswith(".html"):
                continue
            rel = os.path.relpath(os.path.join(dirpath, f), ROOT).replace(os.sep, "/")
            if rel in SKIP:
                continue
            path = os.path.join(ROOT, rel)
            html = open(path, encoding="utf-8").read()
            tag = f'<link rel="canonical" href="{url_for(rel)}">'
            new = CANON_RE.sub("", html)
            new, n = re.subn(r"(</title>)", r"\1\n" + tag.replace("\\", "\\\\"), new, count=1, flags=re.I)
            if n == 0:
                new, n = re.subn(r"(</head>)", tag + r"\n\1", new, count=1, flags=re.I)
            if n == 0:
                print(f"WARN no <head> in {rel}", file=sys.stderr)
                continue
            if new != html:
                open(path, "w", encoding="utf-8").write(new)
                changed += 1
    print(f"add_canonicals: updated {changed} page(s)")

if __name__ == "__main__":
    main()
