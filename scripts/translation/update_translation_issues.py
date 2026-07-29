#!/usr/bin/env python3
"""Create and update the GitHub issues that coordinate translating the guide.

Every language is tracked by one parent issue, which carries an overview and a
status table, plus one sub-issue per ``.po`` file, where contributors claim line
ranges. This script creates those issues bodies using Markdown templates, computes
the counts using :mod:`stats`, and makes changes to GitHub with the ``gh`` CLI.
``list-of-translation-issues.yml`` records which issue tracks what, and this
script keeps it in sync.

**IMPORTANT:** Issues should be created and update using this script. This ensures
that ``list-of-translation-issues.yml`` is kept in sync with the issues on GitHub.

**IMPORTANT:** Issues should not be edited by hand directly in GitHub because every
time an issue is updated, the script will recreate the issue body and overwrite any
manual changes. If you want to change the text of the issue, edit the templates
in ``scripts/translation/`` and run the script to update the issues.

Run it from a checkout of the repository::

    python scripts/translation/update_translation_issues.py create de
    python scripts/translation/update_translation_issues.py update es

You can also run the script via nox:

    # Refresh an existing language's issues with the current stats:
    nox -s update-translation-issues -- update es

    # Set up a brand new language that has no issues yet:
    nox -s update-translation-issues -- create de

The script will perform pre-checks to make sure the stats will be accurate and if
certain conditions are not met, it will prompt you to take some action before you
can continue. For example, if you are not updating from the main branch, it will warn
you and ask for confirmation you meant to do that.

Before any change is made to GitHub, the script will show you a summary of what it
is about to do and ask for confirmation.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import yaml
from babel import Locale

HERE = Path(__file__).resolve().parent
BASE_DIR = HERE.parents[1]

# This makes possible to import stats.py (same folder) and conf.py (repository root).
sys.path.insert(0, str(BASE_DIR))

from stats import PoFileStats, english_source, get_translation_stats  # noqa: E402

import conf  # noqa: E402

REPO = "pyOpenSci/python-package-guide"
REGISTRY_PATH = HERE / "list-of-translation-issues.yml"
PARENT_TEMPLATE_PATH = HERE / "parent-issue-template.md"
CHILD_TEMPLATE_PATH = HERE / "child-issue-template.md"

# Starting colour for a ``lang-XX`` label the script has to create. The existing
# ones are all different, so this is only a placeholder to recolour on GitHub.
NEW_LABEL_COLOR = "9683B9"

# Below this percentage, nothing in a language is finished enough to be used as a
# the example, so fall back to Spanish.
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

REGISTRY_HEADER = """\
# Registry of the GitHub issues that track translation of the Python Package Guide.
#
# Each language has one parent issue plus one sub-issue per active .po file.
# This file is the register for those issue numbers.
#
# It is maintained by scripts/translation/update_translation_issues.py, which rebuilds
# it in full on every run, so only edit here the values themselves. Files
# are listed alphabetically. `example` is the file shown in the parent's
# "See an example" section of the issue body.
"""

LABELS_COMMENT = """\
# Labels applied when a new issue is created, in addition to the `XX_lang` label.
# Changes here only affect future issues, not relabel existing issues.
"""

DEPRECATION_NOTE = "# deprecated: English source removed, close this issue by hand"


# --------------------------------------------------------------------------- #
# Running commands and talking to the user
# --------------------------------------------------------------------------- #


def run(*args: str, check: bool = True) -> str | None:
    """Run a command in the repository, returning its stdout. Used to run ``gh`` and ``git``.

    Returns ``None`` when the command fails and ``check`` is false; otherwise a
    failure stops the script.
    """
    result = subprocess.run(args, cwd=BASE_DIR, capture_output=True, text=True)
    if result.returncode != 0:
        if check:
            fail(f"`{' '.join(args)}` failed:\n{result.stderr.strip()}")
        return None
    return result.stdout.strip()


def gh(*args: str, check: bool = True) -> str | None:
    """Run a ``gh`` command against the guide's repository."""
    return run("gh", *args, "--repo", REPO, check=check)


