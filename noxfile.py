import os
import pathlib
import shutil
import nox


## Sphinx related options

# Sphinx output and source directories
BUILD_DIR = '_build'
OUTPUT_DIR = pathlib.Path(BUILD_DIR, "html")
SOURCE_DIR = pathlib.Path(".")

# Location of the translation templates
TRANSLATION_TEMPLATE_DIR = pathlib.Path(BUILD_DIR, "gettext")
TRANSLATION_LOCALES_DIR = pathlib.Path("locales")

# Sphinx build commands
SPHINX_BUILD = "sphinx-build"
SPHINX_AUTO_BUILD = "sphinx-autobuild"

# Sphinx parameters used to build the guide
BUILD_PARAMETERS = ["-b", "html"]

# Sphinx parameters used to test the build of the guide
TEST_PARAMETERS = ['-W', '--keep-going', '-E', '-a']

# Sphinx parameters to generate translation templates
TRANSLATION_TEMPLATE_PARAMETERS = ["-b", "gettext"]

# Sphinx-autobuild ignore and include parameters
AUTOBUILD_IGNORE = [
    "_build",
    ".nox",
    "build_assets",
    "tmp",
]
AUTOBUILD_INCLUDE = [
    pathlib.Path("_static", "pyos.css")
]

## Localization options (translations)

# List of languages for which locales will be generated in (/locales/<lang>)
LANGUAGES = ["es", "ja"]

# List of languages that should be built when releasing the guide (docs or docs-test sessions)
RELEASE_LANGUAGES = []


@nox.session
def docs(session):
    """Build the packaging guide."""
    session.install("-e", ".")
    session.run(SPHINX_BUILD, *BUILD_PARAMETERS, SOURCE_DIR, OUTPUT_DIR, *session.posargs)
    # When building the guide, also build the translations in RELEASE_LANGUAGES
    session.notify("build-release-languages", session.posargs)

EXCLUDE_LINKS = [
    "https://github.com"
    "https://*.github.com"
]

@nox.session(name="docs-test")
def docs_test(session):
    """
    Build the packaging guide with more restricted parameters.

    Note: this is the session used in CI/CD to release the guide.
    """
    session.install("-e", ".")
    session.run(SPHINX_BUILD, *BUILD_PARAMETERS, *TEST_PARAMETERS, SOURCE_DIR, OUTPUT_DIR, *session.posargs)
    # Exclude GitHub links from link checker.
    for link in EXCLUDE_LINKS:
        session.run("linkchecker", "--ignore-url", link)
    # When building the guide with additional parameters, also build the translations in RELEASE_LANGUAGES
    # with those same parameters.
    session.notify("build-release-languages", [*TEST_PARAMETERS, *session.posargs])


@nox.session(name="docs-live")
def docs_live(session):
    """
    Build and launch a local copy of the guide.

    This session will use sphinx-autobuild to build the guide and launch a local server so you can
    browse it locally. It will automatically rebuild the guide when changes are detected in the source.

    It can be used with the language parameter to build a specific translation, for example:

        nox -s docs-live -- -D language=es

    Note: The docs-live-lang session below is provided as a convenience session for beginner contributors
    so they don't need to remember the specific sphinx-build parameters to build a different language.
    """
    session.install("-e", ".")
    cmd = [SPHINX_AUTO_BUILD, *BUILD_PARAMETERS, SOURCE_DIR, OUTPUT_DIR, *session.posargs]
    for folder in AUTOBUILD_IGNORE:
        cmd.extend(["--ignore", f"*/{folder}/*"])
    # This part was commented in the previous version of the nox file, keeping the same here
    # for folder in AUTOBUILD_INCLUDE:
    #     cmd.extend(["--watch", folder])
    session.run(*cmd)


@nox.session(name="docs-live-lang")
def docs_live_lang(session):
    """
    A convenience session for beginner contributors to use the docs-live session with
    a specific language.

    It expects the language code to be passed as the first positional argument, so it needs
    to be called with from the command line with the following syntax:

        nox -s docs-live-lang -- LANG

    where LANG is one of the available languages defined in LANGUAGES.
    For example, for Spanish: nox -s docs-live-lang -- es
    """
    if not session.posargs:
        session.error(
            "Please provide a language using:\n\n      "
            "nox -s docs-live-lang -- LANG\n\n     "
            f" where LANG is one of: {LANGUAGES}"
        )
    lang = session.posargs[0]
    if lang in LANGUAGES:
        session.posargs.pop(0)
        session.notify("docs-live", ('-D', f"language={lang}", *session.posargs))
    else:
        session.error(
            f"[{lang}] locale is not available. Try using:\n\n      "
            "nox -s docs-live-lang -- LANG\n\n      "
            f"where LANG is one of: {LANGUAGES}"
        )


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
            pathlib.Path(content).unlink()


