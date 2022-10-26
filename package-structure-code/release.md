(releasing)=
# Releasing a package

This section covers releasing your package to PyPI as well as releasing future versions. Your package should have different versions over time: snapshots of a state of the package that you can release to PyPI for instance. These versions should be properly _numbered_, _released_ and _described in a NEWS file_. More details below.


## Original Release

After the review process has finished, you're ready to release your package to PyPI so others can find and use your awesome package! Releasing to PyPI is easy. Once your package is ready, register it on PyPI by running:

```
python setup.py register
```

## Releasing Updated Versions

When you update your package, you release a new version to PyPI. Fortunately, this is easy! First, we'll talk about the metadata you'll need to update for each version. Then we'll cover how to release your updated version to PyPI [manually via the command line](manual-release) or [automatically via Travis CI](travis-release).

### Version Naming

* We recommend that pyOpenSci packages use [semantic versioning](https://www.python.org/dev/peps/pep-0440/#semantic-versioning). In addition to the [PEP section on it](https://www.python.org/dev/peps/pep-0440/#semantic-versioning), [the semver website has more detail](https://semver.org/).

* Versioning can be done using [bumpversion](https://github.com/peritus/bumpversion), e.g. for a minor update:

```
bumpversion minor
```

"minor" can be replaced with "major" or "patch" depending on the level of update.

(history)=
### History/News/Changelog file

A HISTORY (or NEWS or CHANGELOG) file describing changes associated with each version makes it easier for users to see what's changing in the package and how it might impact their workflow. You must add one for your package, and make it easy to read.

* It is mandatory to use a `HISTORY` file in the root of your package. It can also be called NEWS or CHANGELOG We recommend using `[NAME].md` or `[NAME].rst` to make the file more browsing-friendly on GitHub (GitHub renders certain file types, including Markdown and reStructured text).

* Update the history file before every PyPI release, with a section with the package name, version and date of release.

```
foobar 0.2.0 (2016-04-01)
=========================
```

* Under that header, put in sections as needed, including: `NEW FEATURES`, `MINOR IMPROVEMENTS`, `BUG FIXES`, `DEPRECATED AND DEFUNCT`, `DOCUMENTATION FIXES` and any special heading grouping a large number of changes. Under each header, list items as needed. For each item give a description of the new feature, improvement, bug fix, or deprecated function/feature. Link to any related GitHub issue like `(#12)`. The `(#12)` will resolve on GitHub in Releases to a link to that issue in the repo.

* After you have added a `git tag` and pushed up to GitHub, add the news items for that tagged version to the Release notes of a release in your GitHub repo with a title like `pkgname v0.1.0`. See [GitHub docs about creating a release](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository).

(manual-release)=
### Releasing Versions: Manual

To manually upload a new package version to PyPI, follow these steps:

1. Update your HISTORY file as described [above](#history)
2. Open `setup.py` and change the version, e.g., version='1.0.3'
3. If you added new, non-Python files to the project that need to be distributed as well, e.g., configuration files, add them to `MANIFEST.in`. This does not need to be done for Python code files ending in .py.
4. Open a terminal and go into the parent of the project's root dir
5. `python setup.py sdist`
6. Check the resulting files, especially the egg file: are all the files contained?
7. If everything is ok, upload the new version to PyPI: `python setup.py sdist upload`

That's it!

(travis-release)=
### Releasing via Travis CI
Instead of manually uploading new package versions, Travis can be configured to automatically upload new versions. If you use this, each time you tag a new release and push it to GitHub, Travis will release it to PyPI (assuming it passes testing).

* The pyOpenSci cookiecutter comes with this option mostly set up. For details on how to finish the set up, see [this guide](https://cookiecutter-pyopensci.readthedocs.io/en/latest/travis_pypi_setup.html).

* Also, be sure to check out this [PyPI release checklist](https://cookiecutter-pyopensci.readthedocs.io/en/latest/pypi_release_checklist.html).

