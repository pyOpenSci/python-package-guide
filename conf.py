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

project = 'python-package-guide'
copyright = '2022, pyOpenSci'
author = 'Leah Wasser'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_nb",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx.ext.intersphinx"
]

# colon fence for card support in md
myst_enable_extensions = ["colon_fence"]


# Link to our repo for easy PR/ editing
html_theme_options = {
    "repository_url": "https://github.com/pyopensci/python-package-guide",
    "use_repository_button": True,
    "google_analytics_id": "UA-141260825-1",
    "show_toc_level": 1,
    "toc_title": "On this page",
    "external_links": [
      {"pyOpenSci Website": "link-one-name", "url": "https://www.pyopensci.org"}
  ],
  "announcement": "🚧 UNDER CONSTRUCTION: this guide is under heavy construction right now. 🚧"
}



# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "_build", 
    "Thumbs.db", 
    ".DS_Store", 
    ".github", 
    ".nox", 
    "README.md"
    ]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'
html_static_path = ["_static"]
html_css_files = ["pyos.css"]
html_title = "pyOpenSci Package Guide"
html_logo = "images/logo/logo.png"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']