# Run tests with Continuous Integration

Running your [test suite locally](run-tests) is useful as you develop code and also test new features or changes to the code base. However, you also will want to setup Continuous Integration (CI) to run your tests online. CI allows you to run all of your tests in the cloud. While you may only be able to run tests locally on a specific operating system that you run, in CI you can specify tests to run both on various versions of Python and across different operating systems.

CI can also be triggered for pull requests and pushes to your repository. This means that every pull request that you, your maintainer team or a contributor submit, can be tested. In the end CI testing ensures your code continues to run as expected even as changes are made to the code base.

```{note}
[Learn more about Continuous Integration and how it can be used, here.](ci)
```

## CI & pull requests

CI is invaluable if you have outside people contributing to your software.
You can setup CI to run on all pull requests submitted to your repository.
CI can make your repository more friendly to new potential contributors.
It allows users to contribute code, documentation fixes and more without
having to create development environments, run tests and build documentation
locally.

## Example GitHub action that runs tests

Below is an example github action that runs tests using nox
across both Windows, Mac and Linux and on Python versions
3.9-3.11. It also includes two steps that make your build more
efficient so your dependencies aren't downloaded multiple times.

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
        with:
          # fetch more than the last single commit to help scm generate proper version
          fetch-depth: 20
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
          cache: pip

      # This step and the step below are an optional steps to cache variables to make your build faster / more efficient
      - name: Set Variables
        id: set_variables
        shell: bash
        run: |
          echo "PY=$(python -c 'import hashlib, sys;print(hashlib.sha256(sys.version.encode()+sys.executable.encode()).hexdigest())')" >> $GITHUB_OUTPUT
          echo "PIP_CACHE=$(pip cache dir)" >> $GITHUB_OUTPUT
      - name: Cache dependencies
        uses: actions/cache@v3
        with:
          path: ${{ steps.set_variables.outputs.PIP_CACHE }}
          key: ${{ runner.os }}-pip-${{ steps.set_variables.outputs.PY }}
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install nox
      - name: List installed packages
        run: pip list
      - name: Run tests with pytest & nox
        run: |
          nox -s tests-${{ matrix.python-version }}
      # You only need to upload code coverage once to codecov
      - name: Upload coverage to Codecov
        if: ${{ matrix.os == 'ubuntu-latest' &&  matrix.python-version == '3.10'}}
        uses: codecov/codecov-action@v3
```
