lyst=eval(input("enter a number list: "))
L=len(lyst)
for i in range(L):
    for j in range(L-i-1):
        if lyst[j]>lyst[j+1]:
            lyst[j],lyst[j+1]=lyst[j+1],lyst[j]
print("second largest number in list: ", lyst[-2])
