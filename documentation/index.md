# Intro: Document Your Python Package

```{attention}
🚧 UNDER CONSTRUCTION - THIS CONTENT SHOULD BE FURTHER DEVELOPED BY THE END OF 2022! KEEP CHECKING BACK TO UPDATES AS THEY ARE IN PROGRESS🚧
```
## Documentation is critical to the success of your Python open source package 

Documentation is as important to the success of your Python open source package 
as the code itself. Quality code is of course valuable as it gets the tasks 
that your package seeks to achieve, done. However, if users don't understand 
how to use the tools in your package, then they won't use your tool. 

Further, if you wish to build a base of contributors to your package, having 
explicit information about how to contribute is critical.

## Documentation elements that we look for when reviewing a Python package

In the pyOpenSci peer review process we look for several things when evaluating
package documentation including:

1. [A clear and to the point **README.md** file](readme-files)
2. **Clear package documentation** that helps users understand how to install, use and cite your package. Package documentation is often setup using [Sphinx](https://www.sphinx-doc.org/en/master/) which is a Python-focused documentation engine. You can host your documentation using github pages or an online tool like [readthedocs](https://www.readthedocs.org).
3. **Package API documentation.** Package API documentation refers to documentation for each class, function, method and attribute that is user facing in your package. This mean means that your package methods and classes have docstrings that are formatted with explanations of each variable and better yet quick vignettes that demonstrate how to use the function or class). If you don't know what API documentation means this section is for you! 
4. A **CONTRIBUTING.md** file that outlines how others can contribute to your package. This file should also link to your development guide and code of conduct.A well-crafted contributing guide will make it much easier for the community to contribute to your project. 
5. A license file. 

<!-- # TODO LINK TO CI BUILD examples FOR Documentation - we have plenty in our repos already for folks to look at. -->





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


