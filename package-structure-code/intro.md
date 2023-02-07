# Python package structure information

If you plan to submit a package for review to pyOpenSci and are looking for
some guidance on package structure, code formats and style, then this section is for you.

## Guidelines for pyOpenSci's packaging recommendations

<!-- Might belong on the LANDING page for this entire guide?-->

There are some differing opinions on what Python package structure should
look like and what tools to use across the Python ecosystem.

In this guide, we have made decisions around suggested standards and required
standards, based upon the commonly used approaches in the scientific Python
community.  Our goal is to help standardize packaging across this ecosystem.

In some cases the suggestions here may diverge from those in the non-scientific parts of the Python ecosystem.

```{note}
The suggestions for package layout in this section are made with the
intent of being helpful; they are not specific requirements for your
package to be reviewed and accepted into our ecosystem.
```

In all cases, we try to align our suggestions with the most current, accepted
[PEP's (Python Enhancement Protocols)](https://peps.python.org/pep-0000/) and the [scientific-python community specs](https://scientific-python.org/specs/).
If you plan to submit a package for review to pyOpenSci and are looking for
some guidance on package structure, code formats and style, then this section
is for you.

<!-- TODO: move this either to the top of this section or the landing page?-->

```{note}
Have a look at the
bare-minimum [editor checks](https://www.pyopensci.org/peer-review-guide/software-peer-review-guide/editor-in-chief-guide.html#editor-checklist-template) that pyOpenSci
performs before a review begins. These checks are useful to explore
for both authors planning to submit a package to us for review and for
anyone who is just getting started with creating a Python package.

In general these are basic items that should be in any open software repository.
```

## Guidelines for pyOpenSci's packaging recommendations

<!-- Might belong on the LANDING page for this entire guide?-->

Python is a flexible programming language that is used across numerous
disciplines and domains. Python is so flexible that it is one of the few
languages that can be used to wrap around other languages.

If you are building a pure Python package, then your packaging setup can be
simple. However, some scientific packages have complex requirements as they may
need to support extensions or tools written in other languages such as C or C++.

To support the many different uses of Python, there are many ways to create a
Python package.

The ecosystem is dynamic, and constantly evolving to support
the numerous needs that developers (and scientists) have using Python.

This dynamic yet flexible environment is what many love about Python.

## What you will learn here

In this section of our Python packaging guide, we try to:

* Provide an overview of the options available to you when packaging your tool
* Suggest tools and approaches that both meet your needs and also support existing standards.
* Suggest tools and approaches that will allow you to expand upon a workflow that may begin as a pure Python tool and evolve into a tool that requires addition layers of complexity in the packaging build.
* Align our suggestions with the most current, accepted
[PEPs (Python Enhancement Protocols)](https://peps.python.org/pep-0000/) and the [scientific-python community SPECs](https://scientific-python.org/specs/).
* In an effort to maintain consistency within our community , we also align with existing best practices being implemented by developers of core Scientific Python packages such as Numpy, SciPy and others.


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
What are SDIst & Wheel Files? <python-package-distribution-files-sdist-wheel>
Package Build Tools <python-package-build-tools>
Complex Builds <complex-python-package-builds>
```
