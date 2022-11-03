# assegnamento4
Module: basic Python
Assignment #4 (October 7, 2021)


--- Goal
Create a ProbabilityDensityFunction class that is capable of throwing
preudo-random number with an arbitrary distribution.

(In practice, start with something easy, like a triangular distribution---the
initial debug will be easier if you know exactly what to expect.)


--- Specifications
- the signature of the constructor should be __init__(self, x, y), where
  x and y are two numpy arrays sampling the pdf on a grid of values, that
  you will use to build a spline
- [optional] add more arguments to the constructor to control the creation
  of the spline (e.g., its order)
- the class should be able to evaluate itself on a generic point or array of
  points
- the class should be able to calculate the probability for the random
  variable to be included in a generic interval
- the class should be able to throw random numbers according to the distribution
  that it represents
- [optional] how many random numbers do you have to throw to hit the
  numerical inaccuracy of your generator?



  ######################## assegnamento1 #############################
  Module: advanced Python
  Assignment #1 (October 21, 2019)


  Clean up your ProbabilityDensityFunction class and create a fully-fledged
  Python package.

  --- Goal

  Create a splrand Python package to generate univariate random numbers according
  to a given distribution using splines.

  The layout of the package should be (hopefully the names should be
  self-explaining):

  splrand
  --- splrand/splrand
  ------ splrand/splrand/__init__.py
  ------ splrand/splrand/core.py
  ------ splrand/splrand/version.py
  --- splrand/docs
  ------ splrand/docs/Makefile
  ------ splrand/docs/api.rst
  ------ splrand/docs/conf.py
  ------ splrand/docs/index.rst
  ------ splrand/docs/make.bat
  ------ splrand/docs/release_notes.rst
  --- splrand/tests
  ------ splrand/tests/test_core.py
  --- .travis.yml
  --- LICENSE X
  --- README.md X
  --- requirements.txt X


  --- Specifications
  - the package should have adequate unit tests
  - the package should have continuus integration
  - the package should have adequate documentation
  - the documentation should be on readthedocs
  - [optional] add a rudimentary release manager to automate the tagging process
