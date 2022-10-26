# README File Guidelines and Resources


```{note}

### Readme Resources 

* [The art of the README GitHub Repo](https://github.com/hackergrrl/art-of-readme)
```


The **README.md** file is often the first thing that someone sees when they consider
installing your package. This file is the landing page of:

* your file on package manager landing pages like PyPI and Anaconda
* your package's GitHub repository

# TODO screenshots of landing pages in github and pypi 

It is important that you spend some time up front creating a high quality 
**README.md** file for your Python package. This file should be located in the root 
of your GitHUb repository. 

# TODO provide some screenshots of our repo with a readme file
## Organizing your README File from the most broad information to the most specific - Cognitive funneling

We suggest organizing the content in your README file so that the most broad information is at the top of the file. Information then becomes more specific 
and potentially more technical as the user moves down the file. This approach 
will make your README file more accessible to a broader group of users who 
may find your tool useful but get lost in overly complex language early on 
in the document. 

```{note}
[Cognitive funneling approach](https://github.com/hackergrrl/art-of-readme#cognitive-funneling) refers to content structure where the most 
broad information is at the top and becomes increasingly more specific 
and possibly technical lower down in the file. 
```
## What your README.md file should contain (bare minimum)

Your **README.md** file should at a minimum include (from top to bottom):

### ✅  Your package's name
Ideally your GitHub repository's name is also the name of your package. The more 
self explanatory that name is, the better. 

### ✅  Badges for current package version, continuous integration and test coverage

See [the badges section](#badges) for more information. (But beware of the overuse of badges!)

# TODO - find the badges section and add here?

### ✅  A short, easy-to-understand description of what your package does 

(it's function) and it's goals. The language in this description should use less technical terms so that a variety of users with varying scientific backgrounds can understand it. Consider writing for a 12th grade reading level which is an ideal level for more scientific content that serves a broad user base. The goal of this description to maximize accessibility of your **README** file.

### ✅ Descriptive links to package documentation, tutorials or vignettes.

We suggest that you link to the package's documentation page. 
Then add descriptive links to any tutorials or vignettes that you create 

Tutorials nested within the readme. - we suggest including a single quickstart tutorial in your readme and then linking to other tutorials found in your 
documentation website rather than including too much information in the README.md 
itself. 



### ✅ Installation instructions

Be sure to include Instructions for installing your package. Include instructions for both PiP and Conda if you have published to both. 

### ✅
 Any additional setup required (authentication tokens, etc)

### ✅ Brief demonstration of how to use the package

This description ideally includes a quick start vignette that provides a code sample demonstrating use

### ✅ Links to documentation, tutorials and/or vignettes
 A link to your online documentation

### ✅ Discussion of how this package fits within the broader scientific python landscape.

- If applicable, how the package compares to other similar packages and/or how it relates to other packages

### ✅ Citation information

- Instructions on how to CITE your package. It's ok if you 



**Good/Better/Best Recommendations:**
- **Good:** README with name, description, installation instructions, and direction to further documentation.
- **Better/Best:** All the above plus usage examples, citation information, and CI and/or test coverage badges.

**Better:**
Ideally you should also include a quick-start code demo that provides a quick vignette 
of how the tool might be used. 

The a clear explanation of what your package does, a quick-start vignette and instructions
to install your package provide users with an easy to digest understanding of 
how your package might be useful to them. 
