# Data for your package

In this section we talk about data for your scientific Python package: 
when you would need it, and how you can access it and provide it to your users.

```{admonition}
:class: note
Some material adapted from:
https://www.dampfkraft.com/code/distributing-large-files-with-pypi.html  
https://learn.scientific-python.org/development/patterns/data-files/
```

## When and why you might need data

First we describe when and why you might need data. 
Basically there are two cases: 
for examples, and for tests.
We'll talk through both in the next couple of sections.

### Data for example usage

It's very common for scientific Python packages to need data that helps their users understand how the library is to be used. 
Often the package provides functionality to access this data, 
either by loading it from inside the source code, or by downloading it off of a remote host.
In fact, the latter approach is so common that libraries have been developed just to "fetch" data, 
like pooch. 
We will show you how to use both methods for providing access to data below, 
but here we present some examples.

#### Examples in pyOpenSci packages
* movingpandas: <https://movingpandas.github.io/movingpandas-website/2-analysis-examples/bird-migration.html> 

#### Examples in core scientific Python packages
* scikit-image: <https://github.com/scikit-image/scikit-image/tree/main/skimage/data> 
* scikit-learn: <https://github.com/scikit-learn/scikit-learn/tree/main/sklearn/datasets/data>

### Data for tests 
It is common to design your code and tests in such a way that you can quickly test on fake data, 
ranging from something as simple as a NumPy array of zeros, 
to something much more complex like a test suite that "mocks" data for a specific domain. 
This lets you make sure the core logic of your code works, *without* needing real data.
At the end of the day though, you do want to make sure your code works on real data, 
especially if it is scientific code that may work with very specific data formats.
That's why you will often want at least a small amount of real-world test data.
A good rule of thumb is to have a handful of small files,
say no more than 10 files that are a maximum of 50 MB each.
Anything more than that you will probably want to store on-line and download, 
for reasons we describe in the next section.

## Why you should prefer to download data: size limits

Below we will introduce places you can store data on-line, and show you tools you can use to download that data.
We suggest you prefer this approach when possible, 
The main reason for this is that there are limits on file and project sizes for forges, like GitHub and GitLab, 
and for package indexes--most importantly, PyPI.
Especially with scientific datasets that can be quite large, 
we want to be good citizens of the ecosystem and not place unneccesarry demands on the common infrastructure.

### Forges (GitHub, GitLab, BitBucket, etc.)

Forges for hosting source code have maximum sizes for both files and projects. 
For example, on GitHub, a single file cannot be more than 100 MB. 
You would be surprised how quickly you can make a csv file this big! 
You also want to avoid committing larger binary files (like images or audio) 
to a version control system like git, because it is hard to go back and remove them later, 
and it can really slow down the speed with which you can clone the project.
More importantly, it slows down the speed with which potential contributors can clone your project!

### Data size and PyPI

The Python Package Index (PyPI) places a limit on the size of individual files uploaded--where a "file" is either 
a sdist or a wheel--and also a limit on the total size of the project (the sum of all the "files"). 
These limits are not documented as far as we can tell, 
but most estimates are around 100 MB per file and 1 GB for the total project. 
Files this large place a real strain on the resources supporting PyPI, as discussed here. 
For this reason, as a good citizen in the Python ecosystem you should do everything you can to minimize your impact. 
Don't worry, we're here to help you do that! 
You can request increases for both file size and project size 
(see [here](https://pypi.org/help/#file-size-limit) 
and [here](https://pypi.org/help/#project-size-limit)) 
but we strongly suggest you read about other options here first.

## Where to store your data

Alright, we're strongly suggesting you don't try to cram your data into your code--where should you store it?
Here we provide several options.

### Within the repository

As stated above, there *are* cases where relatively small datasets 
can be included in a package.
If this data consists of examples for usage, 
then you would likely put it inside your source code 
so that it will be included in the sdist and wheel.
If the data is meant only for tests,
and you have a separate test directory (as we suggest)

* strengths and weaknesses
  * Strengths
    * easy to access
    * can be very do-able for smaller files, e.g. text files used in bioinformatics
  * Weaknesses
    * maximum file sizes on forges like GitHub and on PyPI
    * You want to avoid adding these files to your version control history (git) and draining the resources of PyPI
* examples:
    * pyOpenSci:
      * opengenomics: <https://github.com/JonnyTran/OpenOmics/tree/master/tests/data/TCGA_LUAD>   
      * jointly:  <https://github.com/hpi-dhc/jointly/tree/master/test-data> 
    * core scientific-python packages
      * scikit-learn: <https://github.com/scikit-learn/scikit-learn/tree/main/sklearn/datasets/data> 

### In the cloud

#### scientific data repositories
* strengths and weaknesses
  * strength: free, guaranteed lifetime of dataset, often appropriate for pyOpenSci packages
  * weaknesses: may be hard to automate for data that changes frequently
* examples
  * Zenodo
  * OSF
  * FigShare
  * Dryad (paid?)

#### private cloud
* strengths and weaknesses
  * strengths: robust; tooling exists to more easily automate updating of packages, but this requires more technical know-how
  * weaknesses: not free
* examples
  * AWS
  * Google Cloud
  * Linode

```{admonition} Data version control
:class: tip

Did you know that tools exist that let you track changes to datasets in the same way version control systems like git 
lets you track changes to code? Although you don't strictly need data versioning to include data with your package, 
you probably want to be aware that such tools exist if you are reading this section. 
Such tools could be particularly important if your package focuses mainly on providing access to datasets.
Within science, tools have been developed to provide distributed access to datasets. These tools 
general
DataLad https://www.datalad.org/ 
related tools that are used for data engineering and industry (maybe breakout?)
Git-LFS
DVC
Pachyderm (I think it's called?)
```

```{admonition} Field specific standards + metadata
:class: tip

It's important to be aware of field-specific standards
eg astronomy
neuroscience: DANDI, NWB
many pyOpenSci tools exist to address these standards or to provide interoperability because these standards don't exist
see also: FAIR data
```

## How to access your data

Last but definitely not least, it's important to understand how you *and* your users

### For examples: in documentation, tutorials, docstrings, etc.

### Accessing local files with importlib-resources

If you have included data files in your source code, then you can provide access to these through importlib-resources.

link to PyCon talk w/Barry Warsaw
code snippet example here
mention python-3.9 backport
* examples:
  * pyOpenSci packages:
    * crowsetta: <https://github.com/vocalpy/crowsetta/blob/main/src/crowsetta/data/data.py> 
  * core scientific Python packages:
    * scikit-learn: <https://github.com/scikit-learn/scikit-learn/blob/f86f41d80bff882689fc16bd7da1fef4a805b464/sklearn/datasets/_base.py#L297> 

### Accessing files that are hosted remotely with pooch
pooch: 
https://github.com/fatiando/pooch 
code snippet example of using pooch

### For tests
Many of the same tools apply.
You can download test data as a set-up step in your CI.
Pytest fixtures for accessing test data.
