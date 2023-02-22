# <img src="images/logo/logo.png" width=40 /> pyOpenSci Scientific Python Open Source Packaging Guide
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-13-orange.svg?style=flat-square)](#contributors-)
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
      <td align="center" valign="top" width="14.28%"><a href="https://fosstodon.org/@eriknw"><img src="https://avatars.githubusercontent.com/u/2058401?v=4?s=100" width="100px;" alt="Erik Welch"/><br /><sub><b>Erik Welch</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=eriknw" title="Documentation">📖</a> <a href="#design-eriknw" title="Design">🎨</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://nicholdav.info/"><img src="https://avatars.githubusercontent.com/u/11934090?v=4?s=100" width="100px;" alt="David Nicholson"/><br /><sub><b>David Nicholson</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=NickleDave" title="Documentation">📖</a> <a href="#design-NickleDave" title="Design">🎨</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://www.leahwasser.com"><img src="https://avatars.githubusercontent.com/u/7649194?v=4?s=100" width="100px;" alt="Leah Wasser"/><br /><sub><b>Leah Wasser</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=lwasser" title="Documentation">📖</a> <a href="#design-lwasser" title="Design">🎨</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://arianesasso.me"><img src="https://avatars.githubusercontent.com/u/3659681?v=4?s=100" width="100px;" alt="Ariane Sasso"/><br /><sub><b>Ariane Sasso</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=arianesasso" title="Documentation">📖</a> <a href="#design-arianesasso" title="Design">🎨</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://ml-gis-service.com"><img src="https://avatars.githubusercontent.com/u/31246246?v=4?s=100" width="100px;" alt="Simon"/><br /><sub><b>Simon</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=SimonMolinsky" title="Documentation">📖</a> <a href="#design-SimonMolinsky" title="Design">🎨</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://batalex.github.io"><img src="https://avatars.githubusercontent.com/u/11004857?v=4?s=100" width="100px;" alt="Alexandre Batisse"/><br /><sub><b>Alexandre Batisse</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=Batalex" title="Documentation">📖</a> <a href="#design-Batalex" title="Design">🎨</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/tupui"><img src="https://avatars.githubusercontent.com/u/23188539?v=4?s=100" width="100px;" alt="Pamphile Roy"/><br /><sub><b>Pamphile Roy</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=tupui" title="Documentation">📖</a> <a href="#design-tupui" title="Design">🎨</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="http://ocefpaf.github.io/python4oceanographers"><img src="https://avatars.githubusercontent.com/u/950575?v=4?s=100" width="100px;" alt="Filipe"/><br /><sub><b>Filipe</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=ocefpaf" title="Code">💻</a> <a href="#design-ocefpaf" title="Design">🎨</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://jon-e.net"><img src="https://avatars.githubusercontent.com/u/12961499?v=4?s=100" width="100px;" alt="Jonny Saunders"/><br /><sub><b>Jonny Saunders</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=sneakers-the-rat" title="Code">💻</a> <a href="#design-sneakers-the-rat" title="Design">🎨</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/radoering"><img src="https://avatars.githubusercontent.com/u/30527984?v=4?s=100" width="100px;" alt="Randy Döring"/><br /><sub><b>Randy Döring</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=radoering" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Aradoering" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://social.juanlu.space/@astrojuanlu"><img src="https://avatars.githubusercontent.com/u/316517?v=4?s=100" width="100px;" alt="Juan Luis Cano Rodríguez"/><br /><sub><b>Juan Luis Cano Rodríguez</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=astrojuanlu" title="Code">💻</a> <a href="#design-astrojuanlu" title="Design">🎨</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Aastrojuanlu" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://iscinumpy.dev"><img src="https://avatars.githubusercontent.com/u/4616906?v=4?s=100" width="100px;" alt="Henry Schreiner"/><br /><sub><b>Henry Schreiner</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=henryiii" title="Code">💻</a> <a href="#design-henryiii" title="Design">🎨</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Ahenryiii" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://mentat.za.net"><img src="https://avatars.githubusercontent.com/u/45071?v=4?s=100" width="100px;" alt="Stefan van der Walt"/><br /><sub><b>Stefan van der Walt</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=stefanv" title="Code">💻</a> <a href="#design-stefanv" title="Design">🎨</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Astefanv" title="Reviewed Pull Requests">👀</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
