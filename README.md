# <img src="https://www.pyopensci.org/images/logo.png" width=100 /> pyOpenSci scientific Python Packaging Guide

[![All Contributors](https://img.shields.io/github/all-contributors/pyOpenSci/python-package-guide?color=ee8449)](#contributors-)

![GitHub release (latest by date)](https://img.shields.io/github/v/release/pyopensci/python-package-guide?color=purple&display_name=tag&style=plastic)

[![DOI](https://zenodo.org/badge/556814582.svg)](https://zenodo.org/badge/latestdoi/556814582)

[![CircleCI](https://circleci.com/gh/pyOpenSci/python-package-guide.svg?style=svg)](https://circleci.com/gh/pyOpenSci/python-package-guide)

## What is pyOpenSci?

pyOpenSci is devoted to building diverse, supportive community around
the Python open source tools that drive open science. We do this through:

* open peer review
* mentorship
* training

pyOpenSci is an independent organization, fiscally sponsored by Community
Initiatives.

## Contributing statement


## How to setup

This repository contains the source files for the [pyOpenSci Python packaging guide](https://pyopensci.org/python-package-guide).

## Build the guidebook locally

Our guidebook is built with [Sphinx](https://sphinx-doc.org) which is a documentation tool and uses the pydata-sphinx-theme.

The easiest way to build our documentation is to use [the `nox` automation tool](https://nox.thea.codes/),
a tool for quickly building environments and running
commands within them.

Using `nox` ensures that your environment has all the dependencies needed to build the documentation.

To build, follow these steps:

1. Install `nox`

   ```console
   $ python -m pip install nox
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

### Building for release

When building for release, the docs are built multiple times for each translation,
but translations are only included in the production version of the guide after some completion threshold.

The sphinx build environment is controlled by an environment variable `SPHINX_ENV`

- when `SPHINX_ENV=development` (default), sphinx assumes all languages are built,
  and includes them in the language selector
- when `SPHINX_ENV=production`, only those languages in `release_languages` (set in `conf.py`)
  are built and included in the language selector.

Most of the time you should not need to set `SPHINX_ENV`,
as it is forced by the primary nox sessions intended to be used for release or development:

`SPHINX_ENV=development`
- `docs-live` - autobuild english
- `docs-live-lang` - autobuild a single language
- `docs-live-langs` - autobuild all languages

`SPHINX_ENV=production`
- `build-test` - build all languages for production

## Contributing to this guide

We welcome and issues and pull requests to improve the content of this guide.
If you'd like to see an improvement, please [open an issue](https://github.com/pyOpenSci/python-package-guide/issues/new/choose).

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="http://batalex.github.io"><img src="https://avatars.githubusercontent.com/u/11004857?v=4?s=100" width="100px;" alt="Alexandre Batisse"/><br /><sub><b>Alexandre Batisse</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=Batalex" title="Documentation">📖</a> <a href="#design-Batalex" title="Design">🎨</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/WeepingClown13"><img src="https://avatars.githubusercontent.com/u/95921427?v=4?s=100" width="100px;" alt="Ananthu C V"/><br /><sub><b>Ananthu C V</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3AWeepingClown13" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/abravalheri"><img src="https://avatars.githubusercontent.com/u/320755?v=4?s=100" width="100px;" alt="Anderson Bravalheri"/><br /><sub><b>Anderson Bravalheri</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=abravalheri" title="Code">💻</a> <a href="#design-abravalheri" title="Design">🎨</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://arianesasso.me"><img src="https://avatars.githubusercontent.com/u/3659681?v=4?s=100" width="100px;" alt="Ariane Sasso"/><br /><sub><b>Ariane Sasso</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=arianesasso" title="Documentation">📖</a> <a href="#design-arianesasso" title="Design">🎨</a> <a href="https://github.com/pyOpenSci/python-package-guide/commits?author=arianesasso" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Aarianesasso" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/BSuperbad"><img src="https://avatars.githubusercontent.com/u/100496041?v=4?s=100" width="100px;" alt="Brianne Wilhelmi"/><br /><sub><b>Brianne Wilhelmi</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=BSuperbad" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3ABSuperbad" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://ivory.idyll.org/blog/"><img src="https://avatars.githubusercontent.com/u/51016?v=4?s=100" width="100px;" alt="C. Titus Brown"/><br /><sub><b>C. Titus Brown</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=ctb" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Actb" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://medium.com/@calekochenour"><img src="https://avatars.githubusercontent.com/u/54423680?v=4?s=100" width="100px;" alt="Cale Kochenour"/><br /><sub><b>Cale Kochenour</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=calekochenour" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Acalekochenour" title="Reviewed Pull Requests">👀</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://hachyderm.io/web/@willingc"><img src="https://avatars.githubusercontent.com/u/2680980?v=4?s=100" width="100px;" alt="Carol Willing"/><br /><sub><b>Carol Willing</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Awillingc" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/chenghlee"><img src="https://avatars.githubusercontent.com/u/3485949?v=4?s=100" width="100px;" alt="Cheng H. Lee"/><br /><sub><b>Cheng H. Lee</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=chenghlee" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Achenghlee" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://orcid.org/0000-0003-2843-6044"><img src="https://avatars.githubusercontent.com/u/1662261?v=4?s=100" width="100px;" alt="Chiara Marmo"/><br /><sub><b>Chiara Marmo</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=cmarmo" title="Code">💻</a> <a href="#design-cmarmo" title="Design">🎨</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Acmarmo" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://chrisholdgraf.com"><img src="https://avatars.githubusercontent.com/u/1839645?v=4?s=100" width="100px;" alt="Chris Holdgraf"/><br /><sub><b>Chris Holdgraf</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=choldgraf" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Acholdgraf" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://possenrie.de"><img src="https://avatars.githubusercontent.com/u/1423562?v=4?s=100" width="100px;" alt="Daniel Possenriede"/><br /><sub><b>Daniel Possenriede</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=dpprdan" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Adpprdan" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://dhirschfeld.github.io"><img src="https://avatars.githubusercontent.com/u/881019?v=4?s=100" width="100px;" alt="Dave Hirschfeld"/><br /><sub><b>Dave Hirschfeld</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Adhirschfeld" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://nicholdav.info/"><img src="https://avatars.githubusercontent.com/u/11934090?v=4?s=100" width="100px;" alt="David Nicholson"/><br /><sub><b>David Nicholson</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=NickleDave" title="Documentation">📖</a> <a href="#design-NickleDave" title="Design">🎨</a> <a href="#tutorial-NickleDave" title="Tutorials">✅</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/eli-schwartz"><img src="https://avatars.githubusercontent.com/u/6551424?v=4?s=100" width="100px;" alt="Eli Schwartz"/><br /><sub><b>Eli Schwartz</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=eli-schwartz" title="Code">💻</a> <a href="#design-eli-schwartz" title="Design">🎨</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Aeli-schwartz" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://fosstodon.org/@eriknw"><img src="https://avatars.githubusercontent.com/u/2058401?v=4?s=100" width="100px;" alt="Erik Welch"/><br /><sub><b>Erik Welch</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=eriknw" title="Documentation">📖</a> <a href="#design-eriknw" title="Design">🎨</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://flpm.dev"><img src="https://avatars.githubusercontent.com/u/17676929?v=4?s=100" width="100px;" alt="Felipe Moreno"/><br /><sub><b>Felipe Moreno</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Aflpm" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/pyOpenSci/python-package-guide/commits?author=flpm" title="Code">💻</a> <a href="#translation-flpm" title="Translation">🌍</a> <a href="https://github.com/pyOpenSci/python-package-guide/commits?author=flpm" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://ocefpaf.github.io/python4oceanographers"><img src="https://avatars.githubusercontent.com/u/950575?v=4?s=100" width="100px;" alt="Filipe"/><br /><sub><b>Filipe</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=ocefpaf" title="Code">💻</a> <a href="#design-ocefpaf" title="Design">🎨</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://frostming.com"><img src="https://avatars.githubusercontent.com/u/16336606?v=4?s=100" width="100px;" alt="Frost Ming"/><br /><sub><b>Frost Ming</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=frostming" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Afrostming" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ayhanxian"><img src="https://avatars.githubusercontent.com/u/20816603?v=4?s=100" width="100px;" alt="Han"/><br /><sub><b>Han</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=ayhanxian" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Aayhanxian" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://iscinumpy.dev"><img src="https://avatars.githubusercontent.com/u/4616906?v=4?s=100" width="100px;" alt="Henry Schreiner"/><br /><sub><b>Henry Schreiner</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=henryiii" title="Code">💻</a> <a href="#design-henryiii" title="Design">🎨</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Ahenryiii" title="Reviewed Pull Requests">👀</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/hugovk"><img src="https://avatars.githubusercontent.com/u/1324225?v=4?s=100" width="100px;" alt="Hugo van Kemenade"/><br /><sub><b>Hugo van Kemenade</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=hugovk" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Ahugovk" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/InessaPawson"><img src="https://avatars.githubusercontent.com/u/43481325?v=4?s=100" width="100px;" alt="Inessa Pawson"/><br /><sub><b>Inessa Pawson</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=inessapawson" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Ainessapawson" title="Reviewed Pull Requests">👀</a> <a href="#tutorial-inessapawson" title="Tutorials">✅</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/isabelizimm"><img src="https://avatars.githubusercontent.com/u/54685329?v=4?s=100" width="100px;" alt="Isabel Zimmerman"/><br /><sub><b>Isabel Zimmerman</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=isabelizimm" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Aisabelizimm" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://xmnlab.github.io"><img src="https://avatars.githubusercontent.com/u/5209757?v=4?s=100" width="100px;" alt="Ivan Ogasawara"/><br /><sub><b>Ivan Ogasawara</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=xmnlab" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Axmnlab" title="Reviewed Pull Requests">👀</a> <a href="#tutorial-xmnlab" title="Tutorials">✅</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://jacksonwarnerburns.com"><img src="https://avatars.githubusercontent.com/u/33505528?v=4?s=100" width="100px;" alt="Jackson Burns"/><br /><sub><b>Jackson Burns</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=JacksonBurns" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3AJacksonBurns" title="Reviewed Pull Requests">👀</a> <a href="#tutorial-JacksonBurns" title="Tutorials">✅</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://web.science.mq.edu.au/directory/listing/person.htm?id=tjames"><img src="https://avatars.githubusercontent.com/u/1281144?v=4?s=100" width="100px;" alt="James Tocknell"/><br /><sub><b>James Tocknell</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=aragilar" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Aaragilar" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/jezdez"><img src="https://avatars.githubusercontent.com/u/1610?v=4?s=100" width="100px;" alt="Jannis Leidel"/><br /><sub><b>Jannis Leidel</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=jezdez" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Ajezdez" title="Reviewed Pull Requests">👀</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="http://blog.ucodery.com"><img src="https://avatars.githubusercontent.com/u/28751151?v=4?s=100" width="100px;" alt="Jeremy Paige"/><br /><sub><b>Jeremy Paige</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=ucodery" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Aucodery" title="Reviewed Pull Requests">👀</a> <a href="#tutorial-ucodery" title="Tutorials">✅</a> <a href="#maintenance-ucodery" title="Maintenance">🚧</a> <a href="https://github.com/pyOpenSci/python-package-guide/commits?author=ucodery" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/kierisi"><img src="https://avatars.githubusercontent.com/u/23085445?v=4?s=100" width="100px;" alt="Jesse Mostipak"/><br /><sub><b>Jesse Mostipak</b></sub></a><br /><a href="#tutorial-kierisi" title="Tutorials">✅</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/John-Drake"><img src="https://avatars.githubusercontent.com/u/22374979?v=4?s=100" width="100px;" alt="John Drake"/><br /><sub><b>John Drake</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=John-Drake" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3AJohn-Drake" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://jon-e.net"><img src="https://avatars.githubusercontent.com/u/12961499?v=4?s=100" width="100px;" alt="Jonny Saunders"/><br /><sub><b>Jonny Saunders</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=sneakers-the-rat" title="Code">💻</a> <a href="#design-sneakers-the-rat" title="Design">🎨</a> <a href="#ideas-sneakers-the-rat" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://jhkennedy.org"><img src="https://avatars.githubusercontent.com/u/7882693?v=4?s=100" width="100px;" alt="Joseph H Kennedy"/><br /><sub><b>Joseph H Kennedy</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=jhkennedy" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Ajhkennedy" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://social.juanlu.space/@astrojuanlu"><img src="https://avatars.githubusercontent.com/u/316517?v=4?s=100" width="100px;" alt="Juan Luis Cano Rodríguez"/><br /><sub><b>Juan Luis Cano Rodríguez</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=astrojuanlu" title="Code">💻</a> <a href="#design-astrojuanlu" title="Design">🎨</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Aastrojuanlu" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://karencranston.ca/"><img src="https://avatars.githubusercontent.com/u/312034?v=4?s=100" width="100px;" alt="Karen Cranston"/><br /><sub><b>Karen Cranston</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=kcranston" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Akcranston" title="Reviewed Pull Requests">👀</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/kenseehart"><img src="https://avatars.githubusercontent.com/u/612119?v=4?s=100" width="100px;" alt="Ken Seehart"/><br /><sub><b>Ken Seehart</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=kenseehart" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Akenseehart" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/kozo2"><img src="https://avatars.githubusercontent.com/u/12192?v=4?s=100" width="100px;" alt="Kozo Nishida"/><br /><sub><b>Kozo Nishida</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Akozo2" title="Reviewed Pull Requests">👀</a> <a href="#translation-kozo2" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://www.leahwasser.com"><img src="https://avatars.githubusercontent.com/u/7649194?v=4?s=100" width="100px;" alt="Leah Wasser"/><br /><sub><b>Leah Wasser</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=lwasser" title="Documentation">📖</a> <a href="#design-lwasser" title="Design">🎨</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/mknorps"><img src="https://avatars.githubusercontent.com/u/27200848?v=4?s=100" width="100px;" alt="Maria Knorps"/><br /><sub><b>Maria Knorps</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=mknorps" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Amknorps" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://code.scienxlab.org"><img src="https://avatars.githubusercontent.com/u/1692372?v=4?s=100" width="100px;" alt="Matt Hall"/><br /><sub><b>Matt Hall</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=kwinkunks" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Akwinkunks" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://www.stsci.edu/"><img src="https://avatars.githubusercontent.com/u/503615?v=4?s=100" width="100px;" alt="Megan Sosey"/><br /><sub><b>Megan Sosey</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=sosey" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Asosey" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://melissawm.github.io"><img src="https://avatars.githubusercontent.com/u/3949932?v=4?s=100" width="100px;" alt="Melissa Weber Mendonça"/><br /><sub><b>Melissa Weber Mendonça</b></sub></a><br /><a href="#question-melissawm" title="Answering Questions">💬</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Midnighter"><img src="https://avatars.githubusercontent.com/u/135653?v=4?s=100" width="100px;" alt="Moritz E. Beber"/><br /><sub><b>Moritz E. Beber</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=Midnighter" title="Code">💻</a> <a href="#tutorial-Midnighter" title="Tutorials">✅</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://www.linkedin.com/in/ncclementi/"><img src="https://avatars.githubusercontent.com/u/7526622?v=4?s=100" width="100px;" alt="Naty Clementi"/><br /><sub><b>Naty Clementi</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=ncclementi" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Ancclementi" title="Reviewed Pull Requests">👀</a> <a href="#translation-ncclementi" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://www.software.ac.uk"><img src="https://avatars.githubusercontent.com/u/1507151?v=4?s=100" width="100px;" alt="Neil Chue Hong"/><br /><sub><b>Neil Chue Hong</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Anpch" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://orcid.org/0000-0001-6628-8033"><img src="https://avatars.githubusercontent.com/u/8931994?v=4?s=100" width="100px;" alt="Nick Murphy"/><br /><sub><b>Nick Murphy</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=namurphy" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Anamurphy" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://ofek.dev"><img src="https://avatars.githubusercontent.com/u/9677399?v=4?s=100" width="100px;" alt="Ofek Lev"/><br /><sub><b>Ofek Lev</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=ofek" title="Code">💻</a> <a href="#design-ofek" title="Design">🎨</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Aofek" title="Reviewed Pull Requests">👀</a> <a href="#tutorial-ofek" title="Tutorials">✅</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/yardasol"><img src="https://avatars.githubusercontent.com/u/45364492?v=4?s=100" width="100px;" alt="Olek"/><br /><sub><b>Olek</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=yardasol" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Ayardasol" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://oriolabrilpla.cat"><img src="https://avatars.githubusercontent.com/u/23738400?v=4?s=100" width="100px;" alt="Oriol Abril-Pla"/><br /><sub><b>Oriol Abril-Pla</b></sub></a><br /><a href="#question-OriolAbril" title="Answering Questions">💬</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/tupui"><img src="https://avatars.githubusercontent.com/u/23188539?v=4?s=100" width="100px;" alt="Pamphile Roy"/><br /><sub><b>Pamphile Roy</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=tupui" title="Documentation">📖</a> <a href="#design-tupui" title="Design">🎨</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://www.linkedin.com/pub/pat-tressel/2/b6/610"><img src="https://avatars.githubusercontent.com/u/618916?v=4?s=100" width="100px;" alt="Pat Tressel"/><br /><sub><b>Pat Tressel</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=ptressel" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Aptressel" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/pb-413"><img src="https://avatars.githubusercontent.com/u/36516871?v=4?s=100" width="100px;" alt="Patrick Byers"/><br /><sub><b>Patrick Byers</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=pb-413" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Apb-413" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://phil.red"><img src="https://avatars.githubusercontent.com/u/291575?v=4?s=100" width="100px;" alt="Philipp A."/><br /><sub><b>Philipp A.</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=flying-sheep" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Aflying-sheep" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://pradyunsg.me"><img src="https://avatars.githubusercontent.com/u/3275593?v=4?s=100" width="100px;" alt="Pradyun Gedam"/><br /><sub><b>Pradyun Gedam</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=pradyunsg" title="Code">💻</a> <a href="#design-pradyunsg" title="Design">🎨</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Apradyunsg" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/rgommers/"><img src="https://avatars.githubusercontent.com/u/98330?v=4?s=100" width="100px;" alt="Ralf Gommers"/><br /><sub><b>Ralf Gommers</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=rgommers" title="Code">💻</a> <a href="#design-rgommers" title="Design">🎨</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Argommers" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/radoering"><img src="https://avatars.githubusercontent.com/u/30527984?v=4?s=100" width="100px;" alt="Randy Döring"/><br /><sub><b>Randy Döring</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=radoering" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Aradoering" title="Reviewed Pull Requests">👀</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Revathyvenugopal162"><img src="https://avatars.githubusercontent.com/u/104772255?v=4?s=100" width="100px;" alt="Revathy Venugopal"/><br /><sub><b>Revathy Venugopal</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=Revathyvenugopal162" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3ARevathyvenugopal162" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/pyOpenSci/python-package-guide/commits?author=Revathyvenugopal162" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://robpasmue.github.io"><img src="https://avatars.githubusercontent.com/u/37798125?v=4?s=100" width="100px;" alt="Roberto Pastor Muela"/><br /><sub><b>Roberto Pastor Muela</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=RobPasMue" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3ARobPasMue" title="Reviewed Pull Requests">👀</a> <a href="#translation-RobPasMue" title="Translation">🌍</a> <a href="#ideas-RobPasMue" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ryanskeith"><img src="https://avatars.githubusercontent.com/u/657220?v=4?s=100" width="100px;" alt="Ryan"/><br /><sub><b>Ryan</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=ryanskeith" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Aryanskeith" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://ml-gis-service.com"><img src="https://avatars.githubusercontent.com/u/31246246?v=4?s=100" width="100px;" alt="Simon"/><br /><sub><b>Simon</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=SimonMolinsky" title="Documentation">📖</a> <a href="#design-SimonMolinsky" title="Design">🎨</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/sn3hay"><img src="https://avatars.githubusercontent.com/u/156010030?v=4?s=100" width="100px;" alt="Sneha Yadav"/><br /><sub><b>Sneha Yadav</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=sn3hay" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Asn3hay" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://mentat.za.net"><img src="https://avatars.githubusercontent.com/u/45071?v=4?s=100" width="100px;" alt="Stefan van der Walt"/><br /><sub><b>Stefan van der Walt</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=stefanv" title="Code">💻</a> <a href="#design-stefanv" title="Design">🎨</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Astefanv" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://stefaniemolin.com"><img src="https://avatars.githubusercontent.com/u/24376333?v=4?s=100" width="100px;" alt="Stefanie Molin"/><br /><sub><b>Stefanie Molin</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=stefmolin" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Astefmolin" title="Reviewed Pull Requests">👀</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://stefanorivera.com/"><img src="https://avatars.githubusercontent.com/u/442117?v=4?s=100" width="100px;" alt="Stefano Rivera"/><br /><sub><b>Stefano Rivera</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Astefanor" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/tkoyama010"><img src="https://avatars.githubusercontent.com/u/7513610?v=4?s=100" width="100px;" alt="Tetsuo Koyama"/><br /><sub><b>Tetsuo Koyama</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=tkoyama010" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Atkoyama010" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/pyOpenSci/python-package-guide/commits?author=tkoyama010" title="Documentation">📖</a> <a href="#translation-tkoyama010" title="Translation">🌍</a> <a href="#ideas-tkoyama010" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/tomalrussell"><img src="https://avatars.githubusercontent.com/u/2762769?v=4?s=100" width="100px;" alt="Tom Russell"/><br /><sub><b>Tom Russell</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=tomalrussell" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Atomalrussell" title="Reviewed Pull Requests">👀</a> <a href="#tutorial-tomalrussell" title="Tutorials">✅</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Zeitsperre"><img src="https://avatars.githubusercontent.com/u/10819524?v=4?s=100" width="100px;" alt="Trevor James Smith"/><br /><sub><b>Trevor James Smith</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=Zeitsperre" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3AZeitsperre" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://www.linkedin.com/in/tylerjbonnell/"><img src="https://avatars.githubusercontent.com/u/89505514?v=4?s=100" width="100px;" alt="Tyler Bonnell"/><br /><sub><b>Tyler Bonnell</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=Tyler-Bonnell" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3ATyler-Bonnell" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Vaunty"><img src="https://avatars.githubusercontent.com/u/68826427?v=4?s=100" width="100px;" alt="Vaunty"/><br /><sub><b>Vaunty</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=Vaunty" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3AVaunty" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://orcid.org/0000-0002-8999-9003"><img src="https://avatars.githubusercontent.com/u/6338509?v=4?s=100" width="100px;" alt="William F. Broderick"/><br /><sub><b>William F. Broderick</b></sub></a><br /><a href="#tutorial-billbrod" title="Tutorials">✅</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://www.owlfolio.org/"><img src="https://avatars.githubusercontent.com/u/325899?v=4?s=100" width="100px;" alt="Zack Weinberg"/><br /><sub><b>Zack Weinberg</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Azackw" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/h-vetinari"><img src="https://avatars.githubusercontent.com/u/33685575?v=4?s=100" width="100px;" alt="h-vetinari"/><br /><sub><b>h-vetinari</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=h-vetinari" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Ah-vetinari" title="Reviewed Pull Requests">👀</a> <a href="#tutorial-h-vetinari" title="Tutorials">✅</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/hpodzorski-USGS"><img src="https://avatars.githubusercontent.com/u/159824971?v=4?s=100" width="100px;" alt="hpodzorski-USGS"/><br /><sub><b>hpodzorski-USGS</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=hpodzorski-USGS" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Ahpodzorski-USGS" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/jaimergp"><img src="https://avatars.githubusercontent.com/u/2559438?v=4?s=100" width="100px;" alt="jaimergp"/><br /><sub><b>jaimergp</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=jaimergp" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Ajaimergp" title="Reviewed Pull Requests">👀</a> <a href="#tutorial-jaimergp" title="Tutorials">✅</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/miguelalizo"><img src="https://avatars.githubusercontent.com/u/108839050?v=4?s=100" width="100px;" alt="miguelalizo"/><br /><sub><b>miguelalizo</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=miguelalizo" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Amiguelalizo" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/pyOpenSci/python-package-guide/commits?author=miguelalizo" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/nyeshlur"><img src="https://avatars.githubusercontent.com/u/72169901?v=4?s=100" width="100px;" alt="nyeshlur"/><br /><sub><b>nyeshlur</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=nyeshlur" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Anyeshlur" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/yang-ruoxi"><img src="https://avatars.githubusercontent.com/u/13646711?v=4?s=100" width="100px;" alt="ruoxi"/><br /><sub><b>ruoxi</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=yang-ruoxi" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Ayang-ruoxi" title="Reviewed Pull Requests">👀</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/merwok"><img src="https://avatars.githubusercontent.com/u/635179?v=4?s=100" width="100px;" alt="Éric"/><br /><sub><b>Éric</b></sub></a><br /><a href="https://github.com/pyOpenSci/python-package-guide/commits?author=merwok" title="Code">💻</a> <a href="https://github.com/pyOpenSci/python-package-guide/pulls?q=is%3Apr+reviewed-by%3Amerwok" title="Reviewed Pull Requests">👀</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=pyOpenSci/python-package-guide&type=Date)](https://star-history.com/#pyOpenSci/python-package-guide&Date)
