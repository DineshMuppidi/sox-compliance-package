#!/usr/bin/env python3
"""
Markdown -> PDF renderer for the SOX Compliance Package.

Combines the four docs/*.md files (Control Design, Testing Procedures,
Evidence Collection, Audit Readiness) into a single audit-ready
outputs/sox-compliance-report.pdf, in the order listed in JOBS below, each
starting on a new page. Uses the pure-Python `markdown` + `weasyprint`
stack, so the PDF can be regenerated without a system pandoc/LaTeX install.

Run:  python3 docs/build-pdf.py
"""

from __future__ import annotations

import os
import re

import markdown
from weasyprint import HTML

DOCS_DIR = os.path.dirname(__file__)
OUT_DIR = os.path.join(DOCS_DIR, "..", "outputs")
os.makedirs(OUT_DIR, exist_ok=True)

REPORT_TITLE = "SOX Compliance Package"
REPORT_SUBTITLE = "IT General Control Design, Testing Procedures, Evidence Collection & Audit Readiness"

CSS = """
@page {
    size: Letter;
    margin: 2.2cm 1.8cm 2.4cm 1.8cm;
    @bottom-center {
        content: "SOX Compliance Package  |  Confidential - Internal Use  |  Page " counter(page) " of " counter(pages);
        font-size: 8pt;
        color: #595959;
    }
}
body {
    font-family: "Helvetica Neue", Arial, sans-serif;
    font-size: 11.5pt;
    line-height: 1.65;
    color: #1a1a1a;
}
h1 {
    color: #1F3864;
    font-size: 22pt;
    border-bottom: 3px solid #1F3864;
    padding-bottom: 6px;
    margin-top: 0;
    page-break-before: always;
}
h1:first-of-type { page-break-before: avoid; }
h2 {
    color: #1F3864;
    font-size: 16pt;
    margin-top: 22px;
    border-bottom: 1px solid #BFBFBF;
    padding-bottom: 3px;
}
h3 { color: #2E4E8C; font-size: 12pt; margin-top: 16px; }
p { margin: 6px 0; }
table {
    border-collapse: collapse;
    width: 100%;
    margin: 10px 0 16px 0;
    font-size: 9pt;
}
th {
    background-color: #1F3864;
    color: #ffffff;
    text-align: left;
    padding: 5px 7px;
}
td {
    border: 1px solid #BFBFBF;
    padding: 5px 7px;
    vertical-align: top;
}
tr:nth-child(even) td { background-color: #F2F2F2; }
strong { color: #1F3864; }
code {
    background-color: #F2F2F2;
    padding: 1px 4px;
    border-radius: 3px;
    font-size: 9pt;
}
hr { border: none; border-top: 1px solid #BFBFBF; margin: 18px 0; }
ul, ol { margin: 6px 0; padding-left: 22px; }
blockquote {
    border-left: 3px solid #1F3864;
    margin: 10px 0;
    padding: 4px 14px;
    color: #444;
    font-style: italic;
}
.titlepage {
    text-align: center;
    padding-top: 30%;
}
.titlepage h1 { border: none; font-size: 30pt; page-break-before: avoid; }
.titlepage .subtitle { font-size: 14pt; color: #595959; margin-top: 10px; }
.titlepage .meta { font-size: 10pt; color: #595959; margin-top: 40px; }
"""

FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

JOBS = [
    "SOX-Control-Design.md",
    "Testing-Procedures.md",
    "Evidence-Collection.md",
    "Audit-Readiness.md",
]


def parse_front_matter(text: str) -> tuple[dict, str]:
    m = FRONT_MATTER_RE.match(text)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"')
    return meta, text[m.end():]


def render_section(md_path: str) -> str:
    with open(md_path) as f:
        raw = f.read()
    _, body = parse_front_matter(raw)
    return markdown.markdown(body, extensions=["tables", "fenced_code", "sane_lists", "toc"])


def main():
    titlepage = f"""
    <div class="titlepage">
        <h1>{REPORT_TITLE}</h1>
        <div class="subtitle">{REPORT_SUBTITLE}</div>
        <div class="meta">Confidential &mdash; Internal Use | Generated 2026-08-21</div>
    </div>
    """
    sections = "".join(render_section(os.path.join(DOCS_DIR, name)) for name in JOBS)
    full_html = f"""<!doctype html><html><head><meta charset="utf-8">
    <style>{CSS}</style></head><body>{titlepage}{sections}</body></html>"""

    pdf_path = os.path.join(OUT_DIR, "sox-compliance-report.pdf")
    HTML(string=full_html, base_url=DOCS_DIR).write_pdf(pdf_path)
    print(f"Wrote {pdf_path}")


if __name__ == "__main__":
    main()
