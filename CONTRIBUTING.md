# Contributing Guide for the Python open source software packaging book

This is a community resource. We welcome contributions in the form of issues and/or pull requests to this guide.

* If you have an idea for something that should be included in the guide, [please open an issue here](https://github.com/pyOpenSci/python-package-guide/issues).
* If you find a typo, feel free to [submit a pull request](https://github.com/pyOpenSci/python-package-guide/pulls) to modify the text directly. Or, if you are less comfortable with pull requests, feel free to open an issue.
* If you want to see a larger change to the content of the guide book, please submit an issue first!

## How this guide structured

Most of this repository is structured for **Sphinx**, a documentation engine built in `Python`. We are using the Sphinx Book Theme and the `myST` syntax to create each page in this book.

If you wish to contribute by working on the guide book locally, you
will first need to

1. Fork this repository
2. Clone it locally
3. Build the documentation locally

## Instructions for building the documentation locally on your computer

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
