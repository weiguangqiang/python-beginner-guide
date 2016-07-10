# !/usr/bin/Python

# website: http://pythonprogramminglanguage.com/download-file

'''
We can download data using the urllib2 module.. These examples work with both http,
https and for any type of files including text and image.
'''

'''
The urllib2 module has been split across several modules in Python 3.0 named urllib.request and urllib.error.
The 2to3 tool will automatically adapt imports when converting your sources to 3
'''
from urllib.request import urlopen # it's for Python 3

response = urlopen("https://wordpress.org/plugins/about/readme.txt")
data = response.read()
# print(data)

filename = "download.txt"
file_ = open(filename, 'wb') # Python 3
file_.write(data)
file_.close()

img_response = urlopen("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Python_logo_and_wordmark.svg/260px-Python_logo_and_wordmark.svg.png")
imgdata = img_response.read()
imgname = "download_img.png"
img_ = open(imgname, 'wb') # Python 3
img_.write(imgdata)
img_.close()
