# Run your tests

Running your tests is important to ensure that your package
is working as expected. However, it's also important to think about your code running, not only on your computer, but also on the computers of your users who may be running various Python versions and using various operating systems. Thus, you will want to consider the following when running your tests:

1. Run your test suite in a series of environments that represent the Python versions and operating systems your users are likely to have.
2. Running your tests in an isolated environment ensures that they do not pass randomly due to your computer's specific setup. For instance, you might have locally installed dependencies that are not declared in your package's dependency list. This oversight could lead to issues when others try to install or run your package on their computers.

On this page, you will learn about the tools that you can use to both run tests in isolated environments and across
Python versions.

### Tools to run your tests

There are three types of tools that will make is easier to setup and run your tests in various environments:

1. A **test framework**, is a package that provides a particular syntax and set of tools for _both writing and running your tests_. Some test frameworks also have plugins that add additional features such as evaluating how much of your code the tests cover. Below you will learn about the **pytest** framework which is one of the most commonly used Python testing frameworks in the scientific ecosystem. Testing frameworks are essential but they only serve to run your tests. They won't allow you to run tests across Python versions without additional automation tools (see automation tools below).
2. **Automation tools** allow you to automate running workflows such as tests in specific ways using user-defined commands. For instance it's useful to be able to run tests across different Python versions with a single command. Tools such as [**nox**](https://nox.thea.codes/en/stable/index.html) and [**tox**](https://tox.wiki/en/latest/index.html) also allow you to run tests across Python versions. However, it will be difficult to test your build on different operating systems using only nox and tox - this is where continuous integration (CI) comes into play.
3. **Continuous Integration (CI):** is the last tool that you'll need to run your tests. CI will not only allow you to replicate any automated builds you create using nox or tox to run your package in different Python environments. It will also allow you to run your tests on different operating systems (Windows, Mac and Linux). [We discuss using CI to run tests here](tests-ci).

:::{figure-md}
![Figure showing three boxes - the first hasTest Frameworks in it, the second Test Runner and the third Continuous Integration....](../images/test-tools.png)

There are three types of tools that will help you develop and run your tests. Test frameworks like pytest
provide syntax and a **framework** for you to write and
run tests. Test runners automate processes such as creating isolated environments to run your tests in, and running tests across Python versions with a single command. Finally Continuous integrate (CI) is a generic platform where you can run your tests across operating systems. CI allows you to run your tests on every PR and commit to ensure iterative checks as contributors suggest changes to your code.

:::

## What testing framework / package should I use to run tests?

We recommend using `Pytest` to build and run your package tests. Pytest is the most common testing tool used in the Python ecosystem.

