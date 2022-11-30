# Contributing and License Files in your Python Package

Your python package should include a file called **CONTRIBUTING.md** located in the 
root of your repository (with your **README.md** file).

## What should be in the contributing guide

The contributing file should include information about the types 
of contributions that you welcome, and how you'd like to see 
contributions happen. 

This guide should also include information for someone interested in asking questions, 
submitting issues or pull requests:

* Any guidelines that you have in place for users submitting issues, pull requests or asking questions. 
* A link to your code of conduct
* A link to or include how your code of conduct is enforced.

It should also include informative descriptive links for a 
development guide (see below) that has instructions for:

* Setting up a development environment locally to work on your package
* How the test suite is setup and run 
* How you can build docs locally

## Development guide for your package 



### Why a development guide is important 

While a well thought-out continuous integration setup in your repository 
can allow users to skip building the package locally (especially if they are just updating text), it's valuable to have a development guide, in the case that you wish to:

* onboard new maintainers
* allow technically inclined contributors to make thoughtful code based pr's

It also is important to pyOpenSci that the maintenance workflow is 
documented in the case that we need to help you onboard new 
maintainers in the future. 



```{tip}
[The mozilla open workshop has a nice outline of things to consider when 
creating a contributing guide](https://mozillascience.github.io/working-open-workshop/contributing/)
```

### License
pyOpenSci projects should use an open source software license that is approved 
by the Open Software Initiative (OSI). OSI's website has a 
[list of popular licenses](https://opensource.org/licenses), and GitHub has a 
[handy tool](https://choosealicense.com/) for choosing a license.

<!-- 
pyOpenSci packages must:

- Contain full documentation for any user-facing functions.
- Have a test suite that covers the major functionality of the package.
- Use continuous integration.
- Use an OSI approved software license.

**Good/Better/Best:**
- **Good:** Include a open source software license with your package.
- **Better/Best:** Choose a license based on your needs and future use of package, plus explain your choice in your submission for review. -->