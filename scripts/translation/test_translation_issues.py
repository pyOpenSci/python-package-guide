"""Unit tests for the pure helpers in :mod:`update_translation_issues`.

Only the side-effect-free logic is covered here -- rendering, ordering and
choosing. The ``gh`` calls are not tested: the script shows every rendered body
and asks for a final confirmation before touching GitHub, which is the real
safety net for those.

The expected Markdown below is copied from the live issues it has to reproduce,
so a change in wording or layout shows up as a failing test rather than as a
surprise edit on eight issues.

Run with ``nox -s test-translation-scripts``.
"""

from __future__ import annotations

import yaml

import update_translation_issues as issues


def counts(total: int, translated: int = 0, fuzzy: int = 0, *, missing: int = 0):
    """A :class:`stats.PoFileStats` with the percentage worked out for us."""
    return {
        "total": total,
        "translated": translated,
        "fuzzy": fuzzy,
        "untranslated": total - translated - fuzzy,
        "percentage": translated / total * 100 if total else 0.0,
        "stale": False,
        "missing": missing,
    }


# The Italian files and issue numbers, as issue #717 reported them.
ITALIAN = {
    "index.po": counts(100, 100),
    "CONTRIBUTING.po": counts(126, 34),
    "tutorials.po": counts(1193, 1),
    "TRANSLATING.po": counts(118),
    "tests.po": counts(275),
    "maintain-automate.po": counts(321),
    "documentation.po": counts(578),
    "package-structure-code.po": counts(909),
}
ITALIAN_SUBISSUES = {
    "index.po": 766,
    "CONTRIBUTING.po": 767,
    "tutorials.po": 768,
    "TRANSLATING.po": 769,
    "tests.po": 770,
    "maintain-automate.po": 771,
    "documentation.po": 772,
    "package-structure-code.po": 773,
}

# The Spanish `index.po`, as issue #687 reported it: still unfinished.
SPANISH = {"index.po": counts(100, 81, 11)}


# --------------------------------------------------------------------------- #
# Tables
# --------------------------------------------------------------------------- #


def test_parent_table_matches_issue_717():
    expected = """\
| File | Status | Translated | Fuzzy | Untranslated |
| :--- | -----: | ---------: | ----: | -----------: |
| [`index.po`](https://github.com/pyOpenSci/python-package-guide/issues/766) | 100.0% | 100 | 0 | 0 |
| [`CONTRIBUTING.po`](https://github.com/pyOpenSci/python-package-guide/issues/767) | 27.0% | 34 | 0 | 92 |
| [`tutorials.po`](https://github.com/pyOpenSci/python-package-guide/issues/768) | 0.1% | 1 | 0 | 1192 |
| [`TRANSLATING.po`](https://github.com/pyOpenSci/python-package-guide/issues/769) | 0.0% | 0 | 0 | 118 |
| [`tests.po`](https://github.com/pyOpenSci/python-package-guide/issues/770) | 0.0% | 0 | 0 | 275 |
| [`maintain-automate.po`](https://github.com/pyOpenSci/python-package-guide/issues/771) | 0.0% | 0 | 0 | 321 |
| [`documentation.po`](https://github.com/pyOpenSci/python-package-guide/issues/772) | 0.0% | 0 | 0 | 578 |
| [`package-structure-code.po`](https://github.com/pyOpenSci/python-package-guide/issues/773) | 0.0% | 0 | 0 | 909 |
| **Total** | **3.7%** | **135** | **0** | **3485** |"""
    assert issues.render_parent_table(ITALIAN, ITALIAN_SUBISSUES) == expected


def test_child_table_matches_issue_687():
    expected = """\
| Status | Translated | Fuzzy | Untranslated |
| -----: | ---------: | ----: | -----------: |
| 81.0% | 81 | 11 | 8 |"""
    assert issues.render_child_table(SPANISH["index.po"]) == expected


def test_a_file_without_a_number_yet_is_not_linked():
    """A sub-issue that does not exist yet has nothing to point at."""
    table = issues.render_parent_table({"index.po": counts(10, 5)}, {})
    assert "| [`index.po`](#TBD) | 50.0% | 5 | 0 | 5 |" in table


def test_total_row_rounds_rather_than_truncating():
    """Bulgarian's 126/3620 is 3.4806%, which issue #716 shows as 3.5%."""
    bulgarian = {
        "CONTRIBUTING.po": counts(126, 126),
        "index.po": counts(100),
        "TRANSLATING.po": counts(118),
        "tests.po": counts(275),
        "maintain-automate.po": counts(321),
        "documentation.po": counts(578),
        "package-structure-code.po": counts(909),
        "tutorials.po": counts(1193),
    }
    table = issues.render_parent_table(bulgarian, {})
    assert "| **Total** | **3.5%** | **126** | **0** | **3494** |" in table


