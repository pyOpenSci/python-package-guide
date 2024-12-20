(ci-cd)=
# Continuous Integration and Continuous Deployment (CI/CD) For Python Packages

When you develop, work on, and contribute to software, there is more to consider than
just writing code. Having tests and checks ensures that your code
runs reliably and follows a consistent format is also important. You can use
**Continuous Integration (CI)** and **Continuous
Deployment (CD)** to run tests and checks on your code every time someone suggests a change online
in a platform like GitHub or GitLab.

- **Continuous Integration (CI):** Automates the process of running tests,
  code checks, and other workflows each time code is updated.
- **Continuous Deployment (CD):** Extends CI by allowing you to automate publishing your package to PyPI, publishing your documentation, and more.

CI and CD streamline software development by automating repetitive
tasks and ensuring code quality and consistency. Having CI setup also makes it easier for new contributors
to contribute to your code base without setting up all your test suites and
other local checks.

## What is continuous integration?

When you’re ready to publish your code online, you can set up Continuous Integration (CI). CI is a platform that allows you to specify and run jobs or workflows you define.
These workflows include:

- Running your test suite
- Running code checkers / linters / spellcheck
- Building your documentation

CI allows you to automate running workflows across a suite of environments, including:

- environments containing different Python versions and
- different operating systems (Mac, Linux, Windows).

## What is Continuous Deployment (CD)?

Continuous deployment (CD) extends the CI process by automating the deployment of code changes to production or staging environments. In the case of your open source tool, CD can be used to:

- Automate publishing to PyPI
- Automate publishing your documentation to GitHub Pages or Read the Docs.

It is also used once your conda-forge recipe is set up to keep your package up to date on conda-forge.

### Why use CI

CI can be configured to run a workflow on every commit pushed to GitHub and every pull request opened. This ensures that any changes made to your package are tested across environments before merging into the main branch of your code.

These checks are particularly useful if someone new is contributing to your code. Every contributor's change will be tested when pushed to your code repository.

Together, CI and CD streamline the process of building, testing, and deploying code. They aim to improve software development and publication efficiency, quality, and reliability.

```{note}
All pyOpenSci packages must use some form of continuous integration. Even if you are not planning to go through peer review, we strongly recommend that you use continuous integration, too!
```

In the case of GitHub actions (which we will focus on here), CI workflows are running on online servers that support GitHub.

## CI / CD platforms

There are numerous platforms available for CI/CD. Here, we will focus on GitHub Actions (GHA), built into GitHub. GitHub is the most commonly used platform to store scientific open-source software.

:::{note}
If you use [GitLab](https://about.gitlab.com/) CI/CD, many of the principles described here will apply. However, the workflow files may look different.
:::

### If you aren't sure, use GitHub Actions

While you are welcome to use the continuous integration platform of your choice,
we recommend GitHub Actions because it is free-to-use and integrated tightly
into the GitHub user interface. There is also an entire store of GitHub action
templates that you can easily use and adapt to your own needs.

:::{admonition} Other platforms that you may run into
:class: info

- [Appveyor:](https://www.appveyor.com/): Supports running tests on Windows operating systems and predated the release of GitHub Actions. Today, AppVeyor supports operating systems beyond Windows.
- [Travis CI:](https://www.travis-ci.com/) had been a common CI platform choice in our ecosystem. Usage dropped after Travis CI ended free support for open-source projects.
- [CircleCI:](https://circleci.com/) CircleCI can be useful for automated builds of websites and documentation since it offers a preview of the PR changes.
  :::

## Embrace automation

By embracing CI/CD, you can ensure that your code runs as you expect it to across the diverse landscapes of user environments. Further, you can
automate certain checks (and, in some cases, code fixes), including linting and code style. You can even automate spell-checking your documentation
and docstrings!
