'''
Created on Sep 15, 2014

@author: Shathru

'''
array = [10, 5, 3, 4, 4, 3, 5, 6]
#array = [6, 10, 5, 4, 9, 120, 4, 6, 10, 5]
res = len(array)
hashMap = {}
for i in range(0,len(array)):
    index = hashMap.get(array[i])
    if index == None:
        hashMap[array[i]] = i
    else:
        print ("The first element that is repeating is " + str(array[index]))
        break