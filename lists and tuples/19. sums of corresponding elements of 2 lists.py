L=eval(input("enter a list: "))
M=eval(input("enter another list: "))
lyst=[]
for element in range(len(M)):
    lyst.append(L[element]+M[element])
print(lyst)