[The Pytest package](https://docs.pytest.org/en/latest/) also has a number of
extensions that can be used to add functionality such as:

- [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) allows you to analyze the code coverage of your package during your tests, and generates a report that you can [upload to codecov](https://codecov.io/).

[Learn more about code coverage here.](code-cov)

```{note}
TODO: add note about running tests in vscode, breakpoints and –no-cov flag. Then link to tutorial that explains how to deal with this.
```

## Run tests using pytest

If you are using **pytest**, you can run your tests locally by
calling:

`pytest`

Or if you want to run a specific test file - let's call such file - filename.py - you can run:

`pytest filename.py`

Learn more from the [get started docs here](https://docs.pytest.org/en/7.1.x/getting-started.html).

Running pytest on your computer is going to run your tests in whatever
Python environment you currently have activated. This means that tests will be
run on a single version of Python and only on the operating system that you
are running locally.

This is a great start to making your Python package more robust! However, your users may be using your package on different
versions of Python. Or they also may use other operating systems.

An automation tool can simplify the process of running tests
in various Python environments.

### Tools to automate running your tests

To run tests on various Python versions or in various specific environments with a single command, you can use an automation tool such as nox or tox.
Both nox and tox can create an isolated virtual environment that you define. This allows you to easily run your tests in multiple environments and across Python versions.

We will focus on [Nox](https://nox.thea.codes/) in this guide. nox is a Python-based automation tool that builds upon the features of both Make and Tox. Nox is designed to simplify and streamline testing and development workflows. Everything that you do with nox can be implemented using a Python-based interface.

```{admonition} Other automation tools you'll see in the wild
:class: note

- **[Tox](https://tox.wiki/en/latest/index.html#useful-links)** is an automation tool that supports common steps such as building documentation, running tests across various versions of Python, and more. You can find [a nice overview of tox in the plasmaPy documentation](https://docs.plasmapy.org/en/stable/contributing/testing_guide.html#using-tox).

- **[Hatch](https://github.com/ofek/hatch)** is a modern end-to-end packaging tool that works with the popular build backend called hatchling. Hatch offers a tox-like setup where you can run tests locally using different Python versions. If you are using hatch to support your packaging workflow, you may want to also use its testing capabilities rather than using nox.

* [**make:**](https://www.gnu.org/software/make/manual/make.html) Some developers use Make, which is a build automation tool, for running tests
due to its versatility; it's not tied to a specific language and can be used
to run various build processes. However, Make's unique syntax and approach can
make it more challenging to learn, particularly if you're not already familiar
with it. Make also won't manage environments for you like **nox** will do.
```

## Run tests across Python versions with nox

**Nox** is a great automation tool to learn give it is:

- Python-based making it accessible if you already know Python and
- It will create isolated environments to run workflows.

Nox simplifies creating and managing testing environments. With Nox, you can
set up virtual environments, and run tests across Python versions using the environment manager of your choice with a
single command.

Nox can also be used for other development tasks such as building
documentation, creating your package distribution, and testing across various
environment managers such as conda and pip.

## Test Environments

By default, Nox uses the Python built in `venv` environment manager. A virtual environment (`venv`) is a self-contained Python environment that allows you to isolate and manage dependencies for different Python projects. It helps ensure that project-specific libraries and packages do not interfere with each other, promoting a clean and organized development environment.

An example of using nox to run tests in `venv` environments for Python versions 3.9, 3.10 and 3.11 is below.

```{warning}
Note that for the code below to work, you need to have all 3 versions of Python installed on your computer for `venv` to find.
```

### Nox with venv environments

```{admonition} TODO:
TODO: add some tests above and show what the output would look like in the examples below...
```

Below is an example of setting up nox to run tests using `venv` which is the built in environment manager that comes with base Python.

Note that the example below assumes that you have setup your pyproject.toml to declare test dependencies in a way that pip
can understand. And example of that setup is below.

```toml
[project]
dependencies = [
  "geopandas",
  "xarray",
]

[project.optional-dependencies]
tests = ["pytest", "pytest-cov"]
```

If you have the above setup, then you can use `session.install(".[tests]")` to install your test dependencies.
Notice that below one single nox session allows you to run
your tests on 3 different Python environments (Python 3.9, 3.10, 3.11, and 3.12).

```python
import nox

# For this to run you will need to have python3.9, python3.10 and python3.11 installed on your computer. Otherwise nox will skip running tests for whatever versions are missing

@nox.session(python=["3.9", "3.10", "3.11", "3.12"])
def test(session):

# install
session.install(".[tests]")

# Run tests
session.run("pytest")

```

Above you create a nox session in the form of a function
with a `@nox.session` decorator. Notice that within the decorator you declare the versions of python that you
wish to run.

To run the above you'd use the command where `-s` stands for
session. Your function above is called test there for
the session name is test.

```
nox -s test
```

### Nox with conda / mamba

Below is an example for setting up nox to use mamba (or conda) for your
environment manager.
Note that unlike venv, conda can automatically install
the various versions of Python that you need. You won't need to install all three Python versions if you use conda/mamba, like you do with `venv`.

```{note}
For conda to work with nox, you will need to
install a conda-friendly version of Python. We suggest
the mamba-forge installation.

More on that here...<link to tutorial??>
```

```python
import nox

# The syntax below allows you to use mamba / conda as your environment manager, if you use this approach you don’t have to worry about installing different versions of Python

@nox.session(venv_backend='mamba', python=["3.9", "3.10", "3.11", "3.12"])
def test_mamba(session):
    """Nox function that installs dev requirements and runs
    tests on Python 3.9 through 3.12
    """

    # Install dev requirements
    session.install(".[tests]")
    # Run tests using any parameters that you need
    session.run("pytest")
```

To run the above session you'd use:

```bash
nox -s test_mamba
```

## IGNORE ME - testing doctest (not working now)

```{testcode}
a = 1+2
print(a)
```

```{testoutput}

```

TODO: might be able to use doctest to run examples However so far it's not working as intended and may be extra work.
https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html

---
