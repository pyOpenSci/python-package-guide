> _This issue is created automatically and should not be edited directly._

We are translating the Python Package Guide into {{LANGUAGE}}, and we need new contributors. If you speak {{LANGUAGE}} and you are new to open source, this is a great place to start!

### What you will be doing

The guide is divided into sections. For each section, the English text is stored in a `.po` file inside `./locales/{{LOCALE}}/LC_MESSAGES`. Next to each English string, there is a space to write the {{LANGUAGE}} translation.

### Getting started

Read the [Translation Guide](https://www.pyopensci.org/python-package-guide/TRANSLATING.html) first. It explains the workflow and how to set up your local environment.

New to open source? You can also work entirely from the GitHub website. Fork the repository into your account, make your changes on your copy, and open a Pull Request. Two parts of the Translation Guide are worth reading first: [Editing the Translation Files](https://www.pyopensci.org/python-package-guide/TRANSLATING.html#editing-the-translation-files), which shows what a `.po` entry looks like, and the [Frequently Asked Questions (FAQ)](https://www.pyopensci.org/python-package-guide/TRANSLATING.html#frequently-asked-questions-faq).

If you are working in one of our development sprints at a conference, someone from the pyOpenSci team will be available to help you get set up.

### Pick a file and claim your work

Each file in the table below has its own issue. Click a file name to open it. There, leave a comment claiming a range of lines to work on, so your work does not overlap with anyone else's. Read the existing comments first to see which lines are already taken.

Look at the untranslated column — a file with a smaller number there is an easier place to start.

**Not sure where to start?** If `index.po` still has untranslated strings, start there. Finishing it is what lets us publish this language, so it is the most useful file to work on when you don't have a particular section in mind.

### See an example

{{EXAMPLE_SECTION}}

<!--
  {{EXAMPLE_SECTION}} — the "See an example" paragraph. Which file it points at,
  and how it describes that file, are both decided by example_section() in
  update_translation_issues.py. Edit the wording there: a copy kept here would
  have no effect and would quietly go stale.
-->

### Translation status as of {{STATS_DATE}}

The table shows the number of strings in each file.

**If you come across a string marked `fuzzy`**, it already has a {{LANGUAGE}} translation, but that translation needs a second look to confirm it is correct. Usually this is because the English text changed after the string was translated, though a string can be marked fuzzy for other reasons too. Compare the translation against the English text above it. If it still says the right thing, simply remove the line with the **fuzzy** tag. If it does not, rewrite it and then remove the tag. The Translation Guide explains this further in [What happens when a string has changed in the original English text](https://www.pyopensci.org/python-package-guide/TRANSLATING.html#what-happens-when-a-string-has-changed-in-the-original-english-text).

{{STATS_TABLE}}
