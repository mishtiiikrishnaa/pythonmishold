#WAP to find the greatest and smallest in a given list (menu driven).
lyst=eval(input("list of numbers: "))
menu=print('''1. smallest in given list
2. greatest in given list''')
choice=int(input("1/2? "))
greatest=0
smallest=0
for num in range(len(lyst)):
    if lyst[num]>lyst[num-1]:
        greatest=lyst[num]
    elif lyst[num]<lyst[num-1]:
        smallest=lyst[num-1]
if choice==2:
    print("greatest:", greatest)
elif choice==1:
    print("smallest: ", smallest)
