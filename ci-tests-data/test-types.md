# Different types of tests: Unit, Integration & Functional Tests

There are different types of tests that you want to consider when creating your
test suite:

1. Unit tests
2. Integration
3. Functional (also known as end-to-end) tests

Here you will learn about all three different types of tests.

### Unit Tests

A unit test in Python involves testing individual components or units of code in isolation to ensure that they work correctly. The goal of unit testing is to verify that each part of the software, typically at the function or method level, performs its intended task correctly.

Unit tests can be compared to examining each piece of your puzzle to ensure parts of it are not broken. If all of the pieces of your puzzle don’t fit together, you will never complete it. Similarly, when working with code, tests ensure that each function, attribute, class, method works properly when isolated.

**Unit test example:** Pretend that you have a function that converts a temperature value from Celsius to Fahrenheit. A test for that function might ensure that when provided with a value in Celsius, the function returns the correct value in degrees Fahrenheit. That function is a unit test. It checks a single unit (function) in your code.

```{figure} ../images/python-tests-puzzle.png
:height: 350px
:alt: image of two puzzle pieces with some missing parts. The puzzle pieces are purple teal yellow and blue. The shapes of each piece don’t fit together.

If puzzle pieces have missing ends, they can’t work together with other elements in the puzzle. The same is true with individual functions, methods and classes in your software. The code needs to work both individually and together to perform certain sets of tasks.

```

### Integration tests

Integration tests involve testing how parts of your package work together or integrate. Integration tests can be compared to connecting a bunch of puzzle pieces together to form a whole picture. Integration tests focus on how different pieces of your code fit and work together.

For example, if you had a series of steps that collected temperature data in a spreadsheet, converted it from degrees celsius to Fahrenheit and then provided an average temperature for a particular time period. An integration test would ensure that all parts of that workflow behaved as expected.

```{figure} ../images/python-tests-puzzle-fit.png
:height: 450px
:alt: image of puzzle pieces that all fit together nicely. The puzzle pieces are colorful - purple, green and teal.

Your integration tests should ensure that parts of your code that are expected to work
together, do so as expected.

```

### End-to-end (functional) tests

End-to-end tests (also referred to as functional tests) in Python are like comprehensive checklists for your software. They simulate real user end-to-end workflows to make sure the code base supports real life applications and use-cases from start to finish. These tests help catch issues that might not show up in smaller tests and ensure your entire application or program behaves correctly. Think of them as a way to give your software a final check before it's put into action, making sure it's ready to deliver a smooth experience to its users.

```{note}
For scientific packages, creating short tutorials that highlight core workflows that your package supports, that are run when your documentation is built could also serve as end-to-end tests.
```

### Comparing unit, integration and end-to-end tests

Unit tests, integration tests, and end-to-end tests have complementary advantages and disadvantages. The fine-grained nature of unit tests make them well-suited for isolating where errors are occurring, but not very suitable for verifying that different sections of code work together. Integration and end-to-end tests verify that the different portions of the program work together, but are less well-suited for isolating where errors are occurring. A thorough test suite should have a mixture of unit tests, integration tests, and functional tests.

# Code coverage

Code coverage is the amount of your package's codebase that is run as a part of running your project's tests. A good rule of thumb is to ensure that \*\*every line of

your code is run at least once during testing\**. However, note that good code coverage does not *guarantee\* that your package is well-tested. For example, you may run all of your lines of code, but not account for many edge-cases that users may have. Ultimately, you should think carefully about the way your package will be used, and decide whether your tests adequately cover all of that usage.

A common service for analyzing code coverage is [codecov.io](https://codecov.io/). This project is free for open source tools, and will provide dashboards that tell you how much of your codebase is covered during your tests. We recommend setting up an account, and using codecov to keep track of your code coverage.

```{figure} ../images/code-cov-stravalib.png
:height: 450px
:alt: Screenshot of the code cov service - showing test coverage for the stravalib package. in this image you can see a list of package modules and the associated number of lines and % lines covered by tests. at the top of the image you can see what branch is being evaluated and the path to the repository being shown.

the Code cov platform is a useful tool if you wish to visually track code coverage. Using it you can not only get the same summary information that you can get with pytest-cov extension. You can also get a visual representation of what lines are covered by your tests and what lines are not covered. Code cove is mostly useful for evaluating unit tests and/or how much of your package code is "covered. It however will not evaluate things like integration tests and end-to-end workflows. b

```
