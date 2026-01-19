# Test Types for Python packages

## Three types of tests: unit, integration, and functional tests

There are different types of tests that you want to consider when
creating your test suite:

1. Unit tests
2. Integration tests
3. End-to-end (also known as functional) tests

Each type of test has a different purpose. Here, you will learn
about all three types of tests by working through simple, runnable
examples that you can use in your own package.

## Unit tests

A unit test involves testing individual components or units of code
in isolation to ensure that they work correctly. The goal of unit
testing is to verify that each part of the software, typically at the
function or method level, performs its intended task correctly.

Unit tests can be compared to examining each piece of your puzzle to
ensure parts of it are not broken. If all of the pieces of your puzzle
don't fit together, you will never complete it. Similarly, when working
with code, tests ensure that each function, attribute, class, and
method works properly when isolated.

**Unit test example:** Suppose you have a function that adds two
numbers together. A unit test for that function ensures that when
provided with two numbers, it returns the correct sum. This is a unit
test because it checks a single unit (function) in isolation.

```python
# src/mypackage/math_utils.py
def add_numbers(a, b):
    """
    Add two numbers together.

    Parameters
    ----------
    a : float
        First number.
    b : float
        Second number.

    Returns
    -------
    float
        Sum of a and b.
    """
    return a + b
```

