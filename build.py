#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Design Issues book from data-catalogue.json + structure.py.

Chapter prose lives in content/NN-slug.html as a bare HTML fragment.
Any chapter with no fragment is emitted as a stub that still carries its
full provenance (original title, date, and a link to the source essay).

    python3 build.py        # regenerate index.html and chapters/
"""
import json, os, re, html, datetime
from structure import VOLUMES, FRONT_MATTER

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "Design Issues"
BASE = "https://www.w3.org/DesignIssues/"
REPO = "https://github.com/DesignIssues/design-issues"
AUTHOR_SRC = "Tim Berners-Lee"
EDITOR = "Melvin Carvalho"

cat = {e["href"]: e for e in json.load(open(os.path.join(ROOT, "data-catalogue.json")))}

STOP = {"a","an","the","of","and","or","to","in","on","is","it","for","what","why",
        "how","do","does","not","but","can","as","at","be","by","with","from"}

def slug(title):
    t = re.sub(r"[^a-z0-9\s-]", "", title.lower())
    words = [w for w in t.split() if w]
    keep = [w for w in words if w not in STOP] or words
    return "-".join(keep[:5])[:60].strip("-")

def esc(s):
    return html.escape(s, quote=True)

def year(d):
    return d[:4] if d else ""

# ---------------------------------------------------------------- assemble
chapters = []   # ordered list of dicts
n = 0
for vol in VOLUMES:
    for href in vol["chapters"]:
        e = cat[href]
        n += 1
        chapters.append(dict(
            n=n, href=href, title=e["title"], date=e["date"], words=e["words"],
            vol=vol, file="%02d-%s.html" % (n, slug(e["title"])),
        ))
by_href = {c["href"]: c for c in chapters}

def content_path(c):
    return os.path.join(ROOT, "content", c["file"])

def has_content(c):
    p = content_path(c)
    return os.path.exists(p) and os.path.getsize(p) > 200

# ---------------------------------------------------------------- templates
def head(title, desc, rel=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="{SITE}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<link rel="stylesheet" href="{rel}style.css">
</head>
<body>
"""

def source_note(c):
    d = c["date"]
    when = d if len(d) > 4 else (d or "undated")
    return f"""<div class="source-note">
<span class="source-label">Source</span>
<p>This chapter is about <a href="{BASE}{c['href']}"><em>{esc(c['title'])}</em></a>,
a Design Issues note by {AUTHOR_SRC}, dated {esc(when)}, about {c['words']:,} words.</p>
<p>Read the original at <a href="{BASE}{c['href']}">{BASE}{esc(c['href'])}</a>.
The Design Issues notes are {AUTHOR_SRC}'s personal notes and are not endorsed by W3C.
This book is commentary; where it quotes, it attributes.</p>
</div>
"""

def stub_note(c):
    return """<div class="status-stub">
<p><span class="status-label">In preparation.</span>
This chapter has not been written yet. Its place in the reading order is
fixed and its source is linked above, so the argument it must carry is
already determined. Contributions are welcome: see the
<a href="%s">repository</a>.</p>
</div>
""" % REPO

def chapter_html(c, prev, nxt):
    rel = "../"
    vol = c["vol"]
    title = f"Chapter {c['n']}: {c['title']} | {SITE}"
    desc = f"Chapter {c['n']} of {SITE}: {c['title']} ({year(c['date'])}). Volume {vol['num']}, {vol['title']}."
    out = [head(title, desc, rel)]
    out.append(f"""<nav class="chapter-nav">
<a href="{rel}index.html">Contents</a>
<span class="volume-indicator">Volume {vol['num']}: {esc(vol['title'])}</span>
</nav>

<header class="chapter-header">
<p class="chapter-number">Chapter {c['n']}</p>
<h1>{esc(c['title'])}</h1>
<p class="chapter-subtitle">{esc(year(c['date']))}</p>
</header>

<main class="chapter-content">
""")
    out.append(source_note(c))
    if has_content(c):
        out.append(open(content_path(c), encoding="utf-8").read().rstrip() + "\n")
    else:
        out.append(stub_note(c))
    out.append('<nav class="chapter-navigation">\n')
    if prev:
        out.append(f'<a href="{prev["file"]}">&larr; Chapter {prev["n"]}: {esc(prev["title"][:44])}</a>\n')
    else:
        out.append(f'<a href="{rel}index.html">&larr; Contents</a>\n')
    if nxt:
        out.append(f'<a href="{nxt["file"]}">Chapter {nxt["n"]}: {esc(nxt["title"][:44])} &rarr;</a>\n')
    else:
        out.append(f'<a href="{rel}index.html">Contents &rarr;</a>\n')
    out.append("</nav>\n</main>\n")
    out.append(f"""<footer>
<p>{SITE} &middot; Volume {vol['num']}: {esc(vol['title'])}</p>
<p>Commentary <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>
&middot; quoted material &copy; {AUTHOR_SRC}
&middot; <a href="{REPO}">contribute</a></p>
</footer>
</body>
</html>
""")
    return "".join(out)

