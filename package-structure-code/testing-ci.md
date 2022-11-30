# Testing and CI??






### Testing
- All packages should have a test suite that covers major functionality of the package. The tests should also cover the behavior of the package in case of errors.
- It is good practice to write unit tests for all functions, and all package code in general, ensuring key functionality is covered. Test coverage below 75% will likely require additional tests or explanation before being sent for review.
- We recommend using pytest for writing tests, but you can use other tools. Strive to write tests as you write each new function. This serves the obvious need to have proper testing for the package, but allows you to think about various ways in which a function can fail, and to defensively code against those.
- Consider using tox to test your package with multiple versions of Python 2 and 3.
- If you set up CI with code coverage, use your package's code coverage report to identify untested lines, and to add further tests.

**Good/Better/Best:**
- **Good:** A test suite that covers major functionality of the package.
- **Better:** The above, with high code coverage.
- **Best:** All of the above, plus using tox to test multiple versions of Python.

### Continuous Integration
All pyOpenSci packages must use some form of continuous integration.

- For Linux and Mac OSX, we suggest GitHub Actions, Circle CI or Travis CI.
- For Windows, we suggest GitHub Actions or AppVeyor CI.
- In many cases, you will want CI for all platforms. Different continuous integration services will support builds on different operating systems. Packages should have CI for all platforms when they contain:
    - Compiled code
    - Java dependencies
    - Dependencies on other languages
    - Packages with system calls
    - Text munging such as getting people’s names (in order to find encoding issues).
    - Anything with file system / path calls
    - In case of any doubt regarding the applicability of these criteria to your package, it’s better to add CI for all platforms, and most often not too much hassle.

**Good/Better/Best:**
- **Good:** Some sort of CI service with status badge in your README.
- **Better:** The above plus integrated code coverage and linting.
- **Best:** Continuous integration for all platforms: Linux, Mac OSX, and Windows.





This section provides guidelines and tips for creating a Python package to submit for peer-review.

pyOpenSci packages must:
- Have a clear README _including_ installation instructions.
- Contain full documentation for any user-facing functions.
- Have a test suite that covers the major functionality of the package.
- Use continuous integration.
- Use an OSI approved software license.





### License
pyOpenSci projects should use an open source software license that is approved by the Open Software Initiative (OSI). OSI's website has a [list of popular licenses](https://opensource.org/licenses), and GitHub has a [handy tool](https://choosealicense.com/) for choosing a license.

**Good/Better/Best:**
- **Good:** Include a open source software license with your package.
- **Better/Best:** Choose a license based on your needs and future use of package, plus explain your choice in your submission for review.

## Other recommendations
### Python version support
You should always be explicit about which versions of Python your package supports.
Keeping compatibility with old Python versions can be difficult as functionality changes.
A good rule of thumb is that the package should support, at least,
the latest three Python versions (e.g., 3.8, 3.7, 3.6).

### Code Style
pyOpenSci encourages authors to consult [PEP 8](https://www.python.org/dev/peps/pep-0008/) for information on how to style your code.

### Linting
An automatic linter (e.g. flake8) can help ensure your code is clean and free of syntax errors. These can be integrated with your CI.

### Badges

Badges are a useful way to draw attention to the quality of your project and to
assure users that it is well-designed, tested, and maintained.
It is common to provide a collection of badges in a table for others
to quickly browse.

[See this example of a badge table](https://github.com/ropensci/drake). Such a table should be more wide than high. (Note that the badge for pyOpenSci peer-review will be provided upon acceptance.)
