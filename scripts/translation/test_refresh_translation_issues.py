"""Tests for the workflow that keeps the translation issues up to date.

The tables and the example paragraph are checked against the issues currently
live on GitHub, so a change to the wording or the layout fails a test here
rather than quietly rewriting forty-odd issues.
"""

from __future__ import annotations

import re

import refresh_translation_issues as refresh


def counts(percentage, translated, fuzzy, untranslated):
    """One file's stats, in the order the tables read them."""
    return {
        "total": translated + fuzzy + untranslated,
        "translated": translated,
        "fuzzy": fuzzy,
        "untranslated": untranslated,
        "percentage": percentage,
        "stale": False,
        "missing": 0,
    }


def issue(number, title, body=""):
    return {"number": number, "title": title, "body": body}


# Spanish as issue #686 reported it, keyed by filename the way the bodies are.
SPANISH = {
    "index.po": counts(81.0, 81, 11, 8),
    "package-structure-code.po": counts(66.1, 601, 161, 147),
    "documentation.po": counts(31.0, 179, 14, 385),
    "tests.po": counts(23.3, 64, 75, 136),
    "tutorials.po": counts(15.0, 179, 0, 1014),
    "TRANSLATING.po": counts(0.0, 0, 0, 109),
    "CONTRIBUTING.po": counts(0.0, 0, 0, 126),
    "maintain-automate.po": counts(0.0, 0, 0, 292),
}

SPANISH_SUBISSUES = {
    "index.po": 687,
    "package-structure-code.po": 688,
    "tests.po": 689,
    "documentation.po": 690,
    "tutorials.po": 691,
    "TRANSLATING.po": 692,
    "maintain-automate.po": 693,
    "CONTRIBUTING.po": 694,
}

# A language where nothing has been started, so no file can be the example.
UNSTARTED = {
    "index.po": counts(0.0, 0, 0, 100),
    "tests.po": counts(0.0, 0, 0, 275),
}

PARENT_TITLE = "Help translate the Python Packaging Guide into Spanish"

# Two files is enough for the end-to-end tests, and keeps the fixtures readable.
# `stats` keys catalogs by stem, so this is the shape `updates` is handed.
TWO_FILES = {
    "es": {"index": counts(81.0, 81, 11, 8), "tests": counts(23.3, 64, 75, 136)}
}


# --------------------------------------------------------------------------- #
# Tables
# --------------------------------------------------------------------------- #


def test_the_parent_table_matches_the_one_on_issue_686():
    assert (
        refresh.render_parent_table(SPANISH, SPANISH_SUBISSUES)
        == """\
| File | Status | Translated | Fuzzy | Untranslated |
| :--- | -----: | ---------: | ----: | -----------: |
| [`index.po`](https://github.com/pyOpenSci/python-package-guide/issues/687) | 81.0% | 81 | 11 | 8 |
| [`package-structure-code.po`](https://github.com/pyOpenSci/python-package-guide/issues/688) | 66.1% | 601 | 161 | 147 |
| [`documentation.po`](https://github.com/pyOpenSci/python-package-guide/issues/690) | 31.0% | 179 | 14 | 385 |
| [`tests.po`](https://github.com/pyOpenSci/python-package-guide/issues/689) | 23.3% | 64 | 75 | 136 |
| [`tutorials.po`](https://github.com/pyOpenSci/python-package-guide/issues/691) | 15.0% | 179 | 0 | 1014 |
| [`TRANSLATING.po`](https://github.com/pyOpenSci/python-package-guide/issues/692) | 0.0% | 0 | 0 | 109 |
| [`CONTRIBUTING.po`](https://github.com/pyOpenSci/python-package-guide/issues/694) | 0.0% | 0 | 0 | 126 |
| [`maintain-automate.po`](https://github.com/pyOpenSci/python-package-guide/issues/693) | 0.0% | 0 | 0 | 292 |
| **Total** | **30.8%** | **1104** | **261** | **2217** |"""
    )


