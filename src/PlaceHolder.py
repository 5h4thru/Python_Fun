'''
Created on Sep 16, 2014

@author: Shathru
'''
def wordsOfString(a):
    return a.split()

#print (wordsOfString("This is a string!"))
required_list = wordsOfString("This is a string!")
for i in required_list:
    print(i)
    
def insertionSort(a):
    # Let i run from index 1 to length of the array
    for i in range(1,len(a)):
        # Let j keep track of elements just before i
        j = i-1
        # Temporarily store the value of a[i]. This will be used to restore the value back to the array
        val = a[i]
        while (j>=0 and a[j]>val):
            # Paste the larger number to the ith position and decrement j by 1. Upon exiting the loop the temporary value will be stored to jth position
            a[j+1] = a[j]
            j = j-1
        a[j+1] = val
        #a[i] = val
    return a

def bubbleSort(a):
    """ Ideally compares the adjacent elements in the array and pushes the largest of the two to the right side.
    This way, the largest element goes to the end of the array """
    moreSwap = True
    while moreSwap:
        moreSwap = False
        for i in range (0,len(a)-1):
            if (a[i] > a[i+1]):
                moreSwap = True
                print (a[i])
                a[i] = a[i] ^ a[i+1]
                a[i+1] = a[i] ^ a[i+1]
                a[i] = a[i] ^ a[i+1]
    return a

print("Bubble sort: %s" % str((bubbleSort([1,3,4,2,5,8,6]))))
print("Insertion sort: %s" % str(insertionSort([1,4,9,3,6,7,8,2,3,1])))
