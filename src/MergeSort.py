'''
Created on Nov 3, 2014

@author: Shathru
'''



def merge(l,r,a):
    i=j=k=0
    nL=len(l);nR=len(r)
    while(i<nL and j<nR):
        if(l[i]<r[j]):
            a[k]=l[i]
            i=i+1
        else:
            a[k]=r[j]
            j=j+1
        k=k+1
    while(i<nL):
        a[k]=l[i]
        i=i+1; k=k+1
    while(j<nR):
        a[k]=r[j]
        j=j+1; k=k+1
    return a

def customMergeSort(a):
    n=len(a)
    if(n<2):
        return a
    mid=(int)(n/2)
    l=a[0:mid]
    r=a[mid:]
    customMergeSort(l)
    customMergeSort(r)
    return merge(l, r, a)

    
a=customMergeSort([2,4,1,6,8,5,3,7])
print(a)