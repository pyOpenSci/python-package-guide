# Make your Python package PyPI ready - pyproject.toml

:::{todo}
- add a note for hatch - if you want to use dynamic versioning you'll need to add `tool.hatch.version` to the pyproject.toml file.
- TODO: decide how we want to list readme and license? it might make sense to just follow the simplest option and do spdx?
- TODO: make sure they add the dev requirements here... including build.
license = { text = "MIT" } that format is a toml inline table https://toml.io/en/v1.0.0#inline-table and it becomes a subtable of the project table

TODO: make sure that the link to our guide is on this page.  [Learn more about this file in our packaging guide.](https://www.pyopensci.org/python-package-guide/package-structure-code/pyproject-toml-python-package-metadata.html)

myst-nb or nbsphinx to run code
:::


In [the installable code lesson](2-installable-code), you learned how to add the bare minimum information to a `pyproject.toml` file to make it `pip` installable. You then learned how to [publish that bare minimum version of your package to PyPI](publish-pypi.md).

To help users find your package on PyPI, and to add more information about the Python versions your support, development status of your project and about who maintainers your project,
you will want to add additional metadata to your `pyproject.toml` file that
describes the use and contents of your package. You will
learn how to do that in this lesson.

In subsequent lessons you will add a license and README file to your package which will further flesh out both your PyPI landing page and the landing page
of your GitHub or GitLab repository.

:::{admonition} Learning Objectives
:class: tip

In this lesson you will learn:

1. More about what a `pyproject.toml` file is
1. How to declare important information (metadata) about your project to prepare for publication to PyPI

If you wish to learn more about the `pyproject.toml` format, [check out this page. ](../package-structure-code/pyproject-toml-python-package-metadata.md)
:::

<!-- TODO: it might be nice to make this admonition look different if we stick with a TLDR section -->

:::{admonition} Lesson highlights TL&DR

When creating your pyproject.toml file, consider the following:

1. There are only two required metadata tables that you need to install and publish your Python package:
    * **[build-system]**
    * **[project]**.
2. The **[project]** table stores your package's metadata. Within the **[project]** table, There are only two _required_ fields:
    * **name=**
    * **version=**
3. You should add more metadata to the `[project]` table as it will make it easier for users to find your project on PyPI. And it will also make it easier for installers to understand how to install your package.
3. When you are adding classifiers to the **[project]** table, only use valid values from [PyPI’s classifier page](https://PyPI.org/classifiers/). An invalid value here will raise an error when you build and publish your package on PyPI.
4. There is no specific order for tables in the `pyproject.toml` file. However, fields need to be placed within the correct tables. For example `requires =` always need to be in the **[build-system]** table.
5. We suggest that you include your **[build-system]** table at the top of your `pyproject.toml` file.

:::

## What is a pyproject.toml file?

The `pyproject.toml` file is a human and machine-readable file that serves as the primary configuration file for your pure Python package.

The TOML format can be compared to a format such as .json which is another structured format - however the TOML format is a simpler and easier-to-read format.

The `pyproject.toml` file is critical for building your package. Remember, [building your package](build-package) is the step that is required in order to publish to PyPI. The pyproject.toml file tells your build tool:

- What build backend to use to build your package (we are using `hatchling` in this tutorial but there are [many others to chose from](build-backend-options)).
- How and where to retrieve your package's version- either statically where you declare the version version = "1.1" or dynamically where the tool looks to the most recent tag in your history to determine the current version.
- What dependencies your package needs
- What versions of Python your package supports (important for your users).

The `pyproject.toml` file can also be used to configure other
tools such as Black.

### About the .toml format

The **pyproject.toml** file is written in [TOML (Tom's Obvious, Minimal Language) format](https://toml.io/en/). TOML is an easy-to-read structure that is founded on key/value pairs. Each section in the **pyproject.toml** file contains a `[table identifier]`.

Below you can see the build-system table. Within
that table there is one key/value pair.

`requires =`  is the kay and the value is `["hatchling"]`.

```toml
[build-system] # <- this is a table
requires = ["hatchling"] #  requires =  is a key and "hatchling" is a value contained within an array specified by square brackets [].
```

:::{tip}
Check out the [PyPA documentation](https://packaging.python.org/en/latest/tutorials/packaging-projects/#creating-pyproject-toml) if you are interested in setting build configurations for other tools.

Note that some build tools may deviate in how they store project metadata. As such you may want to refer to their documentation if you decide to use a tool other than Hatch and hatchling. We have selected hatchling and hatch as our tool of choice for this tutorial as it adheres to PyPA rules and guidelines.

:::

### What is the metadata for?

As discussed in our [pyproject.toml file overview page in the packaging guide](../package-structure-code/pyproject-toml-python-package-metadata/), the pyproject.toml file is the file that your build tool uses to populate
a `METADATA` that is included in your final Python package.

This `METADATA` file is then used by PyPI to populate your package's PyPI landing page and help users filter through the tens of thousands of packages published there.

```{figure} ../images/python-build-package/pypi-metadata-classifiers.png
:scale: 50 %
:align: center
:alt: Image showing the left side bar of PyPI for the package xclim. The section at the top says Classifier. Below there is a list of items including Development status, intended audience, License, natural language, operating system, programming language and topic. Below each of those sections are various classifier options." width="300px">

When you add the classifier section to your pyproject.toml
and your package is built, the build tool organizes the metadata into a format that PyPI can understand and
represent on your PyPI landing page. These classifiers also allow users to sort through packages by version of python they support, categories and more.
```

### pyproject.toml files make it easier for potential contributors to understand your package's structure

The `pyproject.toml` file also makes it easy for anyone browsing your GitHub
repository to quickly understand:

- How your package is built,
- What Python versions and operating systems it supports
- What it does, who maintains it
- And more

The file is also often used to configure tools such as static type checkers (e.g. mypy), linters (e.g. black, ruff), and other tools.

## Time to update your pyproject.toml file

In the last lesson, you created a bare-bones pyproject.toml
file that contained the core elements needed to build your
package:

1. A `[build]` table where ou defined your project's backend build tool (`hatchling`)
2. A `[project]` table where you defined your project's version and name.

The `pyproject.toml` file that you created, looked like this:

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "pyospackage"
version = "1.1"
```

Your next step is to add additional recommended metadata fields that will both
help users find your package on PyPI and also better describe the scope of your package. Once you add this metadata, you don't have to do it again. These metadata fields will only be updated periodically when you do something such as:

- drop a package dependency
- modify what Python versions your package supports.

:::{admonition} More on hatchling
:class: tip

The documentation for the hatchling back-end is [here](https://hatch.pypa.io/latest/config/metadata/)
:::

## Add metadata to your pyproject.toml `[project]` table

So far you have a project name and a version in the `[project]` table.

```toml
[project]
name = "pyospackage"
version = "1.1"

```

Let's add the following to your table:

- A **description** of your package. This should be a single line and should briefly describe the goal of your package using non technical terms if as all possible!
- package **authors**
- package **maintainers**

:::{admonition} Authors vs. maintainers
:class: tip

When adding maintainers and authors, you may want to think about the difference between the two.

Authors generally include people who:
* originally created / designed developed the package and
* people who add new functionality to the package.

Whereas maintainers are the people that are currently, actively working on the project. It is often the case that there is overlap in authors and maintainers. As such these lists may be similar or the same.

A good example of when the lists might diverge is sometimes you have a package where an initial author developed it and then stepped down as a maintainer to move on to other things. This person may continue to be considered an author but no longer actively maintains the package.

It is important to note there that there are many ways define author vs maintainer and we don't prescribe a single approach in this tutorial.

However, we encourage you to consider carefully, for PyPI publication, who
you want to have listed as authors and maintainers on your PyPI landing page.
:::

When you add authors and maintainers you need to use a format that will look like a Python list with a dictionary within it type of format:

`authors = [{ name = "Firstname lastname", email = "email@pyopensci.org" }]`

If you have two authors you can add them like this:

`authors = [{ name = "Firstname lastname", email = "email@pyopensci.org" }, { name = "Firstname lastname", email = "email@pyopensci.org" }]`

:::{admonition} Author names & emails
:class: note

There is a quirk with PyPI for authors that have names but not emails in the pyproject.toml. If you don't have emails for everyone, we suggest that you only add names.

:::

Your `pyproject.toml` file now should look like the example below. It is OK if you only have 1 author and the same author is also maintainer of your package:

```toml
[project]
name = "pyospackage"
version = "1.1"
description = "Tools that update the pyOpenSci contributor and review metadata that is posted on our website"
authors = [{ name = "Firstname lastname", email = "email@pyopensci.org" }]
maintainers = [{ name = "Firstname lastname", email = "email@pyopensci.org" }, { name = "Firstname lastname", email = "email@pyopensci.org" }]
```

### Add classifiers to your metadata

Next you will add classifiers to your `pyproject.toml` file. The value for each classifier that you add to your `pyproject.toml` file must come from the list of [PyPI accepted classifier values found here](https://PyPI.org/classifiers/). Any deviations in spelling and format will cause issues when you publish to PyPI.

:::{admonition} What happens when you use incorrect classifiers?
:class: tip

If you do not [use standard classifier values](https://PyPI.org/classifiers/), when you try to publish your package on PyPI it will be rejected. 😔 Don't worry if PyPI rejects you on your first try! It has happened to all of us.
:::

Review that list and add items below to your `pyproject.toml` file:

- development status
- intended audiences,
- topic
- license and
- programming language support

The classifier key should look something like the example below. A few notes:

- Your classifier values might be different depending upon the license you have selected for your package, your intended audience, development status of your package and the Python versions that you support
- You can add as many classifiers as you wish as long as you use the [designated PyPI classifier values](https://PyPI.org/classifiers/).

```toml
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Build Tools",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
```

Note that while classifiers are not required in your `pyproject.toml` file, they will help users find your package. As such we strongly recommend that you add them.

### Add package dependencies

Next add your dependencies table to the project table.
Dependencies represent the Python packages that your package requires to run. Similar to the build-system above, dependencies
get added in an array (similar to a Python list) structure.

```toml
dependencies = ["numpy", "requests", "pandas", "pydantic"]

```

:::{admonition} Pin dependencies with caution
Pinnning dependencies references to specifying a specific version of a dependency like this `numpy == 1.0`. In some specific cases, you may chose to pin or specify a lower or upper bound of a specific package. You can do that using syntax like this:

`ruamel-yaml>=0.17.21`

Note that unless you are building an application, you want to be cautious about pinning dependencies. This is because
users will be installing your package into various environments. A pinned dependency can make resolving an environment more challenging. As such only pin dependencies to a specific version if you absolutely need to do so.

One build tool that you should be aware of that pins dependencies by default is Poetry. [Read more about how to safely add dependencies with Poetry, here.](../package-structure-code/python-package-build-tools.html#challenges-with-poetry)
:::

### Requires-python

Finally, add the `requires-python` field to your `pyproject.toml` `[project]` table. The `requires-python` field, helps pip understand the lowest version of Python that you package supports when it's installed. It is thus a single value.

`requires-python = ">=3.10"`

### Your current pyproject.toml file

Once you have dependencies declared in the `pyproject.toml` file, your build
tool will know to install them when your package is installed using pip.

The project table of your `pyproject.toml` file should now look something like the example below.

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "pyospackage"
version = "1.1"
description = "Tools that update the pyOpenSci contributor and review metadata that is posted on our website"
authors = [{ name = "Firstname lastname", email = "email@pyopensci.org" }]
maintainers = [{ name = "Firstname lastname", email = "email@pyopensci.org" }, { name = "Firstname lastname", email = "email@pyopensci.org" }]

classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Build Tools",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",

dependencies = ["ruamel-yaml>=0.17.21", "requests", "python-dotenv", "pydantic"]

```

### Add a license

In the previous lessons, you added both a [README.md](4-add-license-file) file and a [LICENSE](4-add-license-file) to your package repository.
Once you have those files, you can add them to your pyproject.toml file as
links following the example below.


```
requires-python = ">=3.10"
readme = "README.md"
license = {file = 'LICENSE'}
```

and a `requires-Python = ">=3.10"` that is important to have for pip.

## Add the `[project.urls]` table

Finally, add the project.urls table to your
pyproject.toml file.

`project.urls` contains links that are relevant for your project. You might want to include:

- **Homepage:** A link to your published documentation for your project. If you are working through this tutorial, then you may not have this link yet. That's ok, you can skip it for the time being.
- **Bug reports:** a link to your issues / discussions or wherever you want users to report bugs.
- **Source:** the GitHub / GitLab link for your project.

```
[project.urls] # Optional
"Homepage" = "https://www.pyopensci.org"
"Bug Reports" = "https://github.com/pyopensci/pyosmeta/issues"
"Source" = "https://github.com/pyopensci/pyosmeta/"
```

## Putting it all together - your completed pyproject.toml file

Below is an example of a complete `pyproject.toml` file that
is commented with all of the sections we discussed above.

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "pyosmeta"
dynamic = ["version"]
description = "Tools that update the pyOpenSci contributor and review metadata that is posted on our website"
authors = [{ name = "Firstname lastname", email = "email@pyopensci.org" }]

maintainers = [
    { name = "firstname lastname", email = "admin@pyopensci.org" },
]

classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Build Tools",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3 :: Only", # BE sure to specify that you use python 3.x
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
]

dependencies = ["ruamel-yaml>=0.17.21", "requests", "python-dotenv", "pydantic"]

requires-python = ">=3.10"
readme = "README.md"
license = { text = "MIT" }

[project.urls] # Optional
"Homepage" = "https://www.pyopensci.org"
"Bug Reports" = "https://github.com/pyopensci/pyosmeta/issues"
#"Funding" = ""
"Source" = "https://github.com/pyopensci/pyosmeta/issues"
```


## Appendix - A fully commented pyproject.toml file

Below is a fully commented pyproject.toml file if you want to use it for reference.

```toml
# You can delete all of the comments once you have created your own pyproject.toml file.

# The build system table. Here we use pdm.backend as the build back end tool.
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

# The [project] section contains your package's metadata
# notice that the version is setup to be dynamically generated using dynamic=[“version”]

[project]
name = "pyospackage"
# dynamic = ["version"] # you will learn how to dynamically set the version in lesson XX
version = "1.2" # manually assign version (not preferred)
description = "Tools that update the pyOpenSci contributor and review metadata that is posted on our website"
authors = [{ name = "Firstname lastname", email = "email@pyopensci.org" }]

# maintainers section is optional but suggested.
maintainers = [
    { name = "firstname lastname", email = "admin@pyopensci.org" }, # Optional
]

# Classifiers have set values - be sure to only use classifier values from the
# PyPI page here: https://PyPI.org/classifiers/

classifiers = [
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    "Development Status :: 4 - Beta",

    # Indicate who your project is intended for
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Build Tools",

    # Pick your license (using syntax from the classifier page). We suggest MIT, BSD3 or Apache if you are corporate
    "License :: OSI Approved :: MIT License",

    # Specify the Python versions ensuring that you indicate you support Python 3.
    # this is only for PyPI and other metadata associated with your package - for your users to see
    "Programming Language :: Python :: 3 :: Only", # BE sure to specify that you use python 3.x
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
]

# Optional, but suggested. You can decide whether you wish to pin or not pin dependencies. for most projects you want to avoid pinning dependencies
dependencies = ["ruamel-yaml>=0.17.21", "requests", "python-dotenv", "pydantic"]
# This is the metadata that pip reads to understand what versions your package supports
requires-python = ">=3.10"
readme = "README.md"
license = { FILE = LICENSE }

# Examples listed include a pattern for specifying where the package tracks
# issues, where the source is hosted, where to say thanks to the package
# maintainers, and where to support the project financially. The key is
# what's used to render the link text on PyPI.
[project.urls] # Optional
"Homepage" = "https://www.pyopensci.org"
"Bug Reports" = "https://github.com/pyopensci/pyosmeta/issues"
#"Funding" = ""
"Source" = "https://github.com/pyopensci/pyosmeta/issues"

# TODO: look into what hatch needs to recognize src/
# TODO: also look into how hatch vcs interacts
# TODO: look into how you define files that go into sdist with hatchling
# This config is important for telling pdm?? that the package should live in
# a src directory
#package-dir = "src"


# Note that you need to create the tag after all commits are created for vcs based versioning to work
[tool.hatch]
version.source = "vcs"
build.hooks.vcs.version-file = "src/<package>/version.py"
```


## Example `pyproject.toml` files

Below are some examples of `pyproject.toml` files from various packages in the scientific and pyOpenSci ecosystem.
* [PyPAs fully documented pyProject.toml file](https://github.com/pypa/sampleproject/blob/main/pyproject.toml)
* [taxpasta has a nicely organized pyProject.toml file and is a pyOpenSci approved package](https://github.com/taxprofiler/taxpasta/blob/f9f6eea2ae7dd08bb60a53dd49ad77e4cf143573/pyproject.toml)


## What's next??

You are now ready to publish your Python package to PyPI and conda-forge.

* In the next lesson, you will learn [how to publish to PyPI](6-publish-pypi).
* Following that you'll learn how to create the recipe needed for conda-forge to build your package from PyPI and [publish it on conda-forge](7-publish-conda-forge).

<!--
TODO: add link to hatch documentation for metadata (which is what we want to follow using hatchling)
TODO: make sure we have this listing for license
* SPDX for licenses https://spdx.dev/use/overview/
is 2 above enough for examples? should we show a few others?
-->
