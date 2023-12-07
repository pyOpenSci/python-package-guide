# Python Package Dependencies

:::{admonition} What happened to the requirements.txt file for dependencies?
:class: note

The `requirements.txt` file used to be the default way to store dependencies. However in recent years, the ecosystem has moved to storing all of this information in a single **pyproject.toml** file. Some projects still maintain a `requirements.txt` file either for specific local development needs.
:::


## Declaring different types of dependencies

In the [pyproject.toml overview page](pyproject-toml-python-package-metadata),
we discussed how to set up a **pyproject.toml** file with basic metadata
information. On this page, you will learn about storing and accessing dependency
information within the pyproject.toml file.

It is recommended that you store all dependency information in a **pyproject.toml** file. This ensures that all of the metadata associated with your package is declared
in a single place, making it simpler for users and contributors to understand
your package infrastructure.

:::{admonition} Other ways you may see packages storing dependencies
:class: tip

If a project contains extensions written in other languages, you may need a `setup.py` file. Or you may contribute to a package that us using `setup.cfg` for dependency declaration.
[Learn more about this in the setuptools documentation](https://setuptools.pypa.io/en/latest/userguide/dependency_management.html#declaring-required-dependency)
:::


### Required dependencies

Your core project dependencies represent the packages that
a user needs to install and use your package. Dependencies can be stored in a
`dependencies` array located within the `[project]` table of your
**pyproject.toml** file. This looks something like this:

```toml
[project]
name = "examplePy"
authors = [
    {name = "Some Maintainer", email = "some-email@pyopensci.org"},
]

dependencies = [
    "rioxarray",
    "geopandas",
]
```

Ideally, you should only list the packages that are
necessary to install and use your package in the `[dependencies]` section. This minimized the number of additional packages that both your users and packages that depend upon your package have to install.

Remember that fewer dependencies to install reduces the likelihood of version mismatches in user environments.

### Optional dependencies

Dependencies for building your documentation, running your tests and building your package's distribution files are often referred to as development dependencies. These are the dependencies that a user needs to run core development elements of your package such as:

* running your test suite
* building your documentation
* linting and other code cleanup tools

These dependencies are considered optional, because they are not required to install and use your package.

Optional dependencies can be stored in an
`[optional.dependencies]` table in your **pyproject.toml** file.

It's important to note that within the `optional.dependencies` table, you can store additional, optional dependencies within named sub-groups. This is a different table than the dependencies section discussed above which contains a single array with a single list of required packages.

## Create optional dependency groups

To declare dependencies in your **pyproject.toml** file:

1. Add a `[optional.dependencies]` table to your **pyproject.toml** file.
2. Create named groups of dependencies using the syntax:

`group-name = ["dep1", "dep2"]`

:::{admonition} Installing packages from GitHub / Gitlab
:class: tip

If you have dependencies that need to be installed directly from GitHub using
a `git+https` installation approach, you can do so using the pyproject.toml
file like so:

```toml
dependencies = [
"my_dependency >= 1.0.1 @ git+https://git.server.example.com/mydependency.git"
]
```

IMPORTANT: For security reasons, if your library depends on a GitHub-hosted
project, you will need to point to a specific commit/tag of that repository in
order to upload your project to PyPI
:::

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
:::{admonition} Additional dependency resources

* [Learn more: View PyPA's overview of declaring optional dependencies](https://packaging.python.org/en/latest/specifications/declaring-project-metadata/#dependencies-optional-dependencies)

* [Dependency specifiers](https://packaging.python.org/en/latest/specifications/dependency-specifiers/)

:::

### Install dependency groups

:::{admonition} Using `python -m pip`

In all of the examples in this guide, you will notice we are calling
`pip` using the syntax:

`python -m pip`

Calling pip using `python -m` ensures that the pip that you are using to install your package comes from your current active Python
environment. We strongly suggest that you use this approach whenever
you call `pip` to avoid installation conflicts.

To ensure this works as you want it to, activate your package's development
environment prior to installing anything using `pip`.
:::

You can install development dependencies using the
groups that you defined above using the syntax:

`python -m pip install ".[docs]"`

Above you install:
* dependencies needed for your documentation,
* required package dependencies in the `dependency` array and
* your package

using pip. Below you
install your package, required dependencies and optional test dependencies.

`python -m pip install ".[tests]"`

You can install multiple dependency groups in the `[optional.dependencies]` table using:

`python -m pip install ".[docs, tests, lint]"`


```{admonition} For zsh shell users
:class: tip

Some versions of shell including all of the modern Macs that now use zsh shell, support the square bracket syntax. In those cases you will need to add
quotes to your install call like this:

`python -m pip install ".[tests]"`

In some cases you may see syntax like this:

`python -m pip install yourPackage[tests]`

in documentation. This will work on some versions of shell but not all.

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

`python -m pip install ".[dev]"`

```{tip}
When you install dependencies using the above syntax:

`python -m pip install ".[tests, docs]"`

`pip` will also install your package and its core dependencies.
```


:::{admonition} Where does conda fit in?
:class: note

The `pyproject.toml` file allows you to list any
Python package published on PyPI (or on GitHub/ GitLab) as a dependency. Once create this file, declare dependencies, [build your package](python-package-distribution-files-sdist-wheel.md) and [publish your package to PyPI](publish-python-package-pypi-conda.md), people can install both your package and all of it's dependencies with one command.

`pip install yourPackage`

This works great if your package is pure-python (no other languages used).

Some packages, particularly in the scientific Python ecosystem, require dependencies that are not written in Python. Conda was created to support distribution of tools that have code written in both Python and languages other than Python.
:::

## Support conda users with environment.yml files

The above workflow assumes that you want to publish your package on PyPI. And then you plan to publish to conda-forge (optionally), [by submitting a recipe using grayskull](https://www.pyopensci.org/python-package-guide/package-structure-code/publish-python-package-pypi-conda.html).

If you want to support conda users, you may want to also maintain a conda environment that they can use to install your package. Maintaining a conda environment will also help you test that your package installs as you expect into a conda environment.


```{admonition} A note for conda users
:class: tip

If you use a conda environment for developing your tool, keep in mind that when you install your package using `pip install -e .` (or using pip in general), dependencies will be installed from PyPI rather than conda.

Thus, if you are running a conda environment, installing your package in editable mode risks dependency conflicts. This is particularly important if you have a spatial package that required GDAL or has a GDAL supported dependency.

Alternatively, you can install your package using `pip install -e . --no-deps` to only install the package. And install the rest of your dependencies using a conda environment file.
```

## Dependencies in Read the Docs

Now that you have your dependencies specified in your project, you can use them to support other workflows such as publishing to Read the Docs.

Read the Docs is a documentation platform with a continuous integration / continuous deployment service that automatically builds and publishes your documentation.

If you are using Read the Docs to build your documentation, then you may need to install your dependencies using a **readthedocs.yaml** file.

Below is an example of installing the **docs** section of your dependency table in the pyproject.toml file within a readthedocs.yaml file.

```yaml
python:
  install:
    - method: pip
      path: .
      extra_requirements:
        - docs # you can add any of the subgroups of dependencies from your pyproject.toml file to this list.
```

:::{tip}
[Learn more about creating a `readthedocs.yaml` file here. ](https://docs.readthedocs.io/en/stable/config-file/index.html)
:::


:::{admonition} Dependencies using other front-end build tool like PDM, Hatch or Poetry
:class: note

If you are using another front-end build tool such as PDM, Hatch or Poetry to manage dependencies, then your approach to installing dependencies in your ReadtheDocs.yml file may be different. You can learn more about [configuring RTD for tools such as Poetry and PDM here.](https://docs.readthedocs.io/en/stable/build-customization.html#install-dependencies-with-poetry)

:::
