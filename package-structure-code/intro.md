# Python Package Structure

This section provides guidance on your Python package's structure, code format,
and style. It also reviews the various [packaging tools](python-package-build-tools) you can use to
[build](python-package-distribution-files-sdist-wheel) and [publish](publish-python-package-pypi-conda) your Python package.

If you want end-to-end tutorials, check out our tutorial series that starts by introducing [what a Python package is](what-is-a-package).

If you are confused by Python packaging, you are not alone! The good news is
that some great modern packaging tools ensure you follow
best practices. Here, we review tool features and suggest tools you can use
for your Python packaging workflow.

:::{button-link} /tutorials/intro
:color: success
:class: sd-rounded-pill float-left

Checkout our beginning-to-end create a Python package tutorials

:::


:::{admonition} How this content is developed
All of the content in this guide has been vetted by community members, including maintainers and developers of the core packaging tools.
:::


:::::{grid} 1 1 2 2
:class-container: text-center
:gutter: 3

::::{grid-item}
:::{card} ✨ 1. Package file structure ✨
:link: python-package-structure
:link-type: doc

src layout, flat layout and where should tests folders live? No matter what your level of packaging knowledge is, this page will help you decide upon a package structure that follows modern python best practices.
:::
::::

::::{grid-item}
:::{card} ✨ 2. Learn about building your package ✨
:link: python-package-structure
:link-type: doc

To publish your Python package on PyPI, you will need to first build it. The act
of "building" refers to the process of placing your package code and
metadata into a format that can be published on PyPI. Learn more about building
your Python package.
:::
::::


::::{grid-item}
:::{card} ✨ 4. Add metadata ✨
:link: pyproject-toml-python-package-metadata
:link-type: doc

Learn how to add project metadata to your Python package to support both
filtering on PyPI and also the metadata that a package installer needs to
build and install your package.
:::
::::

::::{grid-item}
:::{card} ✨ 3. What Python package tool should you use? ✨
:link: python-package-build-tools
:link-type: doc

Learn more about the suite of packaging tools out there.
And learn which tool might be best for you.
:::
::::

::::{grid-item}
:::{card} ✨ 4. Publish to PyPI and Conda ✨
:link: python-package-build-tools
:link-type: doc

If you have a pure Python package, it's a straight forward
process to publish to both PyPI and then a Conda channel such as
conda-forge. Learn more here.
:::
::::

::::{grid-item}
:::{card} ✨ 5. Setup package versioning ✨
:link: python-package-versions
:link-type: doc

Semver (numeric versioning) and Calver (versioning using the date) are 2
common ways to version a package. Which one should you pick? Learn more here.
:::
::::

::::{grid-item}
:::{card} ✨ 6. Code style & linters ✨
:link: code-style-linting-format
:link-type: doc

Black, blue, flake8, Ruff - which tools can help you ensure your
package follows best practices for code format? Learn more about the options
and why this is important here.
:::
::::

:::::

:::{figure-md} packaging-tools-decision-tree

<img src="../images/python-package-tools-decision-tree.png" alt="Figure showing a decision tree with the various packaging tool front-end and back-end options." width="700px">

Diagram showing the various front-end build tools that you can select from.
See the packaging tools page to learn more about each tool.
:::

:::{note}
If you are considering submitting a package for peer review, have a look
at the bare-minimum [editor checks](https://www.pyopensci.org/software-peer-review/how-to/editor-in-chief-guide.html#editor-checklist-template)
that pyOpenSci performs before a review begins. These checks are useful
to explore for both authors planning to submit a package to us for review
and for anyone who is just getting started with creating a Python package.
:::

## What you will learn here

In this section of our Python packaging guide, we:

- Provide an overview of the options available to you when packaging your
  code.
- Suggest tools and approaches that both meet your needs and also support
  existing standards.
- Suggest tools and approaches that will allow you to expand upon a workflow
  that may begin as a pure Python code and evolve into code that requires
  addition layers of complexity in the packaging build.
- Align our suggestions with the most current, accepted
  [PEPs (Python Enhancement Protocols)](https://peps.python.org/pep-0000/)
  and the [Scientific Python community SPECs](https://scientific-python.org/specs/).
- In an effort to maintain consistency within our community, we also align
  with existing best practices being implemented by developers of core
  Scientific Python packages such as Numpy, SciPy and others.

## Guidelines for pyOpenSci's packaging recommendations

The flexibility of the Python programming language lends itself to a diverse
range of tool options for creating a Python package. Python is so flexible that
it is one of the few languages that can be used to wrap around other languages.
The ability of Python to wrap other languages is one the reasons you will often
hear Python described as a ["glue" language](https://numpy.org/doc/stable/user/c-info.python-as-glue.html)"

If you are building a pure Python package, then your packaging setup can be
simple. However, some scientific packages have complex requirements as they may
need to support extensions or tools written in other languages such as C or C++.

To support the many different uses of Python, there are many ways to create a
Python package. In this guide, we suggest packaging approaches and tools based on:

1. What we think will be best and easiest to adopt for those who are newer to
   packaging.
2. Tools that we think are well maintained and documented.
3. A shared goal of standardizing packaging approaches across this (scientific)
   Python ecosystem.

Here, we also try to align our suggestions with the most current, accepted
[Python community](https://packaging.python.org/en/latest/) and [scientific community](https://scientific-python.org/specs/).

:::{admonition} Suggestions in this guide are not pyOpenSci review requirements
:class: important

The suggestions for package layout in this section are made with the
intent of being helpful; they are not specific requirements for your
package to be reviewed and accepted into our pyOpenSci open source ecosystem.

Please check out our [package scope page](https://www.pyopensci.org/software-peer-review/about/package-scope.html)
and [review requirements in our author guide](https://www.pyopensci.org/software-peer-review/how-to/author-guide.html#)
if you are looking for pyOpenSci's Python package review requirements!
:::

:::{toctree}
:hidden:
:caption: Create & Build Your Package

Intro <self>

Python package structure <python-package-structure>
pyproject.toml Package Metadata <pyproject-toml-python-package-metadata>
Build Your Package <python-package-distribution-files-sdist-wheel>
Declare dependencies <declare-dependencies>
Package Build Tools <python-package-build-tools>
Complex Builds <complex-python-package-builds>
:::

:::{toctree}
:hidden:
:caption: Publish your package

Publish with Conda / PyPI <publish-python-package-pypi-conda>
Package versions <python-package-versions>
Code style <code-style-linting-format>

:::
