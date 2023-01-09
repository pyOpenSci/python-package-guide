# Documentation for your Open Source Python Package: An Overview

```{important}
## Quick Takeaways: Documentation must haves

Your package should at a minimum have:
* README.MD file
* CONTRIBUTING.md file
* CODE_OF_CONDUCT.md 
* LICENSE.txt 
* User-facing documentation website with tutorials 
* API documentation (often found in the user facing documentation website)

The pages in this section of our guide provide you with more 
detail about creating each of the above elements. We also suggest 
tools that will help you build your documentation. 
```

## Documentation is critical to the success of your Python open source package 

Documentation is as important to the success of your Python open source package 
as the code itself. Quality code is of course valuable as its how your package gets the tasks done. However, if users don't understand 
how to use your package in their workflows, then they won't use it. 

Further, explicitly documenting how to contribute is critical if you wish 
to build a base of contributors to your package. 

## Documentation elements that pyOpenSci looks for when reviewing a Python package

In the pyOpenSci open peer review process we look for several files and elements
when evaluating package documentation, including:

1. [A clear and to the point **README.md** file](readme-file-best-practices)
1. [**User focused package documentation**](package-documentation-best-practices) that helps users understand how to install, use and cite your package. Documentation is most often contained in a stand-alone website. 
1. **Tutorials and quick start code examples** that help a user get started using your package. 
1. **Package API documentation.** Package API documentation refers to documentation for each class, function, method and user-facing attribute (*available for a user to see*) in your package. This means that your package methods and classes should have [thoughtful docstrings](https://pandas.pydata.org/docs/development/contributing_docstring.html) that describe both the purpose of the code element and each input and output.
1. A [**CONTRIBUTING.md** file](contributing-license-coc) that outlines how others can contribute to your package. This file should also link to your development guide and code of conduct. A well-crafted contributing guide will make it much easier for the community to contribute to your project.
 1. A [**CODE_OF_CONDUCT.md**](contributing-license-coc.html#the-code-of-conduct-md-file) file. This file sets up the guidelines for how your community interacts. It ideally ensures that everyone feels safe and can report inappropriate behavior if need be.   <!--<not sure why header targets aren't working here with sphinx they work online> -->
1. [**LICENSE.txt file & Citation instructions:**](contributing-license-coc.html#your-repository-should-have-a-license-md-file) A license file declaring the OSI-approved license that you select and instructions for citing your package. 

```{figure} ../images/moving-pandas-python-package-github-main-repo.png
---
name: directive-fig
width: 80%
alt: Image showing the files in the Moving Pandas GitHub repository. 
---
An example from the MovingPandas GitHub repository with all of the major files in it including CONTRIBUTING.md, README.md, CODE_OF_CONDUCT.md and a LICENSE.txt file. *(screen shot taken Nov 23 2022)*
```

The above files are evaluated on many online platforms that track package health.
platforms. Below you can see the community standards page that everyone 
has in their GitHub repository. 

```{figure} ../images/moving-pandas-python-package-github-community-standards.png
---
name: directive-fig
width: 80%
---
GitHub community health looks for a readme file among other elements when it evaluates the community level health of your repository. This example is from the [MovingPandas GitHub repo](https://github.com/anitagraser/movingpandas/community) *(screen shot taken Nov 23 2022)*
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
documentation for your Python package. We will also suggest tools that you can use to build your user-facing documentation website.


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


