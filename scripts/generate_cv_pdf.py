#!/usr/bin/env python3
"""Generate an A4, searchable PDF from the website's published CV HTML.

Requires Python 3.10+ and WeasyPrint (see requirements-cv.txt).
Run from any working directory:
    python scripts/generate_cv_pdf.py

Optional overrides:
    python scripts/generate_cv_pdf.py --source cv/index.html --output /tmp/cv.pdf
"""
from __future__ import annotations

import argparse
from pathlib import Path

from weasyprint import HTML


def generate(source: Path, output: Path) -> Path:
    source = source.expanduser().resolve()
    output = output.expanduser().resolve()
    if not source.is_file():
        raise FileNotFoundError(f"CV HTML does not exist: {source}")
    output.parent.mkdir(parents=True, exist_ok=True)

    # HTML(filename=...) resolves ../css/site.css and ../css/cv.css relative
    # to cv/index.html; the existing @media print rules determine the layout.
    HTML(filename=str(source)).write_pdf(str(output))
    return output


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description="Render the website CV as an A4 PDF")
    parser.add_argument("--source", type=Path, default=root / "cv/index.html")
    parser.add_argument("--output", type=Path, default=root / "cv/matt-lebrun-cv.pdf")
    args = parser.parse_args()
    result = generate(args.source, args.output)
    print(f"Generated {result} ({result.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
