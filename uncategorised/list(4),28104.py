x=eval(input("character list: "))
v,c=0,0
for i in x:
    if i in "AEIOUaeiou":
        v+=1
    else:
        c+=1
print("vowels ", v)
print("consonants ", c)
