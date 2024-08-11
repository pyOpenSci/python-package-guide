# Create tutorials in your Python package documentation

<!-- TODO: modify the nbsphinx example to use nbgallery
as a front end vs Sphinx gallery - will look better that way
-->
Your package should have tutorials that make it easy for a user
to get started using your package. Ideally, those tutorials
also can be run from start to finish providing a second set of
checks (on top of your test suite) to your package's code base.

On this page, we review two Sphinx extensions (`sphinx-gallery` and `nbsphinx`)
that  allow you to create reproducible tutorials that are run
when your Sphinx documentation builds.

## Create Python package tutorials that run when you build your docs

Adding well constructed tutorials to your package will make it easier for someone
new to begin using your package.

There are two Sphinx tools that make it easy to add tutorials to your package:

* [Sphinx Gallery](https://sphinx-gallery.github.io/stable/index.html) and
* [NbSphinx](https://nbsphinx.readthedocs.io/en/latest/)

Both of these tools act as Sphinx extensions and:

* Support creating a gallery type page in your Sphinx documentation where users can explore tutorials via thumbnails.
* Run the code in your tutorials adding another level of "testing" for your package as used.
* Render your tutorials with Python code and plot outputs

### [sphinx gallery:](https://sphinx-gallery.github.io/stable/index.html)

If you prefer to write your tutorials using Python **.py** scripts, you
may enjoy using Sphinx gallery. Sphinx gallery uses **.py** files with
text and code sections that mimic the Jupyter Notebook format. When you build
your documentation, the gallery extension:

1. Runs the code in each tutorial. Running your tutorial like this acts as a check to ensure your package's functions, classes, methods, and attributes (ie the API) are working as they should.
1. Creates a downloadable Jupyter Notebook **.ipynb** file and a  **.py** script for your tutorial that a user can quickly download and run.
1. Creates a rendered  **.html** page with the code elements and code outputs in a user-friendly tutorial gallery.
1. Creates a gallery landing page with visual thumbnails for each tutorial that you create.


```{figure} /images/sphinx-gallery-overview.png
---
name: sphinx-gallery
width: 80%
alt: Image showing the gallery output provided by sphinx-gallery where each tutorial is in a grid and the tutorial thumbnails are created from a graphic in the tutorial.
---
`sphinx-gallery` makes it easy to create a user-friendly tutorial gallery.
Each tutorial has a download link where the user can download a **.py** file or a Jupyter Notebook. And it renders the tutorials in a user-friendly grid.
```

Below you can see what a tutorial looks like created with sphinx-gallery.

```{figure} /images/sphinx-gallery-tutorial.png
---
name: spinx-gallery-tutorial
width: 80%
alt: Image showing ta single tutorial from Sphinx gallery. The tutorial shows a simple matplotlib created plot and associated code.
---
`sphinx-gallery` tutorials by default include download links for both the
python script (**.py** file) and a Jupyter notebook (**.ipynb** file) at the bottom.
```

### Sphinx Gallery benefits
* easy-to-download notebook and .py outputs for each tutorials.
* .py files are easy to work with in the GitHub pull request environment.
* Nice gridded gallery output.
* Build execution time data per tutorial. [Example](https://sphinx-gallery.github.io/stable/auto_examples/sg_execution_times.html)

#### Sphinx gallery challenges

The downsides of using Sphinx gallery include:

* the **.py** files can be finicky to configure, particularly if you have matplotlib plot outputs.

For example: To allow for plots to render, you need to name each file with `plot_`
at the beginning.

* Many users these days are used to working in Jupyter Notebooks. .py may be slightly less user friendly to work with

These nuances can make it challenging for potential contributors to add
tutorials to your package. This can also present maintenance challenge.

Add about the gallery setup:

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
nbsphinx operates similarly to Sphinx gallery in that:

* It runs your notebooks and produces outputs in the rendered tutorials

* Pro/con By default it does not support downloading of **.py** and **.ipynb** files. However you can add a [link to the notebook at the top of the page with
some additional conf.py settings (see: epilog settings)](https://nbsphinx.readthedocs.io/en/0.8.10/prolog-and-epilog.html)


```{figure} /images/python-package-documentation-nb_sphinx-gallery-output.png
---
name: directive-fig
width: 80%
alt: Image showing the gallery output provided by nbsphinx using the sphinx-gallery front end interface.
---
`nbsphinx` can be combined with Sphinx gallery to create a gallery of tutorials.
However, rather than rendering the gallery as a grid, it lists all of the gallery
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
        # the nbsphinx build - we will cover this in a separate tutorial series focused onPythonpackaging!
        tutorials/
            index.html
            index.md
            plot_sample-2.html
            plot_sample-2.ipynb
            ...
```