def test_the_child_table_matches_the_one_on_issue_687():
    assert (
        refresh.render_child_table(SPANISH["index.po"])
        == """\
| Status | Translated | Fuzzy | Untranslated |
| -----: | ---------: | ----: | -----------: |
| 81.0% | 81 | 11 | 8 |"""
    )


def test_a_file_without_a_sub_issue_is_listed_but_not_linked():
    """A new English page gets a catalog before anyone opens its issue."""
    files = {"index.po": counts(81.0, 81, 11, 8), "brand-new.po": counts(0.0, 0, 0, 12)}
    table = refresh.render_parent_table(files, {"index.po": 687})
    assert "| `brand-new.po` | 0.0% | 0 | 0 | 12 |" in table
    assert "brand-new.po](" not in table


def test_files_are_ordered_most_complete_first():
    assert refresh.display_order(SPANISH)[:3] == [
        "index.po",
        "package-structure-code.po",
        "documentation.po",
    ]


def test_a_tie_is_broken_by_the_untranslated_count():
    """Of two files at the same percentage, the shorter one comes first."""
    files = {"long.po": counts(0.0, 0, 0, 292), "short.po": counts(0.0, 0, 0, 109)}
    assert refresh.display_order(files) == ["short.po", "long.po"]


def test_the_total_row_rounds_rather_than_truncating():
    """126 of 3620 is 3.48%, which has to read as 3.5% and not 3.4%."""
    files = {"a.po": counts(0.0, 126, 0, 3494)}
    assert "**3.5%**" in refresh._total_row(files)


def test_stats_are_re_keyed_from_stems_to_filenames():
    assert refresh.by_filename({"index": SPANISH["index.po"]}) == {
        "index.po": SPANISH["index.po"]
    }


# --------------------------------------------------------------------------- #
# The example file
# --------------------------------------------------------------------------- #


def test_the_example_is_the_most_complete_file():
    assert refresh.choose_example("es", SPANISH) == ("es", "index.po")


def test_the_example_falls_back_to_spanish_when_nothing_is_ready():
    assert refresh.choose_example("de", UNSTARTED) == ("es", "index.po")


def test_the_example_never_quotes_a_percentage():
    """The number would go stale on any run that did not rewrite this issue."""
    section = refresh.example_section(("es", "index.po"), "es")
    assert "%" not in section
    assert "locales/es/LC_MESSAGES/index.po" in section


def test_a_borrowed_example_names_the_language_it_came_from():
    """Otherwise it reads as a claim about the language being tracked."""
    section = refresh.example_section(("es", "index.po"), "de")
    assert "Spanish" in section


# --------------------------------------------------------------------------- #
# Working out which issue is which
# --------------------------------------------------------------------------- #


def test_a_title_says_which_issue_it_is():
    assert refresh.role_from_title(PARENT_TITLE) == "parent"
    assert refresh.role_from_title("Translate `index.po` into Spanish") == "index.po"


def test_an_unrelated_labelled_issue_is_ignored_quietly():
    """#522 is a bug report that carries `lang-JA` like any Japanese issue."""
    title = "The emphasized text is not rendering correctly in Japanese document"
    assert refresh.role_from_title(title) is None

    matched, messages = refresh.match_issues("ja", [issue(522, title)])
    assert matched == {}
    assert not any(message.actionable for message in messages)


def test_an_issue_with_no_marker_is_accepted():
    """Every issue that existed before this script did carries no marker."""
    matched, messages = refresh.match_issues("es", [issue(686, PARENT_TITLE)])
    assert set(matched) == {"parent"}
    assert messages == []


def test_a_marker_that_contradicts_the_title_is_reported_and_skipped():
    found = [
        issue(
            687, "Translate `index.po` into Spanish", refresh.marker("es", "tests.po")
        )
    ]
    matched, messages = refresh.match_issues("es", found)
    assert matched == {}
    assert [message.actionable for message in messages] == [True]
    assert "#687" in messages[0].text and "es/tests.po" in messages[0].text


