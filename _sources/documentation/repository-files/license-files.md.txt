# License files for scientific Python open source software

:::{button-link} https://www.pyopensci.org/about-peer-review/
:color: primary
:class: sd-rounded-pill float-left

Want to learn how to add a license file to your GitHub repository? Check out this lesson.
:::

## What is a Open Source License file?

When we talk about LICENSE files, we are referring to a file in your
GitHub or GitLab repository that contains legally binding language
that describes to your users how they can legally use  (and not use) your package.

## Why licenses are important

A license file is important for all open source projects because it protects both you as a maintainer and your users. The license file helps your users and the community understand:

1. How they can use your software
2. Whether the software can be reused or adapted for other purposes
3. How people can contribute to your project

and more.

[Read more about why license files are critical in protecting both you as a maintainer and your users of your scientific Python open source package.](https://opensource.guide/legal/#just-give-me-the-tldr-on-what-i-need-to-protect-my-project)


## Where to store your license

Your `LICENSE` file should be stored at root of your GitHub / GitLab repository.

Some maintainers customize the language in their license files for specific reasons. However, if you are just getting started, we suggest that you select a
permissive license and then use the legal language templates provided both by GitHub and/or the [choosealicense.com](https://choosealicense.com/) website.

Licenses are legally binding, as such you should avoid trying to create your own license unless you have the guidance of legal council.

### Use open permissive licenses when possible

We generally suggest that you use a permissive, license that is [Open Software Initiative (OSI) approved](https://opensource.org/licenses/). If you are
[submitting your package to pyOpenSci for peer review](https://www.pyopensci.org/about-peer-review/index.html), then we require an OSI approved
license.

### How to choose a license

To select your license, we suggest that you use GitHub's
[Choose a License tool ](https://choosealicense.com/).

If you choose your license when creating a new GitHub repository, you can also
automatically get a text copy of the license file to add to your repository. However
in some cases the license that you want is not available through that online
process.

:::{admonition} License recommendations from the SciPy package
[The SciPy documentation has an excellent overview of licenses.](https://docs.scipy.org/doc/scipy/dev/core-dev/index.html#licensing). Once of the key elements
that these docs recommend is ensuring that the license that you select is
complementary to license used in the core scientific Python ecosystem.
Below is a highlight of this text which outlines license that are compatible
with the modified BSD license that SciPy uses.

> Other licenses that are compatible with the modified BSD license that SciPy uses are 2-clause BSD, MIT and PSF. Incompatible licenses are GPL, Apache and custom licenses that require attribution/citation or prohibit use for commercial purposes.

To coordinate with other packages in our scientific ecosystem, we also recommend
that you consider using either BSD or MIT as your
license. If you are unsure, the MIT license tends to be a simpler easier-to-understand option.
:::


## Important: make sure that you closely follow the guidelines outlines by the License that you chose

Every license has different guidelines in terms of what code
you can use in your package and also how others can (or can not) use the code in your package.

If you borrow code from other tools or online sources, make
sure that the license for the code that you are using also complies
with the license that you selected for your package.

:::{admonition} An example of how a license determine how code can be reused
:class: note

Let's use StackOverflow as an example that highlights how a license determines how code can or can not be used.

[Stack overflow uses a Creative Commons Share Alike license.](https://stackoverflow.com/help/licensing). The sharealike license requires you to use the same sharealike license when you reuse any code from StackOverflow.

This means that technically, if you copy code from the Stack Overflow website, and use it in your package. And your packages uses a different license such as a MIT license, you are violating Stack Overflow's license requirements!

🚨 Proceed with caution! 🚨
:::


##  What about software citation?

While many permissive licenses do not require citation we STRONG encourage that you cite all software that you use in papers, blogs and other publications. You tell your users how to cite your package by using a [citation.cff file](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files). We will cover this topic when we talk about creating DOI's for your package using zenodo.

<!-- TODO: add link when lesson is created - but also we don't yet know how citation.cff files work with Zenodo (do they work??) will the citation info update with a new Zenodo link

These files - we need to understand if that date releases auto populates or forces zenodo to modify it's citation. if it's not dynamic it could be problematic


-->
