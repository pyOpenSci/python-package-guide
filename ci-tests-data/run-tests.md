# Running your tests

### What test suite tools should I use to run tests?

We recommend using Pytest to set up testing infrastructure for your package as it is the most common testing tool used in the Python ecosystem.

[Pytest package](https://docs.pytest.org/en/latest/) also has a number of extensions that can be used to add functionality such as:

- [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) allows you to analyze the code coverage of your package during your tests, and generates a report that you can [upload to codecov](https://codecov.io/).

```{note}
Reference the issue with running tests in vscode, breakpoints and –no-cov flag. Then link to tutorial that explains how to deal with this.
```

### Running tests

**Tox**

- [Tox](https://tox.wiki/en/latest/index.html#useful-links) is an automation tool that supports common steps such as building documentation, running tests across various versions of Python, and more. You can find [a nice overview of tox in the plasmaPy documentation](https://docs.plasmapy.org/en/stable/contributing/testing_guide.html#using-tox).

**Make**

- Some developers opt to use Make for writing tests due to its versatility; it's not tied to a specific language and can be employed to orchestrate various build processes. However, Make's unique syntax and approach can make it more challenging to learn, particularly if you're not already familiar with it. Make also won't manage environments for you like nox will do.

**Hatch**

- [Hatch](https://github.com/ofek/hatch) is a modern end-to-end packaging tool that also has a nice build backend called hatchling. Hatch offers a tox-like setup where you can run tests locally using different Python versions. If you are using hatch to support your packaging workflow, you may want to also use its testing capabilities rather than using nox.

**[Nox](https://nox.thea.codes/):** is a Python-based automation tool that builds upon the features of both Make and Tox. Nox is designed to simplify and streamline testing and development workflows. Everything that you do with nox can be implemented using a Python-based interface.

## Run your test suite

Your package will be used by a diverse set of users who will be running various Python versions and using various operating systems. Thus you will want to run your test suite in all of these environments to identify issues that users may have before they run into them “in the wild”.

There are two primary ways that you can run tests - locally on your computer and in your CI build. We discuss both below.

## Section 2: Run tests on your computer

In this guide we recommend Nox for running your tests locally. However you will also see packages using Tox or Hatch to create local environments with different versions of Python for you. Some packages use the more traditional Make approach. Note that Make does not manage environments for you.

As discussed above, it’s ideal for you to make sure that you run your tests on the various combinations of operating systems and Python versions that your users may be using.

### Why we like nox

Nox simplifies the process of creating and managing different testing environments, allowing you to check how your code behaves across various Python versions and configurations. With Nox, you can define specific test scenarios, set up virtual environments, and run tests across operating systems with a single command. Running tests locally using tools like Nox help you create controlled environment(s) to run your tests, making sure your code works correctly on your own computer before sharing it with others.

We recommend Nox for this purpose because you can also use it to setup other types of development builds including building your documentation, package distributions and more. Nox also supports working with conda, venv and other environment managers.

### Working with Nox

## Environments

By default, Nox uses the Python built in ` venv` environment manager. A virtual environment (`venv`) is a self-contained Python environment that allows you to isolate and manage dependencies for different Python projects. It helps ensure that project-specific libraries and packages do not interfere with each other, promoting a clean and organized development environment.

Nox uses `venv`` by default. An example of using nox to run tests in venv environments for python versions 3.9, 3.10 and 3.11 is below.

```{warning}
Note that for the code below to work, you need to have all 3 versions of python installed on your computer for venv to find.
```

Below is an example of setting up nox to run tests using `venv`.

```python
import nox

# for this to run you will need to have python3.9, python3.10 and python3.11 installed on your computer. Otherwise nox will skip running tests for whatever versions are missing

@nox.session(python=["3.9", "3.10", "3.11"])
def test(session):

# install
session.install(".[all]")
# install dev requirements
session.install("-r", "requirements-dev.txt")
# Run tests
session.run("pytest")

```

Below is an example for setting up nox to use mamba (or conda).
Note that when you are using conda, it can automagically install
the various versions of Python that you need. You won't need to install all three Python versions if you use conda/mamba, like you do with `venv`.

```python
import nox

# The syntax below allows you to use mamba / conda as your environment manager, if you use this approach you don’t have to worry about installing different versions of Python

@nox.session(venv_backend='mamba', python=["3.9", "3.10", "3.11"])
def test(session):
    """Nox function that installs dev requirements and runs
    tests on Python 3.9 through 3.11
    """

    # Install dev requirements
    session.install(".[all]")
    # Install dev requirements
    session.install("-r", "requirements-dev.txt")
    # Run tests using any parameters that you need
    session.run("pytest")
```

### Running tests on CI

Running your test suite locally is useful as you develop code and also test new features or changes to the code base. However, you also will want to setup Continuous Integration (CI) to run your tests online. CI allows you to run all of your tests in the cloud. While you may only be able to run tests locally on a specific operating system that you run, in CI you can specify tests to run both on various versions of Python and across different operating systems.

CI can also be triggered for pull requests and pushes to your repository. This means that every pull request that you, your maintainer team or a contributor submit, can be tested. In the end CI testing ensures your code continues to run as expected even as changes are made to the code base. [Read more about CI here. ](https://docs.google.com/document/d/1jmo2l5u02c_F1zZi0bAIYXeJ6HiIryJbXzsNbMQQX6o/edit#heading=h.3mx2na93o7bf)

### CI Environment

CI Environment: When you’re ready to publish your code online, you can setup Continuous Integration (CI). A CI platform will allow you to not only run your tests on various Python versions but also different operating systems like Mac, Linux and Windows. Tools like GitHub Actions and GitLab CI/CD make it easy for you to run tests on various Python versions, and even on Windows, Mac, and Linux. CI can finally be configured to ensure that tests run on every push and pull request to your repository. This ensures that any changes made to your package are tested across operations systems and Python versions before they are merged into the main branch of your codebase. &lt;<tests in ci link here>>

By embracing these testing practices, you can ensure that your code runs as you expect it to across the diverse landscapes of user environments.

pr checks.
