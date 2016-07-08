# !/usr/bin/python

import sys

print('Arguments: ', len(sys.argv))
print('List: ', str(sys.argv))

if len(sys.argv) < 2:
    print('To few Arguments, please specify a filename')

filename = sys.argv[0]
print('FileName: ', filename)
