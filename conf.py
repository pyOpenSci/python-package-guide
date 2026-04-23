# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
from datetime import datetime
import subprocess
import os
from typing import TYPE_CHECKING
from _ext import rss

if TYPE_CHECKING:
    from sphinx.application import Sphinx

current_year = datetime.now().year
organization_name = "pyOpenSci"

# env vars
sphinx_env = os.environ.get("SPHINX_ENV", "development")
language_env = os.environ.get("SPHINX_LANG", "en")


# -- Project information -----------------------------------------------------

project = "pyOpenSci Python Package Guide"
copyright = f"{current_year}, {organization_name}"
author = "pyOpenSci Community"

# Language of the current build
# language can later be overridden (eg with the -D flag)
# but we need it set here so it can make it into the html_context
language = language_env
# all languages that have .po files generated for them
# (excluding english)
languages = ["es", "ja"]
# the languages that will be included in a production build
# (also excluding english)
release_languages = ["ja"]

# languages that will be included in the language dropdown
# (ie. all that are being built in this nox build session)
if sphinx_env == "production":
    build_languages = ["en"] + release_languages
else:
    build_languages = ["en"] + languages

# Use only the Git SHA for the Sphinx "release" string.
# (Sphinx doesn't require PEP 440 here, but we keep it well-formed and stable.)
try:
    release_value = (
        subprocess.check_output(["git", "rev-parse", "--short=12", "HEAD"])
        .decode("utf-8")
        .strip()
    )
    # Basic check: short SHA should be hex.
    if not release_value or any(c not in "0123456789abcdef" for c in release_value.lower()):
        raise ValueError(f"Unexpected git sha: {release_value!r}")
except (subprocess.CalledProcessError, FileNotFoundError, ValueError):
    # Fallback when building from a source archive or without git available
    release_value = "unknown"

release = release_value

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_nb",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx_sitemap",
    "sphinxext.opengraph",
    "sphinx_favicon",
    "sphinxcontrib.bibtex",
    "_ext.translation_graph",
]

# colon fence for card support in md
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "attrs_block",
]
myst_heading_anchors = 3
myst_footnote_transition = False

# Sphinx_favicon is used now in favor of built in support
# https://pypi.org/project/sphinx-favicon/
favicons = [
    {"href": "https://www.pyopensci.org/images/favicon.ico"},
]

html_baseurl = "https://www.pyopensci.org/python-package-guide/"
lang_selector_baseurl = "/python-package-guide/"
if not sphinx_env == "production":
    # for links in language selector when developing locally
    lang_selector_baseurl = "/"

html_theme_options = {
    "announcement": "<p><a href='https://www.pyopensci.org/about-peer-review/index.html'>We run peer review of scientific Python software. Learn more.</a></p>",
    # "navbar_center": ["nav"], this can be a way to override the default navigation structure
    "external_links": [
        {
            "url": "https://www.pyopensci.org",
            "name": "pyOpenSci Website",
        },
        {
            "url": "https://www.pyopensci.org/software-peer-review",
            "name": "Peer Review Guide",
        },
        {
            "url": "https://pyopensci.org/handbook",
            "name": "Handbook",
        },
    ],
    "icon_links": [
        {
            "name": "Mastodon",
            "url": "https://fosstodon.org/@pyOpenSci",
            "icon": "fa-brands fa-mastodon",
        },
    ],
    "logo": {
        # "text": "Python Packaging",
        "image_dark": "logo-dark-mode.png",
        "image_light": "logo-light-mode.png",
        "alt_text": "pyOpenSci Python Package Guide. The pyOpenSci logo is a purple flower with pyOpenSci under it. The o in open sci is the center of the flower",
    },
    "header_links_before_dropdown": 5,
    "use_edit_page_button": True,
    "show_nav_level": 2,
    "navigation_depth": 3,
    "show_toc_level": 1,
    # "navbar_align": "left",  # [left, content, right] For testing that the navbar items align properly
    "github_url": "https://github.com/pyopensci/python-package-guide",
    "footer_start": ["code_of_conduct", "copyright"],
    "footer_end": [],
    "navbar_persistent": ["language-selector", "search-button"]
}

html_context = {
    "github_user": "pyopensci",
    "github_repo": "python-package-guide",
    "github_version": "main",
    "language": language,
    "languages": build_languages,
    "baseurl": lang_selector_baseurl,
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    ".github",
    ".nox",
    "README.md",
    "styles/write-good/README.md",
    "styles/*",
    ".pytest_cache/README.md",
    "vale-styles/*",
    "CODE_OF_CONDUCT.md",
    "CLAUDE.md",
    # Local virtualenv under the doc root; otherwise Sphinx/Myst scans site-packages.
    ".venv",
    "venv",
    "env",
    "LICENSE.rst",
    "SECURITY.md"
]

# For sitemap generation

sitemap_url_scheme = "{link}"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_css_files = ["pyos.css"]
html_title = "Python Packaging Guide"
html_js_files = ["matomo.js", "language_select.js"]


# Social cards
ogp_site_url = "https://www.pyopensci.org/python-package-guide/"
ogp_social_cards = {
    "line_color": "#6D597A",
    "image": "_static/pyopensci-logo-package-guide.png",
}

# Bibliographies
bibtex_bibfiles = ["bibliography.bib"]
# myst complains about bibtex footnotes because of render order
suppress_warnings = ["myst.footnote"]

# -- Options for linkcheck -------------------------------------------------

# config reference: https://www.sphinx-doc.org/en/master/usage/configuration.html
linkcheck_anchors_ignore_for_url = [
    # GitHub code links with line-number anchors are reported as "not found"
    r"https:\/\/.*github\.com.*\/blob\/.*",
]

linkcheck_ignore = [
    # gnu.org is so strictly rate-limited that retries to it really slow down link-checking... just assume they're fine
    r"https:\/\/.*gnu\.org.*",
    # this discord link is correct, but unauthenticated it redirects to a sign-up page
    r"https:\/\/discord\.gg/NQtTTqtv",
]

def _post_build(app: "Sphinx", exception: Exception | None) -> None:
    rss.generate_tutorials_feed(app)


def setup(app: "Sphinx"):
    app.connect("build-finished", _post_build)

    # Parallel safety: https://www.sphinx-doc.org/en/master/extdev/index.html#extension-metadata
    return {"parallel_read_safe": True, "parallel_write_safe": True}
