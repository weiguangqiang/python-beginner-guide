# !/usr/bin/python

# website: http://pythonprogramminglanguage.com/functions

import math

# the 'def' keyword defines a funtion in Python
def pythagoras(a, b):
    value = math.sqrt(a*a + b*b)
    print("value: ", value)

# invoke the functions
pythagoras(3, 4)
