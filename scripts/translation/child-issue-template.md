> _This issue is created automatically and should not be edited directly._

This issue is for translating **[`{{FILENAME}}`]({{FILE_URL}})** into {{LANGUAGE}}. It is one part of the larger effort tracked in the main issue: {{MAIN_ISSUE_URL}}. Start there if you want the full picture and the setup steps.

Thank you for helping! If this is your first open source contribution, you are in the right place.

{{PRIORITY_NOTE}}

<!--
  {{PRIORITY_NOTE}} — a note about `index.po` being the file that lets us
  publish the language on the site. It is worded one way in `index.po`'s own
  sub-issue and another way everywhere else, and disappears once `index.po` is
  finished. All of that is decided by priority_note() in
  update_translation_issues.py. Edit the wording there: a copy kept here would
  have no effect and would quietly go stale.
-->

If you are working in one of our development sprints at a conference, someone from the pyOpenSci team will be available to help you get set up.

### Claim your lines

To keep our work from overlapping, claim a range of lines before you start:

1. Read the comments below to see which lines are already taken.
2. Add a comment with the lines you will translate. You can copy this:
   > I'm working on lines 1–100.
3. When your part is ready, open a Pull Request and link back to this issue.

You can see line numbers when you open the file on GitHub. If you are not sure how much you can take on, start with a small range. You can always claim more later.

When you link this issue from your Pull Request, please write `Part of #{{ISSUE_NUMBER}}` rather than `Closes #{{ISSUE_NUMBER}}`. Several people are translating this file, so it should stay open until every line is done.

### Resources

- [Translation Guide](https://www.pyopensci.org/python-package-guide/TRANSLATING.html) — the full workflow and how to set up your local environment
- [Editing the Translation Files](https://www.pyopensci.org/python-package-guide/TRANSLATING.html#editing-the-translation-files) — what a `.po` entry looks like, and tools that help you edit one
- [Frequently Asked Questions (FAQ)](https://www.pyopensci.org/python-package-guide/TRANSLATING.html#frequently-asked-questions-faq) — common questions answered
{{EXAMPLE_BULLET}}

<!--
  {{EXAMPLE_BULLET}} — a Resources bullet pointing at the example file, so
  contributors have a reference for style and formatting. It is empty in the
  sub-issue whose own file IS the example. Both the choice and the wording are
  decided by example_bullet() in update_translation_issues.py. Edit the wording
  there: a copy kept here would have no effect and would quietly go stale.
-->

### This file, as of {{STATS_DATE}}

**If you come across a string marked `fuzzy`**, it already has a {{LANGUAGE}} translation, but that translation needs a second look to confirm it is correct. Usually this is because the English text changed after the string was translated, though a string can be marked fuzzy for other reasons too. Compare the translation against the English text above it. If it still says the right thing, simply remove the line with the **fuzzy** tag. If it does not, rewrite it and then remove the tag. The Translation Guide explains this further in [What happens when a string has changed in the original English text](https://www.pyopensci.org/python-package-guide/TRANSLATING.html#what-happens-when-a-string-has-changed-in-the-original-english-text).

{{STATS_TABLE}}
