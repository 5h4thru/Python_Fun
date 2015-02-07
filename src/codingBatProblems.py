'''
Created on Nov 8, 2014

@author: Shathru
From the website: http://codingbat.com/java/Recursion-1
Basic String operations:
a="hello" 
print(a[-2:]) #prints "lo"
print(a[1:]) #prints "ello"
print(a[:-2]) #prints "hel"
'''

"""
#Count7
def count7(n1):
    n = int(n1)
    if(n==0):
        return 0
    if(n%10==7):
        return 1+count7(n/10)
    return count7(n/10)

print(count7(717))
print(count7(7))
print(count7(123))
print(count7(771237))
print(count7(77777))
print(count7(70711758))
print(count7(47571))
"""

"""
#changePi
def changePi(a):
    if(a=="" or len(a)<2):
        return a
    if(a[0:2]=="pi"):
        return "3.14"+changePi(a[2:])
    return(a[0]+changePi(a[1:]))
    
print(changePi("xpix"))
print(changePi("pipi"))
print(changePi("pi"))
print(changePi("hip"))
print(changePi("p"))
print(changePi(""))
"""

"""
#noX
def noX(a):
    if(len(a)==0):
        return a
    if(a[0]=="x"):
        return noX(a[1:])
    return a[0]+noX(a[1:])

print(noX("xaxb"))
print(noX("abc"))
print(noX("xx"))
"""
"""
#array6
def array6(a,i):
    if(len(a)==0):
        return False
    if(i>=len(a)):
        return False
    if(a[i]==6):
        return True
    return(array6(a, i+1))

print(array6([1,6,4], 0))
print(array6([1,4], 0))
print(array6([4,6], 0))
print(array6([1,2,6], 0))
print(array6([6,6,6], 0))
print(array6([], 0))
"""
"""
#array11
def array11(a,i):
    if(len(a)==0):
        return 0
    if(i>=len(a)):
        return 0
    if(a[i]==11):
        return 1+array11(a, i+1)
    return 0+array11(a, i+1)

print(array11([1,2,11],0))
print(array11([11,11],0))
print(array11([1,2,3,4],0))
print(array11([1,11,3,11],0))
print(array11([],0))
print(array11([11,2,3,4,11,5],0))
"""
"""
#array220
def array220(a,i):
    if(len(a)==0):
        return False
    if(i>=len(a)-1):
        return False
    if(a[i]*10==a[i+1]):
        return True
    print(str(a[i])+" "+str(a[i]*10)+" "+str(a[i+1]))
    return array220(a, i+1)

print(array220([1,2,20], 0))
print(array220([3,30], 0))
print(array220([3], 0))
print(array220([], 0))
print(array220([20,2,21,210], 0))
print(array220([0,0], 0))
"""
"""
#allStar
def allStar(a):
    if(len(a)<=1):
        return a
    return a[0]+"*"+allStar(a[1:])

print(allStar("abc"))
print(allStar("hello"))
print(allStar("ab"))
print(allStar("a"))
print(allStar(""))
print(allStar("3.14"))
"""
"""
#pairStar
def pairStar(a):
    if(len(a)<=1):
        return a
    if(a[0]==a[1]):
        #return a[0]+"*"+a[1]+pairStar(a[2:])
        return a[0]+"*"+pairStar(a[1:])
    return a[0]+pairStar(a[1:])

print(pairStar("hello"))
print(pairStar("aaaa"))
print(pairStar("xxyy"))
print(pairStar("aa"))
"""
"""
#endX
def endX(a):
    if(len(a)<=1):
        return a
    if(a[0]=="x"):
        return endX(a[1:])+endX(a[0])
    return a[0]+endX(a[1:])

print(endX("xxre"))
print(endX("xxhixx"))
print(endX("xhixhix"))
print(endX(""))
print(endX("x"))
"""
"""
#countPairs
def countPairs(a):
    if(len(a)<=2):
        return 0
    if(a[0]==a[2]):
        return 1+countPairs(a[1:])
    return 0+countPairs(a[1:])

print(countPairs("axa"))
print(countPairs("axax"))
print(countPairs("axbx"))
print(countPairs(""))
print(countPairs("xxx"))
print(countPairs("abcd"))
print(countPairs("xaXaxa"))
"""
"""
#countAbc
def countAbc(a):
    if(len(a)<=2):
        return 0
    if(a[0:3]=="abc" or a[0:3]=="aba"):
        return 1+countAbc(a[1:])
    return 0+countAbc(a[1:])

print(countAbc("abcxxabc"))
print(countAbc("xabc"))
print(countAbc("aaabc"))
print(countAbc(""))
print(countAbc("ab"))
print(countAbc("aba"))
"""
"""
#stringClean
def stringClean(a):
    if(len(a)<=1):
        return a
    if(a[0]==a[1]):
        return stringClean(a[1:])
    return a[0]+stringClean(a[1:])

print(stringClean("xxxx"))
print(stringClean("axxscc"))
print(stringClean("aabbccdd"))
print(stringClean(""))
print(stringClean("abcd"))
print(stringClean("ababab"))
print(stringClean("addaa"))
"""
"""
#strCount
def strCount(a,sub):
    if not sub in a:
        return 0
    if(a[0:len(sub)]==sub):
        return 1+strCount(a[len(sub):], sub)
    return strCount(a[1:],sub)

print(strCount("catcowcat", "cat"))
print(strCount("cowcowcow", "cow"))
print(strCount("catcowcat", "dog"))
print(strCount("cacatcowcat", "cat"))
print(strCount("xyx", "x"))
print(strCount("iiiijj", "ii"))
print(strCount("iiiijj", "iii"))
"""
"""
#strCopies
def strCopies(a,sub,n):
    if(n==0):
        return  True
    if(len(a)<len(sub)):
        return False
    if(a[0:len(sub)]==sub):
        return strCopies(a[1:],sub,n-1)
    return strCopies(a[1:], sub, n)

print(strCopies("catcowcat", "cat", 2))
print(strCopies("catcowcat", "cow", 2))
print(strCopies("catcowcat", "cow", 1))
print(strCopies("iiiijj", "ii", 4))
print(strCopies("iiijj", "ii", 2))
print(strCopies("dogcatdog", "cat", 1))
print(strCopies("dogcatdog", "dog", 2))
"""
"""
#parenBit
def parenBit(a):
    if(a[0]=="("):
        #return parenBit(a[0:str(a).index(")")])
        return a[0:a.index(")")+1]
    return parenBit(a[1:])

print(parenBit("xyz(xxx)123"))
print(parenBit("xyz(Zcxxx)23"))
print(parenBit("()"))
print(parenBit("xyz hel afsd {} [(])"))
"""