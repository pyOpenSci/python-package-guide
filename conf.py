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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
from datetime import datetime
import subprocess
import os

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
release_languages = []

# languages that will be included in the language dropdown
# (ie. all that are being built in this nox build session)
if sphinx_env == "production":
    build_languages = ["en"] + release_languages
else:
    build_languages = ["en"] + languages

# Get the latest Git tag - there might be a prettier way to do this but...
try:
    release_value = (
        subprocess.check_output(["git", "describe", "--tags"])
        .decode("utf-8")
        .strip()
    )
    release_value = release_value[:4]
except subprocess.CalledProcessError:
    release_value = "0.1"  # Default value in case there's no tag

# Update the release value
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
if not sphinx_env == "production":
    # for links in language selector when developing locally
    html_baseurl = "/"

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
    "header_links_before_dropdown": 4,
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
    "baseurl": html_baseurl,
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
