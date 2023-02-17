# Use a pyproject.toml file for your package configuration & metadata

The standard file that Python packages use to specify build requirements and
metadata is called a pyproject.toml. The pyproject.toml file has become the
standard for declaring Python package metadata (including dependencies) rather
than using a setup.py file (or a setup.py + setup.cfg file).

As such you should try to [include all project based metadata and build system specifications in a `pyproject.toml` file.](https://packaging.python.org/en/latest/specifications/declaring-project-metadata/) Using setup.py to manage both package set up and
hold metadata [can cause problems with package development.](https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html)


```{admonition} Benefits of using a pyproject.toml file
:class: tip

1. Because setup.py has a mixture of code and metadata, it will be run twice when
building your package. First it will be run to extract metadata (dependencies). Then it will be run to build your package.
1. Including your package's metadata in a separate human-readable `pyproject.toml` format also allows someone to view the project's metadata without
running any Python code.
```

A pyproject.toml is written in [TOML (Tom's Obvious, Minimal Language) format](https://toml.io/en/). TOML is an easy-to-read structure that is founded on key: value pairs.

Each section in the pyproject.toml file contains a `[table identifier]`.
Below that table identifier are key value pairs that
support configuration for that particular table.

<!-- setup.cfg for project metadata is being deprecated - set setuptools guide and
https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html
pypa -
https://packaging.python.org/en/latest/specifications/declaring-project-metadata/ -->

```{note}
<!-- [PEP518 describes the move away from setup.py to the pyproject.toml file.](https://peps.python.org/pep-0518/) -->
Python package standards are moving away from including both package metadata
and Python code needed to set up a package in the same **setup.py** file.
Instead we are moving towards using a **proproject.toml** file.

In some cases where a build is complex, a **setup.py** file may still be
required. While this guide will not cover complex builds, we will provide
resources working with complex builds in the future.

<!-- https://github.com/pyOpenSci/python-package-guide/pull/23#discussion_r1071541329
ELI: A complex build could mean running a python script that processes some data file and produces a pure python module file.

Probably not common in the scientific community specifically, but I've seen quite a few setup.py files that contain custom build stages which e.g. build gettext locale catalogs.

The main point is that it is more "complex" than simply copying files or directories as-is into the built wheel.
-->
```

## Example pyproject.toml

Below is an example build configuration for a Python project. This setup
requires:

* **setuptools** to create the package structure,
* **wheel** which is used by `setuptools` to create the [**.whl** (wheel) file](https://realpython.com/python-wheels/).
* **setuptools build** to "build" the package
* **setuptools_scm** to manage package version updates

In the example below `[build-system]` is the first table
of values. It has two keys that specify the build front end and backend for a package:

1. `requires =`
1. `build-backend =`

```
[build-system]
requires = ["setuptools>=45", "setuptools_scm[toml]>=6.2"]
build-backend = "setuptools.build_meta"

[project]
name = "examplePy"
authors = [
    {name = "Some Maintainer", email = "some-email@pyopensci.org"}
]
maintainers = [{name = "All the contributors"}]
license = {text = "BSD 3-Clause"}
description = "An example Python package used to support Python packaging tutorials"
keywords = ["pyOpenSci", "python packaging"]
readme = "README.md"

dependencies = [
    "dependency-package-name-1",
    "dependency-package-name-2",
]
```


Notice that you also can specify dependencies in this file.


A major benefit of the pyproject.toml file is that it makes is transparent

1. what build system you are using to create your package
2. what dependencies you need


The package metadata including authors, keywords, etc is also easy to read.
Below you can see the same toml file that uses a different build system (PDM).
Notice how simple it is to swap out the tools needed to build this package!

```
[build-system]
requires = ["pdm-pep517>=1.0.0"]
build-backend = "pdm.pep517.api"

[project]
name = "examplePy"
authors = [
    {name = "Some Maintainer", email = "some-email@pyopensci.org"}
]
maintainers = [{name = "All the contributors"}]
license = {text = "BSD 3-Clause"}
description = "An example Python package used to support Python packaging tutorials"
keywords = ["pyOpenSci", "python packaging"]
readme = "README.md"

dependencies = [
    "dependency-package-name-1",
    "dependency-package-name-2",
]
```



```{note}
[Click here to read about our packaging documentation requirements.](/package-structure-code/python-package-build-tools)
```

<!-- TODO: add link to section on build tools when it exists and
turn this into button:

We discuss build tools for python package more here.
-->



<!-- TODO:
1. add some links to packages that are using a purely toml config
1. link to our example package once it's further along
-->
