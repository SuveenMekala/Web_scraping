import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter the url: ')
    
print('Retrieving:', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)


count = 0
for element in tree.iter('comment'):
    count+=1

comments = tree.findall('comments/comment')
name_count=0
num_count=0

for i in range(count):
   
    name = comments[i].find('name').text
    name_count+=1
    num=comments[i].find('count').text
    num_count+=int(num)
    
print('Count: ',name_count)
print('Sum: ',num_count)  