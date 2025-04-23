# How to publish your Python package documentation online

We suggest that you setup a hosting service for your Python package
documentation. Two free and commonly used ways to
quickly create a documentation website hosting environment are below.

1. You can host your documentation yourself using [GitHub Pages](https://pages.github.com/) or another online hosting service.
1. You can host your documentation using [Read the Docs](https://readthedocs.org/).

## What is Read the Docs ?
[Read the Docs](https://readthedocs.org/) is a documentation hosting service that supports publishing your project's documentation.

Read the Docs is a fully featured, free, documentation hosting
service. Some of its many features include:

* Is free to host your documentation (but there are also paid tiers if you wish to customize hosting)
* Automates building your documentation
* Allows you to turn on integration with pull requests where you can view documentation build progress (success vs failure).
* Supports versioning of your documentation which allows users to refer to older tagged versions of the docs if they are using older versions of your package.
* Supports downloading of documentation in PDF and other formats.
* You can customize the documentation build using a **.readthedocs.yaml** file in your GitHub repository.


## What is GitHub Pages?
[GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages) is a free web
hosting service offered by GitHub. Using GitHub pages, you can build your
documentation locally or using a Continuous Integration setup, and then push
to a branch in your GitHub repository that is setup to run the GitHub Pages
web build.



## Read the Docs vs GitHub Pages

GitHub pages is a great option for your documentation deployment.
However, you will need to do a bit more work to build and deploy your
documentation if you use GitHub pages.

Read the Docs can be setup in your Read the Docs user account. The service
automates the entire process of building and deploying your documentation.

If you don't want to maintain a documentation website for your Python package,
we suggest using the Read the Docs website.
