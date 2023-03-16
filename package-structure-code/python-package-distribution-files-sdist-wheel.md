# The Python Package Source and Wheel Distributions

There are two core distribution files
that you need to create to publish your Python package to
PyPI source distribution (often called an sdist) and wheel. The sdist contains the raw source
code for your package. The Wheel (.whl) contains the built / compiled files
that can be directly installed onto anyones' computer.

Learn more about both distributions below.

```{note}
If your package is a pure python package with no additional
build / compilation steps then the sdist and Wheel distributions will have
similar content. However if your package has extensions in other languages
or is more complex in its build, the two distributions will be very different.

Also note that we are not discussing conda build workflows in this section.
[You can learn more about conda builds here.](https://conda.io/projects/conda-build/en/latest/user-guide/tutorials/index.html)
```

### Source Distribution (sdist)

**Source files** are the unbuilt files needed to build your
package. These are the "raw / as-is" files that you store on GitHub or whatever
platform you use to manage your code.

**S**ource **D**istributions are referred to as sdist. As the name implies, a SDIST contains the source code; it has not been
built or compiled in any way. Thus, when a user installs your source
distribution using pip, pip needs to run a build step first. For this reason, you could define a source distribution as a compressed archive that contains everything required to build a wheel (except for project dependencies) without network access.

Sdist is normally stored as a `.tar.gz` archive (often called a "tarball"). Thus, when a user installs your source distribution using pip, pip needs to run a build step first.

Below is an example sdist for the stravalib Python package:

<!-- TODO: we should likely use a different pure python package with a src/ layout for
consistency -->

```
stravalib-1.1.0.post2-SDist.tar.gz file contents

├─ 📂 stravalib
│  ├─ tests
│  │  ├─ integration
│  │  │  ├─ __init__.py
│  │  │  ├─ conftest.py
│  │  │  ├─ strava_api_stub.py
│  │  │  └─ test_client.py
│  │  ├─ unit
│  │  │  ├─ __init__.py
│  │  │  ├─ test_attributes.py
│  │  │  ├─ ...
│  │  ├─ __init__.py
│  │  ├─ auth_responder.py
│  │  └─ test.ini-example
│  ├─ util
│  │  ├─ __init__.py
│  │  └─ limiter.py
│  ├─ __init__.py
│  ├─ _version.py
│  ├─ _version_generated.py
│  ├─ attributes.py
│  ├─ ...
├─ stravalib.egg-info
│  ├─ PKG-INFO
│  ├─ SOURCES.txt
│  ├─ dependency_links.txt
│  ├─ requires.txt
│  └─ top_level.txt
├─ CODE_OF_CONDUCT.md
├─ CONTRIBUTING.md
├─ LICENSE.txt
├─ MANIFEST.in
├─ Makefile
├─ PKG-INFO
├─ README.md
├─ changelog.md
├─ environment.yml
├─ pyproject.toml
├─ requirements-build.txt
├─ requirements.txt
└─ setup.cfg

```

```{admonition} GitHub archive vs SDist
:class: tip
When you make a release on GitHub, it creates a `git archive` that contains all
of the files in your GitHub repository. While these files are similar to an
SDist, these two archives are not the same. The SDist contains a few other
items including a metadata directory and if you use `setuptools_scm` or `hatch_vcs`
the SDist may also contain a file that stores the version.
```

### Wheel (.whl files):

A wheel file is a ZIP-format archive whose filename follows a specific format
(below) and has the extension `.whl`. The `.whl` archive contains a specific
set of files, including metadata that are generated from your project's
pyproject.toml file. The pyproject.toml and other files that may be included in
source distributions are not included in wheels because it is a built
distribution.

The wheel (.whl) is your built binary distribution. **Binary files** are the built / compiled source files. These files are ready to be installed. A wheel (**.whl**) is a **zip** file containing all of the files needed to directly install your package. All of the files in a wheel are binaries - this means that code is already compiled / built. Wheels are thus faster to install - particularly if you have a package that requires build steps.

The wheel does not contain any of your
packages configuration files such as **setup.cfg** or **pyproject.toml**. This
distribution is already built so it's ready to install.

Because it is built, the wheel file will be faster to install for pure Python
projects and can lead to consistent installs across machines.

<!-- TODO - i need to clarify this as i've gotten mixed feedback on the
real security issues with this IF the whl is already built and that file isn't
included what is the issue? i need more input here-->

```{tip}
Wheels are also useful in the case that a package
needs a **setup.py** file to support a more complex build.
In this case, because the files in the wheel bundle
are pre built, the user installing doesn't have to
worry about malicious code injections when it is installed.
```

The filename of a wheel contains important metadata about your package.

Example: **stravalib-1.1.0.post2-py3-none.whl**

- name: stravalib
- version: 1.1.0
- build-number: 2 (post2) [(read more about post here)](https://peps.python.org/pep-0440/#post-release-separators)
- py3: supports Python 3.x
- none: is not operating system specific (runs on windows, mac, linux)
- any: runs on any computer processor / architecture

What a wheel file looks like when unpacked (unzipped):

```
stravalib-1.1.0.post2-py3-none.whl file contents:

├─ 📂 stravalib
│  ├─ tests
│  │  ├─ functional
│  │  │  ├─ __init__.py
│  │  │  ├─ test_client.py
│  │  ├─ unit
│  │  │  ├─ __init__.py
│  │  │  ├─ test_attributes.py
│  │  ├─ __init__.py
│  │  ├─ auth_responder.py
│  │  └─ test.ini-example
│  ├─ util
│  │  ├─ __init__.py
│  │  └─ limiter.py
│  ├─ __init__.py
│  ├─ _version.py
│  ├─ _version_generated.py
│  ├─ attributes.py
│  ├─ client.py
└─ stravalib-1.1.0.post2.dist-info  # Package metadata are stored here
   ├─ LICENSE.txt
   ├─ METADATA
   ├─ RECORD
   ├─ WHEEL
   └─ top_level.txt

```

```{tip}
[Read more about the wheel format here](https://pythonwheels.com/)
```
