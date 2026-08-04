# Kairos — design notebook

The public notebook for **Kairos**, a proposed weak-signal detection and opportunity-evaluation
system. The idea in one line: don't look for things becoming popular, look for places where demand,
capability or behaviour is changing faster than supply can respond. Popularity is a late signal;
imbalance is the early one.

**Read it:** https://elifterminal.github.io/kairos-notebook/

This repo holds the page and nothing else. Kairos itself isn't built — the notebook is the record of
the design being argued over before anyone writes a collector. It's an open notebook, so the
objections and dead ends stay on the page next to whatever replaced them.

## Building

```sh
python3 src/gen_page.py        # content.py -> docs/index.html
python3 src/check_page.py      # verify the built page
python3 src/check_page.py --self-test   # verify the checks themselves fire
```

`src/content.py` is the single source of truth. Don't hand-edit `docs/index.html` — it gets
overwritten. Figures are hand-emitted inline SVG in `src/figures.py`; there's no chart library and
no image files, because the page has to be readable with no network and survive being pasted to
someone with no context.

`check_page.py` fails the build if the page stops naming its own project in the `<h1>`, if a title
goes generic, if anything reaches off-box, if a theme is missing, or if a tab loses its panel. The
`--self-test` mode feeds each check deliberately broken HTML and asserts it fires — a check nobody
has watched fail isn't a check.
