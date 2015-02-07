'''
Created on Sep 12, 2014

@author: Shathru
'''
res = 0

#SPOJ mixtures
def helper(a):
    return a[0]*a[1]

def minSmoke(a):
    if(len(a)==1):
        return a[0]
    #if(len(a)==2):
    #   return (a[0]+a[1])%100
    res = 0 + helper(a)
    a[1] = (a[0]+a[1])%100
    return minSmoke(a[1:])
    return res
    

    
print(minSmoke([40,60,20]))
print(minSmoke([60,20,40]))
"""print(minSmoke([18,19]))
print(minSmoke([2,3,4,5,6]))
print(minSmoke([10,20,30]))
"""