def fail(message: str) -> None:
    """End with an explanation."""
    sys.stdout.flush()  # so earlier warnings stay above this when output is piped
    print(f"\nError: {message}", file=sys.stderr)
    sys.exit(1)


def warn(message: str) -> None:
    print(f"\nWarning: {message}")


def heading(text: str) -> None:
    print(f"\n{'=' * 78}\n{text}\n{'=' * 78}")


def cancel() -> None:
    """Ends after user chooses to cancel."""
    print("\nStopped. Nothing has been changed on GitHub.")
    sys.exit(0)


def ask(question: str) -> str:
    """Read one answer, treating an interrupt or the end of input as "stop"."""
    try:
        return input(question).strip()
    except (EOFError, KeyboardInterrupt):
        cancel()


def confirm(question: str) -> bool:
    """Ask a yes/no question, defaulting to no."""
    return ask(f"{question} [y/N] ").lower() in ("y", "yes")


# --------------------------------------------------------------------------- #
# Helper functions
# --------------------------------------------------------------------------- #


def by_filename(locale_stats: dict[str, PoFileStats]) -> dict[str, PoFileStats]:
    """Re-key stats by filename.

    :mod:`stats` keys modules by stem (``index``) while the registry, the
    templates and the issue bodies all use the filename (``index.po``).
    """
    return {f"{stem}.po": counts for stem, counts in locale_stats.items()}


def stem_of(filename: str) -> str:
    """Removes the ``.po`` suffix from a filename."""
    return filename.removesuffix(".po")


def display_order(files: dict[str, PoFileStats]) -> list[str]:
    """Sorts with the order to be displayed in issue.

    Most complete files first, then break ties on the untranslated count.
    The idea is to show the files closer to completion first, which are easier
    for beginners to handle.
    """

    def rank(name: str) -> tuple[float, int]:
        return -files[name]["percentage"], files[name]["untranslated"]

    return sorted(files, key=rank)


def choose_example(code: str, files: dict[str, PoFileStats]) -> tuple[str, str]:
    """Select the file to point beginners at, as a ``(locale, filename)`` pair.

    Choose the language's most complete file to show as an example in the issue
    or fall back to a default if they are all starting.
    """
    best = display_order(files)[0]
    if files[best]["percentage"] < EXAMPLE_MIN_PERCENTAGE:
        return EXAMPLE_FALLBACK
    return code, best


# --------------------------------------------------------------------------- #
# Pure helpers: rendering Markdown
# --------------------------------------------------------------------------- #


def po_url(locale: str, filename: str) -> str:
    blob = f"https://github.com/{REPO}/blob/main"
    return f"{blob}/locales/{locale}/LC_MESSAGES/{filename}"


def issue_url(number: int | None) -> str:
    """A link to an issue, or a visible placeholder before it has a number.

    When a new issue is rendered for review or for the sub-issues of a new
    parent issue being created, issue numbers are not available yet.
    """
    return f"https://github.com/{REPO}/issues/{number}" if number else "#TBD"


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
    files: dict[str, PoFileStats], subissues: dict[str, int | None]
) -> str:
    """The parent issue's table: every file, linked to its own sub-issue."""
    rows = [PARENT_TABLE_HEADER]
    for name in display_order(files):
        link = f"[`{name}`]({issue_url(subissues.get(name))})"
        rows.append(_row(link, *_count_cells(files[name])))
    rows.append(_total_row(files))
    return "\n".join(rows)


def render_child_table(counts: PoFileStats) -> str:
    """A sub-issue's table: just the one file it covers."""
    return "\n".join([CHILD_TABLE_HEADER, _row(*_count_cells(counts))])


