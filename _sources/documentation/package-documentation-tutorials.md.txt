# Python Package Documentation

```{note}
Examples of documentation that we love:

* [geopandas](https://geopandas.org/en/stable/)
    * [View rst to create landing page](https://raw.githubusercontent.com/geopandas/geopandas/main/doc/source/index.rst)
* [verde](https://www.fatiando.org/verde/latest/)
    * [View verde landing page code - rst file.](https://github.com/fatiando/verde/blob/main/doc/index.rst)
* [Here is our documentation if you want to see a myST example of a landing page.](https://github.com/pyOpenSci/python-package-guide/blob/main/index.md)
```


## Package documentation 

Your package should have user-facing and API focused documentation. We suggest 
that you setup a website to host your documentation.
Many prefer to use Sphinx to create 
their Python package documentation. Sphinx is a useful tool as it offers extensions
that support things like:

* [automatically documenting your API using docstrings](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html)
* running and testing code examples in your docstrings 

## Documentation landing page best practices 

To make it easy for users to find what they need quickly, all packages should 
have 4 elements on the home page of their documentation:

* **Getting started:** This section should provide the user with a quick start for installing your package. A small example of how to use the package is good to have here as well. 
* **About:** Describe your project, state project goals and what it does. 
* **Community:** Instructions for ho to help and/or get involved. This section might include a development guide. 
* **Documentation:** The actual project documentation. You may have two sections of documentation - the user facing documentation and your API reference. 

NOTE: in many cases you can include your **README** file and your **CONTRIBUTING** files 
in your documentation given those files may have some of the components listed above.
Some packages 

### Sphinx themes 
Sphinx also offers numerous themes that you can use to customize your documentation.
A few Sphinx themes that are commonly used in the Scientific Python community that you might 
consider include:

* [pydata sphinx theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/)
* [sphinx book theme](https://sphinx-book-theme.readthedocs.io/en/stable/) 

This contributing guide is created using a modified version of the Spinx Book 
theme. 

### myST vs rst syntax to create your docs 
There are two commonly used syntaxes for creating docs:

1. [myST:](https://myst-parser.readthedocs.io/en/latest/intro.html) myST is a fusion of markdown and rST. It is a nice option if you are more comfortable writing markdown. But more flexible than markdown. 
2. [rST:](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) this is the native syntax that sphinx supports. 

There is no wrong or right when choosing a syntax to write your documentation. 
Choose whichever syntax works best for you and your community! 

```{note}
If you are on the fence about myST vs rst, you might find that *myST* is easier 
for more people to contribute to.  
```


### Publish your docs on another platform directly from GitHub: ReadTheDocs.org 

If you don't want to maintain a documentation website for your Python package, we 
suggest using the [READTHEDOCS platform](https://www.readthedocs.org) which 
allows you to easily host your documentation and track versions of your docs
as you release updates. 

Beyond a well designed [README FILE](create-readme-files) there are several 
core components of Python package documentation including:

1. User facing documentation
2. API documentation

## User-facing documentation for your Python package: 

User-facing documentation is often an easy to navigate website written with 
user friendly, less technical language. User facing documentation should be:

* easy to read (consider writing for a 12th grade audience)
* contain tutorials or vignettes that support getting started using your package 


## Python package API documentation 

API documentation refers to explanation about the function, inputs and outputs 
of every (*within reason*) function, class, method in your package. API documentation
in python requires that you use a docstring for each class, function or method that:

* Explains what the function, method or class does 
* Explains what every input and output variable's (type) is (ie. `string`, `int`, `np.array`)
* Explains the expected output `return` of the object, method or function.


### Docstring examples Better and Best 

Below is a good example of a well documented function. Notice that this function's 
docstring includes all parameter inputs and outputs. The description of the function 
is short and to the point (2 to 3 sentences). And the return of the function is 
specified. 

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

