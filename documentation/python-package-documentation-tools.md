# Python Package Documentation

In addition to your README, CONTRIBUTING and DEVELOPMENT guides, 
you should also have user-facing documentation for your Python 
package. Below we you will learn about the most common tools that 
are used to build Python packaging documentation. 

```{note}
Examples of documentation that we love:

* [geopandas](https://geopandas.org/en/stable/)
    * [View rst to create landing page](https://raw.githubusercontent.com/geopandas/geopandas/main/doc/source/index.rst)
* [verde](https://www.fatiando.org/verde/latest/)
    * [View verde landing page code - rst file.](https://github.com/fatiando/verde/blob/main/doc/index.rst)
* [Here is our documentation if you want to see a myST example of a landing page.](https://github.com/pyOpenSci/python-package-guide/blob/main/index.md)
```


## What tools to use to build your documentation: sphinx

Most python packages use [sphinx](https://www.sphinx-doc.org/) to build their documentation. 

```{tip} 
Sphinx is a static-site generator. A static site generator is a tool that creates 
html for a website based upon a set of templates. Sphinx is written 
using Python tool which 
is why it's commonly used in the Python ecosystem. 

There are however other tools that could be used such as [mkdocs](https://www.mkdocs.org/). We won't 
got into others tools in this guide given sphinx is currently the most 
popular in the scientific Python ecosystem. However, you are welcome to use whatever documentation tool that you prefer for your Python package development! 
```

Sphinx can be extended with various elements including themes and directives (extensions) as follows:

* You can apply documentation themes for quick generation of beautiful documentation.
* You can [automatically create documentation for your package's functions and classes (API) from docstrings in your code using the autodoc extension](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html)
* You can [run and testing code examples in your docstrings using doctest](https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html)
* While sphinx natively supports the rst syntax. You can add custom syntax parsers to support easier to write syntax such as [myst](https://myst-parser.readthedocs.io/) .

While you are free to use whatever sphinx theme you prefer,
the most common modern templates that recommend for the Python scientific 
community are:  

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
need to use either myST or rST.
1. [rST (ReStructured Text):](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html). rST is the native syntax that sphinx supports. rST was the default syntax used for documentation for many years given the limitations associated with markdown. However, in recent years myST has risen to the top as a favorite for documentation given the flexibility that it allows.
1. [myST:](https://myst-parser.readthedocs.io/en/latest/intro.html) myST is a combination of vanilla of `markdown` and `rST` syntax. It is a nice option if you are more comfortable writing markdown. `myst` is preferred by many because it offers both the rich functionality 
of rST combined with a simple-to-write markdown syntax. 

While you can chose to use any of the syntaxes listed above, `myST` is a 
preferred syntax to because:

* It is a simpler syntax and thus easier to learn;
* Most of your core python package text files, such as your README.md file, are already in `.md` format
* `GitHub` and `Jupyter Notebooks` support this default syntax/file format.

There is no wrong or right when choosing a syntax to write your documentation. 
Choose whichever syntax works best for you and your community! 

```{tip}
If you are on the fence about myST vs rst, you might find that *myST* is easier 
for more people to contribute to.  
```

## How to host your Python package documentation

We suggest that you setup a website to host your documentation. There are two 
ways to do quickly create a documentation website:

1. You can host your documentation yourself using [GitHub Pages](https://pages.github.com/) or another online hosting service. 
2. You can host your documentation using [Read the Docs](https://readthedocs.org/).

If you don't want to maintain a documentation website for your Python package, 
we suggest using the Read the Docs website. Read the Docs allows you to:

* Quickly launch a website using the documentation found in your GitHub repository.  
* Track versions of your documentation as you release updates.

## Tutorials 
* sphinx gallery... 

<!-- Bells and whistles additions-->
## Bells and whistles for your documentation 

* sitemap  - for google seo 
* other extension?? 
* google analytics 
