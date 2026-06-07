lyst=eval(input("list of numbers: "))
for element in range(len(lyst)):
    if lyst[element]>10:
        lyst[element]=10
print(lyst)