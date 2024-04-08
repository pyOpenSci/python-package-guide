# Using Hatch to Migrate setup.py to a pyproject.toml

Hatch can be particularly useful to generate your project's `pyproject.toml` if your project already has a `setup.py`.

:::{admonition} Note
:class: tip

This step is not necessary and is only useful if your project already has a `setup.py` file defined.
* If your project does not already define a `setup.py` see [Make your Python code installable](installable-code.md)
:::

:::{admonition} Learning Objectives
:class: tip

In this lesson you will learn:

1. The process of using Hatch to transition to using `pyproject.toml` for projects that already have a `setup.py` defined.
:::

## What is Hatch?

See [Get to know Hatch](get-to-know-hatch.md).

## Prerequisites

Before we begin, ensure that you have Hatch installed on your system. You can install it via pip:

```bash
pip install hatch
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

   ```bash
   cd path/to/your/project
   ```

2. **Initialize Hatch**: Run the following command to initialize Hatch in your project directory:

   ```bash
   hatch new --init
   ```

3. **Review and Customize**: After running the previous command, Hatch will automatically generate a `pyproject.toml` file based on your existing project configuration. Take some time to review the contents of the generated `pyproject.toml` file. You may want to customize certain settings or dependencies based on your project's requirements (see [pyproject.toml tutorial](pyproject-toml.md) for more information about the `pyproject.toml`).

4. **Verify**: Verify that the `pyproject.toml` file accurately reflects your project configuration and dependencies. You can manually edit the file if needed, but be cautious and ensure that the syntax is correct.
