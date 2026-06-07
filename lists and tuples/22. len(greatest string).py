lyst=eval(input("lyst: "))
lystlen=[]
for element in lyst:
    lystlen.append(len(element))
lystlen.sort(reverse=True)
print(lystlen[0])