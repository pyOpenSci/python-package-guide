# Documentation for your Open Source Python Package

:::{toctree}
:hidden:
:caption: Intro

Documentation Overview <self>
:::

```{toctree}
:hidden:
:maxdepth: 2
:caption: Write User Documentation

Intro <write-user-documentation/intro.md>
Create Your Docs <write-user-documentation/get-started>
Document Your Code (API) <write-user-documentation/document-your-code-api-docstrings.md>
Create Package Tutorials <write-user-documentation/create-package-tutorials.md>
```

```{toctree}
:hidden:
:caption: Docs for Contributors & Maintainers
:maxdepth: 2

Intro <repository-files/intro.md>
Contributing File <repository-files/contributing-file.md>
Development Guide <repository-files/development-guide.md>
Changelog File <repository-files/changelog-file.md>
```

```{toctree}
:hidden:
:caption: Community Docs
:maxdepth: 2

README file <repository-files/readme-file-best-practices.md>
Code of Conduct File <repository-files/code-of-conduct-file.md>
LICENSE files <repository-files/license-files.md>
```

```{toctree}
:maxdepth: 2
:hidden:
:caption: Publication tools for your docs

Intro <hosting-tools/intro>
Sphinx for Docs <hosting-tools/sphinx-python-package-documentation-tools>
myST vs Markdown vs rst <hosting-tools/myst-markdown-rst-doc-syntax>
Publish Your Docs <hosting-tools/publish-documentation-online>
Website Hosting and Optimization <hosting-tools/website-hosting-optimizing-your-docs>
```

```{important}
Please note that the tools discussed here are those that
we see commonly used in the community. As tools evolve we
will update this guide. If you are submitting a package for
pyOpenSci peer review and use other tools that are not listed
in our guide to build your package you can still submit for
review! The tools listed here are suggestions, not
requirements. Our requirements are focused on the
documentation content of your package.
```

## Documentation is critical for your Python package's success

Documentation is as important to the success of your Python open source package
as the code itself.

Quality code is of course valuable as its how your package gets the tasks done. However, if users don't understand
how to use your package in their workflows, then they won't use it.

Further, explicitly documenting how to contribute is important if you wish
to build a base of contributors to your package.

## Two types of Python package users

The documentation that you write for your
package should target two types of users:

### 1. Basic Tool Users

Basic tool users are the people who will use your package code in their
Python workflows. They might be new(er) to Python and/or data science. Or
expert programmers. But they might not have a background in software
development. These users need to know:

- How to install your package
- How to install dependencies that your package requires
- How to get started using the code base
- Information on how to cite your code / give you credit if they are using it
  in a research application.
- Information on the license that your code uses so they know how they can
  or can't use the code in an operational setting.

### 2. Potential tool contributors

The other subset of users are more experienced and/or more engaged
with your package. As such they are
potential contributors. These users:

- might have a software development background,
- might also be able to contribute bug fixes to your package or updates to your documentation
- might also just be users who will find spelling errors in your documentation, or bugs in your tutorials.

These users need all of the things that a basic user needs. But, they
also need to understand how you'd like for them to contribute to your
package. These potential contributors need:

- A development guide to help them understand the infrastructure used in your package repository.
- Contributing guidelines that clarify the types of contributions that you welcome and how you'd prefer those contributions to be submitted.

```{important}
It's important to remember that the definition of what a contribution is can be
broad. A contribution could be something as simple as a bug report. Or fixing a
spelling issue in your documentation. Or it could be a code fix that includes a
new test that covers an edge-case that they discovered.
```

## Documentation elements that pyOpenSci looks for reviewing a Python package

In the pyOpenSci open peer review, we look for
a documentation structure that supports both your tool users and potential
contributors. The files and elements that we look for specifically can be
found in our peer review check list (see link below).

In this guide, we discuss each required element, and also discuss other elements
that you should consider in your package's documentation in more detail.


```{button-link} https://www.pyopensci.org/software-peer-review/how-to/editor-in-chief-guide.html#editor-checklist-template
:color: primary
:class: sd-rounded-pill float-left
View pyOpenSci peer review check list
```


```{figure} ../images/moving-pandas-python-package-github-main-repo.png
---
name: moving-pandas-github-repo-image
width: 80%
alt: Image showing the files in the the MovingPandas GitHub repository. Files in the image include code of conduct.md contributing.md license.txt and readme.md.
---
An example from the MovingPandas GitHub repository with all of the major files in it including CONTRIBUTING.md, README.md, CODE_OF_CONDUCT.md and a LICENSE.txt file. *(screen shot taken Nov 23 2022)*
```

## What's next in this Python package documentation section?

In this section of the pyOpenSci package guide, we will walk
you through best practices for setting up
documentation for your Python package. We will also suggest
tools that you can use to build your user-facing documentation website.

:::{todo}

Python version support
You should always be explicit about which versions of Python your package supports.
Keeping compatibility with old Python versions can be difficult as functionality changes.
A good rule of thumb is that the package should support, at least,
the latest three Python versions (e.g., 3.8, 3.7, 3.6).
:::
