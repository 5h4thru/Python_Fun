'''
Created on Nov 13, 2014

@author: Shathru
'''
"""
def groupSum(index, array, target):
    #After exhausting all the cases, the only possible solution will be if target equals to 0
    if(index>=len(array)):
        return (target==0)
    
    #There will be two cases
    
    #1) Consider that the array[index] is used to form the target
    #2) The array[index] will not be used to form the target
    
    
    #array[index] is being used to form the target in this case
    if(groupSum(index+1, array, target-array[index])):
        return True
    
    #array[index] is NOT being used to form the target in this case
    if(groupSum(index+1, array, target)):
        return True
    
    #If no possible combination of the array can be used to form the target, we will return False
    #because there is no solution
    return False

print(groupSum(0, [2,4,8], 10))
print(groupSum(0, [2,4,8], 12))
print(groupSum(0, [2,4,8], 14))
print(groupSum(0, [2,4,8], 2))
print(groupSum(0, [2,4,8], 4))
print(groupSum(0, [2,4,8], 9))
"""
"""
#splitArray
def splitArray(a):
    return helperSA(0, a, 0, 0)

def helperSA(i,a,s1,s2):
    if(i>=len(a)):
        return (s1==s2)
    if(helperSA(i+1, a, s1+a[i], s2)):
        return True
    if(helperSA(i+1, a, s1, s2+a[i])):
        return True
    return False

print(splitArray([1,1]))
print(splitArray([5,2,3]))
print(splitArray([1,1,1,1,1,1]))
print(splitArray([5,2,2]))
print(splitArray([5,3,2]))
print(splitArray([2,2,10,10,1,1]))
"""
"""
#splitOddSum
def splitOddSum(a):
    return helperOS(0,a,0,0)

def helperOS(i,a,s1,s2):
    if(i>=len(a)):
        #return (s1==s2)
        return (s1%10==0 and s2%2==1)
    if(helperOS(i+1, a, s1+a[i], s2)):
        return True
    if(helperOS(i+1, a, s1, s2+a[i])):
        return True
    return False

print(splitOddSum([5,5,5,2]))
print(splitOddSum([5,5,6]))
print(splitOddSum([5,5,6,1]))
print(splitOddSum([6,5,5,1]))
print(splitOddSum([6,5,5,1,10]))
print(splitOddSum([10,7,5,5,1]))
"""

"""
#split53
def split53(a):
    return helper(0,a,0,0)

def helper(i,a,s1,s2):
    if(i>=len(a)):
        return (s1==s2)
    if(a[i]%5==0):
        return helper(i+1, a, s1+a[i], s2)
    if(a[i]%3==0):
        return helper(i+1, a, s1, s2+a[i])
    return (helper(i+1, a, s1+a[i], s2) or helper(i+1, a, s1, s2+a[i]))
    
print(split53([1,1]))
print(split53([1,1,1]))
print(split53([2,4,2]))
print(split53([2,2,2,1]))
print(split53([3,5,8]))
print(split53([2,4,6]))
"""
