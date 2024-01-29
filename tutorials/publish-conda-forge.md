# Publish your Python package that is on PyPI to conda-forge

In the previous lessons, you've learned:

1. How to [create the most basic version of a Python package](1-installable-code.md). This entailed making your code installable.
2. [How to publish your Python package to PyPI](publish-pypi)
2. How to add a `README` and `LICENSE` file to your package
3. How to setup your `pyproject.toml` file with all of the metadata that PyPI requires and also metadata that will be helpful for users to find your package.

If you have gone through all of the above lessons, you are now ready to
publish your package on conda-forge.

**IMPORTANT:** Please do not practice publishing your package to conda-forge. You should only publish to conda-forge when you have a package on pypi.org that you plan to maintain.


:::{admonition} Learning Objectives
:class: tip

In this lesson you will learn how to:

- How to build your package's sdist and wheel distributions
- Setup an account on testPyPI (the process is similar for the real PyPI)
- Publish your package to PyPI

Once your package is on PyPI you can then easily publish it to conda-forge
using the [grayskull](https://conda.github.io/grayskull/) tool. You do not need to build the package specifically
for conda, conda-forge will build from your PyPI source distribution file (sdist).

:::



:::{figure-md} pypi-conda-channels

<img src="../images/publish-python-package-pypi-conda.png" alt="Image showing the progression of creating a Python package, building it and then publishing to PyPI and conda-forge. You take your code and turn it into distribution files (sdist and wheel) that PyPI accepts. then there is an arrow towards the PyPI repository where ou publish both distributions. From PyPI if you create a conda-forge recipe you can then publish to conda-forge. " width="700px">

Once you have published both package distributions (the source distribution and the wheel) to PyPI, you can then publish to conda-forge. Conda forge requires an source distribution on PyPI in order to build your package on conda-forge. You do not need to rebuild your package to publish to conda-forge.
:::

## What is conda forge?
conda is an open source package and environment management tool that
can be used to install tools from the different channels within the Anaconda Cloud repository.

You can think about a channel as a specific location where a group of packages are stored and can be installed from using a command such as `conda install packagename`. In the case of the Anaconda cloud channels, some of these channels such as the default channel, is managed by Anaconda. Only Anaconda can decide what packages are available in the default channel. However, the conda-forge (and bioconda) channel are community-managed channels.
Anyone can upload a package to these channels.

[Learn more about conda channels here.](#about-conda)

:::{todo}
Make a graphic to replace that geohackweek graphic that is also more specific.
:::

:::{figure-md} pypi-conda-channels

<img src="../images/python-pypi-conda-channels.png" alt="Graphic with the title Python package repositories. Below it says Anything hosted on PyPI can be installed using pip install. Packaging hosted on a conda channel can be installed using conda install. Below that there are two rows. the top row says conda channels. next to it are three boxes one with conda-forge, community maintained; bioconda and then default - managed by the anaconda team. Below that there is a row that says PyPI servers. PyPI - anyone can publish to pypi. and test pypi. a testbed server for you to practice. " width="700px">

Conda channels represent various repositories that you can install packages from. Because conda-forge is community maintained, anyone can submit a recipe there. PiPY is also a community maintained repository. Anyone can submit a package to PyPI and test PyPI. Unlike conda-forge there are no manual checks of packages submitted to PyPI.
:::



## Why publish to conda forge

There are many users, especially in the scientific ecosystem that use conda as their primary package manager / environment tool. Thus, having packages available to these users on the conda-forge channel is useful. In some cases packages on conda-forge can minimize dependency conflicts that can occur when mixing installations using pip and conda. This is particularly important for the spatial ecosystem.

## How publishing to conda-forge works

Once you have built and published your package to PyPI, you have everything that you need to publish to conda-forge. There is no additional build step needed to publish to conda-forge.

Conda-forge will build your package from the source distribution which you [published to PyPI in the previous lesson](publish-pypi) using the recipe that you will create below.

:::{todo}
<graphic for this???>
:::


### Conda-forge publication steps

The high steps to publish to conda-forge are you will walk through below are:

1. Publish your Python package distribution files (sdist & wheel) to PyPI
2. Create a conda-forge recipe, which is a yaml file with instructions on how to build your package on conda-forge, using the grayskull[^grayskull] package.
3. Submit the recipe (yaml file) to the conda-forge staged recipes repository as a pull request for review.

:::{todo}
Here is an example of what a pull request for a conda-forge recipe looks like.

Create screen shot of a staged recipe
:::

4. Once someone from the conda-forge team reviews your pull request, you may need to make some changes. Eventually the pull request will be approved and merged.

Now your package is on conda-forge.

You only create the recipe once. Then you just maintain the repository.


## Maintaining a conda-forge package

Once your package is on conda-forge, the repository will track activity on your PyPI repository for that package. Any time you make a new release to PyPI with a new source distribution, conda-forge will build and update your conda-forge repository.

When that happens, conda-forge will create a new pull request with an updated distribution recipe.

You can review that pull request and then merge it once all of the tests pass.

## Publish your package to conda-forge

It's time to add your package to the conda-forge channel.
Remember that your package needs to be on PyPI before the steps below will work. And also remember that the team managing conda-forge are all volunteers.

* Please only submit your package to conda-forge if you intend to maintain it over time.
* Be sure that your package is on PyPI.org (not test.pypi.org) before you attempt to publish to PyPI.

### Step 1 - Install grayskull

To begin this process you need to [install grayskull](https://conda.github.io/grayskull/user_guide.html). You can install it using either pip

```
pip install grayskull
```

or conda

```
conda install -c conda-forge grayskull
```

Use the shell / terminal that you have been using to run hatch
commands in the previous tutorials.

### Step 2: Create your recipe from PyPI

Next, you can run grayskull on your package.

Grayskull will pull information from PyPI
You don't need to work about what directory you are in when you run grayskull. Grayskull will look for your package on PyPI and will generate your recipe from the PyPI distribution.

Because it is pull from pypi.org, an internet connection is needed for this step.

Run the command below in your favorite shell.

```bash
➜ grayskull pypi pyospackage

#### Initializing recipe for pyospackage (pypi) ####

Recovering metadata from pypi...
Starting the download of the sdist package pyospackage
pyospackage 100% Time:  0:00:00   1.2 MiB/s|###########################|
Checking for pyproject.toml
pyproject.toml found in /var/folders/r8/3vljpqb55psbgb1ghc2qsn700000gn/T/grayskull-pyospackage-du0sf_a4/pyospackage-0.0.1/pyproject.toml
Recovering information from setup.py
Executing injected distutils...
Checking >> -- 100% |#                          |[Elapsed Time: 0:00:00]
Matching license file with database from Grayskull...
Match percentage of the license is 97%. Low match percentage could mean that the license was modified.
License type: BSD-3-Clause
License file: ['LICENSE']
Build requirements:
  <none>
Host requirements:
  - python
  - hatchling
  - pip
Run requirements:
  - python

RED: Missing packages
GREEN: Packages available on conda-forge

Maintainers:
   - lwasser

#### Recipe generated on /your/file/package/here/pyosPackage for pyospackage ####
```

When you run grayskull, it will grab the latest distribution of your package from PyPI and will use that to create a new recipe.

The recipe will be saved in a directory named after your package's name, wherever you run the command.

`packagename/meta.yaml`

At the very bottom of the grayskull output, it will also tell you
where it saved the recipe file.

This will create a meta.yaml file that looks like the example below:

```yaml
{% set name = "pyospackage" %}
{% set version = "0.0.1" %}

package:
  name: {{ name|lower }}
  version: {{ version }}

source:
  url: https://pypi.io/packages/source/{{ name[0] }}/{{ name }}/pyospackage-{{ version }}.tar.gz
  sha256: 43ec82da3a10752a5dbf2f0ef742e357803a3ddb400005f87e86534685bfb8a7

build:
  noarch: python
  script: {{ PYTHON }} -m pip install . -vv --no-deps --no-build-isolation
  number: 0

requirements:
  host:
    - python
    - hatchling
    - pip
  run:
    - python

test:
  imports:
    - pyospackage
  commands:
    - pip check
  requires:
    - pip

about:
  license: BSD-3-Clause
  license_file: LICENSE

extra:
  recipe-maintainers:
    - lwasser

```

### Step 3: tests for conda-forge

Next, have a look at the tests section in your meta.yaml file. At a minimum you should import your package and run `pip check`.

`pip check` will ensure that your package installs properly with all of the proper dependencies.

```yaml
test:
  imports:
    - pyospackage # Test importing the package into a python environment
  commands:
    - pip check # check the package
  requires:
    - pip
```
### Step 4: Submit a pull request to the staged-recipes repository

Finally, create a pull request in the staged-recipes GitHub repository.

When you do this, a suite of CI actions will run that build and test the build of your package. A conda-forge maintainer will work with you to get your recipe in good shape and merged.

You can follow the [instructions here](https://conda-forge.org/docs/maintainer/adding_pkgs.html) to submit your package

To create your pull request:

1. Fork and clone this repo: https://github.com/conda-forge/staged-recipes
1. Create a branch in your fork rather than submitting from the main branch of your fork.
1. Within your fork's branch, create a new directory with the name of your package, and add your meta.yaml file to it.

`staged-recipes/recipes/<name-of-package>/meta.yaml`

1. Submit the pull request
1. Remember that the conda-forge maintainers are volunteers. Be patient for someone to respond and supportive in your communication with them.


```yaml
test:
  imports:
    - pyospackage
  commands:
    - pip check
  requires:
    - pip
```

## Maintaining

<Create a pr on conda-forge - tag filipe (as it is a test package) and add screenshots here so people understand what maintaining a conda recipe entails >

## Footnotes

[^grayskull]: [Grayskull blogpost](https://conda-forge.org/blog/2020/03/05/grayskull/)
