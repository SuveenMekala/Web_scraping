#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 13:09:09 2018

@author: Suveen
"""

import json
import urllib.request, urllib.parse, urllib.error

url = input('Enter the url: ')
    
print('Retrieving:', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

info = json.loads(data)

print('User count:', len(info))

comments= info['comments']

c_count =0
sum_count=0

for item in comments:
#    print('Name', item['name'])
    c_count+=1
#    print('Count', item['count'])
    sum_count+=item['count']

print('Count: ',c_count)
print('Sum: ',sum_count)
 
    
    