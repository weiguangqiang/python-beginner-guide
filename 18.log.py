# !/usr/bin/Python

# website: http://pythonprogramminglanguage.com/logging

'''We can log a process in our program using the module logging.'''

import logging

logging.warning('Warning Log')

'''Levels of severity
There are several levels of severity: DEBUG, INFO, WARNING, ERROR, CRITICAL.
You can configure a minimum level of severity, if it’s lower than the set level it’s ignored.'''
logging.basicConfig(level = logging.WARNING)
logging.debug('Debug Log')
logging.info('Info Log')
logging.error('Error Log')
