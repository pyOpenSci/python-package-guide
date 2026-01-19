```{eval-rst}
:og:description: Learn how to use Nox to run tests for your Python package
  locally across multiple Python versions and operating systems.
:og:title: Run tests for your Python package with Nox
```

# Run tests with Nox

**Nox** is a Python-based automation tool for running tests across multiple
Python versions and managing isolated test environments. If you prefer
Python-driven configuration over TOML, or need complex automation workflows,
Nox is an excellent choice.

For more information about Nox, see the
[official Nox documentation](https://nox.thea.codes/) or the
[Scientific Python guide to testing](https://scientific-python.org/tools/testing).

## Why Nox?

**Nox** is a great automation tool because it:

* Is Python-based, making it accessible if you already know Python
* Will create isolated environments to run workflows
* Supports complex, custom automation beyond standard testing
* Is flexible and powerful for intricate build and test scenarios

`nox` simplifies creating and managing testing environments. With `nox`, you
can set up virtual environments and run tests across Python versions using the
environment manager of your choice with a single command.

## Set up Nox

To get started with Nox, you create a `noxfile.py` file at the root of your
project directory. You then define commands using Python functions.

:::{note}
Nox installations

When you install and use Nox to run tests across different Python versions,
Nox will create and manage individual `venv` environments for each Python
version that you specify in the Nox function. Nox will manage each environment
on its own.
:::

Nox can also be used for other development tasks such as building
documentation, creating your package distribution, and testing installations
across both PyPI-related environments (e.g., venv, virtualenv) and `conda`
(e.g., `conda-forge`).

## Test environments

By default, `nox` uses Python's built-in `venv` environment manager. A virtual
environment (`venv`) is a self-contained Python environment that allows you to
isolate and manage dependencies for different Python projects. It helps ensure
that project-specific libraries and packages do not interfere with each other,
promoting a clean and organized development environment.

### Nox with venv environments

Below is an example of setting up Nox to run tests using `venv`, which is the
built-in environment manager that comes with base Python.

Note that the example below assumes that you have setup your `pyproject.toml`
to declare test dependencies using `project.optional-dependencies`:

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "pyosPackage"
version = "0.1.0"
dependencies = [
  "geopandas",
  "xarray",
]

[project.optional-dependencies]
tests = ["pytest", "pytest-cov"]
```

With this setup, you can use `session.install(".[tests]")` to install your
test dependencies. Notice that below one single Nox session allows you to run
your tests on 4 different Python environments (Python 3.9, 3.10, 3.11, and
3.12).

:::{note}
For this to run you will need to have python3.9, python3.10, python3.11, and
python3.12 installed on your computer. Otherwise nox will skip running tests
for whatever versions are missing.
:::

```python
# This code would live in a noxfile.py file located at the root of your
# project directory
import nox

@nox.session(python=["3.9", "3.10", "3.11", "3.12"])
def test(session):
    # Install dependencies
    session.install(".[tests]")
    # Run tests
    session.run("pytest")
```

Above you create a Nox session in the form of a function with a
`@nox.session` decorator. Notice that within the decorator you declare the
versions of Python that you wish to run.

To run the above, you'd execute the following command, specifying which
session with `--session` (sometimes shortened to `-s`). Your function above is
called `test`, therefore the session name is `test`:

```bash
nox --session test
```

### Nox with conda / mamba

Below is an example for setting up Nox to use mamba (or conda) for your
environment manager. Unlike venv, conda can automatically install the various
versions of Python that you need. You won't need to install all four Python
versions if you use conda/mamba, like you do with `venv`.

:::{note}
For `conda` to work with `nox`, you will need to ensure that either `conda` or
`mamba` is installed on your computer.
:::

```python
# This code should live in your noxfile.py file
import nox

# The syntax below allows you to use mamba / conda as your environment
# manager. If you use this approach, you don't have to worry about installing
# different versions of Python

@nox.session(venv_backend='mamba', python=["3.9", "3.10", "3.11", "3.12"])
def test_mamba(session):
    """Nox function that installs dev requirements and runs tests on Python
    3.9 through 3.12.
    """
    # Install dev requirements
    session.conda_install(".[tests]")
    # Run tests using any parameters that you need
    session.run("pytest")
```

To run the above session you'd use:

```bash
nox --session test_mamba
```

## Hatch vs Nox

If you're trying to decide between Hatch and Nox, see the
[comparison and recommendations on the main testing page](run-tests.md#nox-vs-hatch-choosing-the-right-tool).

## In summary

* **Choose Hatch** if you're already using Hatch for packaging and want
  everything in one place
* **Choose Nox** if you need maximum flexibility, prefer Python-driven
  configuration, or need complex automation workflows

## Next steps

Now that you understand how to run tests locally with Nox, you can learn about
[running tests automatically with continuous integration](tests-ci) or
[running tests with Hatch](run-tests.md).
