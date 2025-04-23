(contributing-file)=
# Your Python Package CONTRIBUTING File

The **CONTRIBUTING.md** is the landing page guide for your project's contributors. It outlines how contributors can get involved, the contribution types that you welcome, and how contributors should interact or engage with you and your maintainer team. The contributor guide should also link to get-started resources that overview how to set up development environments, what type of workflow you expect on GitHub/GitLab, and anything else that contributors might need to get started.

This file benefits maintainers and contributors. For contributors, it provides a roadmap that helps them get started and makes their first contribution easier. For maintainers, it answers commonly asked questions and reduces the burden of explaining your process to every person who wants to contribute. This document creates a more collaborative and efficient development process for everyone.

## CONTRIBUTING files lower barriers to entry

The contributing file lowers barriers to entry for new and seasoned contributors as it provides a roadmap.

- **For Contributors**: It provides clear instructions on contributing, from reporting issues to submitting pull requests.
- **For Maintainers**: It streamlines contributions by setting expectations and standardizing processes, reducing the time spent clarifying common questions or handling incomplete issues or pull requests.

Including a well-written CONTRIBUTING.md file in your project is one way of making it more welcoming and open to new and seasoned contributors. It also helps create a smoother workflow for everyone involved.

## Make it welcoming

Make the guide welcoming. Use accessible language to encourage participation from contributors of all experience levels. For example:

- Avoid technical jargon or explain terms when necessary (for example, "fork the repository").
- Include a friendly introduction, such as "Thank you for your interest in contributing! We're excited to collaborate with you."
- Highlight that all contributions, no matter how small, are valued.

## What a CONTRIBUTING.md file should contain

:::{admonition} Example contributing files
:class: tip

- [PyGMT contributing file](https://github.com/GenericMappingTools/pygmt/blob/main/CONTRIBUTING.md)
- [Verde's contributing file](https://github.com/fatiando/verde/blob/main/CONTRIBUTING.md)
:::

Your Python package should include a file called **CONTRIBUTING.md** located in the
root of your repository next to [your **README.md** file](readme-file).

The CONTRIBUTING.md file should include information about:

- The types of contributions that you welcome

> Example: We welcome contributions of all kinds. If you want to address an existing issue, check out our issues in this repository and comment on the one that you'd like to help with. Otherwise, you can open a new issue...

- How you'd like contributions to happen. Clearly outline your contribution process. For example:
  - Should contributors address open issues
  - Are new issues welcome?
  - Should contributors open a pull request (PR) directly or discuss changes first?

- Include instructions for the fork and pull request workflow and link to resources or guides explaining these steps (if available).
- Guidelines that you have in place for users submitting issues, pull requests, or asking questions.

If you have a [development guide](development-guide), link to it. This guide should provide clear instructions on how to set up your development environment locally. It also should overview CI tools that you have that could simplify the contribution process (for example, pre-[commit.ci bot](https://www.pyopensci.org/python-package-guide/package-structure-code/code-style-linting-format.html#pre-commit-ci), and so on), [linters, code formatters](https://www.pyopensci.org/python-package-guide/package-structure-code/code-style-linting-format.html#code-linting-formatting-and-styling-tools), and so on.

This guide should also include information for someone
interested in asking questions. Some projects accept questions as GitHub or GitLab issues. Others use GitHub discussions, Discourse, or even a Discord server.

The contributing file should also include:

- A link to your [code of conduct](coc-file)
- A link to your project's [LICENSE](license-file)
- A link to a [development guide](development-guide) if you have one

## Summary

A well-crafted CONTRIBUTING.md file is welcome mat for your project! By providing clear instructions, helpful resources, and a welcoming tone, you make it easier for contributors to get involved and build a stronger, more collaborative community around your project.
