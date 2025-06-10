---
:og:description: Learn how to add a command-line interface (CLI) to your Python package using the argparse library. This lesson walks you through creating a CLI entry point so users can run your package directly from the terminal.
:og:title: Command Line Reference Guide
---

# Command Line Reference Guide

```{important}
**What these tables are:** These tables summarize the command line inputs (e.g., `pipx install hatch`,  `hatch build`) necessary to complete all steps in the package creation process, from installing Hatch to publishing the package on PyPI and conda-forge.

**What these tables are not:** These tables do not cover the manual/non-automated steps (e.g., create PyPI account, create PyPI API token) you have to complete throughout the package creation process.

**Operating system note:** The current iteration of this guide has been tested on the Windows OS only. Many commands are Windows-specific. OS-specific commands are indicated with parentheses after the description of the command, e.g., [COMMAND_DESCRIPTION] (Windows). Corresponding commands for macOS and Linux will be added in the future.
```

## Environment Setup

:::{table}
:widths: auto
:align: center

| Description | Syntax |
|---|---|
| Set PowerShell execution policy (Windows) | `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` |
| Install Scoop (Windows) | `Invoke-RestMethod -Uri https://get.scoop.sh \| Invoke-Expression` |
| Add "main" bucket as download source (Windows) | `scoop bucket add main` |
| Add "versions" bucket as download source (Windows) | `scoop bucket add versions` |
| Install pipx (Windows) | `scoop install pipx` or `scoop install main/pipx` |
| Update PATH variable with pipx directory | `pipx ensurepath` |
| Install hatch | `pipx install hatch` or `pip install hatch` |
| List hatch commands | `hatch -h` |
| Open location of hatch config file | `hatch config explore` |
| Print contents of hatch config file | `hatch config show` |
| Install grayskull | `pipx install grayskull` or `pip install grayskull` |

:::

## Package Development

:::{table}
:widths: auto
:align: center

| Description | Syntax |
|---|---|
| Create package structure and baseline contents | `hatch new [PACKAGE_NAME]` |
| Install package locally in editable mode | `python -m pip install -e .` |
| Install development dependencies | `python -m pip install ".[DEPENDENCY_GROUP]"` |
| List packages installed in current environment | `pip list` |
| Install package from GitHub | `pip install git+https://github.com/user/repo.git@branch_or_tag` |
| Create development environment | `hatch env create` |
| Activate development environment | `hatch shell` |
| Exit development environment | `exit` |

:::

## Package Publishing

:::{table}
:widths: auto
:align: center

| Description | Syntax |
|---|---|
| Build package sdist and wheel distributions | `hatch build` |
| Publish package to Test PyPI | `hatch publish -r test` |
| Install package from Test PyPI | `pip install -i https://test.pypi.org/simple/ [PACKAGE_NAME]` |
| Publish package to PyPI | `hatch publish` |
| Install package from PyPI | `pip install -i https://pypi.org/simple/ [PACKAGE_NAME]` |
| Create conda-forge recipe | `grayskull pypi [PACKAGE_NAME]` |
| Check that package installs properly | `pip check` |
| Install package from conda-forge | `conda install -c conda-forge [PACKAGE_NAME]` |

:::

## Versions and Environments

:::{table}
:widths: auto
:align: center

| Description | Syntax |
|---|---|
| View environments | `hatch env show` |
| Print path to active hatch environment | `hatch env find` |
| Bump package version - major | `hatch version major` |
| Bump package version - minor | `hatch version minor` |
| Bump package version - patch | `hatch version patch` |
| Run test scripts on multiple Python versions | `hatch run all:[SCRIPT_NAME]` |

:::
