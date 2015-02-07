'''
Created on Nov 2, 2014

@author: Shathru
'''

memo = {};
def fib(n):
    if n in memo:
        return memo[n];
    if n<=2:
        return 1;
    else:
        memo[n] = fib(n-1) + fib(n-2);
    #memo[n] = f;
    return memo[n];

print("Enter the value of n:\n");
n = int(input());
print(fib(n));
""" print(memo); """ 