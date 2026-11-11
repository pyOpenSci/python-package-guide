(in-tree-tests)=
# Shipping tests with your package (in-tree tests)

Throughout this guide we recommend keeping your `tests/` directory **outside**
of your package directory (an "out-of-tree" layout). This keeps your wheel
small and, combined with the [src layout](src-layout-test), helps ensure
that your tests run against the *installed* package rather than the files in
your working directory.

Some packages, however, benefit from shipping their tests inside the package
("in-tree" tests). This is common in the scientific Python ecosystem: NumPy,
SciPy, and scikit-image all do it.

## When in-tree tests make sense
Consider in-tree tests if your package:
* **Contains compiled code** (C, C++, Cython, Rust, or Fortran). A wheel built
  on one platform may import fine but produce wrong results on another.
  Letting users run the test suite against the wheel they installed
  is the most reliable way to find out.
* **Is built by downstream packagers** such as conda-forge, Debian, or Spack.
  Downstream packagers building from an sdist can run tests included in that
  source distribution, even when tests are excluded from wheels. If supporting
  these builds is the only goal, including tests in the sdist may be sufficient
  (see below).
* Has users who need to **verify an installation** on an HPC cluster or
  another locked-down environment where they can't clone the repository.

If your package is pure Python with a small test suite, out-of-tree tests are
simpler, and we recommend sticking with them.

## Alternative: include tests in the sdist only
Tests do not have to be installed with a wheel to be available to downstream
packagers. A project can keep its `tests/` directory outside the package and
include those files in its source distribution (sdist) without including them
in the wheel. Downstream packagers building from the sdist can then run the
tests without increasing the size of wheels distributed to end users.
This supports downstream validation using files from the sdist, but users
cannot run those tests from an installed wheel alone.

For example, with setuptools, an out-of-tree `tests/` directory can be
included in the sdist using a `MANIFEST.in` entry:

```text
graft tests
```
This does not itself control wheel contents: ensure `tests/` is not selected
as an installed package or included by other wheel configuration. Different
build backends provide different controls for source and wheel contents.
Check both built artifacts to confirm which files are included. For example,
build into a fresh output directory containing one sdist and one wheel:

```bash
python -m build --outdir dist-check
tar -tf dist-check/*.tar.gz | grep '/tests/'
unzip -Z -1 dist-check/*.whl | grep -E '(^|/)tests/'
```

For the sdist-only approach, the first command listing files should show the
tests, while the wheel listing should have no matching files. The final `grep`
will exit with status 1 when no tests are found; that is expected here.
See the [setuptools guidance on wheel and sdist contents](https://setuptools.pypa.io/en/latest/userguide/miscellaneous.html#wheel-vs-sdist).

If users need to run tests against an installed wheel, including tests in the
importable package as described below may be more appropriate.

## Layout
Move `tests/` inside your package directory and give it an `__init__.py` so
that it is discovered and installed like any other subpackage:

```bash
src/
  mypackage/
    __init__.py
    core.py
    tests/
      __init__.py
      test_core.py
docs/
pyproject.toml
```

:::{admonition} Make sure the tests ship
:class: tip
Check your build backend's package-discovery settings. If you list packages
explicitly, add `mypackage.tests`. After building, inspect the wheel
(`unzip -l dist/*.whl`) to confirm that the test files are included.
:::

## Run tests against the installed package
With tests inside the package, run them using pytest's `--pyargs` flag. This
tells pytest to import `mypackage` from the active environment, locate its
`tests` subpackage, and run it, regardless of your current working directory:

```bash
pytest --pyargs mypackage
```

Many scientific packages also expose a convenience function so that users
don't need to remember the flag:
```python
# src/mypackage/__init__.py
def test(*args):
    """Run the mypackage test suite."""
    import pytest

    return pytest.main(["--pyargs", "mypackage", *args])
```

```python
>>> import mypackage
>>> mypackage.test()
```

Because `pytest` is imported only when the function is called, it is not
required for ordinary package use. If the distributed tests import pytest
or the public `test()` helper shown above uses pytest, declare it as an
optional dependency so users can install it when they need to run tests:

```toml
[project.optional-dependencies]
test = ["pytest"]
```
If distributed tests use `unittest` and do not require pytest, there is no
need to expose pytest as an optional dependency solely because developers
use it as a test runner. Instead, projects can declare pytest in a
development dependency group or manage it through their development environment.

For packages that ship `unittest.TestCase` tests inside the importable
package, users can run an installed test module with Python's built-in
`unittest` runner without installing pytest:

```bash
python -m unittest mypackage.tests.test_core
```

Replace `mypackage.tests.test_core` with the fully qualified name of an
installed test module. To discover all compatible tests in the installed
tests package, use:

```bash
python -m unittest discover -s mypackage.tests
```

The `unittest` runner does not collect standalone pytest-style test functions
and does not provide pytest fixtures. Tests that depend on pytest-specific
features may require pytest to run successfully.

If distributed tests or a public test helper require third-party dependencies,
projects may declare those dependencies in a `test` extra to support running
the tests after installation.

## Pitfalls
**Running tests on the source tree by accident.** This is the main reason we
recommend out-of-tree tests for beginners. If you run
`pytest src/mypackage/tests` from the repository root, Python may import your
*un-built* source files instead of the installed package. With compiled code,
this surfaces as confusing `ImportError`s about missing extension modules.
Always use `pytest --pyargs mypackage` (or a `nox` or `tox` session that
installs the package first) rather than pointing pytest at a path.

**Test data.** Don't ship large datasets inside your wheel. See
[don't include test suite datasets in your package](src-layout-test)
for alternatives such as Pooch.

**Wheel size.** Every test file is downloaded by every user. Keep the in-tree
suite focused. Very slow or data-heavy tests can stay out of tree and run only
in CI.

For a real-world example, see how
[NumPy](https://github.com/numpy/numpy/tree/main/numpy) organizes
`numpy/tests` and `numpy/<submodule>/tests`, and exposes `numpy.test()`.
