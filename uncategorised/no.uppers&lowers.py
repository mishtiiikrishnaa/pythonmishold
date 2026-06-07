string=input("somestring: ")
u=l=0
for ch in string:
    if ch.isupper():
        u+=1
    elif ch.islower():
        l+=1
print(u,l)
