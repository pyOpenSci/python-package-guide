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
You can do this by clicking the "Fork" button in the top right corner of the repository page.

[Learn more: Fork and Clone GitHub Repos](https://datascienceskills.org/lessons/git-github/git-intro/3-fork-clone/) is a good resource to learn more about forking.

To fork a repo,

1. Make sure you are logged into GitHub.

2. Go to the repo you would like to fork, in this case the [Python Packaging Guide](https://www.github.com/pyopensci/python-package-guide) repo.

3. In the top right-hand corner of the page there is a 'Fork' button. Click that button. You will be brought to a new page where you will 'Create a new fork'. Feel free to keep all the default inputs and click 'Create fork'. This will create a copy of the repo at `https://github.com/<username>/python-package-guide`, where `<username>` is your GitHub username.

<img width="395" alt="fork_repo" src="https://github.com/user-attachments/assets/949223fb-b58b-4b6d-85db-003bd117da46">


## Contributing via the GitHub website

### How to edit a MarkDown file

The Python Packaging Guide is written in myST, a variant of MarkDown. You can edit the files directly in the GitHub website.
To do so, navigate to the file you want to edit and click the pencil icon in the top right corner of the file.

```{figure} images/contributing/edit-button-pencil.png
---
name: edit-button-pencil in GitHub
width: 80%
alt: Edit button in GitHub
---
An image showing how to edit a file in GitHub. The pencil icon is highlighted with a red rectangle.

```{figure} images/contributing/edit-file.png
---
name: edit-file in GitHub
width: 80%
alt: Edit file in GitHub
---
An image showing when a file is being edited in GitHub. The file content is displayed in a text editor.
```

To preview your changes, click the "Preview changes" tab.

```{figure} images/contributing/preview-changes.png
---
name: preview-changes in GitHub
width: 80%
alt: Preview changes in GitHub
---
An image showing how to preview changes in GitHub. The file content is displayed in a text editor. The preview changes tab is highlighted with a red rectangle.
```

### How to commit your changes

When you are done editing the file, scroll down to the bottom of the page. You will see a section called "Commit changes".
Here you can write a title and a description for your changes. Make sure to write a clear and concise title that describes the changes you made.

```{figure} images/contributing/commit-changes.png
---
name: commit-changes in GitHub
width: 80%
alt: Commit changes in GitHub
---
An image showing how to commit changes in GitHub. The commit message is displayed in a text editor. The commit changes section is highlighted with a red rectangle.
```

After writing your commit message, click the "Commit changes" button to save your changes.

## Contributing locally on your computer

### Clone your forked repository

To clone your forked repository to your computer, you need to copy the URL of your forked repository and run the following command in your terminal:

```bash
git clone <URL>
```
Replace `<URL>` with the URL of your forked repository. You can find the URL by clicking the green "Code" button on your forked repository page.

```{figure} images/contributing/clone-repository.png
---
name: clone-repository in GitHub
width: 80%
alt: Clone repository in GitHub
---
An image showing how to clone a repository in GitHub. The URL of the repository is displayed in a text editor. The code button is highlighted with a red rectangle.
```

### Create a new branch

Before making any changes, you should create a new branch to work on. This will help keep your changes separate from the main branch and make it easier to submit a pull request.

To create a new branch, run the following command in your terminal:

```bash
git checkout -b <branch-name>
```

### Create a virtual environment

To build the guide locally, you need to create a virtual environment and install the dependencies. You can do this by running the following commands in your terminal:

- **On Windows**:
    ```bash
    python -m venv .venv
    .venv\Scripts\activate
    ```

- **On MacOS and Linux**:
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

### Install the development dependencies

To install the development dependencies, run the following command in your terminal:

```bash
python -m pip install -e .[dev]
```

### Commit your changes

After making your changes, you need to commit them to your local repository. To do this, run the following commands in your terminal:

- To see the changes you made:
    ```bash
    git status
    ```
- To add the changes to the staging area:
    ```bash
    git add .
    ```
- To commit the changes:
    ```bash
    git commit -m "Your commit message here"
    ```
Replace `"Your commit message here"` with a clear and concise message that describes the changes you made.

### How to build the guide locally

To build the guide locally, you can use the `nox` command. This will run the default `nox` session, which builds the guide and opens it in your browser.

To see the different sessions available, you can run the following command in your terminal:

```bash
nox --list-sessions
```
There are different sessions in nox related to building the docs: `docs`, `docs-test`, `docs-live`. You can run them by specifying the session name after the `nox` command.

- `docs`: this session builds the guide and opens it in your browser.
    ```bash
    nox -e docs
    ```
    To see the guide built locally, open the file `_build/html/index.html` in your browser.

- `docs-test`: this session runs the tests for the guide.
    ```bash
    nox -e docs-test
    ```
    If the tests fail, you will see an error message in your terminal. You need to fix the errors before submitting your pull request.

- `docs-live`: this session builds the guide and opens it in your browser with live reloading.
    ```bash
    nox -e docs-live
    ```
    open the local version of the guide in your browser at ``localhost`` shown in the terminal.

### Before you submit your pull request

Before submitting your pull request, make sure to run the tests and check the formatting of your code.

```bash
nox -e docs-test
```
If the tests fail, you will see an error message in your terminal. You need to fix the errors before submitting your pull request.
Also make sure to check the formatting of your documentation by building the docs locally and checking that your changes look correct.


## Submitting a pull request with your contribution

### How to make a pull request

1. To open a pull request on GitHub, navigate to the main page of your forked repository and click on the "Pull requests" tab.

```{figure} images/contributing/pull-requests-tab.png
---
name: pull-requests-tab in GitHub
width: 80%
alt: Pull requests tab in GitHub
---
An image showing how to navigate to the pull requests tab in GitHub. The pull requests tab is highlighted with a red rectangle.
```

2. Click on the "New pull request" button.

```{figure} images/contributing/new-pull-request.png
---
name: new-pull-request in GitHub
width: 80%
alt: New pull request button in GitHub
---
An image showing how to create a new pull request in GitHub. The new pull request button is highlighted with a red rectangle.
```

3. Write a clear and concise title and description for your pull request. Make sure to describe the changes you made and why they are necessary.

### What happens when you submit a pull request (CI/CD)

Once you submit a pull request, a series of checks will be run to ensure that your changes do not introduce any bugs or errors. These checks include:

- **Code formatting and styles**: checks that your code is formatted correctly, by `pre-commit.ci - pr check`.
- **docs build**: checks that the documentation builds correctly, using `circleci`.

You will see the status of these checks in your pull request.

```{figure} images/contributing/pull-requests-checks.png
---
name: pull-requests-checks in GitHub
width: 80%
alt: Pull request checks in GitHub
---
An image showing the status of the checks in a pull request in GitHub. The checks are displayed in a table with a status icon next to each check. The checks are highlighted with a red rectangle.
```
If any of these checks fail, you will see an error message in your pull request. You need to fix the errors before your changes can be merged.

```{figure} images/contributing/pull-requests-checks-fails.png
---
name: pull-requests-checks-fails in GitHub
width: 80%
alt: Pull request checks failed in GitHub
---
An image showing the status of the checks in a pull request in GitHub. The checks are displayed in a table with a status icon next to each check. The checks that failed and the details link are highlighted with a red rectangle.
```

To get more information about the errors, you can click on the "Details" link next to the failed check.

### What to expect from the review process

Once you submit a pull request, a maintainer of the repository will review your changes and provide feedback. The review process may involve:

- **Comments**: the reviewer may leave comments on your pull request to ask questions or provide feedback.
- **Suggestions**: the reviewer may suggest changes to your code or documentation.
- **Approvals**: once the reviewer is satisfied with your changes, they will approve the pull request.

You can make changes to your pull request by pushing new commits to the branch. The pull request will be updated automatically with your new changes.

Once your pull request is approved, it will be merged into the main branch and your changes will be included in the guide.

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

If you need example code that doesn't yet exist in `examples/` see [creating code for documentation](#creating-code-for-documentation).

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
