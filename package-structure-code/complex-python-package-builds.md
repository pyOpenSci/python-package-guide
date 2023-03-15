# Complex Python package builds

This guide is focused on packages that are either pure-python or that
have a few simple extensions in another language such as C or C++.

In the future, we want to provide resources for packaging workflows that require more complex builds. If you have questions about these types of package, please [add a question to our discourse](https://pyopensci.discourse.group/) or open an [issue about this guide specifically in the GitHub repo for this guide](https://github.com/pyOpenSci/python-package-guide/issues). There are many nuances to building and distributing Python packages that have compiled extensions requiring non-Python dependencies at build time. For an overview and thorough discussion of these nuances, please see [this site.](https://pypackaging-native.github.io/)

## Pure Python Packages vs. packages with extensions in other languages

You can classify Python package complexity into three general categories. These
categories can in turn help you select the correct package front-end and
back end tools.

1. **Pure-python packages:** these are packages that only rely on Python to function. Building a pure Python package is simpler. As such, you can chose a tool below that
has the features that you want and be done with your decision!
2. **Python packages with non-Python extensions:** These packages have additional components called extensions written in other languages (such as C or C++). If you have a package with non-python extensions, then you need to select a build back-end tool that allows you to add additional build steps needed to compile your extension code. Further, if you wish to use a front-end tool to support your workflow, you will need to select a tool that
supports additional build setps. In this case, you could use setuptools. However, we suggest that you chose build tool that supports custom build steps such as Hatch with Hatchling or PDM. PDM is an excellent choice as it allows you to also select your build back end of choice. We will discuss this at a high level on the complex builds page.
3.**Python packages that have extensions written in different languages (e.g. fortran and C++) or that have non Python dependencies that are difficult to install (e.g. GDAL)** These packages often have complex build steps (more complex than a package with just a few C extensions for instance). As such, these packages require tools such as [scikit-build](https://scikit-build.readthedocs.io/en/latest/)
or [meson-python](https://mesonbuild.com/Python-module.html) to build. NOTE: you can use meson-python with PDM.


<!--
On this page, we will focus on using front-end tools to package pure python
packages. We will note if a package does have the flexibility to support other
back-ends and in turn more complex builds (*mentioned in #2 and #3 above*). -->
<!--
## COmbine the two sets of statement below...
ELI:
PDM supports C/Cython extensions too: https://pdm.fming.dev/latest/pyproject/build/#build-platform-specific-wheels

It does this by allowing you to write a python script that gets injected into a setuptools build process :) so that's not necessarily the greatest choice. It's a bit like using setuptools directly. ;)

Ralf:
Hatch only supports pure Python packages as of now. setuptools is still a very reasonable choice, and okay if all you have is a few C/Cython extensions. But I'd say you should probably recommend meson-python and scikit-build-core as the two best tools for building packages containing compiled extensions.


* link to ralf's blog and book on complex builds
* keep this page high level so we don't get weight downsides
* can use the examplePy repo stefan and I are working on that will test various build combinations

*****

ELI: It would be more accurate to say that PDM supports using PDM and setuptools at the same time, so you run setuptools to produce the C extensions and then PDM receives the compiled extension files (.so, .pyd) and packages it up alongside the pure python files.

Hatch - https://hatch.pypa.io/latest/config/build/#build-hooks uild hooks

Ralf -
Hatch has the worst take on building compiled code by some distance. Unless its author starts developing an understanding of build systems / needs, and implements support for PEP 517 build backend hooks in pyproject.toml, it's pretty much a dead end.
****


 HEnry: Poetry will move to PEP 621 configuration in version 2.

* pdm, hatch and poetry all have "ways" of supporting c extensions via pdm-backend, hatchling and poetry's build back end.
* poetry's support for C extensions is not fully developed and documented (yet). * Poetry doesn't offer a way to facilitate "communication" between poetry front end and another back end like meson to build via a build hook. so while some have used it with other back end builds it's not ideal for this application
* pdm and poetry both rely on setuptools for C extensions. pdm's support claims to be fully developed and documented. poetry claims nothing, and doesn't document it.
* hatch both offers a plugin type approach to support custom build steps
PDM (right now) is the only tool that supports other back ends (hatch is working on this - 2 minor releases away)
At some point a build becomes so complex that you need to use a tool like scikit or meson to support that complexity.



**Setuptools** is the oldest tool in the above list. While it doesn't have a
friendly user front end, because "OG" tool that has been used for Python packaging for over a decade, we discuss it here.

**Hatch** and PDM are newer, more modern tool that support customization of any
part of your packaging steps. These tools also support some C and C++
extensions.


OFEK - Why use hatchlin vs pdm back end -
File inclusion is more configurable and easier by default
There is already a rich ecosystem of plugins and a well-thought-out interface
Consistency since the official Python packaging tutorial uses Hatchling by default


Henry -
The scikit-hep cookie provides 11 backends including flit-core and hatchling, and I've moved packaging to flit-core, and lots of other things to hatchling, and I can say that hatching's defaults are much nicer than flit-core's. Hatching uses .gitignore to decide what to put in the SDist. Flit-core basically tries to keep its hands off of adding defaults, so you have to configure everything manually. To make it even more confusing, if you use flit instead of a standard tool like build, it will switch to using VCS and those ignored files won't be added - meaning it is really easy to have a project that doesn't support build, including various GitHub Actions. Hatchling wins this by a ton.

<!-- TODO: add - compatible with other build back ends eg pdm can work with hatchling

Eli:
poetry: supports it, but is undocumented and uses setuptools under the hood, they plan to change how this works and then document it
pdm-backend: supports it, and documents it -- and also uses setuptools under the hood
hatchling: permits you to define hooks for you to write your own custom build steps, including to build C++ extensions

-->



<!-- from eli about pdm
It would be more accurate to say that PDM supports using PDM and setuptools at the same time, so you run setuptools to produce the C extensions and then PDM receives the compiled extension files (.so, .pyd) and packages it up alongside the pure Python files.

Comment about hatch.
https://github.com/pyOpenSci/python-package-guide/pull/23#discussion_r1081108118

From ralf: There are no silver bullets here yet, no workflow tool is complete. Both Hatch and PDM are single-author tools, which is another concern. @eli-schwartz's assessment is unfortunately correct here I believe (at a high level at least, not sure about details). Hatch has the worst take on building compiled code by some distance. Unless its author starts developing an understanding of build systems / needs, and implements support for PEP 517 build backend hooks in pyproject.toml, it's pretty much a dead end.

-->

<!--TODO Add examples of builds using each of the tools below?

pdm, hatch and poetry all have "ways" of supporting c extensions via pdm-build, hatchling and poetry's build back end.
poetry's support for C extensions is not fully developed and documented (yet). Poetry doesn't offer a way to facilitate "communication" between poetry front end and another back end like meson to build via a build hook.
PDM and hatch both offer a plugin type approach to support custom build steps
PDM (right now) is the only tool that supports other back ends (hatch is working on this - 2 minor releases away)
At some point a build becomes so complex that you need to use a tool like scikit or meson to support that complexity.

CORRECTIONS:
pdm doesn't use plugins. Hatch does.
pdm and poetry both rely on setuptools for C extensions. pdm's support claims to be fully developed and documented. poetry claims nothing, and doesn't document it.


??
Poetry supports extensions written in other languages but this functionality is
currently undocumented.

Tools such as Setuptools, PDM, Hatch and Poetry all have some level of support
for C and C++ extensions.
Some Python packaging tools,
such as **Flit** and the **flit-core** build back-end only support pure-Python
package builds.
Some front-end packaging tools, such as PDM, allow you to use other
build back-ends such as **meson** and **scikit-build**.


me:
pdm, hatch and poetry all have "ways" of supporting c extensions via pdm-build, hatchling and poetry's build back end.
poetry's support for C extensions is not fully developed and documented (yet). Poetry doesn't offer a way to facilitate "communication" between poetry front end and another back end like meson to build via a build hook.
PDM and hatch both offer a plugin type approach to support custom build steps
PDM (right now) is the only tool that supports other back ends (hatch is working on this - 2 minor releases away)
At some point a build becomes so complex that you need to use a tool like scikit or meson to support that complexity.
@eli-schwartz eli-schwartz 3 weeks ago
PDM and hatch both offer a plugin type approach to support custom build steps

ELI:
pdm doesn't use plugins. Hatch does.
pdm and poetry both rely on setuptools for C extensions. pdm's support claims to be fully developed and documented. poetry claims nothing, and doesn't document it.


https://pdm.fming.dev/latest/pyproject/build/#build-platform-specific-wheels
-->


<!-- https://github.com/pyOpenSci/python-package-guide/pull/23#discussion_r1071541329
ELI: A complex build could mean running a python script that processes some data file and produces a pure python module file.

Probably not common in the scientific community specifically, but I've seen quite a few setup.py files that contain custom build stages which e.g. build gettext locale catalogs.

The main point is that it is more "complex" than simply copying files or directories as-is into the built wheel.
-->
