# README File Guidelines and Resources

 The **README.md** file is often the first thing that someone sees when they consider
installing your package. Thus, it is important that you spend some time up front creating a high quality 
**README.md** file for your Python package.

This file is the landing page of:

* Your file on package manager landing pages like PyPI and Anaconda
* Your package's GitHub repository

# TODO screenshots of landing pages in github and pypi 

Your README.md file should be located in the root 
of your GitHub repository. 

# TODO provide some screenshots of our repo with a readme file
## Organizing your README File from the most broad information to the most specific - Cognitive funneling

We suggest organizing the content in your README file so that the most broad information is at the top of the file. Information then becomes more specific 
and potentially more technical as the user moves down the file. 

This approach of starting broad and progressively getting more specific
will make your README file more accessible and easier-to-digest for a broader group of users. An overly complex or poorly organized README 
file will likely result in users getting lost, not understanding 
what your package does and how it could be useful to them.

```{note}
[Cognitive funneling approach](https://github.com/hackergrrl/art-of-readme#cognitive-funneling) refers to content structure where the most 
broad information is at the top and becomes increasingly more specific 
and possibly technical lower down in the file. 
```
## What your README.md file should contain (bare minimum)

Your **README.md** file should at a minimum include (from top to bottom):

### ✅ Your package's name
Ideally your GitHub repository's name is also the name of your package. The more 
self explanatory that name is, the better. 

### ✅ Badges for current package version, continuous integration and test coverage

Badges are a useful way to draw attention to the quality of your project and to
assure users that your package is well-designed, tested, and maintained.
It is common to provide a collection of badges towards the top of your 
README file for others to quickly browse.

Some badges that you might consider adding to your README file include:

* Current version of the package on pypi / conda forge (the example below is a github release value given our package guide isn't an installable tool.)

![GitHub release (latest by date)](https://img.shields.io/github/v/release/pyopensci/python-package-guide?color=purple&display_name=tag&style=plastic)

* Status of tests (pass or fail)

[![CircleCI](https://circleci.com/gh/pyOpenSci/python-package-guide.svg?style=svg)](https://circleci.com/gh/pyOpenSci/python-package-guide)

![Docs Building](https://github.com/pyOpenSci/python-package-guide/actions/workflows/build-book.yml/badge.svg)

* DOI (for citation) [![DOI](https://zenodo.org/badge/556814582.svg)](https://zenodo.org/badge/latestdoi/556814582)

Once you package is accepted to pyOpenSci, we will provide you with 
a badge to add to your repository that shows that it has been reviewed! 

# TODO: add a pyopensci accepted badge here

```{note}
Beware of the overuse of badges! There is such a thing as too much of a good thing (which can overload a potential user!).
```

### ✅ A short, easy-to-understand description of what your package does 

At the top of your README file you should have a short, easy-to-understand, 1-3 sentence description of what your package does. And your goals for the package. The language in this description should use less technical terms so that a variety of users with varying scientific (and development) backgrounds can understand it. 

Consider writing for a 12th grade reading level which is an ideal level for more scientific content that serves a broad user base. The goal of this description to maximize accessibility of your **README** file.



### ✅ Installation instructions

Include instructions for installing your package. If you have published 
the package on both PyPI and Conda be sure to include instructions for both. 

### ✅ Document any addition setup required

Add any additional setup required  such as authentication tokens,  to 
get started using your package.

### ✅ Brief demonstration of how to use the package

This description ideally includes a quick start vignette that provides a code sample demonstrating use

### ✅ Descriptive links to package documentation, tutorials or vignettes.

Include descriptive links to to:

* The package's documentation page. 
* Tutorials or vignettes that demonstrate application of your package. 

```{note}
### TOO MUCH OF A GOOD thing

Try to avoid including several tutorials in the readme file itself. This too will overwhelm the user with information. 

A short quickstart vignette that shows a user how to use your package is plenty for the README file. All other tutorials and documentation should be presented as descriptive links. 
```

### ✅ Discussion of how this package fits within the broader scientific python landscape.

If applicable, describe how the package compares to other similar packages or complementary packages in the scientific Python ecosystem. This discussion can be brief. 

### ✅ Citation information

Finally be sure to include instructions on how to cite your package. 


### ✅ Links to Contributing Guide, Code of Conduct 
Last but not least it's a good idea to link to direct users to your 
contributing guide in case they want to contribute. And also to link to your project's code of conduct. 


**Good/Better/Best Recommendations:**
- **Good:** README with name, description, installation instructions, and direction to further documentation.
- **Better/Best:** All the above plus usage examples, citation information, and CI and/or test coverage badges.

**Better:**
Ideally you should also include a quick-start code demo that provides a quick vignette 
of how the tool might be used. 

The a clear explanation of what your package does, a quick-start vignette and instructions
to install your package provide users with an easy to digest understanding of 
how your package might be useful to them. 


```{note}
### README Resources 

Below are some resources on creating great README.md files that you 
might find helpful.

* [The art of the README GitHub Repo](https://github.com/hackergrrl/art-of-readme)
* [Write a great readme - Bane Sullivan](https://github.com/banesullivan/README)
```

