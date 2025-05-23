---
orphan: true
---

# Translation Guide for the Python Packaging Guide

This guide will help you get started contributing to the translation of the Python Packaging Guide.

The process of contributing to the translation of the guide is similar to the process of contributing to the guide itself, except that instead of working on the guide source files directly, you will be working on the translation files.

# Translation Status

```{translation-graph}
```

## Overview of the Translation Process

The process of adapting software to different languages is called internationalization, or i18n for short. Internationalization makes sure that translation can happen without having to modify the source code, or in our case, the original English source files of the guide.

Sphinx, the documentation engine we use to build the Python Package Guide, has built-in support for internationalization, so the workflow is very straightforward.

The process of actually translating the guide into different languages is called localization, or l10n for short. This is the step you will be helping with your contribution.

Here is a quick overview of how the translation process works:

1. The guide is originally written in English and stored in a set of MarkDown files.
2. The source files are processed by Sphinx to generate a set of translation files stored in a folder for each target language.
3. Contributors (like you!) translate these files into the different languages.
4. When the guide is built, Sphinx creates a version of the guide in the original language (English) and the translated versions for the languages defined in the configuration.

```{note}
You don't need to understand the technical details to contribute, but if you are interested in learning how Sphinx handles internationalization and localization, you can find more information [here](https://www.sphinx-doc.org/en/master/usage/advanced/intl.html).
```

## Setting up Your Local Environment

Before you start, you will need to set up your local work environment.

First, fork the guide repository into your personal GitHub account and clone the forked repository to your local computer.

To create a virtual environment and install the development dependencies for the guide, run the following commands:

```shell
$ cd ./python-package-guide
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install .[dev]
```

TODO: This section needs more work or to be replaced with a reference to the CONTRIBUTING guide.

## Starting a New Language Translation

If you plan to work on an existing translation, you can skip this step and go directly to the next section.

```{admonition} Important
If you would like to start the translation of the guide into a new language, start by [creating an issue](https://github.com/pyOpenSci/python-package-guide/issues) in the repository.
```

