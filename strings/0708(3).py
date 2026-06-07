#individual character printing-reverse and normal
string=input("enter word of choice: ")
rev=0
for norm in range(-1,(-len(string)-1),-1):
    print(string[rev], "\t", string[norm])
    rev+=1
