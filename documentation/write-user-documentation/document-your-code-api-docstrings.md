# Document the code in your package's API using docstrings

## What is an API?
API stands for **A**pplied **P**rogramming **I**nterface. When
discussed in the context of a (Python) package, the API refers to
the functions, methods and classes that a package maintainer creates for users.

A simple example of a package API element:
For instance, a package might have a function called `add_numbers()`
that adds up a bunch of numbers. To add up numbers, you as the user
simply call `add_numbers(1,2,3)` and the package function calculates the value and returns `6`. By calling the `add_numbers` function, you are
using the package's API.

Package APIs consist of functions and/or classes, methods and attributes that create a user interface (known as the API).

## What is a docstring and how does it relate to documentation?
In Python a docstring refers to text in a function, method or class
that describes what the function does and its inputs and outputs. Python programmers usually refer to the inputs to functions as ["parameters"](https://docs.python.org/3/glossary.html#term-parameter) or ["arguments"](https://docs.python.org/3/faq/programming.html#faq-argument-vs-parameter), and the outputs are often called "return values"

The docstring is thus important for:

* When you call `help()` in Python, for example, `help(add_numbers)`, the text of the function's docstring is printed. The docstring thus helps a user better understand how to applying the function more effectively to their workflow.
* When you build your package's documentation, the docstrings can be also used to automagically create full API documentation that provides a clean view of all its functions, methods, attributes, and classes.

```{tip}
Example API Documentation for all functions, methods, attributes and classes in a package.
* [View example high level API documentation for the Verde package. This page lists every function and class in the package along with a brief explanation of what it does](https://www.fatiando.org/verde/latest/api/index.html)
* [You can further dig down to see what a specific function does within the package by clicking on an API element](https://www.fatiando.org/verde/latest/api/generated/verde.grid_coordinates.html#verde.grid_coordinates)
```

## Python package API documentation

If you have a descriptive docstring for every user-facing
class, method, attribute and/or function in your package (*within reason*), then your package's API is considered well-documented.

In Python, this means that you need to add a docstring for
every user-facing
class, method, attribute and/or function in your package (*within reason*) that:

* Explains what the function, method, attribute or class does
* Defines the `type` inputs and outputs (ie. `string`, `int`, `np.array`)
* Explains the expected output `return` of the object, method or function.

### Three Python docstring formats and why we like NumPy style

There are several Python docstring formats that you can chose to use when documenting
your package including:

* [NumPy-style](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard)
* [google style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
* [reST style](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html)

<!-- https://peps.python.org/pep-0287/ - 2002 pep 287-->
We suggest using [NumPy-style docstrings](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard) for your
Python documentation because:

* NumPy style docstrings are core to the scientific Python ecosystem and defined in the [NumPy style guide](https://numpydoc.readthedocs.io/en/latest/format.html). Thus you will find them widely used there.
* The Numpy style docstring is simplified and thus easier-to-read both in the code and when calling `help()` in Python. In contrast, some  feel that reST style docstrings is harder to quickly scan, and can take up more lines of code in modules.

```{tip}
If you are using NumPy style docstrings, be sure to include the [sphinx napoleon
extension](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html) in your documentation `conf.py` file. This extension allows Sphinx
to properly read and format NumPy format docstrings.
```

### Docstring examples Better and Best

Below is a good example of a well documented function. Notice that this
function's docstring describes the function's inputs and the function's output
(or return value). The initial description of the function is short (one line).
Following that single line description there is a slightly longer description of
what the function does (2 to 3 sentences). The return of the function is also
specified.

```Python
def extent_to_json(ext_obj):
    """Convert bounds to a shapely geojson like spatial object.

    This format is what shapely uses. The output object can be used
    to crop a raster image.

    Parameters
    ----------
    ext_obj : list or geopandas.GeoDataFrame
        If provided with a `geopandas.GeoDataFrame`, the extent
        will be generated from that. Otherwise, extent values
        should be in the order: minx, miny, maxx, maxy.

    Returns
    -------
    extent_json: A GeoJSON style dictionary of corner coordinates
    for the extent
        A GeoJSON style dictionary of corner coordinates representing
        the spatial extent of the provided spatial object.
    """
```

<!-- I can't seem to get doc targets across pages to work-->
(docstring_best_practice)=
### Best: a docstring with example use of the function

This example contains an example of using the function that is also tested in
sphinx using [doctest](https://docs.python.org/3/library/doctest.html).

```Python
def extent_to_json(ext_obj):
    """Convert bounds to a shapely geojson like spatial object.

    This format is what shapely uses. The output object can be used
    to crop a raster image.

    Parameters
    ----------
    ext_obj : list or geopandas.GeoDataFrame
        If provided with a `geopandas.GeoDataFrame`, the extent
        will be generated from that. Otherwise, extent values
        should be in the order: minx, miny, maxx, maxy.

    Returns
    -------
    extent_json : A GeoJSON style dictionary of corner coordinates
    for the extent
        A GeoJSON style dictionary of corner coordinates representing
        the spatial extent of the provided spatial object.

    Example
    -------
    Convert a `geopandas.GeoDataFrame` to an extent dictionary:

    >>> import geopandas as gpd
    >>> import earthpy.spatial as es
    >>> from earthpy.io import path_to_example

	We start by loading a Shapefile.

    >>> rmnp = gpd.read_file(path_to_example('rmnp.shp'))

	And then use `extent_to_json` to do the conversion from `shp` to
    `geopandas.GeoDataFrame`.

    >>> es.extent_to_json(rmnp)
    {'type': 'Polygon', 'coordinates': (((-105.4935937, 40.1580827), ...),)}

    """

```

```{figure} /images/sphinx-rendering-extent-to-json-earthpy.png
---
name: earthpy-json-example
width: 80%
---
Using the above NumPy format docstring in sphinx, the autodoc extension will
create the about documentation section for the `extent_to_json` function. The
output of the `es.extent_to_json(rmnp)` command can even be tested using
doctest adding another quality check to your package.
```


## Using doctest to run docstring examples in your package's methods and functions
<!-- This link isn't working no matter how i create the target. not sure
why -->
Above, we provided some examples of good, better, best docstring formats. If you are using Sphinx to create your docs, you can add the [doctest](https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html) extension to your Sphinx build. Doctest provides an additional; check for docstrings with example code in them.
Doctest runs the example code in your docstring `Examples` checking
that the expected output is correct. Similar to running
tutorials in your documentation, `doctest` can be a useful step that
assures that your package's code (API) runs as you expect it to.

```{note}
It's important to keep in mind that examples in your docstrings
help users using your package. Running `doctest` on those examples provides a
check of your package's API. doctest ensures that the functions and methods in your package
run as you expect them to. Neither of these items replace a separate,
stand-alone test suite that is designed to test your package's core functionality
across operating systems and Python versions.
```

Below is an example of a docstring with an example.
doctest will run the example below and test that if you provide
`add_me` with the values 1 and 3 it will return 4.


```python
def add_me(aNum, aNum2):
    """A function that prints a number that it is provided.

    Parameters
    ----------
    aNum : int
        An integer value to be printed

    Returns
    -------
        Prints the integer that you provide the function.

    Examples
    --------
    Below you can see how the `print_me` function will print a number that
    you provide it.

    >>> add_me(1+3)
    4

    """

    return aNum + aNum2


```


## Beyond docstrings: type hints

We use docstrings to describe data types that we pass into functions as parameters or 
into classes as attributes. *We do it with our users in mind.*

**What with us – developers?** We can think of ourselves and the new contributors, 
and start using *type hinting* to make our journey safer!

There are solid reasons why to use type hints:

- Development and debugging are faster,
- We clearly see data flow and its transformations,
- We can use tools like `mypy` or integrated tools of Python IDEs for static type checking and code debugging.

We should consider type hinting if our package performs data processing, 
functions require complex inputs, and we want to lower the entrance barrier for our contributors. 
The icing on the cake is that the code in our package will be aligned with the best industry standards.

But there are reasons to *skip* type hinting:

- Type hints may make code unreadable, especially when a parameter’s input takes multiple data types and we list them all,
- Writing type hints for simple scripts and functions that perform obvious operations don't make sense.

Fortunately for us, type hinting is not all black and white. 
We can gradually describe the parameters and outputs of some functions but leave others as they are. 
Type hinting can be a task for new contributors to get them used to the package structure.
That way, their learning curve about data flow and dependencies between API endpoints will be smoother.

## Type hints in practice

Type hinting was introduced with Python 3.5 and is described in [PEP 484](https://peps.python.org/pep-0484/). 
**PEP 484** defines the scope of type hinting. Is Python drifting towards compiled languages with this feature?
It is not. Type hints are optional and static. They will work like that in the future until Python is Python.
The power of type hints lies somewhere between docstrings and unit tests, and with it, we can avoid many bugs 
throughout development.

We've seen type hints in the simple example earlier. Let's come back to it and change it slightly:


```python
from typing import Dict, List


def extent_to_json(ext_obj: List) -> Dict:
    """Convert bounds to a shapely geojson like spatial object."""
    ...

```

Here we focus on the new syntax. First, we described the parameter `ext_obj` as the `List` class. How do we do it? 
Add a colon after the parameter (variable) and the name of a class that is passed into a function. 
It’s not over. Do you see, that the function definition after closing parenthesis is expanded? 
If we want to inform the type checker what the function returns, then we create the arrow sign `->` that points to a returned type, 
and after it, we put the function’s colon. Our function returns a Python dictionary (`Dict`).

```{note}
We have exported classes `List` and `Dict` from the `typing` module, but we may use 
`list` or `dict` keywords instead. We will achieve the same result. 
Capitalized keywords are required when our package uses Python versions that are lower than
Python 3.9. Python 3.7 will be deprecated in June 2023, and Python 3.8 in October 2024.
Thus, if your package supports the whole ecosystem, it should use the `typing` module syntax.
```

### Type hints: basic example

The best way to learn is by example. We will use the [pystiche](https://github.com/pystiche/pystiche/tree/main) package.
To avoid confusion, we start with a mathematical operation:

```python
import torch


def _norm(x: torch.Tensor, dim: int = 1, eps: float = 1e-8) -> torch.Tensor:
    ...

```

The function has three parameters:

- `x` that is required, and its type is `torch.Tensor`,
- `dim`, optional `int` with a default value equal to `1`,
- `eps`, optional `float` with a default value equal to `1e-8`.

As we see, we can use basic data types to mark simple variables. The basic set of those types is:

- `int`,
- `float`,
- `str`,
- `bool`
- `complex`.

We will most frequently use those types within simple functions that are *close to data*.
However, sometimes our variable will be a data structure that isn't built-in within Python itself 
but comes from other packages:

- `Tensor` from `pytorch`,
- `ndarray` from `numpy`,
- `DataFrame` from `pandas`,
- `Session` from `requests`.

To perform type checking, we must import those classes. Then we can set those as a parameter's type.
The same is true if we want to use classes from within our package (but we should avoid **circular imports**, 
the topic we will uncover later).

### Type hints: complex data types

We can use type hints to describe other objects available in Python.
A little sample of those objects are: 

- `List` (= `list`)
- `Dict` (= `dict`)
- `Tuple` (= `tuple`)
- `Set` (= `set`)

How do `pystiche` developers use those objects in their code? Let's take a look at the example below:

```python
from typing import List, Optional
import torch


def _extract_prev(self, idx: int, idcs: List[int]) -> Optional[str]:
    ...

```

The function has two parameters. The parameter `idcs` is a list of integers. We may write it as `List[int]` or `List` without 
square brackets and data type that is within a list.

The `_extract_prev` function returns the `Optional` type. It is a special type that describes inputs and output 
that can be `None`. There are more interesting types that we can use in our code:

- `Union` – we can use it to describe a variable of multiple types. An example could be:

```python
from typing import List, Union
import numpy as np
import pandas as pd


def process_data(data: Union[np.ndarray, pd.DataFrame, List]) -> np.ndarray:
    ...

```

What's the problem with the example above? The function definition becomes unreadable with more data types passed into the parameter `data`. 
We have two solutions for this issue. The first one is to use the `Any` type, which is a wildcard that is equal to not passing any type.

```python
from typing import Any


def process_data(data: Any) -> np.ndarray:
    ...

```

The second solution is to think what is a high-level representation of a passed data type. The examples are:

- `Sequence` – we can use it to describe a variable as a sequence of elements. Sequential are `list`, `tuple`, `range` and `str`.
- `Iterable` – we can use it to describe an iterable variable. Iterables are `list`, `tuple`, `range`, `str`, `dict` and `set`.
- `Mapping` – we can use it to describe a variable that is a mapping. Mappings are `dict` and `defaultdict`.
- `Hashable` – we can use it to describe a hashable variable. Hashables are `int`, `float`, `str`, `tuple` and `frozenset`.
- `Collection` - we can use it to describe a collection variable. Collections are `list`, `tuple`, `range`, `str`, `dict`, `set` and `frozenset`.

Thus, the function could look like this:

```python
from typing import Iterable


def process_data(data: Iterable) -> np.ndarray:
    ...

```

### Type hints: unique objects and interesting cases

The `typing` module provides us with more objects that we can use to describe our variables. 
An interesting object is `Callable` that we can use to describe a variable that is a function. Usually,
when we write decorators or wrappers, we use the `Callable` type. The example in the context of the `pystiche` package:

```python
from typing import Callable


def _deprecate(fn: Callable) -> Callable:
    ...

```

The `Callable`can be used as a single word or a word with square brackets with two parameters: `Callable[[arg1, arg2], return_type]`. 
The first parameter is a list of arguments, and the second is a function output's data type.

There is an important case around type hints. Sometimes we want to describe a variable that comes from within 
our package. Usually, we can do it without problems:

```python
from my_package import my_data_class


def my_function(data: my_data_class) -> None:
    ...

```

And it will work fine. But we may encounter *circular imports* that need to be fixed. What is a *circular import*? 
It is a case when we want to import module B into module A, but module A is already imported into module B. 
We are importing the same module into itself. The issue is rare when we program without type
hinting. However, with type hints, it could be tedious.

Thus, if you encounter this error:

```python
from my_package import my_data_class


def my_function(data: my_data_class) -> None:
    ...

```

```shell
ImportError: cannot import name 'my_data_class' from partially initialized module 'my_package' (most likely due to a circular import) (/home/user/my_package/__init__.py)
```

Then you should use the `typing.TYPE_CHECKING` clause to avoid circular imports. The example:

```python
from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from my_package import my_data_class


def my_function(data: my_data_class) -> None:
    ...

```

Unfortunately, the solution is *dirty* because we have to 
use the `if TYPE_CHECKING` clause and `from __future__ import annotations` import to make it work. It make our
script messier! Type hinting is not only the roses and butterflies!

The nice feature of type hinting is that we can define variable's type within a function:

```python
from typing import Dict
import numpy as np


def validate_model_input(data: np.ndarray) -> Dict:
    """
    Function checks if dataset has enough records to perform modeling.
    
    Parameters
    ----------
    data : np.ndarray
        Input data.
    
    Returns
    -------
    : Dict
        Dictionary with `data`, `info` and `status` to decide if pipeline can proceed with modeling.
    """
    
    output: Dict = None  # type hinting
    
    # Probably we don't have the lines below yet
    
    # if data.shape[0] > 50:
    #     output = {"data": data, "info": "Dataset is big enough for statistical tests.", "status": True}
    # else:
    #     output = {"data": data, "info": "Dataset is too small for statistical tests.", "status": False}
        
    return output

```

We will use this feature rarely. The most probable scenario is when we start defining a function and its output, but 
we don't know how we will process data. In this context, we can still run type checking to be sure that the
function behaves as we expect within the newly designed pipeline. 

(Another scenario: we will be forced to add type hints to silence dynamic type checkers from some IDEs ;) ).


### Type hinting: final remarks

There are tools designed for static type checking. The most popular one is [`mypy`](https://mypy.readthedocs.io/en/stable/).
Adding it to your Continuous Integration (CI) pipeline is a good idea.
Other tools are integrated with popular IDEs like `PyCharm` or `VSCode`; most are based on `mypy` logic.

The last thing to remember is that **type hints are optional in all our functions, and we can introduce them gradually, 
which won't damage our code and output generated by CI type checking tools**.  
It is a very convenient way of using this extraordinary feature!