To generate the translation files for a new language, add the language to the `LANGUAGES` list in the `noxfile.py` configuration file. [Nox](https://nox.thea.codes/en/stable/index.html) is the tool we use to manage the building of the guide and its translations.

Inside `noxfile.py`, find the `LANGUAGES` list and add the corresponding two-letter code. For example, if you want to start the translation of the guide into French, you would add `'fr'`:

```python
## Localization options (translations)

# List of languages for which locales will be generated in (/locales/<lang>)
LANGUAGES = ["es", "fr"]

```

```{note}
You can find a list of the two-letter Sphinx language option [here](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language).
```

## Preparing the Translation Files

The translation files contain the original English text and a space for you to enter the translated text. Before starting to translate, you need to make sure the translation files are up to date with the latest changes to the guide.

You can do this by running the following command, replacing LANG by the language code you plan to work on (e.g., `es` for Spanish):

```shell
$ nox -s update-language -- LANG
```

This command will create the translation files if they don't exist yet, or update them with the latest changes if they already exist.

The translation files are text files with the `.po` extension stored in the `./locales`, in folders corresponding to each language. For example, the translation files for Spanish are stored in the `locale/es/LC_MESSAGES` directory.

Because the translation files map the original English text to translated text, they are sometimes referred to as "catalog" files or "portable object" files.

```{note}
You don't need to know all the details about the PO format in order to translate. If you are interested in learning more, you can find additional details in the [GNU gettext documentation](https://www.gnu.org/software/gettext/manual/html_node/PO-Files.html).
```

## Working on a Translation

In order to start translating, go to the folder inside `./locales` corresponding to the target language you want to translate to (for example, `./locale/es/LC_MESSAGES/` for the Spanish translation).

In this folder you will find a set of `.po` files, corresponding to the different sections of the guide:

```shell
$ cd ./locales/es/LC_MESSAGES/
$ ls *.po

./locales/es/LC_MESSAGES/CONTRIBUTING.po
./locales/es/LC_MESSAGES/index.po
./locales/es/LC_MESSAGES/tests.po
./locales/es/LC_MESSAGES/tutorials.po
./locales/es/LC_MESSAGES/documentation.po
./locales/es/LC_MESSAGES/package-structure-code.po
./locales/es/LC_MESSAGES/TRANSLATING.po
```

```{note}
You may also see some `.mo` files in the same folder. These are compiled versions of the `.po` files create by Sphinx during the build process, and used to generate the translated version of the guide. They are intermediary files and are not meant to be edited directly or stored in the repository.
```

If you are working on a new translation, choose one of the `.po` files to start with. If you are working on an existing translation, you can start with the `.po` files that need the most work.

To see how much of each file has been translated, use the `sphinx-intl stat`. You will be able to see the number of translated, fuzzy, and untranslated strings in each `.po` file.

For example, to see the statistics for the Spanish translation, you would run:

```shell
$ sphinx-intl stat -l es

locales/es/LC_MESSAGES/tutorials.po: 0 translated, 0 fuzzy, 950 untranslated.
locales/es/LC_MESSAGES/TRANSLATING.po: 0 translated, 0 fuzzy, 44 untranslated.
locales/es/LC_MESSAGES/package-structure-code.po: 0 translated, 0 fuzzy, 885 untranslated.
locales/es/LC_MESSAGES/CONTRIBUTING.po: 0 translated, 0 fuzzy, 38 untranslated.
locales/es/LC_MESSAGES/documentation.po: 0 translated, 0 fuzzy, 430 untranslated.
locales/es/LC_MESSAGES/tests.po: 155 translated, 2 fuzzy, 3 untranslated.
locales/es/LC_MESSAGES/index.po: 88 translated, 0 fuzzy, 5 untranslated.
```

What do these categories mean:

- Translated strings are strings that have been translated into the target language.
- Fuzzy strings are strings that have been translated but need to be reviewed because the original English string in the guide changed.
- Untranslated strings are strings that have not been translated yet.

```{note}
When Sphinx is building the guide in another language, it will look into the corresponding folder in `./locales/` for translated strings. If the translation is available, Sphinx will replace the English text with the equivalent text in the target language. If the translation is not available, Sphinx will use the original English strings.
```

## Editing the Translation Files

You can use any text editor to edit the `.po` file. But if you prefer, there are also tools like [Poedit](https://poedit.net/) that provide a graphic use interface.

Depending on your editor of choice, you may be able to install a plugin or extension that can provide syntax highlighting and other features for working with `.po` files. Like for example, the [gettext](https://marketplace.visualstudio.com/items?itemName=mrorz.language-gettext) extension for Visual Studio Code.

When you open a `.po` file, you will see a series of entries that look like this:

```po

#: ../../index.md:1
msgid "pyOpenSci Python Package Guide"
msgstr ""

```

The first line of an entry starts with `#:` and is a reference to the original source file and line number from which the text was extracted. This information is useful for finding the context of the text in the guide.

The `msgid` field contains the original English text that needs to be translated. The `msgstr` field is where you will enter the translated text. This field might contain text if someone else already translated the entry.

```po

#: ../../index.md:1
msgid "pyOpenSci Python Package Guide"
msgstr "La guía de paquetes de Python de pyOpenSci"

```

Sometimes the original English text may be too long for a single line, and it may be split into multiple lines. In this case, you can keep the same structure in the translated text. Notice that both the `msgid` and `msgstr` fields in the example below start with an empty string, indicating that the text continues in the next line.

```po
#: ../../index.md:254
msgid ""
"Every page in this guidebook goes through an extensive community review "
"process. To ensure our guidebook is both beginner-friendly and accurate, "
"we encourage reviews from a diverse set of pythonistas and scientists "
"with a wide range of skills and expertise."
msgstr ""
"Cada página en esta guía es revisada extensamente por la "
"comunidad. Para asegurar que nuestra guía sea comprensible a los principiantes y "
"a la vez precisa, un conjunto diverso de desarrolladores y científicos con una amplia "
"gama de conocimientos y experiencia participa en el proceso."
```

The English text will sometimes contain Markdown formatting, such as bold or italic text. You should keep the formatting in the translated text, making sure to translate the text inside the formatting tags.

The English text may also contain links to other sections of the guide or external resources. You should keep the links in the translated text, making sure to update the link text when appropriate.

```po
#: ../../index.md:75
msgid "[What is a Python package?](/tutorials/intro)"
msgstr "[¿Que es un paquete de Python?](/tutorials/intro)"
```

An entry may be marked as `fuzzy`, which means that the original English text has changed since the translation was made, and the translation may need to be revised. When this is the case you will see an additional line in the entry, starting with `#,`:

```po

#: ../../tests/write-tests.md:84
#, fuzzy
msgid ""
"**Test special cases:** Sometimes there are special or outlier cases. For"
" instance, if a function performs a specific calculation that may become "
"problematic closer to the value = 0, test it with the input of both 0 and"
msgstr ""
"**Prueba casos especiales:** A veces hay casos especiales o atípicos. Por"
" ejemplo, si una función realiza un cálculo específico que puede tener "
"problemas cerca del valor = 0, pruébalo con la entrada de 0 y un valor"
" normal."
```

You can review the translation and make any necessary changes, removing the `fuzzy` tag once you are satisfied with the translation.

You can also add comments to the translation file, by adding lines that start with a `#` character to the entry. This can be helpful to add context to the translation for other translators or reviewers to see, but this might be only necessary in special circumstances.

```{admonition} Important
When working on a translation, you **should not** modify the original English text in the `msgid` field. If you see a typo or an error in the original text, please consider fixing it in the original source file (use the first line of the entry to locate it) and submit a separate pull request.
```

## Building the Translated Documentation

Once you finished translating or when you want to check the translation in context, you can build the guide locally on your computer, using the following command, replacing LANG by the proper language code (e.g., `es` for Spanish)

```shell
nox -s build-language -- LANG
```

This command will build all the translated versions of the guide defined in the `LANGUAGES` list in `noxfile.py`. These translations will be stored in the `_build/html`, in folders named after the language code (e.g., `es`, `fr`, etc.).

To view the translated version of the guide in your browser, open the corresponding `index.html` file. For example, to view the Spanish translation, you would open `_build/html/es/index.html`.

You can also build a live version of the guide that updates automatically as you make changes to the translation files. To do this, use the `nox -s docs-live-lang` command. Note that in this case you need to specify which language you want to build. For example, if you are working on the Spanish translation, you would run:

```shell
nox -s docs-live-lang -- es
```

Note the `--` before the language code, it indicates that the following arguments should be passed into the nox session and not be interpreted directly by nox. If you forget the `--`, nox will look instead for a session named 'es' and raise an error that it does not exist.

This command will use `sphinx-autobuild` to launch a local web server where you can access the translated version of the guide. You can open the guide in your browser by navigating to `http://localhost:8000`.

This is a great way to see how the translated version of the guide looks as you make changes to the translation files.

## Submitting a PR for Your Contribution

Once you are finished translating and before you submit a pull request (PR) for your translation, you need to make sure that the translated version of the guide builds without any errors or warning and looks correctly in the browser.

You can follow these steps:

1. Build the translations of the guide with same parameters that will be used during the release:

```shell
nox -s build-all-languages-test
```

2. Make sure there are no warnings or errors in the output. If there are, you will need to fix them before submitting the PR.
3. Make sure the translated version of the guide looks good in the browser by opening the `_build/html/<lang>/index.html` file, where `<lang>` is the language you have been working on.

If everything looks good, you can submit a PR with your changes.

```{note}
When you submit a PR for a translation, you should only include changes to one language. If you worked in multiple languages, please submit a separate PR for each language.
```

Translations PRs will be tagged with a label indicating the language to make them easier to identify and review. For example, contributions to the Spanish translation will be tagged with 'lang-es'.

TODO: This tagging could be automated with a GitHub Actions.

When you submit the PR, make sure to include a short description of the changes you made and any context that might be helpful for the reviewer (e.g., you translated new strings, you reviewed fuzzy entries, you fixed typos, etc.)

## The Review Process

The review process for a translation contribution is similar to the review process for any other contribution to the guide.

TODO: This section needs more work, depending on the review workflow we decide to adopt. Other projects usually assign a coordinator/editor for each language, who is responsible for reviewing and merging translation contributions.

Each language has an assigned editor who is responsible for reviewing and merging translation contributions. The editor will review the changes to make sure they are accurate and consistent with the style and tone of the guide.

Sometimes the editor may ask for clarification or suggest changes to improve the translation. If this happens, you can make the requested changes and push them to the same branch where you submitted the original PR.

When the editor is satisfied with the translation, they will merge the PR. The translated version of the guide will be available on the pyOpenSci website once the language is released.

## The Release Process

If a language is ready to go live, the maintainers will add the language code to the `RELEASE_LANGUAGES` list in the `noxfile.py` configuration file.

When the guide is built for release in CI, Sphinx will also generate the translated versions of the guide for the languages in the `RELEASE_LANGUAGES` list.

Translations are released in the same way as the English version of the guide, and the translated versions will be available in folders named after the language code. For example, the Spanish translation will be available at: `https://www.pyopensci.org/python-package-guide/es/` when it is published online.

## Frequently Asked Questions (FAQ)

### How do I know which strings need to be translated?

When you run the `sphinx-intl stat` command, you will see a list of `.po` files with the number of translated, fuzzy, and untranslated strings. You can start by working on the files with the most untranslated strings.

### What happens when a string has changed in the original English text?

If a string has changed in the original English version, it will be marked as `fuzzy` in the translation file the next time it is updated (`update-language`, `update-all-languages`, or `update-all-release-languages`). Contributors working on the translation can then review the fuzzy entries and make the necessary changes to ensure it is accurate, before removing the `fuzzy` tag.

### How do I handle links in the translated text?

You should keep the links in the translated text, but make sure to update the link text if necessary. For example, if the original English text contains a link to `[What is a Python package?](/tutorials/intro)`, you should keep the link in the translated text but update the link text to `[¿Que es un paquete de Python?](/tutorials/intro)`.

### How do I handle formatting in the translated text?

You should keep the formatting in the translated text, but make sure to translate the text inside the formatting tags as well. For example, if the original English text is `**Test special cases:**`, you should keep the bold formatting in the translated text but update the text inside the formatting tags to `**Prueba casos especiales:**`.

### How do I handle strings that are too long for a single line?

If the original English text is too long for a single line, it may be split into multiple lines. Multiline strings in the `.po` file are indicated by an empty string in the `msgid` and `msgstr` fields, followed by the continuation of the text in the next line. For example:

```po

#: ../../index.md:254
msgid ""
"This is a multiple line string. The text continues on the next line."
" Notice the space in the beginning of the second line, you need to make sure"
" to account for the concatenation, there is no space inserted when starting a"
" a new line in a multiline string."
msgstr ""
```

### How do I translate images?

You should not translate images in the guide. Producing translated versions of images is a complex process that requires additional tools and resources, and it is not typically done unless the translated images are created alongside the original images. More often, the text around the image is modified to include any necessary translations.

In some special cases, an image might be critical to the understanding of the content. In those cases, the translations will be handled by the maintainers and editors outside this workflow.

### I am interested in translating the guide into a language that is not listed. How can I get started?

If you want to start a new translation of the guide into a language that is not listed, you should [create an issue](https://github.com/pyOpenSci/python-package-guide/issues) in the repository to let the maintainers know that you intend to work on it. This will help avoid duplication of effort and ensure that the maintainers are ready to review your contribution when you are done.

### How do I know when a translation is ready to be released?

When a translation is ready to be included in the next release of the guide, the maintainers will add the language code to the `RELEASE_LANGUAGES` list in the `noxfile.py` configuration file. This will trigger the build of the translation during the release process, and the translated version of the guide will be available on the pyOpenSci website.

TODO: There are many approaches here, some projects release a translation as soon as some strings are translated, others wait until a certain percentage of the content is translated.

### How can I get help with my translation?

If you have any questions or need help with your translation, you can create an [issue](https://github.com/pyOpenSci/python-package-guide/issues) in the [Packaging Guide repository](https://github.com/pyOpenSci/python-package-guide)

You can also ask in the PyOpenSci Discord server ([click here](https://discord.gg/NQtTTqtv) to join), you will find a general channel for questions related to our workflow, processes, and tools (translation-general) and channels for each of the languages we are working on (spanish-translation, japanese-translation, etc).