@nox.session(name="update-release-languages")
def update_release_languages(session):
    """
    Update the translation files (./locales/*/.po) for languages in RELEASE_LANGUAGES.

    Note: this step is called in the CI to keep release translations up to date with
    the latest changes in the guide.
    """
    if RELEASE_LANGUAGES:
        session.install("-e", ".")
        session.install("sphinx-intl")
        session.log("Updating templates (.pot)")
        session.run(SPHINX_BUILD, *TRANSLATION_TEMPLATE_PARAMETERS, SOURCE_DIR, TRANSLATION_TEMPLATE_DIR, *session.posargs)
        for lang in RELEASE_LANGUAGES:
            session.log(f"Updating .po files for [{lang}] translation")
            session.run("sphinx-intl", "update", "-p", TRANSLATION_TEMPLATE_DIR, "-l", lang)
    else:
        session.warn("No release languages defined in RELEASE_LANGUAGES")


@nox.session(name="update-language")
def update_language(session):
    """
    Update the translation files (./locales/*/.po) for a specific language translation.

    Note: this step is used by language coordinators to keep their translation files up to date
    with the latest changes in the guide, before the translation is released.
    """
    if session.posargs and (lang := session.posargs.pop(0)):
        if lang in LANGUAGES:
            session.install("-e", ".")
            session.install("sphinx-intl")
            session.log("Updating templates (.pot)")
            session.run(SPHINX_BUILD, *TRANSLATION_TEMPLATE_PARAMETERS, SOURCE_DIR, TRANSLATION_TEMPLATE_DIR, *session.posargs)
            session.log(f"Updating .po files for [{lang}] translation")
            session.run("sphinx-intl", "update", "-p", TRANSLATION_TEMPLATE_DIR, "-l", lang)
        else:
            f"[{lang}] locale is not available. Try using:\n\n      "
            "nox -s docs-live-lang -- LANG\n\n      "
            f"where LANG is one of: {LANGUAGES}"
    else:
        session.error(
            "Please provide a language using:\n\n      "
            "nox -s update-language -- LANG\n\n     "
            f" where LANG is one of: {LANGUAGES}"
        )

@nox.session(name="build-language")
def build_language(session):
    """
    Build the guide for a specific language translation

    For example: nox -s build-language -- es.
    """
    if session.posargs and (lang := session.posargs.pop(0)):
        if lang in LANGUAGES:
            session.install("-e", ".")
            session.log(f"Building [{lang}] guide")
            session.run(SPHINX_BUILD, *BUILD_PARAMETERS, "-D", f"language={lang}", ".", OUTPUT_DIR / lang, *session.posargs)
        else:
            session.error(f"Language {lang} is not in LANGUAGES list.")
    else:
        session.error(
            "Please provide a language using:\n\n      "
            "nox -s build-language -- LANG\n\n     "
            f" where LANG is one of: {LANGUAGES}"
        )


@nox.session(name="build-release-languages")
def build_release_languages(session):
    """
    Build the translations of the guide for the languages in RELEASE_LANGUAGES.
    """
    if not RELEASE_LANGUAGES:
        session.warn("No release languages defined in RELEASE_LANGUAGES")
        return
    session.install("-e", ".")
    for lang in RELEASE_LANGUAGES:
        session.log(f"Building [{lang}] guide")
        session.run(SPHINX_BUILD, *BUILD_PARAMETERS, "-D", f"language={lang}", ".", OUTPUT_DIR / lang, *session.posargs)
    session.log(f"Translations built for {RELEASE_LANGUAGES}")

@nox.session(name="build-all-languages")
def build_all_languages(session):
    """
    Build the translations of the guide for the languages in LANGUAGES.
    """
    if not LANGUAGES:
        session.warn("No languages defined in LANGUAGES")
        return
    session.install("-e", ".")
    for lang in LANGUAGES:
        session.log(f"Building [{lang}] guide")
        session.run(SPHINX_BUILD, *BUILD_PARAMETERS, "-D", f"language={lang}", ".", OUTPUT_DIR / lang, *session.posargs)
    session.log(f"Translations built for {LANGUAGES}")


@nox.session(name="build-all-languages-test")
def build_all_languages_test(session):
    """
    Build all translations of the guide with the testing parameters.

    This is a convenience session to test the build of all translations with the testing parameters
    in the same way docs-test does for the English version.
    """
    session.notify("build-all-languages", [*TEST_PARAMETERS])
