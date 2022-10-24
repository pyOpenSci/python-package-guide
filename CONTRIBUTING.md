# Contributing to this repository

Most of this repository is structured for **Sphinx**, a documentation engine built in Python.

## Build the documentation

The easiest way to build the documentation in this repository is to use `nox`, 
a tool for quickly building environments and running commands within them.
Nox ensures that your environment has all the dependencies needed to build the documentation.

To do so, follow these steps:

1. Install `nox`

   ```
   pip install nox
   ```
2. Build the documentation:

   ```
   nox -s docs_build
   ```

This should create a local environment in a `.nox` folder, build the documentation (as specified in the `noxfile.py` configuration), and the output will be in `_build/html`.

To build live documentation that updates when you update local files, run the following command:

```
nox -s docs_live
```
