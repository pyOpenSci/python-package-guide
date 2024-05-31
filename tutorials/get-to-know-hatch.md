# Get to know Hatch

Our Python packaging tutorials use the tool Hatch.
In this tutorial, you will install and get to know Hatch a bit more before starting to use it.

## Install Hatch
To begin, install Hatch from the command line using [pipx](https://pipx.pypa.io/stable/)

```bash
pipx install hatch
```

:::{tip}
Hatch can also be installed directly using `pip` or `conda`, but we encourage you to use `pipx`.
This is because `pipx` will ensure that your package is available across all of your Python
environments on your computer rather than just in the environment that you install it into.
If you install hatch this way you will have to take care that the environment it is installed into
is activated for the command to work.
:::

You can check that hatch is working properly by issuing a simple command to get the version

```bash
hatch --version
# Hatch, version 1.9.4
```

Note the version numbers will likely be different

## Configure hatch

Once you have installed Hatch, you will want to customize the configuration.

Hatch stores your configuration information in a [`config.toml` file](https://hatch.pypa.io/latest/config/project-templates/).

While you can update the `config.toml` file through the command line,
it might be easier to look at it and update it in a text editor if you are using it for the first time.

### Step 1: Open and edit your `config.toml` file

To open the config file in your file browser, run the following command in your shell:

`hatch config explore`

This will open up a directory window that will allow you to double click on the file and open it in your favorite text editor.

You can also retrieve the location of the Hatch config file by running the following command in your shell:

```bash
hatch config find
# hatch config --help will show you all the options for config.
```

### Step 2 - update your email and name

Once the file is open, update the [template] table of the `config.toml` file with your name and email. This information will be used in any `pyproject.toml` metadata files that you create using Hatch.

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
recommended permissive license from [choosealicense.com](https://www.choosealicense.com) and as such we will
use it for this tutorial series.

You are of course welcome to select another license.

:::{todo}
I think we'd need the SPDX license options here if they want to chose bsd-3 for instance
:::

### Step 4: Close the config file and run `hatch config show`

Once you have completed the steps above run the following command in your shell.

`hatch config show`

`hatch config show` will print out the contents of your `config.toml` file in your shell. look at the values and ensure that your name, email is set. Also make sure that `tests=false`.

## Hatch features

Hatch offers a suite of features that will make creating, publishing
and maintaining your Python package easier.

:::{admonition} Comparison to other tools
:class: tip
[We compared Hatch to several of the other popular packaging tools in the ecosystem including flit, pdm and poetry. Learn more here](package-features)
:::

[More on Hatch here](hatch)

A few features that Hatch offers


1. it will convert metadata stored in a `setup.py` or `setup.cfg` file to a pyproject.toml file for you (see [Migrating setup.py to pyproject.toml using Hatch](setup-py-to-pyproject-toml.md
))
2. It will help you by storing configuration information for publishing to PyPI after you've entered it once.

Use `hatch -h` to see all of the available commands.


## What's next

In the next lesson you'll learn how to package and make your code installable using Hatch.
