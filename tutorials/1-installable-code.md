# Make your Python code pip installable

The first step in creating a Python package based on code that you
have is to make that code pip installable. You will learn how to make
your code pip installable in this lesson.

<!--
TODO: is it clear where to add commands? bash vs. python console

Bash vs zsh is different
does this work on windows and mac? i know it works on mac/linux
-->

:::{figure-md} code-to-script

<img src="../images/tutorials/code-to-script-diagram.png" alt="Diagram showing the basic steps to creating an installable package. There are 4 boxes with arrows pointing towards the right. The boxes read, your code, create package structure, add metadata to pyproject.toml and pip install package." width="700px">

A basic installable package needs a few things: code, a specific package structure and a `pyproject.toml` containing your package's name and version. Once you have these items in the correct directory structure, you can pip install your package into any environment on your computer.
:::

:::{admonition} Learning Objectives
:class: tip

In this lesson you will learn:

- How to make your code pip-installable into a Python environment
- How to create a basic `pyproject.toml` file to declare dependencies and metadata
- How to declare a build backend which will be used to build and install your package (learn more about what build back ends are here - link to guide)
- How to install your package in editable mode for interactive development

To complete this lesson you will need a local Python (development)
environment. You are welcome to use any environment manager that you choose.

* [If you need guidance creating a Python environment, review this lesson](extras/1-create-environment.md) which walks you through creating an environment using both `venv` and `conda`.
* If you aren't sure which environment manager to use and
you are a scientist, we suggest that you use `conda`.
:::

## Make your package installable


:::{figure-md} packages-environment

<img src="../images/tutorials/environment-package-install.png" alt="This diagram has two smaller boxes with arrows pointing to the right to a python environment. The small boxes read your-package and pip install package. The environment box on the right reads - your python environment. It them lists your-package along with a few other core packages such as matplotlib, numpy, pandas, xarray and geopandas." width="700px">

Making your code pip installable is the first step towards creating a Python package. Once it is pip installable, you can add it to any Python environment on your computer and import that package in the same way that you might import a package such as `Pandas` or `Geopandas`.
:::

## Make a basic Python package

It’s time to create the most basic version of a Python package.
While this code can't be yet published to PyPI or conda and
is not documented, it will be installable on your computer or
anyone elses.

### What does a basic package directory structure look like?
To make your code installable you need:

- A `pyproject.toml` file
- An (optional but recommended) `__init__.py` file in your code directory
- A specific directory structure
- Some code.

The directory structure you’ll create in this first section looks like this:

```bash
pyospackage/
     └─ pyproject.toml
     └─ src/  # The src directory ensures your tests always run on the installed
             └── pyospackage/ # Package directory where code lives, use the package name
              	      ├── __init__.py
                      ├── add_numbers.py
                      └── # Add any other .py modules that you want here
```

Below, you will learn about each element of the above package structure.

### About the basic package directory structure

Notice a few things about the above layout:

