# How to migrate from setup.py to pyproject.toml

Authors: Leah Wasser, Filipe Fernandes

If you have an existing Python package that has a `setup.py` or a `setup.cfg` file storing your project's metadata, then this tutorial is for you!

Here you will learn how to migrate your project's metadata and build information over to a `pyproject.toml` file.

## Setup.py files serve a purpose

Sometimes you may need a setup.py file if you have a complex build
that is compiling extensions in other languages or wrapping other
languages. Even if you require a setup.py file, to build your package,
you should still have a pyproject.toml file to store project metadata.

Below we discuss migrating your information from a setup.py or setup.cfg file to a pyproject.toml file.

## If your metadata are in a setup.cfg

If your metadata are already in a setup.cfg file, then moving your metadata to a pyproject.toml file, should be a straightforward process.

- Here you can see an example of [example setup.cfg file](https://github.com/stravalib/stravalib/blob/65f903248b6562febf4109d2699b38a1744e50fb/setup.cfg) from the stravalib project.
- And here you can see the what the [migration looked like to pyproject.toml](https://github.com/lwasser/stravalib/blob/ac9c683751969457730743ea435dcf827e015b7d/pyproject.toml)

The biggest difference that you will see between the setup.cfg and pyproject.toml is that instead of using `[metadata]` as a defined section to store your project metadata, you use `[project]` in the pyproject.toml. There are some other small differences in how the pyproject.toml file is structured; however if you include all of the required elements discussed below, you will be in good shape.

Below is an example from a setup.cfg file from the stravalib package.

```toml
[metadata]
name = stravalib
fullname = stravalib
description = A Python package that makes it easy to access and download data from the Strava V3 REST API.
```

We migrated the package over to pyproject.toml file, and the same metadata looked like this:

```toml
[project]
name = "stravalib"
description = "A Python package that makes it easy to access and download data from the Strava V3 REST API."
```

## If metadata are in a setup.py

The process for moving your metadata from a setup.py file is similar to the setup.cfg. You can completely remove the setup() method if it only contains metadata information and all of the package metadata then gets migrated to your pyproject.toml file.

```python
from setuptools import setup # Package metadata

name = "mypackage"
version = "1.0.0"
author = "Your Name"
author_email = "your@email.com"
description = "A brief description of your package"
```

Then you call a **setup()** method. This method will
ensure that the metadata is placed into the proper
METADATA file when your package's wheel <link to build page about wheel> is created.

```python
setup(name=name,
      version=version,
      author=author,
      author_email=author_email)
```

In this case, with a setup.py file, you can remove all of the content within the `setup()` method that declares the project’s metadata. And then you can migrate the metadata items one by one over to your pyproject.toml file.

## Pyproject.toml vs Setup.py, setup.cfg

There are numerous advantages to using pyproject.toml over the setup.cfg of the setup.py files.

pyproject.toml:

- Allows you to declare what build system you are using. This makes it easier for a new contributor to quickly understand how your package is built.
- Allows you to specify metadata for all pypi classifiers and also core package metadata in one place using consistent formatting
- Pyproject.toml file allows you to also add configuration for other tools such as black and flake8 making it a goto spot for anyone to understand the setup of your packages structure

## Migrating from setup.py to pyproject.toml

Here we will use the GEMGIS package as an example of a pure python project that
migrated from a setup.py file to a **pyproject.toml** file.

Below is the setup.py file. Note that this specific setup.py file is comprised only
of package metadata. Thus, this package is a perfect candidate for migrating over to
a pyproject.toml file and removing the setup.py file altogether from the project build.

Note that in the package structure below,

- setuptools is being called.
  this is your build back end that will create your packages distributions (sdist and wheel)
- Version is being updated / maintained manually. this isn't ideal as it leaves more room for human error.

Also note the readability of the file. It's a bit less human readable than we might like.

```python
from setuptools import setup, find_packages
from os import path

version = '1.0.12'

# Loading Readme for Description on PyPi
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='gemgis',
    version=version,
    packages=find_packages(exclude=('test', 'data', 'notebooks')),
    include_package_data=True,
    install_requires=[],
    url='https://github.com/cgre-aachen/gemgis',
    license='LGPL v3',
    author='Alexander Jüstel, Arthur Endlein Correia, Florian Wellmann, Marius Pischke',
    author_email='alexander.juestel@rwth-aachen.de',
    description="GemGIS is a Python-based, open-source spatial data processing library.
                It is capable of preprocessing spatial data such as vector data
                raster data, data obtained from online services and many more data formats.",
    keywords=['geology', 'structural geology', 'GIS', 'spatial data'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
```

Below all of the information above has been moved to a pyproject.toml file.

At the top you specify the build system which in this case is setuptools.
This specific package is also referencing using setuptools_scm which is a versioning
tool that works with setuptools to deermine your package's current version at
build time using git tags.

```toml
[build-system]
requires = ["setuptools>=68.1.2",
            "setuptools_scm[toml]>=6.2"]
build-backend = "setuptools.build_meta"
```

Below the metadata from the setup.py file, has been migrated over to the [project] table
in the pyproject.toml file.

```toml
[build-system]
requires = ["setuptools>=68.1.2"]
build-backend = "setuptools.build_meta"

[project]
name = "GemGIS"
authors = [
    {name = "Alexander Jüstel", email = "alexander.juestel@rwth-aachen.de"},
]
# add any other maintainers here
maintainers = [
    {name = "Alexander Jüstel", email = "alexander.juestel@rwth-aachen.de"},
]
description = "Spatial data processing for geomodeling"
keywords = ['geology', 'structural geology', 'GIS', 'spatial data']
readme = "README.md"
license = {file = LICENSE}
version = 1.0.12
requires-python = ">=3.9"
classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Science/Research',
    'Topic :: Scientific/Engineering :: Information Analysis',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Operating System :: OS Independent',
]
dependencies = [
    "geopandas",
    "rasterio",
    "pyvista",
]

[project.urls]
Documentation = 'https://gemgis.readthedocs.io/'
Home = 'https://gemgis.readthedocs.io/'
"Bug Tracker" = 'https://github.com/cgre-aachen/gemgis/issues'
Repository = 'https://github.com/cgre-aachen/gemgis'
Source Code = 'https://github.com/cgre-aachen/gemgis'
```

**breakout**
Note that above under project.urls some of the key values are in quotes. This is because those keys contain two words with a space in between. if you have more
than a single word on the left of the equal sign in a toml file,
then you will need quotes.

## Using dynamic versioning

If you want to use a tool such as setuptools_Scm or pdm's dynamic versioning you can make a few small modifications to the above file.

Rather than setting up the version like this in the project table:

`version = 1.0.12`

You set the version to be dynamic like this:

`dynamic=["version"]`

and then you'd add `setuptools_Scm[toml]` to your build setup:

```toml
[build-system]
requires = ["setuptools>=68.1.2", "setuptools_scm[toml]>=6.2"]
build-backend = "setuptools.build_meta"
```

A few reminders

1. make sure that the classifiers that you select are from the [PyPI list of accepted classifiers](https://pypi.org/classifiers/)
2. Most of the project table metadata is optional. You really only NEED the version and name of your project. However we strongly recommend that you use other project metadata as it will help users find your project on pypi and better understand what it does.

breakout:
If you want to see an example of a pyproject.toml file that uses setuptools and setuptools_scm plus the recommended package src/ layout, [click here.](https://github.com/stravalib/stravalib/blob/main/pyproject.toml)
