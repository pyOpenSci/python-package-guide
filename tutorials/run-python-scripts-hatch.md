---
:og:description: Learn how to run standalone Python scripts with Hatch using
  inline metadata so dependencies and Python versions are managed
  automatically.
:og:title: Run standalone Python scripts with Hatch
---

# Run standalone Python scripts with Hatch

Python supports inline metadata for scripts (a feature added in 2024). This makes it possible to run
standalone scripts with dependencies and Python versions managed
automatically.

Many tools support this workflow, including PDM, Hatch, and uv. In this
tutorial, we focus on Hatch and UV. The same metadata format can also be used with
other tools.

:::{seealso}

* [Hatch: How to run Python scripts](https://hatch.pypa.io/latest/how-to/run/python-scripts/)
* [uv: Running scripts](https://docs.astral.sh/uv/guides/scripts/#creating-a-python-script)
:::

## How to create a reproducible script

Sometimes you want to share or run a single script without creating a full
package. To do this, you can use inline script metadata. This format lets you
specify dependencies and Python versions at the top of your script in a
comment block.

When you add metadata at the top of a script, Hatch (or PDM or uv) will use
that metadata to:

* Create an isolated virtual Python environment for that script.
* Install the dependencies listed in the script into that environment.
* Use the required Python version that you specify in the metadata.

This approach is useful for workflows that you want to make reproducible, but
that do not need to become full Python packages.

## Why use Hatch for scripts?

Inline metadata helps you make scripts reproducible. Anyone can run your
script without manually creating a new environment or guessing which
dependencies it needs. Hatch takes care of installing dependencies and using
the correct Python version.

## How to add inline metadata to your script

You will use Hatch in this example, but you can also use uv if that is your
preferred tool.

First, create a new file named `script.py` with the block below at the top.
The metadata block starts with `# /// script` and ends with `# ///`.
Everything in between must be TOML metadata written as comments.

In the example below, the script requires Python 3.11 or newer, and NumPy is
declared as a dependency.

```python
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "numpy",
# ]
# ///

import numpy as np

temperatures_c = np.array([12.4, 13.1, 14.8, 15.2, 16.0, 14.4, 13.7])
mean_temp = np.mean(temperatures_c)
anomalies = temperatures_c - mean_temp

print(f"Mean temperature: {mean_temp:.2f} C")
print("Temperature anomalies:", np.round(anomalies, 2))
```

## Run the script with Hatch

Open your terminal and change to the directory where `script.py` lives.
Then run:

```bash
hatch run script.py
```

On first run, Hatch will create an environment and install dependencies. On
later runs, Hatch will reuse that environment so startup is faster.

:::{note}
The environment name is based on the script path. If you move the script to a
new location, Hatch will treat it as a new script environment.
:::

## Optional: configure script environment behavior

You can control script-specific Hatch behavior in the same metadata block.
For example, to use `pip` instead of `uv` as the installer:

```python
# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
#
# [tool.hatch]
# installer = "pip"
# ///
```

:::{admonition} Run the same script with uv

If you prefer uv, you can run the same inline-metadata script with:

```bash
uv run script.py
```

The same `# /// script` metadata block works with uv, including
`requires-python` and `dependencies`.

For more on using uv to run scripts, see the guide:
[Running scripts with uv](https://docs.astral.sh/uv/guides/scripts/#creating-a-python-script).
:::

## When to use scripts vs. packages

You may be wondering when to use scripts versus creating a package.

This depends on your use case. Scripts are often useful when:

* You have one small task, or a specific workflow that is not generalizable.
* Your workflow is still evolving, but you want to run it in a reproducible
  environment.
* You want reproducible dependencies quickly.
* You are sharing a single file with collaborators.

Create a full package when:

* You are building reusable modules for multiple projects.
* You need tests, documentation, releases, and long-term maintenance.
* Your codebase is growing beyond one or two scripts.

:::{seealso}

* [Get to know Hatch](get-to-know-hatch.md)
* [Create a Python package](create-python-package.md)
* [Command line reference guide](command-line-reference.md)
:::
