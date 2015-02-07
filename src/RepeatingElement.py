def repeatingElement(a):
    result = a[0]
    for i in range(1,len(a)):
        result = result ^ a[i]
        print (result)

repeatingElement([1,2,3,4,5,5,6,7,8])