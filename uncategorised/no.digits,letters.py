string=input("somestring: ")
d=a=0
for ch in string:
    if ch.isdigit():
        d+=1
    elif ch.isalpha():
        a+=1
print(d,a)