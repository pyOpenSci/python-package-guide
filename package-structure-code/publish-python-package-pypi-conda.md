# Publishing Your Package In A Community Repository: PyPI or Anaconda.org

<!--todo: add as resource https://docs.conda.io/projects/conda/en/latest/glossary.html -->

pyOpenSci requires that your package has an distribution that can be installed
from a public community repository such as PyPI or a conda channel such as
`bioconda` or `conda-forge` on Anaconda.org.

Below you will learn more about the various publishing options for your Python
package.

:::{admonition} Take Aways

* Installing packages in the same environment using both pip and conda can
lead to package conflicts.
* To minimize conflicts for users who may be using conda (or pip) to manage local environments, consider publishing your package to both PyPI and the conda-forge channel on Anaconda.org.

Below you will learn more specifics about the differences between PyPI and conda publishing of your Python package.
:::


:::{figure-md} upload-conda-forge

<img src="../images/publish-python-package-pypi-conda.png" alt="Image showing the progression of creating a Python package, building it and then publishing to PyPI and conda-forge. You take your code and turn it into distribution files (sdist and wheel) that PyPI accepts. Then there is an arrow towards the PyPI repository where ou publish both distributions. From PyPI if you create a conda-forge recipe you can then publish to conda-forge. " width="700px">

Once you have published both package distributions (the source distribution and the wheel) to PyPI, you can then publish to conda-forge. The conda-forge requires a source distribution on PyPI in order to build your package on conda-forge. You do not need to rebuild your package to publish to conda-forge.
:::

## What is PyPI

