(task-runners-intro)=
# Task Runners for Python Packaging

## What is a Task Runner?

A task runner is a tool that automates repetitive development
workflows. Instead of typing out long command sequences every time you
need to test your code, build documentation, or check your package, you
define these tasks once and run them with simple commands.

For example, rather than running:

```bash
python -m build
twine check dist/*
check-wheel-contents dist/*.whl
```

You can define a task and run:

```bash
hatch run build:check
```

Most modern task runners also include environment management features
that make it quick and easy to run tasks. Task runners ensure that
workflows are executed consistently every time, whether you're running
them on your laptop or in continuous integration, and they also make it
easier for contributors to recreate the same workflows in their local
environments.

## Benefits of task runners

Task runners provide several benefits for package development. When you
use a task runner, everyone on your team runs tasks the same way,
reducing environment-specific issues and "works on my machine"
problems. Complex multi-step processes become single commands, so
contributors don't need to memorize or look up lengthy command
sequences.

Many task runners also create isolated environments for different
workflows, ensuring the right dependencies are available for each task
without conflicts. This means your tasks run the same way locally and
in continuous integration, making debugging easier and builds more
reliable.

## Two types of task runners

The most common task runners used in the Python ecosystem fall into two categories:

### Environment + command managers

You can use these to both create custom isolated environments and also to run your tasks.

