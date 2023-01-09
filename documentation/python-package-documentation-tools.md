# Python Package Documentation

<!-- TODO: make this into include files so we can have a summary 
important points page -->

```{important}

## Take Aways: Key Python Package Tools to Use

* Use Sphinx to build your documentation
* Publish your documentation on ReadTheDocs (or GitHub pages if you are more advanced and also prefer to maintain your website locally)
* Use `myST` syntax to write your documentation 
* Use sphinx gallery to write tutorials using .py files that automagically have downloadable .py and jupyter notebook files. Use nbsphinx if you prefer writing tutorials in jupyter notebook format and don't need a grid formatted gallery. *Both of these tools will run your tutorials from beginning to end providing an addition layer of testing to your package!*
* OPTIONAL: Use [doctest](https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html) to run the examples in your code's docstrings as a way to make sure that your code's functions and methods (the API) are running as you expect them to. 
```

In addition to your:
* [README.md file](readme-file-best-practices), 
* [CONTRIBUTING.md and development guides and LICENSE file](contributing-license-coc),

you should also have user-facing documentation for your Python 
package. Most often, user-facing documentation is contained on a hosted 
website. 

Below you will learn about the most common tools that 
are used to build scientific Python packaging documentation. You will also 
learn about hosting options for your documentation. 

Here, we focus on tools and infrastructure that you can use. 
[Click here if you want to learn more about documentation best practices](package-documentation-best-practices.md).

```{note}
Examples of documentation websites that we love:

* [GeoPandas](https://geopandas.org/en/stable/)
    * [View rst to create landing page](https://raw.githubusercontent.com/geopandas/geopandas/main/doc/source/index.rst)
* [verde](https://www.fatiando.org/verde/latest/)
    * [View verde landing page code - rst file.](https://github.com/fatiando/verde/blob/main/doc/index.rst)
* [Here is our documentation if you want to see a myST example of a landing page.](https://github.com/pyOpenSci/python-package-guide/blob/main/index.md)
```


## Sphinx, the most common tool used in the scientific Python ecosystem 

