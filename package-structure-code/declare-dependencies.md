# Declaring Development Dependencies - Python Packaging

## How to declare documentation, test, and other dependencies

In the [pyproject.toml overview page](pyproject-toml-python-package-metadata),
we discussed how to set up a **pyproject.toml** file with basic metadata
information. On this page, you will learn about storing and accessing dependency
information within the pyproject.toml file.

It is recommended that you store all dependency information in a pyproject.toml file
(with a few caveats).

This ensures that all of the metadata associated with your package is declared
in a single place, making it simpler for users and contributors to understand
your package infrastructure.

## Direct project dependencies

Your core project dependencies - representing the packages that
a user requires to install your package, can be stored in a
dependencies array located within the `[project]` table of your
pyproject.toml file. This looks something like this:

```toml
[project]
name = "examplePy"
authors = [
    {name = "Some Maintainer", email = "some-email@pyopensci.org"},
]
# more metadata here...
dependencies = [
    "rioxarray",
    "geopandas",
]
```

## Development dependencies

Dependencies for building your documentation, running your tests and building your package's distribution files are often referred to as development dependencies. These are the dependencies that a user needs to run core development elements of your package such as:

* running your test suite
* building your documentation
* linting and other code cleanup tools

These dependencies can be stored in an
`[optional.dependencies]` table within the **pyproject.toml** file.

:::{admonition} What happened to the requirements.txt file for dependencies?
:class: note

The requirements.txt file used to be the default way to store dependencies. However in recent years, the ecosystem has moved to storing all of this information in a single **pyproject.toml** file. You may find that some projects do still maintain a requirements.txt file either for specific local development needs OR to support users who may want to create a pip-based virtual environment.
:::

## How to declare development dependencies

To declare dependencies in your **pyproject.toml** file:

1. Add a [optional.dependencies] table to your **pyproject.toml** file.
2. Create named groups of dependencies using the syntax:

`group-name = ["dep1", "dep2"]`

```{admonition} Installing packages from GitHub / Gitlab
:class: tip

If you have dependencies that need to be installed
directly from github using a `git+https` installation
approach then you may still need to use a requirements.txt or a conda environment file for your dependency installs.

```

Below we've created 3 sets of optional dependencies named: tests, docs and lint:

```toml
[project.optional-dependencies]
tests = [
  "pytest",
  "pytest-cov"
]
docs = ["sphinx", "pydata_sphinx_theme"]
lint = [
  "black",
  "flake8"
]

```

[Learn more: View PyPA's overview of declaring optional dependencies](https://packaging.python.org/en/latest/specifications/declaring-project-metadata/#dependencies-optional-dependencies)

## How to install dependencies from your pyproject.toml

:::{admonition} Using `python -m pip`

In all of the examples in this guide, you will notice we are calling
`pip` using the syntax:

`python -m pip`

Calling pip using `python -m` ensures that the pip that you are using to install your package comes from your current active Python
environment. We strongly suggest that you use this approach whenever
you call `pip` to avoid installation conflicts.
:::

You can install development dependencies using the
groups that you defined above using the syntax:

`python -m pip install .[docs]`

Above you install the dependencies needed for your documentation and also your package using pip. Below you
install just the dependencies needed to run your tests:

`python -m pip install .[tests]`

You can install all dependencies in the `[optional.dependencies]` table using:

`python -m pip install .[docs, tests, lint]`

Each time you call `python -m pip install .[groups-here]`, you are also installing your package locally and also any dependencies
that your package needs / has declared in your pyproject.toml file.

```{admonition} For zsh shell users
:class: tip

Some versions of shell don't support the square bracket syntax. In those cases you will need to add
quotes to your install call like this:

`python -m pip install 'yourPackage.[tests]'`

```

### Combining sets of dependencies

Above we reviewed how to install dependencies from your pyproject toml. In some cases you may want to group sets of dependencies like so:

```toml
[project.optional-dependencies]
tests = ["pytest", "pytest-cov"]
docs = ["sphinx", "pydata_sphinx_theme"]
dev = [
    "packageName[tests, docs]",
    "build",
    "twine"
]
```

The above allows you to install both the tests and docs dependency lists
using the command:

`python -m pip install .[dev]`

```{tip}
When you install dependencies using the above syntax:

`python -m pip install .[tests, docs]`

pip will also install both your package and its core dependencies.
```

## Where does conda fit in ?

The above workflow assumes that you want to publish your package on PyPI. And then you plan to publish to conda-forge (optionally), [by submitting a recipe using greyskull](https://www.pyopensci.org/python-package-guide/package-structure-code/publish-python-package-pypi-conda.html).

If you want to support conda users, you may want to also maintain a conda environment that they can use to install your package. Maintaining a conda environment will also help you test that your package installs as you expect into a conda environment.

## Read the Docs & project dependencies

If you are using readthedocs to build your documentation, then you may need to install your dependencies using a **readthedocs.yaml** file.

Below is an example of installing the **docs** section of your dependency table in the pyproject.toml file within a readthedocs.yaml file.

```yaml
python:
  install:
    - method: pip
      path: .
      extra_requirements:
        - docs # you can add any of the subgroups of dependencies from your pyproject.toml file to this list.
```

```{tip}

[Learn more about creating a readthedocs.yaml file here. ](https://docs.readthedocs.io/en/stable/config-file/index.html)
```

## If you are using a front-end build tool like PDM, Hatch or Poetry

The above should work if you are using a vanilla packaging approach with a tool such as the [PyPA build tool](https://pypa-build.readthedocs.io/en/stable/) and any back-end that works with `build`.

If you are using another front-end build tool such as PDM, Hatch or Poetry to manage dependencies, then your approach to installing dependencies may be different. Each tool has its own, slightly different way of declaring dependencies in the **pyproject.toml** file. You can learn more about [configuring RTD for tools such as Poetry and PDM here.](https://docs.readthedocs.io/en/stable/build-customization.html#install-dependencies-with-poetry)

```{admonition} A note for conda users
:class: tip

If you use a conda environment for developing your tool, keep in mind that when you install your package using `pip install -e .` (or using pip in general), dependencies will be installed from PyPI rather than conda.

Thus, if you are running a conda environment, installing your package in editable mode risks dependency conflicts. This is particularly important if you have a spatial package that required GDAL or has a GDAL supported dependency.

Alternatively, you can install your package using `pip install -e . --no-deps` to only install the package. And install the rest of your dependencies using a conda environment file.
```
