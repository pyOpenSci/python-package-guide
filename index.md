# Welcome to the pyOpenSci Python Package Development Guide  

## pyOpenSci provides recommendations and a curated list of community resources that Python package infrastructure for the scientific community.

::::{grid} 2
:reverse:

:::{grid-item}
:columns: 4
:class: sd-m-auto

:::  

:::{grid-item}
:columns: 8
:class: sd-fs-3


<!-- 
Removing button for the time being
```{button-ref} start/your-first-book
:ref-type: doc
:color: primary
:class: sd-rounded-pill float-left


Get Involved (Maybe a link to a get involved page)

% SVG rendering breaks latex builds for the GitHub badge, so only include in HTML
``` -->

```{only} html
![GitHub release (latest by date)](https://img.shields.io/github/v/release/pyopensci/python-package-guide?color=purple&display_name=tag&style=plastic)
[![](https://img.shields.io/github/stars/pyopensci/python-package-guide?style=social)](https://github.com/pyopensci/contributing-guide)
[![DOI](https://zenodo.org/badge/556814582.svg)](https://zenodo.org/badge/latestdoi/556814582)
```

:::
::::


<!-- I think this is the end of the header - below begins the next grid-->

::::{grid} 1 1 1 2
:class-container: text-center
:gutter: 3

:::{grid-item-card}
:link: documentation/intro
:link-type: doc
:class-header: bg-light

✨ Documentation Criteria & Recommendations ✨
^^^

Learn about the good, better and best practices 
associated with Python package documentation. Topics 
covered include: README files, tutorials and full docs. 
:::

:::{grid-item-card}
:link: code-style-structure/intro
:link-type: doc
:class-header: bg-light

✨Code style and structure✨
^^^
Get a basic overview of our open peer review process for Python scientific open source software.
:::

::::


### Python Packaging Guide for Maintainers Submitting to PyOpenSci

Welcome to pyOpenSci! We assume you are here because 

1. you are considering submitting a package to pyOpenSci and want to understand the best practices that we suggest 
2. You are looking for guidance on creating your first Python package. 
3. Or you're just looking for resources associated with Python packaging.

Well, my friend you've come to the right place! 

## What you will find in this guidebook 

This guidebook contains: 

* Explanation for "Good enough" minimum requirements associated with being reviewed by pyOpenSci
* Explanation of better and best practices in case you want to set the bar higher for your package (which we hope you will)!
* A curated list of resources to help you get your package into documented, usable and tested shape. 


Most of the sections also include Good/Better/Best recommendations.
Good meets the requirements, but going beyond the minimum can make package maintenance easier-to-use for new users, easier-to contribute for new contributors and easier-to-maintain for you.

```{toctree}
:hidden:
:caption: Documentation

documentation/intro
documentation/readme-files
documentation/package-documentation-tutorials
```

```{toctree}
:hidden:
:caption: Code Style & Structure

code-style-structure/intro
```

```{toctree}
:hidden:
:caption: Test your code

testing-infrastructure/test-code
testing-infrastructure/continuous-integration
```

<!-- 
Removing button for the time being
```{button-ref} start/your-first-book
:ref-type: doc
:color: primary
:class: sd-rounded-pill float-left
Get Involved (Maybe a link to a get involved page)
``` -->


