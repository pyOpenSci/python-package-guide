# Get started with documentation

```{important}
## Quick takeaways: best practices

Your package: 
* Should have a documentation website 
* Should have all of its public (user-facing) functions and classes (the API) documented
* Should use numpy-style docstrings 
* Documentation landing page should direct users to 4 core sections: get started, documentation content, about and community.
* Documentation should include short quick-start tutorials
```

## Core components of Python package documentation 
In addition to the [core files that should be in your GitHub 
Repository](/documentation/repository-files/intro), 
there are several core components of Python package documentation, 
including:

* **User-facing documentation website:** This refers to easy-to-read documentation that helps a user work with your package. This documentation should help users both install and use the functionality of your package. User-facing documentation should include a get-started page that shows a user how to install your package and begin using it. 
* **Short Tutorials:** Your user facing documentation should also include [**short tutorials** that show a user how to quickly get started using your package](create-package-tutorials).   
* **API documentation:** The API refers to the functions and classes in a 
package that makes up the user interface. API documentation is generated from [docstrings](https://pandas.pydata.org/docs/development/contributing_docstring.html) found in your 
code. Ideally you have docstrings for all user-facing functions, methods and classes in 
your Python package. [We discuss code documentation and docstrings in greater detail here.](document-your-code-api-docstrings)

### Write easy-to-read documentation 

User-facing documentation should be published on a easy-to-navigate website. All language should be written with non-developer users in mind. This means 
using language that is less technical.

A few tips to make sure your documentation is accessible include: 

* Whenever possible, define technical terms and jargon.
* Consider writing instructions for a high-school level reader. 
* Include step-by-step code examples, tutorials or vignettes that support getting started using your package.

## Documentation landing page best practices 

To make it easy for users to find what they need quickly, all packages should 
have 4 elements on the home page of their documentation:

* **Getting started:** This section should provide the user with a quick start for installing your package. A small example of how to use the package is good to have here as well. 
* **About:** Describe your project, state project goals and what it does. 
* **Community:** Instructions for how to help and/or get involved. This section might include a development guide. 
* **Documentation:** The actual project documentation. You may have two sections of documentation - the user facing documentation and your API reference. 


```{figure} /images/geopandas-documentation-landing-page.png
---
name: directive-fig
width: 80%
alt: Image showing the landing page for GeoPandas documentation which has 4 sections including Getting started, Documentation, About GeoPandas, Community. 
---
The documentation landing page of GeoPandas, a spatial Python library, has the 4 element specified above. Notice that the landing page is simple and directs users to each element using a Sphinx card.
```

NOTE: in many cases you can include your **README** file and your **CONTRIBUTING** files 
in your documentation given those files may have some of the components listed above.

`````{tip}
You can include files in sphinx using the include directive.
Below is an example of doing this using `myst` syntax. 
````
```{include} ../README.md
```
````
`````