def stale_footnote(files: dict[str, PoFileStats], code: str) -> str:
    """Return a note that the percentage is overestimated if files are stale.

    A ``.po`` file that is not up to date with the English source is missing
    English strings entirely, so its percentage divides by a denominator that
    is too small, making the percentage look higher than it really is.

    :mod:`stats` estimates if the file is ``stale`` in a greedy way, so it
    over-reports by design. Only the missing-strings case is worth putting
    in front of contributors.
    """
    behind = [name for name in display_order(files) if files[name]["missing"]]
    if not behind:
        return ""
    listed = ", ".join(f"`{name}` (+{files[name]['missing']})" for name in behind)
    return (
        "> **Note:** the following are not up to date with the latest English "
        "text, so they are missing strings and the percentage shown for them is "
        f"higher than the real one: {listed}. A maintainer can refresh them with "
        f"`nox -s update-language -- {code}`."
    )


def with_footnote(table: str, files: dict[str, PoFileStats], code: str) -> str:
    """A stats table followed by its staleness note, when there is one."""
    footnote = stale_footnote(files, code)
    return f"{table}\n\n{footnote}" if footnote else table


def is_finished_model(
    example: tuple[str, str], code: str, files: dict[str, PoFileStats]
) -> bool:
    """Whether the example file is complete enough to be copied as it stands."""
    locale, name = example
    # `files` only covers the current locale, for examples in a different locale
    # we cannot know if it is finished.
    return locale == code and files[name]["percentage"] >= 100


def example_description(finished: bool) -> str:
    """Custom wording for the finished case."""
    if finished:
        return "one of the most complete files"
    return "the file that is furthest along"


def example_section(
    example: tuple[str, str], code: str, files: dict[str, PoFileStats]
) -> str:
    """The parent issue's "See an example" paragraph."""
    locale, name = example
    finished = is_finished_model(example, code, files)
    described = example_description(finished)
    sentences = ["Want to see what a translated file looks like?"]
    if locale != code:
        language = Locale.parse(locale).get_display_name("en")
        sentences.append(f"Here is an example from the {language} translation.")
    sentences.append(f"Look at [`{name}`]({po_url(locale, name)}).")
    if finished:
        sentences.append(
            f"It is {described}, so it is a good model for what a finished "
            "translation looks like."
        )
    else:
        sentences.append(
            f"It is {described}. It is not done yet, so you will still find "
            "untranslated and fuzzy strings in it."
        )
    return " ".join(sentences)


def example_bullet(
    example: tuple[str, str],
    code: str,
    files: dict[str, PoFileStats],
    filename: str,
) -> str:
    """Bullet for the sub-issue's Resources, pointing at the example file."""
    locale, name = example
    if (locale, name) == (code, filename):
        return ""
    link = f"[`{name}`]({po_url(locale, name)})"
    described = example_description(is_finished_model(example, code, files))
    return f"- {link} — {described}; a useful reference for style and formatting"


def priority_note(
    files: dict[str, PoFileStats],
    language: str,
    filename: str,
    subissues: dict[str, int | None],
) -> str:
    """A note in the sub-issue's about ``index.po`` being the file worth doing first.

    Our current policy to release a language to the site once its landing page is
    translated (``index.po``) so we point people there. If index is done or if this is
    already in the right sub-issue, we don't include.
    """
    index = files.get("index.po")
    if index is None or index["percentage"] >= 100:
        return ""
    if filename == "index.po":
        return (
            "> **This is the file to do first.** It holds the guide's landing "
            f"page, and translating it is what lets us publish the {language} "
            "guide on the site."
        )
    link = f"[`index.po`]({issue_url(subissues.get('index.po'))})"
    return (
        f"> **Not sure where to start?** {link} holds the guide's landing page "
        f"and is at {index['percentage']:.1f}%. Translating it is what lets us "
        f"publish the {language} guide on the site, so it is the most useful "
        "file to pick if you have not started yet."
    )


def parent_title(language: str) -> str:
    """The parent issue's title, used when the issue is created.

    Updating an issue leaves its title alone, so this is also what
    :func:`precheck_update` compares against to spot a title that has drifted.

    Change it here if you want future parent issues to have a different title, you
    will need to edit existing issues by hand.
    """
    return f"Help translate the Python Package Guide into {language}"


