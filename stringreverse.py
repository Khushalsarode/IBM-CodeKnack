strings = 'Hello World'

string=strings.split()
reversed=[]
string1=""
for i in string:
    nr = i[::-1]
    reversed.append(nr)
    
for words in reversed:
    string1+=words+" "
    print(string1.strip())
    
    
