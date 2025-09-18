---
bibliography:
  - ../../bibliography.bib
---

(license-file)=

# License files for Python open source software

:::{button-link} <https://www.pyopensci.org/about-peer-review/>
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

We generally suggest that you use a permissive, license that is [Open Software Initiative (OSI) approved](https://opensource.org/license). If you are
[submitting your package to pyOpenSci for peer review](https://www.pyopensci.org/about-peer-review/index.html), then we require an OSI approved
license.

:::{admonition} Copyleft licenses
The other major category of licenses are ["copyleft" licenses](https://en.wikipedia.org/wiki/Copyleft).
Copyleft licenses require people that use your work to redistribute it with the same (or greater) rights to modify, copy, share, and redistribute it.
In other words, copyleft licenses prohibit someone taking your work, making a proprietary version of it, and redistributing it without providing the source code so others can do the same.
Copyleft licenses are "sticky" in that they are designed to ensure that more free software is created.

The difference between copyleft and permissive licenses is an important cultural divide in free and open source software (e.g., see {footcite}`hunterReclaimingComputingCommons2016`, {footcite}`gnuprojectWhatFreeSoftware2019`, {footcite}`gnuprojectWhatCopyleft2022`).
It is important to understand this difference when choosing your license. Copyleft licenses represents the "free" part of "free and open source software".
Free and open source software is intrinsically political, and it is important to be aware of power dynamics in computing as well as the practical problems of license compatibility (discussed below).
:::

### How to choose a license

To select your license, we suggest that you use GitHub's
[Choose a License tool](https://choosealicense.com/).

If you choose your license when creating a new GitHub repository, you can also
automatically get a text copy of the license file to add to your repository. However
in some cases the license that you want is not available through that online
process.

:::{admonition} License recommendations from the SciPy package
[The SciPy documentation has an excellent overview of licenses.](https://docs.scipy.org/doc/scipy/dev/core-dev/index.html#licensing) One of the key elements
that these docs recommend is ensuring that the license that you select is
compatible with licenses used in many parts of the scientific Python ecosystem.
Below is a highlight of this text which outlines license that are compatible
with the modified BSD license that SciPy uses.

> Other licenses that are compatible with the modified BSD license that SciPy uses are 2-clause BSD, MIT and PSF. Incompatible licenses are GPL, Apache and custom licenses that require attribution/citation or prohibit use for commercial purposes.

If your primary goal is for your code to be used by other, major packages in the scientific ecosystem, we also recommend
that you consider using either BSD or MIT as your
license. If you are unsure, the MIT license tends to be a simpler easier-to-understand option.
:::

## Important: make sure that you closely follow the guidelines outlines by the License that you chose

Every license has different guidelines in terms of what code
you can use in your package and also how others can (or can not) use the code in your package.

If you borrow code from other tools or online sources, make
sure that the license for the code that you are using also complies
with the license that you selected for your package.

A useful way to think about license compatibility is the distinction between **"inbound"** and **"outbound"** compatibility.
"Inbound" licenses are those that cover the software you plan to include in your package.
Your package is protected by an "outbound" license.

**Permissive licenses** like BSD and MIT have few **outbound** restrictions - they can be used in any way by downstream consumers, including making them proprietary.
This is why they are favored by many businesses and large packages that want to be adopted by businesses.
Permissive licenses have more **inbound** restrictions - they can't use software that requires more freedoms to be preserved than they do, like copyleft licenses.
A package licensed under MIT needs to take special care when including or modifying a package licensed under the GPL-3.

**Copyleft licenses** like GPL-3 have more **outbound** restrictions - they require more of packages that include, use, modify, and reproduce them.
This is the purpose of copyleft licenses, to ensure that derivative works remain free and open source.
They have fewer **inbound** restrictions - a GPL-3 licensed package can include any other permissively licensed and most copyleft licensed packages.

|                                                      Compatible | Dependency <br> ("Inbound") | Your Package | Downstream Package <br> ("Outbound") |
|----------------------------------------------------------------:|-----------------------------|--------------|--------------------------------------|
| <i class="fa-solid fa-check" style="color: MediumSeaGreen"></i> | Permissive                  | Permissive   |                                      |
|            <i class="fa-solid fa-x" style="color: Crimson"></i> | Copyleft                    | Permissive   |                                      |
| <i class="fa-solid fa-check" style="color: MediumSeaGreen"></i> |                             | Permissive   | Permissive                           |
| <i class="fa-solid fa-check" style="color: MediumSeaGreen"></i> |                             | Permissive   | Copyleft                             |
| <i class="fa-solid fa-check" style="color: MediumSeaGreen"></i> | Permissive                  | Copyleft     |                                      |
| <i class="fa-solid fa-check" style="color: MediumSeaGreen"></i> | Copyleft                    | Copyleft     |                                      |
|            <i class="fa-solid fa-x" style="color: Crimson"></i> |                             | Copyleft     | Permissive                           |
| <i class="fa-solid fa-check" style="color: MediumSeaGreen"></i> |                             | Copyleft     | Copyleft                             |

:::{admonition} An example of how a license determine how code can be reused
:class: note

Let's use StackOverflow as an example that highlights how a license determines how code can or can not be used.

[Stack Overflow uses a Creative Commons Share Alike license.](https://stackoverflow.com/help/licensing). The sharealike license requires you to use the same sharealike license when you reuse any code from Stack Overflow.

This means that from a legal perspective, if you copy code from the Stack Overflow website and use it in your package that is licensed differently, say with a MIT license, you are violating Stack Overflow's license requirements!
This would not be true with a GPL licensed package. `GPL-3` packages can include code licensed by `CC-BY-SA` {footcite}`creativecommonsShareAlikeCompatibilityGPLv32015`.

🚨 Proceed with caution! 🚨
:::

## What about software citation?

While many permissive licenses do not require citation, we strongly encourage that you cite all software that you use in papers, blogs, and other publications. You tell your users how to cite your package by using a [citation.cff file](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files).

### Citation.cff files: Making your software citable

A `CITATION.cff` file is a machine-readable file that provides citation information for your software package. The "cff" stands for "Citation File Format," which is a standardized format for software citation metadata.

#### What citation.cff files add to your repository

When you add a `CITATION.cff` file to your repository, GitHub automatically detects it and displays a "Cite this repository" button. This makes it easy for users to properly cite your software. The file contains standardized citation information that tools and services can automatically read and use. GitHub will generate both APA and BibTeX citation formats for users.

#### How dates are tracked in citation.cff files

The citation file tracks important dates for your software. The `date-released` field shows when the current version was released. The `date-published` field shows when the software was first made available. You also include a `version` field with the specific version number.

You should update these dates with each new release so people cite the correct version of your software.

#### Integration with Zenodo

Citation.cff files work well with Zenodo, which is a popular place to store research software and get DOIs. When you create a Zenodo release, it can automatically pull information from your citation file. This keeps your citation information the same between GitHub and Zenodo. You can also include your Zenodo DOI in the citation file. Each time you make a new GitHub release, it can create a new Zenodo version with updated citation information.


Here's a basic example of what a `CITATION.cff` file might look like:

```yaml
cff-version: 1.2.0
message: "If you use this software, please cite it as below."
authors:
  - family-names: "Your Last Name"
    given-names: "Your First Name"
    orcid: "https://orcid.org/0000-0000-0000-0000"
title: "Your Package Name"
version: 1.0.0
doi: "10.5281/zenodo.1234"
date-released: 2025-07-12
url: "https://github.com/yourusername/your-package"
```

# References

```{footbibliography}
```
