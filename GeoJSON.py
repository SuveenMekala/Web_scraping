#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 13:48:10 2018

@author: Suveen
"""

import urllib.request, urllib.parse, urllib.error
import json

# Note that Google is increasingly requiring keys
# for this API
serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'


address = input('Enter location: ')
url = serviceurl + urllib.parse.urlencode({'address': address})

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

#print(data)
js= json.loads(data)

#print(json.dumps(js, indent=4))


placeID = js['results'][0]['place_id']

print('Place id ',placeID)
