#WAP to find the greatest and smallest in a given list (menu driven).
lyst=eval(input("list of numbers: "))
menu=print('''1. smallest in list
2. greatest in given list''')
choice=int(input("1/2? "))
lyst.sort()
if choice==1:
    print("smallest in list: ", lyst[0])
elif choice==2:
    print("greatest in list: ", lyst[-1])
else:
    print("enter a valid number!")
