enter=input("enter a string: ")
print(list(enter))
lyst=enter.split()
print(lyst)
ve,v=[],0
CS,C=[],0
for word in lyst:
    if word[-1] in "aeiouAEIOU":
        ve.append(word)
        v+=1
    if word[0].isupper():
        CS.append(word)
        C+=1
print(ve,"word count: ",v)
print(CS,"word count: ",C)