string=input("give a string: ")
if string[-3:]=="ing":
    print(string[0:-3]+"ly")
elif len(string)<3:
    print(string)
elif string[-3:]!="ing":
    print(string[0:-3]+"ing")

