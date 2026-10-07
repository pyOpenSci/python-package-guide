#!/usr/bin/env bash
# Build the Sphinx Python package guide on Netlify (deploy previews).
set -euo pipefail

# Full history so hatch-vcs can resolve the version from git tags.
if [ "$(git rev-parse --is-shallow-repository)" = "true" ]; then
  git fetch --unshallow
fi
git fetch --tags || true

python -m pip install --upgrade pip
python -m pip install nox
nox -s docs
