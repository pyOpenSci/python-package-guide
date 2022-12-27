# Contributing, License and Code of Conduct Files in your Python Open Source Package

A healthy Python package repository (or any open source software repository) should also have a: 

* Contributing.md file
* A development guide (if possible)
* A License file and 
* A CODE_OF_CONDUCT.md file 

## What a CONTRIBUTING.md file should contain

Your Python open source package should include a file called **CONTRIBUTING.md** located in the 
root of your repository (with your **README.md** file).

The contributing file should include information about the types 
of contributions that you welcome, and how you'd like to see 
contributions happen. 

This guide should also include information for someone interested in asking questions, 
submitting issues or pull requests:

* Any guidelines that you have in place for users submitting issues, pull requests or asking questions. 
* A link to your code of conduct
* A link to a development guide if you have one
* A link to licensing information found in your README file. 

## What the development guide for your Python package should contain 

Ideally, your package should also have a development guide. This file may live in your package documentation and should be linked to from your CONTRIBUTING.md file (discussed above).
A development guide should clearly show 
technically proficient users how to:

* Set up a development environment locally to work on your package
* Run the test suite 
* Build documentation locally

It's also helpful to specify the types of tests you request if a contributor submits a new feature or a change to an existing feature that will not be covered by your existing test suite. 

If you have time to document it, it's also helpful to document your maintainer workflow and release processes. 

### Why a development guide is important 

It's valuable to have a development guide, in the 
case that you wish to:

* onboard new maintainers
* allow technically inclined contributors to make thoughtful and useful code based pull requests to your repository

It also is important to pyOpenSci that the maintenance workflow is 
documented in the case that we need to help you onboard new 
maintainers in the future. 

```{note}
A well thought-out continuous integration setup in your repository 
can allow users to skip building the package locally (especially if they are just updating text).
``` 

```{tip}
A development guide, while strongly recommended, is not a file that 
pyOpenSci requires a package to have in order to be eligible for 
review. Some maintainers may also opt to include the development information in their contributing guide.  
```




```{tip}
[The mozilla open workshop has a nice outline of things to consider when 
creating a contributing guide](https://mozillascience.github.io/working-open-workshop/contributing/)
```

## Your repository should have a LICENSE.md file

The root of your GitHub repository should also have a LICENSE.txt file. 

To be reviewed by pyOpenSci your project should use an open source 
software license that is approved 
by the Open Software Initiative (OSI). OSI's website has a 
[list of popular licenses](https://opensource.org/licenses). GitHub also has a 
[handy tool](https://choosealicense.com/) for choosing a license. 

If you choose your license through GitHub, you can also automatically get a copy of the license file to add to your repository. 

<!-- 
pyOpenSci packages must:

- Contain full documentation for any user-facing functions.
- Have a test suite that covers the major functionality of the package.
- Use continuous integration.
- Use an OSI approved software license.

**Good/Better/Best:**
- **Good:** Include a open source software license with your package.
- **Better/Best:** Choose a license based on your needs and future use of package, plus explain your choice in your submission for review. -->