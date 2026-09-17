#!/usr/bin/env python3
"""Translation statistics for the guide's ``.po`` files.

This module computes the translation counts and percentages. It is used by:

* ``_ext/translation_graph.py`` to build the site's translation heatmap.
* ``update_translation_issues.py`` to update the GitHub translation issues.

It can also be run as a script outputting the stats dataset as JSON on stdout.

Note: a string counts as *translated* only when it has a non-empty translation and is
**not** marked ``fuzzy``.
"""

from __future__ import annotations

import functools
import json
import math
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Annotated as A
from typing import TypeAlias, TypedDict

from babel.messages import pofile

# scripts/translation/stats.py -> repository root
BASE_DIR = Path(__file__).resolve().parents[2]
LOCALES_DIR = BASE_DIR / "locales"

# Timeout for the individual git calls used to date the English sources.
GIT_TIMEOUT = 10


class PoFileStats(TypedDict):
    """Counts for a single ``.po`` file.

    ``stale`` and ``missing`` describe how well the catalog tracks the current
    English text; see :func:`get_translation_stats` for how they are derived.
    """

    total: int
    translated: int
    fuzzy: int
    untranslated: int
    percentage: float
    stale: bool
    missing: int


TranslationStats: TypeAlias = dict[
    A[str, "locale"], dict[A[str, "po_file"], PoFileStats]
]


def english_source(po_file: str) -> Path | None:
    """Return the English source a ``.po`` file was generated from.

    Each ``.po`` file should correspond to either a top-level page (``index.md``)
    or a section directory (``documentation/``). A ``.po`` file with neither is
    one whose English source has since been removed -- e.g.,
    ``continuous-integration`` is discontinued: it still has ``.po``
    files on disk, but no translation work should be reported against it.
    """
    page = BASE_DIR / f"{po_file}.md"
    if page.is_file():
        return page
    section = BASE_DIR / po_file
    if section.is_dir():
        return section
    return None


def get_po_files() -> list[Path]:
    """Every ``.po`` file across all locales, in a stable order.

    Note that discontinued ``.po`` files are included here.
    :func:`get_translation_stats` does the filtering.
    """
    return sorted(LOCALES_DIR.rglob("*.po"))


def _as_aware(value: datetime | None) -> datetime | None:
    """Normalize to an aware datetime."""
    if value is None:
        return None
    if value.tzinfo is None:
        return value.replace(tzinfo=timezone.utc)
    return value


def _git(*args: str) -> str | None:
    """Run a read-only git command, returning ``None`` if it cannot be used.

    Note: this must not raise errors, because it runs inside the Sphinx build
    and if an error occurs (git is missing) the build must not fail over a
    check for .po staleness.
    """
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=BASE_DIR,
            capture_output=True,
            text=True,
            timeout=GIT_TIMEOUT,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    if result.returncode != 0:
        return None
    return result.stdout.strip() or None


@functools.lru_cache(maxsize=1)
def git_history_available() -> bool:
    """Whether git history is deep enough to date the English sources.

    ``actions/checkout`` clones with ``fetch-depth: 1`` by default, which leaves
    no usable history. Callers should surface a negative answer rather than
    imply that nothing is stale -- "we could not check" is not "all current".
    """
    return _git("rev-parse", "--is-shallow-repository") == "false"


@functools.lru_cache(maxsize=None)
def source_last_modified(po_file: str) -> datetime | None:
    """When the ``.po`` file's English source was last committed, if knowable."""
    source = english_source(po_file)
    if source is None or not git_history_available():
        return None
    stamp = _git("log", "-1", "--format=%cI", "--", str(source))
    if stamp is None:
        return None
    try:
        return _as_aware(datetime.fromisoformat(stamp))
    except ValueError:
        return None


def _count(catalog) -> dict[str, int | float]:
    """Count strings in an already-parsed catalog."""
    total = translated = fuzzy = 0
    for message in catalog:
        if not message.id:
            continue  # the header entry carries no source string
        total += 1
        if message.fuzzy:
            fuzzy += 1
        elif message.string:
            translated += 1

    # Floor instead of round: a catalog at 99.996% must not report 100,
    # because that would imply it is complete when it is not.
    percentage = math.floor(translated / total * 10000) / 100 if total else 0.0
    return {
        "total": total,
        "translated": translated,
        "fuzzy": fuzzy,
        "untranslated": total - translated - fuzzy,
        "percentage": percentage,
    }


