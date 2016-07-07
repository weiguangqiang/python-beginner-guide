# !/usr/bin/Python

# website: http://pythonprogramminglanguage.com/date-and-time/

'''To get the date or time in Python we need to use the standard time module.'''

import time

ticks = time.time()
print('ticks: ', ticks, '\n')

localTime = time.localtime()
print('local time: ', localTime, '\n')

timeNow = time.localtime(time.time())
print('timeNow: ', timeNow, '\n')

timeNowFormat = time.asctime(time.localtime(time.time()))
print('timeNowFormat: ', timeNowFormat, '\n')

functionNames = dir(time)
print('name: ', functionNames)
