---
:og:description: "The pyOpenSci pure Python package template uses Hatch to manage environments and run tests, docs, and other maintenance steps. Learn how to use Hatch environments to manage your Python package."
:og:title: "Use Hatch environments with your Python package: a beginner-friendly tutorial"
---

(develop-package)=
# Use Hatch environments with your pure Python package

:::{admonition} About this lesson
:class: tip

[In a previous lesson](create-pure-python-package), you learned how to create a Python package using the pyOpenSci copier template. In this lesson, you'll learn how to manage and use the Hatch environments set up by de
**What you need to complete this lesson**

To complete this lesson, you will need a local Python
environment and shell on your computer.
 You will need to have created a package using our pyOpenSci copier template. You should also have [Hatch installed](get-to-know-hatch).

If you are using Windows or are not familiar with Shell, you may want to check out the [Carpentries shell lesson](https://swcarpentry.github.io/shell-novice/). Windows users will likely need to configure a tool such as [GitBash](https://gitforwindows.org/) for any Shell and git-related steps.

:::

Welcome to your shiny new package! This page will help you get started with using Hatch to run tests, build and check your package, and build your documentation.

To begin, have a look at the `pyproject.toml` file in your package directory. This file contains the configuration for your package. This file is written using a .toml format. [You can learn more about toml here.](https://www.pyopensci.org/python-package-guide/package-structure-code/pyproject-toml-python-package-metadata.html) Here's the TL&DR:

* Each `[]` section in the toml file is called a table.
* You can nest tables with double brackets like this`[[]]`
* Tables contain information about a certain thing that you want to configure.

:::{tip}
You can configure Hatch to use UV by default for environment management. UV is a package manager built in Rust. It is fast and will significantly speed up environment creation.

To use UV with Hatch, configure Hatch in the "tools" section of your `pyproject.toml` file.

```toml
[tool.hatch.envs.default]
installer = "uv"
```
:::

## Using Hatch for developing, building, and maintaining your pure Python package

In the pyOpenSci Python package template, we have set up Hatch environments. You will notice at the bottom of the file, a [hatch environment](https://hatch.pypa.io/1.13/environment/) section, that looks like this:

```
########################################
# Hatch Environments
########################################
```

Hatch allows you to configure and run environments and scripts similar to a workflow tool like tox or nox.

:::{tip}
Hatch defaults to using `venv` to manage environments. However, you can configure it to use other environment tools, such as conda or mamba.

[Read the hatch documentation to learn more about environments. ](https://hatch.pypa.io/1.13/tutorials/environment/basic-usage/)
:::


Below is the Hatch environment used to build and test your package.
Anytime you see: `tool.hatch.envs.test`, it tells Hatch:

> "Hey, Hatch, this is the definition for an environment.`test` is the name of the environment that I want you to create."

So `tool.hatch.envs.build` will create an environment called `build`.

Below the environment "declaration," you can see the definition of what should be in that environment.

## A Hatch environment to build your package

Below is a Hatch environment definition that you will find in your [new project's pyproject.toml file](create-python-package). It is set up to [build your package's](build-package) distribution files ([source distribution](python-source-distribution) and [wheel](python-wheel)).

Notice that the environment definition declares two dependencies: `pip` and `twine`, which the environment needs to run successfully. This declaration is similar to declaring dependencies for your package at the top of your `pyproject.toml`. This section tells Hatch to create a new VENV with pip and twine installed.

```toml
[tool.hatch.envs.build]
description = """Test the installation the package."""
dependencies = [
    "pip",
    "twine",
]
detached = true
```

:::{admonition} Hatch will install your package in editable mode by default
Notice the `detached = True` flag at the bottom of the environment. By default, hatch will install your package in editable mode into any environment it creates. `detached=True` tells it not to install your package into the environment.
:::


### Hatch scripts

Hatch supports defining scripts that run in specific Hatch environments.

Above, you have defined a new environment called 'build' that Hatch will create as a virtual environment (venv). Because `detached = True` in that environment, Hatch won't install your package into it.

You can then use that environment to run "scripts". The definition below tells Hatch to run the following scripts in the build environment.

`[tool.hatch.envs.build.scripts]`

You define this `scripts` to run using the following syntax, where:

* `tool.hatch`: Alerts Hatch that this table is for Hatch to use
* `envs.build`: Use the defined build environment.
* `scripts`: Define what scripts to run. In this case, Hatch will run shell scripts.


Below is the `build.scripts` table that defines 3 shell commands to be run:

* `pip check` # verifies your dependencies
* `hatch build --clean` # build your packages distribution files.
* `twine check dist/*` # use twine to check that your package's sdist (source distribution) is ok.

```toml
# This table installs the command hatch run install:check, which will build and check your package.
[tool.hatch.envs.build.scripts]
check = [
    "pip check",
    "hatch build {args:--clean}",
    "twine check dist/*",
]
detached = true
```

:::{tip}
Hatch, by default, will install your package in editable mode into any virtual environment (venv) that it creates. If `detached=True` is set, then it will skip that step.
:::

### Running the build script

You can run the build script and build your package like this:

`hatch run build:check`

This step updates the build environment and then builds and checks the output distributions of your package.

You can enter the build environment in your shell to check it out:

```console
$ hatch shell build
```

If you run `pip list` in the environment, twine will be there:

```console
$ pip list
```

To leave the environment use:

```console
$ deactivate
```

### Hatch, testing, and matrix environments

It's always helpful to run your tests on the Python versions that you expect your users to be using. In this section, you'll explore the test environment setup in the pyOpenSci template package.

Below, you see the Hatch environment test table.

Similar to the above build environment, the environment below defines the dependencies that Hatch needs to install into the test environment (required to run your tests).

```toml
[tool.hatch.envs.test]
description = """Run the test suite."""
dependencies = [
    "pytest",
    "pytest-cov",
    "pytest-raises",
    "pytest-randomly",
    "pytest-xdist",
]
```

### Your test environment has a matrix associated with it

If the environment has a matrix associated with it, that tells Hatch to run the tests across different Python versions. Below, you are running tests on versions 3.10 through 3.13.

:::{tip}
Hatch by default will install Python [using UV](https://docs.astral.sh/uv/guides/install-python/) both when you install Hatch and also when you declare a matrix environment like the one below
:::

```toml
[[tool.hatch.envs.test.matrix]]
python = ["3.10", "3.11", "3.12", "3.13"]
```

In your project, if you run `hatch shell test`, you will see the output below.
This means that because there is a matrix of Python versions to choose from, you need to select the environment with the Python version you want to use.

```console
➜ hatch shell test
Environment `test` defines a matrix, choose one of the following instead:

test.py3.10
test.py3.11
test.py3.12
test.py3.13
```

Pick the Python test environment that you want to use and enter it, like this (this will open Python 3.13):

```console
$ hatch shell test.py3.13
```

To leave the environment use:

```console
$ deactivate
```

### Hatch scripts for tests

In that same tests section, you will see a `tool.hatch.envs.test.scripts` section.
Similar to what you saw above with the build steps, this is where the "script" to run your tests is defined.

Notice that below, the script has a script called `run`. And that script runs pytest with a set of arguments, including generating code coverage.

```toml
[tool.hatch.envs.test.scripts]
run = "pytest {args:--cov=greatproject --cov-report=term-missing}"
```

To run this script in your terminal, use the syntax:

`hatch run test:run`

:::{admonition} Reminder
:class: tip

* `hatch run`: this calls hatch and tells it that it will be running a command
* `test:run` defines the environment you want it to run (`test`) in this case, and the script is defined as `run`
:::

If you have a matrix setup for tests, then it will both install the needed Python version using UV and run your tests in each version of the Python environment. In this case, since there are four Python versions in the environment, your tests will be run four times, once in each Python version listed in the matrix table.

```
@lwasser ➜ /workspaces/pyopensci-scipy25-create-python-package (main) $ hatch run test:run
──────────────────────────────────────────────────────────────────────── test.py3.10 ────────────────────────────────────────────────────────────────────────
==================================================================== test session starts ====================================================================
platform linux -- Python 3.10.16, pytest-8.4.1, pluggy-1.6.0
Using --randomly-seed=1490740387
rootdir: /workspaces/pyopensci-scipy25-create-python-package
configfile: pyproject.toml
testpaths: tests
plugins: xdist-3.8.0, randomly-3.16.0, raises-0.11, cov-6.2.1
collected 2 items

tests/system/test_import.py .                                                                                                                         [ 50%]
tests/unit/test_example.py .                                                                                                                          [100%

****************** SOME OUTPUT IS INTENTIONALLY DELETED ********************
====================================================================== tests coverage =======================================================================
_____________________________________________________ coverage: platform linux, python 3.11.12-final-0 ______________________________________________________

Name                           Stmts   Miss Branch BrPart    Cover   Missing
----------------------------------------------------------------------------
src/greatproject/__init__.py       0      0      0      0  100.00%
src/greatproject/example.py        2      0      0      0  100.00%
----------------------------------------------------------------------------
TOTAL                              2      0      0      0  100.00%
===================================================================== 2 passed in 0.05s =====================================================================
```

## Build your documentation with Hatch environments

Finally, you can build and serve your documentation using hatch.
To build a static HTML version of the docs run:

`hatch run docs:build`

To run a local server with your docs updated as you update your markdown files, run:

`hatch run docs:serve`

To stop serving the docs use:

mac: <kbd>ctrl + c</kbd>
windows:
