# Python Package Code Style & Linting

Consistent code format and style is useful to both your package 
and across the scientific python ecosystem because using similar 
formats makes code easier to read.

For instance, if you saw a sentence like this one without any 
spaces it would take your brain longer to process it. 

```
forinstanceifyousawasentencelikethisonewithoutany... 
```

pyOpenSci requires you to follow standard Python PEP 8 format 
rules. But we also suggest that you use a code formatter too. 
If more packages start using formatter, we will slowly gain consistency 
across the scientific ecosystem. Code across packages will then 
be consistent and as such easier to scan, understand and contribute to.

### pyOpenSci requirements for code style and format 

pyOpenSci doesn't require you to use a specific code format tool. However we do look for 
consistency and readbility in code style. pyOpenSci also requires that you 
follow the [python PEP8 style guide](https://peps.python.org/pep-0008/) for decisions 
related to styling your open source Python packages code.  We also require that your code adheres 
to the PEP8 style guidelines.  

We do strongly recommend that you implement a code styler tool suite in your 
package as it will save you and your maintainer team time. It will also ensure 
that format and style is consistent accross all of your code. 


Below you will find a list of commonly used Python code formatters. 
Currently, [black](https://github.com/psf/black) is the most popular code styler for Python.

## Code format and style
We suggest that you use a code formatter such as [black](https://black.readthedocs.io/en/stable/) or 
[blue](https://blue.readthedocs.io/en/latest/)  to ensure your 
code is consistently formatted throughout your package. Using an existing, 
widely used tool will avoid lengthy discussions with contributors and other 
maintainers about personalized code format preferences during reviews. 

## Code linters and formatters
A code linter is a tool that will review your code and identify errors or 
issues. A linter typically does not actually modify the code for you. It will 
just tell you what the error is and on what line it was discovered.

### flake8 is a preferred code linting tool for Python packages

To adhere to Python `pep8` format standards, we suggest that you use 
[flake8](https://flake8.pycqa.org/en/latest/). 

Below you can see the output of running 
`flake8 filename.py` at the command line for a python file within a package 
called `stravalib`. The line length standard for PEP8 is 79 characters. flake8 
will:
* flags every line in your code that extends beyond 79 characters
* spacing issues that conflict with pep8 such as missing spaces after commas

It also flags unused imports in your modules. 

Notice below that you run flak8 in the command line and it returns a list of 
each error it finds in a file. All of this output is at the command line. The 
python file is not modified. 

```bash
(stravalib-dev) username@computer stravalib % flake8 stravalib/model.py
stravalib/model.py:8:1: F401 'os' imported but unused
stravalib/model.py:29:80: E501 line too long (90 > 79 characters)
stravalib/model.py:34:80: E501 line too long (95 > 79 characters)
stravalib/model.py:442:80: E501 line too long (82 > 79 characters)
stravalib/model.py:443:39: E231 missing whitespace after ','
stravalib/model.py:493:20: E225 missing whitespace around operator
stravalib/model.py:496:80: E501 line too long (82 > 79 characters)
```

### Black and Blue 
While `flake8` is a linter that identifies issues with your code, [black](https://black.readthedocs.io/en/stable/) and also 
[blue](https://blue.readthedocs.io/en/latest/) (which wraps around black) are code 
formatters. Both black and blue will manually (and unapologetically) 
fix spacing issues and ensure format is consistent throughout your package.

These formatters leave you more time to work on code function rather than 
format. Black and blue do 
generally adhere to pep8 style guidelines with some exceptions. 

* Black defaults to a line width of 88 (79 + 10%) rather than the 79 character `pep8` specification (but this setting can be manually overwritten in your black setup)
* Black and blue will not adjust line length in your comments or docstrings. 
* Neither tool will review and fix import order (you need isort to do that).

Blue adresses a few format decisions in black that some maintainers do not like. 
[You can compare the differences here](https://blue.readthedocs.io/en/latest/#so-what-s-different) and decide which tool suites your preferences! 

```{tip}
If you are interested in seeing how black will format your code, you can 
use the [black playground](https://black.vercel.app/?version=stable&state=_Td6WFoAAATm1rRGAgAhARYAAAB0L-Wj4ARsAnNdAD2IimZxl1N_WlkPinBFoXIfdFTaTVkGVeHShArYj9yPlDvwBA7LhGo8BvRQqDilPtgsfdKl-ha7EFp0Ma6lY_06IceKiVsJ3BpoICJM9wU1VJLD7l3qd5xTmo78LqThf9uibGWcWCD16LBOn0JK8rhhx_Gf2ClySDJtvm7zQJ1Z-Ipmv9D7I_zhjztfi2UTVsJp7917XToHBm2EoNZqyE8homtGskFIiif5EZthHQvvOj8S2gJx8_t_UpWp1ScpIsD_Xq83LX-B956I_EBIeNoGwZZPFC5zAIoMeiaC1jU-sdOHVucLJM_x-jkzMvK8Utdfvp9MMvKyTfb_BZoe0-FAc2ZVlXEpwYgJVAGdCXv3lQT4bpTXyBwDrDVrUeJDivSSwOvT8tlnuMrXoD1Sk2NZB5SHyNmZsfyAEqLALbUnhkX8hbt5U2yNQRDf1LQhuUIOii6k6H9wnDNRnBiQHUfzKfW1CLiThnuVFjlCxQhJ60u67n3EK38XxHkQdOocJXpBNO51E4-f9z2hj0EDTu_ScuqOiC9cI8qJ4grSZIOnnQLv9WPvmCzx5zib3JacesIxMVvZNQiljq_gL7udm1yeXQjENOrBWbfBEkv1P4izWeAysoJgZUhtZFwKFdoCGt2TXe3xQ-wVZFS5KoMPhGFDZGPKzpK15caQOnWobOHLKaL8eFA-qI44qZrMQ7sSLn04bYeenNR2Vxz7hvK0lJhkgKrpVfUnZrtF-e-ubeeUCThWus4jZbKlFBe2Kroz90Elij_UZBMFCcFo0CfIx5mGlrINrTJLhERszRMMDd39XsBDzpZIYV4TcG7HoMS_IF8aMAAAxI-5uTWXbUQAAY8F7QgAAP01Vc6xxGf7AgAAAAAEWVo=)
```


### Isort 

Python imports refer to the python packages that a module in your package require to run. Following conventional standards, 
all Python imports should be called at the top of your code (.py)files.

In addition to these imports all being at the top of each code 
file (or each module) [PEP 8 has specific standards for the order of these imports](https://peps.python.org/pep-0008/#imports). These standards are listed below:


> Imports should be grouped in the following order:
>
> * Standard library imports.
> * Related third party imports.
> * Local application/library specific imports.

While flake8 will identify unused imports in your code, it won't 
fix or identify issues with the order of those imports.

`isort` will identify where imports in your code are out of 
order. It will then modify your module, automatically reordering 
all imports. This leaves you with one less
thing to think about when cleaning up your code. Further, if 
setup as a precommit hook, isort and a continuous integration 
check, using isort will ensure that new contributors, who may 
be less familiar with pep 8 standards, follow
the pep 8 import order standards as well. 

### Example application of isort

Code imports before `isort` is run:

Below, the exc module is a part of starvalib which is a 
third party package. `abc` and `logging` are core `Python` packages 
distributed with `Python`. Also notice that there are extra 
spaces in the imports listed below. 

```python
from stravalib import exc
import abc
import logging

from collections.abc import Sequence


from stravalib import unithelper as uh
```
Run:
`isort stravalib/model.py`

Python module after `isort` has been run

```python
import abc
import logging
from collections.abc import Sequence

from stravalib import exc
from stravalib import unithelper as uh
```


## How to setup a code formatter to support your 

### Linters, code formatters and your favorite coding tools 
Linters can be run as a command-line tool as shown above. They also can 
be run within your favorite coding tool (e.g. VScode, pycharm, etc). Tools like 
`flake8` and `black` can often be integrated with your favorite code editors to 
run automatically when you save a file. 

### Linters, code formatters and pre-commit hooks
Some maintainers setup a `pre-commit hook` in their repository.  

This section will make the most sense if you are familiar with git. 
You can skip it if you are not yet familiar with git commit! 

A pre-commit hook cna be best described as a trigger that happens making a 
tool run when you type and run 
`git commit -m "message here` at the command line. 

For instance, if you setup the black code formatter as a pre-commit hook, 
when you go to commit changes to a code file and hit enter, black will run 
on your the code files in your commit. It will update any files to match 
black format standards. You can then retype the commit and push files to 
GitHub that have been formatted by black.

Using pre-commit hooks is helpful to ensure code consistency for edits to your 
code files.

```{note}
If you already have a Python package and you want to apply a code formatter, you 
may need to go through the initial effort of formatting all of your code files. 

Running a tool like black is normally quick. However implementing fixes found by 
flake8 can take a bit of time. Make sure that you allocate a bit of time to 
format your code. Also make sure that other maintainers are not actively 
updating your code base as an initial commit with black format changes will 
likely change a significant amount of your code. This is a recipe for merge 
conflicts!
```

## Setting up a `git` pre-commit hook

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
in this case, it specifies a `flake8` using version `3.7.9`.

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

## Summary 
pyOpenSci suggests setting up a linter and a code styler for 
your package, regardless of whether you use pre-commit hooks, CI 
or other infrastructure to manage code format. Setting up these 
tools will give you automatic feedback about your code's 
structure as you (or a contributor) write it. And using tools 
like black or blue that format code for you, reduce effort that 
you need to make surrounding decisions around code format and 
style. 