def child_title(filename: str, language: str) -> str:
    """A sub-issue's title, used when the issue is created.

    Like the parent's, only written at creation and compared on later runs.

    Change it here if you want future sub-issues to have a different title, you
    will need to edit existing issues by hand.
    """
    return f"Translate `{filename}` into {language}"


def fill_template(template: str, values: dict[str, str]) -> str:
    """Substitute ``{{PLACEHOLDER}}`` values and drop the templates' comments.

    The templates document their wording variants in HTML comments, which must
    not reach the issue body. Removing one leaves a run of blank lines behind,
    as does an omitted example bullet, so blank lines are collapsed afterwards.
    """
    for name, value in values.items():
        template = template.replace(f"{{{{{name}}}}}", value)
    template = re.sub(r"<!--.*?-->\n?", "", template, flags=re.DOTALL)
    return re.sub(r"\n{3,}", "\n\n", template)


# --------------------------------------------------------------------------- #
# Planning the issues
# --------------------------------------------------------------------------- #


@dataclass
class PlannedIssue:
    """One issue this run intends to create or edit."""

    filename: str | None  # None for the parent issue
    title: str
    body: str

    @property
    def is_parent(self) -> bool:
        return self.filename is None


def plan_issues(
    code: str,
    language: str,
    files: dict[str, PoFileStats],
    example: tuple[str, str],
    subissues: dict[str, int | None],
    parent: int | None,
) -> list[PlannedIssue]:
    """Every issue for a language, rendered in full, parent first.

    Issue numbers may still be unknown, in which case the cross-links render as
    a placeholder; call this again once they are known.
    """
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    parent_issue = PlannedIssue(
        filename=None,
        title=parent_title(language),
        body=fill_template(
            PARENT_TEMPLATE_PATH.read_text(encoding="utf-8"),
            {
                "LANGUAGE": language,
                "LOCALE": code,
                "EXAMPLE_SECTION": example_section(example, code, files),
                "STATS_DATE": today,
                "STATS_TABLE": with_footnote(
                    render_parent_table(files, subissues), files, code
                ),
            },
        ),
    )

    child_template = CHILD_TEMPLATE_PATH.read_text(encoding="utf-8")
    children = []
    for name in display_order(files):
        number = subissues.get(name)
        children.append(
            PlannedIssue(
                filename=name,
                title=child_title(name, language),
                body=fill_template(
                    child_template,
                    {
                        "LANGUAGE": language,
                        "LOCALE": code,
                        "FILENAME": name,
                        "FILE_URL": po_url(code, name),
                        "MAIN_ISSUE_URL": issue_url(parent),
                        "ISSUE_NUMBER": str(number) if number else "TBD",
                        "PRIORITY_NOTE": priority_note(
                            files, language, name, subissues
                        ),
                        "EXAMPLE_BULLET": example_bullet(example, code, files, name),
                        "STATS_DATE": today,
                        "STATS_TABLE": with_footnote(
                            render_child_table(files[name]), {name: files[name]}, code
                        ),
                    },
                ),
            )
        )
    return [parent_issue, *children]


# --------------------------------------------------------------------------- #
# The registry
# --------------------------------------------------------------------------- #


def load_registry() -> dict:
    """Read the issue registry, checking it says what this script needs."""
    registry = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8"))
    if registry["repo"] != REPO:
        fail(
            f"{REGISTRY_PATH.name} tracks {registry['repo']}, but this script "
            f"is written for {REPO}."
        )
    missing = {"parent", "subissue"} - set(registry.get("labels") or {})
    if missing:
        fail(
            f"{REGISTRY_PATH.name} has no `labels` entry for {sorted(missing)}. "
            "It should list the labels to apply when an issue is created."
        )
    return registry