# --------------------------------------------------------------------------- #
# Ordering and naming
# --------------------------------------------------------------------------- #


def test_display_order_is_most_complete_first_then_easiest():
    order = issues.display_order(ITALIAN)
    assert order[:3] == ["index.po", "CONTRIBUTING.po", "tutorials.po"]
    # The five files at 0.0% are ordered by how much work each one is.
    assert order[3:] == [
        "TRANSLATING.po",
        "tests.po",
        "maintain-automate.po",
        "documentation.po",
        "package-structure-code.po",
    ]


def test_stem_and_filename_map_onto_each_other():
    """`stats` keys modules by stem; everything else uses the filename."""
    assert issues.by_filename({"index": SPANISH["index.po"]}) == SPANISH
    assert issues.stem_of("index.po") == "index"
    assert issues.stem_of("maintain-automate.po") == "maintain-automate"


def test_titles_follow_the_convention():
    """Issue #686 and #687's titles, which every run rewrites to match."""
    assert issues.parent_title("Spanish") == (
        "Help translate the Python Package Guide into Spanish"
    )
    assert issues.child_title("index.po", "Spanish") == (
        "Translate `index.po` into Spanish"
    )


# --------------------------------------------------------------------------- #
# Choosing and describing the example file
# --------------------------------------------------------------------------- #


def test_example_is_the_most_complete_file():
    assert issues.choose_example("it", ITALIAN) == ("it", "index.po")


def test_example_falls_back_to_spanish_when_nothing_is_good_enough():
    """Greek's best file was `index.po` at 20%, and issue #715 used Spanish."""
    greek = {"index.po": counts(100, 20), "tests.po": counts(275, 2)}
    assert issues.choose_example("el", greek) == ("es", "index.po")


def test_only_a_complete_file_in_this_language_counts_as_finished():
    """A borrowed example has no counts here, so it is never called finished."""
    assert issues.is_finished_model(("it", "index.po"), "it", ITALIAN)
    assert not issues.is_finished_model(("es", "index.po"), "es", SPANISH)
    assert not issues.is_finished_model(("es", "index.po"), "el", SPANISH)


def test_finished_example_reads_as_a_model_to_copy():
    """Issue #717's wording, for an `index.po` that is done."""
    assert issues.example_section(("it", "index.po"), "it", ITALIAN) == (
        "Want to see what a translated file looks like? Look at "
        "[`index.po`](https://github.com/pyOpenSci/python-package-guide/blob/main"
        "/locales/it/LC_MESSAGES/index.po). It is one of the most complete files, "
        "so it is a good model for what a finished translation looks like."
    )


def test_unfinished_example_says_so():
    """Issue #686's wording, for an `index.po` still at 81%."""
    assert issues.example_section(("es", "index.po"), "es", SPANISH).endswith(
        "It is the file that is furthest along. It is not done yet, so you will "
        "still find untranslated and fuzzy strings in it."
    )


def test_an_unfinished_example_says_so_whatever_it_is_called():
    """Completeness is checked whatever the file is, not just for `index.po`."""
    files = {"CONTRIBUTING.po": counts(126, 80)}
    assert issues.example_section(("it", "CONTRIBUTING.po"), "it", files).endswith(
        "It is the file that is furthest along. It is not done yet, so you will "
        "still find untranslated and fuzzy strings in it."
    )


def test_spanish_fallback_names_the_language_it_borrows_from():
    """Issue #715's wording, where Greek had nothing complete of its own."""
    section = issues.example_section(("es", "index.po"), "el", SPANISH)
    assert "Here is an example from the Spanish translation." in section
    assert "/locales/es/LC_MESSAGES/index.po" in section


def test_example_bullet_describes_the_file_the_same_way_the_parent_does():
    complete = issues.example_bullet(("it", "index.po"), "it", ITALIAN, "tests.po")
    assert complete.endswith(
        "— one of the most complete files; a useful reference for style and "
        "formatting"
    )
    unfinished = issues.example_bullet(("es", "index.po"), "es", SPANISH, "tests.po")
    assert unfinished.endswith(
        "— the file that is furthest along; a useful reference for style and "
        "formatting"
    )


