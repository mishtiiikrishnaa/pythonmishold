#WAP to create a list of integers that are prime nos as long as the user wants
pn=[]
while True:
    pno=int(input("prime no: "))
    if pno%2!=0 and pno%5!=0 and pno%3!=0 and pno%7!=0:
        pn.append(pno)
    elif str(pno) in "2357":
        pn.append(pno)
    else:
        print("given isnt a prime number")
    inp=input("d'u wanna enter more? y/n: ")
    if inp=="y":
        True
    else:
        break
print(pn)
