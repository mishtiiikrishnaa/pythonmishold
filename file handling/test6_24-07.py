f=open("test.txt")
h=f.readlines()
t=0
for i in h:
    if i[0]=="T":
        t+=1
print("no of lines: ", t)
