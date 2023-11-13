# Publish your Python package to PyPI

:::{figure-md} build_workflow-tutorial
<img src="../images/python-package-development-process.png" alt="Graphic showing the high level packaging workflow. On the left you see a graphic with code, metadata and tests in it. those items all go into your package. Documentation and data are below that box because they aren't normally published in your packaging wheel distribution. an arrow to the right takes you to a build distribution files box. that box leads you to either publishing to testpypi or the real pypi. from pypi you can then connect to conda forge for an automated build that sends distributions from pypi to conda-forge. " width="700px">

You need to build your Python package in order to publish it to PyPI (or Conda). The build process organizes your code and metadata into a distribution format that can be uploaded to PyPI and subsequently downloaded and installed by users. NOTE: you need to publish a sdist to PyPI in order for conda-forge to properly build your package automatically.
:::

<!-- Pypa resource: https://packaging.python.org/en/latest/tutorials/packaging-projects/#uploading-the-distribution-archives
https://spdx.org/licenses/PSF-2.0.html (double check that we can use language from pypa tutorial??


https://packaging.python.org/en/latest/guides/using-testpypi/

-->

In the previous lessons, you've learned the following:

1. How to structure your code into a package like format that can be installed into a Python environment.
2. How to add a `README` and `LICENSE` file to your package
3. How to setup your `pyproject.toml` file with all of the metadata that PyPI requires and also metadata that will be helpful for users to find your package.

If you have gone through all of the above lessons, you are now ready to
build your package's distribution files which are needed for you to publish
to PyPI. Here, you will learn how to set things up on
PyPI and how to manually publish to (test) PyPI using twine.

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

## 3 Steps for publishing a Python package on PyPI

There are 3 things that you need to do to publish your Python package
to PyPI. You need to:

1. [build your package](../package-structure-code/python-package-distribution-files-sdist-wheel). Building a package is the process of turning your code into 2 distribution files - called an sdist and a wheel. These files are what PyPI needs to publish your package . <!--technically it only needs one of the files ... maybe a breakout?? and a note about sdist file size and checking it particularly important for conda-forge...  -->
2. You need to create an account on (test) PyPI if you don't already have one and a token which provides permissions for you to upload your package.
3. Once you have both of the above done, you are ready to use `twine` to publish your package!

<!-- It would be cool to have a graphic outlinting this process of
build and then publish to pypi and conda -->

<!-- Todo this might be a nice grid on this page or buttons.. soemthing visual -->

- [Learn more about building here](../package-structure-code/python-package-distribution-files-sdist-wheel)
- [Learn more about the wheel](../package-structure-code/python-package-distribution-files-sdist-wheel#wheel-whl-files)
- [Learn more about the sdist (source distribution)](../package-structure-code/python-package-distribution-files-sdist-wheel#source-distribution-sdist)

## Step 1: Build your package's sdist and wheel distributions

To begin you will need to create your package's sdist and wheel distribution 
files. 

1. You will build your package locally and then 
2. Push your package to PyPI using twine. 

The first time you publish your package to PyPI you will do it manually. 
After that you can opt to create a automated workflow that publishes an updated 
version of your package to PyPI every time you create a release on GitHub. 

1. activate your development environment if it is not already active. 
2. install your package requirements if you haven't already. based on the pypoject toml 

`pip install -e .[dev]`
3. You are now ready to build your package! Note that here you are using the [PyPA build tool](https://github.com/pypa/build) as a "Front end" tool that builds
your package's sdist and wheel using the hatchling build back end. Remember that you defined your build backend here in the build system table of your pyproject.toml file. So build knows to use [hatchling](https://hatch.pypa.io/latest/).  
To build your package run:

`python -m build`

```bash
❯ python -m build
* Creating virtualenv isolated environment...
* Installing packages in isolated environment... (hatchling)
* Getting build dependencies for sdist...
* Building sdist...
* Building wheel from sdist
* Creating virtualenv isolated environment...
* Installing packages in isolated environment... (hatchling)
* Getting build dependencies for wheel...
* Building wheel...
Successfully built pyospackage-0.1.0.tar.gz and pyospackage-0.1.0-py3-none-any.whl
```
When you build your package, it will create two output "files". A .whl or wheel file and a .tar.gz compressed file. 

You can learn more about both of these distribution files here. <link to the packaging page on sdist and wheel where we show the structure of each>
```
dist/pyospackage-0.1.0-py3-none-any.whl
dist/pyospackage-0.1.0.tar.gz
```

The above two files are what you will need to publish your package to PyPI. The tar.gz file is particularly important if you wish to publish your package to conda-forge. You'll learn more about that in this lesson. <TODO: link to conda forge lesson when it's there>

### Time to celebrate! 

you've now created your package distrbution! you're on your way to publishing your package on PyPI. 
 
## Step 2:


Next, you'll setup an account on testPyPI. we are using testPyPi for now as a way to safely learn how to publish a package to PyPI within filling the real PyPI up with lots of "test" packages used to learn. 

:::{admonition} Test vs real pypi
IF you have a package that you are confident belongs on the real PyPI. All of the steps below will also work for you with slight modifications which will be noted below. 
:::

1. [go to test pypi](https://test.pypi.org/) and [create an account](https://test.pypi.org/account/register/) if you don't already have one. If you have an account login to it now. 

2. Search on PyPI to ensure that the package name that you have selected doesn't already exist. If you are using our test pyosPackage, then we suggest that you add your name or github username to the end of the package name to ensure it's unique. Example: pyosPackage_yourNameHere. 

Set password
You can set the password locally if you wish to publish locally. To do this

2. Create a pypi account
   Create a new token - if the package isn’t already on pypi you may have to create a token for your account at first before you publish
   Once you have created that token and successfully uploaded the project to pypi, you can then create a project specific token for your package. <i believe this is better as then others can use it?? Or atleast it’s not attached to a single user if there are multiple maintainers>
   If you do that be sure to go back after and create one for just your package…

pdm config repository.pypi.password

Start with test pypi for experience
