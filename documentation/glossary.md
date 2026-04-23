# Python packaging glossary

```{eval-rst}
:og:description: A glossary of common terms used across this Python package
  guide.
:og:title: Python packaging glossary
```

## Core packaging

```{glossary}
`__init__.py`
  A special Python file that marks a directory as a Python package.
  When Python sees this file, it knows the folder contains importable
  code. It can either be empty or contain code that runs when the package
  is imported.

API token
  A secret key used to authenticate with PyPI or TestPyPI when
  publishing a package. You generate one in your account settings and
  use it in place of a password. **Treat it like a password and never
  share it or commit it to version control**.

Build backend
  The tool that does the actual work of building your package into
  distribution files. In this guide, the build backend is Hatchling.
  You specify it in your `pyproject.toml` file:

  [build-system]
  requires = ["hatchling >= 1.26"]
  build-backend = "hatchling.build"

  You execute a build by running `hatch build`. Alternatively, you can run  `python -m build`.
  [Reference: official Python Packaging documentation](https://packaging.python.org/en/latest/tutorials/packaging-projects/#choosing-a-build-backend)

Distribution files
  The files you upload to PyPI so others can install your package.
  There are two common types: a wheel (`.whl`) and a source
  distribution (`.tar.gz`). See also `Wheel (.whl)` and `Source
  distribution (sdist)`.

Module
  A single Python file (`.py`) containing code such as functions,
  classes, or variables that can be imported. A package is made up of
  one or more modules.

`pyproject.toml`
  The configuration file at the root of your Python package. Written in
  TOML format, it stores metadata such as name, version, authors, and
  license. It can also configure tools such as Hatch, uv, and pytest.
  See also [Make your Python package PyPI ready](../tutorials/pyproject-toml).

Python package
  A directory of Python code structured so it can be installed,
  imported, and shared with others. A package includes at least an
  `__init__.py` file and a `pyproject.toml` file. This is sometimes
  referred to as a **regular package**.

  Info: You may hear the term **namespaced package** which is not really
  a package at all but a container of subpackages. This is out of scope
  for this guide. If interested, consult the [Python documentation](https://docs.python.org/3/glossary.html#term-namespace-package).

PyPI / TestPyPI
  PyPI (the Python Package Index) is the official repository where
  Python packages are published and installed from. TestPyPI is a
  separate practice environment used for learning and testing publishing
  workflows. See [pypi.org](https://pypi.org) and
  [test.pypi.org](https://test.pypi.org).
  See also [Publish your Python package to PyPI](../tutorials/publish-pypi).

Source distribution (sdist)
  One of the two distribution file types for a Python package. The
  sdist (`.tar.gz`) contains source code and project files. When someone
  installs from an sdist, tools build the package locally first.
  See also [Publish your Python package to PyPI](../tutorials/publish-pypi).

TOML
  Tom's Obvious Minimal Language, a simple format for configuration
  files. TOML organizes data into tables such as `[project]` or
  `[tool.hatch]` and arrays. `pyproject.toml` uses TOML.

Trusted publishing
  A secure way to publish to PyPI using GitHub Actions instead of an
  API token. Rather than storing a secret token, you configure PyPI to
  trust your repository directly.
  See also [Setup Trusted Publishing for secure and automated publishing via GitHub Actions](../tutorials/trusted-publishing).

Wheel (.whl) (binary distribution)
  One of the two distribution file types for a Python package. A wheel
  is a pre-built binary format (`.whl`, a ZIP file) that installs directly
  without a build step. For many pure Python packages, one wheel can
  work across platforms.
  See also [Publish your Python package to PyPI](../tutorials/publish-pypi).
```

## Tools

