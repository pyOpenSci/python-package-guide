# Best practices for writing user-facing documentation for your Python package 

```{important}
## Quick takeaways: best practices

Your package: 
* Should have a documentation website 
* All of its functions and classes (the API) documented
* Your package should use numpy-style docstrings 
* Your documentation landing page should direct users to 4 core sections: get started, documentation content, about and community.
* Documentation should include short quick-start tutorials
```

In addition to a well designed [README.md file](readme-file-best-practices), 
and a [CONTRIBUTING.md file](contributing-file), 
there are several core components of Python package documentation, 
including:

* **User-facing documentation website:** This refers to easy-to-read documentation that helps a user work with your package. This documentation should help users both install and use the functionality of your package.  
    * Your user facing documentation should also include [short tutorials that show a user how to quickly get started using your package](python-package-documentation-tools.html#create-python-package-tutorials-that-both-help-users-and-test-your-package-s-code). If you use a tool such as sphinx-gallery or nbsphinx that runs the code in your tutorials, then these tutorials can also become an important part of your package's test suite.   
* **API documentation:** The API refers to the functions and classes in a 
package that makes up the user interface. API documentation is generated from [docstrings](https://pandas.pydata.org/docs/development/contributing_docstring.html) found in your 
code. Ideally you have docstrings for all user-facing functions, methods and classes in 
your Python package. We will discuss API's and docstrings in greater detail below. 


User-facing documentation should be published on a easy-to-navigate website. All language should be written with non-developer users in mind. This means 
using language that is less technical.

A few tips to make sure your documentation is accessible include: 

* Whenever possible, define technical terms and jargon.
* Consider writing instructions for a high-school level reader. 
* Include step-by-step code examples, tutorials or vignettes that support getting started using your package.

## Documentation landing page best practices 

To make it easy for users to find what they need quickly, all packages should 
have 4 elements on the home page of their documentation:

* **Getting started:** This section should provide the user with a quick start for installing your package. A small example of how to use the package is good to have here as well. 
* **About:** Describe your project, state project goals and what it does. 
* **Community:** Instructions for how to help and/or get involved. This section might include a development guide. 
* **Documentation:** The actual project documentation. You may have two sections of documentation - the user facing documentation and your API reference. 


```{figure} ../images/geopandas-documentation-landing-page.png
---
name: directive-fig
width: 80%
alt: Image showing the landing page for GeoPandas documentation which has 4 sections including Getting started, Documentation, About GeoPandas, Community. 
---
The documentation landing page of GeoPandas, a spatial Python library, has the 4 element specified above. Notice that the landing page is simple and directs users to each element using a Sphinx card.
```

NOTE: in many cases you can include your **README** file and your **CONTRIBUTING** files 
in your documentation given those files may have some of the components listed above.

`````{tip}
You can include files in sphinx using the include directive.
Below is an example of doing this using `myst` syntax. 
````
```{include} ../README.md
```
````
`````

## Create tutorials in your documentation 
Your package should have tutorials that make it easy for a user 
to get started using your package. Ideally, those tutorials 
also can be run from start to finish providing a second set of 
checks (on top of your test suite) to your package's code base. 

In the [documentation tools page](python-package-documentation-tools) we talk about two sphinx extensions (sphinx gallery and nbsphinx)
that  allow you to create reproducible tutorials that are run 
when your sphinx documentation builds. 

## Documenting the code in your package's API using docstrings

### What is an API?
API stands for **A**pplied **P**rogramming **I**nterface. When 
discussed in the context of a (Python) package, the API refers to 
the interface and tools that you, as a package user, use in a package. 

A simple example of a package API element:
For instance, a package might have a function called `add_numbers()` 
that adds up a bunch of numbers. To add up numbers, you as the user 
simply call `add_numbers(1,2,3)` and the package function calculates the value and returns `6`. In using the `add_numbers` function, a user is 
using the package's API. 

 Package API's can consist of functions and/or classes (or object) that provide an easier-to-user interface (the API) for a user. 

### What is a docstring and how does it relate to documentation? 
In Python a docstring refers to text in a function, method or class 
that describes what the function does and its inputs, outputs and what it 
returns.

The docstring is thus important for:

* When you, as a user, call `help()` e.g. `help(add_numbers)` in Python, it returns the elements in your docstring to help guide a user towards using the function more effectively. 
* When you build your package's documentation, the docstrings can be also used to automagically create full API documentation that provides a clean view of all functions methods and classes in a package.  

```{tip}
Example API Documentation (Documentation for all functions and classes in a package)
* [View example high level API documentation for the Verde package. This page lists every function and class in the package along with a brief explanation of what it does](https://www.fatiando.org/verde/latest/api/index.html)
* [You can further dig down to see what a specific function does within the package by clicking on an API element](https://www.fatiando.org/verde/latest/api/generated/verde.grid_coordinates.html#verde.grid_coordinates)
```


## Python package API documentation 

API documentation refers to explanation about the function, inputs and outputs 
of every (*within reason*) function, class, method in your package. API documentation
in python requires that you use a docstring for each class, function or method that:

* Explains what the function, method or class does 
* Explains what every input and output variable's (type) is (ie. `string`, `int`, `np.array`)
* Explains the expected output `return` of the object, method or function.

### Python docstring best practices 

There are several Python docstring formats that you can chose to use when documenting 
your package including:

* [NumPy-style](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard)
* [google style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) 
* [reST style](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html) 

<!-- https://peps.python.org/pep-0287/ - 2002 pep 287-->
We suggest using [NumPy-style docstrings](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard) for your 
Python documentation because:

* NumPy style docstrings are human readable (unlike reST which is harder to quickly scan and takes up more lines of code in your modules)
* NumPy format docstrings are core to the scientific Python ecosystem and defined in the [NumPy style guide](https://numpydoc.readthedocs.io/en/latest/format.html). Thus you will find them widely used there. 

```{tip}
If you are using `NumPy format` docstrings, be sure to include the [sphinx napoleon 
extension](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html) in your documentation `conf.py` file. This extension allows sphinx 
to properly read and format NumPy format docstrings. 
```

### Docstring examples Better and Best 

Below is a good example of a well documented function. Notice that this 
function's docstring describes every function inputs and the function's output 
(or return value). The description of the function is short and to the point 
(2 to 3 sentences). And the return of the function is specified. 

```Python
def extent_to_json(ext_obj):
    """Convert bounds to a shapely geojson like spatial object.
    This format is what shapely uses. The output object can be used
    to crop a raster image.

    Parameters
    ----------
    ext_obj: list or geopandas.GeoDataFrame
        If provided with a geopandas.GeoDataFrame, the extent
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

### Best - a docstring with example use of the function

This example contains an example of using the function that is also tested in 
sphinx using [doctest](https://docs.python.org/3/library/doctest.html).

```Python
def extent_to_json(ext_obj):
    """Convert bounds to a shapely geojson like spatial object.
    This format is what shapely uses. The output object can be used
    to crop a raster image.
    Parameters
    ----------
    ext_obj: list or geopandas geodataframe
        If provided with a geopandas geodataframe, the extent
        will be generated from that. Otherwise, extent values
        should be in the order: minx, miny, maxx, maxy.
    Return
    ------
    extent_json: A GeoJSON style dictionary of corner coordinates
    for the extent
        A GeoJSON style dictionary of corner coordinates representing
        the spatial extent of the provided spatial object.
    Example
    -------
    >>> import geopandas as gpd
    >>> import earthpy.spatial as es
    >>> from earthpy.io import path_to_example
    >>> rmnp = gpd.read_file(path_to_example('rmnp.shp'))
    >>> es.extent_to_json(rmnp)
    {'type': 'Polygon', 'coordinates': (((-105.4935937, 40.1580827), ...),)}
    """

```

```{figure} ../images/sphinx-rendering-extent-to-json-earthpy.png
---
name: directive-fig
width: 80%
---
Using the above NumPy format  docstring in sphinx, the autodoc extension will 
create the about documentation section for the `extent_to_json` function. The 
output of the `es.extent_to_json(rmnp)` command can even be tested using 
doctest adding another quality check to your package. 
```

