---
:og:description: Learn how to create a clear, effective README file for your Python package. This lesson covers what to include, why each section matters, and how a well-structured README improves usability and discoverability on GitHub and PyPI.
:og:title: Add a README file to your Python package
---

# Add a README file to your Python package

In the previous lessons you learned:

1. [What a Python package is](intro.md)
2. [How to make your code installable](create-python-package)
3. [How to publish your package to (test) PyPI](publish-pypi.md)
4. [How to publish your package to conda-forge](publish-conda-forge.md)

:::{admonition} Learning objectives

In this lesson you will learn:

1. How to add a **README.md** file to your package.
2. What the core elements of a **README.md** file are.
:::

## What is a README file?

The `README.md` file is a markdown file located at the root of your project directory that helps
a user understand:

- You package's name
- What the package does. Your README file should clearly state the problem(s) that your software is designed to solve and its target audience.
- The current development "state" of the package (through badges)
- How to get started with using your package.
- How to contribute to your package
- How to cite your package

Your **README.md** file is important as it is often the first thing that someone sees before they install your package. The README file is also used to populate your PyPI landing page.

Note that there is no specific content structure for README files.
However, this tutorial outlines the sections that we suggest that you
include in your README file.

## Create a README.md file for your package

It's time to add a `README.md` file to your project directory.

### Step 0: Create a README file
To get started, if you don't already have a README.md file in your project directory, create one.

:::{tip}
If you created your project directory from

* a GitHub repository online
* using `hatch init`

Then you may already have a README.MD file in your project directory.
:::

<!-- If they use hatch init in the very first lesson -
the readme will already be there-->

### Step 1: Add the name of your package as the README title

At the top of the `README.md` file, add the name of your package.

If you are using markdown it should be a header 1 (H1) tag which is denoted with a single `#` sign.

`# Package-title-here`

### Step 2: add badges to the top of your README file

It's common for maintainers to add badges to the top of their README files. Badges allow you and your package users to track things like:

* Broken documentation and test builds.
* Versions of your package that are on PyPI and conda.
* Whether your package has been reviewed and vetted by an organization such as pyOpenSci and/or JOSS.

If you have already published your package to pypi.org you can use [shields.io to create a package version badge](https://shields.io/badges/py-pi-version). This badge will dynamically update as you release new versions of your package to PyPI.

If not, you can leave the top empty for now and add badges to your README at a later point as they make sense.

### Step 3: Add a description of what your package does

Below the badges (if you have them), add a section of text
that provides an easy-to-understand overview of what your
package does.

* Keep this section short.
* Try to avoid jargon.
* Define technical terms that you use to make the description accessible to more people.

Remember that the more people understand what your package does, the more people will use it.

### Step 4: Add package installation instructions

Next, add instructions that tell users how to install your package.

For example, can they use pip to install your package?
`python -m pip install packagename`

or conda?

`conda install -c conda-forge packagename`.

If you haven't yet published your package to pypi.org then
you can skip this section and come back and add these
instructions later.

### Step 5: Any additional setup

In some cases, your package users may need to manually
install other tools in order to use your package. If that
is the case, be sure to add a section on additional setup
to your README file.

Here, briefly document (or link to documentation for) any
additional setup that is required to use your package.
This might include:

* authentication information, if it is applicable to your package.
* additional tool installations, such as GDAL.

:::{note}
Many packages won't need an additional setup section in their README.
In that case you can always skip this section.
:::


### Step 6: Add a get started section

Next add a get-started section. Within this section, add a small code example that demonstrates importing and using
some of the functionality in your package.

:::{admonition} Provide a fully functional code snippet if possible
:class: important

It is important to try to make the code examples that you provide your users as useful as possible.

Be sure to provide a copy/paste code example that will work as-is when pasted into a Jupyter Notebook or .py file if that is possible.

If there are tokens and other steps needed to run your package, be sure to be clear about what those steps are.
:::

For the pyosPackage, a short get started demo might look like this:

```python
>>> from pyospackage.add_numbers import add_num
>>> add_num(1, 2)
3
```

Or it could simply be a link to a getting started tutorial that you have created. If
you don't have this yet, you can leave it empty for the time being.

This would
also be a great place to add links to tutorials that
help users understand how to use your package for common workflows.


### Step 7: Community section

The community section of your README file is a place to include information for users who may want to engage with your project. This engagement will likely happen on a platform like GitHub or GitLab.

In the community section, you will add links to your contributing guide
and `CODE_OF_CONDUCT.md`. You will create a [`CODE_OF_CONDUCT.md` file in the next lesson](add-license-coc).

As your package grows you may also have a link to a development guide that contributors and your maintainer team will follow. The development guide
outlines how to perform maintenance tasks such as:

* running tests
* making package releases
* building documentation
* and more.



### Step 8: Citation information

Finally it is important to let users know how to cite your package.
You can communicate citation information in a few different ways.

You can use a tool such as zenodo to create a DOI and associated citation
information for your package if it is hosted on a platform such as
GitHub. [Check out this short tutorial that covers setting that up.](https://coderefinery.github.io/github-without-command-line/doi/)

Alternatively if you send your package through a peer review process such
as the [one lead by pyOpenSci](https://www.pyopensci.org/about-peer-review/index.html). After being accepted by pyOpenSci, if your package is in scope, you can be accepted by the Journal of Open Source Software and get a cross-ref DOI through [our partnership with the Journal of Open Source Software.](https://www.pyopensci.org/about-peer-review/index.html)


## The finished README file

Your finished `README.md` file should look something like this:

````markdown
# pyosPackage

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.8365068.svg)](https://doi.org/10.5281/zenodo.8365068)
[![pyOpenSci](https://pyopensci.org/badges/peer-reviewed.svg)](https://github.com/pyOpenSci/software-review/issues/115)

## What pyosPackage does

Short description here using non-technical language that describes what your package does.

## How to install pyosPackage

:::{todo}
- when i add more to the pyos package this can use that readme>
:::

To install this package run:

`python -m pip install pyosPackage`

## OPTIONAL - if you have additional setup instructions add them here. If not, skip this section.

## Get started using pyosPackage

Here add a quick code demo showing a user how to use the package after it is installed.

```python
>>> from pyospackage.add_numbers import add_num
>>> add_num(1, 2)
3

```

You can also add any links to tutorials in your documentation here.

## Community

Add information here about contributing to your package. Be sure to add links to your
`CODE_OF_CONDUCT.md` file and your development guide. For now this section might be
empty. You can go back and fill it in later.

## How to cite pyosPackage

citation information here
````

## <i class="fa-solid fa-hands-bubbles"></i> Wrap up

It's important to consider the information that a new user or contributor might
need when creating your `README.md` file. While there is no perfect template,
above is a set of recommendations as you are just getting started. You may find
the need for other elements to be added to this file as you further develop your
package and as a community begins to use your package.

In the [next lesson](add-license-coc.md), you will add a LICENSE file to
your Python package. A license file is critical as it tells users
how they legally can (and can't) use your package. It also:

* Builds trust with your users
* Discourages misuse of your package and associated code
