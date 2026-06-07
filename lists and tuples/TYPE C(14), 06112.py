#page 369, q(14)
lyst=eval(input("give a list: "))
lyst1=[]
lyst2=[]
for element in lyst:
    if element not in lyst1:
        lyst1.append(element)
    elif element in lyst1:
        lyst2.append(element)
print(lyst1+lyst2)
