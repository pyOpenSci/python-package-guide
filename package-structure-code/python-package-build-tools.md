# Python Package Build Tools

Below, we discuss some of the tools that are commonly used
to build Python packages. This page is intended to help
maintainers select a build tool to use.


<!--
Where i'm leaving off here

* setuptools is the OG clearly a lot of ppl use it. but the code base seems
really messy and it's built on top of disutils that may be sunsetted i python 3.12 ?? so does it make sense for us all to use it or should we consider
an example using hatch which seems really nice. extensible and has vcs built
in as far as i can tell


Below talk about each tool and the potential drawbacks.
post on slack about setuptools (next week) and also maybe discord.

I think this page should be it's own separate PR as i really want eyes on it.
So more eyes == better.
I can then have another Pr that has package structure...

setuptools vs hatch

-->

## Python package distribution files

Before we dive into specific build tools, it's important
to review the pieces of a "built" Python package.

### Build
To understand the two distributions below, it is important to understand two different types of files:

**Source files:** source files are the unbuilt files needed to build your package. An example of a build step would be compiling uncompiled code.
**Binary files:** binary files are the files needed to install your package. These files are pre-build. As such any code that need to be compiled has been compiled / built in a binary distribution.

There are two types of distribution files that you will create to support
publishing your Python package (on PyPI):

1. SDist and
1. Wheel

<!--
* **SDist (Source Distribution):** This file, packaged as a **.tar.gz** tarball represents all of the unbuilt source files needed to build your package into an installable bundle. But the files within the package are not yet "built" if your package requires a  build step. Pure python packages most often do not require a build step.
* **Wheel:** A wheel (**.whl**) is a **.zip** file containing all of the files needed to directly install your package. All of the files in a wheel are binaries - this means that code is already compiled / built. Wheels are thus faster to install - particularly if you have a package that requires build steps. -->

```{note}
If your package is a pure python package with no additional
build / compilation steps then the SDIST and Wheel files will have the same content.
```
<!-- TODO: add an example of the contents from SDIST vs .whl -->


### What is a SDist file?

SDist, short for **S**ource **D**istribution file is a packaged file in `.tar.gz`
format (often called a "tarball") that has all of the files needed to build your
package. In the SDist format, your package's files are not included in a built
format. Thus, anyone using this file, will have to build the files first before
they can be installed.

```{tip}
When you make a release on GitHub, it creates a SDist file (`.tar.gz`) that
anyone can download and use.
```

<!--
* one of the benefits of wheel is pretty much avoiding setup.py which
has code mixed in. makes you more vulnerable to a code injection on install.

assuming this means if the package is already pre-built than setup.py isn't running anything on install because install is just moving files across to the machine to be run.

And having metadata separate allows someone to view the metadata without
running any python code as it's a machine and human readable format.

https://scikit-hep.org/developer/pep621
-->

### Wheel (.whl files):

A wheel or `.whl` file, is a zipped file that has
the extension `.whl`. The wheel does not contain any of your packages
configuration files such as **setup.cfg** or **pyproject.toml**. This distribution
is a pre-build, ready-to-install format.

Because it is prebuilt, the wheel file will be faster to install for pure Python
projects and can lead to consistent installs across machines.

```{tip}
Wheels are also useful in the case that a package
needs a **setup.py** file to support a more complex built.
In this case, because the files in the wheel bundle
are pre built, the user installing doesn't have to
work about malicious code injections when it is installed.
```

