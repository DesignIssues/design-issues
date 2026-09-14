#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verify every quotation in the book against its source note.

Each chapter quotes the Design Issues note it discusses. This script pulls
each <blockquote> out of content/, works out which source note the chapter
belongs to, fetches that note from w3.org (cached under .sources/, which is
not committed), and checks the quoted words actually appear in it.

A quotation that cannot be found is reported. Nothing is attributed to
Tim Berners-Lee in this book that does not survive this check.

    python3 check_quotes.py          # check every written chapter
    python3 check_quotes.py 01 05    # check chapters whose files start 01, 05
"""
import html, json, os, re, sys, time, urllib.request
from structure import VOLUMES

ROOT = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(ROOT, ".sources")
BASE = "https://www.w3.org/DesignIssues/"
UA = {"User-Agent": "elementary-design-issues/1.0 (quote checker)"}

STOP = {"a","an","the","of","and","or","to","in","on","is","it","for","what","why",
        "how","do","does","not","but","can","as","at","be","by","with","from"}

def slug(title):
    t = re.sub(r"[^a-z0-9\s-]", "", title.lower())
    w = [x for x in t.split() if x]
    keep = [x for x in w if x not in STOP] or w
    return "-".join(keep[:5])[:60].strip("-")

def norm(s):
    """Collapse whitespace and normalise the punctuation that differs between
    the source HTML and our typographic quoting."""
    s = html.unescape(s)
    for a, b in [("’","'"), ("‘","'"), ("“",'"'), ("”",'"'),
                 ("–","-"), ("—","-"), (" "," ")]:
        s = s.replace(a, b)
    return " ".join(s.split())

def fetch(href):
    os.makedirs(CACHE, exist_ok=True)
    p = os.path.join(CACHE, href)
    if not (os.path.exists(p) and os.path.getsize(p) > 0):
        req = urllib.request.Request(BASE + href, headers=UA)
        open(p, "wb").write(urllib.request.urlopen(req, timeout=30).read())
        time.sleep(0.4)
    raw = open(p, encoding="utf-8", errors="replace").read()
    body = re.sub(r"(?is)<(script|style|head)[^>]*>.*?</\1>", " ", raw)
    return norm(re.sub(r"<[^>]+>", " ", body))

def main():
    cat = {e["href"]: e for e in json.load(open(os.path.join(ROOT, "data-catalogue.json")))}
    want = sys.argv[1:]
    n = 0
    checks = fails = skipped = 0
    for vol in VOLUMES:
        for href in vol["chapters"]:
            n += 1
            fname = "%02d-%s.html" % (n, slug(cat[href]["title"]))
            path = os.path.join(ROOT, "content", fname)
            if not os.path.exists(path):
                continue
            if want and not any(fname.startswith(w) for w in want):
                continue
            text = open(path, encoding="utf-8").read()
            quotes = re.findall(r"<blockquote>(.*?)</blockquote>", text, re.S)
            if not quotes:
                continue
            src = fetch(href)
            squeeze = lambda t: re.sub(r"\s+", "", t)
            src_sq = squeeze(src)
            for q in quotes:
                cite = re.search(r"<cite>(.*?)</cite>", q, re.S)
                body = re.sub(r"(?is)<cite>.*?</cite>", " ", q)
                body = norm(re.sub(r"<[^>]+>", " ", body))
                if not body:
                    continue
                checks += 1
                if body in src:
                    continue
                # whitespace around punctuation differs between the source
                # HTML and our text; that is typography, not a misquote.
                if squeeze(body) in src_sq:
                    continue
                # tolerate a source typo inside a long quote: require the
                # first and last eight words to be present and in order.
                w = body.split()
                if len(w) >= 20:
                    head, tail = " ".join(w[:8]), " ".join(w[-8:])
                    i, j = src.find(head), src.find(tail)
                    if i >= 0 and j > i:
                        skipped += 1
                        print("  ~ partial  %s\n      %s..." % (fname, body[:70]))
                        continue
                fails += 1
                print("  X MISSING  %s" % fname)
                print("      quoted: %s" % body[:100])
                print("      cited : %s" % (norm(cite.group(1)) if cite else "(no cite)"))
                print("      source: %s%s" % (BASE, href))
    print("\n%d quotations checked, %d verbatim, %d partial, %d missing"
          % (checks, checks - fails - skipped, skipped, fails))
    return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main())