* **[Hatch](https://hatch.pypa.io/):** Hatch is an all-in-one package management tool that includes a built-in task runner. It uses a declarative TOML configuration in your `pyproject.toml` file, which means everything related to your package—metadata, dependencies, and tasks—lives in one place. Hatch also integrates with UV for fast environment creation.
* **[Nox](https://nox.thea.codes/):** Nox is a flexible Python-based task runner that uses a code-based (imperative) configuration approach. You write Python functions to define your tasks in a `noxfile.py`, which gives you maximum flexibility for complex testing scenarios and conditional logic. It's especially popular in the Scientific Python ecosystem.
* **[Tox](https://tox.wiki/):** Tox is a mature declarative tool that uses INI or TOML configuration files. It's particularly well-suited for testing across multiple Python versions and dependency combinations, and has been a standard in the Python community for years.

#### Command-only tools

These tools execute your commands but don't manage environments.

* **[Make](https://www.gnu.org/software/make/):** Make is a traditional build automation tool that uses Makefiles. It's widely known and available on most systems, making it a good choice for simple task automation when you don't need Python-specific features. However, it can have cross-platform compatibility issues, especially on Windows.
* **[Just](https://just.systems/):** Just is a modern command runner written in Rust with simple, Make-like syntax. It's fast, cross-platform, and easy to learn, making it a good lightweight alternative when you need basic task running without environment management.

Generally the two task runners that pyOpenSci suggests and uses are
[Nox](https://nox.thea.codes/en/stable/) and [Hatch (also a package management tool)](https://hatch.pypa.io/latest/).
Below, you will learn about the differences between all of the tools
and can make a decision for yourself depending on your needs.

## pyOpenSci recommends: Hatch and Nox

At pyOpenSci, the recommendation is **Hatch** for Python package
development. Hatch also includes a task and environment system feature.
Using Hatch means you don't need to setup another tool like Nox.

However, **Nox** is also an excellent choice, particularly if you need
complex testing, build or workflow logic.

You'll find many of the pyOpenSci documentation repositories use Nox to
automate workflows such as building and testing documentation.

### Why use Hatch?

Hatch is an all-in-one tool that helps you manage metadata,
dependencies, build configuration, and tasks together in
`pyproject.toml`. Using Hatch, everything related to your package lives
in one place. It combines packaging (building and publishing) with
everyday development tasks like testing, docs, and formatting, making
workflows easier to run and share. Hatch also integrates with UV making
it extremely fast. Finally, Hatch follows modern packaging practices
(for example, PEP 621), so your project stays aligned with community
standards.

### Why use Nox?

Python-based configuration gives Nox maximum flexibility, making it
easy to express complex logic and conditionals directly. Because
sessions are written in Python, they are explicit and easy to inspect
and debug. Nox is particularly powerful for handling complex test and
build scenarios that some packages require.

### Declarative vs. imperative configuration

An important distinction between these tools is how you configure them:

Hatch is a **Declarative tool**. This means it uses a configuration
file where you specify *what* you want. See the example below:

```toml
# pyproject.toml (Hatch)
[tool.hatch.envs.test]
dependencies = ["pytest", "pytest-cov"]

[tool.hatch.envs.test.scripts]
run = "pytest {args:tests}"
```

Nox uses an **Imperative** approach to defining workflows. With Nox,
you write Python code that defines how to perform a task. An example of
a Nox function (which would live in a separate noxfile.py file) is
shown below:

```python
# noxfile.py (Nox)
@nox.session
def test(session):
    session.install("pytest", "pytest-cov")
    session.run("pytest", *session.posargs)
```

## Trade-offs: declarative vs. imperative

* **Declarative (Hatch, Tox):** Simpler syntax, easier to read and
  maintain. Might be slightly less flexible for complex logic (this is
  user dependent).
* **Imperative (Nox):** You can easily include complex logic and
  conditionals. Because it uses Python, it might be more familiar to
  you!

Neither approach is inherently better—it depends on your needs and
preferences. Projects with complex testing scenarios may benefit from
Nox's flexibility, while projects wanting simple, standardized workflows
may prefer the clarity of declarative configuration.

## An overview of the core task runners tools that you will find in
the Python ecosystem

### Comparison table

Below you will see a comparison of features associated with each tool.
Each tool is then described in a bit more detail just in case you want
a better lay of the land.

| Feature | Hatch | Nox | Tox | Make | Just |
|---------|-------|-----|-----|------|------|
| **Configuration** | pyproject.toml | noxfile.py | tox.ini | Makefile | justfile |
| **Configuration Style** | Declarative | Imperative | Declarative | Declarative | Declarative |
| **Language** | TOML | Python | INI/TOML | Make syntax | Just syntax |
| **Python-specific** | Yes | Yes | Yes | No | No |
| **Environment Management** | Yes | Yes | Yes | No | No |
| **Matrix Testing** | Yes | Yes | Yes | No | No |
| **Packaging Integration** | Yes | No | No | No | No |
| **Cross-platform** | Yes | Yes | Yes | Limited | Yes |
| **Best For** | Complete package development | Complex testing workflows and other builds | Legacy projects, standard testing | Simple tasks | Simple commands |

### Hatch

[Hatch](https://hatch.pypa.io/) is a modern, all-in-one packaging and
task automation tool that simplifies Python package development by
handling everything from building and publishing to running tests and
formatting code. Hatch is what we use [in our packaging tutorials found in this guidebook](packaging-101).

#### Why we like Hatch

Hatch stands out because it's a single tool that handles both
packaging AND task running. Instead of juggling multiple tools, you
configure everything in your `pyproject.toml` file—no extra
configuration files needed. Hatch creates isolated environments for
different tasks (like testing or building docs) and integrates with UV
for extremely fast environment setup. It uses a declarative, clean
syntax that's easy to read and maintain, and it supports matrix testing
so you can easily test your package across multiple Python versions.

#### When to use Hatch

Hatch is ideal for complete package development workflows. You can use
it for testing across Python versions, building documentation, running
code formatters and linters, and building and publishing your package
to PyPI. If you want a modern, all-in-one solution that follows current
Python packaging standards (like PEP 621), Hatch is an excellent
choice.

#### Example configuration

Below is an example of how you'd set up a test environment in Hatch.
This configuration creates a `test` environment with pytest and
pytest-cov installed, defines a `run` script to execute your tests, and
sets up matrix testing to run tests on Python 3.10, 3.11, and 3.12:

```toml
# pyproject.toml

# This is a hatch environment (venv) called "test" that contains two dependencies
[tool.hatch.envs.test]
dependencies = ["pytest", "pytest-cov"]

# This is a script that hatch can run in the environment defined above.
[tool.hatch.envs.test.scripts]
run = "pytest {args:tests}"

# This is how you setup a matrix where hatch will create environments for each python version and run the test scripts in each environment. It will use UV to install python for each environment!
[[tool.hatch.envs.test.matrix]]
python = ["3.10", "3.11", "3.12"]
```

You would run the above in your terminal using:

`hatch run test:run`

**Learn more:** [Hatch documentation](https://hatch.pypa.io/)

### Nox

[Nox](https://nox.thea.codes/) is a Python-based automation toolkit
focused on testing across environments. It uses a code-based
(imperative) configuration approach that gives you maximum flexibility
for complex testing workflows.

#### Why we like Nox

Nox stands out because it uses Python code to define your tasks, which
means you can include complex logic and conditionals directly in your
automation workflows. Because sessions are written in Python, they're
explicit, easy to inspect, and straightforward to debug. Nox is
particularly powerful for handling complex test and build scenarios
that some packages require, and it's especially popular in the
Scientific Python ecosystem. You'll find many pyOpenSci documentation
repositories use Nox to automate workflows such as building and testing
documentation.

#### When to use Nox

Nox is ideal when you need complex testing scenarios with conditional
logic or when you prefer Python-based configuration over declarative
formats. It's excellent for testing across Python versions and managing
multiple testing environments. If packaging is handled separately and
you want maximum flexibility in your task automation, Nox is a great
choice.

#### Example configuration

Below is an example of a Nox session that runs tests across multiple
Python versions. The `@nox.session` decorator defines a session
(similar to a task), and you specify which Python versions to test
with. Nox will create isolated environments for each version and run
your tests:

```python
# noxfile.py
@nox.session(python=["3.10", "3.11", "3.12"])
def tests(session):
    # Install test dependencies
    session.install("pytest")
    # Run the tests
    session.run("pytest")
```

You would run the above in your terminal using:

`nox -s tests`

**Learn more:** [Nox documentation](https://nox.thea.codes/)

### Tox

[Tox](https://tox.wiki/) is a mature automation tool for testing in
multiple environments. It uses declarative configuration and has been a
standard in the Python community for years.

#### Why people use Tox

Tox is mature and stable, with a long history in the Python ecosystem.
It uses declarative configuration (traditionally INI format, though
TOML support was added recently) and is particularly good for testing
across Python versions and dependency sets. Many projects use Tox
because it integrates well with CI/CD systems and has a robust plugin
ecosystem.

#### When to use Tox

Tox is ideal if you're maintaining a legacy project that already uses
it, or if you have existing `tox.ini` configuration you want to
preserve. It's also a good choice if you need specific Tox plugins or
prefer declarative configuration separate from your packaging tools.
However, keep in mind that Tox can be slower than modern alternatives
like Hatch.

#### Example configuration

Below is an example of a Tox configuration that runs tests across
multiple Python versions. The `envlist` specifies which Python versions
to test, and the `testenv` section defines what to install and run:

```ini
# tox.ini
[tox]
envlist = py310,py311,py312

[testenv]
deps = pytest
commands = pytest tests/
```

You would run the above in your terminal using:

`tox` (runs all environments) or `tox -e py310` (runs a specific environment)

**Learn more:** [Tox documentation](https://tox.wiki/)

### Make

[Make](https://www.gnu.org/software/make/) is a traditional build
automation tool that uses Makefiles. It's been around since the 1970s
and is widely used across many programming languages.

#### Why people use Make

Make is widely known and available on most systems, making it a
familiar choice for many developers. It has simple syntax for basic
tasks and executes very quickly. Because it's not Python-specific, you
can use it to coordinate tasks across different languages in the same
project.

#### When to use Make

Make is best for simple task automation when you don't need
Python-specific features or environment management. It's a good
lightweight option if you want something fast and universally
available. However, be aware that Make can have cross-platform
compatibility issues, especially on Windows, and you'll need to handle
Python environment management separately.

#### Example configuration

Below is an example of a simple Makefile with tasks for testing and building documentation:

```makefile
test:
    pytest tests/

docs:
    sphinx-build docs docs/_build
```

You would run the above in your terminal using:

`make test` or `make docs`

### Just

[Just](https://just.systems/) is a modern command runner written in
Rust that offers a simpler, more user-friendly alternative to Make.

#### Why people use Just

Just has simple, Make-like syntax but with better error messages and
more intuitive behavior. It's fast, truly cross-platform (unlike Make),
and easy to learn. The tool is written in Rust, which makes it very
performant, and it avoids many of the quirks and gotchas that Make has
accumulated over decades.

#### When to use Just

Just is ideal when you need a lightweight command runner for simple
tasks and don't require Python-specific features or environment
management. It's a great choice if you want something faster and more
modern than Make, with better cross-platform support. However, keep in
mind that Just requires separate installation and has less integration
with the Python packaging ecosystem compared to tools like Hatch or
Nox.

#### Example configuration

Below is an example of a justfile with tasks for testing and building documentation:

```console
# justfile
test:
    pytest tests/

docs:
    sphinx-build docs docs/_build
```

You would run the above in your terminal using:

`just test` or `just docs`

**Learn more:** [Just documentation](https://just.systems/)

## Choosing the right task runner

**Choose Hatch if:**

* You're building a Python package
* You want an all-in-one tool
* You prefer configuration in pyproject.toml
* You want fast environment management
* You prefer declarative configuration

**Choose Nox if:**

* You need complex testing scenarios with conditional logic
* You prefer Python-based, imperative configuration
* You're working in the Scientific Python ecosystem
* Packaging is handled separately
* You want maximum flexibility

**Choose Tox if:**

* You're maintaining a legacy project already using it
* You have existing tox.ini configuration
* You need specific tox plugins
* You prefer declarative configuration separate from packaging

**Choose Make or Just if:**

* You need a lightweight command runner
* You're not doing Python-specific workflows
* You want something simple and fast
* You don't need environment management

## Next steps

* Learn how to use [Hatch environments](https://hatch.pypa.io/latest/tutorials/environment/basic-usage/)
* [Create a package using the Python package tutorial.](create-pure-python-package)
* Explore and use the
  [pyOpenSci package template](https://github.com/pyOpenSci/pyos-package-template)
  with pre-configured Hatch tasks
* Read the
  [Scientific Python development guide on task runners](https://learn.scientific-python.org/development/guides/tasks/).
  This guide is excellent if you plan to use nox as your task runner as
  it has lots of examples that you can follow.
