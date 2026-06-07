lyst=eval(input("a list: "))
lyst1=[]
for element in lyst:
    if element not in lyst1:
        lyst1.append(element)
print(lyst1)