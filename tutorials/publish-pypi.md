# Publish your Python package to PyPI

:::{todo}
- emphasize that we recommended the trusted publisher GitHub action for most maintainers
- Make sure they add /dist to their .gitignore file. We have not discussed GitHub workflows anywhere yet. Where does that fit?
- https://hatch.pypa.io/latest/intro/#existing-project <- hatch will migrate from setup.py for you - if we go with hatch then we may want to add this to the installable code lesson
:::


```bash
pipx install hatch
  installed package hatch 1.9.1, installed using Python 3.12.1
  These apps are now globally available
    - hatch
done! ✨ 🌟 ✨
```

:::

In the previous Python packaging lessons, you've learned:

1. What a Python package is
1. How to make your code installable.

:::{admonition} Learning Objectives
:class: tip

In this lesson you will learn how to:

- Build your package's source (sdist) and wheel distributions
- Setup an account on test PyPI (the process is similar for the real PyPI)
- Publish your package to test PyPI

You will do all of your development work in this lesson using [Hatch](https://hatch.pypa.io/latest/).

Once your package is on PyPI you can publish it to conda-forge (which is a channel on conda)
using [Grayskull](https://conda.github.io/grayskull/).

You will learn how to publish to conda-forge in a future lesson.

You will learn how to publish to conda-forge in the [next lesson](publish-conda-forge).


:::{figure-md} build-workflow-tutorial
<img src="../images/tutorials/publish-package-pypi-conda.png" alt="Graphic showing the high level packaging workflow. On the left you see a graphic with code, metadata and tests in it. Those items all go into your package. An arrow to the right takes you to a build distribution files box. Another arrow to the right takes you to a publish to PyPI box which has an arrow containing sdist and wheel that notes those files go to PyPI for hosting. From PyPI is an arrow containing sdist since you can then connect to conda-forge for an automated build that sends distributions from PyPI to conda-forge." width="700px">

You need to build your Python package in order to publish it to PyPI (or Conda). The build process organizes your code and metadata into a distribution format that can be uploaded to PyPI and subsequently downloaded and installed by users.
:::

## Test PyPI vs PyPI

There are two "warehouses" that you can use to publish
your Python package.

1. **[Test PyPI](https://test.pypi.org):** Test PyPI is a version of the PyPI repository that can be used for testing. This is a great place to practice and learn how to publish a package without taking up space on the real PyPI servers.
2. **[Real PyPI](https://pypi.org):** This is the PyPI "warehouse" where you can officially publish your Python package. IMPORTANT: only publish your package to PyPI when you are ready for it to be used by others and/or confident that it will become a package that you maintain. PyPI is not a place to practice learning how to publish a Python package.

The steps for publishing on test PyPI vs. real PyPI are the same with the
exception of a different url. Thus, in this lesson you will use test PyPI
to practice and learn.

## 4 Steps for publishing a Python package on PyPI

In this lesson you will learn how to publish your package to PyPI
using [Hatch](https://hatch.pypa.io/latest/). There are 4 things that
you need to do to publish your Python package:
to PyPI. You need to:

1. **Create a package development environment**
1. [**Build your package using `hatch build`**](../package-structure-code/python-package-distribution-files-sdist-wheel). Building a package is the process of turning your code into two types of distribution files: sdist and wheel. The wheel distribution file is particularly important for users who will `pip install` your package.
1. **Create an account on (test) PyPI**: You will need to create a PyPI account and associated token which provides permissions for you to upload your package.
1. **Publish to PyPI using `hatch publish`**

In a future lesson, you will learn how to create an automated
GitHub action workflow that publishes an updated
version of your package to PyPI every time you create a GitHub release.

:::{admonition} Learn more about building Python packages in our guide
:class: tip

- [Learn more about what building a Python package is](../package-structure-code/python-package-distribution-files-sdist-wheel)
- [Learn more about package distribution file that PyPI needs called the wheel](#python-wheel)
- [Learn more about the package distribution file that conda-forge will need on PyPI called the sdist (source distribution)](#python-source-distribution)

:::

## Step 1: Create a Python package development environment

The first step in building your package is to create a development environment. The Python environment will contain all of the dependencies needed to both install and work on your package.

Use Hatch to create your environment.

```bash
# This will create a default envt with your package installed in editable mode
> hatch env create
# If you have already created an environment this command will return Environment `default` already exists
```

Then view all of the current environments that hatch has access to:

```bash
> hatch env show
     Standalone
┏━━━━━━━━━┳━━━━━━━━━┓
┃ Name    ┃ Type    ┃
┡━━━━━━━━━╇━━━━━━━━━┩
│ default │ virtual │
└─────────┴─────────┘
```

Then activate the environment. Note that when you call a shell from a
Hatch environment, it will automatically install your package into the environment in development or editable mode.

```bash
# Hatch shell can be used to activate your environment
> hatch shell
... Installing project in development mode
source "/Path/to/env/here/hatch/env/virtual/pyosPackage/Mk7F5Y0T/sphinx-2i2c-theme/bin/activate"
```

View what's in the environment using `pip list`:

```bash
➜ pip list
Package         Version      Editable project location
--------------- ------------ ----------------------------------------------------
numpy           1.26.3
pandas          2.1.4
pip             23.3.1
pyosPackage     0.1.0        /path/to/your/project/here/pyosPackage
python-dateutil 2.8.2
pytz            2023.3.post1
six             1.16.0
tzdata          2023.4
```

At any time you can exit the environment using `exit`.

```bash
➜ hatch shell
source "/Users/leahawasser/Library/Application Support/hatch/env/virtual/pyospackage/twO2iQR3/pyospackage/bin/activate"

# Notice here you're in the (pyospackage) environment which is the default
pyosPackage (☊ main) [✎ ×1 ] is 📦 v0.1.4 via 🐍 pyenv (pyospackage)
➜ exit

pyosPackage (☊ main) [✎ ×1 ] is 📦 v0.1.4 via 🐍 pyenv took 43s
➜
```

### Hatch and environments

Behind the scenes when hatch creates a new virtual environment,
by default it uses venv[^venv] which is the default environment management tool that comes with Python installations.

Hatch will:

1. Create a new virtualenv (venv) that is located on your computer.
2. Install your package into the environment in editable mode (similar to `pip install -e`). This means it installs both your project and your project's dependencies as declared in your pyproject.toml file.

## Step 2: Build your package's sdist and wheel distributions

Once you have your development environment setup, you are ready to build your package using Hatch. Remember that building is the process of turning your Python package file structure into two distribution files:

1. The [wheel distribution](#python-wheel) is a pre-built version of your package. It useful for users as it can be directly installed using a tool such as `pip`. This file has the extension `.whl`.
2. The [source distribution](#python-source-distribution) contains the files that make up your package in an unbuilt format. This file will have the extension `.tar.gz`.

You will use Hatch as a **Front end** tool that builds
your package's sdist and wheel using the [hatchling](https://hatch.pypa.io/latest/) build back-end.
The hatchling build back-end is used because you declared it in your pyproject.toml file in the [previous lesson](installable-code).

To build your package run `hatch build`:

```bash
➜ hatch build
──────────────── sdist ─────────────────
dist/pyospackage-0.1.0.tar.gz
──────────────── wheel ─────────────────
dist/pyospackage-0.1.0-py3-none-any.whl

```

:::{admonition} Learn more about building a Python package
:class: tip
You can learn more about
building in the [build page of our packaging guide](../package-structure-code/python-package-distribution-files-sdist-wheel).
:::

The sdist is important if you wish to [publish
your package to conda-forge](publish-conda-forge). You will learn about this in a later lesson.

:::{todo}
➜ hatch build
────────────────────────────────────── sdist ──────────────────────────────────────
dist/pyospackage-0.1.0.tar.gz
────────────────────────────────────── wheel ──────────────────────────────────────
dist/pyospackage-0.1.0-py3-none-any.whl
:::

### <i class="fa-solid fa-wand-magic-sparkles"></i> Congratulations - you've created your Python package distribution files <i class="fa-solid fa-wand-magic-sparkles"></i>

You've now built your Python package and created your package distribution files. The next step is to setup
your account on testPyPI so you can publish your package.

## Step 3. Setup your test PyPI account

Next, you'll setup an account on Test PyPI. Remember that you
are using test PyPI here instead of the PyPI as a way to
safely learn how to publish a package without stressing the
real PyPI's servers.

:::{admonition} Test PyPI vs. PyPI
If you have a package that you are confident belongs on PyPI, all of the steps below will also work for you. When you publish using Hatch, you will call `hatch publish` to publish directly to PyPI instead of `hatch publish -r test` which publishes to Test PyPI.
:::

1. [Open up a web browser and go to the test PyPI website](https://test.pypi.org/).
2. [Create an account](https://test.pypi.org/account/register/) if you don't already have one. Be sure to store your password in a safe place!
3. Once you have an account setup, login to it.
4. Search on [https://test.pypi.org/](https://test.pypi.org/) to ensure that the package name that you have selected doesn't already exist. If you are using our test pyosPackage, then we suggest that you add your name or GitHub username to the end of the package name to ensure it's unique.

Example: `pyosPackage_yourNameHere`.

:::{todo}
Show them how to do this

1. update the project-name in the pyproject.toml file
2. update the module repository directory to be the same
:::

:::{figure-md} test-pypi-search
<img src="../images/tutorials/testpypi-search.png" alt="This is a screenshot of the test PyPI website. At the top in the search bar, you can see the search for pyosPackage. The search return says there were no results for pyosPackage Did you mean probpackage" width="700px">

Before you try to upload to test PyPI, check to see if the name of your package is already taken. You can do that using
the search box at the top of the test PyPI website.
:::

:::{admonition} Setup 2-factor (2FA) authentication

2-factor authentication is a secure login process that allows you to
use a backup device that only you can access to validate that the person logging in is really you. It addresses the issue of password phishing where someone else gains access to a password and can login to your account.

This matters on PyPI because someone could login to your account and upload a version of your package that has security issues. These issues will then impact all of your users when they download and install that version of the package.

2-factor authentication is required for PyPI authentication
as of 1 January 2024.
:::

## Step 4. Create a package upload token

To upload your package to PyPI, you will need to create a token. Ideally
this token is specific to the package that you are publishing.

However, if your package isn’t already on PyPI, then you will need to create a token for your account first and then create a package-specific token.

:::{admonition} Why create package-specific tokens?

It's ideal to create a package-specific token. When you create an account wide token this allows anyone with access to then access all of your PyPI projects. By creating a package specific token, you are limiting the scope of the token to only your specific package. This is just a safe way to set things up for you particularly if you are collaborating with others on package development.
:::

### Follow the steps below to create your token.

- Login to test PyPI and go to your account settings
- Scroll down to the **API tokens** section
- Click on the **Add API Token** button
  - If you are new to using PyPI and don't have any packages there yet, OR if you have other packages on PyPI but are uploading a new package, you will need to create an account-wide token.
- When you create your token, be sure to copy the token value and store it in a secure place before closing that browser.

Your token should look something like this:

`pypi-abunchofrandomcharactershere...`

It should start with `pypi` followed by a dash and a bunch of characters.

### Upload to PyPI using Hatch

Once you have your token, you are ready to publish to
PyPI.

- Run `hatch publish -r test`

`-r` stands for repository. In this case because you are publishing to test-PyPI you will use `-r test`. Hatch will then ask for a username and credentials.

- Add the word `__token__` for your username. This tells Test PyPI that you are using a token value rather than a username.
- Paste your PyPI token value in at the `Enter your credentials` prompt:

```bash
❯ hatch publish -r test
Enter your username: __token__
Enter your credentials: <past-your-token-value-here>
dist/pyospackage-0.1.0-py3-none-any.whl ... already exists
dist/pyospackage-0.1.0.tar.gz ... already exists

```

If your credentials are valid, and you have already run `hatch build`
and thus have your 2 distribution files in a `dist/` directory then
Hatch will publish your package to test PyPI.

Hatch also has a caching system so once you enter your credentials it
will remember them.

## Install your package from test PyPI

Once your package upload is complete, you can install it from
test PYPI. You can find the installation instructions on the test PyPI
landing page for your newly uploaded package.

:::{figure-md} testpypi-landing-page
<img src="../images/tutorials/test-pypi-package.png" alt="A screenshot of the test PyPI page for pyosPackage. It says pyosPackage 0.1.0 at the top with the pip install instructions below. The landing page of the package has information from the package's README file. " width="700px">

This is an example landing page for the pyosPackage that was just uploaded. Notice at the top of the page there is instruction for how to install the package from test PyPI. You can simply copy that code and use it to install your package from testPyPi locally.
:::

As an example, [check out our pyOpenSci pyosPackage landing page on test PyPI](https://test.pypi.org/project/pyosPackage/). Notice that
the page has information about the current package version and also
installation instructions as follows:

`pip install -i https://test.pypi.org/simple/ pyosPackage`

:::{important} Publishing to test.PyPI.org vs PyPI.org
While you can install from test PyPI it's not recommended that you publish to
testPyPI as a permanent way to install your package. Test PyPi is a perfect place to learn how to publish your package. But your end goal should be to publish to PyPI.org once you have figured out your workflow.
:::

### Time to install your package

- On your computer, activate the development environment that
  you wish to install your newly published package in.
- Run the installation instructions for your package from test PyPI.

::::{tab-set}

:::{tab-item} Conda

```bash
> conda activate pyospkg-dev
> pip install -i https://test.pypi.org/simple/ youPackageNameHere
> conda list
```

:::

:::{tab-item} venv mac / Linux

```bash
> hatch shell
> pip install -i https://test.pypi.org/simple/ youPackageNameHere
> pip list
:::
::::


:::{admonition} The value of end-to-end tools like hatch, flit and poetry
In this lesson you are using Hatch and hatchling to create, build and publish your Python Package. [Click here to learn about other packaging tools in the ecosystem.](../package-structure-code/python-package-build-tools.md)
:::

:::{todo}
teach them to setup trusted publisher for actions... in the actions lesson
https://pypi.org/help/#twofa

from PyPI: https://pypi.org/help/#apitoken - You can create a token for an entire PyPI account, in which case, the token will work for all projects associated with that account. Alternatively, you can limit a token's scope to a specific project.
:::

## Package-specific token vs trusted publisher

For long run maintenance of your package, you have two options
related to PyPI publication.

1. You can create a package-specific token which you will use to publish your package (manually) to PyPI. This is a great option if you don't wish to automate your PyPI publication workflow.
2. You can also create an automated publication workflow on GitHub using GitHub actions. This is a great way to make the publication process easier and it also supports a growing maintainer team. In this case we suggest you don't worry about the token and instead setup a specific GitHub action that publishes your package when you make a release. You can then create a "trusted publisher" workflow on PyPI.

You will learn how to create the automated trusted publisher workflow in a followup lesson.


### OPTIONAL: If you want to use a manual token-based publication workflow

If you plan to use your token regularly to publish to PyPI, we strongly recommend going through the above steps again to create
a token specific to your new package.

To do this:
1. Go to test PyPI
1. Navigate to the "Your Projects" section of your account
2. Click on the manage button for the project that you wish to add a token for
3. Go to settings
4. Click on "Create a token for your-package-name-here"
5. Create the token and follow the steps above publish your package using the repository specific token.

And you're all done!

## You have published your package to (test) PyPI!

Congratulations. You have now successfully published your package to test PyPI. If you have a package that is ready for real-world use on the real PyPI, then you can follow the same steps to publish it on PyPI.org.

Once you publish on PyPI.org, you can then easily add your package to the conda-forge ecosystem using the [grayskull](https://conda-forge.org/blog/posts/2020-03-05-grayskull/) tool.

You will learn how to do that in the next lesson.




## Footnotes

[^venv]: https://docs.python.org/3/library/venv.html
```
