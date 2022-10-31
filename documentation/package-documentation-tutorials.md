# Python Package Documentation

## Package documentation 

Your package should be well documented. While the readme is a great first step, 
you should also have a documentation website. Many prefer to use Sphinx to create 
they Python package documentation. Sphinx is great because it offers some extensions
that support things like documenting your api (see below), running and testing code 
vignettes in your docstrings and more. 

### Sphinx themes 
Sphinx also offers numerous themes that you can use to customize your documentation.
A few Spinx themes that are commonly used in the Scientific Python community that you might 
consider include:

* [pydata sphinx theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/)
* [sphinx book theme](https://sphinx-book-theme.readthedocs.io/en/stable/) 

This contributing guide is created using a modified version of the Spinx Book 
theme. 

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

```{note}
## Example documentation

[Geopandas](https://geopandas.org/en/stable/): Geopandas has put tremendous energy into their documentation 

```

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
