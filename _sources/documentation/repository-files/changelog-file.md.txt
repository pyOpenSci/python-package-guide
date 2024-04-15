# CHANGELOG.md Guide

## Introduction

The `CHANGELOG.md` document serves as a valuable resource for developers and users alike to track the evolution of a project over time. Understanding the structure and purpose of a changelog helps users and contributors stay informed about new features, bug fixes, and other changes introduced in each release.

## What is CHANGELOG.md?

The primary purpose of `CHANGELOG.md` is to provide a record of notable changes made to the project with each new release. This document helps users understand what has been added, fixed, modified, or removed with each version of the software.

[Keep a CHAGELOG.md](https://keepachangelog.com/en/1.1.0/) is a great, simple resource for understanding what a changelog is and how to create a good changelog. It also includes examples of things to avoid.

```{admonition} Versioning your Python package and semantic versioning
:class: tip

An important component of a package that serves as the backbone behind the changelog file is a good versioning scheme. Semantic Versioning is widely used across Python packages.
* [Creating New Versions of Your Python Package](../../package-structure-code/python-package-versions.md)
* [Semantic Versioning](https://semver.org)
```

## Why is it important?

A well-maintained changelog is essential for transparent communication with users and developers. It serves as a centralized hub for documenting changes and highlights the progress made in each release. By keeping the changelog up-to-date, project maintainers can build trust with their user base and demonstrate their commitment to improving the software.

## What does it include?

The contents of a changelog.md file typically follow a structured format, detailing the changes introduced in each release. While the exact format may vary depending on the project's conventions, some common elements found in changelogs for Python packages include:

- **Versioning**: Clear identification of each release version using semantic versioning or another versioning scheme adopted by the project.

- **Release Date**: The date when each version was released to the public, providing context for the timeline of changes.

- **Change Categories**: Organizing changes into categories such as "Added," "Changed," "Fixed," and "Removed" to facilitate navigation and understanding.

- **Description of Changes**: A concise description of the changes made in each category, including new features, enhancements, bug fixes, and deprecated functionality.

- **Links to Issues or Pull Requests**: References to relevant issue tracker items or pull requests associated with each change, enabling users to access more detailed information if needed.

- **Upgrade Instructions**: Guidance for users on how to upgrade to the latest version, including any breaking changes or migration steps they need to be aware of.

- **Contributor Recognition**: Acknowledgment of contributors who made significant contributions to the release, fostering a sense of community and appreciation for their efforts.

## How do maintainers use it?

Often you will see a changelog that documents a few things:

### Unreleased Section

Unreleased commits are at the top of the changelog, commonly in an `Unreleased` section. This is where you can add new fixes, updates and features that have been added to the package since the last release.

This section might look something like this:

```markdown
## Unreleased
* Fix: Fixed a bug.... more here. (@github_username, #issuenumber)
* Add: new feature to... more here. (@github_username, #issuenumber)
```

### Release Sections

When you are ready to make a new release, you can move the elements into a section that is specific to that new release number.

This specific release section will sit below the unreleased section and can include any updates, additions, deprecations and contributors.

The unreleased section then always lives at the top of the file and new features continue to be added there. At the same time, after releasing a version like v1.0 all of its features remain in that specific section.

```markdown
## Unreleased

## v1.0

### Updates
* Fix: Fixed a bug.... more here. (@github_username, #issuenumber)

### Additions
* Add: new feature to ...more here (@github_username, #issuenumber)

### Deprecations

### Contributors to this release
```

## What does it look like?

This example comes from [Devicely](https://github.com/hpi-dhc/devicely/blob/main/CHANGELOG.md), a pyOpenSci accepted package.

```markdown
# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] - 2021-08-24
- removed acceleration magnitude from devicely.EmpaticaReader and devicely.FarosReader since it was out of the scope of the package
- added more flexibility to missing files (e.g. ACC.csv, EDA.csv) to devicely.EmpaticaReader
- changed TagsReader to TimeStampReader to be more consistent with the class naming structure in devicely
- deprecated methods in devicely.SpacelabsReader: set_window and drop_EB
- fixed issue with the timestamp index and fixed column names in devicely.SpacelabsReader

## [1.0.0] - 2021-07-19
### Added
- devicely.FarosReader can both read from and write to EDF files and directories
- devicely.FarosReader has as attributes the individual dataframes (ACC, ECG, ...) and not only the joined dataframe

### Changed
- in devicely.SpacelabsReader, use xml.etree from the standard library instead of third-party "xmltodict"
- switch from setuptools to Poetry

### Removed
- removed setup.py because static project files such as pyproject.toml are preferred
```