```{glossary}
copier
  A command-line tool for creating new projects from templates. In this
  guide, you can use copier with the pyOpenSci package template to set
  up structure, configuration, and tooling quickly. See
  [copier.readthedocs.io](https://copier.readthedocs.io).

coverage.py
  A tool that measures how much of your code is exercised by tests,
  often as a percentage. It shows which lines and branches are covered.
  See [coverage.readthedocs.io](https://coverage.readthedocs.io).

Hatch
  A modern Python packaging and project management tool. In this guide,
  Hatch is used to build packages, manage environments, run scripts, and
  publish. Configuration lives in `pyproject.toml`. See
  [hatch.pypa.io](https://hatch.pypa.io).
  See also [Get to know Hatch](../tutorials/get-to-know-hatch).

Hatchling
  The build backend used by Hatch. When you run `python -m build` or
  `hatch build`, Hatchling reads `pyproject.toml` and creates sdist
  and wheel files.
  See [hatch.pypa.io/latest/backend](https://hatch.pypa.io/latest/backend/).

pip
  Python's default package installer. You can use it to install packages
  from PyPI into an environment with commands such as
  `pip install package-name`. See [pip.pypa.io](https://pip.pypa.io).

pytest
  A widely used Python testing framework for discovering and runnning tests.
  In this guide, pytest often runs through Hatch scripts. See
  [docs.pytest.org](https://docs.pytest.org).

Ruff
  A fast Python linter and formatter. It checks style and can
  automatically fix many styling issues. See
  [docs.astral.sh/ruff](https://docs.astral.sh/ruff).

Sphinx
  A documentation generator for Python projects. Sphinx reads docstrings
  and documentation files to build a docs site. See
  [sphinx-doc.org](https://www.sphinx-doc.org).

Twine
  A tool for securely uploading distribution files to PyPI or TestPyPI.
  See [twine.readthedocs.io](https://twine.readthedocs.io).

uv
  A fast Python package and environment manager. In this guide, you can
  use uv to manage dependencies and run commands in project environments.
  See [docs.astral.sh/uv](https://docs.astral.sh/uv).
```

## Hatch-specific concepts

```{glossary}
Hatch environment
  An isolated Python environment managed by Hatch. You can define
  multiple environments in `pyproject.toml` for testing, docs, builds,
  and style checks, each with its own dependencies and scripts.

Script (Hatch)
  A named command defined inside a Hatch environment in
  `pyproject.toml`. Scripts provide shortcuts such as
  `hatch run build:check` and `hatch run test:run`.

Task runner
  A tool that automates repetitive development workflows. Hatch can
  function as a task runner by letting you define scripts that run in
  specific environments.
```

## Development concepts

```{glossary}
Code coverage
  A measure of how much source code executes during tests, usually as a
  percentage. High coverage does not guarantee no bugs, but low coverage
  can indicate untested areas.

Dependencies
  Other Python packages needed for your package to work. Common classes
  include required dependencies, optional dependencies, and development
  dependencies.

Docstring
  A string at the top of a function, class, or module that describes
  behavior, inputs, and outputs. Docstrings can be used by tools such as
  Sphinx to generate API documentation.

End-to-end test
  A test that simulates a complete user workflow from start to finish.
  In scientific packages, tutorials executed during docs builds can
  serve as end-to-end tests.

Integration test
  A test that checks how multiple functions or components work together.
  Unlike a unit test, it verifies behavior across a broader workflow.

Linting
  Automatic checks for style issues, formatting problems, and potential
  errors in code.

Unit test
  A test that checks one function or method in isolation. Unit tests are
  fast and help pinpoint where failures occur.

Version specifier / lower bound
  A constraint on which dependency versions are accepted. For example,
  `numpy>=1.24` sets a lower bound so versions older than 1.24 are not
  used.
```

## Git / GitHub

```{glossary}
git
  A tool for version control.

GitHub
  A service providing accounts and organizations to facilitate sharing repositories.

GitHub Codespace
  A cloud-based development environment that runs in a browser. See
  [github.com/features/codespaces](https://github.com/features/codespaces).

Scoped commit
  A git commit that makes one focused change, such as one fix or one
  feature update. Scoped commits improve reviewability and history
  clarity.
```

## Documentation

```{glossary}
Code of conduct
  A document that sets expectations for how contributors and community
  members treat one another in a project.

Contributing guide
  A document, often `CONTRIBUTING.md`, that explains how others can
  contribute, including setup steps, workflow, and code style.

MyST Markdown
  Markedly Structured Text, a Markdown flavor that supports Sphinx
  directives and roles. It allows Markdown-based docs while keeping
  Sphinx features. See
  [myst-parser.readthedocs.io](https://myst-parser.readthedocs.io).

README
  The front page of your package on GitHub and often on PyPI. A good
  README explains purpose, installation, usage, and support options.
```

## AI

```{glossary}
Generative AI / LLM
  Generative AI systems produce content such as text, code, or images.
  LLM stands for Large Language Model, the technology behind tools such
  as ChatGPT, GitHub Copilot, and Claude.
```
