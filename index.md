# pyOpenSci Python Open Source Package Development Guide  

<!-- Github community standards 
https://github.com/pyOpenSci/python-package-guide/community -->

## Welcome, Python open source enthusiast! 

Here you will find guidelines for what we look for in your scientific 
Python package when reviewing. You will also find best practice recommendations and curated lists of community resources surrounding packaging and documentation. 

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

::::{grid} 1 1 1 2
:class-container: text-center
:gutter: 3

:::{grid-item-card}
:link: documentation/index
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

✨ Package Structure & Code ✨
^^^
<!-- 
Get a basic overview of our open peer review process for Python scientific open source software. -->
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

1. Considering submitting a package to pyOpenSci and want to understand what we are looking for when we review your package
2. Looking for guidance on creating a Python package. 
3. Looking for resources associated with Python packaging.

Well, friend, you've come to the right place! 

## What you will find in this guidebook 

This guidebook contains: 

* Explanation for "Good enough" minimum requirements associated with being reviewed by pyOpenSci
* Explanation of better and best practices in case you want to set the bar higher for your package (which we hope you will)!
* A curated list of resources to help you get your package into documented, usable and tested shape. 

## Where this guide is headed 

Most of the sections in this guide will ultimately include Good/Better/Best recommendations for Python open source software packaging. 

Good meets the requirements. Going beyond the minimum can make package maintenance easier-to-use for new users, easier-to contribute for new contributors and easier-to-maintain for you.

This guide is now a work in progress. If you have ideas of things you'd like 
to see here, [we invite you to open an issue on GitHub that details any changes or additions that you'd like to see.](https://github.com/pyOpenSci/python-package-guide/issues).


```{toctree}
:hidden:
:caption: Documentation

Intro to Documentation <documentation/index>
The README File <documentation/create-readme-files.md>
README Files <documentation/readme-files>
Package documentation <documentation/package-documentation-sphinx>
Contributing & license files <documentation/contributing>
```

```{toctree}
:hidden:
:caption: Package structure & code style

Intro <package-structure-code/intro>

Python package structure <package-structure-code/python-package-structure>
Package Build Tools <package-structure-code/python-package-build-tools>
Package Versions <package-structure-code/python-package-versions>
package-structure-code/overview
package-structure-code/collaboration
Code Style & Format <package-structure-code/code-structure-style>
```





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
