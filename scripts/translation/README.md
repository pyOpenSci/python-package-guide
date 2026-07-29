# Translation issue scripts

This folder contains the scripts to work with the GitHub issues that coordinate
the translation of the Python Package Guide. Each language has:

- a **parent issue** — overview, setup links, and a table of every `.po` file;
- one **sub-issue per `.po` file** — where contributors claim line ranges.

Note: the sub-issues are ordinary issues linked by text (not GitHub's sub-issue feature),
because translation work is ongoing and per-file completion is never really
"done".

## Files

| File | Description |
| :--- | :--- |
| `update_translation_issues.py` | Creates and updates the issues. Start here. |
| `parent-issue-template.md` | Template for a language's parent issue. |
| `child-issue-template.md` | Template for one file's sub-issue. |
| `stats.py` | Computes the string counts. |
| `list-of-translation-issues.yml` | Registry of the current parent + sub-issue numbers per language. |
| `test_translation_issues.py` | Unit tests for the rendering logic. |

## Creating and updating the issues

You do not need to know the translation workflow to run this. The script walks
you through it, shows you every issue body it wants to write, and changes
nothing on GitHub until you confirm at the end.

```bash
# Refresh an existing language's issues with the current stats:
nox -s update-translation-issues -- update es

# Set up a brand new language that has no issues yet:
nox -s update-translation-issues -- create de
```

Or without nox, from the repository root:

```bash
python scripts/translation/update_translation_issues.py update es
```

You need the [`gh` CLI](https://cli.github.com/) installed and logged in
(`gh auth login`). Run it from an up-to-date `main`: the stats come from the
`.po` files in your working tree, so an old checkout produces old numbers. The
script warns you if it finds either of those to be untrue.

**What each mode does**

`update` re-renders the parent and every registered sub-issue with the current
stats, opens sub-issues for any new `.po` file, and warns you about `.po` files
that have become obsolete. `create` opens the whole set for a language that has
none: the parent first, then one sub-issue per `.po` file, then the parent again
so its table can link to them.

**What survives a hand edit.** Updating rewrites the body and nothing else, so
of the three things you can change on an issue:

| | Set on create | On update |
| :--- | :--- | :--- |
| Body | yes | **overwritten** — edit the templates instead |
| Title | yes | left alone |
| Labels | from the `labels:` block | left alone |

Titles are set once, at creation:

- **parent** — ``Help translate the Python Package Guide into <Language>``
- **sub-issue** — ``Translate `<file>.po` into <Language>``

Because updating leaves them alone, a title that no longer matches the
convention would go unnoticed, so the script checks each one against the
expected form and warns you. It does not change it — retitling is your call.

**Interruptions are safe.** Creating a language cannot be atomic — the parent
must exist before the sub-issues can link to it, and the sub-issues must exist
before the parent's table can link to them. So each issue number is written to
the registry the moment it is known. If a run dies half way, run `create` again
and it picks up where it left off instead of opening duplicates.

**It never closes anything.** When a `.po` file goes obsolete the script tells
you and marks it deprecated in the registry, but closing the issue is always
your decision.

## Issue registry

`list-of-translation-issues.yml` is the registry of which GitHub issue tracks each
language and file. The script rebuilds this file in full on every run, so edit
the script rather than the file. Read it with:

```python
import yaml

registry = yaml.safe_load(open("scripts/translation/list-of-translation-issues.yml"))
registry["languages"]["es"]["parent"]            # 686
registry["languages"]["es"]["subissues"]         # {"index.po": 687, ...}
```

Files are listed alphabetically, the same way for every language, so the
languages are easy to compare. That is **not** the order the issue tables use —
those are sorted by how complete each file is. Neither order is written down as
a list anywhere, so adding or removing a `.po` file needs no code change.

## Placeholders

Both templates use `{{NAME}}` placeholders. HTML comments in each template say
where the example section/bullet wording is decided; those comments are stripped
out before the body reaches GitHub.

**Parent** — `{{LANGUAGE}}` (e.g. `Spanish`), `{{LOCALE}}` (e.g. `es`),
`{{EXAMPLE_SECTION}}`, `{{STATS_DATE}}` (e.g. `2026-07-20`), `{{STATS_TABLE}}`.

**Child** — `{{LANGUAGE}}`, `{{LOCALE}}`, `{{FILENAME}}` (e.g. `index.po`),
`{{FILE_URL}}` (the file on `main`), `{{MAIN_ISSUE_URL}}` (the parent issue),
`{{ISSUE_NUMBER}}` (the sub-issue's own number, for `Part of #N`),
`{{PRIORITY_NOTE}}`, `{{EXAMPLE_BULLET}}`, `{{STATS_DATE}}`, `{{STATS_TABLE}}`.

An issue's own number is not knowable until GitHub assigns it, so a body is
rendered twice: once for you to review, with `#TBD` where a number will go, and
again after creation with the real numbers filled in.

## Labels

The labels applied when an issue is created live in the `labels:` block of
`list-of-translation-issues.yml`, not in the script — change them there. Editing
them does not relabel issues that already exist, and the script never touches the
labels on an issue it is only updating.

On top of those, every issue for a language gets that language's own `lang-XX`
label — `lang-` plus the uppercased locale code. If the repository does not have
it yet, the script offers to create it; the colour it picks is a placeholder you
can change on GitHub afterwards.

## Pointing contributors at `index.po`

A language can be published on the site once its landing page is translated,
which makes `index.po` worth more than its size suggests. The parent issue says
so in a static line, and each sub-issue carries a `{{PRIORITY_NOTE}}` linking
back to `index.po`'s own sub-issue with its current percentage. The note is
worded differently in `index.po`'s own sub-issue, where the reader is already in
the right place, and disappears everywhere once the file reaches 100%.

## Choosing the example file

The "See an example" link should point to the language's **most complete** file,
so newcomers can see what a good translation looks like. If nothing in that
language is complete enough yet, it falls back to the Spanish `index.po`. The
example bullet is omitted in the sub-issue whose own file is the example.

The script picks the file automatically and shows you the choice while you
review the parent body; press `e` to pick a different one and everything
re-renders.

How the example is described follows from one thing: whether it is a file in
this language at 100%. If it is, it reads as a model to copy; anything else,
including a borrowed Spanish example, says it is not done yet, so newcomers do
not take its gaps for the house style. The parent's paragraph and the
sub-issues' bullet share that description and cannot disagree.

## Translation stats

`stats.py` is the single source of truth for translation counts. The site's
translation heatmap (`_ext/translation_graph.py`) imports it, as does
`update_translation_issues.py`, so the numbers in the issues and the numbers on
the site cannot drift apart. A string counts as *translated* only if it has a
non-empty translation and is **not** marked `fuzzy`.

It returns **data, not Markdown** — presentation belongs to each caller. In
Python:

```python
from scripts.translation.stats import get_translation_stats

stats = get_translation_stats()          # {locale: {po_file: PoFileStats}}
stats["es"]["index"]["percentage"]       # 81.0
```

From a shell, the same dataset as JSON:

```bash
python scripts/translation/stats.py
```

`.po` files with no English source left in the repo (currently
`continuous-integration`) are detected automatically and excluded.

Note that `stats.py` keys modules by stem (`index`) while the registry, the
templates and the issue bodies all use the filename (`index.po`).

### Table layout

The issue tables list files **most complete first**, breaking ties on the
untranslated count so the easiest file to pick up comes first. This is
deliberate: the parent issue tells contributors to look at that column when
choosing where to start.

### Stale catalogs

Each file carries `stale` and `missing`. A catalog is `stale` when its
`POT-Creation-Date` predates the newest evidence the English text moved on —
either a sibling locale syncing more recently, or a commit touching the English
source. `missing` counts strings that exist in the most complete version of that
file but are absent here.

Two things to keep in mind when reporting these:

- **`stale` means _may be_ out of date, not _is_.** A commit touching a section
  need not have changed any translatable string, so this over-reports.
- **A stale file's percentage is inflated**, because it is computed against a
  denominator that is missing strings. `es/maintain-automate` divides by 292
  where the current English has 321.

Because `stale` over-reports, the issue bodies only mention the files that are
actually missing strings, in a note under the table. Fix a stale catalog with
`nox -s update-language -- <lang>`.

Staleness detection uses `git log`, so it is degraded in a shallow clone
(`actions/checkout` defaults to `fetch-depth: 1`). Check
`git_history_available()` — when it is `False`, only the cross-locale signal is
available and same-day changes to the English source will be missed.

## Tests

The rendering logic is covered by unit tests that check the output against the
issues currently live on GitHub, so a change in wording or layout fails a test
rather than quietly rewriting eight issues:

```bash
nox -s test-translation-scripts
```

The `gh` calls are deliberately not tested. The review-and-confirm flow is the
safety net for those.
