(pyos-development-guide)=
# What the development guide for your Python package should contain

Ideally, your package should also have a development guide. This file may live in your package documentation and should be linked to from your CONTRIBUTING.md file (discussed above).
A development guide should clearly show
technically proficient users how to:

* Set up a development environment locally to work on your package
* Run the test suite
* Build documentation locally

The development guide should also have guidelines for:

* code standards including docstring style, code format and any specific code approaches that the package follows.

It's also helpful to specify the types of tests you request if a contributor submits a new feature or a change to an existing feature that will not be covered by your existing test suite.

If you have time to document it, it's also helpful to document your maintainer workflow and release processes.

## Why a development guide is important

It's valuable to have a development guide, in the
case that you wish to:

* Onboard new maintainers.
* Allow technically inclined contributors to make thoughtful and useful code based pull requests to your repository.

It also is important to pyOpenSci that the maintenance workflow is
documented in the case that we need to help you onboard new
maintainers in the future.

```{note}
A well thought out continuous integration setup in your repository
can allow users to skip building the package locally (especially if they are just updating text).
```

```{tip}
A development guide, while strongly recommended, is not a file that
pyOpenSci requires a package to have in order to be eligible for
review. Some maintainers may also opt to include the development information in their contributing guide.
```

```{tip}
[The Mozilla Science Lab website has a nice outline of things to consider when
creating a contributing guide](https://mozillascience.github.io/working-open-workshop/contributing/)
```

<!--
pyOpenSci packages must:

- Contain full documentation for any user-facing functions.
- Have a test suite that covers the major functionality of the package.
- Use continuous integration.
- Use an OSI approved software license.

**Good/Better/Best:**
- **Good:** Include a open source software license with your package.
- **Better/Best:** Choose a license based on your needs and future use of package, plus explain your choice in your submission for review. -->
