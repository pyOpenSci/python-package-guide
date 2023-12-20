# Tests and data for your Python package

Tests are an important part of your Python package because they
provide a set of checks that ensure that your package is
functioning how you expect it to.

In this section you will learn more about the importance of writing
tests for your Python package and how you can setup infrastructure
to run your tests both locally and on GitHub.


::::{grid} 1 1 3 3
:class-container: text-center
:gutter: 3

:::{grid-item-card}
:link: write-tests
:link-type: doc

✨ Why write tests ✨
^^^

Learn more about the art of writing tests for your Python package.
Learn about why you should write tests and how they can help you and
potential contributors to your project.
:::

:::{grid-item-card}
:link: test-types
:link-type: doc

✨ Types of tests ✨
^^^
There are three general types of tests that you can write for your Python
package: unit tests, integration tests and end-to-end (or functional) tests. Learn about all three.
:::

:::{grid-item-card}
:link: run-tests
:link-type: doc

✨ How to Run Your Tests ✨
^^^

Learn more about what tools you can use to run tests. And how to run your
tests on different Python versions and different operating systems both on
your computer and using continuous integration on GitHub (or in any other CI).
:::
::::


:::{figure-md} fig-target

<img src="../images/packaging-lifecycle.png" alt="" width="800px">

Graphic showing the elements of the packaging process.
:::

```{toctree}
:hidden:
:maxdepth: 2
:caption: Create & Run Tests

Intro <self>
Write tests <write-tests>
Test types <test-types>
Run tests <run-tests>
Code coverage <code-cov>

```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Continuous Integration

Intro to CI <ci>
Run tests in CI <tests-ci>

```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Package data

Package data <data>

```
