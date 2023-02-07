# Complex Python package builds


* link to ralf's blog and book on complex builds
* keep this page high level so we don't get weight downsides
* can use the examplePy repo stefan and I are working on that will test various build combinations




* pdm, hatch and poetry all have "ways" of supporting c extensions via pdm-build, hatchling and poetry's build back end.
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

-->

```{note}
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

```
