# Changelog.md Guide

## Introduction

The `changelog.md` document serves as a valuable resource for developers and users alike to track the evolution of a project over time. Understanding the structure and purpose of a changelog helps users and contributors stay informed about new features, bug fixes, and other changes introduced in each release.

## What is changelog.md?

`changelog.md` is a file commonly found in Python packages. Its primary purpose is to provide a chronological record of significant changes made to the project with each new release. This document helps users understand what has been added, fixed, or modified in the latest version of the software. In addition, it allows the contributors and users to understand the versioning syntax used for the package.

[Keep a Changelog.md](https://keepachangelog.com/en/1.1.0/) is great, simple resource for understanding what a changelog is, how to create a good changelog, and includes some pointers of things to avoid in a changelog. 

```{admonition} Semantic Versioning
:class: tip

An important component of a package that serves as the backbone behind the changelog file is a good versioning scheme. Semantic Versioning is widely used across Python packages.
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

## What does it look like?

```markdown
# Change Log
All notable changes to this project will be documented in this file.
 
The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).
 
## [Unreleased] - yyyy-mm-dd
 
Here we write upgrading notes for brands. It's a team effort to make them as
straightforward as possible.
 
### Added
- [PROJECTNAME-XXXX](http://tickets.projectname.com/browse/PROJECTNAME-XXXX)
  MINOR Ticket title goes here.
- [PROJECTNAME-YYYY](http://tickets.projectname.com/browse/PROJECTNAME-YYYY)
  PATCH Ticket title goes here.
 
### Changed
 
### Fixed
 
## [1.2.4] - 2017-03-15
  
Here we would have the update steps for 1.2.4 for people to follow.
 
### Added
 
### Changed
  
- [PROJECTNAME-ZZZZ](http://tickets.projectname.com/browse/PROJECTNAME-ZZZZ)
  PATCH Drupal.org is now used for composer.
 
### Fixed
 
- [PROJECTNAME-TTTT](http://tickets.projectname.com/browse/PROJECTNAME-TTTT)
  PATCH Add logic to runsheet teaser delete to delete corresponding
  schedule cards.
 
## [1.2.3] - 2017-03-14
 
### Added
   
### Changed
 
### Fixed
 
- [PROJECTNAME-UUUU](http://tickets.projectname.com/browse/PROJECTNAME-UUUU)
  MINOR Fix module foo tests
- [PROJECTNAME-RRRR](http://tickets.projectname.com/browse/PROJECTNAME-RRRR)
  MAJOR Module foo's timeline uses the browser timezone for date resolution 
```
[Sample changelog source](https://gist.github.com/juampynr/4c18214a8eb554084e21d6e288a18a2c)