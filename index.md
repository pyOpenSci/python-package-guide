# pyOpenSci Python Package Guide

We support the Python tools that scientists need to create open science workflows.

::::{grid} 2
:reverse:

:::{grid-item}
:columns: 4
:class: sd-m-auto

:::

:::{grid-item}
:columns: 8
:class: sd-fs-3

```{only} html
![GitHub release (latest by date)](https://img.shields.io/github/v/release/pyopensci/python-package-guide?color=purple&display_name=tag&style=plastic)
[![](https://img.shields.io/github/stars/pyopensci/python-package-guide?style=social)](https://github.com/pyopensci/contributing-guide)
[![DOI](https://zenodo.org/badge/556814582.svg)](https://zenodo.org/badge/latestdoi/556814582)
```

:::
::::

::::{admonition} About this guide

:::{image} /images/tutorials/packaging-elements.png
:align: right
:width: 500
:alt: Image with the pyOpenSci flower logo in the upper right hand corner. The image shows the packaging lifecycle. The graphic shows a high level overview of the elements of a Python package. The inside circle has 5 items - user documentation, code/api, test suite, contributor documentation, project metadata / license / readme. In the middle of the circle is says maintainers and has a small icon with people. On the outside circle there is an arrow and it says infrastructure.
:::

This guide will help you:

1. Learn how to create a Python package from start to finish
1. Understand the broader Python packaging tool ecosystem
1. Navigate and make decisions around tool options
1. Understand all of the pieces of creating and maintaining a Python package

You will also find best practice recommendations and curated lists of community resources surrounding packaging and package documentation.
::::


```{todo}
TODO: change the navigation of docs to have a

user documentation
contributor / maintainer documentation
* development guide
* contributing guide

Community docs
* readme, coc, license

Publish your docs
```
## _new_ Tutorial Series: Create a Python Package

