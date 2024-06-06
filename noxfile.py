import os
import pathlib
import shutil
import nox

nox.options.reuse_existing_virtualenvs = True

## Sphinx related options

# Sphinx output and source directories
OUTPUT_DIR = pathlib.Path("_build", "html")
SOURCE_DIR = pathlib.Path(".")

# Sphinx build commands
SPHINX_BUILD = "sphinx-build"
SPHINX_AUTO_BUILD = "sphinx-autobuild"

# Sphinx parameters used to build the guide
BUILD_PARAMETERS = ["-b", "html"]

# Sphinx parameters used to test the build of the guide
TEST_PARAMETERS = ['-W', '--keep-going', '-E', '-a']

# Sphinx-autobuild ignore and include parameters
AUTOBUILD_IGNORE = [
    "_build",
    "build_assets",
    "tmp",
]
AUTOBUILD_INCLUDE = [
    pathlib.Path("_static", "pyos.css")
]

@nox.session
def docs(session):
    """Build the packaging guide."""
    session.install("-e", ".")
    cmd = [SPHINX_BUILD, *BUILD_PARAMETERS, SOURCE_DIR, OUTPUT_DIR, *session.posargs]
    session.run(*cmd)

@nox.session(name="docs-test")
def docs_test(session):
    """Build the packaging guide with additional parameters."""
    session.install("-e", ".")
    cmd = [SPHINX_BUILD, *BUILD_PARAMETERS, *TEST_PARAMETERS, SOURCE_DIR, OUTPUT_DIR, *session.posargs]
    session.run(*cmd)

@nox.session(name="docs-live")
def docs_live(session):
    """Build and launch a local copy of the guide."""
    session.install("-e", ".")
    cmd = [SPHINX_AUTO_BUILD, *BUILD_PARAMETERS, SOURCE_DIR, OUTPUT_DIR, *session.posargs]
    for folder in AUTOBUILD_IGNORE:
        cmd.extend(["--ignore", f"*/{folder}/*"])
    session.run(*cmd)

@nox.session(name="docs-clean")
def clean_dir(session):
    """Clean out the docs directory used in the live build."""
    session.warn(f"Cleaning out {OUTPUT_DIR}")
    dir_contents = OUTPUT_DIR.glob('*')
    for content in dir_contents:
        session.log(f'removing {content}')
        if content.is_dir():
            shutil.rmtree(content)
        else:
            os.remove(content)
