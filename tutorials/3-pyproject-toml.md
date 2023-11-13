# Make your Python package PyPI ready - pyproject.toml

:::{admonition} TODOS
:class: important
- add a note for hatch - if you want to use dynamic versioning you'll need to add `tool.hatch.version` to the pyproject.toml file. 
- flesh out the readme and license section after those pages exist
- The bottom paragraphs at the very end are still out of place and likely could be combined...
- TODO: make sure they add the dev requirements here... including build.
:::

<!--
TODO: make sure that the link to our guide is on this page.  [Learn more about this file in our packaging guide.](https://www.pyopensci.org/python-package-guide/package-structure-code/pyproject-toml-python-package-metadata.html) -->

In [the installable code lesson](2-installable-code), you learned how to add the bare minimum information to a `pyproject.toml` file to make it pip installable.

To both publish your package to PyPI and also help users find your package, you will want to add additional metadata to your `pyproject.toml` file that describes the use and contents of your package. You will
learn how to do that in this lesson.

<!--
myst-nb or nbsphinx to run code
> TODO: they haven't added other files yet such as readme and license.
> the readme and license are important for publishing to pypi. -->

:::{admonition} Learning Objectives
:class: tip

In this lesson you will learn:

1. More about what a `pyproject.toml` file is
1. How to declare important information (metadata) about your project to prepare for publication to PyPI

If you wish to learn more about the `pyproject.toml` format, [check out this page. ](../package-structure-code/pyproject-toml-python-package-metadata.md)
:::

## What is a pyproject.toml file?

The `pyproject.toml` file is a human and machine-readable TOML file. The `pyproject.toml` file tells your build tool:

- What build backend to use to build your package (e.g. `setuptools`, `hatchling`, `pdm.build`, etc)
- How and where to retrieve your package's version (dynamically vs statically)
- What dependencies you are using
- What versions of Python your package supports

The `pyproject.toml` file can also be used to configure other
tools such as Black.

### About the .toml format

The **pyproject.toml** file is written in [TOML (Tom's Obvious, Minimal Language) format](https://toml.io/en/). TOML is an easy-to-read structure that is founded on key/value pairs. Each section in the **pyproject.toml** file contains a `[table identifier]`.
Below that table identifier are key/value pairs that
support configuration for that particular table.

- Below `[build-system]` is considered a table in the toml language.
- Within the build-system table below requires = is a key.
- The associated value for requires is an array containing the value "hatchling".

```toml
[build-system] # <- this is a table
requires = ["hatchling"] #  requires =  is a key and "hatchling" is a value contained within an array specified by square brackets [].

```

:::{tip}
Check out the [PyPA documentation](https://packaging.python.org/en/latest/tutorials/packaging-projects/#creating-pyproject-toml) if you are interested in setting build configurations for other tools.
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

The file is also often used to configure tools such as static type checkers (e.g. mypy), linters (eg black, ruff), and other tools.

## Time to update your pyproject.toml file

In the last lesson, you created a bare-bones pyproject.toml
file that contained the core elements needed to build your
package:

1. A `[build]` table where ou defined your project's backend build tool (`hatchling`)
2. a `[project]` table where you defined your project's version and name.

The pyproject.toml file that you created, looked like this:

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "pyospackage"
version = "1.1"
```

Here, you will add a suite of recommended metadata fields. Once you add these, you don't have to do it again. These metadata fields will only be updated periodically when you do something such as:

- drop a dependency
- modify what versions of Python your package supports.

As such much of the work you do here will be a one-time thing.

:::{admonition} Python package build backends

While the example above uses the `hatchling` build back-end you can chose
to use `setuptools` or any other tool you wish to create and build
your package.

[Learn more about packaging tools and build back-ends here](https://www.pyopensci.org/python-package-guide/package-structure-code/python-package-build-tools.html#build-back-ends)

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

:::{admonition} Authors vs maintainers
:class: tip

_TODO from karen: It might be worth pointing out that there is no formal definitions for these terms, and projects can define maintainers and authors in a way that best represents their developer community?_

When adding maintainers and authors, you may want to think about the difference between the two.

Authors are generally people who originally created / designed developed the package. And people who add new functionality to the package. Whereas maintainers are the people that are currently, actively working on the project.

It is often the case that there is overlap in authors and maintainers. As such these lists may be similar or the same.

A good example of when the lists might diverge is sometimes you have a package where an initial author developed it and then stepped down as a maintainer to move on to other things. This person may continue to be considered an author but no longer actively maintains the package.
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

- that your classifiers might be different depending upon the license you have selected for your package, and the Python versions you support
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
Dependencies represent the Python packages that your package requires to run. Dependencies
get added in a list like structure.

```toml
dependencies = ["numpy", "requests", "pandas", "pydantic"]

```

:::{admonition} Pin dependencies with caution
Pinnning dependencies references to specifying a specific version of a dependency like this `numpy == 1.0`. In some specific cases, you may chose to pin or specify a lower or upper bound of a specific package. You can do that using syntax like this:

`ruamel-yaml>=0.17.21`

Note that unless you are building an application, you want to be cautious about pinning dependencies. This is because
users will be installing your package into various environments. A pinned dependency can make resolving an environment more challenging. As such only pin dependencies to a specific version if you absolutely need to do so.

_TODO: Add a link to where we talk about pinning in the guide??_
:::

### Requires-python

Lastly, be sure to add the `requires-python` field to your pyproject.toml. This field, helps pip when installing your package understand the lowest version of Python that you package supports.

`requires-python = ">=3.10"`

### Your current pyproject.toml file

Once you have dependencies declared in the `pyproject.toml `file, your build
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

### Add a license..

:::{admonition} THIS SECTION NEEDS WORK
:class: todo

:::

Finally add

- requires-python -
- readme and (they don't have a readme file yet... )
- license.

```
requires-python = ">=3.10"
readme = "README.md"
license = { text = "MIT" } # be sure to direct them to license values and how to chose a license.
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

## Putting it all together - a commented example pyproject.toml file

Below is an example of a complete `pyproject.toml` file that
is commented with all of the sections we discussed above.

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
license = { text = "MIT" }

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


# TODO: update this to work with hatchling
# # Note that you need to create the tag after all commits are created - otherwise
[tool.hatch]
version.source = "vcs"
build.hooks.vcs.version-file = "src/<package>/version.py"
```

:::{admonition} About the toml format
:class: tip

Note that when using the toml format, each section is defined with a `[section-here]` and that section is commonly referred to as a "table".

:::

### Things to consider in your pyproject.toml file

When creating your pyproject.toml file, consider the following:

1. As highlighted above, there are only two tables or tables that you need to install and publish your package: the **[build-system]** table and the **[project]** section.
2. The **[project]** table stores your package's metadata. There are only two _required_ fields in the **[project]** table: **name=** and **version=**. However, you should add more metadata here as it will make it easier for users to find your project on PyPI.
3. When you are adding classifiers to the [project] table, only use valid values from [PyPI’s classifier page](https://PyPI.org/classifiers/). An invalid value here will raise an error when you build your package or publish to PyPI.
4. There is no specific order for tables in the pyproject.toml file. However fields need to be placed within the correct table sections. For example `requires =` always need to be associated with the **[build-system]** table.
5. Related to the above while this is not required, we suggest that you include your **[build-system]** table at the top of your `pyproject.toml` file.

## Example file highlights

Notice a few things about the pyproject.toml file:

1. At the top, we specify the [build backend](https://www.pyopensci.org/python-package-guide/package-structure-code/python-package-build-tools.html#build-back-ends)- being used. This is valuable as a user and potential new contributor can quickly understand what tools you're using to build your package. While you don’t need to list this at the top we suggest that you do. That way it’s easy for a contributor to quickly understand what tools you are using to create your package.
2. Below there is a `[project]` section. This is where you store your project's metadata. For the most part, this metadata is what PyPI will use to populate your landing page for your project.
3. There is:
   - a metadata section specifying Python versions that your package supports (which is what PyPI uses to index your package)
   -

![](https://hackmd.io/_uploads/HJ-p2J223.png)

## Example pyproject.toml file without comments

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

### A few other notes

- The order of the sections of your pyproject.toml file doesn’t matter. What is important is that you have the correct subsections in each section. For example the build-system section should include your build requirements, but not your package classifiers which go in the project section of the pyproject toml.
