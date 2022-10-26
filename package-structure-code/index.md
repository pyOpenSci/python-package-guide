# Python package structure information 

🚧 UNDER CONSTRUCTION - THIS CONTENT SHOULD BE FURTHER DEVELOPED BY THE END OF 2022! KEEP CHECKING BACK TO UPDATES AS THEY ARE IN PROGRESS🚧

If you are looking for a more comprehensive guide to Python packaging we suggest 
you review the following excellent resources:

# TODO: add resource list 


Most of the sections also include Good/Better/Best recommendations.
Good meets the requirements, but going beyond the minimum can make package maintenance easier.


# TODO add a few links to really good guides on python package. 

Before you submit your package for review, you may want to check out the 
basic editor checks that we look for before a review can begin. These are bare-minimum 
infrastructure and content that we expect to see in your GitHub (or gitlab!)
repository before you submit to us. And in general these are basic items
that should be in any open software repository. 

These pages contain guides for authoring packages that will go through the
pyOpenSci review process. This includes best-practices and guidelines for structuring
and releasing your code, as well as considerations to take before you begin your
submission.





This section provides guidelines and tips for creating a Python package to 
submit for peer-review.

If you are considering submitting a package to pyOpenSci, or if you are just 
getting started with building a package, you may want to have a look at the 
bare-minimum [editor checks.](open-source-software-submissions/editor-in-chief-guide.html#editor-checklist-copy-template-below-to-use-in-the-issue) that pyOpenSci
performs before a review even begins. 

#TODO github checks 

These checks include several items

- **Sufficient Documentation** The package has sufficient documentation available online (README, sphinx docs) to allow us to evaluate package function and scope *without installing the package*. This includes:
  Get started tutorials or vignettes that help a user understand how to use the package and what it can do for them (often these have a name like "Getting started")
- **API documentation** - this includes clearly written doc strings with variables defined using a standard docstring format


## Packaging Guide

The [first section of this guidebook](overview) has info for creating and packaging your
Python project for review and release. The guide also includes info on the basic
requirements for pyOpenSci: testing, continuous integration, documentation, etc.

We also have a [section](release) about releasing your package on PyPI, but we encourage
you to wait until after the pyOpenSci review process has finished before uploading to
PyPI. This makes it easier to incorporate changes/suggestions from the reviews.

PyPI also has a [short tutorial](https://packaging.python.org/tutorials/packaging-projects/)
on how to package a Python project for easy installation.