Example unit test for the above function. You'd run this test using
the `pytest` command in your **tests/** directory.

```python
# tests/test_math_utils.py
from mypackage.math_utils import add_numbers


def test_add_numbers():
    """
    Test the add_numbers function.
    """
    # Test with positive numbers
    assert add_numbers(2, 3) == 5

    # Test with negative numbers
    assert add_numbers(-1, 4) == 3

    # Test with zero
    assert add_numbers(0, 5) == 5
```

Notice that the tests above don't just test one case where numbers are
added together. Instead, they test multiple scenarios: adding positive
numbers, adding a negative number, and adding zero. This helps ensure
that the `add_numbers` function behaves correctly in different
situations and is the beginning of thinking about programming
defensively.

You can run this test from your terminal using
`pytest tests/example.py`.

```{figure} ../images/pyopensci-puzzle-pieces-tests.png
:height: 300px
:alt: image of puzzle pieces that all fit together nicely. The puzzle pieces are colorful - purple, green and teal.

Your unit tests should ensure each part of your code works as expected on its own.
```

## Integration tests

Integration tests involve testing how parts of your package work
together or integrate. Integration tests can be compared to connecting
a bunch of puzzle pieces together to form a whole picture. Integration
tests focus on how different pieces of your code fit and work together.

For example, suppose you have functions that convert temperatures and
calculate statistics. An integration test would ensure that these
functions work together correctly in a workflow where you convert
temperatures and then analyze them.

```python
# src/mypackage/temperature_utils.py
def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.

    Parameters
    ----------
    celsius : float
        Temperature in Celsius.

    Returns
    -------
    float
        Temperature in Fahrenheit.
    """
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.

    Parameters
    ----------
    fahrenheit : float
        Temperature in Fahrenheit.

    Returns
    -------
    float
        Temperature in Celsius.
    """
    return (fahrenheit - 32) * 5 / 9


def average_temperature(temps):
    """
    Calculate average temperature from a list.

    Parameters
    ----------
    temps : list
        List of temperatures.

    Returns
    -------
    float
        Average temperature.
    """
    return sum(temps) / len(temps)


def convert_and_average(temps_celsius):
    """
    Convert list of Celsius temps to Fahrenheit and
    calculate the average.

    Parameters
    ----------
    temps_celsius : list
        List of Celsius temperatures.

    Returns
    -------
    float
        Average temperature in Fahrenheit.
    """
    temps_fahrenheit = [celsius_to_fahrenheit(t)
                        for t in temps_celsius]
    return average_temperature(temps_fahrenheit)
```

Here's an integration test that checks how the conversion and
statistics functions work together:

```python
# tests/test_temperature_integration.py
from mypackage.temperature_utils import convert_and_average


def test_convert_and_average():
    """
    Test that convert_and_average correctly combines conversion
    and averaging.
    """
    # Test with known values: [0, 10, 20] Celsius
    # Should average to 10 Celsius = 50 Fahrenheit
    temps_celsius = [0, 10, 20]
    result = convert_and_average(temps_celsius)
    assert abs(result - 50.0) < 0.01

    # Test with different values
    temps_celsius = [0, 100]
    result = convert_and_average(temps_celsius)
    # Average of 32 and 212 Fahrenheit = 122
    assert abs(result - 122.0) < 0.01
```

This integration test verifies that the conversion and averaging
functions work together as expected in a real workflow.

```{figure} ../images/python-tests-puzzle.png
:height: 350px
:alt: image of two puzzle pieces with some missing parts. The puzzle pieces are purple teal yellow and blue. The shapes of each piece don’t fit together.

If puzzle pieces have missing ends, they can’t work together with other elements in the puzzle. The same is true with individual functions, methods and classes in your software. The code needs to work both individually and together to perform certain sets of tasks.

```

```{figure} ../images/python-tests-puzzle-fit.png
:height: 450px
:alt: image of puzzle pieces that all fit together nicely. The puzzle pieces are colorful - purple, green and teal.

Your integration tests should ensure that parts of your code that are expected to work
together, do so as expected.

```

## End-to-end (functional) tests

End-to-end tests (also referred to as functional tests) in Python are
like comprehensive checklists for your software. They simulate real
user workflows to make sure the code base supports real-life
applications and use-cases from start to finish. These tests help catch
issues that might not show up in smaller tests and ensure your entire
application behaves correctly. Think of them as a way to give your
software a final check before it's put into action, making sure it's
ready to deliver a smooth user experience.

```{figure} ../images/flower-puzzle-pyopensci.jpg
:height: 450px
:alt: Image of a completed puzzle showing a daisy

End-to-end or functional tests represent an entire workflow that
your package supports.

```

**End-to-end test example:** Let's say your package opens and processes/converts temperature data from Celsius to Fahrenheit and then calculates the average temperature. An end-to-end test would simulate this entire workflow, ensuring that the package correctly handles the input
temperature data and returns a summary average value. An end-to-end
test would provide sample data, run the entire workflow, and verify
that the final output is correct.

```python
# tests/test_temperature_e2e.py
from mypackage.temperature_utils import convert_and_average


def test_temperature_workflow():
    """
    Test the complete temperature processing workflow.

    This end-to-end test provides sample temperature data in
    Celsius, processes it through the full workflow
    (conversion and averaging), and verifies the output is
    correct.
    """
    # Sample temperature data in Celsius
    temps_celsius = [0, 10, 20]

    # Run the complete workflow
    result = convert_and_average(temps_celsius)

    # Verify the output
    # Average of 32, 50, and 68 Fahrenheit = 50 Fahrenheit
    assert abs(result - 50.0) < 0.01
```

This end-to-end test exercises the entire user workflow: providing
sample data, converting and averaging it, and verifying the output
is correct.

End-to-end tests also verify how a program runs from start to finish.
A tutorial that you add to your documentation and run in CI is another
example of an end-to-end test. For example, a Jupyter (`.ipynb`) notebook or
`.md` file with embedded code that demonstrates a complete user
workflow.

:::{note}
For scientific packages, creating short tutorials that highlight core
workflows that your package supports, that are run when your
documentation is built, could also serve as end-to-end tests.
:::

## When to use which test type

Choosing the right test type depends on what you are trying to verify.
Use this guide to decide which test type is most appropriate for
different situations:

### Decision tree

**Are you testing a single function, method, or class in isolation?**

→ **Yes:** Use a [unit test](test-types.md#unit-tests).

- Example: Testing that `add_numbers(2, 3)` returns `5`.
- Unit tests are fast and help you pinpoint exactly where errors occur.
- Write unit tests for all the core building blocks of your package.

**Are you testing how multiple components work together?**

→ **Yes:** Use an [integration test](test-types.md#integration-tests).

- Example: Testing that temperature conversion and averaging functions
    work together correctly in a single workflow.
- Integration tests verify that your components communicate properly.
- Use these after you have tested individual components with unit tests.

**Are you testing a complete, realistic user workflow from start to finish?**

→ **Yes:** Use an [end-to-end test](test-types.md#end-to-end-functional-tests).

- Example: Simulating a user loading data, processing it, and getting a
    summary result.
- End-to-end tests catch issues that do not show up in smaller tests.
- For scientific packages, tutorials run during documentation builds can
    serve as end-to-end tests.

## Comparing unit, integration, and end-to-end tests

Unit tests, integration tests, and end-to-end tests have complementary
advantages and disadvantages. The fine-grained nature of unit tests
makes them well-suited for isolating where errors are occurring.
However, unit tests are not useful for verifying that different
sections of code work together.

Integration and end-to-end tests verify that different portions of the
program work together, but are less valuable for immediately isolating exactly where
errors are occurring.

## Tests don't have to be perfect
It is important to note that you don't need to spend energy worrying
about the specifics of test types. When you begin to work on your test
suite, consider what your package does and how you may need to test
parts of it. Being familiar with different test types provides a
framework to help you think about writing tests and how they can
complement each other.

## Next steps

Now that you understand test types, learn how to [write effective tests](write-tests) for your package. Then explore how to [run tests locally](run-tests) and in [continuous integration](tests-ci). Track your
(run-tests) and in [continuous integration](tests-ci). You can also learn about tracking the progress of test coverage using tools like [Code cov](code-cov).
