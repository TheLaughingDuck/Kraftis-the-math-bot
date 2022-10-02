# Load package
The package (math_package) should be structured such that it can be loaded with the following command:

from math_package import *

# Functions
The "main" calculator function is main.evaluate(). It takes a string representing some computations and returns the result after calculation.

# Formating
main.evaluate() accepts functions, written with lower-case letters, they can only take one input which must be captured by parentheses (Ex "sin(3)"). The input itself can be a series of operations, (Ex "sin(1+1)"). The current allowed functions are:
* sin()

There are plans for the calculator to be able to interpret variables (for some interval), but currently the variable handling is just a "dormant" part of the package.