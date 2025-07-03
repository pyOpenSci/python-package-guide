(api-docstrings)=
# Document the code in your package's API using docstrings

## What is an API?

API stands for **A**pplied **P**rogramming **I**nterface. When
discussed in the context of a (Python) package, the API refers to
the functions, classes, methods, and attributes that a package maintainer creates for users.

A simple example of a package API element:
For instance, a package might have a function called `add_numbers()`
that adds up a bunch of numbers. To add up numbers, you as the user
simply call `add_numbers(1,2,3)` and the package function calculates the value and returns `6`. By calling the `add_numbers` function, you are
using the package's API.

Package APIs consist of functions, classes, methods and attributes that create a user interface.

## What is a docstring and how does it relate to documentation?

In Python, a docstring refers to text in a function, method or class
that describes what the function does and its inputs and outputs. Python programmers usually refer to the inputs to functions as ["parameters"](https://docs.python.org/3/glossary.html#term-parameter) or ["arguments"](https://docs.python.org/3/faq/programming.html#faq-argument-vs-parameter), and the outputs are often called "return values"

The docstring is thus important for:

- When you call `help()` in Python, for example, `help(add_numbers)` will show the text of the function's docstring. The docstring thus helps a user better understand how to apply the function more effectively to their workflow.
- When you build your package's documentation, the docstrings can also be used to automatically create full API documentation that provides a clean view of all its functions, classes, methods, and attributes.

```{tip}
Example API Documentation for all functions, classes, methods, and attributes in a package.
* [View example high-level API documentation for the Verde package. This page lists every function and class in the package along with a brief explanation of what it does](https://www.fatiando.org/verde/latest/api/index.html)
* [You can further dig down to see what a specific function does within the package by clicking on an API element](https://www.fatiando.org/verde/latest/api/generated/verde.grid_coordinates.html#verde.grid_coordinates)
```

## Python package API documentation

If you have a descriptive docstring for every user-facing
class, method, attribute and/or function in your package (_within reason_), then your package's API is considered well-documented.

In Python, this means that you need to add a docstring for
every user-facing
class, method, attribute and/or function in your package (_within reason_) that:

- Explains what the function, method, attribute, or class does
- Defines the `type` inputs and outputs (ie. `string`, `int`, `np.array`)
- Explains the expected output `return` of the object, method or function.

(numpy-docstring)=
### Three Python docstring formats and why we like NumPy style

There are several Python docstring formats that you can choose to use when documenting
your package including:

- [NumPy-style](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard)
- [google style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
- [reST style](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html)

<!-- https://peps.python.org/pep-0287/ - 2002 pep 287-->

We suggest using [NumPy-style docstrings](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard) for your
Python documentation because:

- NumPy style docstrings are core to the scientific Python ecosystem and defined in the [NumPy style guide](https://numpydoc.readthedocs.io/en/latest/format.html). Thus you will find them widely used there.
- The Numpy style docstring is simplified and thus easier to read both in the code and when calling `help()` in Python. In contrast, some feel that reST style docstrings are harder to quickly scan, and can take up more lines of code in modules.

```{tip}
If you are using NumPy style docstrings, be sure to include the [sphinx napoleon
extension](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html) in your documentation `conf.py` file. This extension allows Sphinx
to properly read and format NumPy format docstrings.
```

### Docstring examples Better and Best

Below is a good example of a well-documented function. Notice that this
function's docstring describes the function's inputs and the function's output
(or return value). The initial description of the function is short (one line).
Following that single-line description, there is a slightly longer description of
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

<!-- This link isn't working no matter how i create the target. Not sure
why -->

Above, we provided some examples of good, better, best docstring formats. If you are using Sphinx to create your docs, you can add the [doctest](https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html) extension to your Sphinx build. Doctest provides an additional check for docstrings with example code in them.
Doctest runs the example code in your docstring `Examples` checking
that the expected output is correct. Similar to running
tutorials in your documentation, `doctest` can be a useful step that
assures that your package's code (API) runs as you expect it to.

```{note}
It's important to keep in mind that examples in your docstrings
help users using your package. Running `doctest` on those examples provides a
check of your package's API. The doctest ensures that the functions and methods in your package
run as you expect them to. Neither of these items replace a separate,
stand-alone test suite that is designed to test your package's core functionality
across operating systems and Python versions.
```

Below is an example of a docstring with an example.
doctest will run the example below and test that if you provide
`add_me` with the values 1 and 3 it will return 4.

```python
def add_me(num1, num2):
    """A function that sums two numbers.

    Parameters
    ----------
    num1 : int
        An integer value to be added
    num2 : int
        An integer value to be added

    Returns
    -------
       The integer sum of the provided numbers.

    Examples
    --------
    Below you can see how the `add_me` function will return a number.

    >>> add_me(1, 3)
    4

    """

    return num1 + num2


```

## Adding type hints to your docstrings

In the example above, you saw the use of numpy-style docstrings to describe data types
that are passed into functions as parameters or
into classes as attributes. In a numpy-style docstring you add those
types in the Parameters section of the docstring. Below you can see that
the parameter `num1` and `num2` should both be a Python `int` (integer) value.

```python
    Parameters
    ----------
    num1 : int
        An integer value to be added
    num2 : int
        An integer value to be added
```

Describing the expected data type that a function or method requires
helps users better understand how to call a function or method.

Type-hints add another layer of type documentation to your code. Type-hints
make it easier for new developers, your future self or contributors
to get to know your code base quickly.

Type hints are added to the definition of your function. In the example below, the parameters aNum and aNum2 are defined as being type = int (integer).

```python
def add_me(num1: int, num2: int):
    """A function that sums two numbers.
```

You can further describe the expected function output using `->`. Below
the output of the function is also an int.

```python
def add_me(num1: int, num2: int) -> int:
    """A function that sums two numbers.
```
(type-hints)=
### Why use type hints

Type hints:

- Make development and debugging faster,
- Make it easier for a user to see the data format inputs and outputs of methods and functions,
- Support using static type checking tools such as [`mypy`](https://mypy-lang.org/) which will check your code to ensure types are correct.

You should consider adding type hinting to your code if:

- Your package performs data processing,
- You use functions that require complex inputs
- You want to lower the entrance barrier for new contributors to help you with your code.

```{admonition} Beware of too much type hinting
:class: caution

As you add type hints to your code consider that in some cases:

- If you have a complex code base, type hints may make code more difficult to read. This is especially true when a parameter’s input takes multiple data types and you list each one.
- Writing type hints for simple scripts and functions that perform obvious operations don't make sense.
```

### Gradually adding type hints

Adding type hints can take a lot of time. However, you can add
type hints incrementally as you work on your code.

```{tip}
Adding type hints is also a great task for new contributors. It will
help them get to know your package's code and structure better before
digging into more complex contributions.
```
