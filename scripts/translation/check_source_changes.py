#!/usr/bin/env python
"""Report which `.po` files a change to the English text could affect.

Run over a list of changed files by the GitHub Action ``track-english-changes.yml``,
which posts the report itself to a tracking issue once the change is on ``main``.

The tracking issue is the lowest numbered issue with the label ``po-refresh-tracker``.
"""

from __future__ import annotations

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
LOCALES_DIR = BASE_DIR / "locales"


MAX_ROWS = 20


def po_stems() -> set[str]:
    """Every ``.po`` name in the repository, without the extension."""
    return {po_file.stem for po_file in LOCALES_DIR.rglob("*.po")}


def english_source(stem: str) -> Path | None:
    """The English page or section a ``.po`` file is generated from."""
    page = BASE_DIR / f"{stem}.md"
    if page.is_file():
        return page
    section = BASE_DIR / stem
    return section if section.is_dir() else None


def translated_sources() -> dict[str, str]:
    """Map each repo-relative English source path to the ``.po`` stem it feeds."""
    found = {}
    for stem in po_stems():
        source = english_source(stem)
        if source is not None:
            found[str(source.relative_to(BASE_DIR))] = stem
    return found


def locale_codes() -> list[str]:
    """The locales with catalogs, in alphabetical order."""
    return sorted(path.name for path in LOCALES_DIR.iterdir() if path.is_dir())


def affected(
    changed: list[str], sources: dict[str, str] | None = None
) -> dict[str, list[str]]:
    """Group the changed paths by the ``.po`` stem whose source they belong to.

    In the current config, a source may be a single page or a whole section directory,
    so a path counts when it is the source itself or sits anywhere below it. Paths that
    do not belong to any known source are ignored.
    """
    known = translated_sources() if sources is None else sources
    hits: dict[str, list[str]] = {}
    for path in changed:
        for source, stem in known.items():
            if path == source or path.startswith(f"{source}/"):
                hits.setdefault(stem, []).append(path)
                break
    return {stem: sorted(paths) for stem, paths in sorted(hits.items())}


def render_report(hits: dict[str, list[str]], locales: list[str]) -> str:
    """The comment left on the tracking issue, or an empty string when no hits."""
    if not hits:
        return ""
    rows = sorted((path, stem) for stem, paths in hits.items() for path in paths)
    shown, hidden = rows[:MAX_ROWS], max(0, len(rows) - MAX_ROWS)
    table = "\n".join(f"| `{path}` | `{stem}.po` |" for path, stem in shown)
    more = f"\n\n{hidden} more changed file(s) are not listed." if hidden else ""
    listed = ", ".join(locales)
    return f"""### English text changed, catalogs (.po files) may need refreshing

A change on `main` touched English text of the guide so the `.po` files may need to be
refreshed by a maintainer.

| English source changed | Catalog it belongs to |
| :--- | :--- |
{table}{more}

To refresh the catalogs, one locale at a time:

```
nox -s update-language -- <locale>    # {listed}
```

Once the catalogs are refreshed, close the issue. The GitHub Action will reopen it when
new changes are made to the English text.

If this change did not touch any translatable text (e.g., code sample, image, link, format),
you can simply close the issue directly.
"""


def main(argv: list[str]) -> int:
    """Print the report for the paths listed in the file named by ``argv[1]``.

    Always succeeds (return 0). We do not fail in CI and cause a red mark on
    a pull request for something its author very likely did not do wrong.
    """
    if len(argv) != 2:
        print(f"usage: {Path(argv[0]).name} CHANGED_FILES", file=sys.stderr)
        return 0
    listing = Path(argv[1])
    changed = listing.read_text(encoding="utf-8").split() if listing.is_file() else []
    report = render_report(affected(changed), locale_codes())
    if report:
        print(report, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
