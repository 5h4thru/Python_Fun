'''
Created on Nov 6, 2014

@author: Shathru
'''
strArr=[0]*10
strArr[0]="1"
for i in range(0,3):
    if strArr[i]=="1":
        strArr[i]="0"
        strArr[i+1]="1"
        print(str(i)+str(strArr))
    elif strArr[i]=="0":
        strArr[i]="1"
        strArr[i+1]="0"
    #print(strArr)
#print(strArr)