[PyPI](https://pypi.org/) is an online Python package repository that
you can use to both find and install and publish your Python package. There is
also a test PyPI repository where you can test publishing your package
prior to the final publication on PyPI.

Many if not most Python packages can be found on PyPI and are thus installable using `pip`.

The biggest different between using pip and conda to install
a package is that conda can install any package regardless
of the language(s) that it is written in. Whereas `pip` can
only install Python packages.

:::{button-link} ../tutorials/publish-pypi.html
:color: primary
:class: sd-rounded-pill float-left

Click here for a tutorial on publishing your package to PyPI.
:::


:::{tip}
On the package build page, we discussed the [two package distribution
types that you will create when making a Python package](python-package-distribution-files-sdist-wheel): SDist (packaged as a .tar.gz or .zip) and
Wheel (.whl) which is really a zip file. Both of those file "bundles" will
be published on PyPI when you use [a standard build tool](python-package-build-tools) to build
your package.
:::

(about-conda)=
## What is conda and Anaconda.org?

conda is an open source package and environment management tool.
conda can be used to install tools from the [Anaconda
repository](https://repo.anaconda.com/).

Anaconda.org contains public and private repositories for
packages. These repositories are known as channels (discussed below).

:::{admonition} A brief history of conda's evolution
:class: note

The conda ecosystem evolved years ago to provide support for, and
simplify the process of, managing software dependencies in scientific
Python projects.

Many of the core scientific Python projects depend upon or wrap around tools and extensions that are written in other languages, such as C++. In the early stages of the scientific ecosystem's development, these non-Python extensions and tools were not well supported on PyPI, making publication difficult. In recent years there is more support for complex builds that allow developers to bundle non-Python code into a Python distribution using the [wheel distribution format](python-wheel).

Conda provides a mechanism to manage these dependencies and ensure that the required packages are installed correctly.
:::

:::{tip}
While conda was originally created to support Python packages, it
is now used across all languages. This cross-language support
makes it easier for some packages to include and have access to
tools written in other languages, such as C/C++ (gdal), Julia, or R.
Creating an environment that mixes all of these packages is usually easier and more
consistent with full-fledged package managers like conda.
:::

### conda channels

conda built packages are housed within repositories that are called
channels. The conda package manager can install packages from different channels.

There are several core public channels that most people use to install
packages using conda, including:

- **defaults:** this is a channel managed by Anaconda. It is the version of the Python packages that you will install if you install the Anaconda Distribution. Anaconda (the company) decides what packages live on the `defaults` channel.
- [**conda-forge:**](https://conda-forge.org/) this is a community-driven channel that focuses on scientific packages. This channel is ideal for tools that support geospatial data. Anyone can publish a package to this channel.
- [**bioconda**](https://bioconda.github.io/): this channel focuses on biomedical tools.

**conda-forge** emerged as many of the scientific packages did not
exist in the `defaults` Anaconda channel.

:::{figure-md} pypi-conda-channels

<img src="../images/python-pypi-conda-channels.png" alt="Graphic with the title Python package repositories. Below it says Anything hosted on PyPI can be installed using pip install. Packaging hosted on a conda channel can be installed using conda install. Below that there are two rows. The top row says conda channels. Next to it are three boxes one with conda-forge, community maintained; bioconda and then default - managed by the anaconda team. Below that there is a row that says PyPI servers. PyPI - anyone can publish to PyPI. And test PyPI. A testbed server for you to practice. " width="700px">

Conda channels represent various repositories that you can install packages from. Because conda-forge is community maintained, anyone can submit a recipe there. PyPI is also a community maintained repository. Anyone can submit a package to PyPI and test PyPI. Unlike conda-forge there are no manual checks of packages submitted to PyPI.
:::


## conda channels, PyPI, conda, pip - Where to publish your package

You might be wondering why there are different package repositories
that can be used to install Python packages.

And more importantly you are likely wondering how to pick the right
repository to publish your Python package.

The answer to both questions relates dependency conflicts.

:::{figure-md} xkcd-dep-conflict

<img src="../images/python-dependency-conflicts-xkcd.png" alt="Image showing an XKCD comic that shows a web of Python environments and tools and installations. At the bottom is says -  My python environment has become so degraded that my laptop has been declared a superfund site." width="700px">

Installing Python and Python packages from different repositories can lead
to environment conflicts where a version of on package doesn't work with
a version of another package. To keep your environments clean and working, it's
best to install packages from the same repository. So use pip to install
everything. Or use conda. If you can, try to avoid installing package from
both pip and conda into the same environment.
:::

### Managing Python package dependency conflicts

Python environments can encounter conflicts because Python tools can be installed from different repositories.
Broadly speaking, Python environments have a smaller chance of
dependency conflicts when the tools are installed from the same
package repository. Thus environments that contain packages
installed from both pip and conda are more likely to yield
dependency conflicts.

Similarly installing packages from the default anaconda channel mixed with the conda-forge channel can also lead to dependency conflicts.

Many install packages directly from conda `defaults` channel. However, because
this channel is managed by Anaconda, the packages available on it are
limited to those that Anaconda decides should be core to a stable installation. The conda-forge channel was created to complement the `defaults` channel. It allows anyone to submit a package to be published in the channel . Thus, `conda-forge` channel ensures that a broad suite of user-developed community packages can be installed from conda.

### Take-aways: If you can, publish on both PyPI and conda-forge to accommodate more users of your package

The take-away here for maintainers is that if you anticipate users wanting
to use conda to manage their local environments (which many do), you should
consider publishing to both PyPI and the conda-forge channel (_more
on that below_).

:::{admonition} Additional resources
* [learn more about why conda-forge was created, here](https://conda-forge.org/docs/user/introduction.html)

* [To learn more about conda terminology, check out their glossary.](https://docs.conda.io/projects/conda/en/latest/glossary.html )
:::

<!-- One of our packages on conda-forge https://anaconda.org/conda-forge/pandera -->

## How to submit to conda-forge

While pyOpenSci doesn't require you to add your package to conda-forge,
we encourage you to consider doing so!

Once your package is on PyPI, the process to add your package to conda-forge
is straight forward to do. [You can follow the detailed steps provided
by the conda-forge maintainer team.](https://conda-forge.org/docs/maintainer/adding_pkgs.html).


:::{button-link} ../tutorials/publish-conda-forge.html
:color: primary
:class: sd-rounded-pill float-left

Click here for a tutorial on adding your package to conda-forge.
:::

If you want a step by step tutorial, click here.


Once your package is added, you will have a feedstock repository on GitHub with your packages name

:::{tip}
[Here is an example conda-forge feedstock for the pyOpenSci approved package - movingpandas](https://github.com/conda-forge/movingpandas-feedstock)
:::

### Maintaining your conda-forge package repository

Once your package is on the conda-forge channel, maintaining it is simple.
Every time that you push a new version of your package to PyPI, it will
kick off a continuous integration build that updates your package in the
conda-forge repository. Once that build is complete, you will get a
notification to review the update.

You can merge the pull request for that update once you are happy with it.
A ready-to-merge PR usually means ensuring that your project's dependencies
(known as runtime requirements) listed in the updated YAML file found in the
pull request match the PyPI metadata of the new release.
