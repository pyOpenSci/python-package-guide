# Get Started with Documenting Your Python Package

🚧 UNDER CONSTRUCTION - THIS CONTENT SHOULD BE FURTHER DEVELOPED BY THE END OF 2022! KEEP CHECKING BACK TO UPDATES AS THEY ARE IN PROGRESS🚧


Documentation is as important to the success of your Python open source package 
as the code itself. While quality code is valuable as it gets the tasks that your
package seeks to achieve, completed, if users don't understand how to use the 
tools in your package then they won't use your tool. 

## Documentation elements that we look for when reviewing a Python package

In the pyOpenSci peer review process we look for several things when evaluating
package documentation including:

1. A clear and to the point README file 
2. Documentation of the functionality of your code. This is often setup using Sphinx/ Read the docs or some other documentation platform 
3.  Sufficient API documentation of your packages API (this means that docstrings are formatted with explanations of each variable and better yet quick vignettes that demonstrate how to use the function or class)
4. A CONTRIBUTING guide that has clear instructions that others can follow to setup a development environment. This will support others contributing to your project.

# TODO LINK TO CI BUILDS FOR Documentation>
Maybe we can curate a list of CI builds that people can use??? or is that moving too close to a cookie cutter situation




### License file 

Your software should be licensed using an OSI approved license. The GitHub 
repo should have a license file for that specific license. 
<LINK TO A LICENSE RESOURCE(s) for selecting a license>

### CONTRIBUTING file  

pyOpenSci packages must:

- Contain full documentation for any user-facing functions.
- Have a test suite that covers the major functionality of the package.
- Use continuous integration.
- Use an OSI approved software license.




### License
pyOpenSci projects should use an open source software license that is approved by the Open Software Initiative (OSI). OSI's website has a [list of popular licenses](https://opensource.org/licenses), and GitHub has a [handy tool](https://choosealicense.com/) for choosing a license.

**Good/Better/Best:**
- **Good:** Include a open source software license with your package.
- **Better/Best:** Choose a license based on your needs and future use of package, plus explain your choice in your submission for review.

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


