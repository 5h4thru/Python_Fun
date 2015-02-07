'''
Created on Nov 6, 2014

@author: Shathru
'''
result = 0
def count(S, m, n):
    if n==0:
        return 1;
    elif n<0:
        return 0;
    elif n>0 and m<=0:
        return 0;
    result1 = count(S, m-1, n)
    result2 = count(S, m, n-S[m-1])
    res = result1+result2
    return res
S = [1, 2, 3, 4];
#S = [1,2]
m = len(S);
n = 4
print(count(S, m, n));
