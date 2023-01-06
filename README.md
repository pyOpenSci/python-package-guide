# <img src="images/logo/logo.png" width=40 /> pyOpenSci Scientific Python Open Source Packaging Guide
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-4-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

![GitHub release (latest by date)](https://img.shields.io/github/v/release/pyopensci/python-package-guide?color=purple&display_name=tag&style=plastic)

[![DOI](https://zenodo.org/badge/556814582.svg)](https://zenodo.org/badge/latestdoi/556814582)

[![CircleCI](https://circleci.com/gh/pyOpenSci/python-package-guide.svg?style=svg)](https://circleci.com/gh/pyOpenSci/python-package-guide)

## What is pyOpenSci?

pyOpenSci is devoted to building diverse, supportive community around
the Python open source tools that drive open science. We do this through:

* open peer review
* mentorship and 
* training.

pyOpenSci is an independent organization, fiscally sponsored by Community 
Initiatives.  

:construction: Construction note :construction:

This repository is currently under heavy construction. So please note that if
you are working through the content!

## Contributing statement


## How to setup

This repository contains the source files for the [pyOpenSci governance](https://pyopensci.org/governance).

## Build the governance document locally

Our governance documentation is built with [Sphinx](https://sphinx-doc.org) which is a documentation tool.

The easiest way to build our documentationis to use [the `nox` automation tool](https://nox.thea.codes/), a tool for quickly building environments and running commands within them.
Using `nox` ensures that your environment has all the dependencies needed to build the documentation.

To build, follow these steps:

1. Install `nox`

   ```console
   $ pip install nox
   ```
2. Build the documentation:

   ```console
   $ nox -s docs
   ```

This should create a local environment in a `.nox` folder, build the documentation (as specified in the `noxfile.py` configuration), and the output will be in `_build/html`.

To build live documentation that updates when you update local files, run the following command:

```console
$ nox -s docs-live
```


## Contributing to this guide

We welcome and issues and pull-requests to improve the content of this guide.
If you'd like to see an improvement, please [open an issue](https://github.com/pyOpenSci/governance/issues/new/choose).

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center"><a href="https://fosstodon.org/@eriknw"><img src="https://avatars.githubusercontent.com/u/2058401?v=4?s=100" width="100px;" alt="Erik Welch"/><br /><sub><b>Erik Welch</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=eriknw" title="Documentation">📖</a> <a href="#design-eriknw" title="Design">🎨</a></td>
      <td align="center"><a href="https://nicholdav.info/"><img src="https://avatars.githubusercontent.com/u/11934090?v=4?s=100" width="100px;" alt="David Nicholson"/><br /><sub><b>David Nicholson</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=NickleDave" title="Documentation">📖</a> <a href="#design-NickleDave" title="Design">🎨</a></td>
      <td align="center"><a href="http://www.leahwasser.com"><img src="https://avatars.githubusercontent.com/u/7649194?v=4?s=100" width="100px;" alt="Leah Wasser"/><br /><sub><b>Leah Wasser</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=lwasser" title="Documentation">📖</a> <a href="#design-lwasser" title="Design">🎨</a></td>
      <td align="center"><a href="http://arianesasso.me"><img src="https://avatars.githubusercontent.com/u/3659681?v=4?s=100" width="100px;" alt="Ariane Sasso"/><br /><sub><b>Ariane Sasso</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=arianesasso" title="Documentation">📖</a> <a href="#design-arianesasso" title="Design">🎨</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!