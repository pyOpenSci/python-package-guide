# Python Package Structure & Code

This section covers everything you need to structure your Python package, configure metadata, choose build tools, and publish your package to PyPI and conda-forge.

:::::{grid} 1 2
:gutter: 3

::::{grid-item}
:::{card} New to Python packaging?
:class-card: sd-shadow-sm

**Start with our step-by-step tutorials:**

- Follow along as we create a package from scratch
- Learn by doing with guided examples
- Perfect for your first package

```{button-link} /tutorials/intro
:color: success
:class: sd-rounded-pill

Start the tutorial series
```

:::
::::

::::{grid-item}
:::{card} Already have code to package?
:class-card: sd-shadow-sm

**Jump into the reference guides:**

- Learn about package structure and metadata
- Compare build tools and choose what's right for you
- Understand the publishing process

Start with the cards below ↓
:::
::::

:::::

:::{admonition} How this content is developed
:class: note

All of the content in this guide has been vetted by community members, including maintainers and developers of the core packaging tools.
:::

## What you'll learn

In this section, you'll learn how to:

- **Structure your package** - Choose between src and flat layouts, organize tests and documentation
- **Configure metadata** - Set up `pyproject.toml` with project information, dependencies, and versioning
- **Choose build tools** - Compare Hatch, PDM, Poetry, and setuptools to find the right fit
- **Build distributions** - Create sdist and wheel files ready for publication
- **Publish your package** - Make your package available on PyPI and optionally conda-forge
- **Maintain code quality** - Set up linters and formatters to keep your code consistent

Our recommendations align with current [Python packaging standards](https://packaging.python.org/en/latest/) and [Scientific Python community specs](https://scientific-python.org/specs/), while prioritizing tools that are beginner-friendly and well-maintained.

## Package setup

:::::{grid} 1 1 2 2
:class-container: text-center
:gutter: 3

::::{grid-item}
:::{card} ✨ Package file structure ✨

Learn how to organize your package files using [src or flat layouts](package-source-layout). This page helps you decide on a package structure that follows modern Python best practices, including where to place [tests](src-layout-test) and [documentation](package-source-layout).
:::
::::

::::{grid-item}
:::{card} ✨ Add metadata ✨

Learn how to add [project metadata](pyproject-toml-python-package-metadata) to your Python package to support both
filtering on PyPI and also the metadata that a package installer needs to
build and install your package.
:::
::::

::::{grid-item}
:::{card} ✨ Declare dependencies ✨

Learn how to specify [required dependencies](required-dependencies), [optional feature dependencies](optional-dependencies), and [development dependencies](dependency-groups) in your [pyproject.toml file](pyproject-toml-overview).
:::
::::

::::{grid-item}
:::{card} ✨ Setup package versioning ✨

Learn how to manage package versions using [semantic versioning (SemVer)](package-versioning) or [calendar versioning (CalVer)](package-versioning). This page helps you choose the right versioning strategy and set up [automated version management](tools-version-management) using tools like hatch_vcs or setuptools-scm.
:::
::::

:::::

## Development practices

:::::{grid} 1 1 2 2
:class-container: text-center
:gutter: 3

::::{grid-item}
:::{card} ✨ Code style & linters ✨

Learn how to set up [code formatters and linters](code-style-tools) ([Black](about-black), [Ruff](about-ruff), [flake8](about-flake8)) to ensure your package follows [PEP 8 standards](code-style-tools) and maintains consistent code style throughout your project.
:::
::::

:::::

## Build & publish

:::::{grid} 1 1 2 2
:class-container: text-center
:gutter: 3

::::{grid-item}
:::{card} ✨ Choose your build tool ✨

Learn how to choose the right packaging tool for your project. Compare [Hatch](about-hatch), [PDM](about-pdm), [Poetry](about-poetry), and [setuptools](about-setuptools) to find the best fit for your workflow. See the [summary comparison](summary-build-tools) to help decide.
:::
::::

::::{grid-item}
:::{card} ✨ Build your package ✨

Learn how to build your Python package into [distribution files](build-package) ([sdist](python-source-distribution) and [wheel](python-wheel)) that can be published on [PyPI](publish-pypi-conda).
:::
::::

::::{grid-item}
:::{card} ✨ Publish to PyPI and Conda ✨

Learn how to publish your package to [PyPI](publish-pypi-conda) and optionally to [conda-forge](how-to-submit-to-conda-forge). This page covers the complete process for making your package available to users, including the [conda-forge submission process](how-to-submit-to-conda-forge) after publishing to PyPI.
:::
::::

:::::

## Choosing the right tools

Not sure which build tool to use? This decision tree can help you choose based on your package's needs:

:::{figure-md} packaging-tools-decision-tree

<img src="../images/python-package-tools-decision-tree.png" alt="Figure showing a decision tree with the various packaging tool front-end and back-end options." width="700px">

Use this decision tree to help select a packaging tool. See the [packaging tools page](python-package-build-tools) for detailed comparisons and recommendations.
:::

## Our recommendations

We suggest tools and approaches based on three principles:

1. **Beginner-friendly** - Tools that are easy to learn and use for those new to packaging
2. **Well-maintained** - Tools with active development and good documentation
3. **Standards-aligned** - Tools that follow current [Python packaging standards](https://packaging.python.org/en/latest/) and [Scientific Python community specs](https://scientific-python.org/specs/)

### Pure Python vs. complex builds

- **Pure Python packages** can use any modern tool (Hatch, PDM, Poetry, Flit) - choose based on the features you want
- **Packages with C/C++ extensions** may need additional build steps. See our [complex builds page](complex-python-package-builds) for guidance. For comprehensive information on packaging compiled projects, see the [Scientific Python Development Guide on compiled packaging](https://learn.scientific-python.org/development/guides/packaging-compiled/).

Most scientific Python packages start simple and can evolve to handle more complex requirements as needed.

## Submitting your package for peer review?

If you're planning to submit your package to pyOpenSci for [peer review](https://www.pyopensci.org/about-peer-review/index.html), check out our [editor checklist](https://www.pyopensci.org/software-peer-review/how-to/editor-in-chief-guide.html#editor-checklist-template) for the minimum requirements. These checks are useful for anyone creating a Python package, not just those submitting for review.

:::{admonition} These are recommendations, not requirements
:class: tip

The suggestions in this guide are designed to help you create a well-structured package. They are **not** specific requirements for pyOpenSci peer review.

If you're submitting to pyOpenSci, see our [package scope](https://www.pyopensci.org/software-peer-review/about/package-scope.html) and [author guide](https://www.pyopensci.org/software-peer-review/how-to/author-guide.html#) for actual review requirements.
:::

:::{toctree}
:hidden:
:caption: Create & Build Your Package

Intro <self>

Python package structure <python-package-structure>
pyproject.toml Package Metadata <pyproject-toml-python-package-metadata>
Declare dependencies <declare-dependencies>
Package Build Tools <python-package-build-tools>
Build Your Package <python-package-distribution-files-sdist-wheel>
Complex Builds <complex-python-package-builds>
:::

:::{toctree}
:hidden:
:caption: Publish your package

Publish with Conda / PyPI <publish-python-package-pypi-conda>
Package versions <python-package-versions>
Code style <code-style-linting-format>

:::
