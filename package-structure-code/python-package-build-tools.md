# Python Package Build Tools 

Below, we discuss some of the tools that are commonly used 
to build Python packages. This page is intended to help 
maintainers select a build tool to use. 


<!--
Where i'm leaving off here 

* setuptools is the OG clearly a lot of ppl use it. but the code base seems 
really messy and it's built on top of disutils that may be sunsetted i python 3.12 ?? so does it make sense for us all to use it or should we consider 
an example using hatch which seems really nice. extensible and has vcs built 
in as far as i can tell 


Below talk about each tool and the potential drawbacks.
post on slack about setuptools (next week) and also maybe discord.

I think this page should be it's own separate PR as i really want eyes on it. 
So more eyes == better. 
I can then have another Pr that has package structure...

setuptools vs hatch

-->

## Python package distribution files 

Before we dive into specific build tools, it's important 
to review the pieces of a "built" Python package. 

### Build 
To understand the two distributions below, it is important to understand two different types of files:

**Source files:** source files are the unbuilt files needed to build your package. An example of a build step would be compiling uncompiled code.  
**Binary files:** binary files are the files needed to install your package. These files are pre-build. As such any code that need to be compiled has been compiled / built in a binary distribution.

There are two types of distribution files that you will create to support 
publishing your Python package (on PyPI):

1. SDIST and 
1. Wheel 

<!-- 
* **SDist (Source Distribution):** This file, packaged as a **.tar.gz** tarball represents all of the unbuilt source files needed to build your package into an installable bundle. But the files within the package are not yet "built" if your package requires a  build step. Pure python packages most often do not require a build step. 
* **Wheel:** A wheel (**.whl**) is a **.zip** file containing all of the files needed to directly install your package. All of the files in a wheel are binaries - this means that code is already compiled / built. Wheels are thus faster to install - particularly if you have a package that requires build steps. -->

```{note}
If your package is a pure python package with no additional 
build / compilation steps then the SDIST and Wheel files will have the same content. 
```
<!-- TODO: add an example of the contents from SDIST vs .whl -->


### What is a SDist file? 

SDist, short for **S**ource **D**istribution file is a packaged file in `.tar.gz` 
format (often called a "tarball") that has all of the files needed to build your 
package. In the SDist format, your package's files are not included in a built 
format. Thus, anyone using this file, will have to build the files first before 
they can be installed. 

```{tip}
When you make a release on GitHub, it creates a SDist file (`.tar.gz`) that 
anyone can download and use. 
```

<!--
* one of the benefits of wheel is pretty much avoiding setup.py which 
has code mixed in. makes you more vulnerable to a code injection on install. 

assuming this means if the package is already pre-built than setup.py isn't running anything on install because install is just moving files across to the machine to be run. 

And having metadata separate allows someone to view the metadata without 
running any python code as it's a machine and human readable format.

https://scikit-hep.org/developer/pep621
-->

### Wheel (.whl files):  

A wheel or `.whl` file, is a zipped file that has 
the extension `.whl`. The wheel does not contain any of your packages 
configuration files such as **setup.cfg** or **pyproject.toml**. This distribution 
is a pre-build, ready-to-install format.

Because it is prebuilt, the wheel file will be faster to install for pure Python 
projects and can lead to consistent installs across machines. 

```{tip}
Wheels are also useful in the case that a package 
needs a **setup.py** file to support a more complex built. 
In this case, because the files in the wheel bundle 
are pre built, the user installing doesn't have to 
work about malicious code injections when it is installed. 
```

