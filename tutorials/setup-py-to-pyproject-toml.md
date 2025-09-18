---
:og:description: If you’re creating a pure Python project, pyproject.toml is preferred over setup.py for packaging and configuration. Learn how to migrate from the older setup.py format to the modern pyproject.toml file. This lesson walks you through updating your package metadata and build settings to align with current Python packaging standards.
:og:title: Using Hatch to Migrate setup.py to a pyproject.toml
---

# Using Hatch to Migrate setup.py to a pyproject.toml

Hatch can be useful for generating your project's `pyproject.toml` file if your project already has a `setup.py` file.

:::{admonition} Note
:class: tip

This step is not necessary and is only helpful if your project already has a `setup.py` file defined.
* If your project does not already define a `setup.py` see [Make your Python code installable](create-python-package)
:::

:::{admonition} Learning Objectives
:class: tip

In this lesson, you will learn:

1. The process of using Hatch to transition to using `pyproject.toml` for projects that already have a `setup.py` defined.
:::

## What is Hatch?

Hatch is a Python package manager designed to streamline the process of creating, managing, and distributing Python packages. It provides a convenient CLI (Command-Line Interface) for tasks such as creating new projects, managing dependencies, building distributions, and publishing packages to repositories like PyPI.

:::{admonition} Get to know Hatch
:class: tip

See [Get to know Hatch](get-to-know-hatch) for more information.

:::

## Prerequisites

Before we begin, ensure that you have Hatch installed on your system. You can install it via pip:

```bash
pipx install hatch
```

## Sample Directory Tree

Let's take a look at a sample directory tree structure before and after using `hatch init`:

### Before `hatch init`

```
project/
│
├── src/
│   └── my_package/
│       ├── __init__.py
│       └── module.py
│
├── tests/
│   └── test_module.py
│
└── setup.py
```

### After `hatch init`

```
project/
│
├── pyproject.toml
│
├── src/
│   └── my_package/
│       ├── __init__.py
│       └── module.py
│
├── tests/
│   └── test_module.py
│
└── setup.py
```

As you can see, the main change after running `hatch init` is the addition of the `pyproject.toml` file in the project directory.

## Step-by-Step Guide

Now, let's walk through the steps to use Hatch to create a `pyproject.toml` file for your project.

1. **Navigate to Your Project Directory**: Open your terminal or command prompt and navigate to the directory where your Python project is located.

2. **Initialize Hatch**: Run the following command to initialize Hatch in your project directory:

   ```bash
   hatch new --init
   ```

3. **Review and Customize**: After running the previous command, Hatch will automatically generate a `pyproject.toml` file based on your existing project configuration. Take some time to review the contents of the generated `pyproject.toml` file. You may want to customize certain settings or dependencies based on your project's requirements (see [pyproject.toml tutorial](pyproject-toml) for more information about the `pyproject.toml`).

4. **Verify**: Verify that the `pyproject.toml` file accurately reflects your project configuration and dependencies. You can manually edit the file, but be cautious and ensure that the syntax is correct.

5. **Delete setup.py**: Since we're migrating to using `pyproject.toml` exclusively, the `setup.py` file becomes unnecessary. You can safely delete it from your project directory.

6. **Test Build**: Before proceeding further, it's essential to ensure that your project builds successfully using only the `pyproject.toml` file. Run the following command to build your project:

```bash
hatch build
```

This command will build your project based on the specifications in the `pyproject.toml` file. Make sure to check for any errors or warnings during the build process.

7. **Test Existing Functionality**: After successfully building your project with `pyproject.toml`, it's crucial to ensure that your project's existing functionality remains intact. Run any pre-existing tests to verify that everything still works as expected.