def calculate_translation_percentage(po_path: Path, locale: str) -> PoFileStats:
    """Counts for a single ``.po`` file, read in isolation.

    ``stale`` and ``missing`` are reported as "not stale" here because detecting
    staleness requires comparing a ``.po`` file against its siblings in other
    locales. Use :func:`get_translation_stats` when those fields matter.
    """
    with open(po_path, "r", encoding="utf-8") as f:
        catalog = pofile.read_po(f, locale=locale)
    return {**_count(catalog), "stale": False, "missing": 0}


def get_translation_stats(*, include_english: bool = False) -> TranslationStats:
    """Stats for every locale, keyed ``{locale: {po_file: PoFileStats}}``.

    Discontinued ``.po`` files are omitted entirely.

    Note: this functions tries to detect the staleness of a ``.po`` file
    using a couple of heuristics since to compute the exact staleness requires
    comparing it with a ``.pot`` file that is costly to generate.

    We mark a ``.po`` file as ``stale`` when its ``POT-Creation-Date`` predates
    the most recent evidence that the English source changed, which is the
    later of:

    * the newest ``POT-Creation-Date`` for the same ``.po`` file in any locale,
      and
    * the last commit touching the English source of that ``.po`` file.

    So ``stale`` means *may* be out of date, not *is*: a commit touching a section
    may not have changed a single translatable string, so this over-reports by
    design. ``missing`` counts strings present in the most complete version of
    this ``.po`` file in another locale but absent in this one.
    Note that ``missing`` and ``stale`` are different metrics: a ``.po`` file
    can be stale but not missing any strings, and vice versa.

    When ``include_english`` is true, an ``"en"`` locale is prepended in which
    every ``.po`` file is 100% translated by definition (for use as a
    reference row in a chart). It is off by default.
    """
    entries = []
    for po_path in get_po_files():
        po_file = po_path.stem
        if english_source(po_file) is None:
            continue
        locale = po_path.parent.parent.name
        with open(po_path, "r", encoding="utf-8") as f:
            catalog = pofile.read_po(f, locale=locale)
        entries.append(
            (locale, po_file, _count(catalog), _as_aware(catalog.creation_date))
        )

    # Reference points, computed across every locale of the same ``.po`` file.
    newest_sync: dict[str, datetime] = {}
    largest_total: dict[str, int] = {}
    for _, po_file, counts, created in entries:
        if created is not None:
            known = newest_sync.get(po_file)
            if known is None or created > known:
                newest_sync[po_file] = created
        largest_total[po_file] = max(largest_total.get(po_file, 0), counts["total"])

    results: TranslationStats = {}
    for locale, po_file, counts, created in entries:
        reference = newest_sync.get(po_file)
        source_date = source_last_modified(po_file)
        if source_date is not None and (reference is None or source_date > reference):
            reference = source_date

        results.setdefault(locale, {})[po_file] = {
            **counts,
            "stale": bool(created and reference and created < reference),
            "missing": largest_total[po_file] - counts["total"],
        }

    if include_english:
        results = {"en": _english_row(results)} | results
    return results


def english_string_counts(stats: TranslationStats) -> dict[str, int]:
    """How many strings each ``.po`` file has in the current English source.

    This is the most complete count seen across all locales, since locales
    might not be up to date. This serves as an estimate of the number of
    strings in an up-to-date ``.pot`` file without having to generate it.
    """
    counts: dict[str, int] = {}
    for locale_stats in stats.values():
        for po_file, po_file_stats in locale_stats.items():
            full_count = po_file_stats["total"] + po_file_stats["missing"]
            counts[po_file] = max(counts.get(po_file, 0), full_count)
    return dict(sorted(counts.items()))


def _english_row(stats: TranslationStats) -> dict[str, PoFileStats]:
    """The fake English locale: every ``.po`` file 100% translated."""
    return {
        po_file: PoFileStats(
            total=count,
            translated=count,
            fuzzy=0,
            untranslated=0,
            percentage=100,
            stale=False,
            missing=0,
        )
        for po_file, count in english_string_counts(stats).items()
    }


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Print translation stats as JSON.")
    parser.add_argument(
        "--english",
        action="store_true",
        help="prepend a synthetic 'en' locale at 100%% (off by default)",
    )
    args = parser.parse_args()
    print(json.dumps(get_translation_stats(include_english=args.english), indent=2))


if __name__ == "__main__":
    main()
