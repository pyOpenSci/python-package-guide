(environment-managers)=
# Environment Managers for Python Packaging

:::{admonition} Quick Decision Guide

- **Python-only project, want simplicity?** → venv + pip
- **Python-only, want speed?** → **uv** (recommended)
- **Installing CLI tools globally?** → pipx
- **Need conda packages or cross-language dependencies?** → **pixi** (recommended) or conda/mamba
- **Creating a Python package?** → Use Hatch -- with UV as a dependency manager

You can mix tools! For example, use **pipx** to install tools you use often (at the command line) like Hatch, ruff or pre-commit, then use **uv** within your projects for package and environment management.
:::

# Environment and package managers

Package and environment managers are important tools in your Python packaging workflows. To make
Your packaging experience when selecting a tool will be easier if you understand the difference between the two.

1. A **package manager** is used to install, update, and remove Python packages (libraries and tools) and their dependencies in your environment. When you use a package manager, you are often downloading packages from a repository like PyPI (Python Package Index) or a local repository like GitHub / GitLab.

:::{note}
When you run `pip install numpy`, pip acts as a package manager and installs numpy from PyPI. Pip's default repository when you install a package is PyPI, but it can be used to install packages from other repositories such as GitHub.
:::

2. An **environment manager** creates isolated spaces (environments) for your Python projects. Each environment has its own Python installation and its own installed packages. Using isolated environments for different projects reduces the change of environment conflicts when using the same environment across different projects with different dependencies.

There are many tools listed below, but if you're short on time, you may want to consider

1. Hatch combined with UV if you are managing a Python package. [Check out our tutorials for more on this workflow.](create-pure-python-package)
2. Pixi or mamba as faster alternatives to conda if you are working in the non-Pure Python packaging space.

## Where environment managers save your environment

Environment managers save environments in different locations by default. For instance, `venv`, an environment manager that ships with Python, saves an environment by default in your current working directory. UV has the same native behavior. In contrast, conda and mamba save environments in a global location, allowing you to access them easily across projects.

:::{tip}
UV does have a global cache even tho its default behavior is to create an environment in your current working directory.
:::


## Some tools do everything

Some modern tools handle both package installation and environment management. For instance, UV, conda and mamba can be used to both create environments, add dependencies, and build and install tools.

## Comparison Table: pip ecosystem

| Tool | Type | Language | Speed | Default Environment Location | Description |
|------|------|----------|-------|------------------------------|-------------|
| **pip** | Package manager | Python | Slower | N/A (uses existing environment) | Python's standard package installer. pip also builds packages |
| **pipx** | Package manager | Python | Slower | Global (isolated per tool) | Installs tools that you need to regularly use across projects such as nox, pytest or ruff in a global location |
| **uv** | Both | Rust | Fastest | Current working directory | Fast package installer and environment creator |
| **venv** | Environment manager | Python | Slower | Current working directory | Python's built-in environment creator |
| **virtualenv** | Environment manager | Python | Moderate | Current working directory | Feature-rich alternative to venv |

## Comparison Table: conda ecosystem
| Tool | Type | Language | Speed | Default Environment Location | Description |
|------|------|----------|-------|------------------------------|-------------|
| **conda** | Both | Python/C++ | Slower | Global (`~/anaconda3/envs/`) | Cross-language package and environment manager |
| **mamba** | Both | C++ | Faster | Global (`~/anaconda3/envs/`) | Faster drop-in replacement for conda |
| **pixi** | Both | Rust | Fastest | Current working directory (`.pixi/`) | Modern conda-based tool with lock files |

```{tip}
**Speed comparison:** Rust-based tools (uv, pixi) are significantly faster when installing packages and resolving complex environments than Python-based tools. Mamba is faster than conda but might be slower than Rust-based alternatives such as Pixi.
```

## Package Managers

### pip

* Pip is Python's standard package installer. It is included with Python by default.
* Pip is great for installing packages from PyPI and GitHub / GitLab into existing environments.
* It is also great for development if you want to install your package locally in editable mode.

**Basic usage:**
```bash
pip install numpy
pip install -e .  # Install your package in editable mode
```

### pipx

* Pipx is can be used to install a tool that you need to use across projects (like `riff`, `pytest`, `sphinx`, `nox`), globally.

Why use it: You might use it to avoid reinstalling the same tool over and over on your machine.

**Basic usage:**
```bash
pipx install black
pipx install hatch
```

### conda / mamba

Conda is a cross-language package manager that installs Python packages, R packages, system libraries, and more. Mamba is a faster, drop-in replacement for conda and we highly recommend mamba over conda if you are still using conda.

These tools are best for scientific computing projects and environments that need non-Python dependencies (like C libraries, GDAL, or R packages).

**Basic usage:**
```bash
# conda
conda install numpy

# mamba (faster/preferred alternative)
mamba install numpy
```