def test_a_marker_from_another_locale_is_caught_too():
    found = [
        issue(
            687, "Translate `index.po` into Spanish", refresh.marker("pt", "index.po")
        )
    ]
    matched, messages = refresh.match_issues("es", found)
    assert matched == {}
    assert messages[0].actionable


def test_the_lowest_numbered_duplicate_wins():
    """The older issue is the one contributors have been commenting on."""
    title = "Translate `index.po` into Spanish"
    matched, messages = refresh.match_issues(
        "es", [issue(900, title), issue(687, title)]
    )
    assert matched["index.po"]["number"] == 687
    assert messages[0].actionable
    assert "#687" in messages[0].text and "#900" in messages[0].text


# --------------------------------------------------------------------------- #
# Rendering the body
# --------------------------------------------------------------------------- #


def rendered():
    """The bodies for a Spanish parent and one sub-issue."""
    matched = {
        "parent": issue(686, PARENT_TITLE),
        "index.po": issue(687, "Translate `index.po` into Spanish"),
    }
    return refresh.render_bodies("es", SPANISH, matched, "2026-08-04")


def test_every_rendered_body_ends_with_its_own_marker():
    bodies = rendered()
    assert bodies[686].endswith("<!-- translation-issue: es/parent -->")
    assert bodies[687].endswith("<!-- translation-issue: es/index.po -->")


def test_no_placeholder_survives_into_a_rendered_body():
    for body in rendered().values():
        assert "{{" not in body


def test_a_sub_issue_links_back_to_its_parent_and_to_itself():
    body = rendered()[687]
    assert "https://github.com/pyOpenSci/python-package-guide/issues/686" in body
    assert "Part of #687" in body


def test_the_templates_carry_the_placeholders_the_script_fills():
    """A template edit that renames a placeholder has to fail a test.

    Nothing else reads these files, so a typo would otherwise reach GitHub as a
    literal `{{LANGAUGE [sic]}}` in forty issues.
    Note: the [sic] is required to avoid triggering a codespell failure in CI.
    """
    parent = refresh.PARENT_TEMPLATE_PATH.read_text(encoding="utf-8")
    child = refresh.CHILD_TEMPLATE_PATH.read_text(encoding="utf-8")
    assert set(re.findall(r"{{(\w+)}}", parent)) == {
        "LANGUAGE",
        "LOCALE",
        "EXAMPLE_SECTION",
        "STATS_DATE",
        "STATS_TABLE",
    }
    assert set(re.findall(r"{{(\w+)}}", child)) == {
        "LANGUAGE",
        "FILENAME",
        "FILE_URL",
        "MAIN_ISSUE_URL",
        "ISSUE_NUMBER",
        "STATS_DATE",
        "STATS_TABLE",
    }
    # The marker is appended by the script, so a comment in a template would be
    # the only other thing that could cause a false positive.
    assert "<!--" not in parent and "<!--" not in child


# --------------------------------------------------------------------------- #
# Deciding whether an issue has really changed
# --------------------------------------------------------------------------- #


def test_line_endings_and_a_trailing_blank_line_are_not_a_change():
    """This is the form GitHub hands a body back in."""
    assert refresh.is_unchanged("one\r\ntwo\r\n\r\n", "one\ntwo")


def test_a_body_that_only_changed_its_date_is_unchanged():
    assert refresh.is_unchanged("as of 2026-08-04", "as of 2027-01-15")


def test_new_counts_are_a_change_even_on_the_same_day():
    assert not refresh.is_unchanged(
        "as of 2026-08-04: 81.0%", "as of 2026-08-04: 82.0%"
    )


# --------------------------------------------------------------------------- #
# End to end
# --------------------------------------------------------------------------- #


def test_only_the_issues_that_differ_are_returned():
    """An issue already carrying the right body is not rewritten."""
    matched = {
        "parent": issue(686, PARENT_TITLE),
        "index.po": issue(687, "Translate `index.po` into Spanish"),
        "tests.po": issue(689, "Translate `tests.po` into Spanish"),
    }
    files = refresh.by_filename(TWO_FILES["es"])
    bodies = refresh.render_bodies("es", files, matched, "2026-08-04")
    # Hand back the parent as it would already be, and the rest as stale.
    matched["parent"]["body"] = bodies[686]
    found = {"es": list(matched.values())}

    changed, _ = refresh.updates(found, stats=TWO_FILES, today="2026-08-04")
    assert sorted(entry["number"] for entry in changed) == [687, 689]


