#!/usr/bin/env python
"""Update the GitHub issues that coordinate translation with fresh stats.

Run by the GitHub Action ``refresh-translation-issues.yml`` whenever a ``.po``
file changes on ``main``. Note: all locale issues are checked whenever any ``.po`` file
changes, not just the ones for the locale that changed in the last commit. This simplifies
the workflow without major cost since issues that do not need updating are skipped, and
ensures that the stats are always up to date and the bodies always remain consistent.

Each language has one parent issue that serves as an index for the translation work. It
contains a table with the stats for each ``.po`` file, which are represented by
sub-issues containing each file's stats where contributors can claim line ranges.

Every time a ``.po`` file changes the stats in these issues need to be updated, so
this script recreates the body each issue should have, compares it against
the current body it has, and returns for update only the ones that need to change.

Usage::

    python refresh_translation_issues.py ISSUES_JSON BODIES_JSON REPORT_MD

``ISSUES_JSON`` maps each locale to the open issues carrying its ``lang-XX``
label, as ``{"es": [{"number": 686, "title": ..., "body": ...}, ...]}``.
``BODIES_JSON`` receives the issues to rewrite, as ``[{"number", "body"}]``.
``REPORT_MD`` receives the comment to post, and is left empty when there is
nothing a maintainer has to do.

If the scripts encounters discrepancies with what it expects, it reports back to
the action, which then notifies maintainers by making a comment on the translation
maintenance issue.

The following situations are reported:

- An issue's hidden HTML marker contradicts its title. The issue is skipped: one of the
  two is wrong, and guessing would overwrite whatever it really holds.
- Two issues claim the same role. The lowest-numbered one is updated and the
  other needs closing or renaming.
- A sub-issue tracks a catalog the guide no longer translates. Left alone.
- A ``.po`` file has no sub-issue. The parent lists it without a link until
  someone opens one.
- Sub-issues exist but no parent matched. The whole locale is skipped, since a
  sub-issue's body links back to its parent.
- An existing locale has ``.po`` files but no open issues (e.g. ``ja``)
- A parent issue exists for the locale, but sub-issues do not (e.g. ``de``)
- A locale has no ``.po`` files the guide still translates, so there is nothing
  to render a body from.

"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import NamedTuple

from babel import Locale
from stats import PoFileStats, TranslationStats, get_translation_stats

HERE = Path(__file__).resolve().parent
PARENT_TEMPLATE_PATH = HERE / "parent-issue-template.md"
CHILD_TEMPLATE_PATH = HERE / "child-issue-template.md"

REPO = "pyOpenSci/python-package-guide"

# The string that identifies the parent issues in the maps below. Sub-issues are
# identified by the name of the `.po` files they track.
PARENT_ROLE = "parent"

# Below this percentage nothing in a language is finished enough to point a
# beginner to, so the example falls back to a default language that has one.
EXAMPLE_MIN_PERCENTAGE = 50.0
EXAMPLE_FALLBACK = ("es", "index.po")

PARENT_TABLE_HEADER = (
    "| File | Status | Translated | Fuzzy | Untranslated |\n"
    "| :--- | -----: | ---------: | ----: | -----------: |"
)
CHILD_TABLE_HEADER = (
    "| Status | Translated | Fuzzy | Untranslated |\n"
    "| -----: | ---------: | ----: | -----------: |"
)

# The only date in the body is the one stamped on its stats heading.
DATE_STAMP = re.compile(r"\d{4}-\d{2}-\d{2}")

PARENT_TITLE = re.compile(r"^Help translate the Python Packaging Guide into ")
CHILD_TITLE = re.compile(r"^Translate `([^`]+\.po)` into ")

# A hidden HTML comment marker we add to the issue bodies to verify later we
# are reading the right issue.
MARKER = re.compile(r"<!-- translation-issue: (\S+) -->")


class Message(NamedTuple):
    """A message we want to post as a comment to the Translation Maintenance issue.

    Use `actionable=True` for messages that maintainers have to take action on. This
    signals to the GitHub action that these messages should be posted to the translation
    maintenance issue and end up in the #translations channel in Slack.
    """

    text: str
    actionable: bool


# --------------------------------------------------------------------------- #
# Rendering Markdown
# --------------------------------------------------------------------------- #


def by_filename(locale_stats: dict[str, PoFileStats]) -> dict[str, PoFileStats]:
    """Re-key stats by filename.

    :mod:`stats` keys catalogs by stem (``index``) while the issue bodies and
    their titles all use the filename (``index.po``).
    """
    return {f"{stem}.po": counts for stem, counts in locale_stats.items()}


def display_order(files: dict[str, PoFileStats]) -> list[str]:
    """Sort the way the tables read: most complete first.

    Ties break on the untranslated count, so the file that is quickest to finish
    comes first. The parent issue tells contributors to choose by that column.
    """

    def rank(name: str) -> tuple[float, int]:
        return -files[name]["percentage"], files[name]["untranslated"]

    return sorted(files, key=rank)


def choose_example(code: str, files: dict[str, PoFileStats]) -> tuple[str, str]:
    """The file to point a beginner to, as a ``(locale, filename)`` pair."""
    best = display_order(files)[0]
    if files[best]["percentage"] < EXAMPLE_MIN_PERCENTAGE:
        return EXAMPLE_FALLBACK
    return code, best


def language_name(code: str) -> str:
    """Use babel to get the language name, e.g.: ``"es"`` to ``"Spanish"``."""
    return Locale.parse(code).get_display_name("en")


def po_url(locale: str, filename: str) -> str:
    return (
        f"https://github.com/{REPO}/blob/main/locales/{locale}/LC_MESSAGES/{filename}"
    )


def issue_url(number: int) -> str:
    return f"https://github.com/{REPO}/issues/{number}"


def _row(*cells: str) -> str:
    return "| " + " | ".join(cells) + " |"


def _count_cells(counts: PoFileStats | dict[str, float]) -> list[str]:
    return [
        f"{counts['percentage']:.1f}%",
        str(counts["translated"]),
        str(counts["fuzzy"]),
        str(counts["untranslated"]),
    ]


def _total_row(files: dict[str, PoFileStats]) -> str:
    total = sum(counts["total"] for counts in files.values())
    summed = {
        key: sum(counts[key] for counts in files.values())
        for key in ("translated", "fuzzy", "untranslated")
    }
    summed["percentage"] = summed["translated"] / total * 100 if total else 0.0
    return _row("**Total**", *(f"**{cell}**" for cell in _count_cells(summed)))


def render_parent_table(
    files: dict[str, PoFileStats], subissues: dict[str, int]
) -> str:
    """The parent issue's table: every po file, linked to its own sub-issue."""
    rows = [PARENT_TABLE_HEADER]
    for name in display_order(files):
        number = subissues.get(name)
        # A po file without an open sub-issue is named but not linked. It will be
        # reported by the GitHub action in the maintenance issue.
        cell = f"[`{name}`]({issue_url(number)})" if number else f"`{name}`"
        rows.append(_row(cell, *_count_cells(files[name])))
    rows.append(_total_row(files))
    return "\n".join(rows)


