# What is continuous integration?

When you’re ready to publish your code online, you can setup Continuous Integration (CI). CI is a platform that allows you to specify and run jobs or workflows that you define.
These workflows include:

- Running your test suite
- Running code checkers / linters / spellcheck
- Building your documentation
- Deploying your documentation to GitHub pages

CI allows you to automate running workflows across a suite of environments including:

- environments containing different Python versions and
- different operating systems (Mac, Linux, Windows).

### What is Continuous Deployment (CD)?

Continuous deployment (CD) extends the CI process by automating the deployment of code changes to production or staging environments. In the case of your open source tool, CD can be used to:

- Automate publishing to PyPI
- Automate publishing your documentation to GitHub Pages or Read the Docs.

It is also used once your conda-forge recipe is set up to keep your package up to date on conda-forge.

### Why Use CI

CI can be configured to run a workflow on every commit pushed to GitHub and every pull request opened. This ensures that any changes made to your package are tested across environments before they are merged into the main branch of your code.

These checks are particularly useful if someone new is contributing to your code. Every change a contributor makes will be tested when it’s pushed to your code repository.

Together, CI and CD streamline the process of building, testing, and deploying code. They aim to improve the efficiency, quality, and reliability of software development and publication.

```{note}
All pyOpenSci packages must use some form of continuous integration. Even if you are not planning to go through peer review, we strongly recommend that you use continuous integration too!
```

In the case of GitHub actions (which we will focus on here), CI workflows are running on online servers that support GitHub.

## CI / CD Platforms

There are numerous platforms available for CI/CD. Here, we will focus on GitHub Actions (GHA) which is built into GitHub. GitHub is the most commonly used platform to store scientific open source software.

:::{note}
If you are using GitLab CI/CD many of the principles described here will apply, however the workflow files may look different.
:::

### If you aren't sure, use GitHub Actions

While you are welcome to use the continuous integration platform of your choice,
we recommend GitHub Actions because it is free-to-use and integrated tightly
into the GitHub user interface. There is also an entire store of GitHub action
templates that you can easily use and adapt to your own needs.

:::{admonition} Other platforms that you may run into
:class: info

- [Appveyor:](https://www.appveyor.com/) used to be a `GOTO` for running tests on Windows operating systems until GitHub actions evolved to support Windows. AppVeyor has evolved to support other operating systems since Microsoft acquired GitHub.
- [Travis CI:](https://www.travis-ci.com/) Had been the most common CI platform used in our ecosystem until they dropped free support for open source.
- [CircleCI:](https://circleci.com/) You will still see some people using CircleCI for specific tasks. CircleCI can be useful for automated builds of websites and documentation allowing you to preview the changes to that website in your browser.
  :::

## Embrace automation

By embracing CI/CD, you can ensure that your code runs as you expect it to across the diverse landscapes of user environments. Further you can
automate certain checks (and in some cases code fixes) including linting and code style. You can even automate spell checking your documentation
and docstrings!