def test_example_bullet_is_omitted_in_its_own_sub_issue():
    assert issues.example_bullet(("it", "index.po"), "it", ITALIAN, "index.po") == ""


# --------------------------------------------------------------------------- #
# Pointing contributors at `index.po` first
# --------------------------------------------------------------------------- #

SPANISH_SUBISSUES = {"index.po": 687, "tests.po": 690}


def test_other_sub_issues_point_at_index_po_and_say_why():
    assert issues.priority_note(SPANISH, "Spanish", "tests.po", SPANISH_SUBISSUES) == (
        "> **Not sure where to start?** [`index.po`](https://github.com/pyOpenSci"
        "/python-package-guide/issues/687) holds the guide's landing page and is "
        "at 81.0%. Translating it is what lets us publish the Spanish guide on "
        "the site, so it is the most useful file to pick if you have not started "
        "yet."
    )


def test_index_po_is_told_it_is_the_one_to_do_first():
    """Its own sub-issue has no reason to send the reader anywhere else."""
    note = issues.priority_note(SPANISH, "Spanish", "index.po", SPANISH_SUBISSUES)
    assert note == (
        "> **This is the file to do first.** It holds the guide's landing page, "
        "and translating it is what lets us publish the Spanish guide on the site."
    )


def test_the_note_disappears_once_index_po_is_finished():
    """Italian's `index.po` is done, so the language can already be published."""
    assert issues.priority_note(ITALIAN, "Italian", "tests.po", ITALIAN_SUBISSUES) == ""
    assert issues.priority_note(ITALIAN, "Italian", "index.po", ITALIAN_SUBISSUES) == ""


def test_the_note_survives_a_sub_issue_that_has_no_number_yet():
    """Bodies are rendered once for review before GitHub has assigned numbers."""
    note = issues.priority_note(SPANISH, "Spanish", "tests.po", {"index.po": None})
    assert "[`index.po`](#TBD)" in note


# --------------------------------------------------------------------------- #
# Filling the templates
# --------------------------------------------------------------------------- #


def test_template_comments_never_reach_the_issue_body():
    filled = issues.fill_template(
        "Example: {{THING}}\n\n<!--\n  A note for whoever edits this.\n-->\n\nNext\n",
        {"THING": "a value"},
    )
    assert filled == "Example: a value\n\nNext\n"


def test_an_omitted_bullet_does_not_leave_a_gap():
    filled = issues.fill_template(
        "- last resource\n{{EXAMPLE_BULLET}}\n\n<!--\n  a note\n-->\n\n### Next\n",
        {"EXAMPLE_BULLET": ""},
    )
    assert filled == "- last resource\n\n### Next\n"


# --------------------------------------------------------------------------- #
# The staleness note and the registry
# --------------------------------------------------------------------------- #


def test_footnote_names_only_the_files_that_are_missing_strings():
    files = {
        "index.po": counts(100, 50),
        "TRANSLATING.po": counts(109, missing=9),
        "maintain-automate.po": counts(292, missing=29),
    }
    note = issues.stale_footnote(files, "es")
    assert "`TRANSLATING.po` (+9), `maintain-automate.po` (+29)" in note
    assert "index.po" not in note
    assert "nox -s update-language -- es" in note


def test_no_footnote_when_every_file_is_up_to_date():
    assert issues.stale_footnote(ITALIAN, "it") == ""
    assert issues.with_footnote("TABLE", ITALIAN, "it") == "TABLE"


def test_registry_survives_a_round_trip():
    """Rendering is the only way the registry is written, so it must reparse."""
    original = yaml.safe_load(issues.REGISTRY_PATH.read_text(encoding="utf-8"))
    assert yaml.safe_load(issues.render_registry(original)) == original


def test_registry_lists_files_alphabetically():
    """The same order for every language, derived rather than hardcoded, so a
    new or removed `.po` file needs no change here."""
    registry = {
        "repo": issues.REPO,
        "updated": "2026-07-28",
        "labels": {"parent": ["help wanted"], "subissue": ["good first issue"]},
        "languages": {
            "xx": {
                "name": "Example",
                "label": "lang-XX",
                "parent": 1,
                "example": {"locale": "xx", "file": "index.po"},
                "subissues": {"tests.po": 4, "brand-new.po": 2, "index.po": 3},
            }
        },
    }
    listed = [
        line.strip().split(":")[0]
        for line in issues.render_registry(registry).splitlines()
        if line.strip().split(":")[0].endswith(".po")
    ]
    assert listed == ["brand-new.po", "index.po", "tests.po"]
