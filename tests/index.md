(tests-intro)=
# Tests and data for your Python package

Tests are an important part of your Python package because they
provide a set of checks that ensure that your package is
functioning how you expect it to.

In this section, you will learn more about the importance of writing
tests for your Python package and how you can set up infrastructure
to run your tests both locally and on GitHub.

:::::{grid} 1 1 3 2
:class-container: text-center
:gutter: 3

::::{grid-item}
:::{card} ✨ Why write tests ✨
:link: write-tests
:link-type: doc
:class-card: left-aligned

Learn about the importance of writing tests for your Python
package and how they help you and potential contributors.
:::
::::

::::{grid-item}
:::{card} ✨ Types of tests ✨
:link: test-types
:link-type: doc
:class-card: left-aligned

Understand the three test types: unit, integration, and
end-to-end tests. Learn when and how to use each.
:::
::::

::::{grid-item}
:::{card} ✨ Run tests locally ✨
:link: run-tests
:link-type: doc
:class-card: left-aligned

Learn about testing tools like pytest, nox, and tox to run
tests across different Python versions on your computer.
:::
::::

::::{grid-item}
:::{card} ✨ Run tests online (using CI) ✨
:link: tests-ci
:link-type: doc
:class-card: left-aligned

Set up continuous integration with GitHub Actions to run
tests across Python versions and operating systems.
:::
::::

::::{grid-item}
:::{card} ✨ Code coverage ✨
:link: code-cov
:link-type: doc
:class-card: left-aligned

Measure how much of your package code runs during tests.
Learn to generate local reports and visualize coverage online.
:::
::::

:::::

```{toctree}
:hidden:
:maxdepth: 2
:caption: Create & Run Tests

Intro <self>
Write tests <write-tests>
Test types <test-types>
Run tests locally <run-tests>
Run tests with Nox <run-tests-nox>
Run tests online (using CI) <tests-ci>
Code coverage <code-cov>
```
