# Run tests with Continuous Integration

Running your [test suite locally](run-tests) is useful as you develop code and also test new features or changes to the code base. However, you also will want to setup Continuous Integration (CI) to run your tests online. CI allows you to run all of your tests in the cloud. While you may only be able to run tests locally on a specific operating system, using CI you can specify tests to run both on various versions of Python and across different operating systems.

CI can also be triggered for pull requests and pushes to your repository. This means that every pull request that you, your maintainer team or a contributor submit, can be tested. In the end CI testing ensures your code continues to run as expected even as changes are made to the code base.

::::{todo}
```{note}
Learn more about Continuous Integration and how it can be used, here. (add link)
```
::::

## CI & pull requests

CI is invaluable if you have outside people contributing to your software.
You can setup CI to run on all pull requests submitted to your repository.
CI can make your repository more friendly to new potential contributors.
It allows users to contribute code, documentation fixes and more without
having to create development environments, run tests and build documentation
locally.

## Example GitHub Actions that runs tests

Below is an example GitHub Actions that runs tests using nox
across both Windows, Mac and Linux and on Python versions
3.9-3.11.

To work properly, this file should be located in a root directory of your
GitHub repository:

```bash
pyospackage/
├──.github/
   └── workflows/
       └── run-tests.yml # The name of this file can be whatever you wish
```


```yaml
name: Pytest unit/integration

on:
  pull_request:
  push:
    branches:
      - main

# Use bash by default in all jobs
defaults:
  run:
    shell: bash

jobs:
  build-test:
    name: Test Run (${{ matrix.python-version }}, ${{ matrix.os }})
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: false
      matrix:
        os: ["ubuntu-latest", "macos-latest", "windows-latest"]
        python-version: ["3.9", "3.10", "3.11"]

    steps:
      - uses: actions/checkout@v4
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          python -m pip install nox
      - name: List installed packages
        run: pip list
      - name: Run tests with pytest & nox
        run: |
          nox -s tests-${{ matrix.python-version }}
      # You only need to upload code coverage once to codecov unless you have a
      # more complex build that you need coverage for.
      - name: Upload coverage to Codecov
        if: ${{ matrix.os == 'ubuntu-latest' &&  matrix.python-version == '3.10'}}
        uses: codecov/codecov-action@v3
```
