# Documentation for your Open Source Python Package - An Overview


## Documentation is critical to the success of your Python open source package 

Documentation is as important to the success of your Python open source package 
as the code itself. Quality code is of course valuable as it gets the tasks 
that your package seeks to achieve, done. However, if users don't understand 
how to use the tools in your package, then they won't use your tool. 

Further, if you wish to build a base of contributors to your package, having 
explicit information about how to contribute is critical.

## Documentation elements that pyOpenSci looks for when reviewing a Python package


In the pyOpenSci peer review process we look for several things when evaluating
package documentation including:

1. [A clear and to the point **README.md** file](readme-files)
2. **User oriented package documentation** that helps users understand how to install, use and cite your package. 
3. **Package API documentation.** Package API documentation refers to documentation for each class, function, method and attribute that is user facing in your package. This mean means that your package methods and classes have docstrings that are formatted with explanations of each variable and better yet quick vignettes that demonstrate how to use the function or class). If you don't know what API documentation means this section is for you! 
4. A **CONTRIBUTING.md** file that outlines how others can contribute to your package. This file should also link to your development guide and code of conduct. A well-crafted contributing guide will make it much easier for the community to contribute to your project.
5. A **CODE_OF_CONDUCT.md** file.  
5. **License & Citation:** A license file and instructions for citing your package. 



```{figure} ../images/moving-pandas-python-package-github-main-repo.png
---
name: directive-fig
width: 80%
alt: Image showing the files in the Moving Pandas GitHub repository. 
---
An example GitHub repository with all of the major files in it including CONTRIBUTING.md, README.md, CODE_OF_CONDUCT.md and a LICENSE.txt file. *(screen shot taken Nov 23 2022)*
```

The above files are ones that are evaluated in many online package health
platforms. Below you can see the community standards page that everyone 
has in their GitHub repository. 

```{figure} ../images/moving-pandas-python-package-github-community-standards.png
---
name: directive-fig
width: 80%
---
GitHub community health looks for a readme file among other elements when it evaluates the community level health of your repository. This example is from the [moving pandas GitHub repo](https://github.com/anitagraser/movingpandas/community) *(screen shot taken Nov 23 2022)*
```

SNYK is another well-known company that keeps tabs on package health.
Below you can see a similar evaluation of files in the Github repo as a 
measure of community health. 

```{figure} ../images/moving-pandas-python-package-snyk-health.png
---
name: directive-fig
width: 80%
---
Screenshot showing [SNYK](https://snyk.io/advisor/python/movingpandas) package health for moving pandas. Notice both platforms look for a README file. *(screen shot taken Nov 23 2022)*
```


## What's next in this Python package documentation section?

The rest of the pages in this section will walk you through best practices for setting up
documentation for your Python package.


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


