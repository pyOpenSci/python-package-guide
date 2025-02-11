(readme-file)=

# README File Guidelines and Resources

Your **README.md** file should be located in the root of your GitHub repository.
The **README.md** file is important as it is often the first thing that someone
sees before they install your package.

The README.md file is the landing page of:

* Your package as it appears on a repository site such as PyPI or Anaconda.org
* Your package's GitHub repository

Your README.md file is also used as a measure of package and community
health on sites such as:

* [GitHub community health for MovingPandas (available for all repositories)](https://github.com/movingpandas/movingpandas/community) and [Snyk - MovingPandas example](https://snyk.io/advisor/python/movingpandas)

```{figure} /images/pandera-python-package-readme-github.png
---
name: pandera-readme
width: 80%
alt: README landing page screenshot for the Pandera package. It has the Pandera logo at the top - which has two arrows in a chevron pattern pointing downward within a circle. Subtitle is statistical data testing toolkit. A data validation library for scientists, engineering, and analytics seeking correctness. Below that are a series of badges including CI tests passing, docs passing, version of Pandera on pypi (0.13.4), MIT license and that it has been pyOpenSci peer reviewed. There are numerous badges below that. Finally below the badges the text says, Pandera provides a flexible and expressive API for performing data validation on dataframe-like objects to make data processing pipelines more readable and robust.
---
Your GitHub repository landing page highlights the README.md file. Here you can see the README.md file for the pyOpenSci package [Pandera](https://github.com/unionai-oss/pandera). *(screen shot taken Nov 23 2022)*
```

Thus, it is important that you spend some time up front creating a high quality
**README.md** file for your Python package.

````{note}
An editor or the editor in chief will ask you to revise your README file
before a review begins if it does not meet the criteria specified below.

Please go through this list before submitting your package to pyOpenSci

```
### pyOpenSci README checklist

Your README file should have the following information:
- [ ] The name of the package
- [ ] Badges for the packages current published version, documentation and test suite build. (OPTIONAL: test coverage)
- [ ] Easy-to-understand explanation (2-4 sentences) of what your tool does
- [ ] Context for how the tool fits into the broader ecosystem
- [ ] If your library/package "wraps" around another package, link to the package that it is wrapping and any associated documentation. *(HINT: If you don't know what a wrapper is, this probably doesn't apply to you!)*
- [ ] A simple quick-start code example that a user can follow to provide a demonstration of what the package can do for them
- [ ] Links to your package's documentation / website.
- [ ] A few descriptive links to any tutorials you've created for your package.
```
````

## What your README.md file should contain

Your **README.md** file should contain the following things (listed from top to bottom):

### ✔️ Your package's name

Ideally your GitHub repository's name is also the name of your package. The more
self explanatory that name is, the better.

### ✔️ Badges for current package version, continuous integration and test coverage

Badges are a useful way to draw attention to the quality of your project. Badges
assure users that your package is well-designed, tested, and maintained. They
are also a useful maintenance tool to evaluate if things are building properly.
A great example of this is adding a [Read the Docs status badge](https://docs.readthedocs.io/en/stable/badges.html) to your README.md file to quickly
see when the build on that site fails.

It is common to provide a collection of badges towards the top of your
README file for others to quickly browse.

Some badges that you might consider adding to your README file include:

* Current version of the package on PyPI / Anaconda.org

Example: [![PyPI version shields.io](https://img.shields.io/pypi/v/pandera.svg)](https://pypi.org/project/pandera/)

* Status of tests (pass or fail) - Example: [![CI Build](https://github.com/pandera-dev/pandera/workflows/CI%20Tests/badge.svg?branch=main)](https://github.com/pandera-dev/pandera/actions?query=workflow%3A%22CI+Tests%22+branch%3Amain)

* Documentation build - Example: ![Docs Building](https://github.com/pyOpenSci/python-package-guide/actions/workflows/build-book.yml/badge.svg)

* DOI (for citation) Example: [![DOI](https://zenodo.org/badge/556814582.svg)](https://zenodo.org/badge/latestdoi/556814582)

```{tip}
Once you package is accepted to pyOpenSci, we will provide you with
a badge to add to your repository that shows that it has been reviewed.
[![pyOpenSci](https://pyopensci.org/badges/peer-reviewed.svg)](https://github.com/pyOpenSci/software-review/issues/12)

```

```{caution}
Beware of the overuse of badges! There is such a thing as too much of a good thing (which can overload a potential user!).
```

### ✔️ A short, easy-to-understand description of what your package does

At the top of your README file you should have a short, easy-to-understand, 1-3
sentence description of what your package does. This section should clearly
state your goals for the package. The language in this description should use
less technical terms so that a variety of users with varying scientific (and
development) backgrounds can understand it.

In this description, it's useful to let users know how your package fits within
the broader scientific Python package ecosystem. If there are other similar packages
or complementary package mentions them here in 1-2 sentences.

```{tip}
Consider writing for a high school level (or equivalent) level. This
level of writing is often considered an appropriate level for scientific content that
serves a variety of users with varying backgrounds.

The goal of this description is to maximize accessibility of your **README**
file.
```

### ✔️ Installation instructions

Include instructions for installing your package. If you have published
the package on both PyPI and Anaconda.org, be sure to include instructions for both.

### ✔️ Document any additional setup required

Add any additional setup required such as authentication tokens, to
get started using your package. If setup is complex, consider linking to an
installation page in your online documentation here rather than over complicating
your README file.

### ✔️ Brief demonstration of how to use the package

This description ideally includes a brief, quick start code
example that shows a user how to get started using your package.

### ✔️ Descriptive links to package documentation, short tutorials

Include descriptive links to:

* The package's documentation page.
* Short tutorials that demonstrate application of your package.

```{admonition} Too Much Of A Good Thing
:class: tip

Try to avoid including several tutorials in the README.md file itself. This too will overwhelm the user with information.

A short quick-start code example that shows someone how to use your package
is plenty of content for the README file. All other tutorials and
documentation
should be presented as descriptive links.
```

### ✔️ A Community Section with Links to Contributing Guide, Code of Conduct

Use your README.md file to direct users to more information on:

* Contributing to your package
* Development setup for more advanced technical contributors
* Your code of conduct
* Licensing information

All of the above files are important for building community around your
project.

### ✔️ Citation information

Finally be sure to include instructions on how to cite your package.
Citation should include the DOI that you want used when citing your package,
and any language that you'd like to see associated with the citation.

:::{admonition} README Resources
:class: tip

Below are some resources on creating great README.md files that you
might find helpful.

* [How to Write a Great README - Bane Sullivan](https://github.com/banesullivan/README)
* [Art of README - Kira (@hackergrrl)](https://github.com/hackergrrl/art-of-readme)

:::
