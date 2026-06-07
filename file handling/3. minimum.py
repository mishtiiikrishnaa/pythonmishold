lyst=eval(input("lyst: "))
mini=0
for element in range(1,len(lyst)):
    if lyst[element]<lyst[element-1]:
        mini=lyst[element]
    elif lyst[element]>lyst[element-1]:
        mini=lyst[element-1]
print(mini)
print(lyst.index(mini))