[Read more about the wheel format here](https://pythonwheels.com/)

## Tools to build python packages 

There are a suite of build tools that you can use to create your Python package's **SDist** and *Wheel* distributions. 
To better understand your options, it's important to first understand the difference between a 
build tool front-end and build backend. 

## Build front-end vs. build backend tools for Python packaging

### Build back-ends 
Every tool has a back-end 
build tool that actually builds the package and creates associated (SDist and wheel) distribution 
files. Some of the tools below such as Flit and pdm only 
support straight forward builds that do not have a compilation or other additional build step. These 
types of tools are ideal if you have a pure python 
project. 

Other tools such as Hatch/ hatchling and setuptools 
support more complex builds with custom steps. 

### Build front-ends
Each tool discussed below has a front-end interface that you can use to 
perform different types of Python packaging tasks.
For instance, 
you can use **Flit** to both build your package and 
to publish your package 
to PyPI (or test PyPI). 

Using a tool like **Flit** makes your workflow commands consistent and simple. For example, rather than using `twine` to publish your package to PyPi, you use `flit publish` (see below). 

Example to build your package with Flit: 

`flit build`

Example to publish to PyPI: 
`flit publish --repository testpypi` 

In the Pytyhon package build space **setuptools** is 
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


:::{figure-md} fig-target

<img src="../images/python-package-tools-2022-survey-pypa.png" alt="Graph showing the results of the 2022 PyPA survey of Python packaging tools. On the x axis is percent response and on the y axis are the tools." width="700px">

The Python developers survey results (n=>8,000 PyPI users) show setuptools and poetry as the most commonly used Python packaging tools. The core tools that we've seen being used in the scientific community are included here. [You can view the full survey results by clicking here.](https://drive.google.com/file/d/1U5d5SiXLVkzDpS0i1dJIA4Hu5Qg704T9/view)
:::

The tools that we review below are those that were the most commonly used in the above survey. They include:

* setuptools 
* flit 
* hatch
* pdm 


```{note}
Note that we are intentionally not including Poetry in this list because

1. Poetry pins dependencies using `^`. This `^` symbol means that there is an "upper bound" to the dependency. Thus poetry will bump a dependency version to a new major version.  Thus if your package using a dependency that is at version 1.2.3, poetry will never bump the dependency to 2.0 even if there is a new major version of the package. It will bump up to 1.9.x. . [This approach has been found to be problematic by many of our core scientific packages.](https://iscinumpy.dev/post/bound-version-constraints/)
## 1. TODO:  look at how it creates a pyproject toml file too... 

As such, we don't suggest that use of poetry for your 
development workflow even though it is an excellent and 
well documented tool. It's dependency management 
decisions have caused breaking changes in several large 
Python packages. 
```

## How to chose a build development tool

When deciding what tools you wish to use, there are a few basic criteria that 
you can use to help guide your decision:

### Build tools for pure Python packages 
If your package is a pure Python package and it doesn't have any additional build steps (such as compiling code, etc) you can use any of the tools discussed on 
this page including:

* Flit 
* Hatch 
* setuptools 
* pdm
 
 ### Build tools for Python packages with complex build steps 
If your package is not pure python, or it has complex build steps (or build
steps that you need to customize), then you should consider using: 

* Setuptools 
* Hatch 

Both of these tools allow you to customize your workflow with build steps needed 
to compile code. 

**Setuptools** is the "OG" tool that has been used for Python packaging for many years. 
**Hatch** is the newer, more modern tool that supports customization of any part of your packaging steps. 

## Tools that also support version bumping 
Of the tools listed on this page, two of them support 
direct package versioning:

* setuptools has setuptools_scm
* hatch has hatch_vcs

Each tool listed above allows you to setup a release 
workflow using your version control platform of choice 
(we are using GitHub as an example here given it is 
currently the most popular platform). 

## Python packaging tools summary 
A summary of what each of the tools offers can be found in the table below:
| Feature                                                                | Setuptools            | Flit      | Hatch     | PDM |
| ---------------------------------------------------------------------- | --------------------- | --------- | --------- | --- |
| Build backend                                                          | setuptools.build_meta | flit_core | hatchling |  pdm-pep517   |
| Supports projects that aren't pure python                              | yes                   | no        | yes       | no  |
| Supports custom build steps (before creating wheel)                    | yes                   | no        | yes       | no  |
| Has built in dependency management                                     | no                    | no        | no (future feature)       | yes |
| Can be used to publish directly to pypi                                | no (use twine)        | yes       | yes       | yes |
| Has version control based (eg git based) tooling to bump version       | setuptools_scm        | no        | hatch-vcs | ?   |
| Supports automated GitHub only releases (no local command line needed) | yes                   | no        | yes       |     |
(GitHu
## Setuptools 

build-backend: setuptools.build_meta 
build_frontend: setuptools 
build_versioning: setuptools_scm

[Setuptools](https://setuptools.pypa.io/en/latest/) is one of the most mature Python packaging tools with [development dating back to 2009 and earlier](https://setuptools.pypa.io/en/latest/history.html#). Given this history, it is said to be the most heavily used Python packaging tool.

### Potential benefits of setuptools
Some of the benefits include:
* Fully customizable build workflow
* Examples from many packages already using 
* Built in versioning using **setuptools_scm** 
* Supports modern packaging using **pyproject.toml** for metadata
 
### Potential drawbacks of setuptools 

Setuptools has a few drawbacks: 

* Because **setuptools** has to maintain backwards compatibility across a range of packages, it is 
not as flexible in its adoption of modern Python packaging
standards. This backwards compatibility also makes for a more complex code-base.
* To push to PyPI you will need to use another tool, **twine**. 
* TODO: Pradyun - bad defaults??

## Flit 

* Build Backend: **flit_core.buildapi**
* Versioning: No, Flit uses the  version from your package's ` __version__`. To update this you'd want to use another tool such as: bump2version <!!not really maintained now>
* [Why use flit?](https://flit.pypa.io/en/stable/rationale.html)

[Flit is a modern, no-nonsense, streamlined packaging tool](https://flit.pypa.io/en/stable/) that supports modern Python packaging standards. 

If you have a pure Python project and don't need any 
additional build steps for your package, Flit could be 
a tool for you. 

**Flit** supports **proproject.toml** files for metadata and dependency management.

**Flit** also has a front end command line that will help
you publish your package to both testPyPI and PyPI. 

<!--
many thanks to the resources here: https://henryiii.github.io/level-up-your-python/notebooks/2.7%20Creating%20Packages.html#  -->

## Hatch 

* Build Backend: **hatchling**
* Version control based versioning: Yes -  **hatch-vcs** 
* Push to PyPI: 

[**Hatch**](https://hatch.pypa.io/latest/) can be compared to **Flit** in that it simplifies your 
package's build workflow using consistent commands. However, it adds:

* A fully customizable build back-end 
* Full flexibility for each step of the build process. 
* Matrix environment creation to support testing across Python versions 
* [Nox / MAKEFILE like functionality](https://hatch.pypa.io/latest/environment/#selection) 
where you can create workflows in the pyproject.toml configuration to do things 
like serve docs locally and cleaning your package build directory. 

Hatch does about everything that you might need to support 
package development. It is ideal for packages that have compiled code and thus 
require custom build steps. 

While hatch does have some "opinions" about how parts
of the packaging build run, you can customize any aspect 
of it's build making if fully flexible. 

## PDM 

[PDM is a Python packaging and dependency management tool.](https://pdm.fming.dev/latest/). 
It is designed to support pure python projects. 

Benefits of using PDM:

* Dependency management

HELP! Can someone help me understand why you'd pick pdm please? my guess if is you want dependency management
