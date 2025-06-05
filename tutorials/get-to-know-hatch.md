---
:og:description: Get started with Hatch, a modern Python packaging tool. This lesson introduces Hatch’s features and shows how it simplifies environment management, project scaffolding, and building your package.
:og:title: Get to Know Hatch
---

# Get to Know Hatch

Our Python packaging tutorials use the tool
[Hatch](https://hatch.pypa.io/latest/). While there are [many great packaging
tools](/package-structure-code/python-package-build-tools) out there, we have
selected Hatch because:

1. It is an end-to-end tool that supports most of the steps required to create
   a quality Python package. Beginners will have fewer tools to learn if they
   use Hatch.
2. It supports different build back-ends if you ever need to compile code in
   other languages.
3. As a community, pyOpenSci has decided that Hatch is a user-friendly tool that
   supports many different scientific Python use cases.

In this tutorial, you will install and get to know Hatch a bit more before
starting to use it.

You need two things to successfully complete this tutorial:

1. You need Python installed.
2. You need Hatch installed.

:::{important}
If you don't already have Python installed on your computer, Hatch will do it
for you when you install Hatch.
:::

## Install Hatch

To begin, follow the operating-system-specific instructions below to install
Hatch.

::::{tab-set}

:::{tab-item} MAC

Follow the instructions [here](https://hatch.pypa.io/latest/install/#installers).

* Download the latest GUI installer for MAC [hatch-universal.pkg](https://github.com/pypa/hatch/releases/latest/download/hatch-universal.pkg).
* Run the installer and follow the setup instructions.
* If your terminal is open, then restart it.

:::

:::{tab-item} Windows

* In your browser, download the correct `.msi` file for your system:
[hatch-x64.msi](https://github.com/pypa/hatch/releases/latest/download/hatch-x64.msi)
* Run your downloaded installer file and follow the on-screen instructions.

:::

:::{tab-item} Linux

We suggest that you install Hatch using pipx on Linux.
however, if you prefer another method, check out the [Hatch installation documentation](https://hatch.pypa.io/latest/install/) for other methods.

```bash
# First install pipx
> apt install pipx
# Then install hatch using pipx
> pipx install hatch
```

:::
::::

:::{tip}
Hatch can also be installed directly using [pip](https://hatch.pypa.io/latest/install/#pip) or [conda](https://hatch.pypa.io/latest/install/#conda). We encourage you to
follow the instructions above because we have found that the Hatch installers
for Windows and Mac are the easiest and most efficient.

Our Linux users have found success installing Hatch with pipx if they already
use apt install.

Both approaches (using a graphical installer on Windows/Mac and pipx) ensure
that you have Hatch installed globally. A global install means that Hatch is
available across all of your Python environments on your computer.
:::

### Check that hatch installed correctly

Once you have completed the installation instructions above, you can open your
terminal, and make sure that Hatch installed correctly using the command below:

```bash
hatch --version
# Hatch, version 1.9.4
```

*Note the version number output of `hatch --version` will likely  be
different from the output above in this tutorial.*

## Configure Hatch

Once you have installed Hatch, you can customize its configuration. This
includes setting the default name and setup for every package you create. While
this step is not required, we suggest that you do it.

Hatch stores your configuration in a [`config.toml` file](https://hatch.pypa.io/latest/config/project-templates/).

While you can update the `config.toml` file through the command line, it might
be easier to look at and update it in a text editor if you are using it for the
first time.

### Step 1: Open and Edit Your `config.toml` File

To open the config file in your file browser, run the following command in your
shell:

`hatch config explore`

This will open up a directory window that allows you to double-click on the file
and open it in your favorite text editor.

You can also retrieve the location of the Hatch config file by running the
following command in your shell:

```bash
hatch config find
# hatch config --help will show you all the options for config.
```

### Step 2 - update your email and name

Once the file is open, update the [template] table of the `config.toml` file
with your name and email. This information will be used in any `pyproject.toml`
metadata files that you create using Hatch.

```toml
[template]
name = "firstName LastName"
email = "your-email@your-domain.org"
```

### Step 3

Next, set tests to false in the `[template.plugins.default]` table.

While tests are important, setting the tests configuration in Hatch
to `true` will create a more complex `pyproject.toml` file. You won't
need to use this feature in this beginner friendly tutorial series
but we will introduce it in later tutorials.

Your `config.toml` file should look something like the one below.

```toml
mode = "local"
project = ""
shell = ""

[dirs]
project = []
python = "isolated"
data = "/Users/your/path/Application Support/hatch"
cache = "/Users/your/path/Library/Caches/hatch"

[dirs.env]

[projects]

[publish.index]
repo = "main"

[template]
name = "Leah Wasser"
email = "leah@pyopensci.org"

[template.licenses]
headers = true
default = [
    "MIT",
]

[template.plugins.default]
tests = false
ci = false
src-layout = true

[terminal.styles]
```

Also notice that the default license option is MIT. While we will discuss
license in more detail in a later lesson, the MIT license is the
recommended permissive license from
[choosealicense.com](https://www.choosealicense.com) and as such we will
use it for this tutorial series.

You are of course welcome to select another license.

:::{todo}
I think we'd need the SPDX license options here if they want to chose bsd-3 for instance
:::

### Step 4: Close the config file and run `hatch config show`

Once you have completed the steps above run the following command in your shell.

`hatch config show`

`hatch config show` will print out the contents of your `config.toml` file in
your shell. Look at the values and ensure that your name, email is set. Also
make sure that `tests=false`.

## Hatch features

Hatch offers a suite of features that will make creating, publishing
and maintaining your Python package easier.

:::{admonition} Comparison to other tools
:class: tip
[We compared Hatch to several of the other popular packaging tools in the ecosystem including flit, pdm and poetry. Learn more here](package-features)
:::

[More on Hatch here](hatch)

A few features that Hatch offers

1. It will convert metadata stored in a `setup.py` or `setup.cfg` file to a pyproject.toml file for you (see [Migrating setup.py to pyproject.toml using Hatch](setup-py-to-pyproject-toml.md
))
2. It will help you by storing configuration information for publishing to PyPI after you've entered it once.

Use `hatch -h` to see all of the available commands.

## What's next

In the next lesson you'll learn how to package and make your code installable using Hatch.
