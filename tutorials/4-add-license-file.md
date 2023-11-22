# Add a LICENSE & CODE_OF_CONDUCT to your Python package

In the [previous lesson](2-add-readme) you created a basic `README.md` file for your scientific Python package's repository.

:::{admonition} Learning objectives
:class: tip

In this lesson you will learn:

1. How to select and add a `LICENSE` file to your package repository with a focus on the GitHub interface.
2. How to add a `CODE_OF_CONDUCT` file to your package repository.
3. How you can use the Contributors Covenant website to add generic language as a starting place for your `CODE_OF_CONDUCT`.
:::

<!--
NOTE: in this case if they add a license on github they will want to pull those changes down.

So in the previous lesson we should have them add the readme, then commit the readme and push to github main branch.

TODO: be sure to ask them to add a link to both their license and their COC in this lesson -->

## Add a LICENSE file to your repository

A license file is a document that contains legal language about how users are allowed to use and reuse your software. Generally, we suggest that you select a permissive license that accommodates the other most commonly used licenses in the scientific Python ecosystem (MIT and BSD-3).

[Click here for an overview of license recommendations for the scientific Python ecosystem](../documentation/repository-files/license-files.html#use-open-permissive-licenses-when-possible)

### Where should the license file live & how do you add it?

Your `LICENSE` file should be placed at the root of your package's repository.

There are two ways to add a license file:

1. When you create a new repository on GitHub, it will ask you if you wish to add a `LICENSE` file at that time.
2. You can also always go back and add a `LICENSE` file to your repo.

### How to add a LICENSE to your GitHub repository

If you don't already have a `LICENSE` file in your repo, add one now.

* Follow the instructions to select and add a license to your repository on the [<i class="fa-brands fa-github"></i> GitHub LICENSE page]( https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) .
* Once you have added your LICENSE file, be sure to sync your git local repository with the repository on GitHub.com. This means running `git pull` to update your local branch.

:::{admonition} An overview of LICENSES in the scientific Python ecosystem
:class: note

In the pyOpenSci [packaging guidebook](../documentation/repository-files/license-files.html), we provide an overview of license in the scientific Python ecosystem. We review why license files are important, which ones are most commonly used for scientific software and how to select the correct license.

If you want a broad overview of why licenses are important for protecting open source software, [check out this blog post that overviews the legal side of things.](https://opensource.guide/legal/#just-give-me-the-tldr-on-what-i-need-to-protect-my-project)
:::

:::{figure-md} github-new-repo
<img src="../images/tutorials/github-new-repo.png" alt="Add alt " width="500px">

When you initially create a repository on GitHub you can add a license
through their interface.
:::


:::{figure-md} view-license
<img src="../images/tutorials/view-license-github.png" alt="Add alt " width="500px">

You can also view an overview of the license on GitHub if you view it in the GitHub interface.
:::

Next, you will add a `CODE_OF_CONDUCT` file to your repository.

## Add a CODE_OF_CONDUCT file to your repo

A `CODE_OF_CONDUCT` file is critical to supporting your community as
grows around your project. The `CODE_OF_CONDUCT` is important as it:
1. Establishes guidelines for how users and contributors interact with each other and you in your software repository.
2. Identifies negative behaviors that you don't want in your interactions. In extreme situations, you can use this language as a moderation tool that can be references when moderating tense conversations.

If you are unsure of what language to add to your `CODE_OF_CONDUCT`
file, we suggest that you adopt the [contributor covenant language](https://www.contributor-covenant.org/version/2/1/code_of_conduct/) as a starting place.

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](#)

* Add a `CODE_OF_CONDUCT.md` file to your repository if it doesn't
already exist.
* Visit the contributor covenant website and [add the language here to the file.](https://www.contributor-covenant.org/version/2/1/code_of_conduct/) [A markdown version can be found here.](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md)


:::{admonition} Additional Code of Conduct resources
:class: note

* [<i class="fa-brands fa-github"></i> Guide: `CODE_OF_CONDUCT.md` files](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-code-of-conduct-to-your-project)
* [pyOpenSci package guide `CODE_OF_CONDUCT.md` overview](https://www.pyopensci.org/python-package-guide/documentation/repository-files/code-of-conduct-file.html)

:::

## <i class="fa-solid fa-arrows-rotate"></i> Sync your LICENSE & COC files to GitHub / GitLab

It's time to sync your repository to ensure that all of the files that you have added locally are on GitHUB.com and all of the files that have been added on GitHub are local.

* If you added a `LICENSE` file to GitHub using the GitHub online interface, be sure to pull it down locally using `git pull`.
* Similarly be sure to pull or push your newly added `CODE_OF_CONDUCT` to your GitHub repository if you created that file locally.

## <i class="fa-solid fa-hands-bubbles"></i> Wrap up

In this lesson and the [last lesson](2-add-readme), you have now added:

* `README` file
* `LICENSE` file
* `CODE_OF_CONDUCT` file

These are core files that every scientific Python package should include. In the next lessons, you will:
* [Flesh out your `pyproject.toml` file](5-pyproject-toml) which will support building and publishing your package on PyPI. and
* You will learn how to [publish your package to PyPI](6-publish-pypi)!
