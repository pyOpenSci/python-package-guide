(in-tree-tests)=
# Shipping tests with your package (in-tree tests)

Throughout this guide we recommend keeping your `tests/` directory **outside**
of your package directory (an "out-of-tree" layout). This keeps your wheel
small and, combined with the [src layout](src-layout-test), guarantees that
your tests run against the *installed* package rather than the files in your
working directory.

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
  Packagers routinely run a package's test suite as part of their build, and
  they can only do so if the tests ship with the package.
* Has users who need to **verify an installation** on an HPC cluster or
  another locked-down environment where they can't clone the repository.

If your package is pure Python with a small test suite, out-of-tree tests are
simpler, and we recommend sticking with them.

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

Because `pytest` is only imported inside the function, it stays an optional
dependency. Add it to a `test` extra in your `pyproject.toml`:

```toml
[project.optional-dependencies]
test = ["pytest"]
```

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
