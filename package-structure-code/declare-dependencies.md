```{eval-rst}
:og:title: Add required and optional dependencies to your Python package
:og:description: A Python package dependency refers to an external package or software that your Python project requires to function properly. Learn how to add different types of dependencies to your Python package.
```



:::{todo}

keep this comment - https://github.com/pyOpenSci/python-package-guide/pull/106#issuecomment-1844278487 in this file for now - jeremiah did a nice inventory of common shells and whether they need quotes or not. It's really comprehensive. But do we want it in the guide?? it's really useful for more advanced users i think.

Following this comment:
https://github.com/pyOpenSci/python-package-guide/pull/106#pullrequestreview-1766663571

Jonny will add a section that talks about:

Why you specify dependencies
How to specify dependencies
When you use different specifiers
:::

# Python Package Dependencies

## What is a package dependency?

A Python package dependency refers to an external package or
software that your Python project:

1. Needs to function properly.
2. Requires if someone wants to develop / work on improving your package locally or
3. Requires if a user wants to add additional functionality (that is not core) to your package

A dependency is not part of your project's codebase. It is a package or software that is called
within the code of your project or during development of your package.


### Understanding optional vs. required dependencies
You can think about dependencies as being either optional or required. If they are required, they will be listed in the `dependencies` key in the `project` table of your `pyproject.toml` file. If they are optional, they will be listed in the `[optional.dependencies]` table of your `pyproject.toml`.

You will learn about both below.

:::{figure-md} python-package-dependency-types

<img src="../images/python-package-dependency-types.png" alt="">

There are two broad groups of Python package dependencies: those that are optional and those that are required. Required packages are those that a user needs to use your package. Optional dependencies are packages a user can chose to install to add functionality to your package.
Within those 2 groups, there are three use cases that you can think about. 1. Core dependencies are **required** for a user to use your package. 2. Development dependencies are optional and only needed if someone wants to work on your package locally. 3. Finally feature dependencies are optional and add additional functionality to your package. Not all packages will have feature dependencies.
:::


### Required (or core) dependencies

Required dependencies are called directly within your package's code. On this page we refer to these dependencies
as **core dependencies** as they are needed in order to run your package. You should place your core or required dependencies in the `dependencies` key of the `[project]` table of your `pyproject.toml` file.

### Optional dependencies

Optional dependencies dependencies can be optionally installed by users
depending upon their needs. There are two broad groups of optional dependencies:

1. **Development dependencies**: These are dependencies that are required to support development of your package. They include tools to run tests such as `pytest`, linters (like `flake8` and `ruff`) and code formatters such as `black` and even automation tools such as `nox` or `tox` that run tasks.

2. **Feature dependencies:** These are dependencies that a user can chose to install to add functionality to your package.

When a Python project is installed, the Python package manager (either `pip`
or `conda`) installs your package's dependencies automatically. This ensures
that when you call a function in a specific dependency, it is available in your
user's environment.

:::{admonition} Dependencies can be added to your pyproject.toml file

In the [pyproject.toml overview page](pyproject-toml-python-package-metadata),
you learned how to set up a **pyproject.toml** file with basic metadata
for your package. On this page, you will learn how to specify different types of
dependencies in your `pyproject.toml`.

:::

## How do you declare dependencies?

We recommend that you declare your dependencies using your `pyproject.toml` file.
This ensures that all of the metadata associated with your package is declared
in a single place, making it simpler for users and contributors to understand
your package infrastructure.

Previously, it was common to use a `requirements.txt` file to declare package dependencies.
However in recent years, the ecosystem has moved to storing this
information in your **pyproject.toml** file. You may notice however that some
projects still maintain a `requirements.txt` file for specific local development
needs.

:::{admonition} Other ways you may see packages storing dependencies
:class: tip