The first round of our community-developed, how to create a Python package tutorial series for scientists is complete! Join our community review process or watch development of future tutorials in our [GitHub repo here](https://github.com/pyOpenSci/python-package-guide).


:::::{grid} 1 1 2 2
:class-container: text-center
:gutter: 3

::::{grid-item}
:::{card} ✿ Create a Package Tutorials ✿
:class-card: left-aligned

* [What is a Python package?](/tutorials/intro)
* [Create a Python package](/tutorials/create-python-package)
* [Publish your package to (test) PyPI](/tutorials/publish-pypi)
* [Publish your package to conda-forge](/tutorials/publish-conda-forge)

:::
::::

::::{grid-item}
:::{card} ✿ Package Metadata Tutorials ✿
:class-card: left-aligned

* [How to add a README file](/tutorials/add-readme)
* [How to add metadata to a pyproject.toml file for publication to PyPI.](/tutorials/pyproject-toml.md)

:::
::::

::::{grid-item}
:::{card} ✿ Packaging Tool Tutorials ✿
:class-card: left-aligned

* [Introduction to Hatch](/tutorials/get-to-know-hatch)

:::
::::

::::{grid-item}
:::{card} ✿ Reference Guides ✿
:class-card: left-aligned

* [Command Line Reference Guide](/tutorials/command-line-reference)

:::
::::

:::::


## Python Packaging for Scientists

Learn about Python packaging best practices. You will also get to know the
the vibrant ecosystem of packaging tools that are available to help you with your Python packaging needs.

:::::{grid} 1 1 2 2
:class-container: text-center
:gutter: 3

::::{grid-item}
:::{card} ✨ Create your package ✨
:class-card: left-aligned

* [Package file structure](/package-structure-code/python-package-structure)
* [Package metadata / pyproject.toml](package-structure-code/pyproject-toml-python-package-metadata.md)
* [Build your package (sdist / wheel)](package-structure-code/python-package-distribution-files-sdist-wheel.md)
* [Declare dependencies](package-structure-code/declare-dependencies.md)
* [Navigate the packaging tool ecosystem](package-structure-code/python-package-build-tools.md)
* [Non pure Python builds](package-structure-code/complex-python-package-builds.md)

:::
::::

::::{grid-item}
:::{card} ✨ Publish your package ✨
:class-card: left-aligned

Gain a better understanding of the Python packaging ecosystem
Learn about best practices for:

* [Package versioning & release](/package-structure-code/python-package-versions.md)
* [Publish to PyPI & Conda-forge](/package-structure-code/publish-python-package-pypi-conda.md)

:::
::::
:::::

## Documentation

:::::{grid} 1 1 2 2
:class-container: text-center
:gutter: 3

::::{grid-item}
:::{card} ✨ Write The Docs ✨
:class-card: left-aligned

* [Create documentation for your users](/documentation/write-user-documentation/intro)
* [Core files to include in your package repository](/documentation/repository-files/intro)
* [Write tutorials to show how your package is used](/documentation/write-user-documentation/create-package-tutorials)
:::
::::

::::{grid-item}
:::{card} ✨ Developer Docs ✨
:class-card: left-aligned

* [Create documentation for collaborating developers](/documentation/repository-files/contributing-file)
* [Write a development guide](/documentation/repository-files/development-guide)
:::
::::

::::{grid-item}
:::{card} ✨ Document For A Community ✨
:class-card: left-aligned

* [Writing a README file](/documentation/repository-files/readme-file-best-practices)
* [Set norms with a Code of Conduct](/documentation/repository-files/code-of-conduct-file)
* [License your package](/documentation/repository-files/license-files)
:::
::::

::::{grid-item}
:::{card} ✨ Publish Your Docs ✨
:class-card: left-aligned

* [How to publish your docs](/documentation/hosting-tools/intro)
* [Using Sphinx](/documentation/hosting-tools/intro)
* [Markdown, MyST, and ReST](/documentation/hosting-tools/myst-markdown-rst-doc-syntax)
* [Host your docs on Read The Docs or GitHub Pages](/documentation/hosting-tools/publish-documentation-online)
:::
::::

:::::

## Tests

*We are actively working on this section. [Follow development here.](https://github.com/pyOpenSci/python-package-guide)*

:::::{grid} 1 1 2 2
:class-container: text-center
:gutter: 3

::::{grid-item}
:::{card} ✨ Tests for your Python package ✨
:class-card: left-aligned

* [Intro to testing](tests/index.md)
* [Write tests](tests/write-tests)
* [Types of tests](tests/test-types)
:::
::::

::::{grid-item}
:::{card} ✨ Run your tests ✨
:class-card: left-aligned

* [Run tests locally](tests/run-tests)
* [Run tests in CI](tests/tests-ci)
:::
::::
:::::

## Contributing

:::::{grid} 1 1 2 2
:class-container: text-center
:gutter: 3


::::{grid-item}
:::{card} ✨ Code style & Format ✨
:class-card: left-aligned
:link: CONTRIBUTING
:link-type: doc

* [Code style](package-structure-code/code-style-linting-format.md)
:::
::::

::::{grid-item}
:::{card} ✨ Want to contribute? ✨
:link: CONTRIBUTING
:link-type: doc
:class-card: left-aligned

We welcome contributions to this guide. Learn more about how you can
contribute.
:::
::::

:::::


:::{figure} https://www.pyopensci.org/images/people-building-blocks.jpg
:align: right
:width: 350
:alt: xkcd comic showing a stick figure on the ground and one in the air. The one on the ground is saying. `You're flying! how?`  The person in the air replies  `Python!` Below is a 3 rectangle comic with the following text in each box. Box 1 - I learned it last night. Everything is so simple. Hello world is just print hello world. Box 2 - the person on the ground says - come join us programming is fun again. It's a whole new world. But how are you flying? box 3 - the person flying says - i just typed import antigravity. I also sampled everything in the medicine cabinet. But i think this is the python. The person on the ground is saying - that's it?
:::

### A community-created guidebook

Every page in this guidebook goes through an extensive community review
process. To ensure our guidebook is both beginner-friendly and accurate, we encourage reviews from a diverse set of pythonistas and scientists with a wide range of skills and expertise.

```{button-link} https://github.com/pyOpenSci/python-package-guide#contributors-
:color: primary
:class: sd-rounded-pill float-left

View guidebook contributors

```

## Who this guidebook is for

This guidebook is for anyone interested in learning more about Python packaging. It is beginner-friendly and will provide:

1. Beginning-to-end guidance on creating a Python package.
1. Resources to help you navigate the Python packaging ecosystem of tools and approaches to packaging.
1. A curated list of resources to help you get your package into documented, usable and maintainable shape.

## Where this guide is headed

If you have ideas of things you'd like
to see here clarified in this guide, [we invite you to open an issue on GitHub.](https://github.com/pyOpenSci/python-package-guide/issues).

If you have questions about our peer review process or packaging in general, you are welcome to use our [pyOpenSci Discourse forum](https://pyopensci.discourse.group/).

This living Python packaging guide is updated as tools and best practices evolve in the Python packaging ecosystem. We will be adding new content over the next year.


:::{toctree}
:hidden:
:caption: Tutorials

Tutorials  <tutorials/intro>
:::

:::{toctree}
:hidden:
:caption: Packaging

Packaging <package-structure-code/intro>

:::

:::{toctree}
:hidden:
:caption: Documentation

Documentation <documentation/index>

:::


:::{toctree}
:hidden:
:caption: Testing

Tests  <tests/index>

:::


:::{toctree}
:hidden:
:caption: Continuous Integration

CI/CD  <continuous-integration/index>

:::
