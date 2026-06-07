f=open("test.txt")
h=f.read()
x=h.split()
c,c1=0,0
for i in x:
    if i=="the":
        c+=1
    elif i=="my":
        c1+=1
print("count 'the': ", c)
print("count 'my': ",c1)
f.close()
