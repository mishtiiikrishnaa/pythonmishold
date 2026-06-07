#WAP using lists to find the index position of the number entered by user.
L=[1,2,3,4,5,6,6,7,8,9,9,10]
un=int(input("give a number: "))
if un in L:
    print(L.index(un))
else:
    print("unfound")

