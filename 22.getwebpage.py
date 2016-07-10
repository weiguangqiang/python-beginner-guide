# !/usr/bin/Python

# website: http://pythonprogramminglanguage.com/get-links-from-webpage

'''
The module urllib2 can be used to download webpage data.
Webpage data is always formatted in HTML format.
To cope with the HTML format data, we use a Python module named BeautifulSoup.
'''

# The below code is about to get links from Webpage

from BeautifulSoup import BeautifulSoup
import urllib2
import re

html_page = urllib2.urlopen("http://www.google.com") # download the webpage data
soup = BeautifulSoup(html_page) # load the webpage data into BeautifulSoup
link = []
for link in soup.findAll('a'):
    links.append(link.get('href'))

print(links)
