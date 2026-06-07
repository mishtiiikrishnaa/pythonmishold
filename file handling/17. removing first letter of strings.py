lyst=eval(input("a list of strings: "))
for string in range(len(lyst)):
    lyst[string]=lyst[string].lstrip(lyst[string][0])
print(lyst)