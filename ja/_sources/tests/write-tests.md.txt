# Write tests for your Python package

Writing code that tests your package code, also known as test suites, is important for you as a maintainer, your users, and package contributors. Test suites consist of sets of functions, methods, and classes
that are written with the intention of making sure a specific part of your code
works as you expected it to.

## Why write tests for your package?

Tests act as a safety net for code changes. They help you spot and rectify bugs
before they affect users. Tests also instill confidence that code alterations from
contributors won't breaking existing functionality.

Writing tests for your Python package is important because:

- **Catch Mistakes:** Tests are a safety net. When you make changes or add new features to your package, tests can quickly tell you if you accidentally broke something that was working fine before.
- **Save Time:** Imagine you have a magic button that can automatically check if your package is still working properly. Tests are like that magic button! They can run all those checks for you saving you time.
- **Easier Collaboration:** If you're working with others, or have outside contributors, tests help everyone stay on the same page. Your tests explain how your package is supposed to work, making it easier for others to understand and contribute to your project.
- **Fearless Refactoring:** Refactoring means making improvements to your code structure without changing its behavior. Tests empower you to make these changes as if you break something, test failures will let you know.
- **Documentation:** Tests serve as technical examples of how to use your package. This can be helpful for a new technical contributor that wants to contribute code to your package. They can look at your tests to understand how parts of your code functionality fits together.
- **Long-Term ease of maintenance:** As your package evolves, tests ensure that your code continues to behave as expected, even as you make changes over time. Thus you are helping your future self when writing tests.
- **Easier pull request reviews:** By running your tests in a CI framework such as GitHub Actions, each time you or a contributor makes a change to your code-base, you can catch issues and things that may have changed in your code base. This ensures that your software behaves the way you expect it to.

### Tests for user edge cases

Edge cases refer to unexpected or "outlier" ways that some users may use your package. Tests enable you to address various edge cases that could impair
your package's functionality. For example, what occurs if a function expects a
pandas `dataframe` but a user supplies a numpy `array`? Does your code gracefully
handle this situation, providing clear feedback, or does it leave users
frustrated by an unexplained failure?

:::{note}

For a good introduction to testing, see [this Software Carpentry lesson](https://swcarpentry.github.io/python-novice-inflammation/10-defensive.html)

:::

```{figure} ../images/python-tests-puzzle.png
:height: 350px

Imagine you're working on a puzzle where each puzzle piece represents a function, method, class or attribute in your Python package that you want other people to be able to use. Would you want to give someone a puzzle that has missing pieces or pieces that don't fit together? Providing people with the right puzzle pieces that work together can be compared to writing tests for your Python package.

```

````{admonition} Test examples
:class: note

Let’s say you have a Python function that adds two numbers a and b together.

```python
def add_numbers(a, b):
    return a + b
```

A test to ensure that function runs as you might expect when provided with different numbers might look like this:

```python
def test_add_numbers():
    result = add_numbers(2, 3)
    assert result == 5, f"Expected 5, but got {result}"

    result2 = add_numbers(-1, 4)
    assert result2 == 3, f"Expected 3, but got {result2}"

    result3 = add_numbers(0, 0)
    assert result3 == 0, f"Expected 0, but got {result3}"

test_add_numbers()

```
````

🧩🐍

### How do I know what type of tests to write?

:::{note}
This section has been adapted from [a presentation by Nick Murphy](https://zenodo.org/record/8185113).
:::

At this point, you may be wondering - what should you be testing in your package? Below are a few examples:

- **Test some typical cases:** Test that the package functions as you expect it to when users use it. For instance, if your package is supposed to add two numbers, test that the outcome value of adding those two numbers is correct.

- **Test special cases:** Sometimes there are special or outlier cases. For instance, if a function performs a specific calculation that may become problematic closer to the value = 0, test it with the input of both 0 and

* **Test at and near the expected boundaries:** If a function requires a value that is greater than or equal to 1, make sure that the function still works with both the values 1 and less than one and 1.001 as well (something close to the constraint value)..

* **Test that code fails correctly:** If a function requires a value greater than or equal to 1, then test at 0.999. Make sure that the function fails gracefully when given unexpected values and help and that the user can easily understand why if failed (provides a useful error message).
