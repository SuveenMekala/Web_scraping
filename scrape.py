#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 14:08:46 2018

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
count= input('Enter count: ')
p = input('Enter position: ')
print('Retrieving: ',url)
count=int(count)
for i in range(count):
    
    html = urlopen(url, context=ctx).read()

    soup = BeautifulSoup(html, "html.parser")   

# Retrieve all of the anchor tags
    tags = soup('a')
    index = 0
    for tag in tags:
    
        index= index + 1
        if (index==int(p)):
            str_tag=str(tag)
            url= tag.get('href',None)
            print('Retrieving: ',url)
            target_name=re.findall('>([A-Z][a-z]+)',str_tag)
print(target_name[0])
        


