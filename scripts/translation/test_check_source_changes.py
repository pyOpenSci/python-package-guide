"""Tests for the pull request warning about changed English text."""

from __future__ import annotations

import check_source_changes as check

# A stand-in for the real repository layout: one page, one section.
SOURCES = {
    "index.md": "index",
    "documentation": "documentation",
    "CONTRIBUTING.md": "CONTRIBUTING",
}


def test_a_page_is_matched_exactly():
    assert check.affected(["index.md"], SOURCES) == {"index": ["index.md"]}


def test_a_section_matches_everything_below_it():
    changed = ["documentation/index.md", "documentation/write/tutorials.md"]
    assert check.affected(changed, SOURCES) == {"documentation": sorted(changed)}


def test_paths_outside_any_translated_source_are_ignored():
    changed = [
        "scripts/translation/stats.py",
        ".github/workflows/build-book.yml",
        "noxfile.py",
        "locales/es/LC_MESSAGES/index.po",
    ]
    assert check.affected(changed, SOURCES) == {}


def test_a_name_that_only_starts_the_same_does_not_match():
    """`documentation-old.md` is not part of the `documentation/` section."""
    assert check.affected(["documentation-old.md"], SOURCES) == {}


def test_several_sources_are_grouped_by_catalog():
    changed = ["index.md", "documentation/a.md", "documentation/b.md"]
    assert check.affected(changed, SOURCES) == {
        "documentation": ["documentation/a.md", "documentation/b.md"],
        "index": ["index.md"],
    }


def test_no_report_when_nothing_relevant_changed():
    assert check.render_report({}, ["es", "pt"]) == ""


def test_report_names_the_files_the_catalogs_and_the_command():
    report = check.render_report(
        {"documentation": ["documentation/a.md"]}, ["es", "pt"]
    )
    assert "`documentation/a.md` | `documentation.po`" in report
    assert "nox -s update-language -- <locale>    # es, pt" in report
    assert "may need refreshing" in report


def test_a_long_report_says_how_much_it_left_out():
    paths = [f"documentation/page{n}.md" for n in range(check.MAX_ROWS + 5)]
    report = check.render_report({"documentation": paths}, ["es"])
    assert "5 more changed file(s) are not listed." in report
    assert report.count("| `documentation/page") == check.MAX_ROWS


def test_catalogs_without_an_english_source_are_not_translated_any_more():
    """`continuous-integration.po` is still on disk; its page is gone."""
    assert check.english_source("continuous-integration") is None
    assert "continuous-integration" not in check.translated_sources().values()


def test_the_real_repository_resolves_to_pages_and_sections():
    """A guard on the layout the workflow depends on."""
    sources = check.translated_sources()
    assert sources["index.md"] == "index"
    assert sources["documentation"] == "documentation"
    assert all("locales" not in path for path in sources)
    assert "es" in check.locale_codes()
