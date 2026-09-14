# Design Issues

**Read it: https://designissues.github.io/design-issues/**

A book made from Tim Berners-Lee's
[Design Issues](https://www.w3.org/DesignIssues/) notes: 96 chapters in ten
volumes, put in a reading order, each with its source, its context, and a
note on what happened next.

Every claim is checkable: each chapter names its source and links to it,
quotations are verified against the original by a script, and statements
about what happened since carry the specification and the date.

## Why

Between 1996 and 2024, Berners-Lee wrote 97 notes on why the Web is built the
way it is. They are the closest thing the Web has to a statement of its own
architecture by the person who designed it. They were also written as they
were needed, published when they were useful, and never arranged for a reader
coming to them fresh. Their author says so in his own preface:

> if you are looking for an order of concepts and subconcepts, you have as
> much hope as you would with words in the dictionary.

This book supplies the order. Every note is assigned exactly one chapter, so
that a term is defined before it is used and an argument is met after the
problem it solves.

## Reading it without a background

No prior knowledge is assumed. Three things carry that weight:

- **A fifteen-chapter path.** Ninety-six chapters is a lot to begin with, and
  the reading order is the order in which the ideas depend on one another,
  not the order in which they are best met. The path on the title page picks
  fifteen that carry the whole argument, each with a line on what it gives.
- **A glossary.** Every term the book could not avoid is defined at
  `glossary.html` in plain words, written for somebody meeting it for the
  first time and not leaning on the other entries. The build links the first
  plain-prose use of each term in a chapter to its entry, so the definition
  is one click away at the moment it is first needed.
- **A short version.** The twenty-one chapters a reader is most likely to
  arrive at first open with a plain-language summary before the history
  starts, so the chapter can be understood before it is studied.

Those twenty-one are marked in the table of contents; the fifteen on the path
carry a flag as well.

## What a chapter contains

- **Source.** The original title, its date, and a link to it.
- **The short version.** On landmark chapters: the point, in plain words,
  before any history.
- **The question.** What was being argued about when it was written.
- **The argument.** The note restated in order, quoting where the wording
  matters.
- **What happened since.** What became of the proposal, with dates.
- **Connections.** Where the idea is used elsewhere in the book.
- **Questions.** Four, in place of exercises.

## Structure

| Volume | Subject | Chapters | Kind of claim |
|---|---|---|---|
| I | Axioms | 1–6 | design commitments, argued from first needs |
| II | Naming | 7–15 | architectural fact, checkable against the specs |
| III | Evolution | 16–26 | architectural fact and specification practice |
| IV | Meaning | 27–39 | proposal and specification |
| V | Logic and Notation | 40–48 | proposal and specification |
| VI | Linked Data and Solid | 49–65 | proposal, deployment record, contested present |
| VII | Trust | 66–74 | the contested present, attributed and dated |
| VIII | Law | 75–81 | normative argument, dated |
| IX | Interface and Society | 82–91 | design argument and social observation |
| X | Futures | 92–96 | disciplined speculation, labeled as such |

## Status

Complete. All 96 chapters are written, with 97 inline figures. Every note on
w3.org/DesignIssues has a chapter; the Preface is used as front matter.

What remains is correction and improvement: errata, better readings, better
figures, and updating the "what happened since" sections as things happen.

## Repository layout

- `index.html` — title page, the reading path, volume overview, full contents
- `glossary.html` — generated; the terms the book could not avoid
- `chapters/NN-*.html` — generated; do not edit by hand
- `content/NN-*.html` — the prose of each written chapter, as a fragment
- `structure.py` — volume and chapter assignment, the reading order, and the
  fifteen-chapter path with its blurbs
- `glossary.py` — the glossary entries, as plain data
- `data-catalogue.json` — every source note: title, date, length, URL
- `build.py` — regenerates `index.html` and `chapters/`
- `check_quotes.py` — verifies every quotation against w3.org
- `style.css` — one stylesheet for the whole book, including the diagram palette
- `og-image.svg` / `og-image.png` — the social card, referenced by every page

To build:

```sh
python3 build.py        # regenerate index.html, glossary.html and chapters/
python3 check_quotes.py # verify every quotation against its source note
```

`check_quotes.py` pulls every `<blockquote>` out of `content/`, fetches the
source note it belongs to from w3.org (cached in `.sources/`, not committed),
and fails if the quoted words are not in it. Differences in whitespace are
tolerated, because the source HTML wraps lines; anything else is reported.
Nothing is attributed to Berners-Lee in this book that does not pass it.

A chapter's prose lives in `content/NN-slug.html`, with the same basename as
the generated chapter file, as a bare HTML fragment. The build wraps it and
adds the source note, the navigation, and the collapsible Questions block.

## House standards

- A claim is quoted, cited, or marked as the editor's reading. Nothing is
  asserted in Berners-Lee's voice that he did not write, and every quotation
  is checked against the source by `check_quotes.py`.
- Quotations are verbatim, including the source's own typographical errors.
  Where a sentence is cut short, it is cut at a sentence boundary or marked.
- Perishable facts carry dates. "What happened since" entries name the
  specification, the body, and the month.
- Contested questions are reported as contested, with positions attributed.
- Calm "we"; no contractions; no second person outside the questions; colons
  rather than em-dashes.
- Every chapter links to its source note at the top. The originals are the
  authority; this book is commentary.
- Figures are inline SVG using only the palette defined in `style.css`, carry
  a `<title>` and `<desc>` for screen readers, and must stay legible at phone
  width. A figure earns its place by showing a mechanism the prose cannot.
- The Questions block is written as a plain `<div class="questions">`; the
  build wraps it in a `<details>` so readers can collapse it. Do not write the
  `<details>` by hand.
- A short version is written as a plain `<div class="plain">` at the very top
  of the fragment, before the editor's note. It assumes nothing, defines what
  it uses, and says what the chapter does rather than summarising its
  conclusions.
- Apostrophes and quotation marks in editorial prose are typographic. Inside
  a quotation they are left exactly as the source has them.
- Glossary links are generated, never written by hand. `link_glossary()` in
  `build.py` links each term once per chapter and skips quotations, headings,
  figures, code and existing links. To add a term, add it to `glossary.py`.
- The text column is 38rem, about seventy characters. Figures, tables and the
  panels on the title page bleed out of it by a clamp that reaches zero before
  the window narrows, so nothing overflows on a phone.

## Contributing

Corrections are contributions, and the factual claims here are checkable:
dates against the specifications cited, readings against the source notes,
which are one click away in every chapter.

- **Errata:** [open an issue](../../issues). Say which chapter and section,
  what the text claims, and what is wrong with it.
- **Chapters:** open an issue to claim one before writing it, so two people
  do not write the same chapter. Volumes are written in order.
- **Structure:** arguments about the reading order belong in an issue
  against `structure.py`.

## Sources and permission

This is a work of commentary. Every chapter names its source, links to it,
and quotes from it in order to discuss it. The Design Issues notes are Tim
Berners-Lee's personal notes and are not endorsed by W3C. Copyright in them
remains with him. If the author would like anything here changed or removed,
it will be done: open an issue, or write to the editor.

The editorial matter is licensed
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Edited by Melvin Carvalho.
