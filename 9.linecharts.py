# !/usr/bin/Python

# website: http://pythonprogramminglanguage.com/line-charts

'''In the first two lines we include the numpy and matplotlib library.
This contains logical functions to create line charts amongst others.
We define a list named x with a few random numbers and we set the x and y label.
Finally we call the function show() which will display the line chart.
If you do not call the show() function, nothing will be shown on the screen.'''

# It depends on python-matplotlib
import numbers as np
import matplotlib.pyplot as plt

x = [2,3,4,5,7,9,13,15,17,20]

plt.plot(x)
plt.ylabel('Y')
plt.xlabel('X')
plt.show()
