f=open("test.txt")
h=f.read()
x=h.split()
c=0
for i in x:
    if i=="at":
        c+=1
print(c)
