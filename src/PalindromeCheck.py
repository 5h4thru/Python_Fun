n = int(input())
for i in range(n):
    string = input()
    length = len(string)
    a = []
    a.append(string.split())
    b = string.split()
    tr2 = ''.join(e for e in b if e.isalnum())
    print(tr2)
    tr1 = ''.join(e for e in string if e.isalnum())
    print (tr1)
    
    trimmed = ' '.join(e for e in string if e.isalnum())
    if (''.join(string.split()) == ''.join(string[::-1].split())):
        print ("palindrome")
  #  a = []
   # for i in string:
    #    a.append(trimmed.split())
    """ ans = ""
    if length %2 == 0 :
        half = length // 2
        str_half = string[0:half]
        ans =  str_half + str_half[::-1]       
        #print (ans)  
        if(ans <= string):
            str_half = str(int(str_half) + 1)
            ans = str_half + (str_half[0:half])[::-1]
            #print(str_half, ans)
        print(ans)
    else:
        half = length // 2
        str_half = string[0:half]
        ans = str_half + string[half] + str_half[::-1]
        #print(ans)
        if(ans<= string):            
            str_half = str(int(str_half+string[half]) + 1)
            ans = str_half + (str_half[0:half])[::-1]
            #print(str_half, ans)
        print(ans) """