def test_a_locale_with_catalogs_but_no_issues_is_reported():
    """Somebody has to open the issues by hand: this workflow only rewrites the
    ones that exist. Japanese is in exactly this state today."""
    changed, messages = refresh.updates({"es": []}, stats=TWO_FILES, today="2026-08-04")
    assert changed == []
    assert [message.actionable for message in messages] == [True]
    assert "no translation issues" in messages[0].text


def test_a_locale_with_no_catalogs_left_is_reported():
    """Every `.po` file the guide still translates is gone from this locale, so
    there is nothing to render a body from."""
    found = {"es": [issue(686, PARENT_TITLE)]}
    changed, messages = refresh.updates(found, stats={}, today="2026-08-04")
    assert changed == []
    assert [message.actionable for message in messages] == [True]
    assert "no .po file catalogs" in messages[0].text


def test_a_locale_without_a_parent_issue_is_skipped_and_reported():
    """A sub-issue's body links back to its parent, so there is nothing to render."""
    found = {"es": [issue(687, "Translate `index.po` into Spanish")]}
    changed, messages = refresh.updates(found, stats=TWO_FILES, today="2026-08-04")
    assert changed == []
    assert [message.actionable for message in messages] == [True]
    assert "no parent issue" in messages[0].text


def test_a_sub_issue_for_a_dropped_page_is_left_alone_and_reported():
    """`continuous-integration.po` is still on disk; its English page is gone."""
    found = {
        "es": [
            issue(686, PARENT_TITLE),
            issue(695, "Translate `continuous-integration.po` into Spanish"),
        ]
    }
    changed, messages = refresh.updates(found, stats=TWO_FILES, today="2026-08-04")
    assert [entry["number"] for entry in changed] == [686]
    actionable = [message.text for message in messages if message.actionable]
    assert any("continuous-integration.po" in text for text in actionable)


def test_a_catalog_with_no_sub_issue_is_reported():
    found = {
        "es": [
            issue(686, PARENT_TITLE),
            issue(687, "Translate `index.po` into Spanish"),
        ]
    }
    _, messages = refresh.updates(found, stats=TWO_FILES, today="2026-08-04")
    actionable = [message.text for message in messages if message.actionable]
    assert len(actionable) == 1
    assert "`tests.po` has no sub-issue" in actionable[0]
    # The report has to say enough to act on without opening the workflow.
    # Double backticks: the title contains backticks, and a backslash inside a
    # code span would render as a backslash rather than escape anything.
    assert "``Translate `tests.po` into Spanish``" in actionable[0]
    assert "lang-ES" in actionable[0]


def test_a_language_that_was_never_set_up_is_reported_once_not_file_by_file():
    """A parent with no sub-issues at all is a language somebody began setting up
    and did not finish. It needs a person, but as a single line: one report per
    missing file would bury everything else. German is in this state today."""
    found = {"es": [issue(686, PARENT_TITLE)]}
    changed, messages = refresh.updates(found, stats=TWO_FILES, today="2026-08-04")
    assert [entry["number"] for entry in changed] == [686]
    actionable = [message.text for message in messages if message.actionable]
    assert len(actionable) == 1
    assert "no sub-issues" in actionable[0]


def test_the_report_is_empty_when_nothing_needs_a_person():
    """An empty file is what tells the workflow not to comment at all."""
    assert refresh.render_report([refresh.Message("just so you know", False)]) == ""


def test_the_report_lists_only_what_needs_a_person():
    messages = [
        refresh.Message("just so you know", False),
        refresh.Message("someone has to open an issue", True),
    ]
    report = refresh.render_report(messages)
    assert "- someone has to open an issue" in report
    assert "just so you know" not in report
