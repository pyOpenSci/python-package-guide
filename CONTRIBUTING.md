---
orphan: true
---
# Contributing to the Python Packaging Guide

The guide is a community resource.

## TL;DR

We welcome contributions in the form of issues and pull requests:

* If you have an idea for something that should be included in the guide, [please open an issue here](https://github.com/pyOpenSci/python-package-guide/issues).
* If you find a typo, feel free to [submit a pull request](https://github.com/pyOpenSci/python-package-guide/pulls) to modify the text directly. Or, if you are less comfortable with pull requests, feel free to open an issue.
* If you are interested in helping translate the guide into other languages, take a look at the [translation guide](./TRANSLATING.md).
* If you want to see a larger change to the content of the guide book, please submit an issue first!

If you are unsure about how to contribute or are not familiar with git and github, this guide will help you through the process.

## How the Python Packaging Guide is structured

The Python Packaging Guide is written in myST (a variant of MarkDown and rST) and we use **Sphinx**, a documentation engine built in `Python` to build the HTML version you see online.

We use a tool called Nox to manage the process of building the guide.

## Two approaches to contributing

You can contribute to the guide using two approaches.

The first approach is using a local copy of the guide in your computer. This option requires a more involved setup, but allows you to build the guide locally to verify your contribution did not introduce any bugs before submitting a pull request. It is the recommended approach for larger contribution, like writing a whole new section.

The second approach is making your contribution directly in the GitHub website. This option does not require any setup on your computer and while your contribution will still be tested when you submit a PR (continuous integration), it will take longer for you to get any feedback in case of issue. It is the best way to make small contribution, like fixing typos, or if this is your first contribution to open source and the first approach feels too intimidating.

## Forking the repository

Independently of the approach you choose, the first step is to fork the Python Packaging Guide repository into your personal GitHub space.

*__TODO__: This section should show a beginner user how to fork a repository in GitHub.*

## Contributing via the GitHub website

### How to edit a MarkDown file

*__TODO__: This section should show how to use the GitHub interface to edit and previewing a Markdown file.*

### How to commit your changes

*__TODO__: This section should show how to commit changes via the GitHub interface.*

## Contributing locally on your computer

### Clone your forked repository

*__TODO__: This section should show how to clone a repository from GitHub into your computer.*

### Create a new branch

*__TODO__: This section should show how to create a new branch.*

### Create a virtual environment

*__TODO__: This section should show how to create a virtual environment using venv.*

### Install the development dependencies

*__TODO__: This section should show how to install the development dependencies defined in pyproject.toml.*

### Commit your changes

*__TODO__: This section should describe how to commit from the command line.*

### How to build the guide locally

*__TODO__: This section should describe the different sessions in nox related to building the docs: docs, docs-test, docs-live. It should also show how to see the guide built locally, by opening the right file in the browser or using the live version from docs-live*

### Before you submit your pull request

*__TODO__: This section should describe what steps a user should follow before submitting the pull request: build the docs, verify your changes look correct, etc.*

## Submitting a pull request with your contribution

### How to make a pull request

*__TODO__: This section should describe how to make a pull request in GitHub.*

### What happens when you submit a pull request (CI/CD)

*__TODO__: This section should describe how to see the results of the CD/CI checks and how to get more information about errors*

### What to expect from the review process

*__TODO__: This section should describe how review happens in GitHub, how see the comments, and how to submit changes (push a new branch)*

## Additional help

### How to get help

*__TODO__: This section should describe the options for finding more help in case beginner contributors need more help (e.g., create an issue, post in a forum, etc).*

### Additional resources

*__TODO__: It should also include links to beginner documentation, like the GitHub docs.*

## Annex

### Code examples

This guide uses the [literalinclude Sphinx directive](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-literalinclude)
whenever possible to keep code and prose separate. Code for use in the documentation is kept in the `examples/` folder.

(referencing-code-in-documentation)=
#### Referencing code in documentation

If an example is present elsewhere in the documentation that you want to use, you can copy the `literalinclude`
directive verbatim and the examples will stay in sync.

If you already see code in the examples folder that you can use for new documentation, a new `literalinclude` can be
made to extract it into the site. Only a relative path to the code is required for a working `literalinclude`, but you
should in almost all cases also provide a `:language:` and `:lines:`. The former makes code examples prettier, and the
later can protect your example from future modifications to the code.

**Pro tip**: As an alternative to `:lines:` there are also the `:start-after:`, `:start-at:`, `:end-before:`, and
`:end-at:` options. And if the example code is Python, `:pyobject:` can be an even more future-proof way to keep the
same documentation content even through code refactors.

If you need example code that doesn't yet exist in `examples/` see creating code for documentation](#creating-code-for-documentation).

(creating-code-for-documentation)=
#### Creating code for documentation

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
