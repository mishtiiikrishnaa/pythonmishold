#page 366 q(9)
lyst=eval(input("enter a list: "))
for element in range(2,len(lyst)):
    lyst[element],lyst[-1*(element+1)]=lyst[-1*(element+1)],lyst[element]
print(lyst)
