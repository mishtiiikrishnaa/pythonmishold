#practicals q.17
#Write a program to read a list of numbers and search for the number entered by the user
lyst=eval(input("give a number list: "))
search=int(input("give a number to search across the list: "))
if search in lyst:
    print(search, "found at position", lyst.index(search))
else:
    print(search, "not found")
