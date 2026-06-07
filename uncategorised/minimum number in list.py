lyst=eval(input("enter a number list: "))
lyst1=lyst[:]
L=len(lyst)
for i in range(L):
    for j in range(L-i-1):
        if lyst[j]>lyst[j+1]:
            lyst[j],lyst[j+1]=lyst[j+1],lyst[j]
print("minimum number in list: ",lyst[0],"at position", lyst1.index(lyst[0]))
