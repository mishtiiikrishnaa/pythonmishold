lyst=eval(input("list of elements: "))
lyst1=[]
lyst1.append(lyst[-1])
for e in range(0,len(lyst)-1):
    lyst1.append(lyst[e])
print(lyst1)