def render_registry(registry: dict) -> str:
    """Rebuild the whole registry file.

    Rebuilding rather than patching keeps the layout and the explanatory
    comments consistent. Whether a sub-issue is deprecated is derived here, so it
    is updated even for languages this run did not touch.
    """
    lines = [REGISTRY_HEADER, f"repo: {registry['repo']}"]
    lines.append(f'updated: "{registry["updated"]}"')
    lines.append("")
    lines.append(LABELS_COMMENT + "labels:")
    for kind, labels in registry["labels"].items():
        lines.append(f"  {kind}:")
        lines.extend(f"    - {label}" for label in labels)
    lines.append("")
    lines.append("languages:")
    for code, entry in registry["languages"].items():
        lines.append(f"  {code}:")
        lines.append(f"    name: {entry['name']}")
        lines.append(f"    label: {entry['label']}")
        lines.append(f"    parent: {entry['parent']}")
        example = entry["example"]
        if example["locale"] != code:
            fallback = Locale.parse(example["locale"]).get_display_name("en")
            lines.append("    # No file in this language is complete enough to be")
            lines.append(f"    # a model yet, so the example falls back to {fallback}.")
        lines.append("    example:")
        lines.append(f"      locale: {example['locale']}")
        lines.append(f"      file: {example['file']}")
        lines.append("    subissues:")
        for name in sorted(entry["subissues"]):
            note = "" if english_source(stem_of(name)) else f"  {DEPRECATION_NOTE}"
            lines.append(f"      {name}: {entry['subissues'][name]}{note}")
        lines.append("")
    return "\n".join(lines).rstrip("\n") + "\n"


