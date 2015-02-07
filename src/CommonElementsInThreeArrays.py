'''
Created on Sep 18, 2014

@author: Shathru
'''
from operator import contains
a = [1,2,3,4,5,6,7,8,9,10]
b = [2,4,6,8,10]
c = [3,6,9,12,15,18]

keys = []
hashMap = {}
def commonElements(a,b,c):
    alen = len(a) 
    blen = len(b)
    clen = len(c)
    x = 0
    y = 0
    z = 0
    while(x<alen and y<blen and z<clen):
        print(a[x],b[y],c[z])
        if a[x]==b[y] and a[x]==c[z]:
            keys.append(a[x])
            x+=1
            y+=1
            z+=1
        elif a[x]<b[y]:
            x += 1
        elif b[y]<c[z]:
            y += 1
        else:
            z += 1
    return keys
print(commonElements(a, b, c))