# ---------------------------------------------------------------- index
def index_html():
    written = sum(1 for c in chapters if has_content(c))
    total = len(chapters)
    srcnotes = len(cat)
    words = sum(c["words"] for c in chapters)
    desc = (f"A book made from Tim Berners-Lee's Design Issues notes: "
            f"{total} chapters in ten volumes, in reading order, with editorial context.")
    o = [head(f"{SITE} | The Web's Design Notes, in Reading Order", desc)]
    o.append(f"""<div class="title-page">
<h1>Design Issues</h1>
<p class="subtitle">The Web's design notes, put in order</p>
<p class="ornament">&sect;</p>
<p class="description">
Between 1996 and 2024, {AUTHOR_SRC} wrote {srcnotes} notes on why the Web is
built the way it is. They were written as they were needed, not as a book,
and they are scattered across three decades and ten subjects. This is an
attempt to read them as one argument: in order, with the context each one
assumes, and with a note on what happened next.
</p>
<p class="author">Edited by {EDITOR}</p>
</div>

<blockquote class="epigraph">
each page may be an attempt to put across a given concept serially, but if
you are looking for an order of concepts and subconcepts, you have as much
hope as you would with words in the dictionary.
<span class="attribution">&mdash; {AUTHOR_SRC}, <em>Preface</em>, 1998</span>
</blockquote>

<section>
<h2>What this is</h2>
<p>
The Design Issues notes are the closest thing the Web has to a statement of
its own architecture by the person who designed it. They are also, as their
author says, personal notes: written to settle a question that was live at
the time, published when they were useful, and revised occasionally over
twenty-eight years. They are not endorsed by W3C, and they were never
arranged for a reader coming to them fresh.
</p>
<p>
That is the gap this book fills. Every note is assigned a chapter and a
place in a reading order, so that a term is defined before it is used and an
argument is met after the problem it solves. Each chapter gives the source
note, its date, and a link to the original; sets out what question it was
answering; and records what became of the answer. The originals remain where
they are and should be read there. Nothing here replaces them.
</p>
<p>
Every claim here is meant to be checkable. Each chapter names its source and
links to it, quotations are verified against the original word for word, and
statements about what happened afterwards carry the specification and the
date. Where the editor is reading rather than reporting, the text says so.
</p>
</section>

<div class="volume-overview">
<h3>The ten volumes</h3>
<ul class="volume-list">
""")
    for v in VOLUMES:
        first = by_href[v["chapters"][0]]["n"]
        last = by_href[v["chapters"][-1]]["n"]
        o.append(f"""<li><span class="vol-label">Volume {v['num']} &mdash; {esc(v['title'])}</span>
(Ch {first}&ndash;{last}). {esc(v['blurb'])}
<span class="vol-kind">{esc(v['epistemic'])}</span></li>
""")
    o.append("""</ul>
</div>

<section class="table-of-contents">
<h2>Contents</h2>
""")
    for v in VOLUMES:
        o.append(f'<div class="part">\n<h3>Volume {v["num"]} &mdash; {esc(v["title"])}</h3>\n')
        o.append(f'<p class="part-kind">{esc(v["epistemic"])}</p>\n<ol class="chapters">\n')
        for href in v["chapters"]:
            c = by_href[href]
            cls = "" if has_content(c) else ' class="toc-stub"'
            o.append(f'<li{cls}><span class="ch-num">{c["n"]}.</span>'
                     f'<a href="chapters/{c["file"]}">{esc(c["title"])}</a> '
                     f'<span class="ch-date">({esc(year(c["date"]))})</span>')
            if not has_content(c):
                o.append('<span class="chapter-desc">in preparation</span>')
            o.append("</li>\n")
        o.append("</ol>\n</div>\n")
    o.append(f"""</section>

<section>
<h2>Progress</h2>
<p>
The book is being written a volume at a time. Chapters marked
<em>in preparation</em> have their place and their source fixed but no prose
yet; they are listed so the shape of the whole is visible from the start.
</p>
<table>
<tr><th>Chapters written</th><td>{written} of {total}</td></tr>
<tr><th>Source notes catalogued</th><td>{srcnotes} (96 chapters, plus the Preface as front matter)</td></tr>
<tr><th>Words in the source notes</th><td>{words:,}</td></tr>
<tr><th>Earliest note</th><td>1996</td></tr>
<tr><th>Latest note</th><td>2024</td></tr>
</table>
</section>

<section>
<h2>On sources and permission</h2>
<p>
This is a work of commentary. Each chapter names its source note, links to
it, and quotes from it for the purpose of discussing it. Copyright in the
Design Issues notes remains with {AUTHOR_SRC}; the editorial matter here is
offered under
<a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>.
If the author would like anything changed or removed, that will be done.
</p>
</section>

<footer>
<p>{SITE} &middot; edited by {EDITOR} &middot;
<a href="{REPO}">source and corrections</a></p>
<p>Built {datetime.date.today().isoformat()}</p>
</footer>
</body>
</html>
""")
    return "".join(o)

# ---------------------------------------------------------------- write
def main():
    os.makedirs(os.path.join(ROOT, "chapters"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "content"), exist_ok=True)
    for i, c in enumerate(chapters):
        prev = chapters[i-1] if i > 0 else None
        nxt = chapters[i+1] if i < len(chapters)-1 else None
        open(os.path.join(ROOT, "chapters", c["file"]), "w", encoding="utf-8").write(
            chapter_html(c, prev, nxt))
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(index_html())
    w = sum(1 for c in chapters if has_content(c))
    print(f"built {len(chapters)} chapters ({w} written, {len(chapters)-w} stubs) + index.html")

if __name__ == "__main__":
    main()