1. Your package code lives within a `src/packagename` directory. We suggest that you use `src/` directory as it ensure you are running tests on the installed version of your code. However, you are welcome to instead use a [flat layout](https://www.pyopensci.org/python-package-guide/package-structure-code/python-package-structure.html#about-the-flat-python-package-layout) which does not have a src/ directory at the root. [Learn more here.](https://www.pyopensci.org/python-package-guide/package-structure-code/python-package-structure.html#the-src-layout-and-testing)
2. Within the `src/` directory you have a package directory called `pyospackage/`. Use the name of your package for that directory name.
3. In your package directory, you have an `__init__.py` file and all of your Python modules.
4. The `pyproject.toml` file lives at the root directory of your package.

## Init.py and pyproject.toml files

The `__init__.py` and `pyproject.toml` files in the above layout
are important to understand. More on that below.

### What is an init.py file?

The `__init__.py` file tells Python that the directory it’s in should be treated as a Python package.
The `__init__.py` file also:

- Allows you to organize multiple modules within the package.
- Allows you to create shortcuts for importing specific functions, and classes into your code (more on that later!)
- Allows you to create a version object for people to call **version**

:::{admonition} The **init**.py file
:class: tip

Since Python 3.3 came out, you can install a package without an `__init__.py` file. However, we suggest that you include it in your package structure as it allows you to customize your package’s user experience.
:::

### What is a pyproject.toml file?

The **pyproject.toml** file is:

- Where you store your project’s metadata (including its name, authors, license, etc)
- Where you store dependencies (the packages that it depends on)
- Used to specify and configure what build back end you want to use to build your package distributions that are used for PyPI publication.

After the `__init__.py` and `pyproject.toml` files have been added, your package can be built and distributed as an installable Python package using tools such as pip. Note that the `pyproject.toml` file needs to have the a few basic items defined for it to be installable including:

- The `build-backend` that you want to use,
- The project `name` and `version`.

:::{admonition} Why the pyproject.toml file is important
:class: tip

The `pyproject.toml` file replaces some of the functionality of both the setup.py file and setup.cfg files.
If you try to pip install a package with no `pyproject.toml` you will get the following error:

```bash
GitHub/pyospackage/testme
➜ pip install .
ERROR: Directory '.' is not installable.
Neither 'setup.py' nor 'pyproject.toml' found.
```

:::

## Try it yourself - Create your package!

Now that you understand the basics, it's time to create a Python package! Below you will create a directory structure similar to the structure described above.

If you don’t wish to create each of the files and directories below, you can always [fork and clone and customize the pyOpenSci example package, here.](https://github.com/pyOpenSci/pyosPackage)

### Step 1: Set Up the Package Directory Structure

Create a new directory for your package. Choose a name for your package, preferably in lowercase and without spaces (e.g., "pyospackage_yourname").

Inside the package directory,

- Create a `src/` directory
- Within the `src/` directory, create a directory that is named after your package. This subdirectory will contain your package’s code.
- It is ok if the main directory of your package and the directory in `src/` have the same name

Next create two files:

- Inside the package directory, create a new file named `__init__.py` . This file ensures Python sees this directory as a package. You will use this file to customize how parts of your package are imported and to declare your package’s version in a future lesson.
- At the root of your directory, create a file called `pyproject.toml`

Your final package directory structure should look like this:

```
pyospackage/
     └─ pyproject.toml
     └─ src/
             └── pyospackage_yourname/
              	     ├── __init__.py
```

### Step 2: Add code to your package

Within the `pyospackage` subdirectory, add 1 or more Python modules
(.py files) containing the code that you want your package to access and run.
If you don't have code already and are just learning how to
create a Python
package, then create an empty `add_numbers.py` file.

:::{admonition} Python modules and the __init__.py file
:class: tip

When you see the word module, we are referring to a `.py` file containing Python
code.

The _init_.py  allows Python to recognize that a directory contains at least one
module that may be imported and used in your code. A package can have multiple
modules.

[Learn more about Python packages and modules in the python documentation.](https://docs.python.org/3/tutorial/modules.html#packages )

:::

```
pyospackage/
     └─ pyproject.toml
     └─ src/
             └── pyospackage/
              	    ├── __init__.py
                    ├── add_numbers.py

```

### Step 3. Add code to your `add_numbers` module

If you are following along and making a Python package from scratch then you can add the code below to your `add_numbers.py` module. The function below adds two integers together and returns the result. Notice that the code below has a few features that we will review in future tutorials:

1. It has a [numpy-style docstring ](https://www.pyopensci.org/python-package-guide/documentation/write-user-documentation/document-your-code-api-docstrings.html#three-python-docstring-formats-and-why-we-like-numpy-style)
2. It uses [typing](https://www.pyopensci.org/python-package-guide/documentation/write-user-documentation/document-your-code-api-docstrings.html#adding-type-hints-to-your-docstrings)

If you aren’t familiar with docstrings or typing yet, that is ok. We will get
to it later in our tutorial series. Or, you can review the pyOpenSci [packaging guide](https://www.pyopensci.org/python-package-guide/documentation/write-user-documentation/document-your-code-api-docstrings.html)
for an overview.

```python
def add_num(a: int, b: int) -> int:
    """
    Add two numbers.

    Parameters
    ----------
    a : int
        The first number to be added.
    b : int
        The second number to be added.

    Returns
    -------
    int
        The sum of the two input numbers (a + b).

    Examples
    --------
    >>> add_num(3, 5)
    8
    >>> add_num(-2, 7)
    5
    """
    return a + b
```

### Step 4. Add metadata to your `pyproject.toml` file

Next, you will add some metadata (information) to your `pyproject.toml` file. You are
are welcome to copy the file we have in our example repo here.

:::{admonition} Brief overview of the TOML file
:class: tip

The TOML format consists of tables and variables. Tables are sections of information denoted by square brackets:

`[this-is-a-table]`.

Tables can contain variables within them defined by an variable name and
an `=` sign. For
instance, a `build-system` table most often holds 2 variables:

1. `requires = `, which tells a build tool what tools it needs to install prior to building your package. in this case is
   [hatchling](https://pypi.org/project/hatchling/)
2. `build-backend` is used to define specific build-backend name, (in this example we are using `hatchling.build`).

TOML organizes data structures, defining relationships within a configuration
file. You will learn more about the `pyproject.toml` format in the
[next lesson when you add additional metadata / information to this file.](5-pyproject-toml.md)

```toml
# An example of the build-system table which contains two variables - requires and build-backend
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

[Learn more about the pyproject.toml format here.](../package-structure-code/pyproject-toml-python-package-metadata)
:::

- Open up your `pyproject.toml` file in your favorite text editor.
- Add the metadata below to your `pyproject.toml`

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "pyospackage_gh_user_name" # rename this if you plan to publish to test PyPI
# Here you add the package version manually. You will learn how to setup # dynamic versioning in a followup tutorial.
version="1.1"

```

Note that above you manually add your package's version number to the
`pyproject.toml` file. You will learn how to automate defining a package
version using git tags in the version and release your package lesson. <ADD LINK>

:::{admonition} The bare minimum needed in a pyproject.toml file
:class: tip

The core basic information that you need in a `pyproject.toml` file in order to publish on PyPI is your **package's name**  and the **version**. However, we suggest that you flesh out your metadata early on in the `pyproject.toml` file.

Once you have your project metadata in the pyproject.toml file, you will
rarely update it. In the next lesson you’ll add more metadata and structure to this file.
:::

### Step 5. Install your package locally

At this point you should have:

1. A project directory structure with a `pyproject.toml` file at the root
2. A package directory containing an empty `__init__.py` file and
3. At least one Python module (e.g. `add_numbers.py`)

You are now ready to install (and build) your Python package!

Let’s try it out.

- First open bash and `cd` into your package directory
- Activate the Python environment that you wish to use. If you need help with working with virtual environments [check out this lesson](extras/1-create-environment.md).
- Finally run `python -m pip install -e .`

```bash
# Activate your environment using conda or venv
# Below we use conda but you can do the same thing with venv!
> conda activate pyosdev
(pyosdev)
>> conda info
    active environment : pyosdev
    active env location : /Users/your-path/mambaforge/envs/pyosdev
# Install the package
>> python -m pip install -e .

Obtaining file:///Users/leahawasser/Documents/GitHub/pyos/pyosPackage
  Installing build dependencies ... done
  Checking if build backend supports build_editable ... done
  Getting requirements to build editable ... done

# Check to see if the package is installed
> conda list
# use pip list instead of conda list here if you are working in an venv environment rather than a conda envt
```

:::{admonition}  What does `pip install -e .` do?
:class: tip

Let's break down `pip install -e .`

`pip install -e .` installs your package into the current active
Python environment in **editable mode** (`-e`). Installing your package in
editable mode, allows you to work on your code and then test the updates
interactively in your favorite Python interface. One important caveat of editable mode is that every time you update your code, you may need to restart your Python kernel.

If you wish to install the package regularly (not in editable
mode) you can use:

- `python -m pip install . `

**Using `python -m` when calling `pip`**

Above, you use`python -m` to call the version of pip installed into your
current active environment. `python -m` is important to ensure that you are
calling the version of pip installed in your current environment.
:::

#### Look for pyospackage in your environment

Once you have installed your package, you can view it in your current
environment. If you are using `venv` or `conda`, `pip` list will allow you
to see your current package installations.

Note that because pyospackage is installed in editable mode (`-e`) pip will show you the past to where you package installation's code
is.

```bash
$ pip list

➜ pip list
Package                       Version        Editable project location
----------------------------- -------------- --------------------------------------------------------------
...
arrow                         1.2.3
...
...
mamba                         1.1.0
markdown-it-py                2.2.0
MarkupSafe                    2.1.2
matplotlib                    3.7.1
msgpack                       1.0.5
mypy                          1.4.1
nox                           2021.10.1
numpy                         1.24.2
packaging                     23.0
pandas                        1.5.3
pyosPackage                   0.1.0          /Users/yourusername/path/here/pyosPackage
...
...
...
```

### 6. Test out your new package

After installing your package, type “python” at the command prompt to start
a Python session in your active Python environment.

You can now import your package and access the `add_num` function.

```bash
➜ python
Python 3.11.4 | packaged by conda-forge | (main, Jun 10 2023, 18:08:41) [Clang 15.0.7 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import pyospackage
>>> pyospackage.add_num(1, 2)
3
```

<!-- As you review - please tell me what you think about the section below.
There were some various opinions on whether to surface specific functionality
in a package. i've found it useful in my work when done thoughtfully.

But for beginners it could create more confusion if we don't provide
specific use-cases for doing this. Thoughts? -->


## OPTIONAL: Customize access to Python functions using the `__init__.py` file

Let's make one more tweak to the code.

If `add_num` is a function that you think users will use often, you may want to add it to your `__init__.py` file to allow them to import the function directly from the package rather than from the module.

### Add functions to your `__init__.py` file

To make a function or class available at the package level to a user, you can add it to the `__init__.py` file.

- Open the `__init__.py` file .
- At the top of the file add the import below.

```python
from pyospackage.add_numbers import add_num
```

Save the file.

Now, open up a NEW Python terminal or restart your Python kernel.

:::{admonition} Don't forget to restart your Python kernel!
:class: important

It's important that you restart your Python kernel if you wish to access the changes to your code that you just made.
:::

```python
> python
Python 3.10.12 | packaged by conda-forge | (main, Jun 23 2023, 22:41:52) [Clang 15.0.7 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from pyospackage import add_num
>>> add_num(1,2)
3
```

The decision to add specific functions, methods or classes to your
`__init__.py` file is up to you. However be sure that you do this thoughtfully
considering what functionality in your package you want to "elevate" to the top
level vs. what makes the most sense to keep in individual modules.

### Congratulations! You created (the beginning of) your first Python package

You did it! You have now created a Python package that you can install into any Python environment. While there is still more to do, you have completed the first major step.

In the upcoming lessons you will:

* Add a [README file](2-add-readme.md) and [LICENSE ](4-add-license-file.md) to your package
* [Add more metadata to your `pyproject.toml`](5-pyproject-toml.md) file to support PyPI publication.
* [Learn how to build your your package distribution](6-publish-pypi.md) files (**sdist** and **wheel**) and publish to **test PyPI**.
* Finally you will learn how to publish to **conda-forge** from **PyPI**.

If you have a package that is ready for the mainstream user then
you can also publish your package on PyPI.
