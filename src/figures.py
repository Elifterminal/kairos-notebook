"""Hand-emitted inline SVG figures for the Kairos notebook.

No chart library and no image files — every figure is a string of SVG written into the page.
Colours come from CSS custom properties so the figures follow the light/dark theme without
needing a second copy. That's the whole reason for hand-emitting rather than rendering PNGs.
"""
from __future__ import annotations

import math

from content import STAGES, DETECT_FROM, DETECT_TO


def _esc(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def stage_ladder() -> str:
    """Awareness rises while remaining opportunity decays. The detector belongs where they cross.

    This is the figure that carries the argument, so it gets the most care: two curves on a
    shared x-axis of the seven stages, with the usable window shaded.
    """
    w, h = 1040, 430
    # Symmetric margins matter here: the stage captions are centre-anchored under each tick, so a
    # tight right margin pushes the last one ("Everyone hears about it") outside the viewBox.
    left, right = 78, w - 78
    top, base = 46, 300
    span = right - left
    step = span / (len(STAGES) - 1)

    def x_at(i: float) -> float:
        return left + i * step

    # Awareness: near-flat for a long time, then vertical. Logistic centred just past stage five.
    def awareness(i: float) -> float:
        return 1.0 / (1.0 + math.exp(-1.55 * (i - 4.35)))

    # Remaining opportunity: the mirror image, decaying as the crowd arrives.
    def remaining(i: float) -> float:
        return 1.0 - 1.0 / (1.0 + math.exp(-1.35 * (i - 3.55)))

    def path_for(fn) -> str:
        pts = []
        n = 240
        for k in range(n + 1):
            i = k * (len(STAGES) - 1) / n
            pts.append(f"{x_at(i):.1f},{base - fn(i) * (base - top):.1f}")
        return "M" + " L".join(pts)

    band_x0, band_x1 = x_at(DETECT_FROM - 1) - step * 0.42, x_at(DETECT_TO - 1) + step * 0.42

    parts = [
        f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="Awareness rises as remaining '
        f'opportunity decays; the detection window sits at stages two to four.">',
        "<defs>",
        '<linearGradient id="kw" x1="0" y1="0" x2="0" y2="1">',
        '<stop offset="0" stop-color="var(--ok)" stop-opacity=".17"/>',
        '<stop offset="1" stop-color="var(--ok)" stop-opacity=".03"/>',
        "</linearGradient>",
        "</defs>",
        # usable window
        f'<rect x="{band_x0:.1f}" y="{top - 22:.1f}" width="{band_x1 - band_x0:.1f}" '
        f'height="{base - top + 22:.1f}" fill="url(#kw)" stroke="var(--ok)" '
        'stroke-opacity=".45" stroke-dasharray="4 4"/>',
        f'<text x="{(band_x0 + band_x1) / 2:.1f}" y="{top - 29:.1f}" text-anchor="middle" '
        'font-size="13" font-weight="600" fill="var(--ok)">detection window</text>',
        # axes
        f'<line x1="{left}" y1="{base}" x2="{right}" y2="{base}" stroke="var(--line)" stroke-width="1.5"/>',
        f'<line x1="{left}" y1="{top - 22}" x2="{left}" y2="{base}" stroke="var(--line)" stroke-width="1.5"/>',
        # curves
        f'<path d="{path_for(remaining)}" fill="none" stroke="var(--accent)" stroke-width="2.6"/>',
        f'<path d="{path_for(awareness)}" fill="none" stroke="var(--warn)" stroke-width="2.6" '
        'stroke-dasharray="7 4"/>',
    ]

    # stage ticks and numerals
    for i, (num, title, _) in enumerate(STAGES):
        x = x_at(i)
        inside = DETECT_FROM <= i + 1 <= DETECT_TO
        colour = "var(--ok)" if inside else "var(--mut)"
        parts.append(
            f'<line x1="{x:.1f}" y1="{base}" x2="{x:.1f}" y2="{base + 7}" stroke="var(--line)"/>'
        )
        parts.append(
            f'<circle cx="{x:.1f}" cy="{base + 26:.1f}" r="12" fill="none" stroke="{colour}" '
            'stroke-width="1.6"/>'
        )
        parts.append(
            f'<text x="{x:.1f}" y="{base + 31:.1f}" text-anchor="middle" font-size="12.5" '
            f'font-weight="700" fill="{colour}">{num}</text>'
        )
        # two-line wrapped stage title
        words = title.split()
        mid = (len(words) + 1) // 2
        for line_no, chunk in enumerate((" ".join(words[:mid]), " ".join(words[mid:]))):
            if not chunk:
                continue
            parts.append(
                f'<text x="{x:.1f}" y="{base + 58 + line_no * 14:.1f}" text-anchor="middle" '
                f'font-size="11.5" fill="{colour}">{_esc(chunk)}</text>'
            )

    parts += [
        f'<text x="{x_at(0.15):.1f}" y="{base - remaining(0.15) * (base - top) - 14:.1f}" '
        'font-size="12.5" font-weight="600" fill="var(--accent)">opportunity remaining</text>',
        f'<text x="{x_at(5.05):.1f}" y="{base - awareness(5.05) * (base - top) - 14:.1f}" '
        'font-size="12.5" font-weight="600" fill="var(--warn)">public awareness</text>',
        f'<text x="{left - 10}" y="{top - 26}" text-anchor="end" font-size="11" '
        'fill="var(--mut)">high</text>',
        f'<text x="{left - 10}" y="{base}" text-anchor="end" font-size="11" fill="var(--mut)">low</text>',
        f'<text x="{x_at(5.6):.1f}" y="{base - 16:.1f}" text-anchor="middle" font-size="11.5" '
        'fill="var(--mut)">most trend tools measure here</text>',
        "</svg>",
    ]
    return "".join(parts)


def pipeline_reorder() -> str:
    """Two funnels: fit as a terminal multiplier versus fit as a front gate."""
    w, h = 900, 330
    parts = [
        f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="Comparing a pipeline that filters for '
        'fit last against one that filters for fit first.">'
    ]

    def funnel(x0: int, title: str, labels: list[str], widths: list[float], accent: str) -> None:
        parts.append(
            f'<text x="{x0 + 175}" y="26" text-anchor="middle" font-size="13.5" font-weight="700" '
            f'fill="{accent}">{_esc(title)}</text>'
        )
        y = 52
        for label, frac in zip(labels, widths):
            bw = 350 * frac
            cx = x0 + 175 - bw / 2
            parts.append(
                f'<rect x="{cx:.1f}" y="{y}" width="{bw:.1f}" height="34" rx="6" '
                f'fill="{accent}" fill-opacity="{0.10 + 0.10 * (1 - frac):.2f}" '
                f'stroke="{accent}" stroke-opacity=".55"/>'
            )
            parts.append(
                f'<text x="{x0 + 175}" y="{y + 22}" text-anchor="middle" font-size="12" '
                f'fill="var(--fg)">{_esc(label)}</text>'
            )
            y += 44

    funnel(
        20, "Fit last — everything gets processed",
        ["collect everything", "cluster + embed", "burst detect", "convergence", "agent evaluate", "fit ×  →  ~3%"],
        [1.0, 0.97, 0.94, 0.88, 0.82, 0.10],
        "var(--warn)",
    )
    funnel(
        500, "Fit first — only what you could act on",
        ["collect everything", "fit gate  →  ~3%", "evidence floor", "convergence", "card"],
        [1.0, 0.16, 0.13, 0.10, 0.07],
        "var(--ok)",
    )

    parts.append(
        f'<text x="{w / 2}" y="{h - 12}" text-anchor="middle" font-size="12" fill="var(--mut)">'
        "Same output. Twenty to thirty times less to collect, cluster, score and read.</text>"
    )
    parts.append("</svg>")
    return "".join(parts)


def source_matrix() -> str:
    """Sources placed on the two axes that decide inclusion: replayable history, and cost to fake."""
    w, h = 900, 470
    x0, y0, x1, y1 = 90, 50, w - 30, h - 66
    midx = (x0 + x1) / 2
    midy = (y0 + y1) / 2

    quadrants = [
        (x0, y0, "Build v1 on these", "var(--ok)", [
            "Federal Register / state bills",
            "Business formation stats",
            "Filings — capital spending",
        ]),
        (midx, y0, "Useful, but unverifiable", "var(--warn)", [
            "Job postings",
            "Procurement chatter",
        ]),
        (x0, midy, "Corroborate only", "var(--accent)", [
            "Code-hosting events (stars are buyable)",
            "Preprint metadata",
            "Technical news aggregators",
            "Consumer search — as saturation gauge",
        ]),
        (midx, midy, "Live enrichment, untested", "var(--mut)", [
            "Forums and chat communities",
            "Social platforms",
        ]),
    ]

    parts = [
        f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="Sources placed by whether they have a '
        'replayable archive and how expensive they are to fake.">',
        f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" fill="none" '
        'stroke="var(--line)" stroke-width="1.5" rx="8"/>',
        f'<line x1="{midx}" y1="{y0}" x2="{midx}" y2="{y1}" stroke="var(--line)" stroke-dasharray="5 5"/>',
        f'<line x1="{x0}" y1="{midy}" x2="{x1}" y2="{midy}" stroke="var(--line)" stroke-dasharray="5 5"/>',
    ]

    for qx, qy, label, colour, items in quadrants:
        parts.append(
            f'<text x="{qx + 18}" y="{qy + 28}" font-size="12.5" font-weight="700" '
            f'fill="{colour}">{_esc(label)}</text>'
        )
        for n, item in enumerate(items):
            parts.append(
                f'<circle cx="{qx + 24}" cy="{qy + 52 + n * 24}" r="3.4" fill="{colour}"/>'
            )
            parts.append(
                f'<text x="{qx + 36}" y="{qy + 56 + n * 24}" font-size="12" '
                f'fill="var(--fg)">{_esc(item)}</text>'
            )

    parts += [
        f'<text x="{x0 - 12}" y="{y0 + 34}" text-anchor="end" font-size="11.5" font-weight="600" '
        'fill="var(--mut)">expensive</text>',
        f'<text x="{x0 - 12}" y="{midy + 34}" text-anchor="end" font-size="11.5" font-weight="600" '
        'fill="var(--mut)">cheap</text>',
        # Axis title stays horizontal above the y labels. A rotated one collides with
        # "expensive"/"cheap" at this width, and rotation puts its bbox off-canvas.
        f'<text x="8" y="{y0 - 14}" font-size="11.5" font-weight="600" fill="var(--mut)">'
        "cost to fake &#8595;</text>",
        f'<text x="{(x0 + midx) / 2}" y="{y1 + 26}" text-anchor="middle" font-size="11.5" '
        'font-weight="600" fill="var(--mut)">has a replayable archive</text>',
        f'<text x="{(midx + x1) / 2}" y="{y1 + 26}" text-anchor="middle" font-size="11.5" '
        'font-weight="600" fill="var(--mut)">no usable history</text>',
        f'<text x="{w / 2}" y="{y1 + 50}" text-anchor="middle" font-size="12" fill="var(--mut)">'
        "The demand-side signals we most want are mostly in the right-hand column. That's the "
        "problem.</text>",
        "</svg>",
    ]
    return "".join(parts)
