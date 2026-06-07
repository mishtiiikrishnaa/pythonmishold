sq=int(input("number: "))
if sq**(1/2) == 2 or 3 or 5 or 7:
    print("prime")
elif sq**(1/2)<0:
    print("no")
else:
    if sq**(1/2)%2==0 or sq*(1/2)%3==0 or sq**(1/2)%5==0 or sq**(1/2)%7==0:
        print("not prime")
    else:
        print("prime")