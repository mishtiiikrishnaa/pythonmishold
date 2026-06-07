vc=0
string=input("some string: ")
for ch in string:
    if ch in "AEIOU":
        vc+=1
    elif ch in "aeiou":
        vc+=1
print(vc)
