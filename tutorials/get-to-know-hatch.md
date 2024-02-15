# Get to know hatch

Our Python packaging tutorials use the tool Hatch.
In this tutorial, you will install and get to know hatch a bit more before starting to use it.

## Install Hatch
To begin, install Hatch following the
[instructions here](https://hatch.pypa.io/latest/install/).

:::{tip}
If you are comfortable using [pipx](https://pipx.pypa.io/stable/) to install hatch, we encourage you to do so. pipx will ensure that your package is available across all of your Python environments on your computer rather than just in the environment that you install it into.

However if you are not sure about pipx, you can install hatch using pip or conda.
:::

## Configure hatch

Once you have installed hatch, you will want to customize the configuration.

Hatch stores your configuration information in a [config.toml file](https://hatch.pypa.io/latest/config/project-templates/).

While you can update the `config.toml` file through the command line,
it might be easier to look at it and update it in a text editor if you are using it for the first time.

### Step 1: Open and edit your config.toml file

To open the config file in your file browser, run the following command in your shell:

`hatch config explore`

This will open up a directory window that will allow you to double click on the file and open it in your favorite text editor

### Step 2 - update your email and name

Once the file is open, update the [template] table of the config.toml file with your name and email. This information will be used in any pyproject.toml metadata files that you create using hatch.

```toml
[template]
name = "firstName LastName"
email = "your-email@your-domain.org"
```

### Step 3

Next, set tests to false in the `[template.plugins.default]` table.

While tests are important, setting the tests configuration in Hatch
to `true` will create a more complex pyproject.toml file. You won't
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

You are of course welcome to select another license

:::{todo}
I think we'd need the SPDX license options here if they want to chose bsd-3 for instance
:::

### Step 4: Close the config file and run hatch config show

Once you have completed the steps above run the following command in your shell.

`hatch config show`

hatch config show will print out the contents of your config.toml file in your shell. look at the values and ensure that your name, email is set. Also make sure that tests=false.

## Hatch features

Hatch offers a suite of features that will make creating, publishing
and maintaining your Python package easier.

:::{admonition}
:class: tip
[We compared hatch to several of the other popular packaging tools in the ecosystem including flit, pdm and poetry. Learn more here](package-features)
:::

[More on hatch here](hatch)

A few features that hatch offers

1. it will convert metadata stored in a `setup.py` or `setup.cfg` file to a pyproject.toml file for you. While we have not extensively tested this feature yet, please let us know if you try it!
2. It will help you by storing configuration information for publishing to PyPI after you've entered it once.

Use `hatch -h` to see all of the available commands.


## What's next

In the next lesson you'll learn how to package and make your code installable using Hatch.
