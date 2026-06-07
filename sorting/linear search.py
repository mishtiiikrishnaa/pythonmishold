#Write a program to read a list of numbers and search for the number entered by the user.
lyst=eval(input("enter a number list: "))
search=int(input("search for? "))
if search in lyst:
    print("position of", search, lyst.index(search))
else:
    print(search, "not found")