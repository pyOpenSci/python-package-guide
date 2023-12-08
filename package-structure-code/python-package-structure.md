# Python Package Structure for Scientific Python Projects

There are two different layouts that you will commonly see
within the Python packaging ecosystem:
[src and flat layouts.](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)
Both layouts have advantages for different groups of maintainers.

We strongly suggest, but do not require, that you use the **src/** layout (discussed below)
for creating your Python package. This layout is also recommended in the
[PyPA packaging guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/).

```{admonition} pyOpenSci will never require a specific package structure for peer review
:class: important

We understand that it would be tremendous effort for existing
maintainers to move to a new layout.

The overview on this page presents recommendations that we think are best for
someone getting started with Python packaging or someone who's package
has a simple build and might be open to moving to a more fail-proof approach.
```

An example of the **src/package** layout structure can be seen below.

```
myPackageRepoName
├── CHANGELOG.md               ┐
├── CODE_OF_CONDUCT.md         │
├── CONTRIBUTING.md            │
├── docs                       │ Package documentation
│   └── index.md
│   └── ...                    │
├── LICENSE                    │
├── README.md                  ┘
├── pyproject.toml             ] Package metadata and build configuration
├── src                        ┐
│   └── myPackage              │
│       ├── __init__.py        │ Package source code
│       ├── moduleA.py         │
│       └── moduleB.py         ┘
└── tests                      ┐
   └── ...                     ┘ Package tests
```

Note the location of the following directories in the example above:

- **docs/:** discussed in our docs chapter, this directory contains your user-facing documentation website. In a **src/** layout docs/ are normally included at the same directory level of the **src/** folder.
- **tests/** this directory contains the tests for your project code. In a **src/** layout tests are normally included at the same directory level of the **src/** folder.
- **src/package/**: this is the directory that contains the code for your Python project. "Package" is normally your project's name.

Also in the above example, notice that all of the core documentation files that
pyOpenSci requires live in the root of your project directory. These files
include:

- CHANGELOG.md
- CODE_OF_CONDUCT.md
- CONTRIBUTING.md
- LICENSE.txt
- README.md

<!-- TODO: CHANGELOG is not mentioned in either documentation nor peer review -->

```{button-link} https://www.pyopensci.org/python-package-guide/documentation
:color: primary
:class: sd-rounded-pill

Click here to read about our packaging documentation requirements.
```

While we recommend the **src/** layout we also review the **flat** layout here. Both are used in the Python ecosystem.

```{admonition} Example scientific packages that use **src/package** layout

* [Sourmash](https://github.com/sourmash-bio/sourmash)
* [bokeh](https://github.com/bokeh/bokeh)
* [openscm](https://github.com/openscm/openscm-runner)
* [awkward](https://github.com/scikit-hep/awkward)
* [poliastro](https://github.com/poliastro/poliastro/)

```

## The src/ layout and testing

The benefit of using the **src/package** layout, particularly if you
are creating a new package, is that it ensures tests are run against the
installed version of your package rather than the files in your package
working directory. If you run your tests on your files rather than the
installed version, you may be missing issues that users encounter when
your package is installed.

If `tests/` are outside of the **src/package** directory, they aren't included in the package wheel. This makes your package size slightly smaller which then places places a smaller storage burden on PyPI which has over 400,000 packages to support.

- [Read more about reasons to use the **src/package** layout](https://hynek.me/articles/testing-packaging/)

```{admonition} How Python discovers and prioritizes importing modules

By default, Python adds a module in your current working directory to the front of the Python module search path.

This means that if you run your tests in your package's working directory, using a flat layout, `/package/module.py`, Python will discover `package/module.py` file before it discovers the installed package.

However, if your package lives in a src/ directory structure **src/package** then it won't be, by default, added to the Python path. This means that when you import your package, Python will be forced to  search the active environment (which has your package installed).

Note: Python versions 3.11 and above have a path setting that can be adjusted to ensure the priority is to use installed packages first (e.g. `PYTHONSAFEPATH`).
```

### Sometimes tests are needed in a distribution

We do not recommend including tests as part of your package wheel by default. However, not including tests in your package distribution will make it harder for people other than yourself to test whether your package is functioning correctly on their system. If you have a small test suite (Python files + data), and think your users may want to run tests locally on their systems, you can include tests by moving the `tests/` directory into the **src/package** directory (see example below).

```bash
src/
  package/
    tests/
docs/
```

Including the **tests/** directory in your **src/package** directory ensures that tests will be included in your package's wheel.

Be sure to read the [pytest documentation for more about including tests in your package distribution](https://docs.pytest.org/en/7.2.x/explanation/goodpractices.html#choosing-a-test-layout-import-rules).

```{admonition} Challenges with including tests and data in a package wheel
:class: tip

Tests, especially when accompanied by test data can create a few small challenges including:

- Take up space in your distribution which will build up over time as storage space on PyPI
- Large file sizes can also slow down package install.

However, in some cases, particularly in the scientific Python ecosystems you may need to include tests.
```

### **Don't include test suite datasets in your package**

If you do include your tests in your package distribution, we strongly
discourage you from including data in your test suite directory. Rather,
host your test data in a repository such as Figshare or Zenodo. Use a
tool such as [Pooch](https://www.fatiando.org/pooch/latest/) to access
the data when you (or a user) runs tests.

Check out the testing section of our guide for more information about tests.

- The **src/package** layout is semantically more clear. Code is always found in the
  **src/package** directory, `tests/` and `docs/`are in the root directory.

```{important}
If your package tests require data, we suggest that you do NOT include that
data within your package structure. We will discuss this in more detail in a
tutorial. Include data in your package structure increases the size of your
distribution files. This places a maintenance toll on repositories like PyPI and
anaconda cloud that have to deal with thousands of package uploads.
```

## About the flat Python package layout

Currently most scientific packages use the **flat-layout** given:

- It's the most commonly found layout with the scientific Python ecosystem and
  people tend to look to other packages / maintainers that they respect for examples
  of how to build Python packages.
- Many Python tools depend upon tools in other language and / or complex builds
  with compilation steps. Many developers thus appreciate / are used to features
  of the flat layout.

While we present this layout here in our guide, we suggest that those just
getting started with python packaging start with the src/package layout
discussed above. Numerous packages in the ecosystem [have had to move to a
src/ layout](https://github.com/scikit-build/cmake-python-distributions/pull/145)

```{admonition} Why most scientific Python packages do not use source
:class: tip

In most cases the advantages of using the **src/package** layout for
larger scientific packages that already use flat approach are not worth it.
Moving from a flat layout to a **src/package** layout would come at a significant cost to
maintainers.

However, the advantages of using the  **src/package** layout for a beginner are significant.
As such, we recommend that if you are getting started with creating a package,
that you consider using a  **src/package** layout.
```

## What does the flat layout structure look like?

The flat layout's primary characteristics are:

- The source code for your package lives in a directory with your package's
  name in the root of your directory
- Often the `tests/` directory also lives within that same `package` directory.

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

### Benefits of using the flat layout in your Python package

There are some benefits to the scientific community in using the flat layout.

- This structure has historically been used across the ecosystem and packages
  using it are unlikely to change.
- You can import the package directly from the root directory. For some this
  is engrained in their respective workflows. However, for a beginner the
  danger of doing this is that you are not developing and testing against the
  installed version of your package. Rather, you are working directly with the
  flat files.

```{admonition} Core scientific Python packages that use the flat layout
:class: tip

* [numpy](https://github.com/numpy/numpy)
* [scipy](https://github.com/scipy/scipy)
* [pandas](https://github.com/pandas-dev/pandas)
* [xarray](https://github.com/pydata/xarray)
* [Jupyter-core](https://github.com/jupyter/jupyter_core)
* [Jupyter notebook](https://github.com/jupyter/notebook)
* [scikit-learn](https://github.com/scikit-learn/scikit-learn)

It would be a significant maintenance cost and burden to move all of these
packages to a different layout. The potential benefits of the source layout
for these tools is not worth the maintenance investment.
```

<!--
Not sure where to put this now ... most new users won't have multiple packages. maybe this goes into the complex packing page as we build that out?

```{admonition} Multiple packages in a src/ folder
:class: tip

In some more advanced cases you may have more than one package in your src/ directory. See [black's GitHub repo](https://github.com/psf/black/tree/main/src) for an example of this. However, for most beginners you will likely only have one sub-directory in your **src/** folder.
``` -->

<!--
```{admonition} A few notes about the src/ layout
:class: tip

It is important to note here that sometimes when using the src/package structure the directory name (e.g. package name) is different from the actual project or package name. What is important to take away here is that you should store your code within a sub directory within **src/**.
``` -->
