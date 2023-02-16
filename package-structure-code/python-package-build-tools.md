# Python Package Build Tools

There are a suite of build tools that you can use to [create your Python package's **SDist** and *Wheel* distributions](python-package-distribution-files-sdist-wheel). Below, we discuss the features,
benefits and limitations of the most commonly used Python packaging tools.
We focus on pure-python packages in this guide. However, we also
highlight tools that currently support packages with C/C++ and other language
extensions.


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
page for resources.](complex-python-package-builds)
```

## Build front-end vs. build back-end tools

To better understand your options, when it comes to building a Python package, it's important to first understand the difference between a
build tool front-end and build back-end.

### Build back-ends
Most packaging tools have a back-end
build tool that builds you package and creates associated
[(SDist and wheel) distribution files](python-package-distribution-files-sdist-wheel). Some tools, such as **Flit**, only
support pure-Python package builds. A pure-Python build refers
to a package build that does not have extensions that are written in another
programming language (such as `C` or `C++`).

```{note}
**PDM** does have some support for `C`/[`Cython`](https://cython.org/) extensions. [Click here to
learn more.](https://pdm.fming.dev/latest/pyproject/build/#build-platform-specific-wheels
)
```

Other packages that have C and C++ extensions (or that wrap other languages such as fortran) require additional code compilation steps when built.
Back-ends such as and **setuptools.build**, **meson.build**
and **scikit-build** support complex builds with custom steps. If your
build is particularly complex (i.e. you have more than a few `C`/`C++`
extensions), then we suggest you use **meson.build** or **scikit-build**.
<!--
### Build front-ends

Build front-ends have a user-friendly interface that allow you to perform
common Python packaging tasks such as building your package, creating an
environment to run package tests and build documentation, and pushing to PyPI.



For instance, you can use **Flit**, **Hatch** and **PDM** to both build your
package and to publish your package to PyPI (or test PyPI). However, if you
want a tool that also support environment management and versioning your package,
then you might prefer to use **Hatch** or **PDM**.

Using a tool like **Flit**, **Hatch** or **PDM** will simplify your workflow.

Example to build your package with **Flit**:

`flit build`

Example to publish to PyPI:
`flit publish --repository testpypi`

In the Python package build space **setuptools** is
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
======= -->

### Python package build front-ends

A packaging front-end tool refers to a tool that makes it easier for you to
perform common packaging tasks using similar commands. These tasks include:

* [Creating a Sdist and Wheel distribution](python-package-distribution-files-sdist-wheel)
* Managing an environment or multiple environments in which you need to run tests and develop your package
* Building documentation
* Installing your package in a development mode (so it updates when you update your code)
* Running tests
* Publishing to PyPI

There are several Python packaging tools that you can use for pure Python
builds. Each front-end tool discussed below supports a slightly different set of Python
packaging tasks.

For instance, you can use the packaging tools **Flit**, **Hatch** or **PDM**
to both build and publish your package to PyPI. However while  **Hatch** and
**PDM** support versioning and environment management, **Flit** does not. If you want a tool that supports dependency
locking, you can use **PDM** or **Poetry** but not **Hatch**.

```{note}
If you are using **Setuptools**, there is no user-friendly build front-end that performs multiple tasks. You will need to use **build** to build your package and **twine** to publish to PyPI.
```


### Example build steps that can be simplified using a front-end tool

Below, you can see how a build tool streamlines your packaging experience. Example to build your package with **Hatch**:

```bash
# Build your sDist and .whl files
hatch build

# Example to publish to PyPI:
hatch publish --repository testpypi
```
Example build steps using **setuptools** and **build**:

```bash
# Build the package
python3 -m build

