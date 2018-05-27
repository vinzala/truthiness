#!/usr/bin/python

# A simple demonstration of why the use of " import * " should be avoided.

# Each of the following import statements will result in
#  different interpretations of 'True' and 'False' by the python interpreter.

from reality import *
#from reality import maintain


if True:
    print(':)')
else:
    print(':(')
