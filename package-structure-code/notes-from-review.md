<!-- ### Build tools for Python packages with complex build steps
If your package is not pure Python, or it has complex build steps (or build
steps that you need to customize), then you should consider using:

* Setuptools
* Hatch
* PDM

These tools allow you to customize your workflow with build steps needed
to compile code. -->

<!-- From stefan: build, run tests on built version, load the built version into
Python (?how is this different from install??), make editable install, build
wheel, build sdist -->

<!--
The example below is taken from [this thread in GitHub](https://github.com/py-pkgs/py-pkgs/issues/95#issuecomment-1035584750).

```toml
[tool.poetry.dependencies]
python = ">=3.6" # This is muddled in as a dependency, while it's not like the others
numpy = ">=1.13.3"
typing_extensions = { version = ">=3.7", python = "<3.8" }

sphinx = {version = "^4.0", optional = true}
sphinx_book_theme = { version = ">=0.0.40", optional = true }
sphinx_copybutton = { version = ">=0.3.1", optional = true }
pytest = { version = ">=6", optional = true }
importlib_metadata = { version = ">=1.0", optional = true, python = "<3.8" } # TOML error to add an ending comma or new line, even if this gets long
boost-histogram = { version = ">=1.0", optional = true }

[tool.poetry.dev-dependencies]
pytest = ">=5.2"  # All the optional stuff above doesn't help here!
importlib_metadata = {version = ">=1.0", python = "<3.8" }
boost_histogram = ">=1.0"

[tool.poetry.extras]
docs = ["sphinx", "sphinx_book_theme", "sphinx_copybutton"]
test = ["pytest", "importlib_metadata", "boost_histogram" ]
```

vs PDM

```toml
[project]
requires-python = ">=3.6"
dependencies = [
  "numpy>=1.13.3",
  "typing-extensions>=3.7; python_version<'3.8'",
]

# Only needed for extras
[project.optional-dependencies]
docs = [
  "sphinx>=4.0",
  "sphinx-book-theme>=0.0.40",
  "sphinx-copybutton>=0.3.1",
]
test = [
  "pytest>=6",
  "importlib-metadata>=1.0; python_version<'3.8'",
  "boost-histogram>=1.0",
]

# Only needed for "dev" installs
[tool.pdm.dev-dependencies]
dev = [
  "pytest>=6",
  "importlib-metadata>=1.0; python_version<'3.8'",
  "boost-histogram>=1.0",
]
```

From Eli:

poetry: supports it (c extensions), but is undocumented and uses setuptools under the hood, they plan to change how this works and then document it
pdm-back-end: supports it, and documents it -- and also uses setuptools under the hood
hatchling: permits you to define hooks for you to write your own custom build steps, including to build C++ extensions


**PDM** does have some support for `C`/[`Cython`](https://cython.org/) extensions. [Click here to
learn more.](https://pdm.fming.dev/latest/pyproject/build/#build-platform-specific-wheels). This functionality uses setuptools "under the
hood".


-->

<!--
### Build front-ends

Build front-ends have a user-friendly interface that allow you to perform
common Python packaging tasks such as building your package, creating an
environment to run package tests and build documentation, and pushing to PyPI.

For instance, you can use **Flit**, **Hatch**, **Poetry** and **PDM** to both build your
package and to publish your package to PyPI (or test PyPI). However, if you
want a tool that also support environment management and versioning your package,
then you might prefer to use **Hatch**, **Poetry** or **PDM**.

Using a tool like **Flit**, **Hatch**, **Poetry** or **PDM** will simplify your workflow.

Example to build your package with **Flit**:

`flit build`

Example to publish to PyPI:
`flit publish --repository testpypi`

In the Python package build space **setuptools** is
the "OG" -the original tool that everyone used to use.
With a tool like  `setuptools` you have the flexibility
to publish python pure python packages and packages with custom build steps. However, you will also need to use other tools. For example, you will use `twine` to publish to PyPI.

## An ecosystem of Python build tools

Below we introduce several of the most commonly used
Python packaging build  tools. Each tool has various
features that might make you chose to use it
or not use it. There is no right or wrong tool to use
as far as pyOpenSci is concerned. We are just trying to
help you find the tool that works best for
your workflow.
Example build steps using setuptools:
======= -->

<!-- TODO: create build tool selection diagram - https://www.canva.com/design/DAFawXrierc/O7DTnqW5fmMEZ31ao-TK9w/edit -->

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
Hatch has the worst take on building compiled code by some distance. Unless its author starts developing an understanding of build systems / needs, and implements support for PEP 517 build back-end hooks in pyproject.toml, it's pretty much a dead end.
****


 HEnry: Poetry will move to PEP 621 configuration in version 2.

* pdm, hatch and poetry all have "ways" of supporting c extensions via pdm-backend, hatchling and poetry's build back-end.
* poetry's support for C extensions is not fully developed and documented (yet). * Poetry doesn't offer a way to facilitate "communication" between poetry front end and another back-end like meson to build via a build hook. so while some have used it with other back-end builds it's not ideal for this application
* pdm and poetry both rely on setuptools for C extensions. pdm's support claims to be fully developed and documented. poetry claims nothing, and doesn't document it.
* hatch both offers a plugin type approach to support custom build steps
PDM (right now) is the only tool that supports other back-ends (hatch is working on this - 2 minor releases away)
At some point a build becomes so complex that you need to use a tool like scikit or meson to support that complexity.



**Setuptools** is the oldest tool in the above list. While it doesn't have a
friendly user front end, because "OG" tool that has been used for Python packaging for over a decade, we discuss it here.

**Hatch** and PDM are newer, more modern tool that support customization of any
part of your packaging steps. These tools also support some C and C++
extensions.


OFEK - Why use hatchlin vs pdm back-end -
File inclusion is more configurable and easier by default
There is already a rich ecosystem of plugins and a well-thought-out interface
Consistency since the official Python packaging tutorial uses Hatchling by default


Henry -
The scikit-hep cookie provides 11 back-ends including flit-core and hatchling, and I've moved packaging to flit-core, and lots of other things to hatchling, and I can say that hatching's defaults are much nicer than flit-core's. Hatching uses .gitignore to decide what to put in the sdist. Flit-core basically tries to keep its hands off of adding defaults, so you have to configure everything manually. To make it even more confusing, if you use flit instead of a standard tool like build, it will switch to using VCS and those ignored files won't be added - meaning it is really easy to have a project that doesn't support build, including various GitHub Actions. Hatchling wins this by a ton.

<!-- TODO: add - compatible with other build back-ends eg pdm can work with hatchling

Eli:
poetry: supports it, but is undocumented and uses setuptools under the hood, they plan to change how this works and then document it
pdm-back-end: supports it, and documents it -- and also uses setuptools under the hood
hatchling: permits you to define hooks for you to write your own custom build steps, including to build C++ extensions

-->

<!-- from eli about pdm
It would be more accurate to say that PDM supports using PDM and setuptools at the same time, so you run setuptools to produce the C extensions and then PDM receives the compiled extension files (.so, .pyd) and packages it up alongside the pure Python files.

Comment about hatch.
https://github.com/pyOpenSci/python-package-guide/pull/23#discussion_r1081108118

From ralf: There are no silver bullets here yet, no workflow tool is complete. Both Hatch and PDM are single-author tools, which is another concern. @eli-schwartz's assessment is unfortunately correct here I believe (at a high level at least, not sure about details). Hatch has the worst take on building compiled code by some distance. Unless its author starts developing an understanding of build systems / needs, and implements support for PEP 517 build back-end hooks in pyproject.toml, it's pretty much a dead end.

-->

<!--TODO Add examples of builds using each of the tools below?

pdm, hatch and poetry all have "ways" of supporting c extensions via pdm-build, hatchling and poetry's build back-end.
poetry's support for C extensions is not fully developed and documented (yet). Poetry doesn't offer a way to facilitate "communication" between poetry front end and another back-end like meson to build via a build hook.
PDM and hatch both offer a plugin type approach to support custom build steps
PDM (right now) is the only tool that supports other back-ends (hatch is working on this - 2 minor releases away)
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
pdm, hatch and poetry all have "ways" of supporting c extensions via pdm-build, hatchling and poetry's build back-end.
poetry's support for C extensions is not fully developed and documented (yet). Poetry doesn't offer a way to facilitate "communication" between poetry front end and another back-end like meson to build via a build hook.
PDM and hatch both offer a plugin type approach to support custom build steps
PDM (right now) is the only tool that supports other back-ends (hatch is working on this - 2 minor releases away)
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

<!--
COMMENTED OUT TEXT TO BE MOVED


# TODO LINK TO CI BUILDS FOR Documentation>
Maybe we can curate a list of CI builds that people can use??? or is that moving too close to a cookie cutter situation

The text below is being moved to the packaging infrastructure section which
doesn't exist YET... but will soon .
pyOpenSci packages must:

- Contain full documentation for any user-facing functions.
- Have a test suite that covers the major functionality of the package.
- Use continuous integration.
- Use an OSI approved software license.


## Other recommendations
### Python version support
You should always be explicit about which versions of Python your package supports.
Keeping compatibility with old Python versions can be difficult as functionality changes.
A good rule of thumb is that the package should support, at least,
the latest three Python versions (e.g., 3.8, 3.7, 3.6).

### Code Style
pyOpenSci encourages authors to consult [PEP 8](https://www.python.org/dev/peps/pep-0008/) for information on how to style your code.

### Linting
An automatic linter (e.g. flake8) can help ensure your code is clean and free of syntax errors. These can be integrated with your CI.

-->

<!--
```{tip}
### Python packaging resources that we love

We think the resources below are excellent but each have particular opinions
that you may or may not find in our packaging guide. For instance, the PyPA
guide encourages users to store their package in a `src/package-name` directory.
While we accept that approach many of our community members prefer to not use
the `src` directory.

* [Python packaging for research software engineers](https://merely-useful.tech/py-rse/)
* [PyPA packaging guide](https://packaging.python.org/en/latest/)
```
-->

<!--
* one of the benefits of wheel is pretty much avoiding setup.py which
has code mixed in. makes you more vulnerable to a code injection on install.

assuming this means if the package is already pre-built than setup.py isn't running anything on install because install is just moving files across to the machine to be run.

And having metadata separate allows someone to view the metadata without
running any python code as it's a machine and human readable format.

https://scikit-hep.org/developer/pep621
-->
