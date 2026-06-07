f=open("test.txt")
h=f.read()
v=0
for i in h:
    if i in "AEIOUaeiou":
        v+=1
print("no. of vowels in file: ", v)
    
