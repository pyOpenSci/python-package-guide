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


# -- Project information -----------------------------------------------------

project = "python-package-guide"
copyright = "2023, pyOpenSci"
author = "pyOpenSci Community"

# The full version, including alpha/beta/rc tags
release = "0.1"

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
]

# colon fence for card support in md
myst_enable_extensions = [
    "colon_fence",
    "deflist",
]
myst_heading_anchors = 3

# For generating sitemap
html_baseurl = "https://www.pyopensci.org/software-peer-review/"

# Link to our repo for easy PR/ editing
html_theme_options = {
       "favicons": [
      {
         "rel": "icon",
         "sizes": "16x16",
         "href": "https://www.pyopensci.org/images/favicon.ico",
      },
    ],
    "announcement": "<p><a href='https://www.pyopensci.org/about-peer-review/index.html'>We run peer review of scientific Python software. Learn more.</a></p>",
    #"navbar_center": ["nav"], this can be a way to override the default navigation structure
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
            "url": "https://pyopensci.org/governance",
            "name": "Governance",
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
        #"text": "Python Packaging",
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

    "footer_items": ["copyright"],
}

html_context = {
    "github_user": "pyopensci",
    "github_repo": "python-package-guide",
    "github_version": "main",
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
]

# For sitemap
html_baseurl = "https://www.pyopensci.org/package-review-guide/"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_css_files = ["pyos.css"]
html_title = "Python Packaging Guide"
html_js_files = ["matomo.js"]