If a project contains extensions written in other languages, you may need a `setup.py` file. Or you may contribute to a package that us using `setup.cfg` for dependency declaration.
[Learn more about this in the setuptools documentation](https://setuptools.pypa.io/en/latest/userguide/dependency_management.html#declaring-required-dependency)
:::


### Add required dependencies to your pyproject.toml file

Your core project dependencies need to be installed by a
package manager such as `pip` or `conda` when a user installs your package. You can add those dependencies to
the
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
necessary to install and use your package in the
`dependencies` key in the `[project]` table. This minimizes the number of
additional packages that your users must install as well
as the number of packages that depend upon your package
must also install.

Remember that fewer dependencies to install reduces the
likelihood of version mismatches in user environments.

:::{admonition} A dependency example

Let's pretend you have a package called `plotMe` that creates beautiful plots of data stored in `numpy` arrays. To create your plots in the `plotMe` package, you use the `seaborn` package to stylize our plots and also `numpy` to process array formatted data.

In the example above, the plotMe package, depends upon two packages:

* seaborn
* numpy

This means that in order for plotMe to work in a user's `environment` when installed, you also need to ensure that they have both of those required `dependencies` installed in their environment too.

Declaring a dependency in your `pyproject.toml` file will ensure that it is listed as a required dependency when your package is published to PyPI and that a package manager (`pip` or `conda`) will automatically install it into a user's environment alongside your package:

`python -m pip install plotMe`
:::

### Optional dependencies

Optional dependencies for building your documentation, running your tests and building your package's distribution files are often referred to as development dependencies. These are the dependencies that a user needs to work on your package locally and perform tasks such as:

* running your test suite
* building your documentation
* linting and other code cleanup tools

These dependencies are considered optional, because they are not required to install and use your package. Feature
dependencies are considered optional and should also be placed in the `[project.optional-dependencies]` table.

Optional dependencies can be stored in an
`[project.optional-dependencies]` table in your **pyproject.toml** file.

It's important to note that within the `[project.optional-dependencies]` table, you can store additional, optional dependencies within named sub-groups. This is a different table than the dependencies array located within the `[project]` table discussed above which contains a single array with a single list of required packages.

## Create optional dependency groups

To declare optional dependencies in your **pyproject.toml** file:

1. Add a `[project.optional-dependencies]` table to your **pyproject.toml** file.
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
project, you will need to point to a specific commit/tag/hash of that repository in
order to upload your project to PyPI
:::

Below we've created three sets of optional development dependencies named: tests, docs and lint. We've also added a set of feature dependencies.

```toml
[project.optional-dependencies]
tests = [
  "pytest",
  "pytest-cov"
]
docs = [
  "sphinx",
  "pydata_sphinx_theme"
]
lint = [
  "black",
  "flake8"
]
feature = [
  "pandas",
]

```


:::{admonition} Additional dependency resources

* [Learn more: View PyPA's overview of declaring optional dependencies](https://packaging.python.org/en/latest/specifications/declaring-project-metadata/#dependencies-optional-dependencies)

* [Dependency specifiers](https://packaging.python.org/en/latest/specifications/dependency-specifiers/)

:::

### Install dependency groups


:::{figure-md} python-package-dependencies

<img src="../images/python-package-dependencies.png" alt="Diagram showing a Venn diagram with three sections representing the dependency groups listed above - docs feature and tests. In the center it says your-package and lists the core dependencies of that package seaborn and numpy. To the right are two arrows. The first shows the command python - m pip install your-package. It them shows how installing your package that way installs only the package and the two core dependencies into a users environment. Below is a second arrow with python -m pip install youPackage[tests]. This leads to an environment with both the package dependencies - your-package, seaborn and numpy and also the tests dependencies including pytest and pytest-cov ">

When a user installs your package locally using `python -m pip install your-package` only your package and it's core dependencies get installed. When they install your package `python -m pip install your-package[tests]` pip will install both your package and its core dependencies plus any of the dependencies listed within the tests array of your `[project.optional-dependencies]` table.
:::

:::{admonition} Using `python -m pip install` vs. `pip install`

In all of the examples in this guide, you will notice we are calling
`pip` using the syntax:

`python -m pip`

Calling pip using `python -m` ensures that the `pip` that you are using to install your package comes from your current active Python
environment. We strongly suggest that you use this approach whenever
you call `pip` to avoid installation conflicts.

To ensure this works as you want it to, activate your package's development
environment prior to installing anything using `pip`.
:::

You can install development dependencies using the
groups that you defined above using the syntax:

`python -m pip install ".[docs]"`

Above you install:
* dependencies needed for your documentation (`docs`),
* required package dependencies in the `dependencies` array and
* your package

using pip. Below you
install your package, required dependencies and optional test dependencies.

`python -m pip install ".[tests]"`

You can install multiple dependency groups in the `[project.optional-dependencies]` table using:

`python -m pip install ".[docs, tests, lint]"`


```{admonition} For zsh shell users
:class: tip

There are different shell applications that you and your package contributors might use.
* zsh is the shell that comes by default on newer Mac OS computers
* Windows users may use a tool such as git bash

Some shells don't support unquoted brackets (`[tests]`) which is why we add
quotes to the command in this guide like this:

`python -m pip install ".[tests]"`

In some cases you may see commands without the quotes in guidebooks or contributing
guides like the example below:

`python -m pip install your-package[tests]`

Calling your-package[tests] without the double quotes will work on some shells *but not all*.

```

### Combining sets of dependencies

Above we reviewed how to install dependencies from your `pyproject.toml`. In some cases you may want to group sets of dependencies like so:

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
Python package published on PyPI (or on GitHub/ GitLab) as a dependency. Once you create this file, declare dependencies, [build your package](python-package-distribution-files-sdist-wheel.md) and [publish your package to PyPI](publish-python-package-pypi-conda.md), people can install both your package and all of it's dependencies with one command.

`python -m pip install your-package`

This works great if your package is pure-python (no other languages used).

Some packages, particularly in the scientific Python ecosystem, require dependencies that are not written in Python. Conda was created to support distribution of tools that have code written in both Python and languages other than Python.
:::

## Support conda users with environment.yml files

The above workflow assumes that you want to publish your package on PyPI. And then you plan to publish to conda-forge (optionally), [by submitting a recipe using grayskull](https://www.pyopensci.org/python-package-guide/package-structure-code/publish-python-package-pypi-conda.html).

If you want to support conda users, you may want to also maintain a conda environment that they can use to install your package. Maintaining a conda environment will also help you test that your package installs as you expect into a conda environment.


```{admonition} A note for conda users
:class: tip

If you use a conda environment for developing your tool, keep in mind that when you install your package using `python -m pip install -e .` (or using pip in general), dependencies will be installed from PyPI rather than conda.

Thus, if you are running a conda environment, installing your package in "editable" mode risks dependency conflicts. This is particularly important if you have a spatial package that requires geospatial system libraries like GDAL or another system-level dependency.

Alternatively, you can install your package using `python -m pip install -e . --no-deps` to only install the package. And install the rest of your dependencies using a conda environment file.
```

## Dependencies in Read the Docs

Now that you have your dependencies specified in your project, you can use them to support other workflows such as publishing to Read the Docs.

[Read the Docs](https://readthedocs.org) is a documentation platform with a continuous integration / continuous deployment service that automatically builds and publishes your documentation.

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


:::{admonition} Read the Docs and Python packages
:class: note

* [Learn more about creating a `readthedocs.yaml` file here. ](https://docs.readthedocs.io/en/stable/config-file/index.html)
* If you want to install dependencies using
Poetry in Read the Docs, [you can learn more here.](https://docs.readthedocs.io/en/stable/build-customization.html#install-dependencies-with-poetry)

:::

:::{todo}
This is hidden. TO
:::
