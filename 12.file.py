# !/usr/bin/Python

# website: http://pythonprogramminglanguage.com/read-file

'''Python has built in support for reading and writing files.
The function readlines() can be used to read the entire files contents'''

# read file
fileName = 'README.txt'

with open(fileName) as fn:
    content = fn.readlines()

print(content)

# write file
f = open("output-file.txt", "w")
f.write("write file test, \n")
f.write("this is next line.")
f.close()
