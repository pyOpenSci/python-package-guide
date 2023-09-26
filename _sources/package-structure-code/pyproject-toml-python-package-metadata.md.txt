# Use a pyproject.toml file for your package configuration & metadata

The standard file that Python packages use to [specify build requirements and
metadata is called a **pyproject.toml**](https://packaging.python.org/en/latest/specifications/declaring-project-metadata/). Adding metadata, build requirements
and package dependencies to a **pyproject.toml** file replaces storing that
information in a setup.py or setup.cfg file.

The **pyproject.toml** file is written in [TOML (Tom's Obvious, Minimal Language) format](https://toml.io/en/). TOML is an easy-to-read structure that is founded on key/value pairs. Each section in the **pyproject.toml** file contains a `[table identifier]`.
Below that table identifier are key/value pairs that
support configuration for that particular table.

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

## Example pyproject.toml for building using PDM

Below is an example build configuration for a Python project. This example
package setup uses:

- **pdm.backend** to build the [package's sdist and wheels](python-package-distribution-files-sdist-wheel)

```
[build-system]
requires = ["pdm-backend>=1.0.0"]
build-backend = "pdm.backend"

[project]
name = "examplePy"
authors = [
    {name = "Some Maintainer", email = "some-email@pyopensci.org"},
]
maintainers = [
    {name = "All the contributors"},
]
description = "An example Python package used to support Python packaging tutorials"
keywords = ["pyOpenSci", "python packaging"]
readme = "README.md"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
]
dependencies = [
    "dependency-package-name-1",
    "dependency-package-name-2",
]
```

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

```
[build-system]
requires = ["setuptools>=61"]
build-backend = "setuptools.build_meta"

[project]
name = "examplePy"
authors = [
    {name = "Some Maintainer", email = "some-email@pyopensci.org"},
]
maintainers = [
    {name = "All the contributors"},
]
description = "An example Python package used to support Python packaging tutorials"
keywords = ["pyOpenSci", "python packaging"]
readme = "README.md"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
]
dependencies = [
    "dependency-package-name-1",
    "dependency-package-name-2",
]
```

```{note}
[Click here to read about our packaging build tools including PDM, setuptools, Poetry and Hatch.](/package-structure-code/python-package-build-tools)
```
