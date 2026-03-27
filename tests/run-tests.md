```{eval-rst}
:og:description: Learn how to run tests for your Python package locally
  across multiple Python versions and operating systems using Hatch or Nox.
:og:title: Run tests for your Python package across environments
```

# Run tests for your Python package

Running your tests across different Python versions and operating systems is
critical to ensuring your package works for your users. Your users may be
running different versions of Python and operating systems than you are.

This page teaches you how to run tests locally in isolated environments and
across multiple Python versions. You'll learn about two main automation tools:
[**Hatch**](https://hatch.pypa.io/) and
[**Nox**](https://nox.thea.codes/en/stable/index.html). In the next lesson,
you will learn about running your tests online in
[continuous integration (CI)](tests-ci).

## Why test across multiple environments?

When you develop a package on your computer, it works in one specific
environment: your Python version, your operating system, and your installed
dependencies. Your users, however, will run your code in many different
environments. By running your tests across multiple Python versions and
operating systems, you catch compatibility issues before users do.

Additionally, running tests in isolated environments ensures that your tests
pass because of your code, not because of unexpected dependencies installed
on your computer. This gives you confidence that your package will work when
others install it.

On this page, you will learn about the tools that you can use to both
run tests in isolated environments and across Python versions.

:::{seealso}
**Related pages:**

* [Write tests](write-tests.md) for best practices on writing test
  suites
* [Test types](test-types.md) to understand unit, integration, and
  end-to-end tests
* [Run tests online with CI](tests-ci.md) for GitHub Actions setup
* [Code coverage](code-cov.md) to measure how much code your tests
  cover
:::

## Tools to run your tests

There are three categories of tools that will make it easier to setup
and run your tests in various environments:

1. **Testing framework (pytest):** Provides the syntax and tools for
   writing and running your tests. Learn more from the
   [pytest documentation](https://docs.pytest.org/). Below you will learn
   about pytest, the most commonly used testing framework in the scientific
   Python ecosystem. Testing frameworks are essential for running tests, but
   they don't provide an easy way to run tests across Python versions
   or in isolated environments—that's where automation tools come in.

2. **Automation tools (Nox, Tox, Hatch):** Allow you to run tests in
   isolated environments and across multiple Python versions with a
   single command. We focus on
   [**Hatch**](https://hatch.pypa.io/) and
   [**Nox**](https://nox.thea.codes/) below. These tools create virtual
   environments automatically and ensure your tests run consistently.
   However, they typically only test on your local operating system.

3. **Continuous Integration (CI):** Runs your tests online across
   different operating systems (Windows, Mac, and Linux) and Python
   versions. CI integrates with platforms like GitHub Actions to
   automatically test every pull request and code change.
   [Learn about CI here](tests-ci), or see our
   [continuous integration tutorial](../../maintain-automate/ci.html)
   for more context.

### Quick comparison: what each tool does

**Testing Framework (pytest):**

* Runs your tests locally in your current Python environment
* Provides the core syntax for writing tests (assertions, fixtures,
  etc.)
* Can be extended with plugins (like pytest-cov for coverage)

**Automation Tools (Nox, Tox, Hatch):**

* Run tests locally across multiple Python versions
* Create and manage isolated virtual environments automatically
* Can automate other tasks like building documentation
* Make it easy to reproduce test environments

**Continuous Integration (GitHub Actions):**

* Runs tests online automatically for every pull request
* Tests across different operating systems (Windows, Mac, Linux)
* Tests across multiple Python versions in parallel
* Can automate deployments, releases, and other workflows

## What testing framework / package should I use to run tests?

We recommend using `Pytest` to build and run your package tests. Pytest is the most common testing tool used in the Python ecosystem.

[The Pytest package](https://docs.pytest.org/en/latest/) also has a number of
extensions that can be used to add functionality such as:

* [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) allows you to analyze the code coverage of your package during your tests, and generates a report that you can [upload to codecov](https://about.codecov.io/).

:::{todo}
Learn more about code coverage here. (add link)
:::

```{note}
Your editor or IDE may add additional convenience for running tests, setting breakpoints, and toggling the `–no-cov` flag. Check your editor's documentation for more information.
```

## Run tests using pytest

If you are using **pytest**, you can run your tests locally by
calling:

`pytest`

Or if you want to run a specific test file - let's call this file "`test_module.py`" - you can run:

`pytest test_module.py`

Learn more from the [get started docs](https://docs.pytest.org/en/7.1.x/getting-started.html).

Running pytest on your computer is going to run your tests in whatever
Python environment you currently have activated. This means that tests will be
run on a single version of Python and only on the operating system that you
are running locally.

An automation tool can simplify the process of running tests
in various Python environments.

:::{admonition} Tests across operating systems
If you want to run your tests across different operating systems you can [continuous integration. Learn more here](tests-ci).
:::

### Tools to automate running your tests

To run tests on various Python versions or in various specific environments with a single command, you can use an automation tool such as `nox` or `tox`.
Both `nox` and `tox` can create an isolated virtual environments. This allows you to easily run your tests in multiple environments and across Python versions.

We will focus on [Nox](https://nox.thea.codes/) in this guide. `nox` is a Python-based automation tool that builds upon the features of both `make` and `tox`. `nox` is designed to simplify and streamline testing and development workflows. Everything that you do with `nox` can be implemented using a Python-based interface.

```{admonition} Other automation tools you'll see in the wild
:class: note

- **[Tox](https://tox.wiki/en/latest/index.html#useful-links)** is an
  automation tool that supports common steps such as building
  documentation, running tests across various versions of Python, and
  more.

- **[Make](https://www.gnu.org/software/make/manual/make.html)** is a
  build automation tool that some developers use for running tests due
  to its versatility. However, Make's unique syntax can be challenging
  to learn, and it won't manage environments for you like Hatch and Nox
  do.
```

## Run tests with Hatch

**Hatch** is a modern Python packaging and environment manager that
integrates test running capabilities directly into your `pyproject.toml`.
Unlike Nox (which uses a separate `noxfile.py`), Hatch keeps all your
project configuration in one place, making it ideal if you're already
using Hatch for packaging workflows.

### Why Hatch for testing?

* Configuration lives in `pyproject.toml` alongside your project
  metadata
* Integrates seamlessly with Hatch's packaging and build workflows
* No separate Python file needed (unlike Nox)
* Easy to share standardized test environments across your team

### Setting up Hatch environments

Hatch environments are defined in your `pyproject.toml`. Rather than
duplicating dependencies, use `dependency-groups` to reference your test
dependencies:

```toml
[dependency-groups]
tests = [
    "pytest>=7.0",
    "pytest-cov",
]

[tool.hatch.envs.test]
dependency-groups = [
     "tests",
]

[tool.hatch.envs.test.scripts]
run = "pytest {args:--cov=test --cov-report=term-missing --cov-report=xml}"

```

This approach keeps your test dependencies in one place and avoids
duplication. For a complete example, see our
[packaging template tutorial](https://www.pyopensci.org/tutorials/create-python-package.html)
which shows a full `pyproject.toml` configuration.

### Running tests with Hatch

Once you've defined your test environment, you can run tests with simple
commands:

**List available environments:**

```bash
hatch env show
```

**Run pytest in the test environment:**

```bash
hatch run test:run
```

### Testing across Python versions

To test across multiple Python versions, define a matrix in your
`pyproject.toml`:

```toml
[dependency-groups]
tests = [
    "pytest>=7.0",
    "pytest-cov",
]

[tool.hatch.envs.test]
dependency-groups = [
     "tests",
]

[[tool.hatch.envs.test.matrix]]
python = ["3.10", "3.11", "3.12"]
```

Then run all versions with a single command:

```bash
hatch run test:run
```

Hatch will automatically run your tests on Python 3.10, 3.11, and 3.12.
If you only want to test a specific Python version:

```bash
hatch run test.py3.11:pytest
```

### Using Hatch in GitHub Actions

Hatch integrates well with CI/CD. Here's a minimal GitHub Actions
setup:

```yaml
name: Run tests

on:
  pull_request:
  push:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: hynek/setup-hatch@v1
      - run: hatch run test:pytest
```

Since all test dependencies are declared in `pyproject.toml`, your CI
environment is reproducible and consistent with local testing.

## Nox vs Hatch: choosing the right tool

Both Hatch and Nox are excellent automation tools for running tests
across Python versions. Here's how they compare to help you decide which
fits your workflow:

### Hatch

* **Configuration:** All settings live in `pyproject.toml` alongside your
  project metadata
* **Integration:** Seamlessly integrates with Hatch's packaging and build
  workflows—use the same tool for everything
* **Learning curve:** Easier if you prefer configuration over code
* **Best for:** Teams using Hatch for packaging, or those who want
  standardized configuration in one place

### Nox

* **Configuration:** Python-driven via `noxfile.py` for maximum flexibility
* **Customization:** Great for complex workflows that need custom logic
* **Learning curve:** Easier if you already know Python and want flexible
  session control
* **Best for:** Complex automation needs, building docs alongside tests,
  or workflows that don't fit the standard model

### What we recommend

**If you're using Hatch for packaging:** Use Hatch for testing too. You get
everything in one place and one consistent tool.

**If you need maximum flexibility:** Choose Nox. Its Python-driven approach
lets you implement almost any workflow.

**If you're just starting out:** Start with Hatch. It's simpler to set up
and understand, and you can always switch to Nox later if you need to.

**Both tools are solid choices.** The Python scientific community uses both
extensively. For a complete guide to Nox, see [Run tests with
Nox](run-tests-nox.md) and the [Scientific Python testing
guide](https://scientific-python.org/tools/testing).

## Next steps

Now that you understand how to run tests locally across Python versions, you
can learn about [running tests automatically in GitHub Actions with
continuous integration](tests-ci). You can also review [test types](test-types)
and [write tests](write-tests) for your package.
