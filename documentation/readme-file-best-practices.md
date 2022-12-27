# README File Guidelines and Resources

The **README.md** file is often the first thing that someone sees before they
install your package. 

The README.md file is the landing page of:

* Your file on package manager landing pages like PyPI and Anaconda
* Your package's GitHub repository

It is also used to measure:
* community health by github
* and included in package health landing pages such as snyk 


```{figure} ../images/pandera-python-package-readme-github.png
---
name: directive-fig
width: 80%
---
Your GitHub repository landing page highlights the README.md file. Here you can see the README.md file for the pyOpenSci package [Pandera](https://github.com/unionai-oss/pandera). *(screen shot taken Nov 23 2022)*
```

Thus, it is important that you spend some time up front creating a high quality 
**README.md** file for your Python package.

Your README.md file should be located in the root of your GitHub repository. 

````{note}
An editor or the editor in chief will ask you to revise your README file
before a review begins if it does not meet the criteria specified below. 

Please go through this list before submitting your package to pyOpenSci

```
### pyOpenSci README checklist 

Your README file should have the following information: 
- [ ] The name of the package
- [ ] Badges for the packages current published version, documentation and test suite build. (OPTIONAL: test coverage) 
- [ ] Easy-to-understand explanation (2-4 sentences) of what your tool does
- [ ] Context for how the tool fits into the broader ecosystem 
- [ ] If it's your package is a wrapper, link to the package that it is wrapping and any associated documentation. (If you do'nt know what a wrapper is - this probably doesn't apply to you!)
- [ ] A simple quickstart code example that a user can follow to provide a demonstration of what the package can do for them 
- [ ] Links to your package documentation / website.
- [ ] A few descriptive links to any tutorials you've created for your package.
```
````

## What your README.md file should contain

Your **README.md** file should contain the following things (listed from top to bottom):

### ✔️ Your package's name
Ideally your GitHub repository's name is also the name of your package. The more 
self explanatory that name is, the better. 

###  ✔️ Badges for current package version, continuous integration and test coverage

Badges are a useful way to draw attention to the quality of your project. Badges 
assure users that your package is well-designed, tested, and maintained. They 
are also a useful maintenance tool to evaluate if things are building properly. 
A great example of this is adding a readthedocs badge to your readme to quickly
see when the build on that site fails. 

It is common to provide a collection of badges towards the top of your 
README file for others to quickly browse.

Some badges that you might consider adding to your README file include:

* Current version of the package on pypi / conda 

Example: [![PyPI version shields.io](https://img.shields.io/pypi/v/pandera.svg)](https://pypi.org/project/pandera/)

* Status of tests (pass or fail) - Example: [![CI Build](https://github.com/pandera-dev/pandera/workflows/CI%20Tests/badge.svg?branch=main)](https://github.com/pandera-dev/pandera/actions?query=workflow%3A%22CI+Tests%22+branch%3Amain)

* Documentation build - Example: ![Docs Building](https://github.com/pyOpenSci/python-package-guide/actions/workflows/build-book.yml/badge.svg)

* DOI (for citation) Example: [![DOI](https://zenodo.org/badge/556814582.svg)](https://zenodo.org/badge/latestdoi/556814582)

```{tip}
Once you package is accepted to pyOpenSci, we will provide you with 
a badge to add to your repository that shows that it has been reviewed. 
[![pyOpenSci](https://tinyurl.com/y22nb8up)](https://github.com/pyOpenSci/software-review/issues/12)

```


```{caution}
Beware of the overuse of badges! There is such a thing as too much of a good thing (which can overload a potential user!).
```

### ✔️ A short, easy-to-understand description of what your package does 

At the top of your README file you should have a short, easy-to-understand, 1-3 
sentence description of what your package does. This section should clearly 
state your goals for the package. The language in this description should use 
less technical terms so that a variety of users with varying scientific (and 
development) backgrounds can understand it. 

In this description, it's useful to let users know how your package fits within
the broader scientific Python package ecosystem. If there are other similar packages 
or complementary package mentions them here in 1-2 sentences. 

```{tip}
Consider writing for a 12th grade reading level which is an ideal level for more scientific content that serves a broad user base. The goal of this description to maximize accessibility of your **README** file.
```

### ✔️ Installation instructions

Include instructions for installing your package. If you have published 
the package on both PyPI and Conda be sure to include instructions for both. 

### ✔️ Document any addition setup required

Add any additional setup required such as authentication tokens, to 
get started using your package. If setup is complex, consider linking to a 
installation page in your online documentation here rather than over complicating
your README file. 

### ✔️ Brief demonstration of how to use the package

This description ideally includes a quick start vignette that provides a code sample demonstrating use of your package. 

### ✔️ Descriptive links to package documentation, tutorials or vignettes.

Include descriptive links to:

* The package's documentation page. 
* Tutorials or vignettes that demonstrate application of your package. 

```{tip}
### TOO MUCH OF A GOOD thing

Try to avoid including several tutorials in the readme file itself. This too will overwhelm the user with information. 

A short quick-start vignette that shows a user how to use your package is plenty for the README file. All other tutorials and documentation should be presented as descriptive links. 
```

### ✔️ A Community Section with Links to Contributing Guide, Code of Conduct 
In your readme file direct users to more information on:
* contributing to your package 
* development setup for more advanced technical contributors 
* your code of conduct. 

All of the above files are important for building community around your project.

### ✔️ Citation information

Finally be sure to include instructions on how to cite your package. 
 

```{tip}
### README Resources 

Below are some resources on creating great README.md files that you 
might find helpful.

* [Write a great readme - Bane Sullivan](https://github.com/banesullivan/README)
* [The art of the README GitHub Repo](https://github.com/hackergrrl/art-of-readme)

```
