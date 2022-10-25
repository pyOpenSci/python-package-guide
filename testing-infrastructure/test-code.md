# Tests and Continuous Integration 

On this page you will explore the various levels of testing that pyOpenSci suggests
for your package. This page will be useful for you if you are new to creating a 
Python package as it will provide you with and overview of what you need to consider 
in your package development. If you are an existing developer, we hope that it will
guide you in the right direction to having a more robust testing infrastructure 
in your package. 


## Why create tests for your package

Tests are setup to ensure that your package is functioning as you expect it to

# TODO * resources on tests suites and why here... 

If you have tests setup with Continuous Integration (more on that below), tests 
also make it easier for someone other than you to  contribute your package and 
see that they didn't inadvertently break other functionality.

There are several different things that you should consider testing when you 
create your Python package. Setting up this infrastructure early in your development 
is ideal. For tests on things like documentation, it could catch things like 
broken links as you are creating your documentation rather than having to go back 
and fix many broken links later. 

* Tests for package functionality (test suites)
* Tests for documentation builds (build works, link checker, etc)
* Tests for API documentation (optional). API documentation is often published in your documentation website if you are using Sphinx.  

Below you will learn about all three. Rather than turn this into a tutorial 
we will curate resources here that we hope are helpful as you consider the structure 
of your package. 


## Your package should have a test suites that tests functionality

Code test suites are the traditional types of tests that developers consider.
In fact, some developers will create test first, before they begin coding to 
ensure that the code that they write does do what they intend it to do from this 
start. This also forces a developer to consider edge cases - things that users might 
do that you may not expect when initially creating the package. 

All pyOpenSci packages should have a test suite. We will not review your package 
if you do not have a test suite and continuous integration (see below) setup for 
your package. 

# TODO: LINK See editor checks for a reminder of the bare minimum requirements for peer review with pyOpensci 

Tests should cover both major functionality in the package and also the behavior 
of the package in case of errors.

When you write tests please:

- Write unit tests for all functions, and all package code in general, ensuring key functionality is covered. Test coverage below 75% will likely require additional tests or explanation before being sent for review.
- We recommend using pytest for writing tests, but you can use other tools. Strive to write tests as you write each new function. This serves the obvious need to have proper testing for the package, but allows you to think about various ways in which a function can fail, and to defensively code against those.
- Consider using tox to test your package with multiple versions of Python 2 and 3.
- If you set up CI with code coverage, use your package's code coverage report to identify untested lines, and to add further tests.

**Good/Better/Best:**
- **Good:** A test suite that covers major functionality of the package.
- **Better:** The above, with high code coverage.
- **Best:** All of the above, plus using tox to test multiple versions of Python.

