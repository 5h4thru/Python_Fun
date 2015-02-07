import re
#check = "myth";
#string = "Greek mythology is the body of myths and teachings that belong to the ancient Greeks, concerning their gods and heroes, the nature of the world, and the origins and significance of their own cult and ritual practices. It was a part of the religion in ancient Greece. Modern scholars refer to and study the myths in an attempt to throw light on the religious and political institutions of Ancient Greece and its civilization, and to gain understanding of the nature of myth itself.";
check = "air"
string = "An airline is a company that provides air transport services for traveling passengers and freight. Airlines lease or own their aircraft with which to supply these services and may form partnerships or alliances with other airlines for mutual benefit. Generally, airline companies are recognized with an air operating certificate or license issued by a governmental aviation body. Claire is a good friend of mine too."

string = (re.sub("[^A-Za-z]", " ", string))
hashMap = {}
word = string.split();
countMyth = 0
countStarts = 0
firstOccurence = len(string)
for i in range (0,len(word)):
    val = hashMap.get(word[i])
    if val == None:
        hashMap[i] = word[i]
    if ((hashMap.get(i)).lower()==check.lower()):
        countMyth = countMyth + 1
    if ((hashMap.get(i).lower()).startswith(check.lower())):
        if(i<firstOccurence):
            firstOccurence = i
        countStarts = countStarts + 1
        
print (str(countMyth)+";" +str(countStarts)+";"+str(hashMap.get(firstOccurence)))