# Publish to test PyPI
twine upload -r testpypi dist/*
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
* PDM's backend supports C / C++ extensions by using setuptools
* Poetry supports C/C++ extensions however this functionality is currently undocumented. As such we don't recommend using Poetry for complex builds until it is documented.

While we won't discuss more complex builds below, we will identify which tools
allow for C and C++ extensions.


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

When you are selecting a tool, you might consider this general workflow of
questions:

1. **Is your tool pure python? Yes?** You can use any tool that you wish! Pick the tool that has the features that you want to use in your build workflow. We suggest:
* flit, hatch, PDM or poetry (read below for more)
1. **Does your tool have a few C or C++ extensions?** Great, we suggest using
**PDM** for the time being. It is the only tool in the list below that has documented
workflow to support such extensions. It also supports other backends such as scikit build and meson-python that will allow you to fully customize your build.

NOTE: You can also use Hatch but you will need to write your own plugin for this support.


<!-- TODO: create build tool selection diagram - https://www.canva.com/design/DAFawXrierc/O7DTnqW5fmMEZ31ao-TK9w/edit -->


:::{figure-md} fig-target

<img src="../images/python-package-tools-decision-tree.png" alt="ADD ME." width="700px">

ADD ME
:::

<!-- ### Build tools for Python packages with complex build steps
If your package is not pure Python, or it has complex build steps (or build
steps that you need to customize), then you should consider using:

* Setuptools
* Hatch
* PDM

These tools allow you to customize your workflow with build steps needed
to compile code. -->

## Python packaging tools summary
<!-- NOTE - add language around the front end means that you have less individual tools in your build - such as nox / make with hatch -->


Below, we summarize features offered by the most popular build front end tools.
Note that because setuptools does not offer a front-end interface, it is not
included in the table.


### Package tool features table

```{csv-table}
:header: Feature, Flit, Hatch, PDM, Poetry
:widths: 36, 10,10,10,10

Default Build Back-end, Flit-core, Hatch-core, PDM, Poetry
Use Other Build Backends,✖ , ✖,✅  ,✖
Dependency management, ✖,✖,✅,✅
Publish to PyPI, ✅,✅,✅,✅
Version Control based versioning (using `git tags`),✖,✅,✅,✖
Version bumping,✖,✅, ✅, ✅
More than One maintainer?,✖,✖, ✖, ✅
```

Notes:
* *Hatch plans to support using other backends and dependency management in the future*
* Poetry supports semantic versioning. Thus, it will support version bumping following commit messages if you use a tool such as Python Semantic Release

## PDM

[PDM is a Python packaging and dependency management tool](https://pdm.fming.dev/latest/).
PDM supports builds for pure Python projects. It also provides multiple layers of
support for projects that have C and C++ extensions.

```{admonition} PDM support for C and C++ extensions

PDM supports using the PDM-backend and setuptools at the same time.
This means that you can run setuptools to compile and build C extensions. PDM's build backend receives the compiled extension files (.so, .pyd) and packages them with the pure Python files.
```

### PDM Features

```{csv-table}
:header: Feature, PDM, Notes
:widths: 20,5,50

Use Other Build Backends, ✅, When you setup PDM it allows you to select from Hatch; PDM-517 and PDM-core build tools. PDM also can work with Meson-Python which supports move complex python builds.
Dependency management & lock files ,✅,PDM and Poetry are currently the only tools that support creating dependency lock files. However their approach to locking files is different: Poetry uses an upper bound lock approach `^`. <!--Most users won't know what upper bound means--> PDM uses an open lock `>=` Lock files might be most useful to developers creating web apps where locking the environment is critical for consistent user experience.
Select your environment manager of choice (conda; venv; etc),✅ , PDM allows you to select the environment manager that you want to use for managing your package.
Publish to PyPI,✅,PDM supports publishing to both test PyPI and PyPI
Version Control based versioning,✅ , PDM has a setuptools_scm like tool built into it's package which allows you to use dynamic versioning that rely on git tags.
Version bumping, ✅ , PDM supports you bumping the version of your package using standard semantic version terms patch; minor; major
Follows current packaging standards,✅,PDM supports current packaging standards for adding metadata to the **pyproject.toml** file. It also supports pep 517? dependency management which relies upon a local directory containing a users environment.
Install your package in editable mode,✅,PDM supports installing your package in editable mode. **TODO: add info - does it support this and what does that look like? i think it does it when you create an envt??**
Build your SDist and wheel distributions,✅,
```

```{admonition} PDM vs. Poetry
The functionality of PDM is similar to Poetry. However, PDM also offers
additional, documented support for C extensions and version control based
versioning. If you are deciding between the two tools, the main difference between these two tools
is that Poetry follows strict semantic versioning. Strict adherence to semantic
versioning can be problematic in some cases (more on that below).
```

### Challenges with PDM

PDM is a full-featured packaging tool. However it is not without challenges:

* Its documentation can be confusing, especially if you are new to
packaging. For example, PDM doesn't provide an end to end beginning workflow in its documentation.
* PDM also only has one maintainer currently. We consider individual maintainer
teams to be a potential risk. If the maintainer finds they no longer have time
to work on the project, it leaves users with a gap in support. Hatch and Flit
also have single maintainer teams.

[You can view an example of a package that uses PDM here](https://github.com/pyOpenSci/examplePy/tree/main/example4_pdm). The README file for this directly provides you with
an overview of what the PDM command line interface looks like when you use it.


## Flit

[Flit is a no-frills, streamlined packaging tool](https://flit.pypa.io/en/stable/) that supports modern Python packaging standards.
Flit is a great choice if you are
building a basic package to use in a local workflow that doesn't require any advanced features. More on that below.

### Flit Features

```{csv-table}
:header: Feature, Flit, Notes
:widths: 20,5,50

Publish to PyPI and test PyPI,✅,Flit supports publishing to both test PyPI and PyPI
Helps you add metadata to your pyproject.toml file,✅,
Follows current packaging standards,✅,Flit supports current packaging standards for adding metadata to the **pyproject.toml** file.
Install your package in editable mode,✅,Flit supports installing your package in editable mode. However it does use a slightly different syntax from the usual `pip install -e .` to do so.
Build your SDist and wheel distributions,✅,
```

```{admonition} Learn more about flit
* [Why use flit?](https://flit.pypa.io/en/stable/rationale.html)
```

### Why you might not want to use Flit

Because Flit is no frills, it is best for basic, quick builds. If you are a
beginner you may want to select Hatch or PDM which will offer you more support
in common operations.
You may NOT want to use flit if:

* You want to setup more advanced version tracking and management (using version control for version bumping)
* You want a tool that handles dependency versions (use PDM instead)
* You have a project that is not pure Python (Use Hatch, PDM or setuptools)
* Version Support: Flit uses the version from your package's ` __version__`.

## Hatch

[**Hatch**](https://hatch.pypa.io/latest/), similar to Poetry and PDM, provides a
unified command line interface. To separate Hatch from Poetry and PDM, it also
provides an environment manager for testing that will  make it easier for
you to run tests locally across different versions of Python. It also offers a
nox / makefile like feature that allows you to create custom build workflows such
as building your documentation locally, that you may have created in the past
using a tool like **Make** or **Nox**.

### Hatch features

```{csv-table}
:header: Feature, PDM, Notes
:widths: 20,5,50

Use Other Build Backends,✖, Switching out build back ends is not currently an option when using Hatch. However this feature is coming to the package in the near future.
Dependency management,✅,Hatch can help you add dependencies to your `pyproject.toml` metadata.
**??does hatch support this - i forget?** Select your environment manager of choice (conda; venv; etc),✅ , Hatch allows you to select the environment manager that you want to use for managing your package.
Publish to PyPI and test PyPI,✅,Hatch supports publishing to both test PyPI and PyPI
Version Control based versioning,✅ , Hatch offers hatch_vcs which is a plugin that uses setuptools_scm to support versioning using git tags. The workflow with hatch_vcs is the same as that with setuptools_scm.
Version bumping, ✅ , Hatch supports you bumping the version of your package using standard semantic version terms patch; minor; major
Follows current packaging standards,✅,Hatch supports current packaging standards for adding metadata to the **pyproject.toml** file.
Install your package in editable mode,✅,Hatch supports installing your package in editable mode. **TODO: add info - does it support this and what does that look like? i think it does it when you create an envt??**
Build your SDist and wheel distributions,✅,
✨Matrix environment creation to support testing across Python versions✨,✅, The matrix environment creation is a feature that is unique to Hatch in the packaging ecosystem. This feature is useful if you wish to test your package locally across P ython versions (instead of using a tool such as tox).
✨[Nox / MAKEFILE like functionality](https://hatch.pypa.io/latest/environment/#selection)✨, ✅, This feature is also unique to Hatch. This functionality allows you to create workflows in the **pyproject.toml** configuration to do things like serve docs locally and clean your package build directory. This means you may have one less tool in your build workflow.
✨A flexible build backend, **hatchling**✨, ✅, **The hatchling build back-end offered by the maintainer of Hatch allows developers to easily build plugins to support custom build steps when packaging.
```

_** There is some argument about this approach placing a burden on maintainers to create a custom build system. But others appreciate the flexibility_

<!-- QUESTION: Does hatch allow you to use other envt managers like conda?? i don't see that it does
so it might be similar to Poetry in that regard -->

### Why you might not want to use Hatch

There are a few features that hatch is missing that may be important for some.
These include:

Hatch:
* Doesn't support dependency "pinning"
* Currently doesn't support use with other build back ends. Lack of support for other build back ends makes Hatch less desirable for users with more complex package builds. If your package is pure
Python, this won't be an issue. NOTE: there is a plan for this feature to be added in the upcoming months.
* Doesn't allow you to select what environment manager you use. <!-- (is this right??) -->
* Hatch doesn't provide an end to end beginning workflow in it's documentation.
* Hatch, similar to PDM and Flit currently only has one maintainer.

```
While Hatch does have some "opinions" about how parts of the packaging build
run, you can customize any aspect of its build using plugins.
```

## Poetry

[Poetry is a full-featured build tool.](https://python-poetry.org/) It is also
the second most popular front-end packaging tool (based upon the PyPA survey).
Poetry is user-friendly and has clean and easy-to-read documentation.

```{note}
While some have used Poetry for Python builds with C/C++ extensions, this support
is currently undocumented. Thus we don't recommend it for more complex builds.
```

### Poetry features

```{csv-table}
:header: Feature, PDM, Notes
:widths: 20,5,50


Dependency management,✅,Poetry helps you add dependencies to your `pyproject.toml` metadata. _NOTE: currently Poetry adds dependencies using an approach that is slightly out of alignment with current Python peps - however there is a plan to fix this in an upcoming release._ Allows you to organize dependencies in groups: docs, package, tests.
Dependency pinning,✖✅ ,Poetry offers dependency "pinning" however it does so in a way that can be problematic - read below for more
Select your environment manager of choice (conda; venv; etc),✅ , Poetry allows you to either use it's simply environment management tool or  select the environment manager that you want to use for managing your package. [Read more about it's built in environment management options](https://python-poetry.org/docs/basic-usage/#using-your-virtual-environment).
Publish to PyPI and test PyPI,✅,Poetry supports publishing to both test PyPI and PyPI
Version Control based versioning,✅ , Hatch offers hatch_vcs which is a plugin that uses setuptools_scm to support versioning using git tags. The workflow with hatch_vcs is the same as that with setuptools_scm.
Version bumping, ✅ , Poetry supports you bumping the version of your package using standard semantic version terms patch; minor; major
Follows current packaging standards,✖✅,Poetry does not quite support current packaging standards for adding metadata to the **pyproject.toml** file but plans to fix this in an upcoming release.
Install your package in editable mode,✅,Poetry supports installing your package in editable mode using `--editable`
Build your SDist and wheel distributions,✅,
```

### Challenges with Poetry

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

```{admonition} where does this belong?
:class: note
There are some features that Hatch and PDM offer that Poetry does not.

Hatch: offers matrix environment management that allows you to run tests across
Python versions. It also offers a Nox / Make file like tool to streamline your
build workflow.
PDM: does not offer matrix environments of Nox / Makefile like tools. It does
offer dependency management but adheres to a >= approach when pinning. This
avoids the issue described below with Poetry's upper bound pinning.
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




<!--
Where i'm leaving off here

* setuptools is the OG clearly a lot of ppl use it. but the code base seems
really messy and it's built on top of distutils that may be sunsetted i python 3.12 ?? so does it make sense for us all to use it or should we consider
an example using hatch which seems really nice. extensible and has vcs built
in as far as i can tell


Below talk about each tool and the potential drawbacks.
post on slack about setuptools (next week) and also maybe discord.

I think this page should be it's own separate PR as i really want eyes on it.
So more eyes == better.
I can then have another Pr that has package structure...

setuptools vs hatch

-->


<!-- From stefan: build, run tests on built version, load the built version into Python (?how is this different from install??), make editable install, build wheel, build sdist -->
