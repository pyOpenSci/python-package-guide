# Code coverage for your Python package test suite

Code coverage measures how much of your package's code runs during testing.
Achieving high coverage can help ensure the reliability of your codebase, but
it’s not a guarantee of quality. Below, we outline key considerations for
using code coverage effectively.

## Why aim for high code coverage?

A good practice is to ensure that every line of your code runs at least once
during your test suite. This helps you:

- Identify untested parts of your codebase.
- Catch bugs that might otherwise go unnoticed.
- Build confidence in your software's stability.

## Limitations of code coverage

While high code coverage is valuable, it has its limits:

- **Difficult-to-test code:** Some parts of your code might be challenging to
  test, either due to complexity or limited resources.
- **Missed edge cases:** Running all lines of code doesn’t guarantee that edge
  cases are handled correctly.

Ultimately, you should focus on how your package will be used and ensure your
tests cover those scenarios adequately.

## Tools for analyzing Python package code coverage

Some common services for analyzing code coverage are [codecov.io](https://codecov.io/) and [coveralls.io](https://coveralls.io/). These projects are free for open source tools and will provide dashboards that tell you how much of your codebase is covered during your tests. We recommend setting up an account (on either CodeCov or Coveralls) and using it to keep track of your code coverage.

:::{figure} ../images/code-cov-stravalib.png
:height: 450px
:alt: Screenshot of the code cov service - showing test coverage for the stravalib package. This image shows a list of package modules and the associated number of lines and % lines covered by tests. At the top of the image, you can see what branch is being evaluated and the path to the repository.

The CodeCov platform is a useful tool if you wish to track code coverage visually. Using it, you can not only get the same summary information that you can get with the **pytest-cov** extension. You can also see what lines are covered by your tests and which are not. Code coverage is useful for evaluating unit tests and/or how much of your package code is "covered". It, however, will not evaluate things like integration tests and end-to-end workflows.

:::



:::{admonition} Typing & MyPy coverage
You can also create and upload typing reports to CodeCov.
:::

## Exporting Local Coverage Reports

In addition to using services like CodeCov or Coveralls, you can generate local coverage reports directly using the **coverage.py** tool. This can be especially useful if you want to create reports in Markdown or HTML format for offline use or documentation.

To generate a coverage report in **Markdown** format, run:

```bash
$ python -m coverage report --format=markdown
```
This command will produce a Markdown-formatted coverage summary that you can easily include in project documentation or share with your team.

To generate an HTML report that provides a detailed, interactive view of which lines are covered, use:

```bash
python -m coverage html
```

The generated HTML report will be saved in a directory named htmlcov by default. Open the index.html file in your browser to explore your coverage results.

These local reports are an excellent way to quickly review coverage without setting up an external service.
