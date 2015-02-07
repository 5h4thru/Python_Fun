'''
Created on Sep 15, 2014

@author: Shathru
Given a sorted array (sorted in non-decreasing order) of positive numbers,
find the smallest positive integer value that cannot be represented as sum of elements of any subset of given set. 
Expected time complexity is O(n).
'''
arr = [1, 3, 6, 10, 11, 15]
res = 1
for i in arr:
    if res >= i:
        res += res
        print (res)
        
print ("The smallest number that cannot be represented as sum of elements in the given array is " + str(res))