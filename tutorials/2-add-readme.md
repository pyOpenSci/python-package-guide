# What goes into your Python package README.md file?

```{button-link} https://www.pyopensci.org/python-package-guide/documentation/repository-files/readme-file-best-practices.html
:color: primary
:class: sd-rounded-pill float-left

If you want to learn more about readme files, you can check out our guidebook reference: the art of readme files.
```

:::{admonition} TODOS
:class: important

> this series would be great if there was a graphic with all of the steps. and each was highlighted at the top of the page.
> **TODO:** we didn't ask them to put code into a src dir in the previous lesson? probably good to do that.
> ...

:::

In the previous lesson you:

1. learned how create the basic structure of a Python package and
2. how to make your code `pip` installable.

:::{admonition} Learning objectives

In this lesson you will learn:

1. How to add a README.md file to your package.
2. What the core elements of a readme file are.

:::

## What is a README file?

The `README.md` file is a file located at the root of your GitHub or GitLab repo that helps
a user understand:

- You package's name and what it does
- The current development "state" of the package (through badges)
- How to use your package: this might include a short get started demo that shows someone how to import and quickly use your package. Or it could be a set of links to get started tutorials in your documentation.
- How to contribute to your package: normally you would link to a `CONTRIBUTING.md` and `Code_of_conduct` file in this part of the readme
- How to cite your package

Your **README.md** file is important as it is often the first thing that someone sees before they install your package. The README file also will be used to populate your PyPI landing page. So it's good to create this file before publishing to PyPI.

### GitHub and readme files.

Every GitHub repository landing page has a right hand side bar. This sidebar lists the elements of your package including there is column on the right hand side that lists and links to core informational elements of your package including:

- the Readme file
- License
- starts and
- forks

:::{figure-md} github-sidebar
<img src="../images/tutorials/github-repo-sidebar.png" alt="Add alt " width="500px">

The README.md file is not only the landing page for your package, it also is listed as one of the core elements describing your package repository on GitHub.
:::

## Create a README.md file for your package

- To get started if it doesn't already exist, create a file called `README.md` in your local github repository.

- At the top of the `README.md` file, add the name of your package (and a logo if you have one). It's fine if you don't have a logo.

- Next add the following sections to your `README.md` file

1. **Badges:** Add any badges below the name of your file. if you don't have badges yet, that is ok. you'll have at least one once you [publish your package to PyPI](4-publish-pypi) in lesson 4.
2. **Package overview:** Below the badges, add a section that provides an easy-to-understand overview of what your package does. Keep this section short and if you can avoid jargon or define technical words to make the description accessible to more people.
3. **Installation Instructions:** Below the description add installation instructions. this might tell people how to install your package `pip install packagename` or `conda install`... You can come back and add this information after you publish to PyPI in lesson 4.
4. **Additional Setup Information** In this section also briefly document (or link to documentation for) any additional setup that is required to use your package. This might include tokens or authentication information if it is applicable to your package. Or additional installations of tools such as GDAL, etc. Note: many packages wont need any additional information here!
5. **How to use your package:** Next add a brief demo of how to use your package. this might include a small code chunk that demonstrates importing and a quick call to functionality in your package.
6. **Descriptive links to docs:** Unless you already have your documentation online, you can leave this section empty for now. this section would include links to tutorials or documentation get-started pages that will help your users understand how to use your package.
7. **Community section:** this is where you'll add links to your contributing guide and code_of_conduct once you create those. You can also leave this empty for now.
8. **Citation information:** also leave this empty for now. You can learn how to setup your repository with zenodo to make it citable in [this lesson](extras/2-connect-repo-to-zenodo.md) in a future lesson.

Your finished `README.md` file should look something like this:

```markdown
# pyOpenSci-package

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.8365068.svg)](https://doi.org/10.5281/zenodo.8365068)
[![pyOpenSci](https://tinyurl.com/y22nb8up)](https://github.com/pyOpenSci/software-review/issues/115)

## What packagename does

Short description here using non technical language that describes what your package does.

## How to install

<todo - when i add more to the pyos package this can use that readme>
To install this package... use:

`pip install packagename`

## OPTIONAL - if you have additional setup instructions add them here. if not, skip this section.

## Get started using packagename

Here add a quick code demo showing a user how to use the package after it is installed.

`
from packagename.module import xmethod

a = xmethod.dosomething(var1, var2)

`

You can also add any links to this section to tutorials in your documentation.

## Community

information here about contributing to your package. links to your code of conduct and development guide.

## How to cite packagename

citation information here
```

## Wrapping up

While there are no hard and fast rules dictating what a README file looks like,
it's important to consider the information that a new user or contributor might
need when creating it. Above is a set of recommendations as you are just getting
started. You may find the need for other elements to be added to this file
as you further develop your package and as a community begins to use your
package.

In the next lesson, you will add another critical file - a LICENSE file - to
your Python package repository.
