# Run tests on Continuous Integration

continuous integration is... [learn more here](ci).

Running your [test suite locally](run-tests) is useful as you develop code and also test new features or changes to the code base. However, you also will want to setup Continuous Integration (CI) to run your tests online. CI allows you to run all of your tests in the cloud. While you may only be able to run tests locally on a specific operating system that you run, in CI you can specify tests to run both on various versions of Python and across different operating systems.

CI can also be triggered for pull requests and pushes to your repository. This means that every pull request that you, your maintainer team or a contributor submit, can be tested. In the end CI testing ensures your code continues to run as expected even as changes are made to the code base. [Read more about CI here. ](https://docs.google.com/document/d/1jmo2l5u02c_F1zZi0bAIYXeJ6HiIryJbXzsNbMQQX6o/edit#heading=h.3mx2na93o7bf)

## CI & pull requests

CI is invaluable if you have outside people contributing to your software.
You can setup CI to run on all pull requests submitted to your repository.
CI can make your repository more friendly to new potential contributors.
It allows users to contribute code, documentation fixes and more without
having to create development environments, run tests and build documentation
locally.
