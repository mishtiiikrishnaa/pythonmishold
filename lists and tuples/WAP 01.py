#WAP to read a list of numbers, enter a number to search inside the list, if found print the index position
#of number.
lyst=eval(input("a list of numbers: "))
search=int(input("search for? "))
if search in lyst:
    print("position", end= ": ")
    print(lyst.index(search))
else:
    print(search, "not found")
