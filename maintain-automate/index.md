(maintain-intro)=
# Automate Workflows and Maintain Your Package

Once you've [created your package](create-pure-python-package),
[published it](publish-pypi-tutorial), and set up a repository for it, the next
step is to automate development and maintenance workflows. Automation
makes maintaining your package easier, more robust, and more secure. It
also helps new contributors get started quickly without having to
manually set up complex development environments and testing workflows.

## Why automate?

When you automate repetitive tasks like running tests, checking code
style, and building documentation, you ensure that these important steps
happen consistently every time. This consistency helps you catch bugs
early, maintain code quality, and make it easier for others to
contribute to your package. Automation also saves you time—instead of
remembering and typing long command sequences, you can run everything
with simple commands or have workflows run automatically when you push
code to GitHub.

## What you'll learn

This section will walk you through two key automation strategies for
Python packages:

[**Task runners**](task-runners-intro) help you automate common development tasks locally—
things like running tests, building documentation, formatting code, and
checking for errors. Instead of typing out long command sequences every
time, you define tasks once and run them with simple commands. Task
runners like Hatch and Nox also manage isolated environments for
different workflows, ensuring you have the right dependencies for each
task.

[**Continuous Integration (CI)**](ci-cd) takes automation further by running your
tests and checks automatically every time code is pushed to GitHub or
when someone opens a pull request. CI ensures that all changes are
tested across different Python versions and operating systems before
they're merged. You can also use Continuous Deployment (CD) to automate
publishing your package to PyPI and deploying your documentation.

Together, task runners and CI/CD create a robust development workflow
that makes your package easier to maintain and more welcoming to
contributors.

:::{toctree}
:caption: Maintain & Automate
:hidden: true

What is CI?  <ci.md>
Task runners  <task-runners.md>
Environment Managers <environment-managers.md>
:::
