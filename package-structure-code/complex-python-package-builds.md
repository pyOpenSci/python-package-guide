# Complex Python package builds

This guide is focused on packages that are either pure-python or that
have a few simple extensions in another language such as C or C++.

In the future, we want to provide resources for packaging workflows that require more complex builds. If you have questions about these types of package, please [add a question to our discourse](https://pyopensci.discourse.group/) or open an [issue about this guide specifically in the GitHub repo for this guide](https://github.com/pyOpenSci/python-package-guide/issues). There are many nuances to building and distributing Python packages that have compiled extensions requiring non-Python dependencies at build time. For an overview and thorough discussion of these nuances, please see [this site.](https://pypackaging-native.github.io/)

## Pure Python Packages vs. packages with extensions in other languages

You can classify Python package complexity into three general categories. These
categories can in turn help you select the correct package front-end and
back-end tools.

1. **Pure-python packages:** these are packages that only rely on Python to function. Building a pure Python package is simpler. As such, you can chose a tool below that has the features that you want and be done with your decision!

2. **Python packages with non-Python extensions:** These packages have additional components called extensions written in other languages (such as C or C++). If you have a package with non-python extensions, then you need to select a build back-end tool that allows you to add additional build steps needed to compile your extension code. Further, if you wish to use a front-end tool to support your workflow, you will need to select a tool that supports additional build setups. In this case, you could use setuptools. However, we suggest that you chose build tool that supports custom build steps such as Hatch with Hatchling or PDM. PDM is an excellent choice as it allows you to also select your build back-end of choice. We will discuss this at a high level on the complex builds page.

3. **Python packages that have extensions written in different languages (e.g. Fortran and C++) or that have non Python dependencies that are difficult to install (e.g. GDAL)** These packages often have complex build steps (more complex than a package with just a few C extensions for instance). As such, these packages require tools such as [scikit-build](https://scikit-build.readthedocs.io/en/latest/)
   or [meson-python](https://mesonbuild.com/Python-module.html) to build. NOTE: you can use meson-python with PDM.
