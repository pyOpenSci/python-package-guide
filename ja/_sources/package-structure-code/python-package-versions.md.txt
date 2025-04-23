# Creating New Versions of Your Python Package

<!-- * mention release should be incremental
* rep changes in the code that are either patches, minor fixes, major updates -->

```{admonition} Key Takeways

* Follow [semantic versioning guidelines (SemVer) rules](https://semver.org/) when bumping (increasing) your Python's package version; for example a major version bump (version 1.0 --> 2.0) equates to breaking changes in your package's code for a user.
* You may want to consider using a plugin like hatch_vsc for managing versions of your package - if you want to have a GitHub only release workflow.
* Otherwise most major package build tools such as Hatch, Flit and PDM have a version feature that will help you update your package's version
* Avoid updating your packages version number manually by hand in your code!
```

pyOpenSci recommends that you follow the [Python PEP 440](https://peps.python.org/pep-0440) which recommends using
[semantic versioning guidelines](https://www.python.org/dev/peps/pep-0440/#semantic-versioning)
when assigning release values to new versions of your Python package.

[Semantic versioning](https://semver.org/) is an approach
to updating package versions that considers the type and extent of a
change that you are making to the package code. Being consistent
with how and when you update your package versions is important as:

1. It helps your users (which might include other developers that depend on your package) understand the extent of changes to a package.
2. It helps your development team make decisions about when to
   bump a package version based on standard rules.
3. Consistent version increases following semver rules mean that values of your package version explain the extent of the changes made in the code base from version to version. Thus your package version numbers become "expressive" in the same way that naming code variables well can [make code expressive](https://medium.com/@daniel.oliver.king/writing-expressive-code-b69ef7a5a2fa).

```{admonition} A note about versioning
In some cases even small version changes can turn a package update
into a breaking change for some users. What is also important is that
you document how you version your code and if you can, also
document your deprecation policy for code.
```

<!-- TODO: Better link to what expressive code is?-->

## SemVer rules

Following SemVer, your bump your package version to a:

- patch (1.1.1 --> 1.1.**2**)
- minor (1.1.1 --> 1.**2**.1)
- major (1.1.1 --> **2**.1.1)

version number change based on the following rules:

> Given a version number MAJOR.MINOR.PATCH, increment the:
>
> - **MAJOR version** when you make incompatible API changes
> - **MINOR version** when you add functionality in a backwards compatible manner
> - **PATCH version** when you make backwards compatible bug fixes
>   Additional labels for pre-release and build metadata are
>   available as extensions to the MAJOR.MINOR.PATCH format.

```{note}
Some people prefer to use [calver](https://calver.org/index.html) for versioning. It may be a simpler-to-use system given it relies upon date values associated with released versions. However, calver does not provide a user with a sense of when a new version
might break an existing build. As such we still suggest semver.

pyOpenSci will never require semver in a peer review as long as a
package has a reasonable approach to versioning!
```

## Avoid manually updating Python package version numbers if you can

Often times you may want to have your package version value in
multiple locations. One example of this is that it might be both
an attribute in your package **version** and also called
in your documentation.

We recommend that you avoid manual updates of your package version
number to avoid human-error. It is better
practice to keep your version number in one location.

If you can't implement a single location version, then consider
using a tool like hatch, PDM or bump2version that will update
the version values for you - throughout your package.

Below we discuss some tools that you can use to manage updating
Python package versions.

<!-- bump2version isn't really maintained anymore - are there alternatives? -->

## Tools to manage versions for your Python package

There are a handful of tools that are widely used in the scientific ecosystem that you can use to manage your package
versions. Some of these tools are built into or work with your chosen
[packaging build tools that discussed in this chapter.](python-package-build-tools)

<!-- TODO: ADD LINK when other pr merged -->

Below, we provide an overview of these tools.

<!--
If you are on the fence about what tool to use, we suggest
that you use `setuptools-scm`. Thinking now PDM or hatch + hatch_vcs  -->

There are three general groups of tools that you can use to manage
package versions:

1. **semantic release tools:** These tools will automagically determine what type of version bump to use using the text in your commit messages. Below we discuss [Python Semantic Release](https://python-semantic-release.readthedocs.io/en/latest/) as a Python tool
   that implements a semantic versioning approach.
1. **Manual incremental bump tools:** Tools like [Hatch](https://hatch.pypa.io/latest/version/) offer version bumping within your package. Normally this is implemented at the command link for instance `hatch version major` would bump your project from 0.x to 1.0.
1. **Version Control System tools:** Finally there are tools that rely on your version control system to track versions. These tools often are plugins to your package build tool (ex: setuptools build or hatchling). We discuss this option below assuming that you are using **.git tags** and **GitHub** to manage your package repository.

### Semantic release, vs version control based vs manual version bumping

Generally semantic release and version control system tools
can be setup to run automatically on GitHub using GitHub Actions.
This means that you can create a workflow where a GitHub release
and associated new version tag is used to trigger an automated
build that:

1. Builds your package and updates the version following the new tag
1. Tests the build and publishes to test PyPI
1. Publishes the package to PyPI

```{note}
Bumping a package version refers to the step of increasing the package
version after a set number of changes have been made to it. For example,
you might bump from version 0.8 to 0.9 of a package or from 0.9 to 1.0.

Using semantic versioning, there are three main "levels"
of versions that you might consider:

Major, minor and patch. These are described in more detail below.
```

## Tools for bumping Python package versions

In this section we discuss the following tools for managing
your Python package's version:

- hatch &
- hatch_vcs plugin for hatchling
- setuptools-scm
- python-semantic-version

### Tool 1: Hatch and other build tools that offer incremental versioning

Many of the modern build tool front end tools offer version support
that follow semantic versioning rules. These tools are different
from Python Semantic Version in that they do not require specific
commit messages to implement version. Rather, they allow you
to update the version at the command line using commands such as:

- `tool-name version update major`
- `tool-name version update minor`

[Hatch](https://hatch.pypa.io/latest/version/), for instance offers `hatch version minor` which will modify
the version of your package incrementally. With **Hatch** the version value will be found in your `pyproject.toml` file. <!-- TODO double check this -->

#### Hatch (or other tools like PDM) Pros

- Easy to use version updates locally using a single tool!

#### Hatch (or other tools like PDM) Cons

- There will be some setup involved to ensure package version is updated throughout your package

### Tool 2: Hatch_vcs & hatchling build back-end

[hatch_vcs](https://github.com/ofek/hatch-vcs) is a versioning tool
that allows you to manage package versions using **git tags**.
Hatch_vcs creates a **\_version.py** file in your package ecosystem that
keeps track of the package's current version.

Hatch keeps track of your package's version in a `_version.py` file. Storing the
version in a single file managed by Hatch provides
your package with a "single source of truth" value for the version
number. This in turn eliminates potential error associated with
manually updating your package's version.

When you (or your CI system) build your package, hatch checks the current tag number for your package. If it has increased, it will update
the **\_version.py** file with the new value.

Thus, when you create a new tag or a new release with a tag and build your package, Hatch will access the new tag value and use it to update
your package version.

To use **hatch_vcs** you will need to use the **hatchling** build back end.

```{tip}
Hatchling can also be used with any of the modern build tools
including **Flit** and **PDM** if you prefer those for your day to
day workflow.
```

#### Hatch example setup in your pyproject.toml

```toml
# pyproject.toml example build setup to use hatchling and hatch_vcs
[build-system]
requires = ["hatchling", "hatch-vcs"]
build-backend = "hatchling.build"
```

**Hatch_vcs** supports a fully automated package release and build, and
push to PyPI workflow on GitHub.

```toml
# Example hatch vcs setup in the pyproject.toml file
[tool.hatch.build.hooks.vcs]
version-file = "_version.py"
```

```{tip}
If you use **setuptools_scm**, then you might find **hatch_vcs** and **hatchling** to be the modern equivalent to your current setuptools / build workflow.
```

#### hatch_vcs Pros

- Hatch supports modern Python packaging standards
- It creates a single-source file that contains your package version.
- You never manually update the package version
- You can automate writing the version anywhere in your package including your documentation!
- It supports a purely GitHub based release workflow. This simplifies maintenance workflows.
- Version number is updated in your package via a hidden `_version.py` file. There is no manual configuration updates required.
- While we like detailed commit messages (See Python Semantic Version below), we know that sometimes when maintaining a package specific guidelines around commit messages can be hard to apply and manage.

#### hatch_vcs Cons

- In a CI workflow you will end up manually entering or creating the version number via a tag on GitHub. But you could locally develop a build to "bump" tag
  versions

### Tool 3: setuptools-scm versioning using git tags

[`Setuptools_scm`](https://github.com/pypa/setuptools_scm/) is an
extension that you can use with setuptools to manage package
versions. **Setuptools_scm** operates the same way that
**hatch_vcs** (discussed above) does. It stores a version in a **\_version.py** file and relies on (**git**) tags to
determine the package's current version.

If you are using **setuptools** as your primary build tool, then `*setuptools-scm` is a good choice as:

<!-- Are the pros and cons useful? -->

setuptools_scm Pros

- It creates a single-source file that contains your package version.
- You never manually update the package version
- You can automate writing the version anywhere in your package including your documentation!
- It supports a purely GitHub based release workflow. This simplifies maintenance workflows.
- Version number is updated in your package via a hidden `_version.py` file. There is no manual configuration updates required.
- While we like detailed commit messages (See Python Semantic Version below), we know that sometimes when maintaining a package specific guidelines around commit messages can be hard to apply and manage.
- **setuptools** is still the most commonly used Python packaging build tool

#### setuptools_scm Cons

- In a CI workflow you will end up manually entering or creating the version number via a tag on GitHub.
- Not well documented
- Because setuptools will always have to support backwards compatibility it will always be slower in adopting modern Python packaging conventions.

As such you might consider using a more modern tool such as
**hatch_vcs** and **hatchling** to build your package and manage
package versions.

<!--
```{important}
pyOpenSci will be creating tutorials on working with `setuptools-scm` and GitHub releases to
update versions of your package and push to PyPI. These should be published sometime
during the spring/summer 2023. In the meantime [here is a high quality blog post
that will help you get started with using setuptools-scm](https://www.moritzkoerber.com/posts/versioning-with-setuptools_scm/)
``` -->

### Tool 4: [Python semantic release](https://python-semantic-release.readthedocs.io/en/latest/)

Python semantic release uses a commit message workflow that updates
the version of your package based on keywords found in your commit
messages. As the name implies, Python Semantic Release follows
semver release rules.

With Python Semantic Release, versions are triggered using
specific language found in a git commit message.

For example, the words `fix(attribute_warning):` trigger Python
Semantic Release to implement a **patch** version bump.
For instance if your package was at version 1.1.0 and you
made the commit below with the words fix(text-here), Python Semantic
Release would bump your package to version 1.1.1.

```bash
$ git commit -m "fix(mod_plotting): fix warnings returned athlete attributes"
```

Similarly a feature (`feat()`) triggers a minor version bump.
For example from version 1.1 to version 1.2

```bash
git commit -m "feature(add_conversions): add value conversions to activity date"
```

```{tip}
You can find a thoughtful discussion of python semantic version [in this Python package guide](https://py-pkgs.org/07-releasing-versioning#automatic-version-bumping). Note that the guide hasn't been updated since 2020 and will potentially be updated in the future! But for now, some of the commands are dated but the content is still excellent.
```

#### Python Semantic Release Pros

- Follows semver versioning closely
- Enforces maintainers using descriptive commit messages which can simplify troubleshooting and ensure a cleaner and more self-describing git history.

#### Python Semantic Release Cons

- Requires very specific commit language to work. In practice some maintainers and contributors may not be able to maintain that level of specificity in commit messages (NOTE: there are bots that will check git commit messages in a repo)
- Release happens at the command line. This makes is harder to implement a GitHub based release workflow as the wrong commit message could trigger a release.
- The version number is manually updated in a configuration file such as `pyproject.toml` vs. in a package **\_version.py** file.

<!-- However, this tool differs
from **setuptools-scm**. With **setuptools-scm**, a version
control tag, is used to trigger a version update.  -->