def render_child_table(counts: PoFileStats) -> str:
    """A sub-issue's table with the stats for the file it covers."""
    return "\n".join([CHILD_TABLE_HEADER, _row(*_count_cells(counts))])


def example_section(example: tuple[str, str], code: str) -> str:
    """The parent issue's "See an example" paragraph.

    We don't put the percentage to avoid it being out of date if the example file
    changes.
    """
    locale, name = example
    link = f"[`{name}`]({po_url(locale, name)})"
    if locale == code:
        return (
            "Want to see what a translated file looks like? Look at "
            f"{link}, the file that is furthest along in this language."
        )
    # If we use another language as example, we say which.
    return (
        "Want to see what a translated file looks like? Here is one from the "
        f"{language_name(locale)} translation: {link}."
    )


def marker(locale: str, role: str) -> str:
    """A hidden marker we add to the issue body to save its locale and role."""
    return f"<!-- translation-issue: {locale}/{role} -->"


def fill_template(template: str, values: dict[str, str]) -> str:
    """Substitute the ``{{PLACEHOLDER}}`` values."""
    for name, value in values.items():
        template = template.replace(f"{{{{{name}}}}}", value)
    return template


# --------------------------------------------------------------------------- #
# Working out which issue is which
# --------------------------------------------------------------------------- #


def role_from_title(title: str) -> str | None:
    """Identify the issue role (parent or the po file for a sub-issue) using the title."""
    if PARENT_TITLE.match(title):
        return PARENT_ROLE
    found = CHILD_TITLE.match(title)
    return found.group(1) if found else None


