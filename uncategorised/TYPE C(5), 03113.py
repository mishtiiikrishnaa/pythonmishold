#page 370, q(5)
lyst=eval(input("enter a list of strings: "))
for string in range(len(lyst)):
    lyst[string]=lyst[string].lstrip(lyst[string][0])
print(lyst)
