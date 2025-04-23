# Create User Facing Documentation for your Python Package

<!-- ```{important}
## Quick takeaways: best practices

Your package:
* Should have a documentation website
* Should have all of its public (user-facing) functions and classes (the API) documented
* Should use numpy-style docstrings
* Documentation landing page should direct users to 4 core sections: get started, documentation content, about and community.
* Documentation should include short quick-start tutorials
``` -->

## Core components of user-facing Python package documentation
Below we break documentation into two broad types.

**User-facing documentation** refers to documentation that describes the way the
tools within a package are broadly used in workflows. **API documentation** refers
to documentation of functions, classes, methods, and attributes in your code and
is written at a more granular level. This documentation is what a user sees when
they type `help(function-name)`.

Your user-facing documentation for your Python package should include several
core components.

* **Documentation Website:** This refers to easy-to-read documentation that helps someone use your package. This documentation should help users both install and use your package.
* **Short Tutorials:** Your user-facing documentation should also include [**short tutorials** that showcase core features of your package](create-package-tutorials).
* **Package Code / API documentation:** You package's functions, classes, methods, and attributes (the API) should also be documented. API documentation can be generated from [docstrings](https://pandas.pydata.org/docs/development/contributing_docstring.html) found in your
code. Ideally, you have docstrings for all user-facing functions, classes, and methods in
your Python package. [We discuss code documentation and docstrings in greater detail here.](document-your-code-api-docstrings)

### Write usable documentation

User-facing documentation should be published on a
easy-to-navigate website. The documentation should be written keeping in mind that users may not be developers or expert-level programmers. Rather, the language
that you use in your documentation should not be
highly technical.

To make the language of your documentation more accessible
to a broader audience:

* Whenever possible, define technical terms and jargon.
* Consider writing instructions for a high-school level reader.
* Include step-by-step code examples, tutorials or vignettes that support getting started using your package.

## Four elements of a good open source documentation landing page

To make it easy for users to find what they need quickly,
consider adding quick links on your package's landing
page to the following elements:

* **Getting started:** This section should provide the user with a quick start for installing your package. A small example of how to use the package is good to have here as well. Or you can link to useful tutorials in the get started section.
* **About:** Describe your project,  stating its goals and its functionality.
* **Community:** Instructions for how to help and/or get involved. This might include links to your issues (if that is where you let users ask questions) or the discussion part of your GitHub repo. This section might include a development guide for those who might contribute to your package.
* **API Documentation:** This is the detailed project documentation. Here you store documentation for your package's API including all user-facing functions, classes, methods, and attributes as well as any additional high level discussion that will help people use your package.


```{figure} /images/geopandas-documentation-landing-page.png
---
name: geopandas-landing
width: 80%
alt: Image showing the landing page for GeoPandas documentation which has 4 sections including Getting started, Documentation, About GeoPandas, Community.
---
The documentation landing page of GeoPandas, a spatial Python library, has the 4 element specified above. Notice that the landing page is simple and directs users to each element using a Sphinx card.
```

NOTE: in many cases you can include your **README** file and your **CONTRIBUTING** files
in your documentation given those files may have some of the components listed above.

`````{tip}
You can include files in Sphinx using the include directive.
Below is an example of doing this using `myst` syntax.
````
```{include} ../README.md
```
````
`````