def role_from_body_marker(body: str) -> str | None:
    """Find the ``<locale>/<role>`` from the body marker if there is one."""
    found = MARKER.search(body)
    return found.group(1) if found else None


def _listed(numbers: list[int]) -> str:
    return ", ".join(f"#{number}" for number in numbers)


def match_issues(
    locale: str, issues: list[dict]
) -> tuple[dict[str, dict], list[Message]]:
    """Sort a locale's issues into ``{role: issue}``, saying what was left out.

    Issues are matched on their title, then confirmed against the hidden marker in
    their body to prevent rewriting at the wrong issue.
    """
    matched: dict[str, dict] = {}
    messages: list[Message] = []
    ignored: list[int] = []
    # If two issues claim the same file, the older one wins (lowest number)
    for issue in sorted(issues, key=lambda issue: issue["number"]):
        number = issue["number"]
        role = role_from_title(issue["title"])
        if role is None:
            ignored.append(number)
            continue
        claimed = role_from_body_marker(issue.get("body") or "")
        if claimed is not None and claimed != f"{locale}/{role}":
            messages.append(
                Message(
                    f"#{number} is titled as the issue for `{locale}/{role}`, but "
                    f"its body is marked `{claimed}`. It was left alone: one of "
                    "the two is wrong, and guessing which would overwrite "
                    "whatever the issue really holds.",
                    actionable=True,
                )
            )
            continue
        if role in matched:
            messages.append(
                Message(
                    f"#{matched[role]['number']} and #{number} both look like the "
                    f"issue for `{locale}/{role}`. The first was updated; close "
                    "or rename the other.",
                    actionable=True,
                )
            )
            continue
        matched[role] = issue
    if ignored:
        messages.append(
            Message(
                f"`{locale}`: {len(ignored)} labelled issue(s) are not translation "
                f"trackers and were ignored: {_listed(ignored)}.",
                actionable=False,
            )
        )
    return matched, messages


# --------------------------------------------------------------------------- #
# Comparing against what is already on GitHub
# --------------------------------------------------------------------------- #


def normalize_body(body: str) -> str:
    """Normalize the body for comparison.

    GitHub hands bodies back with CRLF line endings and without any blank line
    the body ended on. The stats date will always changes, so it should not count
    as a difference.
    """
    return DATE_STAMP.sub("", body.replace("\r\n", "\n").strip())


def is_unchanged(current: str, planned: str) -> bool:
    """Whether an issue already says what we would write."""
    return normalize_body(current) == normalize_body(planned)


# --------------------------------------------------------------------------- #
# Putting it together
# --------------------------------------------------------------------------- #


def render_bodies(
    locale: str,
    files: dict[str, PoFileStats],
    matched: dict[str, dict],
    today: str,
) -> dict[int, str]:
    """Every issue this run would write for one locale, keyed by issue number."""
    language = language_name(locale)
    example = choose_example(locale, files)
    parent = matched[PARENT_ROLE]
    subissues = {
        role: issue["number"] for role, issue in matched.items() if role != PARENT_ROLE
    }

    def finish(body: str, role: str) -> str:
        return f"{body.rstrip()}\n\n{marker(locale, role)}"

    bodies = {
        parent["number"]: finish(
            fill_template(
                PARENT_TEMPLATE_PATH.read_text(encoding="utf-8"),
                {
                    "LANGUAGE": language,
                    "LOCALE": locale,
                    "EXAMPLE_SECTION": example_section(example, locale),
                    "STATS_DATE": today,
                    "STATS_TABLE": render_parent_table(files, subissues),
                },
            ),
            PARENT_ROLE,
        )
    }

    child_template = CHILD_TEMPLATE_PATH.read_text(encoding="utf-8")
    for name, number in subissues.items():
        if name not in files:
            continue  # its English page is gone. This will be reported in the maintenance issue.
        bodies[number] = finish(
            fill_template(
                child_template,
                {
                    "LANGUAGE": language,
                    "FILENAME": name,
                    "FILE_URL": po_url(locale, name),
                    "MAIN_ISSUE_URL": issue_url(parent["number"]),
                    "ISSUE_NUMBER": str(number),
                    "STATS_DATE": today,
                    "STATS_TABLE": render_child_table(files[name]),
                },
            ),
            name,
        )
    return bodies