[Read more about the wheel format here](https://pythonwheels.com/)

## Tools to build python packages

There are a suite of build tools that you can use to create your Python package's **SDist** and *Wheel* distributions.
To better understand your options, it's important to first understand the difference between a
build tool front-end and build backend.

<!-- From stefan: build, run tests on built version, load the built version into Python (?how is this different from install??), make editable install, build wheel, build sdist -->

Below, we discuss some of the commonly-used tools for
building Python packages. This page is intended to help
maintainers select a build tool to use.

This page will focus on pure-python builds. We will add additional resources for
more complex packaging needs in the future.

## Tools to build python packages

There are several different build tools that you can use to [create your Python
package's **SDist** and **Wheel** distributions](python-package-distribution-files-sdist-wheel).
To better understand your options, it's important to first understand the
difference between a
build tool front-end and build back-end.

<<<<<<< HEAD
### Build back-ends
Every tool has a back-end
build tool that actually builds the package and creates associated (SDist and wheel) distribution
files. Some of the tools below such as Flit and pdm only
support straight forward builds that do not have a compilation or other additional build step. These
types of tools are ideal if you have a pure python
project.

Other tools such as Hatch/ hatchling and setuptools
support more complex builds with custom steps.

### Build front-ends
Each tool discussed below has a front-end interface that you can use to
perform different types of Python packaging tasks.
For instance,
you can use **Flit** to both build your package and
to publish your package
to PyPI (or test PyPI).

Using a tool like **Flit** makes your workflow commands consistent and simple. For example, rather than using `twine` to publish your package to PyPi, you use `flit publish` (see below).

Example to build your package with Flit:
<!--TODO Add examples of builds using each of the tools below? -->

Below, we discuss some of the tools that are commonly used
to build Python packages. This page is intended to help
maintainers select a build tool to use.

## Tools to build python packages

There are several different build tools that you can use to create your Python
package's **SDist** and **Wheel** distributions.
To better understand your options, it's important to first understand the
difference between a
build tool front-end and build backend.

## Build front-end vs. build backend tools for Python packaging

### Build back-ends
Most packaging tools have a back-end
build tool that builds the package and creates associated
(SDist and wheel) distribution files. Some tools, such as **Flit**
and **Hatch**, only support pure-Python package builds. A pure-Python build refers
to a package build that does not have extensions that are written in another
programming language (such as `C` or `C++`). These non-pure Python builds often
have additional code compilation steps.

```{note}
**PDM** does have some support for `C`/[`Cython`](https://cython.org/) extensions. [Click here to
learn more.](https://pdm.fming.dev/latest/pyproject/build/#build-platform-specific-wheels
)
```

There are, however back-ends such as and **setuptools.build**, **meson.build**
and **scikit-build** that support complex builds with custom steps. If your
build is particularly complex (ie you have more than a few `C`/`C++`
extensions), we suggest you consider using **meson.build** or **scikit-build**.

### Build front-ends
Each tool discussed below has a front-end interface that you can use to perform
different types of Python packaging tasks.

For instance, you can use **Flit**, **Hatch** and **PDM** to both build your
package and to publish your package to PyPI (or test PyPI). Setuptools,
on the other hand requires you to use **twine** to push to PyPI.

Using a tool like **Flit**, **Hatch** or **PDM** will simplify your workflow.

Example to build your package with **Flit**:
>>>>>>> 9ba0e17 (Add: content about sdist and wheel and break out to new page)

`flit build`

Example to publish to PyPI:
`flit publish --repository testpypi`

In the Pytyhon package build space **setuptools** is
the "OG" -the original tool that everyone used to use.
With a tool like  `setuptools` you have the flexibility
to publish python pure python packages and packages with custom build steps. However, you will also need to use other tools. For example, you will use `twine` to publish to PyPI.

## An ecosystem of Python build tools

Below we introduce several of the most commonly used
Python packaging build  tools. Each tool has various
features that might make you chose to use it
or not use it. There is no right or wrong tool to use
as far as pyOpenSci is concerned. We are just trying to
help you find the tool that works best for
your workflow.
Example build steps using setuptools:
=======
## Build front-end vs. build back-end tools for Python packaging

### Python package build front-ends

A packaging front-end tool refers to a tool that makes it easier for you to
perform common packaging tasks using similar commands, such as:

* [Creating a Sdist and Wheel distribution](python-package-distribution-files-sdist-wheel)
* Managing an environment or multiple environments in which you need to run tests and develop your package
* Building documentation
* Installing your package in a development mode (so it updates when you update your code)
* Publishing to PyPI

There are several Python packaging tools that you can use for pure Python
builds. Each tool
offers different sets of functionality to support your build.

For instance, you can use the packaging tools **Flit**, **Hatch** or **PDM**
to both build and publish your package to PyPI.
**Setuptools** on the other hand is a build back end tool. You will need
to use **twine** to publish to PyPI if you use setuptools.

If you are just getting started with packaging, then using a tool like **Flit**,
**Hatch** or **PDM** will simplify your workflow.

### Example build steps that can be simplified using a front-end tool

Example to build your package with **Hatch**:

```bash
# Build your sDist and .whl files
hatch build

# Example to publish to PyPI:
hatch publish --repository testpypi
```
Example build steps using **setuptools** and **build**:
>>>>>>> 09e4d0d (Fix: ingest comments to update build tools page focused on python)

```bash
# Build the package
python3 -m build
# Check build
twine check dist/*
# Publish to test PyPI
twine upload -r testpypi dist/*
```

However each tool has different features and limits on the types of packaging
steps that it supports.
```{admonition} Pure Python Packages vs. packages with extensions in other languages

You can classify Python package complexity into three general categories. These
categories can in turn help you select the correct package front-end and
back end tools.

1.  **Pure-python packages:** these are packages that only rely on Python to function. Building a pure Python package is simpler. As such, you can chose a tool below that
has the features that you want and be done with your decision!
2.  **Python packages with non-Python extensions:** These packages have additional components called extensions written in other languages (such as `C` or `C++`). If you have a package with non-python extensions, then you need to select a build back-end tool that allows you to add additional build steps needed to compile your extension code. Further, if you wish to use a front-end tool to support your workflow, you will need to select a tool that
supports additional build setps. In this case, you could use setuptools. However, we suggest that you chose build tool that supports custom build steps such as Hatch with Hatchling or PDM. PDM is an excellent choice as it allows you to also select your build back end of choice. We will discuss this at a high level on the complex builds page.
3. **Python packages that have extensions written in different languages (e.g. fortran and C++) or that have non Python dependencies that are difficult to install (e.g. GDAL)** These packages often have complex build steps (more complex than a package with just a few C extensions for instance). As such, these packages require tools such as [scikit-build](https://scikit-build.readthedocs.io/en/latest/)
or [meson-python](https://mesonbuild.com/Python-module.html) to build. NOTE: you can use meson-python with PDM.

On this page, we will focus on using front-end tools to package pure python
packages. We will note if a package does have the flexibility to support other
back-ends and in turn more complex builds (*mentioned in #2 and #3 above*).
[If you are interested in tool support for non pure python builds, check out this
page for resources.](complex-python-packaging-builds)
```

### Build back-ends

Most front-end packaging tools have their own back-end build tool. The build
tool creates your package's (SDist and Wheel) distribution files. For pure
Python packages, the main difference between the different build back-ends
discussed below is:

* How configurable they are and
* How much you need to configure them to ensure the correct files are included in your SDist and Wheel files.

It is also important to note that some back-ends, such as Flit-core, only support
pure Python builds. Other back ends support C and C++ extensions:

* setuptools supports builds using C / C++ extensions
* Hatchling supports C extensions via plugins that the developer creates to customize a build
* PDM-pep517 supports C extensions by using setuptools
* Poetry supports C/C++ extensions however this functionality is currently undocmented. As such we don't recommend exploring it now for non pure Python builds.

While we won't discuss more complex builds below, we will identify which tools
allow for C and C++ extensions as we discuss each tool below.


<!--
From Eli:

poetry: supports it (c extensions), but is undocumented and uses setuptools under the hood, they plan to change how this works and then document it
pdm-backend: supports it, and documents it -- and also uses setuptools under the hood
hatchling: permits you to define hooks for you to write your own custom build steps, including to build C++ extensions

-->

<!-- ```{note}
**PDM** does have some support for `C`/[`Cython`](https://cython.org/) extensions. [Click here to
learn more.](https://pdm.fming.dev/latest/pyproject/build/#build-platform-specific-wheels). This functionality uses setuptools "under the
hood".
``` -->


Below we describe the broader ecosystem of Python package build tools.
We also highlight the benefits and potential limitations presented by each tool.

## An ecosystem of Python build tools

Below we introduce several of the most commonly used Python packaging build
tools (see chart below).

:::{figure-md} fig-target

<img src="../images/python-package-tools-2022-survey-pypa.png" alt="Graph showing the results of the 2022 PyPA survey of Python packaging tools. On the x axis is percent response and on the y axis are the tools." width="700px">

The Python developers survey results (n=>8,000 PyPI users) show setuptools and poetry as the most commonly used Python packaging tools. The core tools that we've seen being used in the scientific community are included here. [You can view the full survey results by clicking here.](https://drive.google.com/file/d/1U5d5SiXLVkzDpS0i1dJIA4Hu5Qg704T9/view) NOTE: this data represent maintainers across domains and is likely heavily represented by those in web development. So this represents a snapshot across the broader Python ecosystem.
:::


## How to chose a build workflow tool

The tools that we review below include:

* setuptools + twine, build
* Flit
* Hatch
* PDM
* Poetry

We suggest that you pick one of the modern tools listed above rather than
setuptools because setuptools will require some additional knowledge
to set up correctly.


<!-- TODO: create build tool selection diagram -->

<!-- ### Build tools for Python packages with complex build steps
If your package is not pure Python, or it has complex build steps (or build
steps that you need to customize), then you should consider using:

* Setuptools
* Hatch
* PDM

These tools allow you to customize your workflow with build steps needed
to compile code. -->

[We will discuss non pure python builds here.](complex-python-packaging-builds)

## Python packaging tools summary
<!-- NOTE - add language around the front end means that you have less individual tools in your build - such as nox / make with hatch -->
*Table to BE UPDATED!!*
Below, we summarize features offered by the most popular build front end tools.
Note that because setuptools does not offer a front-end interface, it is not
included in the table.


<!-- to add
* pins dependencies (poetry and pdm)
* what else?
-->

| Feature                                                                | Setuptools            | Flit      | Hatch     | PDM |
| ---------------------------------------------------------------------- | --------------------- | --------- | --------- | --- |
| Build backend                                                          | setuptools.build_meta | flit_core | hatchling |  pdm-pep517   |
| Supports projects that aren't pure python                              | yes                   | no        | yes       | no  |
| Supports custom build steps (before creating wheel)                    | yes                   | no        | yes       | no  |
| Has built in dependency management                                     | no                    | no        | no (future feature)       | yes |
| Can be used to publish directly to pypi                                | no (use twine)        | yes       | yes       | yes |
| Has version control based (eg git based) tooling to bump version       | setuptools_scm        | no        | hatch-vcs | ?   |
| Supports automated GitHub only releases (no local command line needed) | yes                   | no        | yes       |     |


## PDM


[PDM is a Python packaging and dependency management tool](https://pdm.fming.dev/latest/).
PDM supports builds for pure Python projects but also provides some support for
projects that have some C and C++ extensions.

```{admonition} PDM support for C and C++ extensions
PDM supports using the PDM-backend and setuptools at the same time.
This means that you can run setuptools to compile and build C extensions. PDM's build backend receives the compiled extension files (.so, .pyd) and packages them with the pure Python files.
```

### PDM Features

PDM:
* Offers dependency management and pinning that follows community best practices
* Follows modern packaging standards.
* Supports using other build backends and associated backend plugins (such as flit-core, and hatchling)
* Allows you to select your environment manager of choice (conda, venv, etc)
* Provides support for both version bumping (similar to bumpversion) and version control based versioning

The functionality of PDM is similar to Poetry. However, it also offers
additional, documented support for C extensions and version control based versioning.

### Challenges with PDM

PDM is a full-featured packaging tool. However it is not without challenges:

* its documentation can be confusing, especially if you are new to
packaging.
* PDM doesn't provide an end to end beginning workflow in its documentation.
* PDM also only has one maintainer currently. We consider individual maintainer teams
to be a risk as if a maintainer needs to step down, it could impact the user
community.

[You can view an example of a package that uses PDM here.](https://github.com/pyOpenSci/examplePy/tree/main/example4_pdm). The readme for this directly provides you with
an overview of what the PDM command line interface looks like when you use it.


## Flit

[Flit is a no-frills, streamlined packaging tool](https://flit.pypa.io/en/stable/) that supports modern Python packaging standards.

If you have a pure Python project and don't need:

* Any additional build steps for your package,
* Support for dependency version pinning
* support for version "bumping"

Flit could be the tool for you. Flit is also a great choice if you are
building a basic package to use in a local workflow.

### Flit Features

Flit can:

* Help you setup your **pyproject.tom**l metadata
* Build your SDist and wheel distributions
* Publish to testPyPI and PyPI
* Install your package

```{admonition} Learn more about flit
* [Why use flit?](https://flit.pypa.io/en/stable/rationale.html)
```

### Challenges with Flit:

Flit does not offer:
* Version Support: Flit uses the version from your package's ` __version__`.
* Dependency Pinning
* Environment support

Because Flit is no frills, it is best for basic, quick builds. If you are a
beginner you may want to select Hatch or PDM which will offer you more support
in common operations.


### Why you might not want to use Flit
You may NOT want to use flit if:

* You want to setup more advanced version tracking and management (using version control of version bumping)
* You want a tool that handles dependency versions (use PDM instead)
* You have a project that is not pure Python (Use Hatch, PDM or setuptools)

## Hatch

[**Hatch**](https://hatch.pypa.io/latest/), similar to Poetry and PDM, provides a
unified command line interface. To separate Hatch from Poetry and PDM, it also
provides an environment manager for testing that will  make it easier for
you to run tests locally across different versions of Python. It also offers a
nox / makefile like feature that allows you to create custom build workflows such
as building your documentation locally, that you may have created in the past
using a tool like **Make** or **Nox**.

### Hatch features

Hatch features include:

* Version control based versioning using **hatch-vcs**. (If you are familiar with setuptools_scm hatch wraps around that tool.)
* Publish to PyPI
* Build your package SDist and Wheel locally.
* Create an environment and install your package in development mode
* Matrix environment creation to support testing across Python versions
* [Nox / MAKEFILE like functionality](https://hatch.pypa.io/latest/environment/#selection)
where you can create workflows in the **pyproject.toml** configuration to do things
like serve docs locally and clean your package build directory. This means you may have one less tool in your build workflow

<!-- QUESTION: Does hatch allow you to use other envt managers like conda?? i don't see that it does
so it might be similar to Poetry in that regard -->

### Advanced features:
* A flexible build backend, **hatchling**, that allows developers to add plugins that can be used to customize a build.


### Challenges with Hatch

There are a few features that hatch is missing that may be important for some.
These include:

Hatch:
* Doesn't support dependency "pinning" and management
* Currently doesn't support use with other build back ends. Lack of support for other build back ends makes Hatch less desirable for users with more complex package builds. If your package is pure
Python, this won't be an issue.
* Doesn't allow you to select what environment manager you use. <!-- (is this right??) -->
* Hatch doesn't provide an end to end beginning workflow in it's documentation.
* Hatch, similar to PDM and Flit currently only has one maintainer.

```{note}
While Hatch does have some "opinions" about how parts of the packaging build
run, you can customize any aspect of its build.
```

## Poetry

[Poetry is a full-featured build tool.](https://python-poetry.org/) It is also
the second most popular front-end packaging tool (based upon the PyPA survey).
Poetry is user-friendly and has clean and easy-to-read documentation.

While some have used Poetry for Python builds with C/C++ extensions, this support
is currently undocumented. Thus we don't recommend it for more complex builds.


### Poetry features

* Publish to PyPi and Test PyPI
* Builds your package's SDist and Wheel distribution files
* Version bumping at the command line
* Poetry offers dependency "pinning" however it does so in a way that can be problematic - read below for more
* [Built in environment management with options](https://python-poetry.org/docs/basic-usage/#using-your-virtual-environment) to either use your own environment or to create an environment in your local directory <!-- will it recognize a conda envt?? -->
* Offers support for [both a src/ and flat layout](python-package-structure.md)
* Installs you package in editable mode (using `--editable`)
* Allows you to organize dependencies in groups: docs, package, tests etc


### Challenges with Poetry

There are some features that Hatch and PDM offer that Poetry does not.

Hatch: offers matrix environment management that allows you to run tests across
Python versions. It also offers a Nox / Make file like tool to streamline your
build workflow.
PDM: does not offer matrix environments of Nox / Makefile like tools. It does
offer dependency management but adheres to a >= approach when pinning. This
avoids the issue described below with Poetry's upper bound pinning.



Some challenges of poetry include:

* Poetry pins dependencies using an "upper bound" limit specified with the `^` symbol. See breakout below for more regarding why this is potentially problematic.
* Doesn't support version control based versioning
* *Minor:* The way Poetry currently adds metadata to your pyproject.toml file does not does not follow current Python standards. However, this is going to be addressed when they release version 2.0.

Poetry is an excellent tool. Use caution when pinning dependencies as
Poetry's approach to pinning has been showing to be problematic for many builds.

```{admonition} Challenges with Poetry dependency pinning
:class: important

Poetry pins dependencies using `^`. This `^` symbol means that there is
an "upper bound" to the dependency. Thus poetry will bump a dependency
version to a new major version. Thus, if your package uses a dependency that
is at version 1.2.3, Poetry will never bump the dependency to 2.0 even if
there is a new major version of the package. Poetry will instead bump up to 1.9.x.

Poetry does this because it adheres to strict sesmantic versioning which stats
that a major version bump (from 1.0 to 2.0 for example) means there are breaking
changes in the tool. however, not all tools follow strict semantic versioning.
[This approach has been found to be problematic by many of our core scientific packages.](https://iscinumpy.dev/post/bound-version-constraints/)

This approach also won't support over ways of versioning tools, for instance,
some tools use [calver](https://calver.org/) which creates new versions based on the date.
```

<!--todo: look at eli's comments about this-->


<!--
The example below is taken from [this thread in GitHub](https://github.com/py-pkgs/py-pkgs/issues/95#issuecomment-1035584750).

```toml
[tool.poetry.dependencies]
python = ">=3.6" # This is muddled in as a dependency, while it's not like the others
numpy = ">=1.13.3"
typing_extensions = { version = ">=3.7", python = "<3.8" }

sphinx = {version = "^4.0", optional = true}
sphinx_book_theme = { version = ">=0.0.40", optional = true }
sphinx_copybutton = { version = ">=0.3.1", optional = true }
pytest = { version = ">=6", optional = true }
importlib_metadata = { version = ">=1.0", optional = true, python = "<3.8" } # TOML error to add an ending comma or new line, even if this gets long
boost-histogram = { version = ">=1.0", optional = true }

[tool.poetry.dev-dependencies]
pytest = ">=5.2"  # All the optional stuff above doesn't help here!
importlib_metadata = {version = ">=1.0", python = "<3.8" }
boost_histogram = ">=1.0"

[tool.poetry.extras]
docs = ["sphinx", "sphinx_book_theme", "sphinx_copybutton"]
test = ["pytest", "importlib_metadata", "boost_histogram" ]
```

vs PDM

```toml
[project]
requires-python = ">=3.6"
dependencies = [
  "numpy>=1.13.3",
  "typing-extensions>=3.7; python_version<'3.8'",
]

# Only needed for extras
[project.optional-dependencies]
docs = [
  "sphinx>=4.0",
  "sphinx-book-theme>=0.0.40",
  "sphinx-copybutton>=0.3.1",
]
test = [
  "pytest>=6",
  "importlib-metadata>=1.0; python_version<'3.8'",
  "boost-histogram>=1.0",
]

# Only needed for "dev" installs
[tool.pdm.dev-dependencies]
dev = [
  "pytest>=6",
  "importlib-metadata>=1.0; python_version<'3.8'",
  "boost-histogram>=1.0",
]
```
-->

## Using Setuptools Back-end for Python Packaging

[Setuptools](https://setuptools.pypa.io/en/latest/) is the most
mature Python packaging build tool with [development dating back to 2009 and earlier](https://setuptools.pypa.io/en/latest/history.html#).
Setuptools also has the largest number of users. Setuptools does not offer a user
front-end like Flit, Poetry and Hatch offer. As such you will need to use other
tools such as **build** to create
your package distributions and **twine** to publish to PyPI.

While setuptools is the most commonly used tool, we encourage package maintainers
to consider using a more modern tool for packaging such as Hatch or PDM.

We discuss setuptools here because it's commonly found in the ecosystem and
contributors may benefit from understanding it.

### Potential benefits of setuptools

Some of features of setuptools include:

* Fully customizable build workflow
* Many scientific Python focused packages use it.
* If offers version control based package versioning using **setuptools_scm**
* Supports modern packaging using **pyproject.toml** for metadata
* Supports backwards compatibly for older packaging approaches.

### Challenges using setuptools

Setuptools has a few challenges:

* Because **setuptools** has to maintain backwards compatibility across a range of packages, it is
not as flexible in its adoption of modern Python packaging
standards.
* The above-mentioned backwards compatibility makes for a more complex code-base.
* Your experience as a user will be less streamlined and simple using setuptools compared to other tools discussed on this page.

There are also some problematic default settings that users should be aware of
when using setuptools. For instance,

* setuptools will build a
project without a name or version if you are not using a **pyproject.toml** file
to store metadata.
*Setuptools also will include all of the files in your package
repository if you do not explicitly tell it to exclude files using a
**MANIFEST.in** file
