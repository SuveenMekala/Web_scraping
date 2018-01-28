import re

hand = open('regex_sum_62479.txt')

numlist= list()

for line in hand:
     line= line.rstrip()
     stuff=re.findall('[0-9]+',line)
#     print(len(stuff))

     for k in range(len(stuff)):
        num = float(stuff[k])
#        print (num)
        numlist.append(num)
     
#print (numlist)
print (sum(numlist))
