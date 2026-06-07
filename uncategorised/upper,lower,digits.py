#to find upper, lower, digits
string=input("string: ")
u,l,d=0,0,0
for ch in string:
    if ch.isupper():
        u+=1
    elif ch.islower():
        l+=1
    elif ch.isdigit():
        d+=1
print(u,l,d)
