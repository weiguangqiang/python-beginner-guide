# !/usr/bin/Python

# website: http://pythonprogramminglanguage.com/randon-numbers/

import random

# Simply call the random() method to generate a real (float) number between 0 and 1.
x = random.random()
print(x)

# use the randint() method to generate a whole number.
y = random.randint(1, 60)
print(y)

# generate a list of 20 random numbers
list = []

for i in range(0, 20):
    z = random.randint(1, 9)
    list.append(z)

print(list)

# get 5 random items from a list
m = random.sample(list, 2)
print(m)
