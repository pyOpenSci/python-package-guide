# Python package structure information 

If you plan to submit a package for review to pyOpenSci and are looking for 
some guidance on package structure, code formats and style, then this section is for you. 

## Guidelines for pyOpenSci's packaging recommendations 

<!-- Might belong on the LANDING page for this entire guide?-->

There are some differing opinions on what Python package structure should 
look like and what tools to use across the Python ecosystem. 

In this guide, we have made decisions around suggested standards and required 
standards, based upon the commonly used approaches in the scientific Python 
community.  Our goal is to help standardize packaging across this ecosystem.

In some cases the suggestions here may diverge from those in the non-scientific parts of the Python ecosystem. 

```{note}
The suggestions for package layout in this section are made with the 
intent of being helpful; they are not specific requirements for your 
package to be reviewed and accepted into our ecosystem.
```

In all cases, we try to align our suggestions with the most current, accepted
[PEP's (Python Enhancement Protocols)](https://peps.python.org/pep-0000/) and the [scientific-python community specs](https://scientific-python.org/specs/). 

```{note}
Have a look at the 
bare-minimum [editor checks](https://www.pyopensci.org/peer-review-guide/software-peer-review-guide/editor-in-chief-guide.html#editor-checklist-template) that pyOpenSci
performs before a review begins. These checks are useful to explore 
for both authors planning to submit a package to us for review and for 
anyone who is just getting started with creating a Python package. 

In general these are basic items that should be in any open software repository. 
```


<!-- 

These checks include several items

- **Sufficient Documentation** The package has sufficient documentation available online (README, sphinx docs) to allow us to evaluate package function and scope *without installing the package*. This includes:
  Get started tutorials or vignettes that help a user understand how to use the package and what it can do for them (often these have a name like "Getting started")
- **API documentation** - this includes clearly written doc strings with variables defined using a standard docstring format -->
<!-- 
```{tip}
### Python packaging resources that we love 

We think the resources below are excellent but each have particular opinions 
that you may or may not find in our packaging guide. For instance, the PyPA
guide encourages users to store their package in a `src/package-name` directory.
While we accept that approach many of our community members prefer to not use 
the `src` directory. 

* [Python packaging for research software engineers](https://merely-useful.tech/py-rse/)
* [PyPA packaging guide](https://packaging.python.org/en/latest/)
```
-->