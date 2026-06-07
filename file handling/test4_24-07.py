f=open("test.txt")
h=f.read()
x=h.split()
m,e=0,0
for i in x:
    if i[0]=="M" or i[0]=="m":
        m+=1
    elif i[-1]=="e":
        e+=1
print("no of words starting with M or m:", m)
print("no of words ending with e: ", e)
