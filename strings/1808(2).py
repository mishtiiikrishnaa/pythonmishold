##program 2, page 321
string=input("input a string: ")
vow="aeiou"
newstring=" "
for cno in string:
    if cno in vow:
        string=string.replace(cno,"*")
newstring+=string
print(newstring)
        
    
