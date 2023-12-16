# Code coverage

Code coverage is the amount of your package's codebase that is run as a part of running your project's tests. A good rule of thumb is to ensure that every line of your code is run at least once during testing. However, note that good code coverage does not guarantee that your package is well-tested. For example, you may run all of your lines of code, but not account for many edge-cases that users may have. Ultimately, you should think carefully about the way your package will be used, and decide whether your tests adequately cover all of that usage.

Some common services for analyzing code coverage are [codecov.io](https://codecov.io/) and [coveralls.io](https://coveralls.io/). These projects are free for open source tools, and will provide dashboards that tell you how much of your codebase is covered during your tests. We recommend setting up an account (on either CodeCov or Coveralls), and using it to keep track of your code coverage.

```{figure} ../images/code-cov-stravalib.png
:height: 450px
:alt: Screenshot of the code cov service - showing test coverage for the stravalib package. in this image you can see a list of package modules and the associated number of lines and % lines covered by tests. at the top of the image you can see what branch is being evaluated and the path to the repository being shown.

The CodeCov platform is a useful tool if you wish to visually track code coverage. Using it you can not only get the same summary information that you can get with **pytest-cov** extension. You can also get a visual representation of what lines are covered by your tests and what lines are not covered. Code coverage is mostly useful for evaluating unit tests and/or how much of your package code is "covered". It however will not evaluate things like integration tests and end-to-end workflows.

```
