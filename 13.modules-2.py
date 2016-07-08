# !/usr/bin/Python

# website: http://pythonprogramminglanguage.com/modules

'''Find available functions and variables in a Python module
To find the available functions in a module, you can use the below code'''

import math

content = dir(math)
print(content)
