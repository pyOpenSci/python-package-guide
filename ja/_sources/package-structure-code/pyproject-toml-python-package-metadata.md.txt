(pyprojecttoml-metadata)=
# Use a pyproject.toml file for your package configuration & metadata

<!-- :::{admonition} TODOs for this page
:class: important

what's missing

::: -->

:::{admonition} Important pyproject.toml take aways
:class: todo

1. There are only two tables that are required for an installable Python package: **[build-system]** and **[project]**. The **[project]** table stores your package's metadata.
2. There are only two _required_ fields in the **[project]** table: **name=** and **version=**.
3. We suggest you add additional metadata to your `pyproject.toml` file as it will make it easier for users to find your project on PyPI.
4. When you are adding classifiers to the [project] table, only use valid values from [PyPI’s classifier page](https://PyPI.org/classifiers/). An invalid value here will raise an error when you build your package or publish to PyPI.
5. There is no specific order for tables in the `pyproject.toml` file. However fields need to be placed within the correct table sections. For example `requires =` always need to be associated with the **[build-system]** table.
6. **python-requires**: is important to have in your `pyproject.toml` file as it helps pip install your package.

:::

:::::{todo}

when these are published, remove this todo

::::{grid} 2

:::{grid-item}
:columns: 6
:class: sd-fs-3

```{button-link} ../tutorials/3-pyproject-toml.html
:color: success

Need help creating your pyproject.toml file?

This tutorial will walk you through the process.
```

:::

:::{grid-item}
:columns: 6
:class: sd-fs-3

```{button-link} ../tutorials/extras/6-setuppy-to-pyproject-toml.html
:color: success

Click here if need help migrating from setup.py/setup.cfg to pyproject.toml

```

:::
::::
:::::

## About the pyproject.toml file

Every modern Python package should include a `pyproject.toml` file. If your project is pure Python and you're using a `setup.py` or `setup.cfg` file to describe its metadata, you should consider migrating your metadata and build information to a `pyproject.toml` file.

If your project isn’t pure-python, you might still require a `setup.py` file to build the non Python extensions. However, a `pyproject.toml` file should still be used to store your project’s metadata.

:::{admonition} What happened to setup.py & how do i migrate to pyproject.toml?
:class: note
Prior to August 2017, Python package metadata was stored either in the `setup.py` file or a `setup.cfg` file. In recent years, there has been a shift to storing Python package metadata in a much more user-readable `pyproject.toml` format. Having all metadata in a single file:

- simplifies package management,
- allows you to use a suite of different [build backends](https://www.pyopensci.org/python-package-guide/package-structure-code/python-package-build-tools.html#build-back-ends) such as (flit-core, hatchling, pdm-build), and
- aligns with modern best practices.

<!--Commented until tutorials go live

 If you are migrating from a **setup.py** or **setup.cfg** file, and want help, [check out this tutorial.](../tutorials/extras/6-setuppy-to-pyproject-toml.md) -->
:::

The standard file that Python packages use to [specify build requirements and
metadata is called a **pyproject.toml**](https://packaging.python.org/en/latest/specifications/declaring-project-metadata/). Adding metadata, build requirements
and package dependencies to a **pyproject.toml** file replaces storing that
information in a setup.py or setup.cfg file.

### About the .toml format

The **pyproject.toml** file is written in [TOML (Tom's Obvious, Minimal Language) format](https://toml.io/en/). TOML is an easy-to-read structure that is founded on key/value pairs. Each section in the **pyproject.toml** file contains a `[table identifier]`.
Below that table identifier are key/value pairs that
support configuration for that particular table.

- Below `[build-system]` is considered a table in the toml language.
- Within the `build-system` table below `requires =` is a key.
- The associated value for `requires` is an array containing the value `"hatchling"`.

:::{literalinclude} ../examples/pure-hatch/pyproject.toml
:language: toml
:start-at: [build-system]
:end-at: requires = [
:::

### How the pyproject.toml is used when you build a package

<!-- TODO: this text below is now on the build sdist / wheel page. That entire section likely belongs here.  -->

When you publish to PyPI, you will notice that each package has metadata listed. Let’s have a look at [xclim](https://pypi.org/project/xclim/), one of our [pyOpenSci packages](https://www.pyopensci.org/python-packages.html). Notice that on the PyPI landing page you see some metadata about the package including python, maintainer information and more. PyPI is able to populate this metadata because it was defined using correct syntax and classifiers by Xclim's maintainers, [pyproject.toml file](https://github.com/Ouranosinc/xclim/blob/master/pyproject.toml). This metadata when the xclim package is built, is translated into a distribution file that allows PyPI to read the metadata and print it out on their website.

```{figure} ../images/python-build-package/pypi-metadata-classifiers.png
:scale: 50 %
:align: center
:alt: Image showing the left side bar of PyPI for the package xclim. The section at the top says Classifier. Below there is a list of items including Development status, intended audience, License, natural language, operating system, programming language and topic. Below each of those sections are various classifier options." width="300px">

When you add the classifier section to your pyproject.toml
and your package is built, the build tool organizes the metadata into a format that PyPI can understand and
represent on your PyPI landing page. These classifiers also allow users to sort through packages by version of python they support, categories and more.
```

## Benefits of using a pyproject.toml file

Including your package's metadata in a separate human-readable **pyproject.toml**
format also allows someone to view the project's metadata in a GitHub repository.

<!-- setup.cfg for project metadata is being deprecated - set setuptools guide and
https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html
pypa -
https://packaging.python.org/en/latest/specifications/declaring-project-metadata/ -->

```{admonition} Setup.py is still useful for complex package builds
:class: tip

Using **setup.py** to manage package builds and metadata [can cause problems with package development](https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html).
In some cases where a Python package build is complex, a **setup.py** file may
be required. While this guide will not cover complex builds, we will provide
resources working with complex builds in the future.

```

## Optional vs. Required pyproject.toml file fields

When you create your `pyproject.toml` file, there are numerous metadata fields that you can use. Below we suggest specific fields to get you started that support publication on PyPI and users finding your package.

[An overview of all of the project metadata elements can be found here.](https://packaging.python.org/en/latest/specifications/core-metadata/#project-url-multiple-use)

### Required fields for the `[project]` table

As mentioned above, your `pyproject.toml` file needs to have a **`name`** and **`version`** field in order to properly build your package:

- `name`: This is the name of your project provided as a string
- `version`: This is the version of your project. If you are using a SCM tool for versioning (using git tags to determine versions), then the version may be dynamic (more on that below).

### Optional fields to include in the `[project]` table

We strongly suggest that you also add the metadata keys below as they will
help users finding your package on PyPI. These fields will make it
clear how your package is structured, what platforms you support and
what dependencies your package requires.

- **Description:** this is a short one-line description of your package.
- **Readme:** A link to your README.md file is used for the long long-description. This information will be published on your packages PyPI landing page.
- **Requires-python** (used by pip): this is a field that is used by pip. Here you tell the installer whether you are using Python 2.x or 3.x. Most projects will be using 3.x.
- **License:** the license you are using
- **Authors:** these are the original authors of the package. Sometimes the authors are different from the maintainers. Other times they might be the same.
- **Maintainers:** you can choose to populate this or not. You can populate this using a list with a sub element for each author or maintainer name, email

:::{literalinclude} ../examples/pure-hatch/pyproject.toml
:language: toml
:start-at: authors = [
:end-at: ]
:::

- **dependencies:** dependencies are optional but we strongly suggest you include them in your pyproject.toml. Dependencies will be installed by pip when your project is installed creating a better user-experience.

- **`[project.optional-dependencies]`:** the optional or development dependencies will be installed if someone runs `python -m pip install projectname[dev]`. This is a nice way to include your development dependencies for users who may wish to contribute to your project.

- **keywords:** These are the keywords that will appear on your PyPI landing page. Think of them as words that people might use to search for your package.
- **classifiers:** The classifiers section of your metadata is also important for the landing page of your package in PyPI and for filtering of packages in PyPI. A list of [all options for classifiers can be found her](https://PyPI.org/classifiers/)e. Some of the classifiers that you should consider including
  - Development Status
  - Intended Audience
  - Topic
  - License
  - Programming language

### Advanced options in the pyproject.toml file

The examples at the bottom of this page contain ...

- **`[project.scripts]` (Entry points):** Entry points are optional. If you have a command line tool that runs a specific script hosted in your package, you may include an entry point to call that script directly at the command line (rather than at the Python shell).

  - Here is an example of[a package that has entry point script](https://github.com/pyOpenSci/pyosMeta/blob/main/pyproject.toml#L60)s. Notice that there are several core scripts defined in that package that perform sets of tasks. The pyOpenSci is using those scripts to process their metadata.
- **Dynamic Fields:** if you have fields that are dynamically populated. One example of this is if you are using scm / version control based version with tools like `setuptooms_scm`, then you might use the dynamic field, such as version (using scm) **dynamic = ["version"]**

## Add dependencies to your pyproject.toml file

The pyproject.toml file can also be used as a replacement for the requirements.txt file which has been traditionally used to store development dependencies such as pytest, code formatters such as Black and documentation tools such as sphinx.

To add dependencies to your build, add a `[project.optional-dependencies]` table to your pyproject.toml file.

Then specify dependency groups as follows:

:::{literalinclude} ../examples/pure-hatch/pyproject.toml
:language: toml
:start-at: [project.optional-dependencies]
:::

Following the above example, you install dependencies like this:

- `python -m pip install -e .[tests]`

The above will install both your package in editable mode and all of the dependencies declared in the tests section of your `[project.optional-dependencies]` table.

To install all dependencies and also your package, you'd use:

`python -m pip install -e .[tests,lint,docs]`

:::{admonition} Recursive dependencies
:class: tip

You can also setup sets of recursive dependencies. [See this blog post for more.](https://hynek.me/articles/python-recursive-optional-dependencies/)

:::

## Example pyproject.toml for building using hatchling

Below is an example build configuration for a Python project. This example
package setup uses **hatchling** to build the [package's sdist and wheels](python-package-distribution-files-sdist-wheel).

:::{literalinclude} ../examples/pure-hatch/pyproject.toml
:language: toml
:end-before: [project.optional-dependencies]
:::

Notice that dependencies are specified in this file.

## Example pyproject.toml for building using setuptools

The package metadata including authors, keywords, etc is also easy to read.
Below you can see the same TOML file that uses a different build system (setuptools).
Notice how simple it is to swap out the tools needed to build this package!

In this example package setup you use:

- **setuptools** to build the [package's sdist and wheels](python-package-distribution-files-sdist-wheel)
- **setuptools_scm** to manage package version updates using version control tags

In the example below `[build-system]` is the first table
of values. It has two keys that specify the build backend API and containing package:

1. `requires =`
1. `build-back-end =`

:::{literalinclude} ../examples/pure-setuptools/pyproject.toml
:language: toml
:::

```{note}
[Click here to read about our packaging build tools including PDM, setuptools, Poetry and Hatch.](/package-structure-code/python-package-build-tools)
```
