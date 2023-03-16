# pyOpenSci Python Open Source Package Development Guide

```{toctree}
:hidden:
:caption: Documentation

Documentation <documentation/index>

```

```{toctree}
:hidden:
:caption: Packaging

Packaging <package-structure-code/intro>

```

```{toctree}
:hidden:
:caption: CI and Testing

CI & Tests  <ci-and-testing/intro>
```

<!-- Github community standards
https://github.com/pyOpenSci/python-package-guide/community -->

## Welcome, Python open source enthusiast!

Here you will find guidelines for what we look for in your scientific
Python package when reviewing. You will also find best practice recommendations and curated lists of community resources surrounding packaging and documentation. Our goal is to help the
community make decisions around how to create scientific Python packages. We are working towards a shared vision of packaging that helps users better understand where to start.

::::{grid} 2
:reverse:

:::{grid-item}
:columns: 4
:class: sd-m-auto

:::

:::{grid-item}
:columns: 8
:class: sd-fs-3

```{button-link} https://www.pyopensci.org/about-peer-review/
:color: primary
:class: sd-rounded-pill float-left
Learn about our open peer review process
```

```{only} html
![GitHub release (latest by date)](https://img.shields.io/github/v/release/pyopensci/python-package-guide?color=purple&display_name=tag&style=plastic)
[![](https://img.shields.io/github/stars/pyopensci/python-package-guide?style=social)](https://github.com/pyopensci/contributing-guide)
[![DOI](https://zenodo.org/badge/556814582.svg)](https://zenodo.org/badge/latestdoi/556814582)
```

:::
::::

<!-- I think this is the end of the header - below begins the next grid-->

::::{grid} 1 1 2 2
:class-container: text-center
:gutter: 3

:::{grid-item-card}
:link: documentation/index
:link-type: doc
:class-header: bg-light

✨ Documentation Criteria & Recommendations ✨
^^^

Learn more about the best practices for Python package
documentation and also some of the tools for creating
documentation that are
commonly used in the scientific Python community.
:::

:::{grid-item-card}
:link: package-structure-code/intro
:link-type: doc
:class-header: bg-light

✨ Python packaging tools & structure ✨
^^^
All of the modern tools discussed in this guide will help you build an efficient packaging workflow. This section helps you select the tool that will work best for you.
:::

:::{grid-item-card}
:link: CONTRIBUTING
:link-type: doc
:class-header: bg-light

✨ Want to contribute? ✨
^^^
We welcome contributions to this guide. Learn more about how you can
contribute.
:::
::::

## Who this guidebook is for

We assume that you are here because you are:

1. Looking for guidance on creating a Python package.
1. Looking for resources associated with Python packaging.
1. Considering submitting a package to pyOpenSci and want to understand what we are looking for when we review your package

Well, friend, you've come to the right place!

## What you will find in this guidebook

This guidebook contains:

- Explanation for "Good enough" minimum requirements associated with being reviewed by pyOpenSci
- Explanation of better and best practices in case you want to set the bar higher for your package (which we hope you will)!
- A curated list of resources to help you get your package into documented, usable and tested shape.

## Where this guide is headed

Most of the sections in this guide will ultimately include Good/Better/Best recommendations for Python open source software packaging.

Good meets the requirements. Going beyond the minimum can make package maintenance easier-to-use for new users, easier-to contribute for new contributors and easier-to-maintain for you.

This guide is now a work in progress. If you have ideas of things you'd like
to see here, [we invite you to open an issue on GitHub that details any changes or additions that you'd like to see.](https://github.com/pyOpenSci/python-package-guide/issues).
