#!/usr/bin/env python3
"""Fail the build on the things a human forgets.

The living-page rules exist because we broke them before: a page went out titled "Asset Log",
which is a document type, not a project, and next to a properly-named sibling it read as
anonymous. So the naming rule is enforced here rather than trusted to memory.

Every check has a matching case in --self-test that feeds it deliberately broken HTML and
asserts the check actually fires. A check nobody has watched fail is not a check.

Usage:
    python src/check_page.py            # verify docs/index.html
    python src/check_page.py --self-test  # verify the checks themselves
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import content as C  # noqa: E402

PAGE = Path(__file__).resolve().parent.parent / "docs" / "index.html"

# A living page named with any of these identifies nothing — it would fit any other project
# unchanged. Constraint 0 of the format.
GENERIC = {
    "asset log", "log", "notebook", "findings", "index", "study", "notes",
    "record", "project", "docs", "report", "page", "results", "analysis",
}

# Anything that would make the page reach off-box at render time. The page must be readable
# with no network, forever.
EXTERNAL = re.compile(
    r"""(?:src|href)\s*=\s*["'](?!#)(https?:|//|data:image/svg\+xml;base64)"""
    r"""|@import|cdn\.|googleapis|unpkg|jsdelivr""",
    re.I,
)


class Failure(Exception):
    pass


def check_project_named(html: str) -> None:
    """Constraint 0: the h1 is the project name, the document type is a kicker above it."""
    if not C.PROJECT or not C.PROJECT.strip():
        raise Failure("content.PROJECT is empty — the page would be anonymous")
    if C.PROJECT.strip().lower() in GENERIC:
        raise Failure(f"content.PROJECT {C.PROJECT!r} is a generic noun; it identifies nothing")

    m = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S | re.I)
    if not m:
        raise Failure("no <h1> in the rendered page")
    h1 = re.sub(r"<[^>]+>", "", m.group(1)).strip()
    if C.PROJECT.lower() not in h1.lower():
        raise Failure(f"<h1> is {h1!r} but must contain the project name {C.PROJECT!r}")
    if h1.lower() in GENERIC:
        raise Failure(f"<h1> {h1!r} is a document type, not a project name")


def check_title(html: str) -> None:
    m = re.search(r"<title[^>]*>(.*?)</title>", html, re.S | re.I)
    if not m:
        raise Failure("no <title>")
    title = m.group(1).strip()
    if C.PROJECT.lower() not in title.lower():
        raise Failure(f"<title> {title!r} must contain the project name {C.PROJECT!r}")


def check_self_contained(html: str) -> None:
    hit = EXTERNAL.search(html)
    if hit:
        line = html[: hit.start()].count("\n") + 1
        raise Failure(f"external reference at line {line}: {hit.group(0)!r}")


def check_both_themes(html: str) -> None:
    if "prefers-color-scheme:dark" not in html.replace(" ", ""):
        raise Failure("no dark-theme block — both themes must be designed, not one plus an accident")
    if "--bg:" not in html:
        raise Failure("design tokens missing")


def check_tabs_wired(html: str) -> None:
    """Every tab must have a panel and every panel a tab. A dead tab is invisible until clicked."""
    tabs = set(re.findall(r'data-panel="([^"]+)"', html))
    panels = set(re.findall(r'<div class="panel[^"]*" id="([^"]+)"', html))
    if not tabs:
        raise Failure("no tabs found")
    if tabs != panels:
        raise Failure(f"tab/panel mismatch — tabs only: {tabs - panels}, panels only: {panels - tabs}")
    declared = {pid for pid, _ in C.TABS}
    if declared != tabs:
        raise Failure(f"rendered tabs {tabs} do not match content.TABS {declared}")


def check_exactly_one_active(html: str) -> None:
    if html.count('class="panel active"') != 1:
        raise Failure("exactly one panel must start active")


CHECKS = [
    ("project is named in the h1", check_project_named),
    ("title carries the project name", check_title),
    ("no external requests", check_self_contained),
    ("both themes designed", check_both_themes),
    ("tabs and panels agree", check_tabs_wired),
    ("one panel starts active", check_exactly_one_active),
]

# Deliberately broken pages, one per check, to prove the check fires.
GOOD = (
    '<title>Kairos &mdash; design notebook</title><style>:root{--bg:#fff}'
    "@media (prefers-color-scheme:dark){:root{--bg:#000}}</style>"
    '<h1>Kairos</h1><button data-panel="premise"></button>'
    '<div class="panel active" id="premise"></div>'
)
BROKEN = {
    "project is named in the h1": GOOD.replace("<h1>Kairos</h1>", "<h1>Findings</h1>"),
    "title carries the project name": GOOD.replace("Kairos &mdash; design notebook", "Design Notebook"),
    "no external requests": GOOD + '<script src="https://cdn.example.com/x.js"></script>',
    "both themes designed": GOOD.replace("@media (prefers-color-scheme:dark){:root{--bg:#000}}", ""),
    "tabs and panels agree": GOOD.replace('id="premise"', 'id="nowhere"'),
    "one panel starts active": GOOD + '<div class="panel active" id="second"></div>',
}


def self_test() -> int:
    bad = 0
    for name, fn in CHECKS:
        try:
            fn(BROKEN[name])
        except Failure:
            print(f"  ok    {name} — fires on broken input")
        else:
            print(f"  BROKEN{name} — did NOT fire on input designed to break it")
            bad += 1
    if bad:
        print(f"\n{bad} check(s) do not actually work.")
        return 1
    print("\nAll checks proven to fire.")
    return 0


def main() -> int:
    if "--self-test" in sys.argv:
        return self_test()

    if not PAGE.is_file():
        print(f"error: {PAGE} not built — run src/gen_page.py first", file=sys.stderr)
        return 1
    html = PAGE.read_text(encoding="utf-8")

    failed = 0
    for name, fn in CHECKS:
        try:
            fn(html)
        except Failure as exc:
            print(f"  FAIL  {name}: {exc}")
            failed += 1
        else:
            print(f"  ok    {name}")

    size = len(html.encode()) / 1024
    print(f"\n{PAGE.name}: {size:.1f} KB, {'FAILED' if failed else 'clean'}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
