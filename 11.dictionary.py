# !/usr/bin/Python

# website: http://pythonprogramminglanguage.com/dictionary

'''A dictionary in Python is a one to one mapping.
Every key points to a value, separated by a colon (:).
A dictionary is defined using curly brackets[中括号].
The value left of the colon is called the key,
the value right of the colon is called the value.
Every (key,value) pair is separated by a comma.
Keys must be unique values, you can not use the same key twice.
Values may or may not be unique.'''

dictionary = {'EN':'English', 'CH':'Chinese'}
print(dictionary['CH'])

# Add a key-value
dictionary['FR'] = 'French'
print(dictionary['FR'])
print(dictionary)

# Del a key-value
del dictionary['FR']
print(dictionary)
