# Publish to conda-forge

In the previous lessons, you've learned the following:

1. How to structure your code into a package like format that can be installed into a Python environment.
2. How to add a `README` and `LICENSE` file to your package
3. How to setup your `pyproject.toml` file with all of the metadata that PyPI requires and also metadata that will be helpful for users to find your package.

If you have gone through all of the above lessons, you are now ready to
build your package's distribution files which are needed for you to publish
to PyPI. Here, you will learn how to set things up on
PyPI and how to manually publish to (test) PyPI using twine.

:::{figure-md} build-workflow-tutorial
<img src="../images/tutorials/publish-package-pypi-conda.png" alt="Graphic showing the high level packaging workflow. On the left you see a graphic with code, metadata and tests in it. those items all go into your package. Documentation and data are below that box because they aren't normally published in your packaging wheel distribution. an arrow to the right takes you to a build distribution files box. that box leads you to either publishing to testPyPI or the real pypi. from PyPI you can then connect to conda forge for an automated build that sends distributions from PyPI to conda-forge." width="700px">

You need to build your Python package in order to publish it to PyPI (or Conda). The build process organizes your code and metadata into a distribution format that can be uploaded to PyPI and subsequently downloaded and installed by users. NOTE: you need to publish a sdist to PyPI in order for conda-forge to properly build your package automatically.
:::

<!-- Pypa resource: https://packaging.python.org/en/latest/tutorials/packaging-projects/#uploading-the-distribution-archives
https://spdx.org/licenses/PSF-2.0.html (double check that we can use language from pypa tutorial??


https://packaging.python.org/en/latest/guides/using-testpypi/

-->


You can follow the same steps to setup your package on the real PyPI. However
in this lesson we will use testPyPI as a practice run.

in xx lesson, you will learn how to setup an automated release workflow on GitHub
using GitHub actions that will automate the PyPI publication process whenever
you create a new software release.

:::{admonition} Learning Objectives
:class: tip

In this lesson you will learn how to:

- how to build your package's sdist and wheel distributions
- Setup an account on testPyPI (the process is similar for the real PyPI)
- Publish your package to PyPI

Once your package is on PyPI you can then easily publish it to conda-forge
using the [grayskull](https://conda.github.io/grayskull/) tool. You do not need to build the package specifically
for conda, conda-forge will build from your PyPI source distribution file (sdist).

:::
