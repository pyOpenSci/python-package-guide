# README File Guidelines and Resources

The **README.md** file is often the first thing that someone sees when they consider
installing your package. 

This file is both the landing page of:

* Your file on package manager landing pages like PyPI and Anaconda
* Your package's GitHub repository

Thus, it is important that you spend some time up front creating a high quality 
**README.md** file for your Python package.

<!-- # TODO screenshots of landing pages in github and pypi  -->

Your README.md file should be located in the root 
of your GitHub repository. 

<!-- # TODO provide some screenshots of our repo with a readme file -->

## Organizing your README File from the most broad information to the most specific - Cognitive funneling

We suggest organizing the content in your **README** file so that the most broad information is at the top of the file. Information then 
becomes more specific 
and potentially more technical as the user moves down the file. 

```{note}
[Cognitive funneling approach](https://github.com/hackergrrl/art-of-readme#cognitive-funneling) refers to content structure where the most 
broad information is at the top and becomes increasingly more specific 
and possibly technical lower down in the file. 
```

This approach of starting broad and progressively getting more specific
will make your **README** file more accessible and easier-to-digest for a broader group of users. An overly complex or poorly organized **README** 
file will likely result in users getting lost, not understanding 
what your package does and how it could be useful to them.


<!-- # TODO make a checklist block style -->

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
- [ ] Links to your packages documentation / website.
- [ ] A few descriptive links to any tutorials you've created for your pacakge.
```
````

A more detailed explanation of every element in this check list is below. 

## What your README.md file should contain (bare minimum)

At a minimum, your package's **README.md** file should include 
(from top to bottom):

### ✅ Your package's name
Ideally your GitHub repository's name is also the name of your package. The more 
self explanatory that name is, the better. 

### ✅ Badges for current package version, continuous integration and test coverage

Badges are a useful way to draw attention to the quality of your project and to
assure users that your package is well-designed, tested, and maintained.
It is common to provide a collection of badges towards the top of your 
README file for others to quickly browse.

Some badges that you should adding to your README file include:

* Current version of the package on pypi / conda forge (the example badge below provides a github release value in our package guide isn't an installable tool.)

![GitHub release (latest by date)](https://img.shields.io/github/v/release/pyopensci/python-package-guide?color=purple&display_name=tag&style=plastic)
 

```markdown
Github release 
![GitHub release (latest by date)](https://img.shields.io/github/v/release/your-github-org-name/package-repo-name?color=purple&display_name=tag&style=plastic)
```

* Continuous integration Status of tests (pass or fail)

Circle CI badge: 
[![CircleCI](https://circleci.com/gh/pyOpenSci/python-package-guide.svg?style=svg)](https://circleci.com/gh/pyOpenSci/python-package-guide)

Example GitHub actions badge:

![Docs Building](https://github.com/pyOpenSci/python-package-guide/actions/workflows/build-book.yml/badge.svg)

```
![Docs Building](https://github.com/pyOpenSci/python-package-guide/actions/workflows/build-book.yml/badge.svg)
```

* Citation badge (DOI). It is OK if you do not have a DOI prior to the review. [![DOI](https://zenodo.org/badge/556814582.svg)](https://zenodo.org/badge/latestdoi/556814582)

Once you package is accepted to pyOpenSci, we will provide you with 
a badge to add to your repository that shows that it has been reviewed and accepted into the pyOpenSci scientific Python open source ecosystem! 

<!-- # TODO: add a pyopensci accepted badge here -->

```{note}
Beware of the overuse of badges! There is such a thing as too much of a good thing (which can overload a potential user!).
```

### ✅ A short, easy-to-understand description of what your package does 

At the top of your README file you should have a short, easy-to-understand, description that details the goals of your package and what purpose it serves.  The language in this description should use less technical terms so that a variety of users with varying scientific (and development) backgrounds can understand it. 

Consider writing for a 12th grade reading level which is an ideal level for more scientific content that serves a broad user base. The goal of this description to maximize accessibility of your **README** file.


### ✅ BRIEF quickstart code demonstration of how to use the package

Include a code quickstart that demonstrates how to use your package.
This quickstart should be simple. 

```{important}
### TOO MUCH OF A GOOD thing

Try to avoid including several tutorials in the readme file itself. This too will overwhelm the user with information. 

A short quickstart vignette that shows a user how to use your package is plenty for the README file. All other tutorials and documentation should be presented as descriptive links. 
```

### ✅ Descriptive links to package documentation, tutorials or vignettes.

Include descriptive links in your README file to:

* The package's documentation page. 
* Tutorials or vignettes that demonstrate application of your package. 

### ✅ Discussion of how this package fits within the broader scientific python landscape.

If applicable, describe how the package compares to other similar packages or complementary packages in the scientific Python ecosystem. This discussion can be brief. It's important for package maintainers to consider their package in the context of the broader ecosystem. You will be asked to do this when you submit your package for review for pyOpenSci.

### ✅ Installation instructions

Include instructions for installing your package. If you have published 
the package on both `PyPI` and `Conda` be sure to include instructions for both. 

### ✅ Document any addition setup required to use you package

Add any additional setup required that someone will need to do before using your package. Examples of additional setup steps including authentication tokens, or critical dependencies that don't get automatically installed when your package is installed. 

### ✅ Citation information

Finally be sure to include instructions on how to cite your package. 

### ✅ Links to Contributing Guide, Code of Conduct 
Last but not least provide direct links to your 
**CONTRIBUTING** guide and to your project's **code of conduct**. 


```{note}
### README Resources 

Below are some resources on creating great README.md files that you 
might find helpful.

* [The art of the README GitHub Repo](https://github.com/hackergrrl/art-of-readme)
* [Write a great readme - Bane Sullivan](https://github.com/banesullivan/README)
* [Readme resources from rOpenSci](https://devguide.ropensci.org/building.html#readme)
```