def _bookkeeping(
    locale: str, files: dict[str, PoFileStats], subissue_roles: set[str]
) -> list[Message]:
    """Alert on changes between the `.po` files on disk and the issues on GitHub."""
    messages = []
    for name in sorted(subissue_roles - set(files)):
        messages.append(
            Message(
                f"`{locale}`: the issue for `{name}` tracks a catalog the guide no "
                "longer translates. Its body was left alone. Close it if that page "
                "is gone for good or migrate the strings into whichever catalog "
                "covers it now.",
                actionable=True,
            )
        )
    for name in sorted(set(files) - subissue_roles):
        messages.append(
            Message(
                f"`{locale}`: `{name}` has no sub-issue, so the parent issue lists "
                "it without a link. Open one titled "
                # Double backticks, because the title itself contains backticks
                # and a backslash inside a code span renders as a backslash.
                f"``Translate `{name}` into {language_name(locale)}`` with the "
                f"`lang-{locale.upper()}` label, then re-run this workflow.",
                actionable=True,
            )
        )
    return messages


def updates(
    found: dict[str, list[dict]],
    stats: TranslationStats | None = None,
    today: str | None = None,
) -> tuple[list[dict], list[Message]]:
    """Updates the issues that need new stats."""
    if stats is None:
        stats = get_translation_stats()
    if today is None:
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    changed: list[dict] = []
    messages: list[Message] = []
    for locale in sorted(found):
        matched, notes = match_issues(locale, found[locale])
        messages.extend(notes)

        files = by_filename(stats.get(locale, {}))
        if not files:
            messages.append(
                Message(
                    f"`{locale}` has no .po file catalogs the guide still translates.",
                    actionable=True,
                )
            )
            continue
        if not matched:
            messages.append(
                Message(
                    f"`{locale}` has no translation issues. This workflow only "
                    "updates issues, please create them manually.",
                    actionable=True,
                )
            )
            continue

        subissue_roles = set(matched) - {PARENT_ROLE}
        if PARENT_ROLE not in matched:
            messages.append(
                Message(
                    f"`{locale}` has {len(subissue_roles)} sub-issue(s) but no "
                    "parent issue, and a sub-issue's body links back to its "
                    "parent. The whole language was skipped. Open the parent, "
                    "titled `Help translate the Python Packaging Guide into "
                    f"{language_name(locale)}` with the `lang-{locale.upper()}` "
                    "label.",
                    actionable=True,
                )
            )
            continue
        if not subissue_roles:
            messages.append(
                Message(
                    f"`{locale}` has a parent issue but no sub-issues, so only the "
                    "parent was refreshed. Open one sub-issue per `.po` file so "
                    "contributors have somewhere to claim line ranges.",
                    actionable=True,
                )
            )
        else:
            messages.extend(_bookkeeping(locale, files, subissue_roles))

        current = {
            issue["number"]: issue.get("body") or "" for issue in matched.values()
        }
        for number, body in render_bodies(locale, files, matched, today).items():
            if not is_unchanged(current[number], body):
                changed.append({"number": number, "body": body})
    return changed, messages


def render_report(messages: list[Message]) -> str:
    """The comment for the translation maintenance issue."""
    needed = [message.text for message in messages if message.actionable]
    if not needed:
        return ""
    listed = "\n".join(f"- {text}" for text in needed)
    return f"""### Some translation issues need a look

The `.po` files changed, so the issues tracking them were rewritten with the
current numbers. These could not be handled automatically:

{listed}

Nothing was closed, retitled or relabelled: this workflow only ever rewrites the
body of an issue.
"""


def main(argv: list[str]) -> int:
    """Render the bodies for the issues described in ``argv[1]``.

    Always succeeds to prevent a red mark on `main` from reporting a bookkeeping
    problem as if the translation that triggered this run were at fault.
    """
    if len(argv) != 4:
        print(
            f"usage: {Path(argv[0]).name} ISSUES_JSON BODIES_JSON REPORT_MD",
            file=sys.stderr,
        )
        return 0
    _, issues_path, bodies_path, report_path = argv
    found = json.loads(Path(issues_path).read_text(encoding="utf-8"))
    changed, messages = updates(found)

    Path(bodies_path).write_text(json.dumps(changed), encoding="utf-8")
    Path(report_path).write_text(render_report(messages), encoding="utf-8")

    for message in messages:
        print(message.text, file=sys.stderr)
    print(f"\n{len(changed)} issue(s) need rewriting.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
