[![Build Status](https://travis-ci.org/dfarrell07/CBenchF.svg?branch=master)](https://travis-ci.org/dfarrell07/CBenchF)

## CBenchF

SDN Controller Benchmark Framework

**This project is very new, under early development. It is not ready for use!**

Note: There are a number of TODOs external to CBenchF that need to be knocked out before CBenchF can continue (for example, Dockerizing OpenDaylight). I'm working on those TODOs in the context of the ODL Integration Team. Don't take a lack of commits here as a lack of progress. ;)

### Overview

This project aims to bring some sanity to the SDN controller performance testing landscape by providing a well architected framework for such tests.

Performance tests for controllers are typically one-off scripts written by unconnected developers. They are not shared, documented or tested. They don't enable code reuse. They aren't easy to find (many are emailed dev to dev). They don't support multiple controllers.

By providing a framework with a base set of tests, support for multiple SDN controllers, reusable code for working with northbound and southbound devices, a standard results format, stats/graphing tools and support for publishing results to a central location, we hope to dramatically advance the state of SDN controller performance testing.

See the [Architecture](https://github.com/dfarrell07/CBenchF/wiki/Architecture), [Tests](https://github.com/dfarrell07/CBenchF/wiki/Tests) and [Requirements](https://github.com/dfarrell07/CBenchF/wiki/Requirements) wiki pages for more information.

### Running Tests

The project uses Tox to run unit tests with various Python interpreters, confirm that Sphinx-gen'd docs build and test that the code conforms to PEP8 style. To kick off all tests, simply issue the `tox` command in the project's root. Note that Tox automatically builds and brings down virtual environments, installing required dependences as it does.

```
[~/perf]$ tox
<snip>
  py27: commands succeeded
  py33: commands succeeded
  pypy: commands succeeded
  docs: commands succeeded
  pep8: commands succeeded
  congratulations :)
```

To run a specific set of tests in a virtual environment, use `tox -e<name of tests>`. For example, `tox -epep8` to run PEP8 style checks or `tox -epy27` to run unit tests with a Python 2.7 interpreter.

### Contributing

Contributions are encouraged! At this point, I think most contributions would come as feature requests and use case examples. Please add those to the [Requirements](https://github.com/dfarrell07/CBenchF/wiki/Requirements) wiki page. If the feature requests are very narrowly scoped they may also be suitable for an [Issue](https://github.com/dfarrell07/CBenchF/issues).

### Contact

For feature requests, bug reports and questions please raise an [Issue](https://github.com/dfarrell07/CBenchF/issues). Daniel Farrell is the primary developer of this tool. He can be contacted directly at dfarrell@redhat.com or on IRC (dfarrell07 on Freenode). **Prefer public, documented communication like Issues over direct 1-1 communication. This is an Open Source project. Keep the community in the loop.**
