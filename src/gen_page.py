#!/usr/bin/env python3
"""Render the Kairos design notebook to docs/index.html.

One source of truth in content.py, figures hand-emitted in figures.py, and nothing external:
no CDN, no web fonts, no analytics, no image files. The page has to survive being pasted to
someone with no context and read cold, so everything it needs travels inside it.

Usage:  python src/gen_page.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import content as C  # noqa: E402
import figures as F  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "docs" / "index.html"

CSS = """
*{box-sizing:border-box}
:root{--bg:#fbfbfc;--panel:#fff;--fg:#16181d;--mut:#636a76;--line:#e3e5ea;
      --accent:#2563eb;--warn:#dc2626;--ok:#15803d;--code:#f3f4f6;}
@media (prefers-color-scheme:dark){
 :root{--bg:#0d0f13;--panel:#14171d;--fg:#e9eaee;--mut:#98a0ad;--line:#262b34;
       --accent:#6ea0ff;--warn:#ff7a70;--ok:#68d391;--code:#1b1f26;}}
html,body{margin:0;padding:0}
body{background:var(--bg);color:var(--fg);
     font:15px/1.62 ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;
     -webkit-font-smoothing:antialiased}
.wrap{max-width:1120px;margin:0 auto;padding:48px 28px 96px}
header{border-bottom:1px solid var(--line);padding-bottom:22px;margin-bottom:8px}
.kicker{font-size:11.5px;letter-spacing:.13em;text-transform:uppercase;color:var(--mut);
        font-weight:700;margin:0 0 6px}
h1{font-size:38px;line-height:1.1;letter-spacing:-.02em;margin:0 0 10px;font-weight:750}
h2{font-size:22px;letter-spacing:-.02em;margin:38px 0 12px;font-weight:700}
h3{font-size:16.5px;letter-spacing:-.01em;margin:26px 0 8px;font-weight:700}
.sub{color:var(--mut);font-size:16px;max-width:74ch;margin:0}
.meta{color:var(--mut);font-size:12.5px;margin-top:12px}
p{max-width:80ch}
a{color:var(--accent)}
nav.tabs{display:flex;flex-wrap:wrap;gap:4px;border-bottom:1px solid var(--line);
         margin:20px 0 30px;padding-bottom:0}
button.tab{background:none;border:0;border-bottom:2px solid transparent;color:var(--mut);
           font:inherit;font-size:14px;font-weight:600;padding:10px 14px;cursor:pointer;
           margin-bottom:-1px;border-radius:6px 6px 0 0}
button.tab:hover{color:var(--fg);background:var(--panel)}
button.tab.active{color:var(--accent);border-bottom-color:var(--accent)}
.panel{display:none}
.panel.active{display:block}
.card{background:var(--panel);border:1px solid var(--line);border-radius:12px;
      padding:20px 22px;margin:18px 0}
.card h3{margin-top:0}
.read{border-left:3px solid var(--accent);background:var(--panel);border-radius:0 10px 10px 0;
      padding:14px 18px;margin:16px 0}
.read.warn{border-left-color:var(--warn)}
.read.ok{border-left-color:var(--ok)}
.read p{margin:0 0 8px}
.read p:last-child{margin-bottom:0}
.read .lbl{display:block;font-size:11.5px;letter-spacing:.09em;text-transform:uppercase;
           font-weight:700;color:var(--mut);margin-bottom:5px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(168px,1fr));gap:12px;margin:18px 0}
.stat{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:14px 16px}
.stat .n{font-size:25px;font-weight:750;letter-spacing:-.02em;display:block;line-height:1.2}
.stat .k{font-size:12.5px;color:var(--mut);display:block;margin-top:3px}
.tag{display:inline-block;font-size:11px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;
     padding:3px 8px;border-radius:99px;border:1px solid var(--line);color:var(--mut);
     vertical-align:middle}
.tag.ok{color:var(--ok);border-color:var(--ok)}
.tag.warn{color:var(--warn);border-color:var(--warn)}
.tag.bad{color:var(--warn);border-color:var(--warn);background:color-mix(in srgb,var(--warn) 12%,transparent)}
.tag.mut{color:var(--mut)}
table.survives{border-collapse:collapse;width:100%;font-size:13.5px;margin:16px 0}
table.survives th{text-align:left;text-transform:uppercase;font-size:11px;letter-spacing:.08em;
                  color:var(--mut);border-bottom:1px solid var(--line);padding:8px 10px;font-weight:700}
table.survives td{border-bottom:1px solid var(--line);padding:9px 10px;vertical-align:top}
table.survives td:first-child{white-space:nowrap;font-weight:600}
table.survives td:last-child{width:38%;color:var(--mut)}
.fig{overflow-x:auto;margin:22px 0;background:var(--panel);border:1px solid var(--line);
     border-radius:12px;padding:14px}
.fig svg{min-width:640px;width:100%;height:auto;display:block}
.fig.wide svg{min-width:1060px}
.fig figcaption{font-size:12.5px;color:var(--mut);margin-top:10px;padding:0 4px}
.q{border-left:3px solid var(--warn);padding:12px 18px;margin:16px 0;background:var(--panel);
   border-radius:0 10px 10px 0}
.q .qh{font-weight:700;margin:0 0 6px}
.jump-card{display:grid;gap:6px;margin:16px 0 26px}
@media(min-width:700px){.jump-card{grid-template-columns:1fr 1fr}}
a.jump{display:block;text-decoration:none;border:1px solid var(--line);border-radius:9px;
       padding:9px 13px;background:var(--panel);color:var(--fg);font-size:13.5px}
a.jump:hover{border-color:var(--accent)}
a.jump .jt{font-weight:650}
a.jump .jd{color:var(--mut);font-size:12px;display:block}
ul{max-width:80ch}
li{margin:5px 0}
footer{margin-top:56px;padding-top:20px;border-top:1px solid var(--line);color:var(--mut);
       font-size:12.5px}
code{background:var(--code);padding:1px 5px;border-radius:4px;font-size:13px}
"""

JS = """
document.querySelectorAll('button.tab').forEach(function(b){
  b.addEventListener('click', function(){
    document.querySelectorAll('button.tab').forEach(function(x){x.classList.remove('active')});
    document.querySelectorAll('.panel').forEach(function(x){x.classList.remove('active')});
    b.classList.add('active');
    document.getElementById(b.dataset.panel).classList.add('active');
    window.scrollTo({top:0,behavior:'smooth'});
  });
});
"""

WEIGHT_TAG = {
    "fatal": ('bad', 'fatal'),
    "high": ('warn', 'serious'),
    "med": ('mut', 'material'),
    "low": ('mut', 'minor'),
}


def fig(svg: str, caption: str, wide: bool = False) -> str:
    cls = "fig wide" if wide else "fig"
    return f'<figure class="{cls}">{svg}<figcaption>{caption}</figcaption></figure>'


def read(label: str, body: str, kind: str = "") -> str:
    cls = f"read {kind}".strip()
    return f'<div class="{cls}"><span class="lbl">{label}</span><p>{body}</p></div>'


def panel_premise() -> str:
    out = ["<h2>The idea, stated plainly</h2>"]
    out.append(
        "<p>Don't search for things that are becoming popular. Search for situations where demand, "
        "capability or behaviour is changing faster than supply can respond. Popularity is a late "
        "signal. Imbalance is the early one.</p>"
    )
    for label, body in C.PREMISE_READS:
        out.append(read(label, body))

    out.append("<h2>The seven stages</h2>")
    out.append(
        "<p>Emerging opportunities seem to move through a recognisable sequence. The point of "
        "naming the stages is not taxonomy — it's that it turns a vague instinct into a placement "
        "decision. You have to choose which stage your detector listens to, and that choice "
        "determines everything else about the system.</p>"
    )
    out.append(fig(
        F.stage_ladder(),
        "Public awareness and remaining opportunity move in opposite directions. The usable "
        "window sits where specialists are experimenting and money has started moving, but before "
        "the category has a name.",
        wide=True,
    ))

    rows = "".join(
        f"<tr><td>{n}. {t}</td><td>{d}</td>"
        f"<td>{'<span class=\"tag ok\">detect here</span>' if C.DETECT_FROM <= int(n) <= C.DETECT_TO else ''}</td></tr>"
        for n, t, d in C.STAGES
    )
    out.append(
        f'<table class="survives"><thead><tr><th>Stage</th><th>What it looks like</th>'
        f"<th></th></tr></thead><tbody>{rows}</tbody></table>"
    )

    out.append(f'<div class="card"><h3>{C.FADS_CARD["title"]}</h3><p>{C.FADS_CARD["body"]}</p>'
               f'<p>{C.FADS_CARD["tail"]}</p></div>')
    return "".join(out)


def panel_holds() -> str:
    out = [
        "<h2>What holds up</h2>",
        "<p>This notebook is mostly a critique, which risks giving a false impression of the "
        "design being critiqued. So this comes first. The proposal is better than most systems "
        "design of its kind, and these parts should survive into anything that gets built.</p>",
    ]
    for title, body in C.HOLDS:
        out.append(read(title, body, "ok"))
    return "".join(out)


def panel_breaks() -> str:
    out = [
        "<h2>Where it breaks</h2>",
        "<p>Nine objections, ordered by how much damage they do. The first one is different in "
        "kind from the rest — it's load-bearing for the whole design, and nothing downstream "
        "survives it intact.</p>",
    ]
    jumps = "".join(
        f'<a class="jump" href="#{b["id"]}"><span class="jt">{b["title"]}</span>'
        f'<span class="jd">{WEIGHT_TAG[b["weight"]][1]}</span></a>'
        for b in C.BREAKS
    )
    out.append(f'<div class="jump-card">{jumps}</div>')

    for b in C.BREAKS:
        tag_cls, tag_txt = WEIGHT_TAG[b["weight"]]
        out.append(f'<div class="card" id="{b["id"]}">')
        out.append(f'<h3>{b["title"]} <span class="tag {tag_cls}">{tag_txt}</span></h3>')
        out.append(f'<p>{b["claim"]}</p>')
        out.append(read("Why", b["why"], "warn"))
        if b["worse"]:
            out.append(read("And worse", b["worse"], "warn"))
        out.append(read("What to do instead", b["fix"], "ok"))
        out.append("</div>")

    out.append("<h2>The source problem, drawn</h2>")
    out.append(
        "<p>Two axes decide whether a source earns a place: can you replay its history to test "
        "anything, and how much does it cost someone to fake it. Sorting the candidates this way "
        "makes the central difficulty visible.</p>"
    )
    out.append(fig(
        F.source_matrix(),
        "Supply-side and capability signals are well archived. Demand-side signals — the ones the "
        "design leans on hardest — mostly are not. So the parts you most want to validate are the "
        "parts you cannot.",
    ))
    return "".join(out)


def panel_design() -> str:
    out = ["<h2>The one structural change worth making</h2>"]
    out.append(f'<div class="card"><h3>{C.REORDER["title"]}</h3>'
               f'<p>{C.REORDER["lede"]}</p><p>{C.REORDER["body"]}</p></div>')
    out.append(fig(
        F.pipeline_reorder(),
        "Fit as a terminal multiplier means fully processing everything and then discarding most "
        "of it. Fit as a front gate means never touching it.",
    ))
    out.append(read("Why it also raises precision", C.REORDER["kicker"], "ok"))

    out.append("<h2>Pipeline order</h2>")
    rows = "".join(
        f"<tr><td>{i}. {name}</td><td>{desc}</td><td></td></tr>"
        for i, (name, desc) in enumerate(C.PIPELINE, 1)
    )
    out.append(
        f'<table class="survives"><thead><tr><th>Step</th><th>What it does</th><th></th></tr>'
        f"</thead><tbody>{rows}</tbody></table>"
    )

    out.append("<h2>Sources for a first version</h2>")
    rows = "".join(
        f"<tr><td>{name}</td>"
        f'<td>{note}</td>'
        f'<td><span class="tag {"ok" if arch == "yes" else "warn"}">'
        f'{"replayable" if arch == "yes" else "live only"}</span> '
        f'<span class="tag mut">fake cost: {cost}</span></td></tr>'
        for name, arch, cost, note in C.SOURCES
    )
    out.append(
        f'<table class="survives"><thead><tr><th>Source</th><th>Why</th><th>Properties</th></tr>'
        f"</thead><tbody>{rows}</tbody></table>"
    )

    out.append("<h2>What is possible, and what isn't</h2>")
    for kind, title, body in C.FEASIBILITY:
        css = {"ok": "ok", "warn": "", "bad": "warn"}[kind]
        out.append(read(title, body, css))
    out.append(read("The binding constraint", C.BINDING_CONSTRAINT, "warn"))

    out.append('<div class="card"><h3>The commitment that makes it checkable</h3>'
               "<p>Every card gets written to a dated, append-only log with a falsifiable claim and "
               "its kill conditions, reviewed at ninety and one hundred eighty days. Without that, "
               "the system can run for a year and never answer whether it beats a coin flip.</p>"
               "<p>And the shutdown rule gets agreed in advance, while it's still cheap to be "
               "objective: after eight weeks, if the digest hasn't produced one candidate that led "
               "to a real action, and the ninety-day review shows no call that landed, it gets "
               "turned off. Not tuned. Turned off.</p></div>")
    return "".join(out)


def panel_open() -> str:
    out = [
        "<h2>Open questions</h2>",
        "<p>Things this notebook does not know. They're listed because an open notebook that only "
        "records conclusions isn't one.</p>",
    ]
    for q, body in C.OPEN_QUESTIONS:
        out.append(f'<div class="q"><p class="qh">{q}</p><p>{body}</p></div>')
    return "".join(out)


def panel_built() -> str:
    out = ["<h2>What the build found</h2>", f"<p>{C.BUILT_LEDE}</p>"]

    out.append("<h2>Where the argument held, or got stronger</h2>")
    for title, body in C.BUILT_CONFIRMED:
        out.append(read(title, body, "ok"))

    out.append(f'<h2>{C.BUILT_BUGS["title"]}</h2>')
    out.append(f'<p>{C.BUILT_BUGS["lede"]}</p>')
    for title, body in C.BUILT_BUGS["items"]:
        out.append(read(title, body, "warn"))

    out.append(f'<div class="card"><h3>{C.BUILT_DISCIPLINE["title"]}</h3>'
               f'<p>{C.BUILT_DISCIPLINE["body"]}</p>'
               f'<p>{C.BUILT_DISCIPLINE["tail"]}</p></div>')

    out.append("<h2>The design's author reviewed this page</h2>")
    out.append(f"<p>{C.REVIEW['lede']}</p>")
    r = C.REVIEW["refuted"]
    out.append(f'<div class="card"><h3>{r["title"]} <span class="tag warn">refuted</span></h3>'
               f'<p>{r["body"]}</p><p>{r["tail"]}</p></div>')
    for title, body in C.REVIEW["adopted"]:
        out.append(read(title, body, "ok"))
    pb = C.REVIEW["pushback"]
    out.append(f'<div class="card"><h3>{pb["title"]}</h3>'
               f'<p>{pb["body"]}</p><p>{pb["tail"]}</p></div>')

    rg = C.RADAR_GATE
    out.append("<h2>It turned out to be two systems</h2>")
    out.append(f'<p>{rg["lede"]}</p>')
    out.append(fig(F.radar_and_gate(),
                   "The split matters because a thin week could mean Radar found nothing or Gate "
                   "rejected everything — and those call for opposite responses."))
    for key in ("radar", "gate"):
        part = rg[key]
        out.append(f'<div class="card"><h3>{part["title"]}</h3><p>{part["body"]}</p>'
                   f'<p>{part["judged"]}</p></div>')
    for title, body in rg["why"]:
        out.append(read(title, body))
    out.append(f'<div class="read ok"><p>{rg["status"]}</p></div>')

    a = C.ADJACENCY
    out.append(f'<h2>{a["title"]}</h2>')
    out.append(f'<p>{a["lede"]}</p>')
    for title, body in a["items"]:
        out.append(read(title, body, "warn"))

    c = C.CONTAMINATION
    out.append(f'<div class="card"><h3>{c["title"]} <span class="tag bad">caught late</span></h3>'
               f'<p>{c["body"]}</p><p>{c["tail"]}</p></div>')

    out.append("<h2>What still cannot be claimed</h2>")
    for title, body in C.BUILT_STILL_UNPROVEN:
        out.append(f'<div class="q"><p class="qh">{title}</p><p>{body}</p></div>')

    return "".join(out)


def panel_reply() -> str:
    out = ["<h2>For the design's author</h2>", f"<p>{C.REPLY_TO_CHATGPT['lede']}</p>"]
    for title, body in C.REPLY_TO_CHATGPT["points"]:
        out.append(read(title, body))
    out.append(
        '<div class="card"><h3>What a useful reply looks like</h3><p>Not a defence and not a '
        "concession — a counter-argument with a mechanism. The most valuable possible response is "
        "to the archive asymmetry: name one demand-side source with genuine replayable history, "
        "and this design gets materially better in a way no modelling change could match.</p></div>"
    )
    return "".join(out)


PANELS = {
    "premise": panel_premise,
    "holds": panel_holds,
    "breaks": panel_breaks,
    "design": panel_design,
    "open": panel_open,
    "built": panel_built,
    "reply": panel_reply,
}


def build() -> str:
    tabs = "".join(
        f'<button class="tab{" active" if i == 0 else ""}" data-panel="{pid}">{label}</button>'
        for i, (pid, label) in enumerate(C.TABS)
    )
    panels = "".join(
        f'<div class="panel{" active" if i == 0 else ""}" id="{pid}">{PANELS[pid]()}</div>'
        for i, (pid, _) in enumerate(C.TABS)
    )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{C.PROJECT} &mdash; {C.DOC_TYPE.lower()}</title>
<meta name="description" content="{C.SUBTITLE}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%232563eb'/%3E%3Ctext x='16' y='23' font-family='system-ui,sans-serif' font-size='20' font-weight='700' fill='%23fff' text-anchor='middle'%3EK%3C/text%3E%3C/svg%3E">
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
<header>
  <p class="kicker">{C.DOC_TYPE}</p>
  <h1>{C.PROJECT}</h1>
  <p class="sub">{C.SUBTITLE}</p>
  <p class="meta">Updated {C.UPDATED} &middot; open notebook &mdash; objections and dead ends stay
  on the page, in their original wording, next to whatever replaced them.</p>
</header>
<nav class="tabs">{tabs}</nav>
{panels}
<footer>
  <p>{C.PROJECT} is built and running. Its operator-fit layer is already useful; its
  weak-signal layer has validated nothing and will stay unvalidated until a prediction log has
  accumulated and a replay has run. Those are two different claims and the page tries hard not to
  let the first one flatter the second. The design argument in the first five tabs is preserved
  exactly as written before any code existed — corrections attach, they never replace, and the
  errors stay up in their original wording.</p>
  <p>Generated from <code>src/content.py</code>. No external requests, no trackers, no fonts.</p>
</footer>
</div>
<script>{JS}</script>
</body>
</html>
"""


def main() -> int:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    html = build()
    OUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUT} ({len(html.encode()) / 1024:.1f} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
