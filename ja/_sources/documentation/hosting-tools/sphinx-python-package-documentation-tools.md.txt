# Using Sphinx to Build Python Package Documentation

<!-- TODO: make this into include files so we can have a summary
important points page -->
<!--
```{important}

## Take Aways: Key Python Package Tools to Use

* Use Sphinx to build your documentation
* Publish your documentation on ReadTheDocs (or GitHub pages if you are more advanced and also prefer to maintain your website locally)
* Use `myST` syntax to write your documentation
* Use Sphinx gallery to write tutorials using .py files that automagically have downloadable .py and jupyter notebook files. Use nbsphinx if you prefer writing tutorials in jupyter notebook format and don't need a grid formatted gallery. *Both of these tools will run your tutorials from beginning to end providing an addition layer of testing to your package!*
* OPTIONAL: Use [doctest](https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html) to run the examples in your code's docstrings as a way to make sure that your code's functions and methods (the API) are running as you expect them to.
``` -->

On this page we discuss using [Sphinx](https://www.sphinx-doc.org/) to build your user-facing
package documentation. While Sphinx is currently the most
commonly-used tool in the scientific Python ecosystem, you
are welcome to explore other tools to build documentation
such as [mkdocs](https://www.mkdocs.org/) which is gaining
popularity in the Python packaging ecosystem.

```{tip}
Examples of documentation websites that we love:

* [GeoPandas](https://geopandas.org/en/stable/)
    * [View rst to create landing page](https://raw.githubusercontent.com/geopandas/geopandas/main/doc/source/index.rst)
* [verde](https://www.fatiando.org/verde/latest/)
    * [View verde landing page code - rst file.](https://github.com/fatiando/verde/blob/main/doc/index.rst)
* [Here is our documentation if you want to see a myST example of a landing page.](https://github.com/pyOpenSci/python-package-guide/blob/main/index.md)
```

## Sphinx - a static site generator

Sphinx is a [static-site generator](https://www.cloudflare.com/learning/performance/static-site-generator/). A static site generator is a tool that creates
html for a website based upon a set of templates. The html files are then served "Statically" which means that there is no generation or modification of the files on the fly.

Sphinx is written using Python.

### Sphinx sites can be customized using extensions and themes

The functionality of Sphinx can be extended using extensions
and themes. A few examples include:

* You can apply documentation themes for quick generation of beautiful documentation.
* You can [automatically create documentation for your package's functions and classes (the package's API) from docstrings in your code using the autodoc extension](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html)
* You can [run and test code examples in your docstrings using the doctest extension](https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html)
* While Sphinx natively supports the `rST` syntax, you can add custom syntax parsers to support easier-to-write syntax using tools such as [the MyST parser](https://myst-parser.readthedocs.io/).

### Commonly used Sphinx themes

You are free to use whatever Sphinx theme that you prefer.
However, the most common Sphinx themes used in the Python
scientific community include:

* [pydata-sphinx-theme](https://pydata-sphinx-theme.readthedocs.io/)
* [sphinx-book-theme](https://sphinx-book-theme.readthedocs.io/)
* [furo](https://pradyunsg.me/furo/quickstart/)


```{tip}
This book is created using Sphinx and the `furo` theme.
```
<!-- Should this also be it's own page?-->
