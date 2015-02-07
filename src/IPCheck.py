t = input()
start = []
end = []
check = []
a = []

def isCheck(start, end, check):
    print(type(check))
    print(type('0.0.0.0'))
    if check < int('0.0.0.0'):
        print ("ASSA")
#     pass
for i in range(0,int(t)):
    temp = input()
    a.append(temp.split())
    
print (len(a))
for i in range(0,int(t)):
    print(a[i][0],a[i][1],a[i][2])
    print(a[i][0].split())
    isCheck(int(a[i][0]),int(a[i][1]),int(a[i][2]))