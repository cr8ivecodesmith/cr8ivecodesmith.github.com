[~cr8ivecodesmith]
==================

> There are only 2 important things in life:
>
> - Code
> - Coffee
> - Peanut butter
>
> ~ A programmer

[~cr8ivecodesmith]: https://mattlebrun.com

## Curriculum vitae PDF

The printable CV is generated from [`cv/index.html`](cv/index.html), using the
website's existing styles. Do not edit the PDF separately.

```sh
python -m pip install -r scripts/requirements-cv.txt
python scripts/generate_cv_pdf.py
```

The script writes `cv/matt-lebrun-cv.pdf`. Review the generated pages before
committing an updated PDF. The CV page links to this committed file, so changes
to the HTML require regenerating the PDF.

Two focused CVs use the same generator and their own HTML sources:

```sh
python scripts/generate_cv_pdf.py --source cv/engineering-leadership.html --output cv/matt-lebrun-engineering-leadership.pdf
python scripts/generate_cv_pdf.py --source cv/technical-education.html --output cv/matt-lebrun-technical-education.pdf
```

Edit the relevant HTML and regenerate its PDF when updating either version.
The HTML files are accessible on the static site, although they are not linked
from the main CV page. Review the PDF pages before committing.