Most scientific Python packages use [sphinx](https://www.sphinx-doc.org/) to 
build their documentation. As such, we will focus on sphinx in this guide. 

Sphinx is a [static-site generator](https://www.cloudflare.com/learning/performance/static-site-generator/). A static site generator is a tool that creates 
html for a website based upon a set of templates. Sphinx is written 
using Python tool which 
is why it's commonly used in the Python ecosystem. 

```{tip} 
There are other static site generator tools that could be used to create user-facing documentation including 
 [mkdocs](https://www.mkdocs.org/). We won't 
discuss others tools in this guide given sphinx is currently the most 
popular in the scientific Python ecosystem. 

You are welcome to use whatever documentation tool that you prefer for your Python package development! 
```

### Sphinx sites can be optimized for documentation with extensions and themes 

The functionality of sphinx can be extended using extensions and themes. A few 
examples include:

* You can apply documentation themes for quick generation of beautiful documentation.
* You can [automatically create documentation for your package's functions and classes (that package's API) from docstrings in your code using the autodoc extension](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html)
* You can [run and test code examples in your docstrings using the doctest extension](https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html)
* While sphinx natively supports the `rST` syntax. You can add custom syntax parsers to support easier-to-write syntax using tools such as [myst](https://myst-parser.readthedocs.io/).

You are free to use whatever sphinx theme that you prefer. However, the most 
common sphinx themes that we recommend for the Python scientific 
community include:  

* [pydata-sphinx-theme](https://pydata-sphinx-theme.readthedocs.io/) 
* [sphinx-book-theme](https://sphinx-book-theme.readthedocs.io/)
* [furo](https://pradyunsg.me/furo/quickstart/)


```{tip}
This book is created using sphinx and the `furo` theme.
```

## Documentation syntax: markdown vs. myST vs. rst syntax to create your docs 

There are three commonly used syntaxes for creating Python documentation:
1. [markdown](https://www.markdownguide.org/): Markdown is an easy-to-learn text 
syntax. It is the default syntax use in Jupyter Notebooks. There are tools that you can add to a sphinx website that allow it to render markdown as html. However, using markdown to write documentation has limitations. For instance if you want to add references, 
colored call out blocks and other custom elements to your documentation, you will 
need to use either **myST** or **rST**.
1. [rST (ReStructured Text):](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html). **rST** is the native syntax that sphinx supports. rST was the default syntax used for documentation for many years given the limitations of markdown. However, in recent years myST has risen to the top as a favorite for documentation given the flexibility that it allows.
1. [myST:](https://myst-parser.readthedocs.io/en/latest/intro.html) myST is a combination of vanilla of `markdown` and `rST` syntax. It is a nice option if you are comfortable writing markdown. `myst` is preferred by many because it offers both the rich functionality 
of rST combined with a simple-to-write markdown syntax. 

While you can chose to use any of the syntaxes listed above, we suggest using 
`myST` because:

* It is a simpler syntax and thus easier to learn;
* The above simplicity will make it easier for more people to contribute to your documentation. 
* Most of your core python package text files, such as your README.md file, are already in `.md` format
* `GitHub` and `Jupyter Notebooks` support markdown thus it's more widely used in the scientific ecosystem. 


```{tip}
If you are on the fence about myST vs rst, you might find that **myST** is easier 
for more people to contribute to.  
```

## Create python package tutorials that both help users and test your package's code

Adding well constructed tutorials to your package will make it easier for someone 
new to begin using your package. 

There are two sphinx tools that make it easy to add tutorials to your package:

* [Sphinx Gallery](https://sphinx-gallery.github.io/stable/index.html) and 
* [NbSphinx](https://nbsphinx.readthedocs.io/en/latest/)

Both of these tools act as sphinx extensions and:

* Support creating a gallery type page in your sphinx documentation where users can explore tutorials via thumbnails.
* Run the code in your tutorials adding another level of "testing" for your package as used. 
* Render your tutorials with Python code and plot outputs

### [sphinx gallery:](https://sphinx-gallery.github.io/stable/index.html) 

If you prefer to write your tutorials using Python **.py** scripts, you 
may enjoy using sphinx gallery. Sphinx gallery uses **.py** files with 
text and code sections that mimic the Jupyter Notebook format. When you build 
your documentation, the gallery extension: 

1. Runs the code in each tutorial. Running your tutorial this acts as a check to ensure your package functions and classes (ie the API) are working as they should. 
1. Creates a downloadable Jupyter Notebook **.ipynb** file and a  **.py** script for your tutorial that a user can quickly download and run. 
1. Creates a rendered  **.html** page with the code elements and code outputs in a user-friendly tutorial gallery.  
1. Creates a gallery landing page with visual thumbnails for each tutorial that you create


```{figure} ../images/sphinx-gallery-overview.png
---
name: directive-fig
width: 80%
alt: Image showing the gallery output provided by sphinx-gallery where each tutorial is in a grid and the tutorial thumbnails are created from a graphic in the tutorial.
---
`sphinx-gallery` makes it easy to create a user-friendly tutorial gallery.
Each tutorial has a download link where the user can download a **.py** file or a Jupyter Notebook. And it renders the tutorials in a user-friendly grid. 
```

Below you can see what a tutorial looks like created with sphinx-gallery.

```{figure} ../images/sphinx-gallery-tutorial.png
---
name: directive-fig
width: 80%
alt: Image showing ta single tutorial from sphinx gallery. The tutorial shows a simple matplotlib created plot and associated code. 
---
`sphinx-gallery` tutorials by default include download links for both the 
python script (**.py** file) and a Jupyter notebook (**.ipynb** file) at the bottom. 
```

### Sphinx Gallery benefits 
* easy-to-download notebook and .py outputs for each tutorials
* .py files are easy to work with in the GitHub pull request environment. 
* Nice gridded gallery output
* Build execution time data per tutorial [Example](https://sphinx-gallery.github.io/stable/auto_examples/sg_execution_times.html)

#### Sphinx gallery challenges 

The downsides of using sphinx gallery include: 

* the **.py** files can be finicky to configure, particularly if you have matplotlib plot outputs. 

For example: To make allow for plots to render, you need to name each file with `plot_` 
at the beginning. 

* Many users these days are used to working in Jupyter Notebooks. .py may be slightly less user friendly to work with 

These nuances can make it challenging for potential contributors to add 
tutorials to your package. This can also present maintenance challenge.

Add about the gallery setup - 

```bash 
$ docs % make html 

Sphinx-Gallery successfully executed 2 out of 2 files
```
File directory structure: 

```bash
tutorials/
    index.rst # landing page for your gallery
    plot_tutorial.py # a tutorial 
    plot_tutorial-2.py # a tutorial that produces a plot output
_build/
    build_examples/ # This is where the downloadable tutorial files live 
        plot_sample-1.ipynb
        plot_sample-1.py
        ...
    html/ 
        built_examples/ # You can specify this dir name in gallery settings
            index.html 
            plot_sample-1.html 
            plot_sample.html 
            sg_execution_times.html # in case you want to see build times for each tutorial 

```

### [nbsphinx - tutorials using Jupyter Notebooks](https://nbsphinx.readthedocs.io/en/latest/)

If you prefer to use Jupyter Notebooks to create tutorials you can use nbsphinx.
nbsphinx operates similarly to sphinx gallery in that:

* It runs your notebooks and produces outputs in the rendered tutorials 

* Pro/con By default it does not support downloading of **.py** and **.ipynb** files. However you can add a [link to the notebook at the top of the page with 
some additional conf.py settings (see: epilog settings)](https://nbsphinx.readthedocs.io/en/0.8.10/prolog-and-epilog.html)


```{figure} ../images/python-package-documentation-nb_sphinx-gallery-output.png
---
name: directive-fig
width: 80%
alt: Image showing the gallery output provided by nbsphinx using the sphinx-gallery front end interface. 
---
`nbsphinx` can be combined with sphinx gallery to create a gallery of tutorials. 
However, rather render the gallery as a grid, it lists all of the gallery 
elements in a single column. 
```

```bash
tutorials/
    index.md # Landing page for your gallery
    tutorial.ipynb # A tutorial in a jupyter notebook
    another_tutorial.ipynb
# This shows you what the build directory looks like when you build with sphinx-build
_build/
    html/
        # Notice that nbsphinx runs each notebook and produces an 
        # html file with all of the outputs of your code 
        # you can link to the notebook in your docs by modifying 
        # the nbsphinx build - we will cover this in a separate tutorial series focused on python packaging!
        tutorials/ 
            index.html
            index.md 
            plot_sample-2.html 
            plot_sample-2.ipynb
            ...
``` 

## Using doctest to run docstring examples in your packages methods and functions
<!-- This link isn't working no matter how i create the target. not sure 
why -->
[In the package documentation page we provided some examples of good, better, best docstring formats](package-documentation-best-practices.html#docstring_best_practice). If you wish, you can also add the [doctest](https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html) extension to your Sphinx build
as an addition check for docstrings with example code in them. 
Doctest, runs the example code in your docstring `Examples` checking 
that the expected output is in fact correct. Similar to running
tutorials in your documentation, doctest can be a useful step that 
assures that your packages code (API) runs as you expect it to.

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
    
    """
   return aNum + aNum2

Examples
--------
Below you can see how the `print_me` function will print a number that 
you provide it.

>>> add_me(1+3)
4

```
