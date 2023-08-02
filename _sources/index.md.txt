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
Python package when reviewing. You will also find best practice recommendations and curated lists of community resources surrounding packaging and package documentation.

### pyOpenSci's packaging goals

Our goal is to help the
community make decisions around how to create scientific Python packages. We are working towards a shared vision of packaging that helps users better understand where to start.

### How this guide is created

This guide is created by pyOpenSci through an extensive review process. Each page in the guide has been reviewed by experts in the broader Python packaging landscape including people from :

- conda & conda-forge
- the python packaging authority
- core Python developers
- core scientific Python developers
- and others with expertise in packaging, package documentation, usability and other related knowledge areas

[View all of the people who have contributed to this guide here.
](https://github.com/pyOpenSci/python-package-guide#contributors-)

We use this guide as a foundation for our open peer review process of
scientific software.

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

✨ Python packaging tools & structure ✨
^^^
All of the modern tools discussed in this guide will help you build an efficient packaging workflow. This section helps you select the tool that will work best for you.
:::

:::{grid-item-card}
:link: CONTRIBUTING
:link-type: doc

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

:::{figure-md} fig-target

<img src="/images/python-flying-xkcd.png" alt="xkcd comic showing a stick figure on the ground and one in the air. The one on the ground is saying. `You're flying! how?`  The person in the air replies  `Python!` Below is a 3 rectangle comic with the following text in each box. box 1 - I learned it last night. Everything is so simple. Hello world is just print hello world. box 2 - the person on the ground says - come join us programming is fun again. it's a whole new world. But how are you flying? box 3 - the person flying says - i just typed import antigravity. I also sampled everything in the medicine cabinet. But i think this is the python. the person on the ground is saying - that's it?" width="400px">

Many love to use Python because it is a clean language to learn. It also is incredibly flexible allowing it to be used across numerous domains. Source: xkcd comics.
:::

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

<!--
COMMENTED OUT TEXT TO BE MOVED


# TODO LINK TO CI BUILDS FOR Documentation>
Maybe we can curate a list of CI builds that people can use??? or is that moving too close to a cookie cutter situation

The text below is being moved to the packaging infrastructure section which
doesn't exist YET... but will soon .
pyOpenSci packages must:

- Contain full documentation for any user-facing functions.
- Have a test suite that covers the major functionality of the package.
- Use continuous integration.
- Use an OSI approved software license.


## Other recommendations
### Python version support
You should always be explicit about which versions of Python your package supports.
Keeping compatibility with old Python versions can be difficult as functionality changes.
A good rule of thumb is that the package should support, at least,
the latest three Python versions (e.g., 3.8, 3.7, 3.6).

### Code Style
pyOpenSci encourages authors to consult [PEP 8](https://www.python.org/dev/peps/pep-0008/) for information on how to style your code.

### Linting
An automatic linter (e.g. flake8) can help ensure your code is clean and free of syntax errors. These can be integrated with your CI.

-->
