'''
Created on Nov 5, 2014

@author: Shathru
'''
a = [10,20,30]
#x = [[0]*len(a) for x in range(2**len(a))]

x = [0]*(2**len(a))
#print(len(x))
print(x)
res = 0
check = 10
count = 0
"""
for i in range(0,len(x)):
    for j in range (0,len(x[i])):
        x[i][j]=bin(count)
        count=count+1
        #res = res + x[i]*a[i];
        #print(x[i])
    #print()
print(x)
"""

for i in range(0,2**len(a)):
    x[i]=count
    count=count+1
    binVal = (bin(x[i])[2:].zfill(len(a)))
    print("New value:")
    print(binVal)
    print("Separated values:")
    lenB = len(binVal)
    intBinVal = int (binVal)
    #for j in range(0,lenB):
        #print(binVal[lenB-1])
        #lenB = lenB-1
    while(intBinVal!=0):
        print(intBinVal%10)
        inBinVal = intBinVal/10
        #print(binVal)
        """ for j in range(0,len(a)):
             while(binVal!=0):
                 temp = (int)(binVal)%10
                 binVal = binVal/10
                # print(temp)
         """
        