:::{note}
Conda and mamba also function as environment managers - see below!
:::

## Environment Managers

### hatch for pure Python packaging

:::{admonition} pyOpenSci Recommends
:class: tip
We recommend **hatch** as a complete project management tool for Python packaging. Hatch manages environments, builds packages, runs tests, and handles publishing—all in one tool. It can use **uv** as its backend for even faster operations.
:::

Hatch is a comprehensive modern Python project manager that handles environments, package building, testing, and publishing. Hatch creates isolated environments for different tasks (testing, docs, development). Hatch uses UV under the hood to install Python, and can be set to use UV to manage environment installations too.

Hatch is best for Python package developers who want an all-in-one tool that handles the entire packaging workflow from development to publication.

[Check out our tutorial](create-pure-python-package)

**Basic usage:**

::::{tab-set}

:::{tab-item} hatch (recommended)
```bash

# Create a new project (using the pyOpenSci template (requires that you install copier)
copier copy gh:pyopensci/pyos-package-template .

# or with hatch
hatch new my-project

# Run tests in an isolated environment using the pyOpenSci template
hatch run tests:run

# Build your package using a Hatch environment and our template
hatch run build:check
```
:::

:::{tab-item} hatch with uv backend
```bash
# Configure hatch to use uv (in pyproject.toml or hatch.toml)
# [tool.hatch.envs.default]
# installer = "uv"

```
:::

::::

:::{note}
Hatch acts as a task runner and can manage multiple environments that you define. It also handles project and dependency installation, making it ideal for package maintainers who want consistency across development tasks.
:::

### venv

venv is Python's built-in environment creator (included with Python 3.3+).
It is best for simple pure Python projects. Because venv ships with Python, and it is used by Hatch, UV and other tools under the hood, it is the most widely used tool.

Basic usage:

```bash
# Create environment
python -m venv .venv

# Activate (Mac/Linux)
source .venv/bin/activate

# Activate (Windows)
.venv\Scripts\activate

# Install packages
pip install numpy
```

### virtualenv

virtualenv is a more feature-rich alternative to venv with better performance and additional options.
It's best for you if you need more control over your environments.

**Basic usage:**

```bash
# Install virtualenv first
pip install virtualenv

# Create environment
virtualenv .venv

# Activate (same as venv)
source .venv/bin/activate
```

### uv

:::{admonition} pyOpenSci Recommends
:class: tip
We recommend **uv** for fast, reliable Python package and environment management. It's significantly faster than pip and easily handles both installing packages and creating environments.
:::

UV is a fast, Rust-based tool that replaces both pip and venv. It installs packages and creates virtual environments at lightning speed. UV is best for any pure Python project. Pixi is better if are working in the non-pure Python packaging space.

**Basic usage:**

::::{tab-set}

:::{tab-item} uv (recommended)

```console
# Add a dependency to your project with uv add (will add to the pyproject.toml file)
> uv add numpy

# Create environment and run python with your dependencies installed
# UV will also install your package in editable mode
> uv run python
```
:::

:::{tab-item} venv + pip
```bash
# Create environment
python -m venv .venv
source .venv/bin/activate

# Install packages
pip install numpy

# Install your package in editable mode with your dev dependency group
pip install -e ".[dev]"
```
:::

:::{tab-item} pixi
```bash
# Initialize project (creates environment automatically)
pixi init

# Add packages
pixi add numpy

# Install your package in dev mode
pixi add --pypi --editable "package-name[dev] @ file:///absolute/path/to/package"
```
:::

::::

### conda / mamba (as environment managers)

Conda and mamba create isolated environments that can contain Python, R, system libraries, and more.
The conda ecosystem tools are best for managing complex dependencies across languages or when you need specific system libraries.

**Basic usage:**
```bash
# Create environment with conda
conda create -n myenv python=3.11
conda activate myenv

# Or with mamba (faster)
mamba create -n myenv python=3.11
mamba activate myenv
```

### pixi
```{admonition} pyOpenSci Recommends
:class: tip
For projects needing conda packages, we recommend **pixi** over conda/mamba. It's faster, uses lock files for reproducibility, and works cross-platform.
```

Pixi is a modern, fast package and environment manager built on conda ecosystems. Similar to UV, Pixi uses lock files for reproducible environments. Pixi is best suited for scientific projects that require conda packages, teams that require exact reproducibility, or cross-platform development.

**Basic usage:**

```bash
# Initialize new project
pixi init

# Add Python packages
pixi add numpy pandas

# Add conda packages (like GDAL)
pixi add gdal

# Run commands in the environment
pixi run python script.py

# Activate environment in an interactive shell
pixi shell
```
```{note}
Pixi automatically creates a lock file (`pixi.lock`) ensuring everyone on your team gets identical environments.
```
