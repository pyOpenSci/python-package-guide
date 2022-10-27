# Intro: Document Your Python Package

```{attention}
🚧 UNDER CONSTRUCTION - THIS CONTENT SHOULD BE FURTHER DEVELOPED BY THE END OF 2022! KEEP CHECKING BACK TO UPDATES AS THEY ARE IN PROGRESS🚧
```

Documentation is as important to the success of your Python open source package 
as the code itself. While quality code is valuable as it gets the tasks that your
package seeks to achieve, completed, if users don't understand how to use the 
tools in your package then they won't use your tool. 

## Documentation elements that we look for when reviewing a Python package

In the pyOpenSci peer review process we look for several things when evaluating
package documentation including:

1. A clear and to the point **README.md** file 
2. Documentation of the functionality of your code. This is often setup using Sphinx/ Read the docs or some other documentation platform 
3. Sufficient API documentation of your packages API (this means that docstrings are formatted with explanations of each variable and better yet quick vignettes that demonstrate how to use the function or class). If you don't know what API documentation means this section is FOR YOU! 
4. A **CONTRIBUTING.md** file that has clear instructions that others can follow to setup a development environment. This will support others contributing to your project. 
5. A license file that helps people 

# TODO LINK TO CI BUILD examples FOR Documentation - we have plenty in our repos already for folks to look at.





<!-- 
Commenting this out for now - it will be moved to another section

## Other recommendations
### Python version support
You should always be explicit about which versions of Python your package supports.
Keeping compatibility with old Python versions can be difficult as functionality changes.
A good rule of thumb is that the package should support, at least,
the latest three Python versions (e.g., 3.8, 3.7, 3.6).

### Code Style
pyOpenSci encourages authors to consult [PEP 8](https://www.python.org/dev/peps/pep-0008/) for information on how to style your code.

### Linting
An automatic linter (e.g. flake8) can help ensure your code is clean and free of syntax errors. These can be integrated with your CI. -->


