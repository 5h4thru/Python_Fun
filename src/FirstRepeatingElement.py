'''
Created on Sep 15, 2014

@author: Shathru

'''
array = [10, 5, 31, 14, 13, 15, 5]
#array = [6, 10, 5, 4, 9, 120, 4, 6, 10, 5]
res = len(array)
hashMap = {}
for i in range(0,len(array)):
    index = hashMap.get(array[i])
    if index == None:
        hashMap[array[i]] = i
    elif index < res:
        res = index
if res != len(array):
    print ("The first repeating element is " + str(array[res]))
else:
    print ("There is no repeating element in the array")