# Test Types for Python packages

## Three types of tests: Unit, Integration & Functional Tests

There are different types of tests that you want to consider when creating your
test suite:

1. Unit tests
2. Integration
3. End-to-end (also known as Functional) tests

Each type of test has a different purpose. Here, you will learn about all three types of tests.

```{todo}
I think this page would be stronger if we did have some
examples from our package here: https://github.com/pyOpenSci/pyosPackage

```

## Unit Tests

A unit test involves testing individual components or units of code in isolation to ensure that they work correctly. The goal of unit testing is to verify that each part of the software, typically at the function or method level, performs its intended task correctly.

Unit tests can be compared to examining each piece of your puzzle to ensure parts of it are not broken. If all of the pieces of your puzzle don’t fit together, you will never complete it. Similarly, when working with code, tests ensure that each function, attribute, class, method works properly when isolated.

**Unit test example:** Pretend that you have a function that converts a temperature value from Celsius to Fahrenheit. A test for that function might ensure that when provided with a value in Celsius, the function returns the correct value in degrees Fahrenheit. That function is a unit test. It checks a single unit (function) in your code.

```python
# Example package function
def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.

    Parameters:
        celsius (float): Temperature in Celsius.

    Returns:
        float: Temperature in Fahrenheit.
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
```

Example unit test for the above function. You'd run this test using the `pytest` command in your **tests/** directory.

```python
import pytest
from temperature_converter import celsius_to_fahrenheit

def test_celsius_to_fahrenheit():
    """
    Test the celsius_to_fahrenheit function.
    """
    # Test with freezing point of water
    assert pytest.approx(celsius_to_fahrenheit(0), abs=0.01) == 32.0

    # Test with boiling point of water
    assert pytest.approx(celsius_to_fahrenheit(100), abs=0.01) == 212.0

    # Test with a negative temperature
    assert pytest.approx(celsius_to_fahrenheit(-40), abs=0.01) == -40.0

```

```{figure} ../images/pyopensci-puzzle-pieces-tests.png
:height: 300px
:alt: image of puzzle pieces that all fit together nicely. The puzzle pieces are colorful - purple, green and teal.

Your unit tests should ensure each part of your code works as expected on its own.
```

## Integration tests

Integration tests involve testing how parts of your package work together or integrate. Integration tests can be compared to connecting a bunch of puzzle pieces together to form a whole picture. Integration tests focus on how different pieces of your code fit and work together.

For example, if you had a series of steps that collected temperature data in a spreadsheet, converted it from degrees celsius to Fahrenheit and then provided an average temperature for a particular time period. An integration test would ensure that all parts of that workflow behaved as expected.

```python

def fahr_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.

    Parameters:
        fahrenheit (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature in Celsius.
    """
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Function to calculate the mean temperature for each year and the final mean
def calc_annual_mean(df):
    # TODO: make this a bit more robust so we can write integration test examples??
    # Calculate the mean temperature for each year
    yearly_means = df.groupby('Year').mean()

    # Calculate the final mean temperature across all years
    final_mean = yearly_means.mean()

    # Return a converted value
    return fahr_to_celsius(yearly_means), fahr_to_celsius(final_mean)

```

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

End-to-end tests (also referred to as functional tests) in Python are like comprehensive checklists for your software. They simulate real user end-to-end workflows to make sure the code base supports real life applications and use-cases from start to finish. These tests help catch issues that might not show up in smaller tests and ensure your entire application or program behaves correctly. Think of them as a way to give your software a final check before it's put into action, making sure it's ready to deliver a smooth experience to its users.

```{figure} ../images/flower-puzzle-pyopensci.jpg
:height: 450px
:alt: Image of a completed puzzle showing a daisy

End-to-end or functional tests represent an entire workflow that you
expect your package to support.

```

End-to-end test also test how a program runs from start to finish. A tutorial that you add to your documentation that runs in CI in an isolated environment is another example of an end-to-end test.

```{note}
For scientific packages, creating short tutorials that highlight core workflows that your package supports, that are run when your documentation is built could also serve as end-to-end tests.
```

## Comparing unit, integration and end-to-end tests

Unit tests, integration tests, and end-to-end tests have complementary advantages and disadvantages. The fine-grained nature of unit tests make them well-suited for isolating where errors are occurring. However, unit tests are not useful for verifying that different sections of code work together.

Integration and end-to-end tests verify that the different portions of the program work together, but are less well-suited for isolating where errors are occurring. For example, when you refactor your code, it is possible that that your end-to-end tests will
break. But if the refactor didn't introduce new behavior to your existing
code, then you can rely on your unit tests to continue to pass, testing the
original functionality of your code.

It is important to note that you don't need to spend energy worrying about
the specifics surrounding the different types of tests. When you begin to
work on your test suite, consider what your package does and how you
may need to test parts of your package. Bring familiar with the different types of tests can provides a framework to
help you think about writing tests and how different types of tests can complement each other.
