#page 452, 13.1
lyst=eval(input("original list: "))
L=len(lyst)
for i in range(0,L):
    for j in range(0,L-i-1): #decreases the checking to last before value
        if lyst[j]>lyst[j+1]:
            lyst[j],lyst[j+1]=lyst[j+1],lyst[j]
print("sorted list: ",lyst)
    
