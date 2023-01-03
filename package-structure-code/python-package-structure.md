# Python Package Structure for Scientific Python Projects
There are two different general layouts that you will commonly see 
within the Python packaging ecosystem: 
[src and flat layouts (click here to learn more).](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/) 
We believe that both layouts have advantages.
The Python packaging authority advocates for the [**src/** layout](https://py-pkgs.org/04-package-structure), 
in their tutorials. 

```{important}
pyOpenSci however will never require a specific package structure for its 
peer review process. The overview on this page presents recommendations. 
```

Below you will learn about the pros and cons of both layouts.

Currently most scientific packages use the **flat-layout** given:

* It's the most commonly found layout with the scientific Python ecosystem 
* Many Python tools depend upon tools in other language and / or complex builds with compilation steps. Many developers thus appreciate features of the flat layout such as tests being included with the package when they are installed) to support troubleshooting across installations.

 In the end, the advantages of using the **src/** layout for scientific packages 
 that already use this approach do not 
 outweigh the maintenance cost that a large cultural change in 
 package structure would bring to existing maintainers the scientific 
 Python ecosystem. 


```{tip}

## Core scientific Python packages that use the flat layout

* [numpy](https://github.com/numpy/numpy)
* [scipy](https://github.com/scipy/scipy)
* [pandas](https://github.com/pandas-dev/pandas)
* [xarray](https://github.com/pydata/xarray) 
* [Jupyter-core](https://github.com/jupyter/jupyter_core)
* [Jupyter notebook](https://github.com/jupyter/notebook)
* [scikit-learn](https://github.com/scikit-learn/scikit-learn)

It would be a significant maintenance cost and burden to move all of these
packages to a different layout. The potential benefits of the source layout 
for these tools is not worth the maintenance investment. To avoid dividing the scientific Python community, 
pyOpenSci supports maintainers using a flat layout for scientific packages. 
```

## What does the flat layout structure look like? 

The flat layout's primary characteristics are: 

* The source code for your package lives in a directory with your package's name in the root of your directory 
* Often the `tests/` directory also lives within that same `package-name` directory.

Below you can see the recommended structure of a scientific Python package 
using the flat layout. 

```bash
myPackage/
├── CHANGELOG.md             ┐
├── CODE_OF_CONDUCT.md       │
├── CONTRIBUTING.md          │
├── docs/                    │ Package documentation
│   └── ...                  │
├── LICENSE                  │
├── README.md                ┘
├── pyproject.toml           ] Package metadata and build configuration  
|   myPackage/               ┐ 
│     ├── __init__.py        │ Package source code
│     ├── moduleA.py         │
│     └── moduleB.py         ┘
      tests/                 ┐
        └── test-file1.py    | Package tests
        └── ....             ┘ 
```


```{note} 
If you look at 
[the `matplotlib` repository on GitHub](https://github.com/matplotlib/matplotlib), 
you will notice it too has a src/ directory, however 
that structure is there because `matplotlib` has uncompiled source code in that 
directory. it is not adhering to the **src/** layout explicitly. 
```

### Benefits of using the flat layout in your Python package

There are some benefits to the scientific community in using the flat layout.

* This structure has historically been used across the ecosystem and packages 
using it are unlikely to change. Thus, you'd be following a convention that many 
packages use already.  
* This structure is simpler to setup to support packaging compared to the `src/` 
approach given the package source code is in the root directory. This means that 
your package will be "found" by build back-ends automagically. 
* You can directly install the package directly from the root directory. 
* Tests are shipped with your package. This allows developers to invoke tests on 
various machines to troubleshoot installations if needed. (This could easily 
be implemented using a `src/` layout too!)

### The `src/` layout for Python packages
 
The `src/` layout is another option to structure you Python package. This layout 
is advocated for by the [PyPA](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
The key characteristic of this layout is that your package
uses a `src/package-name` directory structure. Tests are
often located in a directory outside of the package (but they don't have to be).

#### Pros of the src/ layout

The benefits of the `src/` layout approach include:

* It ensures that tests are always running on the installed version of your 
package rather than on the flat files
* If `tests/` are outside of the `src/` directory, they aren't delivered to the user 
installing your package. This makes the package size slightly smaller. 
* This layout is semantically more clear. Code is always found in the 
`src/package-name` directory, `tests/` are in the root and with docs/
 
#### Cons of the src/ layout
* Can be slightly trickier to configure. examples:
   * Tools like build won't automatically find the package directory if it's 
   within `src/package-name` without being configured.
* Setting up continuous integration is more complex as you will have to account 
for the `src/` directory when installing the package
* While this layout is common in the broader Python ecosystem, it does not 
necessarily support the needs of the scientific Python ecosystem which often has 
tools that wrap around other compiled languages such as C++. Often times code 
that needs to be compiled is stored in `src/`.
 
An example of the `src/` layout structure can be seen below:

```
myPackage
├── CHANGELOG.md               ┐
├── CODE_OF_CONDUCT.md         │
├── CONTRIBUTING.md            │
├── docs                       │ Package documentation
│   └── index.md
│   └── ...                    │
├── LICENSE                    │
├── README.md                  ┘
├── pyproject.toml             ┐
├── src                        │
│   └── myPackage               │ Package source code, metadata,
│       ├── __init__.py        │ and build instructions
│       ├── moduleA.py         │
│       └── moduleB.py         ┘
└── tests                      ┐
   └── ...                     ┘ Package tests
```



<!-- Not sure why i added this here? -->
To install your package in editable mode use:

```bash
$ cd package-name
$ pip install -e .`
```

## Core file requirements for a Python package

In the above example, notice that all of the core documentation files that 
pyOpenSci requires live in the root of your project directory. These files 
include: 

<!-- TODO: add link when documentation section is merged -->
* CHANGELOG.md 
* CODE_OF_CONDUCT.md 
* CONTRIBUTING.md 
* LICENSE.txt
* README.md 

Also note that there is a **docs/** directory at the root where your user-facing 
documentation website content lives.

```{button-link} https://www.pyopensci.org/python-package guide/documentation
:color: primary
:class: sd-rounded-pill float-left
Click here to read about our packaging documentation requirements. <<This LINK won't work until OPEN doc PR IS MERGED>>
```

Finally, notice that the **tests/** directory containing your test suite is 
located within the **packageName/** directory. 

<!-- This tutorial obviously doesn't exist yet... but we need to somehow 
specify this because it's i think the main concern behind tests shipping with 
code - PyPI maintenance burden grows quickly -->

```{important}
If your package tests require data, we suggest that you NOT include that 
data within your package structure. We will discuss this in more detail in a 
tutorial.
```

<!--
```{note}
### Src vs. flat layouts for Python packaging
While you will see other structures, [such as the `src/` 
layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/) recommended by the [Python packaging authority](https://py-pkgs.org/04-package-structure) and others, all scientific
Python packages have used a flat layout. This structure has been 
prevalent for almost a decade. 

Because a core goal shared by both pyOpenSci and the Scientific Python 
project, is to see increased standardization in Python packaging, we 
are advocating for a structure that is used by existing packages in the 
ecosystem. 

Many of our core scientific Python packages wrap around other compiled languages, such as C++. They thus have source code that requires compilation. It would be challenging and potentially time-consuming for all of those packages to modify their current 
structure. And further it would not provide them with any core benefit.


```
-->

## Use a pyproject.toml file for your package configuration & metadata

We strongly recommend that you [include all project based metadata and build system specifications in a `pyproject.toml` file.](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/) [Using setup.py to manage both package setup and hold metadata can present numerous risks.](https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html)


```{note}
Moving away from the **setup.py** file provides two benefits:

1. Because setup.py has a mixture of code and metadata, it opens the user to a potential bad code injection on their computer when the package is installed. 
1. Including your package's metadata in a separate human-readable `pyproject.toml` format also allows someone to view the project's metadata without 
running any Python code.
```

The [TOML (Tom's Obvious, Minimal Language) format](https://toml.io/en/), is an easy-to-read structure that is founded on key: value pairs. 

Each section in the file contains a `[table identifier]`. 
Below that table identifier are key value pairs that 
support configuration for that particular table. 

```{note}
[PEP518 describes the move away from setup.py to the pyproject.toml file.](https://peps.python.org/pep-0518/)
Python package standards are moving away from 
including both package metadata and python code needed to setup a package installation in the same **setup.py** file. Instead we are moving towards using 
a **proproject.toml** file sometimes combined with a **setup.cfg** file. 

In some cases 
where a build is particularly complex, a **setup.py** file may still be required. 
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
requires = ["setuptools>=45", "wheel", "setuptools_scm[toml]>=6.2"]
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


<!-- TODO: add link to section on build tools when it exists and 
turn this into button: 

We discuss build tools for python package more here. 
-->

<!-- TODO: where does this tip belong? -->
```{tip}
PEPs stand for Python Enhancement Protocols. They provide guidelines for standardizing 
Python code and packaging. 
```


<!-- TODO: 
1. add some links to packages that are using a purely toml config 
1. link to our example package once it's further along
-->