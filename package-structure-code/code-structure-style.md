# Code Style and Structure 

pyOpenSci suggests that you follow the [python PEP8 style guide](https://peps.python.org/pep-0008/) for decisions 
related to styling your open source Python packages code.  

We also suggest that you consider:
1. adhering to a commonly used docstring format. If you use xx or xx then it will further support easy API documentation using tools such as Sphinx autodoc.
2. Adding a linter to your development build that will catch style issues and tell you how to reformat your code as needed. (see below for more )
3. Add a code styler such as black or blue to keep the entire package consistent.

## Docstring styles

```{note}
what is a docstring...
https://peps.python.org/pep-0257/#what-is-a-docstring
```

* https://numpydoc.readthedocs.io/en/latest/
* Ask on slack this week what resources people like for this

## Code linters

Code linters are tools that look at your code and identify problems such as:

* unused variables
* invalide styles 
* missing docstrings 
* incorrect spacing 

and more 

Linters can be run as a command-line tool and/or can also be setup as a part of 
your favorite programming tool (e.g. VScode, pycharm, etc).

Some maintainers stup a pre-commit hook in their reporisoty. A hook will check 
your code prior to your committing it. IT will itendify issues and if the 
hook includes a styler, will fix any issues with code style before you commit. 

This type of setup can be helpful to ensure code consistency associated with new 
contributions... 


Regardless of how you set this up, We suggest setting up a linter and a code styler 
as they will give you automatic feedback about your code's structure as you (or a contributor) write it.

## Some popular linters 

* A very popular code linter for Python is [flake8](https://flake8.pycqa.org/en/latest/).
`Flake8` checks if the code is according to [PEP 8](https://www.python.org/dev/peps/pep-0008/), 
the Python Enhancement Proposal about `Style Guide for Python Code`.


See also:

- [mypy](http://mypy-lang.org/)
- [numpydoc](https://numpydoc.readthedocs.io/en/latest/)
- [pydocstyle](https://github.com/PyCQA/pydocstyle)


## Code stylers

Code stylers are tools that fix styling issues in a file, formatting it automatically.
Code *styling* is different from code *linting* because it doesn't change the functionality
of your code at all, it *only* changes how it looks. 
Using an automatic formatting tool helps to keep the source code within specification
and also helps review workflow. While stylers might cause your code to look differently
than you would have chosen, many projects have adopted them in order to have a single
code style that is consistent across projects.

Currently, [black](https://github.com/psf/black) is the most popular code styler for Python.
It will format the code according the `PEP 8` and should work fine with `flake8` (maybe it needs
some extra configuration as, for example, `line-length`).
 
See also:

- [isort](https://github.com/timothycrosley/isort)


## Git pre-commit hook

Git pre-commit hook is a useful tool that checks your code automatically when you run a `git commit` and,
if it fails, the `git commit` is canceled. This is often used to make sure
that the changes to your code match a particular style, or that there are no
code linting errors.

For example, if you want that `git commit` checks if your code matches the PEP8 specification,
you can configure a git flake8 pre-commit hook:


```yaml
# file: .pre-commit-config.yaml
repos:
  - repo: https://gitlab.com/pycqa/flake8
    rev: '3.7.9'
    hooks:
    -   id: flake8

```

```{note}
See [the flake8 hooks explanation](https://flake8.pycqa.org/en/latest/user/using-hooks.html) for more details.
```

This file specifies a hook that will be triggered automatically before each `git commit`,
in this case, it specifies a flake8 using version `3.7.9`.

Before you can see any change, first you should install `pre-commit` library. 
One way to do it is using `pip` or `conda`:

```sh
pip install pre-commit

# or

conda install -c conda-forge pre-commit
```

Now, you can install your pre-commit hook using `pre-commit install`, and it will create the hook based on
the file `.pre-commit-config.yaml`.

Before each `git commit` command, in this case, git will run `flake8` and, if it fails, the `commit` will be canceled.


## What git pre-commit hook should I use?

The git pre-commit hook you should use, depends on the project needs or the team needs.
Some pre-commit hooks you can find useful would be:

- [flake8](https://flake8.pycqa.org/en/latest/user/using-hooks.html)
- [mypy](https://github.com/pre-commit/mirrors-mypy)
- [black](https://black.readthedocs.io/en/stable/integrations/source_version_control.html)
- [isort](https://github.com/pre-commit/mirrors-isort)

If you want more information about `pre-commit`, check out its [documentation](https://pre-commit.com/).