def save_registry(registry: dict) -> None:
    """Write the registry, stamped with today's date."""
    registry["updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    REGISTRY_PATH.write_text(render_registry(registry), encoding="utf-8")


# --------------------------------------------------------------------------- #
# Prechecks
# --------------------------------------------------------------------------- #


def check_environment() -> None:
    """Fail on the things that would make a run impossible or incorrect."""
    if run("gh", "auth", "status", check=False) is None:
        fail(
            "The `gh` CLI is missing or not authenticated. Install it from "
            "https://cli.github.com/, run `gh auth login`, then try again."
        )
    branch = run("git", "rev-parse", "--abbrev-ref", "HEAD")
    if branch != "main":
        warn(
            f"You are on branch `{branch}`, not `main`. The stats are read from "
            "the `.po` files in your working tree, so they will describe this "
            "branch rather than the published guide."
        )
        if not confirm("Continue anyway?"):
            cancel()
    check_up_to_date()


def check_up_to_date() -> None:
    """Warn when the working tree's ``.po`` files may be out of date.

    The stats come from the files on disk, so a stale checkout quietly produces
    stale issue bodies.
    """
    remotes = run("git", "remote", "-v") or ""
    remote = next(
        (line.split()[0] for line in remotes.splitlines() if f"{REPO}" in line), None
    )
    if remote is None:
        remote = "origin"
        warn(
            "No remote points at pyOpenSci/python-package-guide, so this is "
            f"probably a fork. Comparing against `{remote}` instead. The fork "
            "itself may be behind pyOpenSci, which you should check yourself."
        )
        if not confirm("Continue anyway?"):
            cancel()

    if run("git", "fetch", remote, "main", check=False) is None:
        warn(
            f"Could not fetch from `{remote}`, so we cannot check if this branch is "
            f"behind `{remote}/main`. The stats may be out of date."
        )
        if not confirm("Continue anyway?"):
            cancel()
        return

    behind = run("git", "rev-list", "--count", f"HEAD..{remote}/main", check=False)
    if behind and behind != "0":
        warn(
            f"This branch is {behind} commit(s) behind `{remote}/main`, so the "
            "stats may not reflect the newest `.po` files. Consider updating "
            "before you continue."
        )
        if not confirm("Continue anyway?"):
            cancel()


def precheck_create(code: str, registry: dict, files: dict[str, PoFileStats]) -> dict:
    """Check a language exists in the registry or generate a new entry.

    The entry is only built in memory here. An entry already on the file means either an
    earlier run was interrupted part-way (this one resumes it) or it already exists.
    """
    existing = registry["languages"].get(code)
    if existing:
        if existing["parent"] and set(existing["subissues"]) >= set(files):
            fail(
                f"`{code}` already has a full set of issues in "
                f"{REGISTRY_PATH.name} (parent #{existing['parent']}). Use "
                f"`update {code}` to refresh them."
            )
        warn(
            f"`{code}` is already partly registered, so an earlier run was "
            "interrupted. This run will create only what is missing."
        )
        return existing

    return {
        "name": Locale.parse(code).get_display_name("en"),
        "label": f"lang-{code.upper()}",
        "parent": None,
        "example": {"locale": code, "file": "index.po"},
        "subissues": {},
    }


def precheck_update(code: str, registry: dict) -> tuple[dict, dict[int, str]]:
    """Check a language's registered issues, returning them and their titles.

    The titles are read back because updating does not rewrite them, so they
    are what should still be seen on GitHub afterwards.
    """
    entry = registry["languages"].get(code)
    if entry is None:
        fail(
            f"No issues are registered for `{code}` in {REGISTRY_PATH.name}.\n"
            "  If issues for it do exist on GitHub, then either this branch is "
            "out of date (update it and try again), or they were created by "
            "hand, which is not recommended.\n"
            "  In that case, either close them and recreate them with "
            f"`create {code}`, or add them to the registry by hand -- also not "
            "recommended."
        )

    print(f"Checking the {len(entry['subissues']) + 1} registered issues...")
    broken = []
    titles = {}
    for label, number in [("parent", entry["parent"]), *entry["subissues"].items()]:
        # Note: this gh command uses the jq inside gh to avoid having to parse JSON in Python
        # by returning a tab-separated string of issue state and title or empty if the
        # issue is not found.
        found = gh(
            "issue",
            "view",
            str(number),
            "--json",
            "state,title",
            "--jq",
            '.state + "\\t" + .title',
            check=False,
        )
        # `partition` ensures unpacking always 3 values (split could unpack more
        # if the title contains tabs)
        state, _, title = (found or "").partition("\t")
        if state != "OPEN":
            broken.append(f"    #{number} ({label}): {state or 'not found'}")
            continue
        titles[number] = title
        expected = (
            parent_title(entry["name"])
            if label == "parent"
            else child_title(label, entry["name"])
        )
        if title != expected:
            warn(
                f"#{number} is titled {title!r}, not {expected!r}. Updating "
                "leaves titles unchanged, so fix it on GitHub if that was not "
                "deliberate."
            )
    if broken:
        fail(
            f"{REGISTRY_PATH.name} is out of sync with GitHub. These issues are "
            "not open:\n" + "\n".join(broken) + "\n"
            "  Fix that before running this again. If your branch is simply out "
            "of date, update it. Otherwise ask a translation maintainer -- the "
            "`translations` label on the issue tracker will show you who is "
            "active."
        )
    return entry, titles


def report_obsolete(entry: dict, files: dict[str, PoFileStats]) -> None:
    """Warn about registered sub-issues whose ``.po`` file no longer counts.

    Nothing is closed: closing an issue is always the maintainer's decision.
    """
    for name, number in entry["subissues"].items():
        if name in files:
            continue
        reason = (
            "its English source has been removed from the guide"
            if english_source(stem_of(name)) is None
            else "its `.po` file is no longer in the repository"
        )
        warn(
            f"`{name}` is obsolete: {reason}. Issue #{number} will be marked "
            f"deprecated in {REGISTRY_PATH.name} but left open -- close it by "
            "hand once you are happy to."
        )


# --------------------------------------------------------------------------- #
# Review
# --------------------------------------------------------------------------- #


def review_bodies(
    plan: list[PlannedIssue],
    example: tuple[str, str],
    entry: dict,
    titles: dict[int, str],
    *,
    allow_skip: bool,
) -> list[PlannedIssue] | None:
    """Show every rendered body and collect an approval for each.

    Returns the approved issues, or ``None`` when the maintainer wants a
    different example file -- that rewrites every body, so the review restarts.
    """
    print(f"\nExample file: `{example[1]}` from the `{example[0]}` translation.")
    approved = []
    for issue in plan:
        number = number_of(entry, issue)
        # An existing issue keeps the title it has; only a new one gets ours.
        heading(f"#{number}: {titles[number]}" if number else f"new: {issue.title}")
        print(issue.body)
        skip = "[s]kip this issue, " if allow_skip else ""
        options = f"[a]ccept, {skip}[e]xample (choose a different one), [q]uit"
        while True:
            answer = ask(f"\n{options}: ").lower()[:1]
            if answer == "a":
                approved.append(issue)
                break
            if answer == "s" and allow_skip:
                print(f"Skipping {issue.filename or 'the parent issue'}.")
                break
            if answer == "e":
                return None
            if answer == "q":
                cancel()
    return approved


def prompt_for_example(
    code: str, files: dict[str, PoFileStats], current: tuple[str, str]
) -> tuple[str, str]:
    """Ask which file the "See an example" section should point at."""
    print("\nFiles in this language:")
    for name in display_order(files):
        print(f"  {name:<28} {files[name]['percentage']:.1f}%")
    fallback = "/".join(EXAMPLE_FALLBACK)
    while True:
        answer = ask(
            f"\nFile to use, or `{fallback}` for the Spanish fallback "
            f"(currently `{'/'.join(current)}`): "
        )
        if answer == fallback:
            return EXAMPLE_FALLBACK
        if answer in files:
            return code, answer
        print(f"`{answer}` is not one of the files above.")


# --------------------------------------------------------------------------- #
# Applying
# --------------------------------------------------------------------------- #


def create_issue(title: str, body: str, labels: list[str]) -> int:
    """Create an issue and return its number."""
    with tempfile.NamedTemporaryFile("w", suffix=".md", encoding="utf-8") as body_file:
        body_file.write(body)
        body_file.flush()
        url = gh(
            "issue",
            "create",
            "--title",
            title,
            "--body-file",
            body_file.name,
            "--label",
            ",".join(labels),
        )
    return int(url.rsplit("/", 1)[-1])


def edit_issue(number: int, body: str) -> None:
    """Replace an issue's body, leaving its title and labels alone.

    The body is generated in full, so there is nothing in it worth keeping. A
    title or a label, though, may have been adjusted deliberately, and that is
    the maintainer's call to make rather than this script's to undo.
    """
    with tempfile.NamedTemporaryFile("w", suffix=".md", encoding="utf-8") as body_file:
        body_file.write(body)
        body_file.flush()
        gh("issue", "edit", str(number), "--body-file", body_file.name)


def ensure_label(label: str, language: str) -> None:
    """Create the language's ``lang-XX`` label if the repository lacks it."""
    existing = gh("api", f"repos/{REPO}/labels", "--paginate", "--jq", ".[].name")
    if label in (existing or "").splitlines():
        return
    if not confirm(f"\nLabel `{label}` does not exist yet. Create it?"):
        fail(f"The issues need `{label}`. Create it on GitHub, then run this again.")
    gh(
        "api",
        f"repos/{REPO}/labels",
        "-f",
        f"name={label}",
        "-f",
        f"color={NEW_LABEL_COLOR}",
        "-f",
        f"description={language} Translation",
    )
    print(f"Created `{label}`. Its colour is a placeholder you can change on GitHub.")


def number_of(entry: dict, issue: PlannedIssue) -> int | None:
    if issue.is_parent:
        return entry["parent"]
    return entry["subissues"].get(issue.filename)


def apply_plan(
    approved: list[PlannedIssue],
    code: str,
    language: str,
    files: dict[str, PoFileStats],
    example: tuple[str, str],
    entry: dict,
    registry: dict,
) -> None:
    """Create whatever is missing, then write every approved body.

    Creation cannot be atomic: the parent must exist before the sub-issues can
    link to it, and the sub-issues must exist before the parent's table can link
    to them. Each number is written to the registry the moment it is known, so
    an interrupted run resumes rather than creating duplicates.
    """
    ensure_label(entry["label"], language)
    registry["languages"][code] = entry
    entry["example"] = {"locale": example[0], "file": example[1]}

    for issue in approved:
        if number_of(entry, issue) is not None:
            continue
        labels = registry["labels"]["parent" if issue.is_parent else "subissue"]
        number = create_issue(issue.title, issue.body, [*labels, entry["label"]])
        if issue.is_parent:
            entry["parent"] = number
        else:
            entry["subissues"][issue.filename] = number
        save_registry(registry)
        print(f"Created #{number}: {issue.title}")

    # Every number is known now, so the cross-links can finally be filled in.
    approved_files = {issue.filename for issue in approved}
    final = plan_issues(
        code, language, files, example, entry["subissues"], entry["parent"]
    )
    for issue in final:
        if issue.filename in approved_files:
            number = number_of(entry, issue)
            edit_issue(number, issue.body)
            print(f"Updated #{number}: body for {issue.filename or 'the parent'}")

    save_registry(registry)


# --------------------------------------------------------------------------- #
# Entry point
# --------------------------------------------------------------------------- #


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create or update the GitHub issues tracking a translation."
    )
    modes = parser.add_subparsers(dest="mode", required=True)
    modes.add_parser("create", help="create a new language's issues").add_argument(
        "code", help="locale code, for example `de`"
    )
    modes.add_parser("update", help="refresh a language's issues").add_argument(
        "code", help="locale code, for example `es`"
    )
    args = parser.parse_args()
    code = args.code

    check_environment()
    registry = load_registry()
    if code not in conf.languages:
        fail(
            f"`{code}` is not in the `languages` list in conf.py, so the guide "
            "does not officially support it yet. Add it there first."
        )

    files = by_filename(get_translation_stats().get(code, {}))
    if not files:
        fail(
            f"No `.po` files were found for `{code}` under locales/{code}/"
            f"LC_MESSAGES. Generate them with `nox -s update-language -- {code}` "
            "first."
        )

    if args.mode == "create":
        entry, titles = precheck_create(code, registry, files), {}
    else:
        entry, titles = precheck_update(code, registry)
        report_obsolete(entry, files)
    language = entry["name"]

    print(f"\nPlanning the {language} issues from {len(files)} `.po` files.")
    example = choose_example(code, files)
    recorded = entry["example"]
    if entry["parent"] and (recorded["locale"], recorded["file"]) != example:
        warn(
            f"The best file has changed since the last run: the example was "
            f"`{recorded['locale']}/{recorded['file']}` and is now "
            f"`{example[0]}/{example[1]}`. Choose `e` below to keep the old one."
        )

    while True:
        plan = plan_issues(
            code, language, files, example, entry["subissues"], entry["parent"]
        )
        approved = review_bodies(
            plan, example, entry, titles, allow_skip=args.mode == "update"
        )
        if approved is not None:
            break
        example = prompt_for_example(code, files, example)

    heading("Ready to apply")
    creating = [i for i in approved if number_of(entry, i) is None]
    editing = [i for i in approved if number_of(entry, i) is not None]
    print(f"  {len(creating)} issue(s) to create, {len(editing)} to update.")
    print("  Nothing has changed on GitHub yet.")
    if not confirm("\nApply these changes?"):
        cancel()

    apply_plan(approved, code, language, files, example, entry, registry)

    heading(f"Done: {language}")
    print(f"  Parent issue:  {issue_url(entry['parent'])}")
    print(f"  Created:       {len(creating)} issue(s)")
    print(f"  Updated:       {len(editing)} issue(s)")
    print(f"  Example file:  {example[0]}/{example[1]}")
    print(f"  Registry:      {REGISTRY_PATH.relative_to(BASE_DIR)} updated")


if __name__ == "__main__":
    main()
