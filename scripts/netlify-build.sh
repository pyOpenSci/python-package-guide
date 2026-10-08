#!/usr/bin/env bash
# Build the Sphinx Python package guide on Netlify (deploy previews).
set -euo pipefail

# hatch-vcs reads the package version from git tags. Netlify's checkout
# often has no tags. The docs do not display this version.
export SETUPTOOLS_SCM_PRETEND_VERSION="${SETUPTOOLS_SCM_PRETEND_VERSION:-0.0.0}"

python -m pip install --upgrade pip
python -m pip install nox
python -m nox -s docs
