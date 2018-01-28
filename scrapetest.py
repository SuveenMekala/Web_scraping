#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 20:10:01 2018

@author: Suveen
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()

# html.parser is the HTML parser included in the standard Python 3 library.
# information on other HTML parsers is here:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
count = 0
com_sum = 0
numlist= list()
for tag in tags:
    # Look at the parts of a tag
    count= count+1
    str_tag= str(tag)
#    print('TAg : ',tag)
#    print('String', str_tag)
    stuff=re.findall('[0-9]+',str_tag)
    
    for k in range(len(stuff)):
        num = float(stuff[k])
        com_sum = com_sum+ num
#    print (num)
        numlist.append(num)
#print(numlist)
    
print('Count ',count)
print('Sum ', int(com_sum))