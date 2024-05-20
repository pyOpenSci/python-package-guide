---
orphan: true
---
# Contributing Guide for the Python open source software packaging book

This is a community resource. We welcome contributions in the form of issues and/or pull requests to this guide.

* If you have an idea for something that should be included in the guide, [please open an issue here](https://github.com/pyOpenSci/python-package-guide/issues).
* If you find a typo, feel free to [submit a pull request](https://github.com/pyOpenSci/python-package-guide/pulls) to modify the text directly. Or, if you are less comfortable with pull requests, feel free to open an issue.
* If you want to see a larger change to the content of the guide book, please submit an issue first!

## How this guide is structured

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
   python -m pip install nox
   ```
2. Build the documentation:

   ```
   python -m nox -s docs
   ```

This should create a local environment in a `.nox` folder, build the documentation (as specified in the `noxfile.py` configuration), and the output will be in `_build/html`.
The site can then be viewed locally by opening the top level `index.html` in your web browser. The exact location of this file will depend on you system, but the output of the following command could be copied into an address bar

```
echo "file://$(pwd)/_build/html/index.html"
```

To build live documentation that updates when you update local files, run the following command:

```
python -m nox -s docs-live
```

When build like this, the output will tell you a localhost address where the site can be viewed, generally http://127.0.0.1:8000.

## Code examples

This guide uses the [literalinclude Sphinx directive](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-literalinclude)
whenever possible to keep code and prose separate. Code for use in the documentation is kept in the `examples/` folder.

### Referencing code in documentation

If an example is present elsewhere in the documentation that you want to use, you can copy the `literalinclude`
directive verbatim and the examples will stay in sync.

If you already see code in the examples folder that you can use for new documentation, a new `literalinclude` can be
made to extract it into the site. Only a relative path to the code is required for a working `literalinclude`, but you
should in almost all cases also provide a `:language:` and `:lines:`. The former makes code examples prettier, and the
later can protect your example from future modifications to the code.

**Pro tip**: As an alternative to `:lines:` there are also the `:start-after:`, `:start-at:`, `:end-before:`, and
`:end-at:` options. And if the example code is Python, `:pyobject:` can be an even more future-proof way to keep the
same documentation content even through code refactors.

If you need example code that doesn't yet exist in `examples/` [see creating code for documentation](#creating-code-for-documentation).

### Creating code for documentation

Whenever you come across a place that could benefit from a code block, instead of writing it in-line with a code fence
(`` ``` `` blocked text) you can write it as a file in its own format. Your example may even already exist; [see referencing code in documentation
](#referencing-code-in-documentation).

If you want to add a new example that doesn't fit into any of the existing example files, you can create a new file and
reference it in a `literalinclude` block. If it makes sense for that file to live within one of the existing example
projects please add it there; otherwise create a new folder in the `examples` directory.

If an existing example is incomplete or a new example makes sense to be added to an existing file, go ahead and add it,
but take care to not break the rest of the guide. Whenever possible, extend the example rather that rewrite it. So for
instance, add new functions to the end of the file, new methods after all existing ones in a class.

Example code is checked for correctness, so adding a new example may require adding additional tests for coverage, and
will require fixing any failing tests.

***⚠️ WARNING***: great care should be taken when modifying existing example code, especially any modification beyond
appending to the end of the file. All code examples are (potentially) shared examples. This makes for more consistent
examples in the guide but can mean action-at-a-distance when modifying the examples for one particular use case.
If you find yourself modifying existing examples try running this command and then checking those pages in a new build.
```bash
grep -lr '\.\./examples/path/to/modified\.py' documentation/
```

Example:

Instead of writing example code in markdown like this

````md
Here is an example Python function:

```python
def is_empty(x):
    return not bool(len(x))
```
````

The python can be extracted into a `.py` file
```python
def is_empty(x):
    return not bool(len(x))
```

````md
Here is an example Python function:

:::{literalinclude} ../examples/contributing_example.py
:language: python
:lines: 1-2
````

As another example, if you only need to show part of a `pyproject.toml`, we already have complete project definitions,
you need only to find the relevant part.

Instead of writing this
````md
Classifiers are just a list of plain strings
```toml
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
]
```
````

an example could be extracted from an existing toml file
```md
:::{literalinclude} ../examples/pure-hatch/pyproject.toml
:language: toml
:start-at: classifiers = [
:end-at: ]
```
