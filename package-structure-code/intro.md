# Python package structure information

This section provides guidance on your Python package's structure, code formats and style. It also reviews the various packaging tools that you can use to
support building and publishing your package.

```{note}
If you are considering submitting a package for peer review, have a look at the
bare-minimum [editor checks](https://www.pyopensci.org/peer-review-guide/software-peer-review-guide/editor-in-chief-guide.html#editor-checklist-template) that pyOpenSci
performs before a review begins. These checks are useful to explore
for both authors planning to submit a package to us for review and for
anyone who is just getting started with creating a Python package.

In general these are basic items that should be in any open software repository.
```

## What you will learn here

In this section of our Python packaging guide, we:

* Provide an overview of the options available to you when packaging your tool
* Suggest tools and approaches that both meet your needs and also support existing standards.
* Suggest tools and approaches that will allow you to expand upon a workflow that may begin as a pure Python tool and evolve into a tool that requires addition layers of complexity in the packaging build.
* Align our suggestions with the most current, accepted
[PEPs (Python Enhancement Protocols)](https://peps.python.org/pep-0000/) and the [scientific-python community SPECs](https://scientific-python.org/specs/).
* In an effort to maintain consistency within our community , we also align with existing best practices being implemented by developers of core Scientific Python packages such as Numpy, SciPy and others.

## Guidelines for pyOpenSci's packaging recommendations

<!-- Might belong on the LANDING page for this entire guide?-->

The flexibility of the Python programming language lends itself to a diverse
range of tool options for creating a Python package. Python is so flexible that
it is one of the few languages that can be used to wrap around other languages.

If you are building a pure Python package, then your packaging setup can be
simple. However, some scientific packages have complex requirements as they may
need to support extensions or tools written in other languages such as C or C++.

To support the many different uses of Python, there are many ways to create a
Python package. In this guide, we suggest approaches for packaging approaches and tools based
upon:

1. What we think will be best and easiest to adopt for those who are newer to packaging
2. Tools that we think are well maintained and documented.
3. A shared goal of standardizing packaging approaches across this (scientific) Python ecosystem.

Here, we also try to align our suggestions with the most current, accepted
[Python community](https://packaging.python.org/en/latest/) and [scientific community](https://scientific-python.org/specs/).


```{admonition} Suggestions in this guide are not pyOpenSci review requirements
:class: important

The suggestions for package layout in this section are made with the
intent of being helpful; they are not specific requirements for your
package to be reviewed and accepted into our pyOpenSci open source ecosystem.

Please check out our [package scope page](https://www.pyopensci.org/software-peer-review/about/package-scope.html) and [review requirements in our author guide](https://www.pyopensci.org/software-peer-review/how-to/author-guide.html#) if you are looking for Python package review requirements!
```

<!--
```{tip}
### Python packaging resources that we love

We think the resources below are excellent but each have particular opinions
that you may or may not find in our packaging guide. For instance, the PyPA
guide encourages users to store their package in a `src/package-name` directory.
While we accept that approach many of our community members prefer to not use
the `src` directory.

* [Python packaging for research software engineers](https://merely-useful.tech/py-rse/)
* [PyPA packaging guide](https://packaging.python.org/en/latest/)
```
-->


```{toctree}
:hidden:
:caption: Package structure & code style

Intro <self>

Python package structure <python-package-structure>
pyproject.toml Package Metadata <pyproject-toml-python-package-metadata>
What are SDist & Wheel Files? <python-package-distribution-files-sdist-wheel>
Package Build Tools <python-package-build-tools>
Complex Builds <complex-python-package-builds>
```
