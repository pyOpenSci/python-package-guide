---
:og:description: Learn how to run standalone Python scripts with Hatch using
  inline metadata so dependencies and Python versions are managed
  automatically.
:og:title: Run standalone Python scripts with Hatch
---

# Run standalone Python scripts with Hatch

Sometimes you want to share or run a single script without creating a full
package. Hatch supports this workflow using inline script metadata.

When you add metadata at the top of a script, Hatch can:

* Create an isolated environment for that script.
* Install only the dependencies listed in the script.
* Use the required Python version that you specify.

This is useful for quick analyses, data cleanup scripts, and reproducible
automation tasks.

## Why use Hatch for scripts?

Inline metadata helps you avoid "it works on my machine" issues. Anyone can
run the script with Hatch and get the same dependency set.

Compared to running a script in your currently active environment, this
approach is more reproducible because dependencies are declared with the code.

## Add inline metadata to your script

Create a new file named `script.py` with the block below at the top:

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

The metadata block starts with `# /// script` and ends with `# ///`.
Everything in between must be TOML-style metadata written as comments.

## Run the script with Hatch

From your terminal, run:

```bash
hatch run script.py
```

On first run, Hatch will create an environment and install dependencies. On
later runs, Hatch will reuse that environment and start faster.

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

## When to use scripts vs packages

Use this script workflow when:

* You have one small task.
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
